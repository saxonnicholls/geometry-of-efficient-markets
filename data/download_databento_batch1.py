#!/usr/bin/env python3
"""
Databento Batch 1: Daily bars for futures and equities.
Estimated cost: ~$0.08 (well within $125 free credit)

Copyright Saxon Nicholls 2026 MIT Licence
"""

import os
import sys
from pathlib import Path

RAW_DIR = Path(__file__).parent / "raw" / "databento"
RAW_DIR.mkdir(parents=True, exist_ok=True)
PROC_DIR = Path(__file__).parent / "processed"
PROC_DIR.mkdir(exist_ok=True)


def load_key():
    env_path = Path(__file__).parent.parent / ".env"
    for line in open(env_path):
        if line.startswith("DATABENTO_API_KEY="):
            return line.split("=", 1)[1].strip()
    return os.environ.get("DATABENTO_API_KEY")


def main():
    import databento as db
    import pandas as pd

    key = load_key()
    if not key:
        print("ERROR: No Databento API key")
        sys.exit(1)

    client = db.Historical(key)

    # ── Batch 1a: CME futures daily bars ─────────────────────
    print("=" * 60)
    print("  Batch 1a: CME Futures Daily OHLCV (2010-2024)")
    print("=" * 60)

    futures_path = RAW_DIR / "futures_daily_ohlcv.dbn.zst"
    if not futures_path.exists():
        print("  Downloading ES, CL, ZN, ZB, ZF, ZT, GC, SI, NG...")
        try:
            data = client.timeseries.get_range(
                dataset="GLBX.MDP3",
                schema="ohlcv-1d",
                symbols=["ES.FUT", "CL.FUT", "ZN.FUT", "ZB.FUT",
                          "ZF.FUT", "ZT.FUT", "GC.FUT", "SI.FUT", "NG.FUT"],
                start="2010-01-01",
                end="2024-12-31",
            )
            data.to_file(str(futures_path))
            print(f"  Saved to {futures_path}")

            # Convert to parquet for easy use
            df = data.to_df()
            df.to_parquet(RAW_DIR / "futures_daily_ohlcv.parquet")
            print(f"  Also saved as parquet: {df.shape}")
        except Exception as e:
            print(f"  FAILED: {e}")
    else:
        print(f"  SKIP: already exists")

    # ── Batch 1b: Top 50 equities daily bars ─────────────────
    print("\n" + "=" * 60)
    print("  Batch 1b: NASDAQ Top 50 Equities Daily OHLCV (2018-2024)")
    print("=" * 60)

    equities_path = RAW_DIR / "equities_daily_ohlcv.dbn.zst"
    if not equities_path.exists():
        symbols = [
            "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA",
            "BRK.B", "JPM", "V", "JNJ", "WMT", "PG", "XOM", "UNH",
            "MA", "HD", "BAC", "PFE", "ABBV", "KO", "PEP", "MRK",
            "COST", "TMO", "AVGO", "CSCO", "ACN", "MCD", "ABT",
            "DHR", "LIN", "ADBE", "CRM", "NFLX", "AMD", "INTC",
            "QCOM", "TXN", "CMCSA", "AMGN", "INTU", "ISRG", "GILD",
            "VRTX", "REGN", "MDLZ", "ADP", "PYPL", "AMAT",
        ]
        print(f"  Downloading {len(symbols)} stocks...")
        try:
            data = client.timeseries.get_range(
                dataset="XNAS.ITCH",
                schema="ohlcv-1d",
                symbols=symbols,
                start="2018-06-01",
                end="2024-12-31",
            )
            data.to_file(str(equities_path))

            df = data.to_df()
            df.to_parquet(RAW_DIR / "equities_daily_ohlcv.parquet")
            print(f"  Saved: {df.shape}")
        except Exception as e:
            print(f"  FAILED: {e}")
    else:
        print(f"  SKIP: already exists")

    # ── Process into experiment-ready format ──────────────────
    print("\n" + "=" * 60)
    print("  Processing into experiment-ready format")
    print("=" * 60)

    # Futures: pivot to close prices by symbol
    fut_parquet = RAW_DIR / "futures_daily_ohlcv.parquet"
    if fut_parquet.exists():
        try:
            df = pd.read_parquet(fut_parquet)
            # Databento df has 'symbol' and 'close' columns
            if 'symbol' in df.columns and 'close' in df.columns:
                closes = df.pivot_table(index=df.index, columns='symbol', values='close')
                returns = closes.pct_change().dropna()
                returns.to_parquet(PROC_DIR / "futures_daily_returns.parquet")
                print(f"  Futures returns: {returns.shape}")
            else:
                print(f"  Futures columns: {df.columns.tolist()}")
                # Save raw for inspection
                print(f"  Raw futures shape: {df.shape}, saving for manual inspection")
        except Exception as e:
            print(f"  Futures processing: {e}")

    # Equities: same
    eq_parquet = RAW_DIR / "equities_daily_ohlcv.parquet"
    if eq_parquet.exists():
        try:
            df = pd.read_parquet(eq_parquet)
            if 'symbol' in df.columns and 'close' in df.columns:
                closes = df.pivot_table(index=df.index, columns='symbol', values='close')
                returns = closes.pct_change().dropna()
                returns.to_parquet(PROC_DIR / "equities_50_daily_returns.parquet")
                print(f"  Equities returns: {returns.shape}")
            else:
                print(f"  Equities columns: {df.columns.tolist()}")
        except Exception as e:
            print(f"  Equities processing: {e}")

    print("\n  Batch 1 complete.")


if __name__ == "__main__":
    main()
