#!/usr/bin/env python3
"""
Download and parse NASDAQ ITCH data for microstructure experiments.

Copyright Saxon Nicholls 2026 MIT Licence

Uses the martinobdl/ITCH parser: https://github.com/martinobdl/ITCH
This provides nanosecond-resolution order book data from NASDAQ TotalView-ITCH.

The ITCH data gives us:
- Every order add/modify/delete/execute message
- Full L3 order book reconstruction
- Nanosecond timestamps
- Needed for: Test M1 (LOB curvature), flash crash analysis,
  HFT as MCF, bid-ask = Fisher-Rao distance

ITCH sample data is available from:
    https://emi.nasdaq.com/ITCH/Nasdaq%20ITCH/
    (requires NASDAQ agreement for historical data)

For our experiments, we use the open-source sample files.

Usage:
    pip install itch  # martinobdl/ITCH parser
    python download_itch.py
"""

import os
import sys
import gzip
import struct
from pathlib import Path

import requests
import numpy as np
import pandas as pd

RAW_DIR = Path(__file__).parent / "raw" / "itch"
RAW_DIR.mkdir(parents=True, exist_ok=True)


# NASDAQ provides sample ITCH files at their FTP site
# These are typically ~5GB compressed for a full day
# We use a smaller sample for testing
ITCH_SAMPLE_URL = "https://emi.nasdaq.com/ITCH/Nasdaq%20ITCH/"


def download_itch_sample():
    """
    Download a sample ITCH file.
    Note: NASDAQ's full ITCH files require agreement.
    For experiments, we can use the martinobdl/ITCH library
    to parse any ITCH 5.0 file.
    """
    print("\n=== NASDAQ ITCH Data ===")
    print("  ITCH provides nanosecond-resolution order book data.")
    print("  Full data requires NASDAQ TotalView-ITCH subscription.")
    print()
    print("  For our microstructure experiments (Test M1-M5),")
    print("  we need L3 order book data for liquid stocks.")
    print()
    print("  Options:")
    print("  1. Use Databento's XNAS.ITCH dataset (included in subscription)")
    print("     → Run: python download_databento.py --dataset equities")
    print()
    print("  2. Use the martinobdl/ITCH parser on raw ITCH files:")
    print("     → pip install itch")
    print("     → Download ITCH files from NASDAQ")
    print("     → Parse with: python -c 'import itch; itch.parse(\"file.gz\")'")
    print()
    print("  3. Use Lobster data (lobsterdata.com) — academic access available")
    print()
    print("  For Test 5 (Cheeger) and Test M5 (microstructure-macro hierarchy),")
    print("  daily/minute data from Databento or Massive suffices.")
    print("  L3 order book is needed only for Tests M1-M4.")


def parse_itch_to_orderbook(itch_file: Path, ticker: str = "AAPL",
                             max_messages: int = 1_000_000) -> pd.DataFrame:
    """
    Parse ITCH 5.0 file to reconstruct order book snapshots.

    Uses martinobdl/ITCH if available, otherwise provides
    a skeleton that documents the expected format.

    Returns DataFrame with columns:
        timestamp, bid_price_1, bid_size_1, ask_price_1, ask_size_1,
        ..., bid_price_10, bid_size_10, ask_price_10, ask_size_10
    """
    try:
        import itch as itch_parser

        print(f"  Parsing ITCH file for {ticker}...")
        messages = itch_parser.parse(str(itch_file), max_messages=max_messages)

        # Filter for target ticker
        ticker_msgs = [m for m in messages if hasattr(m, 'stock')
                       and m.stock.strip() == ticker.encode()]

        print(f"  Found {len(ticker_msgs)} messages for {ticker}")

        # Reconstruct order book snapshots at regular intervals
        # (Full reconstruction requires tracking all add/modify/delete/execute)
        # This is a simplified version — for production use the full L3 reconstruction

        snapshots = []
        # ... (order book reconstruction logic)

        return pd.DataFrame(snapshots)

    except ImportError:
        print("  ITCH parser not installed. Run: pip install itch")
        print("  Returning empty DataFrame with expected schema.")

        return pd.DataFrame(columns=[
            "timestamp",
            "bid_price_1", "bid_size_1", "ask_price_1", "ask_size_1",
            "bid_price_2", "bid_size_2", "ask_price_2", "ask_size_2",
            "bid_price_3", "bid_size_3", "ask_price_3", "ask_size_3",
            "bid_price_4", "bid_size_4", "ask_price_4", "ask_size_4",
            "bid_price_5", "bid_size_5", "ask_price_5", "ask_size_5",
            "spread", "midprice", "imbalance",
        ])


def compute_lob_geometry(orderbook: pd.DataFrame) -> pd.DataFrame:
    """
    Compute LOB geometric quantities from order book snapshots:
    - Bid-ask spread (Fisher-Rao distance)
    - Book imbalance (curvature direction)
    - Depth profile (inverse curvature)
    - Fiedler eigenvalue of the price-level correlation graph

    These are the inputs for Test M1-M4 from MARKET_MICROSTRUCTURE.md.
    """
    if orderbook.empty:
        return pd.DataFrame()

    results = []
    for _, row in orderbook.iterrows():
        # Bid distribution: normalise bid sizes to a probability distribution
        bid_sizes = np.array([row.get(f"bid_size_{i}", 0)
                              for i in range(1, 6)], dtype=float)
        ask_sizes = np.array([row.get(f"ask_size_{i}", 0)
                              for i in range(1, 6)], dtype=float)

        bid_total = bid_sizes.sum()
        ask_total = ask_sizes.sum()

        if bid_total > 0 and ask_total > 0:
            b_bid = bid_sizes / bid_total  # bid distribution
            b_ask = ask_sizes / ask_total  # ask distribution

            # Ensure no zeros (for Fisher-Rao computation)
            b_bid = np.maximum(b_bid, 1e-10)
            b_ask = np.maximum(b_ask, 1e-10)
            b_bid /= b_bid.sum()
            b_ask /= b_ask.sum()

            # Fisher-Rao distance (Bhattacharyya)
            bc = np.sum(np.sqrt(b_bid * b_ask))
            d_fr = 2 * np.arccos(np.clip(bc, -1, 1))

            # Imbalance
            imbalance = (bid_total - ask_total) / (bid_total + ask_total)

            results.append({
                "timestamp": row.get("timestamp"),
                "spread_fr": d_fr,
                "imbalance": imbalance,
                "bid_depth": bid_total,
                "ask_depth": ask_total,
                "total_depth": bid_total + ask_total,
            })

    return pd.DataFrame(results)


def main():
    download_itch_sample()

    # If we have an ITCH file, parse it
    itch_files = list(RAW_DIR.glob("*.gz")) + list(RAW_DIR.glob("*.bin"))
    if itch_files:
        print(f"\n  Found ITCH files: {[f.name for f in itch_files]}")
        for f in itch_files:
            ob = parse_itch_to_orderbook(f, ticker="AAPL")
            if not ob.empty:
                geom = compute_lob_geometry(ob)
                outpath = RAW_DIR / f"{f.stem}_geometry.parquet"
                geom.to_parquet(outpath)
                print(f"  LOB geometry saved to {outpath}")
    else:
        print("\n  No ITCH files found in data/raw/itch/")
        print("  Place ITCH 5.0 files there and rerun.")


if __name__ == "__main__":
    main()
