#!/usr/bin/env python3
"""
Process raw data into experiment-ready format.

Copyright Saxon Nicholls 2026 MIT Licence

Run after download_all.py. Produces cleaned, aligned datasets in data/processed/
"""

import zipfile
import io
from pathlib import Path

import numpy as np
import pandas as pd

RAW_DIR = Path(__file__).parent / "raw"
PROC_DIR = Path(__file__).parent / "processed"
PROC_DIR.mkdir(exist_ok=True)


# ────────────────────────────────────────────────────────────
# 1. Fama-French
# ────────────────────────────────────────────────────────────

def parse_ff_zip(zippath: Path, skip_footer: int = 0) -> pd.DataFrame:
    """Parse a Fama-French CSV inside a zip file."""
    with zipfile.ZipFile(zippath) as zf:
        # Find the CSV inside (usually one file)
        csv_names = [n for n in zf.namelist() if n.endswith(".CSV") or n.endswith(".csv")]
        if not csv_names:
            raise ValueError(f"No CSV found in {zippath}")
        with zf.open(csv_names[0]) as f:
            content = f.read().decode("utf-8", errors="replace")

    # FF files have header text before the data — find the first numeric line
    lines = content.split("\n")
    data_start = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped and stripped[0].isdigit() and len(stripped) > 6:
            data_start = i
            break

    # Find end of first data block (blank line or non-numeric)
    data_end = data_start
    for i in range(data_start + 1, len(lines)):
        stripped = lines[i].strip()
        if not stripped or (not stripped[0].isdigit() and stripped[0] != '-'):
            data_end = i
            break
    else:
        data_end = len(lines)

    # Parse the data block
    data_text = "\n".join(lines[data_start:data_end])
    df = pd.read_csv(io.StringIO(data_text), header=None)

    return df


def process_ff():
    """Process Fama-French data into clean parquet files."""
    print("\n=== Processing Fama-French data ===")
    ff_dir = RAW_DIR / "fama_french"

    # FF25 daily
    zippath = ff_dir / "25_Portfolios_5x5_Daily_CSV.zip"
    if zippath.exists():
        try:
            df = parse_ff_zip(zippath)
            # First column is date (YYYYMMDD), rest are portfolio returns
            df.columns = ["date"] + [f"p{i}" for i in range(1, df.shape[1])]
            df["date"] = pd.to_datetime(df["date"].astype(str), format="%Y%m%d", errors="coerce")
            df = df.dropna(subset=["date"])
            df = df.set_index("date")
            # Convert from percentage to decimal
            df = df / 100.0
            df.to_parquet(PROC_DIR / "ff25_daily_returns.parquet")
            print(f"  ff25_daily: {df.shape} ({df.index[0].date()} to {df.index[-1].date()})")
        except Exception as e:
            print(f"  ff25_daily: FAILED ({e})")

    # FF5 factors daily
    zippath = ff_dir / "F-F_Research_Data_5_Factors_2x3_daily_CSV.zip"
    if zippath.exists():
        try:
            df = parse_ff_zip(zippath)
            df.columns = ["date", "Mkt-RF", "SMB", "HML", "RMW", "CMA", "RF"]
            df["date"] = pd.to_datetime(df["date"].astype(str), format="%Y%m%d", errors="coerce")
            df = df.dropna(subset=["date"])
            df = df.set_index("date")
            df = df / 100.0
            df.to_parquet(PROC_DIR / "ff5_factors_daily.parquet")
            print(f"  ff5_factors_daily: {df.shape}")
        except Exception as e:
            print(f"  ff5_factors_daily: FAILED ({e})")

    # FF25 monthly
    zippath = ff_dir / "25_Portfolios_5x5_CSV.zip"
    if zippath.exists():
        try:
            df = parse_ff_zip(zippath)
            df.columns = ["date"] + [f"p{i}" for i in range(1, df.shape[1])]
            df["date"] = pd.to_datetime(df["date"].astype(str) + "01", format="%Y%m%d", errors="coerce")
            df = df.dropna(subset=["date"])
            df = df.set_index("date")
            df = df / 100.0
            df.to_parquet(PROC_DIR / "ff25_monthly_returns.parquet")
            print(f"  ff25_monthly: {df.shape}")
        except Exception as e:
            print(f"  ff25_monthly: FAILED ({e})")


# ────────────────────────────────────────────────────────────
# 2. S&P 500 prices → returns
# ────────────────────────────────────────────────────────────

def process_sp500():
    """Convert S&P 500 prices to daily returns."""
    print("\n=== Processing S&P 500 data ===")
    prices_file = RAW_DIR / "sp500" / "sp500_daily_prices.parquet"
    if not prices_file.exists():
        print("  SKIP: prices not downloaded")
        return

    prices = pd.read_parquet(prices_file)

    # Simple returns (price relatives)
    returns = prices.pct_change().dropna(how="all")

    # Drop columns with >20% missing
    missing_frac = returns.isna().mean()
    good_cols = missing_frac[missing_frac < 0.20].index
    returns = returns[good_cols].dropna()

    returns.to_parquet(PROC_DIR / "sp500_daily_returns.parquet")
    print(f"  sp500_daily_returns: {returns.shape} "
          f"({returns.index[0].date()} to {returns.index[-1].date()})")

    # Also save log-returns (for Kelly/growth calculations)
    log_returns = np.log1p(returns)
    log_returns.to_parquet(PROC_DIR / "sp500_daily_log_returns.parquet")
    print(f"  sp500_daily_log_returns: {log_returns.shape}")

    # Price relatives (1 + r) for universal portfolio calculations
    price_relatives = 1.0 + returns
    price_relatives.to_parquet(PROC_DIR / "sp500_daily_price_relatives.parquet")
    print(f"  sp500_daily_price_relatives: {price_relatives.shape}")


# ────────────────────────────────────────────────────────────
# 3. Treasury yield curve
# ────────────────────────────────────────────────────────────

def process_yields():
    """Combine Treasury yields into a yield curve panel."""
    print("\n=== Processing Treasury yield curve ===")
    fred_dir = RAW_DIR / "fred"

    maturities = {
        "DGS1MO": 1/12, "DGS3MO": 3/12, "DGS6MO": 6/12,
        "DGS1": 1, "DGS2": 2, "DGS3": 3, "DGS5": 5,
        "DGS7": 7, "DGS10": 10, "DGS20": 20, "DGS30": 30,
    }

    dfs = {}
    for series_id, tau in maturities.items():
        fpath = fred_dir / f"{series_id}.csv"
        if fpath.exists():
            try:
                df = pd.read_csv(fpath, parse_dates=[0], index_col=0)
                df.columns = [f"y_{tau}"]
                # FRED uses "." for missing
                df = df.replace(".", np.nan).astype(float)
                dfs[f"y_{tau}"] = df.iloc[:, 0]
            except Exception:
                pass

    if dfs:
        yields = pd.DataFrame(dfs)
        yields = yields.dropna(how="all")
        yields.to_parquet(PROC_DIR / "treasury_yield_curve.parquet")
        print(f"  treasury_yield_curve: {yields.shape} "
              f"({yields.index[0]} to {yields.index[-1]})")
    else:
        print("  SKIP: no yield data found")


# ────────────────────────────────────────────────────────────
# 4. Sovereign spreads (for EMU case study)
# ────────────────────────────────────────────────────────────

def process_sovereign():
    """Compute sovereign yield spreads over Germany."""
    print("\n=== Processing sovereign yield data ===")
    fred_dir = RAW_DIR / "fred"

    countries = {
        "IRLTLT01DEM156N": "DE",
        "IRLTLT01FRM156N": "FR",
        "IRLTLT01ITM156N": "IT",
        "IRLTLT01ESM156N": "ES",
        "IRLTLT01GRM156N": "GR",
    }

    dfs = {}
    for series_id, country in countries.items():
        fpath = fred_dir / f"{series_id}.csv"
        if fpath.exists():
            try:
                df = pd.read_csv(fpath, parse_dates=[0], index_col=0)
                df = df.replace(".", np.nan).astype(float)
                dfs[country] = df.iloc[:, 0]
            except Exception:
                pass

    if dfs and "DE" in dfs:
        yields = pd.DataFrame(dfs).dropna(how="all")
        spreads = yields.subtract(yields["DE"], axis=0)
        spreads.to_parquet(PROC_DIR / "sovereign_spreads_over_de.parquet")
        print(f"  sovereign_spreads: {spreads.shape}")
    else:
        print("  SKIP: sovereign data not found")


# ────────────────────────────────────────────────────────────
# 5. VIX
# ────────────────────────────────────────────────────────────

def process_vix():
    """Process VIX data."""
    print("\n=== Processing VIX data ===")
    fpath = RAW_DIR / "fred" / "VIXCLS.csv"
    if fpath.exists():
        try:
            df = pd.read_csv(fpath, parse_dates=[0], index_col=0)
            df = df.replace(".", np.nan).astype(float)
            df.columns = ["VIX"]
            df.to_parquet(PROC_DIR / "vix_daily.parquet")
            print(f"  vix_daily: {df.shape}")
        except Exception as e:
            print(f"  FAILED: {e}")
    else:
        print("  SKIP: VIX data not downloaded")


# ────────────────────────────────────────────────────────────
# 6. Crypto returns
# ────────────────────────────────────────────────────────────

def process_crypto():
    """Convert crypto prices to returns."""
    print("\n=== Processing cryptocurrency data ===")
    fpath = RAW_DIR / "crypto" / "crypto_daily.parquet"
    if fpath.exists():
        prices = pd.read_parquet(fpath)
        returns = prices.pct_change().dropna(how="all")
        returns.to_parquet(PROC_DIR / "crypto_daily_returns.parquet")
        print(f"  crypto_daily_returns: {returns.shape}")
    else:
        print("  SKIP: crypto data not downloaded")


# ────────────────────────────────────────────────────────────
# 7. Sector ETF returns
# ────────────────────────────────────────────────────────────

def process_sectors():
    """Convert sector ETF prices to returns."""
    print("\n=== Processing sector ETF data ===")
    fpath = RAW_DIR / "sector_etfs" / "sector_etfs_daily.parquet"
    if fpath.exists():
        prices = pd.read_parquet(fpath)
        returns = prices.pct_change().dropna(how="all")
        returns.to_parquet(PROC_DIR / "sector_etf_daily_returns.parquet")
        print(f"  sector_etf_daily_returns: {returns.shape}")
    else:
        print("  SKIP: sector ETF data not downloaded")


# ────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────

def main():
    print("=" * 60)
    print("  The Geometry of Efficient Markets — Data Processing")
    print("=" * 60)

    process_ff()
    process_sp500()
    process_yields()
    process_sovereign()
    process_vix()
    process_crypto()
    process_sectors()

    # Summary
    print("\n" + "=" * 60)
    print("  Processed files:")
    for f in sorted(PROC_DIR.glob("*.parquet")):
        size_kb = f.stat().st_size / 1024
        print(f"    {f.name} ({size_kb:.0f} KB)")
    print("=" * 60)
    print("  Ready for experiments. Run code/experiments/ scripts next.")


if __name__ == "__main__":
    main()
