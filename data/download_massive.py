#!/usr/bin/env python3
"""
Download market data from Massive (formerly Polygon.io).

Copyright Saxon Nicholls 2026 MIT Licence

Massive provides:
- US equities (all tickers, daily/minute/tick)
- Options (full OPRA feed)
- Forex (real-time and historical)
- Crypto (major exchanges)

REST API docs: https://polygon.io/docs (legacy) / massive.com/docs

Usage:
    pip install polygon-api-client
    export MASSIVE_API_KEY=your_key
    python download_massive.py
"""

import os
import sys
import time
import argparse
from pathlib import Path
from datetime import datetime, timedelta

import pandas as pd
import requests

RAW_DIR = Path(__file__).parent / "raw" / "massive"
RAW_DIR.mkdir(parents=True, exist_ok=True)


def load_api_key():
    """Load Massive/Polygon API key."""
    key = os.environ.get("MASSIVE_API_KEY")
    if key and key != "your_massive_key_here":
        return key

    env_path = Path(__file__).parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            if line.startswith("MASSIVE_API_KEY="):
                key = line.split("=", 1)[1].strip()
                if key and key != "your_massive_key_here":
                    return key
    return None


def download_sp500_daily(api_key: str, end_date: str):
    """
    Download S&P 500 constituent daily bars from Massive/Polygon.
    More reliable ticker coverage than yfinance.
    """
    print("\n=== Downloading S&P 500 daily bars (Massive) ===")

    # Get S&P 500 tickers
    # Polygon/Massive has a tickers endpoint
    base_url = "https://api.polygon.io"

    # First get the list of tickers
    tickers_url = (f"{base_url}/v3/reference/tickers"
                   f"?market=stocks&exchange=XNYS,XNAS"
                   f"&active=true&limit=1000"
                   f"&apiKey={api_key}")

    try:
        resp = requests.get(tickers_url, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        all_tickers = [t["ticker"] for t in data.get("results", [])]
        print(f"  Found {len(all_tickers)} tickers")
    except Exception as e:
        print(f"  Failed to get tickers: {e}")
        # Fallback to known large-caps
        all_tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META",
                       "BRK.B", "JPM", "V", "JNJ", "WMT", "PG", "XOM",
                       "UNH", "MA", "HD", "BAC", "PFE", "ABBV", "KO"]

    # Download daily bars for each ticker
    all_data = []
    for i, ticker in enumerate(all_tickers[:100]):  # Limit to top 100
        agg_url = (f"{base_url}/v2/aggs/ticker/{ticker}/range/1/day"
                   f"/2000-01-01/{end_date}"
                   f"?adjusted=true&sort=asc&limit=50000"
                   f"&apiKey={api_key}")

        try:
            resp = requests.get(agg_url, timeout=30)
            if resp.status_code == 200:
                data = resp.json()
                if data.get("results"):
                    df = pd.DataFrame(data["results"])
                    df["ticker"] = ticker
                    df["date"] = pd.to_datetime(df["t"], unit="ms")
                    all_data.append(df[["date", "ticker", "c"]])  # close price

            if (i + 1) % 20 == 0:
                print(f"    Downloaded {i + 1}/{min(len(all_tickers), 100)} tickers")

            # Rate limiting (5 requests per minute on free tier)
            time.sleep(0.25)

        except Exception as e:
            pass

    if all_data:
        combined = pd.concat(all_data, ignore_index=True)
        # Pivot to wide format
        prices = combined.pivot(index="date", columns="ticker", values="c")
        prices.to_parquet(RAW_DIR / "sp500_daily_massive.parquet")
        print(f"  Saved: {prices.shape}")
    else:
        print("  No data downloaded")


def download_options_snapshot(api_key: str):
    """Download options snapshot for vol surface construction."""
    print("\n=== Downloading Options Snapshot (Massive) ===")

    base_url = "https://api.polygon.io"
    url = (f"{base_url}/v3/snapshot/options/SPY"
           f"?apiKey={api_key}")

    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        results = data.get("results", [])
        if results:
            df = pd.DataFrame(results)
            df.to_parquet(RAW_DIR / "spy_options_snapshot.parquet")
            print(f"  Saved: {len(results)} option contracts")
        else:
            print("  No options data returned")
    except Exception as e:
        print(f"  FAILED: {e}")


def main():
    parser = argparse.ArgumentParser(description="Download data from Massive/Polygon")
    parser.add_argument("--end-date", default="2024-12-31")
    args = parser.parse_args()

    key = load_api_key()
    if not key:
        print("ERROR: No Massive/Polygon API key found.")
        print("Set MASSIVE_API_KEY in .env or environment.")
        sys.exit(1)

    download_sp500_daily(key, args.end_date)
    download_options_snapshot(key)

    print("\nMassive download complete.")


if __name__ == "__main__":
    main()
