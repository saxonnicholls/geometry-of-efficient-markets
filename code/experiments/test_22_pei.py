#!/usr/bin/env python3
"""
test_22_pei.py

The Palindromic Efficiency Index (PEI) and palindrome partition function
for market return sequences.

PEI(σ) = 1 - minCuts(σ)/(T-1)

where minCuts is the minimum number of cuts to partition σ into palindromes.

Paper: PALINDROMIC_PARTITION_EFFICIENCY.md

Usage:
    python3 test_22_pei.py
    python3 test_22_pei.py --ticker SPY --N 6 --window 1000

Author: Saxon Nicholls
"""

import argparse
import numpy as np
import pandas as pd
import sys
from pathlib import Path

try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False


# ─────────────────────────────────────────────────────────────
# Palindrome DP
# ─────────────────────────────────────────────────────────────

def is_palindrome_table(seq):
    """Build is_pal[i][j] = True iff seq[i:j+1] is a palindrome."""
    n = len(seq)
    is_pal = np.zeros((n, n), dtype=bool)
    # Length 1
    for i in range(n):
        is_pal[i, i] = True
    # Length 2
    for i in range(n - 1):
        is_pal[i, i + 1] = (seq[i] == seq[i + 1])
    # Length 3+
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            is_pal[i, j] = (seq[i] == seq[j] and is_pal[i + 1, j - 1])
    return is_pal


def min_cuts_palindrome(seq):
    """Compute minimum cuts to partition seq into palindromes."""
    n = len(seq)
    if n <= 1:
        return 0
    is_pal = is_palindrome_table(seq)

    # DP for min cuts
    cuts = np.zeros(n, dtype=np.int64)
    for i in range(n):
        if is_pal[0, i]:
            cuts[i] = 0
        else:
            cuts[i] = i  # worst case: all single chars
            for j in range(i):
                if is_pal[j + 1, i]:
                    candidate = cuts[j] + 1
                    if candidate < cuts[i]:
                        cuts[i] = candidate
    return int(cuts[n - 1])


def count_palindrome_partitions(seq):
    """Count the number of palindromic partitions (log-scale to avoid overflow)."""
    n = len(seq)
    if n == 0:
        return 0.0
    is_pal = is_palindrome_table(seq)

    # log partition count DP
    log_P = np.full(n, -np.inf)
    for i in range(n):
        if is_pal[0, i]:
            log_P[i] = 0.0  # one partition: the whole prefix as one palindrome
        # Combine with shorter partitions
        for j in range(i):
            if is_pal[j + 1, i] and log_P[j] > -np.inf:
                # log_P[i] += log_P[j]  (add count, not log)
                log_P[i] = np.logaddexp(log_P[i], log_P[j])
    return log_P[n - 1] / np.log(2)  # in bits


def pei(seq):
    """Palindromic Efficiency Index."""
    n = len(seq)
    if n <= 1:
        return 1.0
    min_cuts = min_cuts_palindrome(seq)
    return 1.0 - min_cuts / (n - 1)


# ─────────────────────────────────────────────────────────────
# Data loading
# ─────────────────────────────────────────────────────────────

def load_returns(ticker="^GSPC", start="1926-01-01"):
    """Load daily log returns."""
    if not YFINANCE_AVAILABLE:
        csv_path = Path(__file__).parent.parent / "data" / "processed" / "sp500_daily.parquet"
        if csv_path.exists():
            df = pd.read_parquet(csv_path)
            prices = df["close"].values if "close" in df.columns else df.iloc[:, 0].values
        else:
            print(f"ERROR: yfinance not available and {csv_path} not found.")
            sys.exit(1)
    else:
        print(f"Downloading {ticker} from {start}...")
        df = yf.download(ticker, start=start, progress=False)
        if df.empty:
            print(f"ERROR: Could not download {ticker}.")
            sys.exit(1)
        if isinstance(df.columns, pd.MultiIndex):
            if ("Adj Close", ticker) in df.columns:
                prices = df[("Adj Close", ticker)].values
            elif ("Close", ticker) in df.columns:
                prices = df[("Close", ticker)].values
            else:
                prices = df.iloc[:, 0].values
        elif "Adj Close" in df.columns:
            prices = df["Adj Close"].values
        elif "Close" in df.columns:
            prices = df["Close"].values
        else:
            prices = df.iloc[:, 0].values

    prices = np.asarray(prices, dtype=float).flatten()
    prices = prices[~np.isnan(prices)]
    log_returns = np.diff(np.log(prices))
    log_returns = log_returns[~np.isnan(log_returns) & np.isfinite(log_returns)]
    return log_returns


def balanced_voronoi(returns, N):
    """Discretise returns into N quantile-balanced cells."""
    quantiles = np.quantile(returns, np.linspace(0, 1, N + 1))
    symbols = np.digitize(returns, quantiles[1:-1])
    return symbols


# ─────────────────────────────────────────────────────────────
# Main analysis
# ─────────────────────────────────────────────────────────────

def run_analysis(ticker, N, window):
    """Compute PEI over rolling windows."""
    print(f"\n{'=' * 70}")
    print(f"PALINDROMIC EFFICIENCY INDEX (PEI)")
    print(f"{'=' * 70}")
    print(f"Ticker:       {ticker}")
    print(f"Alphabet:     N = {N} Voronoi cells")
    print(f"Window:       W = {window} days")

    returns = load_returns(ticker)
    T = len(returns)
    print(f"Total data:   T = {T:,} days")

    symbols = balanced_voronoi(returns, N)

    # Full-sample PEI
    print(f"\n{'-' * 70}")
    print(f"FULL-SAMPLE ANALYSIS")
    print(f"{'-' * 70}")

    # Cap the full-sample analysis at 5000 points for tractability
    # (O(T^2) memory = 25M booleans for T=5000, manageable)
    T_sample = min(T, 5000)
    sample_symbols = symbols[:T_sample]
    print(f"Analysing first {T_sample} points (O(T^2) DP scales)...")

    min_cuts = min_cuts_palindrome(sample_symbols)
    pei_value = 1.0 - min_cuts / (T_sample - 1)
    log_P_bits = count_palindrome_partitions(sample_symbols)

    print(f"\nMinimum cuts:             {min_cuts:,}")
    print(f"Maximum possible cuts:    {T_sample - 1:,}")
    print(f"PEI:                      {pei_value:.4f}")
    print(f"  (0 = fully random, 1 = fully palindromic)")
    print(f"log₂ P(σ):                {log_P_bits:.2f} bits")
    print(f"Partition entropy per symbol: {log_P_bits / (T_sample - 1):.4f} bits/symbol")

    # Class identification
    if pei_value > 0.7:
        cls = "P1/P2 (Sturmian/Episturmian)"
    elif pei_value > 0.4:
        cls = "P3/P4 (Arnoux-Rauzy/Pisot)"
    elif pei_value > 0.2:
        cls = "P5 (Thue-Morse/transitional)"
    else:
        cls = "P6 (Bernoulli/random)"
    print(f"\nInferred universality class: {cls}")

    # Rolling PEI analysis
    print(f"\n{'-' * 70}")
    print(f"ROLLING WINDOW ANALYSIS (window size = {window})")
    print(f"{'-' * 70}")

    n_windows = max(1, (T - window) // (window // 2) + 1)  # overlapping by 50%
    rolling_pei = []
    rolling_dates_idx = []

    for w in range(n_windows):
        start_idx = w * (window // 2)
        end_idx = start_idx + window
        if end_idx > T:
            break
        window_symbols = symbols[start_idx:end_idx]
        w_pei = pei(window_symbols)
        rolling_pei.append(w_pei)
        rolling_dates_idx.append(end_idx)

    print(f"\nRolling PEI statistics:")
    print(f"  Mean:   {np.mean(rolling_pei):.4f}")
    print(f"  Min:    {np.min(rolling_pei):.4f}  (most random/crisis window)")
    print(f"  Max:    {np.max(rolling_pei):.4f}  (most palindromic/efficient window)")
    print(f"  Std:    {np.std(rolling_pei):.4f}")

    # Identify crisis windows (lowest PEI)
    print(f"\nLowest 5 PEI windows (potential crises):")
    order = np.argsort(rolling_pei)
    for i in order[:5]:
        # Approximate date: return index → days since 1926
        approximate_year = 1926 + rolling_dates_idx[i] / 252  # ~252 trading days/year
        print(f"  Window ending ~{approximate_year:.1f}: PEI = {rolling_pei[i]:.4f}")

    print(f"\nHighest 5 PEI windows (most efficient):")
    for i in order[::-1][:5]:
        approximate_year = 1926 + rolling_dates_idx[i] / 252
        print(f"  Window ending ~{approximate_year:.1f}: PEI = {rolling_pei[i]:.4f}")

    print(f"\n{'=' * 70}\n")

    return {
        "pei_full": pei_value,
        "log_P_bits": log_P_bits,
        "rolling_pei": rolling_pei,
        "rolling_dates_idx": rolling_dates_idx,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", default="^GSPC", help="Yahoo ticker")
    parser.add_argument("--N", type=int, default=6, help="Voronoi alphabet size")
    parser.add_argument("--window", type=int, default=500, help="Rolling window size")
    args = parser.parse_args()

    run_analysis(args.ticker, args.N, args.window)


if __name__ == "__main__":
    main()
