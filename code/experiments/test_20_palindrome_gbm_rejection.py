#!/usr/bin/env python3
"""
test_20_palindrome_gbm_rejection.py

Statistical rejection of geometric Brownian motion as a model for equity returns,
using palindromic excess in the Voronoi-discretised symbolic sequence.

Under GBM, log-returns are i.i.d. normal. The symbolic sequence obtained by
Voronoi-discretising the returns is i.i.d. multinomial. For such sequences,
the expected number of palindromes of length 2k in a sequence of length T is
exactly (T - 2k + 1) * N^{-k} where N is the number of Voronoi cells.

We count palindromes in real S&P 500 daily returns (1926 - present) and compare
to this null prediction. Under GBM, we expect Z-scores near 0. Observed Z-scores
of 10+ would comprehensively reject GBM.

Paper: PALINDROMIC_SDE.md, Section 3.

Usage:
    python3 test_20_palindrome_gbm_rejection.py
    python3 test_20_palindrome_gbm_rejection.py --N 8 --ticker SPY
    python3 test_20_palindrome_gbm_rejection.py --max_k 15

Author: Saxon Nicholls
"""

import argparse
import sys
from pathlib import Path
import numpy as np
import pandas as pd

# Optional data source
try:
    import yfinance as yf
    YFINANCE_AVAILABLE = True
except ImportError:
    YFINANCE_AVAILABLE = False


# ─────────────────────────────────────────────────────────────
# Data loading
# ─────────────────────────────────────────────────────────────

def load_returns(ticker: str = "^GSPC", start: str = "1926-01-01") -> np.ndarray:
    """Load daily log returns for a ticker.

    Default: S&P 500 (^GSPC) from 1926. Yahoo may only have data from 1927-12 for this.
    """
    if not YFINANCE_AVAILABLE:
        # Fallback: load from local CSV if available
        csv_path = Path(__file__).parent.parent / "data" / "processed" / "sp500_daily.parquet"
        if csv_path.exists():
            df = pd.read_parquet(csv_path)
            prices = df["close"].values if "close" in df.columns else df.iloc[:, 0].values
        else:
            print(f"ERROR: yfinance not available and {csv_path} not found.")
            print("Install yfinance: pip install yfinance")
            sys.exit(1)
    else:
        print(f"Downloading {ticker} from {start}...")
        df = yf.download(ticker, start=start, progress=False)
        if df.empty:
            print(f"ERROR: Could not download {ticker}.")
            sys.exit(1)
        # Handle yfinance returning MultiIndex columns in recent versions
        if isinstance(df.columns, pd.MultiIndex):
            # Try "Adj Close" first, fall back to "Close"
            if ("Adj Close", ticker) in df.columns:
                prices = df[("Adj Close", ticker)].values
            elif ("Close", ticker) in df.columns:
                prices = df[("Close", ticker)].values
            else:
                # Fall back to first price-like column
                prices = df.iloc[:, 0].values
        elif "Adj Close" in df.columns:
            prices = df["Adj Close"].values
        elif "Close" in df.columns:
            prices = df["Close"].values
        else:
            prices = df.iloc[:, 0].values

    # Log returns
    prices = np.asarray(prices, dtype=float).flatten()
    prices = prices[~np.isnan(prices)]
    log_returns = np.diff(np.log(prices))
    log_returns = log_returns[~np.isnan(log_returns) & np.isfinite(log_returns)]
    return log_returns


# ─────────────────────────────────────────────────────────────
# Voronoi discretisation (balanced)
# ─────────────────────────────────────────────────────────────

def balanced_voronoi(returns: np.ndarray, N: int) -> np.ndarray:
    """Discretise returns into N Voronoi cells with equal empirical frequencies.

    The cell boundaries are quantiles of the empirical distribution, so each
    cell contains exactly 1/N of the data. Under GBM, the same applies (returns
    are i.i.d. so empirical quantiles are unbiased estimators of the CDF quantiles).
    """
    quantiles = np.quantile(returns, np.linspace(0, 1, N + 1))
    # Use digitize with interior boundaries only
    symbols = np.digitize(returns, quantiles[1:-1])
    return symbols


# ─────────────────────────────────────────────────────────────
# Palindrome counting
# ─────────────────────────────────────────────────────────────

def count_palindromes(seq: np.ndarray, length: int) -> int:
    """Count the number of palindromic subsequences of exactly this length.

    For each position i with room for a length-k subsequence, check whether
    seq[i:i+length] equals its reverse.
    """
    T = len(seq)
    if T < length:
        return 0
    count = 0
    half = length // 2
    for i in range(T - length + 1):
        window = seq[i : i + length]
        # A window is a palindrome iff window[:half] == window[-1:-half-1:-1]
        if np.array_equal(window[:half], window[length - 1 : length - 1 - half : -1]):
            count += 1
    return count


def count_palindromes_fast(seq: np.ndarray, length: int) -> int:
    """Vectorised palindrome count — much faster for long sequences."""
    T = len(seq)
    if T < length:
        return 0
    half = length // 2
    # Build index arrays
    starts = np.arange(T - length + 1)
    if half == 0:
        return T - length + 1  # every length-1 is a palindrome trivially
    # Compare seq[i+j] with seq[i+length-1-j] for j = 0, ..., half-1
    left = np.stack([seq[starts + j] for j in range(half)], axis=1)
    right = np.stack([seq[starts + length - 1 - j] for j in range(half)], axis=1)
    is_pal = np.all(left == right, axis=1)
    return int(is_pal.sum())


# ─────────────────────────────────────────────────────────────
# GBM null
# ─────────────────────────────────────────────────────────────

def gbm_palindrome_mean(T: int, k: int, N: int) -> float:
    """Expected palindrome count of length 2k under GBM (i.i.d. uniform)."""
    if T < 2 * k:
        return 0.0
    return (T - 2 * k + 1) * (N ** (-k))


def gbm_palindrome_variance(T: int, k: int, N: int) -> float:
    """Variance of palindrome count of length 2k under GBM null.

    To leading order (for T >> k), the variance is approximately equal to the
    mean (Poisson-like), with a correction from overlapping palindrome windows.
    This is the standard result for i.i.d. pattern counts.
    """
    mu = gbm_palindrome_mean(T, k, N)
    if mu < 1e-10:
        return mu  # degenerate case

    # Leading-order variance: mu (Poisson-like for non-overlapping) plus
    # overlap correction. Overlap correction for palindromes is small but
    # we compute it for completeness.
    L = 2 * k
    overlap_corr = 0.0
    for j in range(1, L):
        # Probability that positions i and i+j are BOTH palindrome centres.
        # For j < L, overlapping windows share 2k - j symbols.
        # This imposes extra constraints; exact formula depends on parity of j.
        # We use the approximation C_j = N^{-(2k - gcd(j, 2k) + 1)} which is
        # accurate for small j.
        # For simplicity and conservatism, use: C_j = N^{-(2k)} for j close to L
        # (independent) and larger for small j.
        overlap_corr += 2 * (T - L + 1 - j) * (N ** (-(2 * k - 1)))

    var = mu * (1 - N ** (-k)) + max(overlap_corr, 0)
    return max(var, mu)  # at least Poisson


# ─────────────────────────────────────────────────────────────
# Bootstrap variance check
# ─────────────────────────────────────────────────────────────

def bootstrap_gbm_variance(T: int, k: int, N: int, n_boot: int = 500) -> tuple:
    """Bootstrap the palindrome count variance under the GBM null.

    Generate n_boot random i.i.d. sequences of length T with N-alphabet,
    count palindromes of length 2k in each, and report mean + variance.
    This confirms the analytical calculation.
    """
    rng = np.random.default_rng(42)
    counts = np.zeros(n_boot, dtype=np.int64)
    for b in range(n_boot):
        seq = rng.integers(0, N, size=T)
        counts[b] = count_palindromes_fast(seq, 2 * k)
    return float(counts.mean()), float(counts.std())


# ─────────────────────────────────────────────────────────────
# Main test
# ─────────────────────────────────────────────────────────────

def run_test(ticker: str, N: int, k_values: list, bootstrap: bool = True) -> pd.DataFrame:
    """Run the palindrome GBM rejection test."""
    print(f"\n{'=' * 70}")
    print(f"TEST: Palindrome-based rejection of GBM")
    print(f"{'=' * 70}")
    print(f"Ticker:       {ticker}")
    print(f"Alphabet:     N = {N} (balanced Voronoi cells)")
    print(f"Palindrome lengths tested: 2k for k in {k_values}")

    # Load data
    returns = load_returns(ticker)
    T = len(returns)
    print(f"Observations: T = {T:,} days")
    print(f"Date range:   inferred from data")

    # Discretise
    symbols = balanced_voronoi(returns, N)
    # Verify balance
    _, counts = np.unique(symbols, return_counts=True)
    print(f"Cell counts:  {counts.tolist()}")
    print(f"Balance:      min/max = {counts.min()}/{counts.max()}")

    # Count palindromes and compute Z-scores
    print(f"\n{'=' * 70}")
    print(f"{'2k':>4} {'Observed':>10} {'GBM mean':>12} {'GBM std':>10} "
          f"{'Z-score':>10} {'p-value':>12}")
    print(f"{'=' * 70}")

    results = []
    for k in k_values:
        L = 2 * k
        observed = count_palindromes_fast(symbols, L)
        mu = gbm_palindrome_mean(T, k, N)
        var = gbm_palindrome_variance(T, k, N)
        std = np.sqrt(var) if var > 0 else 1e-10

        # Z-score
        z = (observed - mu) / std if std > 0 else 0

        # p-value (one-sided, for palindromic excess)
        from scipy.stats import norm
        p_value = 1 - norm.cdf(z)
        # For extreme Z, clamp reporting
        p_str = f"{p_value:.2e}" if p_value > 1e-100 else "< 1e-100"

        print(f"{L:>4} {observed:>10,} {mu:>12,.2f} {std:>10,.2f} "
              f"{z:>10,.2f} {p_str:>12}")

        results.append({
            "2k": L,
            "observed": observed,
            "gbm_mean": mu,
            "gbm_std": std,
            "z_score": z,
            "p_value": p_value,
        })

    df = pd.DataFrame(results)

    # Bootstrap check (for one k value, to confirm analytical variance)
    if bootstrap and len(k_values) > 0:
        k_check = k_values[min(2, len(k_values) - 1)]  # middle k
        print(f"\n{'-' * 70}")
        print(f"Bootstrap check for 2k = {2 * k_check}:")
        mu_boot, std_boot = bootstrap_gbm_variance(T, k_check, N, n_boot=200)
        mu_analytic = gbm_palindrome_mean(T, k_check, N)
        std_analytic = np.sqrt(gbm_palindrome_variance(T, k_check, N))
        print(f"  Analytic:  mean={mu_analytic:.2f}, std={std_analytic:.2f}")
        print(f"  Bootstrap: mean={mu_boot:.2f}, std={std_boot:.2f}")
        print(f"  Ratio:     {mu_boot / mu_analytic:.3f} (mean), "
              f"{std_boot / std_analytic:.3f} (std)")

    # Verdict
    print(f"\n{'=' * 70}")
    print(f"VERDICT")
    print(f"{'=' * 70}")
    max_z = df["z_score"].max()
    if max_z > 10:
        print(f"GBM REJECTED with Z_max = {max_z:.2f}")
        print(f"This is a comprehensive rejection. GBM is NOT a valid model")
        print(f"for the symbolic dynamics of these returns.")
    elif max_z > 3:
        print(f"GBM rejected at conventional levels (Z_max = {max_z:.2f}).")
    else:
        print(f"GBM not rejected (Z_max = {max_z:.2f}).")
    print(f"{'=' * 70}\n")

    return df


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", default="^GSPC", help="Yahoo Finance ticker (default: ^GSPC)")
    parser.add_argument("--N", type=int, default=6, help="Voronoi alphabet size (default: 6)")
    parser.add_argument("--max_k", type=int, default=10, help="Maximum k (half-length) to test")
    parser.add_argument("--no_bootstrap", action="store_true", help="Skip bootstrap variance check")
    parser.add_argument("--save", type=str, default=None, help="Save results CSV")
    args = parser.parse_args()

    k_values = list(range(2, args.max_k + 1))
    df = run_test(args.ticker, args.N, k_values, bootstrap=not args.no_bootstrap)

    if args.save:
        df.to_csv(args.save, index=False)
        print(f"Results saved to {args.save}")


if __name__ == "__main__":
    main()
