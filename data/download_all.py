#!/usr/bin/env python3
"""
Download all data required for the 20 empirical tests in
REAL_DATA_EXPERIMENTS.md

Copyright Saxon Nicholls 2026 MIT Licence

Usage:
    python download_all.py [--end-date 2024-12-31] [--fred-key YOUR_KEY]

All sources are free. FRED requires a free API key from:
    https://fred.stlouisfed.org/docs/api/api_key.html
"""

import os
import sys
import argparse
import zipfile
import io
from pathlib import Path
from datetime import datetime

import pandas as pd
import requests

RAW_DIR = Path(__file__).parent / "raw"
RAW_DIR.mkdir(exist_ok=True)


# ────────────────────────────────────────────────────────────
# 1. Fama-French data (direct HTTP from Ken French's website)
# ────────────────────────────────────────────────────────────

FF_BASE = "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp"

FF_FILES = {
    # name: (zip filename, csv name inside zip, description)
    "ff25_daily": (
        "25_Portfolios_5x5_Daily_CSV.zip",
        "25 Portfolios Formed on Size and Book-to-Market (5 x 5)",
        "Fama-French 25 size/value portfolios, daily returns"
    ),
    "ff5_factors_daily": (
        "F-F_Research_Data_5_Factors_2x3_daily_CSV.zip",
        "F-F Research Data 5 Factors 2x3",
        "Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA), daily"
    ),
    "ff100_daily": (
        "100_Portfolios_10x10_Daily_CSV.zip",
        "100 Portfolios Formed on Size and Book-to-Market (10 x 10)",
        "Fama-French 100 size/value portfolios, daily returns"
    ),
    "ff25_monthly": (
        "25_Portfolios_5x5_CSV.zip",
        "25 Portfolios Formed on Size and Book-to-Market (5 x 5)",
        "Fama-French 25 size/value portfolios, monthly returns"
    ),
    "ff5_factors_monthly": (
        "F-F_Research_Data_5_Factors_2x3_CSV.zip",
        "F-F Research Data 5 Factors 2x3",
        "Fama-French 5 factors, monthly"
    ),
}


def download_ff(end_date: str):
    """Download Fama-French datasets from Ken French's website."""
    print("\n=== Downloading Fama-French data ===")
    ff_dir = RAW_DIR / "fama_french"
    ff_dir.mkdir(exist_ok=True)

    for name, (zipname, _, desc) in FF_FILES.items():
        url = f"{FF_BASE}/{zipname}"
        outpath = ff_dir / zipname
        if outpath.exists():
            print(f"  SKIP {name} (already exists)")
            continue
        print(f"  Downloading {name}: {desc}")
        try:
            resp = requests.get(url, timeout=60)
            resp.raise_for_status()
            outpath.write_bytes(resp.content)
            print(f"    -> {outpath} ({len(resp.content) / 1024:.0f} KB)")
        except Exception as e:
            print(f"    FAILED: {e}")


# ────────────────────────────────────────────────────────────
# 2. S&P 500 constituents via yfinance
# ────────────────────────────────────────────────────────────

# Current S&P 500 tickers (as of 2024) — we fetch from Wikipedia
SP500_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


def download_sp500(end_date: str):
    """Download S&P 500 daily prices via yfinance."""
    print("\n=== Downloading S&P 500 constituent prices ===")
    sp_dir = RAW_DIR / "sp500"
    sp_dir.mkdir(exist_ok=True)

    # Get ticker list from Wikipedia
    ticker_file = sp_dir / "tickers.csv"
    if not ticker_file.exists():
        print("  Fetching S&P 500 ticker list from Wikipedia...")
        try:
            tables = pd.read_html(SP500_URL)
            tickers = tables[0]["Symbol"].str.replace(".", "-", regex=False).tolist()
            pd.Series(tickers).to_csv(ticker_file, index=False, header=["ticker"])
            print(f"    -> {len(tickers)} tickers saved")
        except Exception as e:
            print(f"    FAILED to fetch tickers: {e}")
            # Fallback: use a minimal set for testing
            tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META",
                       "BRK-B", "JPM", "V", "JNJ", "WMT", "PG", "XOM",
                       "UNH", "MA", "HD", "BAC", "PFE", "ABBV", "KO",
                       "PEP", "MRK", "COST", "TMO", "AVGO", "CSCO",
                       "ACN", "MCD", "ABT", "DHR", "LIN", "ADBE"]
            pd.Series(tickers).to_csv(ticker_file, index=False, header=["ticker"])
    else:
        tickers = pd.read_csv(ticker_file)["ticker"].tolist()

    # Download prices in batches
    prices_file = sp_dir / "sp500_daily_prices.parquet"
    if prices_file.exists():
        print(f"  SKIP prices (already exists at {prices_file})")
        return

    try:
        import yfinance as yf
        print(f"  Downloading {len(tickers)} stocks from Yahoo Finance...")
        print(f"  Date range: 2000-01-01 to {end_date}")
        print(f"  This may take several minutes...")

        # Download in chunks to avoid timeouts
        chunk_size = 50
        all_data = []
        for i in range(0, len(tickers), chunk_size):
            chunk = tickers[i:i + chunk_size]
            print(f"    Batch {i // chunk_size + 1}/{(len(tickers) - 1) // chunk_size + 1}: "
                  f"{chunk[0]}...{chunk[-1]}")
            try:
                data = yf.download(
                    chunk, start="2000-01-01", end=end_date,
                    auto_adjust=True, progress=False
                )
                if "Close" in data.columns.get_level_values(0):
                    closes = data["Close"]
                else:
                    closes = data
                all_data.append(closes)
            except Exception as e:
                print(f"      Batch failed: {e}")

        if all_data:
            prices = pd.concat(all_data, axis=1)
            prices = prices.loc[:, ~prices.columns.duplicated()]
            prices.to_parquet(prices_file)
            print(f"    -> {prices.shape} saved to {prices_file}")
        else:
            print("    FAILED: no data downloaded")

    except ImportError:
        print("  SKIP: yfinance not installed (pip install yfinance)")


# ────────────────────────────────────────────────────────────
# 3. FRED data (Treasury yields, VIX, macro)
# ────────────────────────────────────────────────────────────

FRED_SERIES = {
    # Treasury yields
    "DGS1MO": "1-month Treasury yield",
    "DGS3MO": "3-month Treasury yield",
    "DGS6MO": "6-month Treasury yield",
    "DGS1": "1-year Treasury yield",
    "DGS2": "2-year Treasury yield",
    "DGS3": "3-year Treasury yield",
    "DGS5": "5-year Treasury yield",
    "DGS7": "7-year Treasury yield",
    "DGS10": "10-year Treasury yield",
    "DGS20": "20-year Treasury yield",
    "DGS30": "30-year Treasury yield",

    # Fed funds
    "DFF": "Effective federal funds rate",

    # Volatility indices
    "VIXCLS": "CBOE VIX (daily close)",

    # Sovereign yields (for EMU case study)
    "IRLTLT01DEM156N": "Germany 10Y yield",
    "IRLTLT01FRM156N": "France 10Y yield",
    "IRLTLT01ITM156N": "Italy 10Y yield",
    "IRLTLT01ESM156N": "Spain 10Y yield",
    "IRLTLT01GRM156N": "Greece 10Y yield",

    # CPI components (for inflation paper)
    "CPIAUCSL": "CPI All Items",
    "CPIENGSL": "CPI Energy",
    "CPIFABSL": "CPI Food",
    "CUSR0000SAH1": "CPI Shelter",
    "CUSR0000SAM2": "CPI Medical",
    "CUSR0000SAT1": "CPI Transportation",
}


def download_fred(end_date: str, api_key: str = None):
    """Download FRED series."""
    print("\n=== Downloading FRED data ===")
    fred_dir = RAW_DIR / "fred"
    fred_dir.mkdir(exist_ok=True)

    if api_key is None:
        api_key = os.environ.get("FRED_API_KEY")

    if api_key is None:
        print("  WARNING: No FRED API key. Set FRED_API_KEY environment variable")
        print("  or pass --fred-key. Get a free key at:")
        print("  https://fred.stlouisfed.org/docs/api/api_key.html")
        print("  Attempting download without API (using CSV fallback)...")

        # Fallback: download CSV directly from FRED (no API key needed for some)
        for series_id, desc in FRED_SERIES.items():
            outpath = fred_dir / f"{series_id}.csv"
            if outpath.exists():
                print(f"  SKIP {series_id}")
                continue
            url = (f"https://fred.stlouisfed.org/graph/fredgraph.csv"
                   f"?id={series_id}&cosd=1990-01-01&coed={end_date}")
            try:
                resp = requests.get(url, timeout=30)
                resp.raise_for_status()
                outpath.write_text(resp.text)
                lines = resp.text.count("\n")
                print(f"  {series_id}: {desc} ({lines} rows)")
            except Exception as e:
                print(f"  {series_id}: FAILED ({e})")
        return

    # Use fredapi if available and key is set
    try:
        from fredapi import Fred
        fred = Fred(api_key=api_key)
        for series_id, desc in FRED_SERIES.items():
            outpath = fred_dir / f"{series_id}.csv"
            if outpath.exists():
                print(f"  SKIP {series_id}")
                continue
            try:
                data = fred.get_series(series_id,
                                       observation_start="1990-01-01",
                                       observation_end=end_date)
                data.to_csv(outpath)
                print(f"  {series_id}: {desc} ({len(data)} obs)")
            except Exception as e:
                print(f"  {series_id}: FAILED ({e})")
    except ImportError:
        print("  fredapi not installed, using CSV fallback")
        download_fred(end_date, api_key=None)


# ────────────────────────────────────────────────────────────
# 4. Cryptocurrency data
# ────────────────────────────────────────────────────────────

CRYPTO_TICKERS = ["BTC-USD", "ETH-USD", "SOL-USD", "DOGE-USD"]


def download_crypto(end_date: str):
    """Download cryptocurrency daily prices via yfinance."""
    print("\n=== Downloading cryptocurrency data ===")
    crypto_dir = RAW_DIR / "crypto"
    crypto_dir.mkdir(exist_ok=True)

    outpath = crypto_dir / "crypto_daily.parquet"
    if outpath.exists():
        print(f"  SKIP (already exists)")
        return

    try:
        import yfinance as yf
        print(f"  Downloading {CRYPTO_TICKERS}...")
        data = yf.download(
            CRYPTO_TICKERS, start="2015-01-01", end=end_date,
            auto_adjust=True, progress=False
        )
        if "Close" in data.columns.get_level_values(0):
            closes = data["Close"]
        else:
            closes = data
        closes.to_parquet(outpath)
        print(f"    -> {closes.shape} saved")
    except ImportError:
        print("  SKIP: yfinance not installed")
    except Exception as e:
        print(f"  FAILED: {e}")


# ────────────────────────────────────────────────────────────
# 5. S&P 500 sector ETFs (for Cheeger constant / crisis test)
# ────────────────────────────────────────────────────────────

SECTOR_ETFS = [
    "XLK",  # Technology
    "XLF",  # Financials
    "XLV",  # Health Care
    "XLY",  # Consumer Discretionary
    "XLP",  # Consumer Staples
    "XLE",  # Energy
    "XLI",  # Industrials
    "XLU",  # Utilities
    "XLB",  # Materials
    "XLRE", # Real Estate
    "XLC",  # Communication Services
]


def download_sector_etfs(end_date: str):
    """Download S&P 500 sector ETF prices."""
    print("\n=== Downloading sector ETF data ===")
    etf_dir = RAW_DIR / "sector_etfs"
    etf_dir.mkdir(exist_ok=True)

    outpath = etf_dir / "sector_etfs_daily.parquet"
    if outpath.exists():
        print(f"  SKIP (already exists)")
        return

    try:
        import yfinance as yf
        print(f"  Downloading {len(SECTOR_ETFS)} sector ETFs...")
        data = yf.download(
            SECTOR_ETFS, start="1999-01-01", end=end_date,
            auto_adjust=True, progress=False
        )
        if "Close" in data.columns.get_level_values(0):
            closes = data["Close"]
        else:
            closes = data
        closes.to_parquet(outpath)
        print(f"    -> {closes.shape} saved")
    except ImportError:
        print("  SKIP: yfinance not installed")
    except Exception as e:
        print(f"  FAILED: {e}")


# ────────────────────────────────────────────────────────────
# Main
# ────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Download all data for The Geometry of Efficient Markets"
    )
    parser.add_argument(
        "--end-date", default="2024-12-31",
        help="End date for data download (YYYY-MM-DD)"
    )
    parser.add_argument(
        "--fred-key", default=None,
        help="FRED API key (or set FRED_API_KEY env var)"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("  The Geometry of Efficient Markets — Data Download")
    print(f"  End date: {args.end_date}")
    print("=" * 60)

    download_ff(args.end_date)
    download_sp500(args.end_date)
    download_fred(args.end_date, args.fred_key)
    download_crypto(args.end_date)
    download_sector_etfs(args.end_date)

    print("\n" + "=" * 60)
    print("  Download complete. Run process_all.py next.")
    print("=" * 60)


if __name__ == "__main__":
    main()
