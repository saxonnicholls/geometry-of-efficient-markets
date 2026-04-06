#!/usr/bin/env python3
"""
Download market data from Databento for experiments requiring
high-quality institutional data.

Copyright Saxon Nicholls 2026 MIT Licence

Databento provides:
- US equities (all exchanges, NBBO, trades, L2/L3 order book)
- Futures (CME, ICE, Eurex)
- Options (OPRA)
- Crypto (Coinbase, Binance)

SDK docs: https://docs.databento.com/getting-started/python

Usage:
    pip install databento
    export DATABENTO_API_KEY=your_key
    python download_databento.py [--dataset equities|futures|options|crypto]
"""

import os
import sys
import argparse
from pathlib import Path
from datetime import date

RAW_DIR = Path(__file__).parent / "raw" / "databento"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def load_api_key():
    """Load Databento API key from .env or environment."""
    key = os.environ.get("DATABENTO_API_KEY")
    if key and key != "your_databento_key_here":
        return key

    # Try .env file
    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("DATABENTO_API_KEY="):
                key = line.split("=", 1)[1].strip()
                if key and key != "your_databento_key_here":
                    return key

    return None


def download_equities(client, end_date: str):
    """
    Download S&P 500 daily OHLCV and NBBO for Tests 1-5, 11.
    Also download tick-level data for a subset for Test M1 (microstructure).
    """
    print("\n=== Downloading US Equities (Databento) ===")

    # Daily OHLCV for S&P 500 (via XNAS.ITCH + XNYS.TRADES)
    print("  Fetching S&P 500 daily bars...")
    try:
        data = client.timeseries.get_range(
            dataset="XNAS.ITCH",
            schema="ohlcv-1d",
            symbols=["SPY", "QQQ", "IWM", "XLK", "XLF", "XLV", "XLY",
                      "XLP", "XLE", "XLI", "XLU", "XLB",
                      "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META",
                      "BRK.B", "JPM", "V", "JNJ", "WMT", "PG", "XOM",
                      "UNH", "MA", "HD", "BAC", "PFE", "ABBV", "KO",
                      "PEP", "MRK", "COST", "TMO", "AVGO", "CSCO",
                      "ACN", "MCD", "ABT", "DHR", "LIN", "ADBE"],
            start="2000-01-01",
            end=end_date,
        )
        outpath = RAW_DIR / "equities_daily_ohlcv.parquet"
        data.to_parquet(outpath)
        print(f"    -> {outpath}")
    except Exception as e:
        print(f"    FAILED: {e}")

    # Tick-level NBBO for a few liquid stocks (for microstructure test)
    print("  Fetching tick-level NBBO for AAPL, MSFT, SPY (last 5 days)...")
    try:
        data = client.timeseries.get_range(
            dataset="XNAS.ITCH",
            schema="mbp-1",  # L1 best bid/offer
            symbols=["AAPL", "MSFT", "SPY"],
            start="2024-12-23",
            end="2024-12-31",
        )
        outpath = RAW_DIR / "tick_nbbo_sample.parquet"
        data.to_parquet(outpath)
        print(f"    -> {outpath}")
    except Exception as e:
        print(f"    FAILED: {e}")


def download_futures(client, end_date: str):
    """
    Download futures data for intermarket spread tests.
    Brent (ICE) vs WTI (CME) for INTERMARKET_GEOMETRY tests.
    """
    print("\n=== Downloading Futures (Databento) ===")

    try:
        # WTI crude (CME)
        data = client.timeseries.get_range(
            dataset="GLBX.MDP3",  # CME Globex
            schema="ohlcv-1d",
            symbols=["CL.FUT"],  # WTI crude continuous front month
            start="2010-01-01",
            end=end_date,
        )
        outpath = RAW_DIR / "wti_daily.parquet"
        data.to_parquet(outpath)
        print(f"  WTI -> {outpath}")
    except Exception as e:
        print(f"  WTI FAILED: {e}")

    try:
        # Treasury futures (for yield curve test)
        data = client.timeseries.get_range(
            dataset="GLBX.MDP3",
            schema="ohlcv-1d",
            symbols=["ZN.FUT", "ZB.FUT", "ZF.FUT", "ZT.FUT"],  # 10Y, 30Y, 5Y, 2Y
            start="2010-01-01",
            end=end_date,
        )
        outpath = RAW_DIR / "treasury_futures_daily.parquet"
        data.to_parquet(outpath)
        print(f"  Treasury futures -> {outpath}")
    except Exception as e:
        print(f"  Treasury futures FAILED: {e}")


def download_options(client, end_date: str):
    """
    Download options data for volatility surface test.
    SPX options for the vol surface geometry.
    """
    print("\n=== Downloading Options (Databento) ===")

    try:
        # SPX options — recent snapshot for vol surface construction
        data = client.timeseries.get_range(
            dataset="OPRA.PILLAR",
            schema="mbp-1",
            symbols=["SPX"],
            start="2024-12-23",
            end="2024-12-31",
            stype_in="parent",
        )
        outpath = RAW_DIR / "spx_options_sample.parquet"
        data.to_parquet(outpath)
        print(f"  SPX options -> {outpath}")
    except Exception as e:
        print(f"  SPX options FAILED: {e}")


def download_crypto(client, end_date: str):
    """Download crypto data for Test 19 (crypto efficiency stages)."""
    print("\n=== Downloading Crypto (Databento) ===")

    try:
        data = client.timeseries.get_range(
            dataset="COINBASE",
            schema="ohlcv-1d",
            symbols=["BTC-USD", "ETH-USD", "SOL-USD"],
            start="2020-01-01",
            end=end_date,
        )
        outpath = RAW_DIR / "crypto_daily_databento.parquet"
        data.to_parquet(outpath)
        print(f"  Crypto -> {outpath}")
    except Exception as e:
        print(f"  Crypto FAILED: {e}")


def main():
    parser = argparse.ArgumentParser(description="Download data from Databento")
    parser.add_argument("--dataset", choices=["equities", "futures", "options",
                                               "crypto", "all"],
                        default="all")
    parser.add_argument("--end-date", default="2024-12-31")
    args = parser.parse_args()

    key = load_api_key()
    if not key:
        print("ERROR: No Databento API key found.")
        print("Set DATABENTO_API_KEY in .env or environment.")
        print("Get your key at: https://databento.com")
        sys.exit(1)

    try:
        import databento as db
    except ImportError:
        print("ERROR: databento SDK not installed.")
        print("Run: pip install databento")
        sys.exit(1)

    client = db.Historical(key=key)
    print(f"Databento connected. End date: {args.end_date}")

    if args.dataset in ("equities", "all"):
        download_equities(client, args.end_date)
    if args.dataset in ("futures", "all"):
        download_futures(client, args.end_date)
    if args.dataset in ("options", "all"):
        download_options(client, args.end_date)
    if args.dataset in ("crypto", "all"):
        download_crypto(client, args.end_date)

    print("\nDatabento download complete.")


if __name__ == "__main__":
    main()
