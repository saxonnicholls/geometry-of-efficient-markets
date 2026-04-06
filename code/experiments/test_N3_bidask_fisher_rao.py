#!/usr/bin/env python3
"""
Test N3: Bid-Ask Spread = Fisher-Rao Distance
===============================================
The LOB bid and ask sides, normalised to distributions, define two
points on the simplex. The Fisher-Rao distance between them should
correlate with the dollar bid-ask spread.

Hypothesis: d_FR(b_bid, b_ask) correlates > 0.8 with the dollar spread.
The Fisher-Rao spread should be MORE STABLE than the dollar spread
(because it normalises by volume at each level).

Data: Databento XNAS.ITCH mbp-10 (L2 book, top 10 levels)
Symbols: AAPL, MSFT, SPY (1 day, market hours)

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "raw" / "databento"
OUT_DIR = ROOT / "data" / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)


def fisher_rao_distance(p, q):
    """
    Bhattacharyya/Fisher-Rao distance between two distributions.
    d_FR = 2 * arccos(Σ √(p_i * q_i))
    """
    p = np.maximum(p, 1e-15)
    q = np.maximum(q, 1e-15)
    p = p / p.sum()
    q = q / q.sum()
    bc = np.sum(np.sqrt(p * q))
    bc = np.clip(bc, -1, 1)
    return 2 * np.arccos(bc)


def process_l2_book(df):
    """
    Process Databento mbp-10 data into bid/ask distributions and spreads.

    The mbp-10 schema has columns for 10 bid and 10 ask price levels:
    bid_px_00, bid_sz_00, ask_px_00, ask_sz_00, ..., bid_px_09, bid_sz_09, etc.
    """
    results = []

    # Check column format
    cols = df.columns.tolist()

    # Databento mbp-10 columns vary by version — detect format
    # Look for bid/ask price and size columns
    bid_px_cols = [c for c in cols if 'bid_px' in c or c.startswith('levels[')]
    ask_px_cols = [c for c in cols if 'ask_px' in c]
    bid_sz_cols = [c for c in cols if 'bid_sz' in c or 'bid_ct' in c]
    ask_sz_cols = [c for c in cols if 'ask_sz' in c or 'ask_ct' in c]

    print(f"  Detected column format:")
    print(f"    Bid price cols: {bid_px_cols[:3]}...")
    print(f"    Ask price cols: {ask_px_cols[:3]}...")
    print(f"    Bid size cols: {bid_sz_cols[:3]}...")
    print(f"    Ask size cols: {ask_sz_cols[:3]}...")

    if not bid_px_cols or not ask_px_cols:
        # Try to detect the Databento nested format
        # mbp-10 may have levels as nested arrays
        print(f"  All columns: {cols}")
        return pd.DataFrame()

    n_levels = min(len(bid_px_cols), len(ask_px_cols), 10)

    # Sample every 100th row to keep it manageable
    step = max(1, len(df) // 10000)

    for idx in range(0, len(df), step):
        row = df.iloc[idx]

        try:
            # Extract bid and ask sizes at each level
            bid_sizes = np.array([row.get(bid_sz_cols[i], 0) for i in range(n_levels)], dtype=float)
            ask_sizes = np.array([row.get(ask_sz_cols[i], 0) for i in range(n_levels)], dtype=float)

            bid_total = bid_sizes.sum()
            ask_total = ask_sizes.sum()

            if bid_total < 1 or ask_total < 1:
                continue

            # Normalise to distributions on the simplex
            b_bid = bid_sizes / bid_total
            b_ask = ask_sizes / ask_total

            # Fisher-Rao distance
            d_fr = fisher_rao_distance(b_bid, b_ask)

            # Dollar spread
            best_bid = row.get(bid_px_cols[0], 0)
            best_ask = row.get(ask_px_cols[0], 0)

            if best_bid > 0 and best_ask > 0:
                dollar_spread = (best_ask - best_bid)
                mid = (best_ask + best_bid) / 2
                pct_spread = dollar_spread / mid * 10000  # in bps
            else:
                continue

            # Book imbalance
            imbalance = (bid_total - ask_total) / (bid_total + ask_total)

            sym = row.get("symbol", "unknown")

            results.append({
                "timestamp": row.name if hasattr(row.name, 'hour') else idx,
                "symbol": sym,
                "d_fr": d_fr,
                "dollar_spread": dollar_spread,
                "pct_spread_bps": pct_spread,
                "mid": mid,
                "bid_total": bid_total,
                "ask_total": ask_total,
                "imbalance": imbalance,
            })
        except Exception:
            pass

    return pd.DataFrame(results)


def run_test_N3():
    print("=" * 70)
    print("  TEST N3: Bid-Ask Spread = Fisher-Rao Distance")
    print("  d_FR(b_bid, b_ask) should correlate with dollar spread")
    print("=" * 70)

    # Load L2 book data
    book_path = DATA_DIR / "l2_book_sample.parquet"
    if not book_path.exists():
        print(f"\n  ERROR: L2 book data not found at {book_path}")
        print(f"  Run download_databento_batch1.py or wait for background download.")
        sys.exit(1)

    df = pd.read_parquet(book_path)
    print(f"\n  Raw L2 data: {df.shape}")
    print(f"  Columns: {df.columns.tolist()[:20]}")

    # Process
    results = process_l2_book(df)

    if results.empty or len(results) < 100:
        print(f"\n  ERROR: Could not extract bid/ask distributions.")
        print(f"  The L2 data format may need adaptation.")
        sys.exit(1)

    print(f"\n  Processed: {len(results)} snapshots")

    # Per-symbol analysis
    for sym in results["symbol"].unique():
        sub = results[results["symbol"] == sym]
        if len(sub) < 50:
            continue

        corr = np.corrcoef(sub["d_fr"], sub["pct_spread_bps"])[0, 1]
        print(f"\n  {sym}: {len(sub)} snapshots")
        print(f"    d_FR: mean={sub.d_fr.mean():.4f}, std={sub.d_fr.std():.4f}")
        print(f"    Spread (bps): mean={sub.pct_spread_bps.mean():.1f}, std={sub.pct_spread_bps.std():.1f}")
        print(f"    Correlation(d_FR, spread_bps): {corr:.4f}")

    # Overall correlation
    overall_corr = np.corrcoef(results["d_fr"], results["pct_spread_bps"])[0, 1]
    print(f"\n  Overall correlation: {overall_corr:.4f}")

    # Verdict
    if overall_corr > 0.8:
        verdict = "PASS"
    elif overall_corr > 0.5:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"\n  VERDICT: {verdict} (correlation = {overall_corr:.3f})")

    # Save
    results.to_csv(OUT_DIR / "test_N3_results.csv", index=False)
    pd.Series({"test": "N3: Bid-Ask = Fisher-Rao", "verdict": verdict,
               "correlation": overall_corr, "n_snapshots": len(results)
               }).to_csv(OUT_DIR / "test_N3_summary.csv")

    return verdict


if __name__ == "__main__":
    verdict = run_test_N3()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
