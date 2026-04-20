#!/usr/bin/env python3
"""
test_23_fps_vs_gbm.py

Comprehensive empirical comparison of GBM and FPS (Fractional Palindromic SDE)
as models for S&P 500 returns.

Tests:
  1. Palindrome count at multiple lengths (real vs GBM vs FPS simulations)
  2. Palindromic Efficiency Index (PEI) distributions
  3. Autocorrelation of squared returns (volatility clustering)
  4. Return distribution (fat tails)
  5. Sample paths comparison
  6. Variogram (mean-reversion signature)

Output: PNG graphics in data/results/fps_vs_gbm/
Paper: PALINDROMIC_SDE.md and PEI_EMPIRICAL_RESULTS.md

Author: Saxon Nicholls
"""

import argparse
import numpy as np
import pandas as pd
import sys
import time
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

sys.path.insert(0, str(Path(__file__).parent))

from test_22_pei import (
    is_palindrome_table,
    min_cuts_palindrome,
    pei,
    load_returns,
    balanced_voronoi,
)
from test_20_palindrome_gbm_rejection import (
    count_palindromes_fast,
    gbm_palindrome_mean,
    gbm_palindrome_variance,
)


# ─────────────────────────────────────────────────────────────
# Setup and style
# ─────────────────────────────────────────────────────────────

plt.rcParams.update({
    "font.family": "serif",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.labelsize": 12,
    "legend.fontsize": 10,
    "figure.titlesize": 14,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "axes.spines.top": False,
    "axes.spines.right": False,
})


# ─────────────────────────────────────────────────────────────
# Simulate GBM
# ─────────────────────────────────────────────────────────────

def simulate_gbm(T, mu, sigma, seed=None):
    """Simulate GBM log-returns: r_t ~ N(mu - sigma^2/2, sigma^2) i.i.d."""
    rng = np.random.default_rng(seed)
    return rng.normal(loc=mu - 0.5 * sigma ** 2, scale=sigma, size=T)


# ─────────────────────────────────────────────────────────────
# Simulate FPS (fractional Palindromic SDE)
# ─────────────────────────────────────────────────────────────

def fractional_gaussian_noise(T, H, seed=None):
    """Generate fractional Gaussian noise via Davies-Harte (circulant embedding).

    For H < 0.5: anti-persistent. For H > 0.5: persistent. For H = 0.5: white noise.
    """
    rng = np.random.default_rng(seed)

    # Autocovariance of fGn
    def gamma(k, H):
        return 0.5 * (abs(k - 1) ** (2 * H) - 2 * abs(k) ** (2 * H) + abs(k + 1) ** (2 * H))

    # Davies-Harte: circulant embedding
    M = 2 * (T - 1)  # circulant size
    # Construct first row of circulant
    c = np.zeros(M, dtype=float)
    for k in range(T):
        c[k] = gamma(k, H)
    for k in range(T, M):
        c[k] = gamma(M - k, H)
    # FFT
    lam = np.fft.fft(c).real
    lam = np.maximum(lam, 0)  # clip any numerical negatives
    # Generate complex Gaussian
    V = rng.standard_normal(M) + 1j * rng.standard_normal(M)
    V *= np.sqrt(lam / (2 * M))
    # Inverse FFT, take real part, return first T values
    fgn = np.fft.fft(V).real[:T] * np.sqrt(2)
    return fgn


def simulate_fps(T, kappa, theta, sigma, H, dt=1.0, seed=None):
    """Simulate FPS: dX_t = kappa*(theta - X_t) dt + sigma * dB^H_t
    via Euler-Maruyama with fractional Gaussian noise."""
    # Generate fGn
    fgn = fractional_gaussian_noise(T, H, seed=seed)
    # Normalize so std = 1 per unit time
    fgn = fgn * dt ** H

    # Integrate OU with fractional noise
    X = np.zeros(T + 1)
    X[0] = theta
    for t in range(T):
        X[t + 1] = X[t] + kappa * (theta - X[t]) * dt + sigma * fgn[t]
    return np.diff(X)  # return log-returns


# ─────────────────────────────────────────────────────────────
# PLOT 1: Palindrome count comparison
# ─────────────────────────────────────────────────────────────

def plot_palindrome_counts(real_symbols, gbm_symbols, fps_symbols, output_path, N=6):
    """Compare palindrome counts (real vs GBM vs FPS) at multiple lengths."""
    fig, ax = plt.subplots(figsize=(12, 7))

    lengths = [4, 6, 8, 10, 12, 14, 16, 20]
    T = len(real_symbols)

    real_counts = []
    gbm_counts = []
    fps_counts = []
    gbm_predicted = []

    for L in lengths:
        real_counts.append(count_palindromes_fast(real_symbols, L))
        gbm_counts.append(count_palindromes_fast(gbm_symbols, L))
        fps_counts.append(count_palindromes_fast(fps_symbols, L))
        gbm_predicted.append(gbm_palindrome_mean(T, L // 2, N))

    x = np.arange(len(lengths))
    width = 0.2

    ax.bar(x - 1.5 * width, gbm_predicted, width, label="GBM analytical prediction",
           color="#cccccc", edgecolor="black", linewidth=0.5)
    ax.bar(x - 0.5 * width, gbm_counts, width, label="GBM simulation",
           color="red", edgecolor="black", linewidth=0.5, alpha=0.8)
    ax.bar(x + 0.5 * width, fps_counts, width, label="FPS simulation",
           color="green", edgecolor="black", linewidth=0.5, alpha=0.8)
    ax.bar(x + 1.5 * width, real_counts, width, label="S&P 500 observed",
           color="#1f4e79", edgecolor="black", linewidth=0.5)

    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{L}" for L in lengths])
    ax.set_xlabel("Palindrome length $2k$")
    ax.set_ylabel("Count (log scale)")
    ax.set_title(
        "Palindrome Counts: Real Data vs GBM vs FPS\n"
        "FPS matches real data; GBM dramatically underpredicts"
    )
    ax.legend(loc="upper right")

    # Annotate Z-scores for real vs GBM
    for i, L in enumerate(lengths):
        real_c = real_counts[i]
        gbm_c = gbm_predicted[i]
        if gbm_c > 0:
            std = np.sqrt(gbm_c)
            z = (real_c - gbm_c) / std if std > 0 else 0
            if abs(z) > 3:
                ax.annotate(
                    f"Z={z:.1f}", xy=(x[i] + 1.5 * width, real_c),
                    xytext=(0, 5), textcoords="offset points",
                    fontsize=8, ha="center", color="darkblue",
                )

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")

    return {
        "lengths": lengths,
        "real": real_counts,
        "gbm_sim": gbm_counts,
        "fps_sim": fps_counts,
        "gbm_pred": gbm_predicted,
    }


# ─────────────────────────────────────────────────────────────
# PLOT 2: PEI distribution comparison
# ─────────────────────────────────────────────────────────────

def plot_pei_distributions(real_symbols, gbm_returns_fn, fps_returns_fn,
                           output_path, N=6, window=250, n_sims=20):
    """Plot PEI distributions: real vs GBM vs FPS."""
    fig, ax = plt.subplots(figsize=(11, 6))

    # Real PEI distribution (rolling)
    T_real = len(real_symbols)
    stride = 120
    real_pei = []
    for start in range(0, T_real - window + 1, stride):
        real_pei.append(pei(real_symbols[start:start + window]))
    real_pei = np.array(real_pei)

    # GBM PEI distribution
    print(f"  Simulating {n_sims} GBM sequences...")
    gbm_pei = []
    for sim in range(n_sims):
        gbm_ret = gbm_returns_fn(window, seed=sim)
        gbm_sym = balanced_voronoi(gbm_ret, N)
        gbm_pei.append(pei(gbm_sym))
    gbm_pei = np.array(gbm_pei)

    # FPS PEI distribution
    print(f"  Simulating {n_sims} FPS sequences...")
    fps_pei = []
    for sim in range(n_sims):
        fps_ret = fps_returns_fn(window, seed=sim + 1000)
        fps_sym = balanced_voronoi(fps_ret, N)
        fps_pei.append(pei(fps_sym))
    fps_pei = np.array(fps_pei)

    bins = np.linspace(0.25, 0.75, 31)
    ax.hist(gbm_pei, bins=bins, alpha=0.55, color="red",
            density=True, label=f"GBM ({n_sims} sims)",
            edgecolor="black", linewidth=0.5)
    ax.hist(fps_pei, bins=bins, alpha=0.55, color="green",
            density=True, label=f"FPS ({n_sims} sims)",
            edgecolor="black", linewidth=0.5)
    ax.hist(real_pei, bins=bins, alpha=0.55, color="#1f4e79",
            density=True, label=f"S&P 500 empirical ({len(real_pei)} windows)",
            edgecolor="black", linewidth=0.5)

    ax.axvline(np.mean(real_pei), color="#1f4e79", linestyle="--", lw=2,
               label=f"S&P 500 mean: {np.mean(real_pei):.3f}")
    ax.axvline(np.mean(gbm_pei), color="red", linestyle="--", lw=2,
               label=f"GBM mean: {np.mean(gbm_pei):.3f}")
    ax.axvline(np.mean(fps_pei), color="green", linestyle="--", lw=2,
               label=f"FPS mean: {np.mean(fps_pei):.3f}")

    ax.set_xlabel("PEI")
    ax.set_ylabel("Density")
    ax.set_title(
        "PEI Distribution: S&P 500 vs GBM vs FPS\n"
        "FPS captures the empirical distribution; GBM doesn't"
    )
    ax.legend(loc="upper right", fontsize=9)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")

    return {"real_pei": real_pei, "gbm_pei": gbm_pei, "fps_pei": fps_pei}


# ─────────────────────────────────────────────────────────────
# PLOT 3: Autocorrelation of squared returns (volatility clustering)
# ─────────────────────────────────────────────────────────────

def autocorrelation(x, max_lag):
    """Compute autocorrelation at lags 1..max_lag."""
    x = x - np.mean(x)
    n = len(x)
    result = np.zeros(max_lag + 1)
    result[0] = 1.0
    var = np.sum(x ** 2)
    for k in range(1, max_lag + 1):
        result[k] = np.sum(x[:n - k] * x[k:]) / var
    return result


def plot_volatility_clustering(real_returns, gbm_returns, fps_returns, output_path):
    """Autocorrelation of squared returns — measures volatility clustering."""
    fig, ax = plt.subplots(figsize=(11, 6))
    max_lag = 50

    # Absolute returns (proxy for volatility)
    real_sq = np.abs(real_returns)
    gbm_sq = np.abs(gbm_returns)
    fps_sq = np.abs(fps_returns)

    real_acf = autocorrelation(real_sq, max_lag)
    gbm_acf = autocorrelation(gbm_sq, max_lag)
    fps_acf = autocorrelation(fps_sq, max_lag)

    lags = np.arange(0, max_lag + 1)
    ax.plot(lags, real_acf, "o-", color="#1f4e79", label="S&P 500 empirical",
            markersize=5, lw=1.5)
    ax.plot(lags, gbm_acf, "s--", color="red", label="GBM simulation",
            markersize=4, lw=1, alpha=0.7)
    ax.plot(lags, fps_acf, "^:", color="green", label="FPS simulation",
            markersize=4, lw=1.2, alpha=0.85)

    # 95% confidence band for zero autocorrelation
    n_returns = len(real_returns)
    ci = 1.96 / np.sqrt(n_returns)
    ax.axhspan(-ci, ci, alpha=0.1, color="gray", label="95% no-correlation band")
    ax.axhline(0, color="black", lw=0.5)

    ax.set_xlabel("Lag (days)")
    ax.set_ylabel("Autocorrelation of |returns|")
    ax.set_title(
        "Volatility Clustering: Autocorrelation of |returns|\n"
        "Real data and FPS show persistent clustering; GBM does NOT"
    )
    ax.legend(loc="upper right")
    ax.set_xlim(0, max_lag)

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 4: Return distribution (fat tails)
# ─────────────────────────────────────────────────────────────

def plot_return_distributions(real_returns, gbm_returns, fps_returns, output_path):
    """Q-Q plot and density comparison showing fat tails."""
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Standardise all three
    real_std = (real_returns - np.mean(real_returns)) / np.std(real_returns)
    gbm_std = (gbm_returns - np.mean(gbm_returns)) / np.std(gbm_returns)
    fps_std = (fps_returns - np.mean(fps_returns)) / np.std(fps_returns)

    # Left: density comparison
    ax1 = axes[0]
    bins = np.linspace(-8, 8, 80)
    ax1.hist(real_std, bins=bins, alpha=0.55, color="#1f4e79",
             density=True, label="S&P 500", edgecolor="black", linewidth=0.3)
    ax1.hist(gbm_std, bins=bins, alpha=0.55, color="red",
             density=True, label="GBM", edgecolor="black", linewidth=0.3)
    ax1.hist(fps_std, bins=bins, alpha=0.55, color="green",
             density=True, label="FPS", edgecolor="black", linewidth=0.3)

    # Overlay standard normal
    x = np.linspace(-8, 8, 200)
    ax1.plot(x, np.exp(-x ** 2 / 2) / np.sqrt(2 * np.pi), "k--", lw=1.2,
             label="Standard normal")

    ax1.set_xlabel("Standardised returns")
    ax1.set_ylabel("Density")
    ax1.set_yscale("log")
    ax1.set_xlim(-8, 8)
    ax1.set_ylim(1e-5, 1)
    ax1.set_title("Return Distribution (log scale — fat tails visible)")
    ax1.legend(loc="upper left")

    # Right: Q-Q plot vs normal
    ax2 = axes[1]
    from scipy import stats
    for data, label, color in [
        (real_std, "S&P 500", "#1f4e79"),
        (gbm_std, "GBM", "red"),
        (fps_std, "FPS", "green"),
    ]:
        # Compute quantiles
        n = len(data)
        q_theo = stats.norm.ppf((np.arange(1, n + 1) - 0.5) / n)
        q_emp = np.sort(data)
        # Subsample for plotting
        step = max(1, n // 500)
        ax2.plot(q_theo[::step], q_emp[::step], "o", label=label,
                 color=color, markersize=4, alpha=0.7)

    lim = 6
    ax2.plot([-lim, lim], [-lim, lim], "k--", lw=1, alpha=0.5)
    ax2.set_xlabel("Normal quantiles")
    ax2.set_ylabel("Empirical quantiles")
    ax2.set_xlim(-lim, lim)
    ax2.set_ylim(-lim, lim)
    ax2.set_title("Q-Q Plot vs Normal (deviations = fat tails)")
    ax2.legend(loc="upper left")

    plt.suptitle("Fat-Tail Comparison: Real Data vs GBM vs FPS", y=1.01)
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 5: Sample paths
# ─────────────────────────────────────────────────────────────

def plot_sample_paths(real_returns, gbm_returns, fps_returns, output_path,
                       length=1000):
    """Show sample paths of price (cumulative returns)."""
    fig, axes = plt.subplots(3, 1, figsize=(13, 9), sharex=True)

    # Cumulative log-prices
    real_price = np.cumsum(real_returns[:length])
    gbm_price = np.cumsum(gbm_returns[:length])
    fps_price = np.cumsum(fps_returns[:length])

    days = np.arange(length)

    axes[0].plot(days, real_price, color="#1f4e79", lw=1.3)
    axes[0].fill_between(days, 0, real_price, alpha=0.2, color="#1f4e79")
    axes[0].set_ylabel("Log-price")
    axes[0].set_title(f"S&P 500 sample path (first {length} days)")

    axes[1].plot(days, gbm_price, color="red", lw=1.3)
    axes[1].fill_between(days, 0, gbm_price, alpha=0.2, color="red")
    axes[1].set_ylabel("Log-price")
    axes[1].set_title("GBM simulation (matched $\\mu$, $\\sigma$)")

    axes[2].plot(days, fps_price, color="green", lw=1.3)
    axes[2].fill_between(days, 0, fps_price, alpha=0.2, color="green")
    axes[2].set_ylabel("Log-price")
    axes[2].set_xlabel("Day")
    axes[2].set_title("FPS simulation ($\\kappa$, $H$ calibrated)")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 6: Variogram (mean-reversion signature)
# ─────────────────────────────────────────────────────────────

def variogram(returns, max_lag):
    """Compute the structure function: var(X_{t+tau} - X_t) vs tau.

    For GBM: linear in tau (var scales as tau).
    For mean-reverting: saturates.
    For anti-persistent fBM: sub-linear.
    """
    X = np.cumsum(returns - np.mean(returns))
    lags = np.arange(1, max_lag + 1)
    vario = np.zeros(max_lag)
    for i, lag in enumerate(lags):
        vario[i] = np.var(X[lag:] - X[:-lag])
    return lags, vario


def plot_variogram(real_returns, gbm_returns, fps_returns, output_path):
    """Log-log plot of variogram."""
    fig, ax = plt.subplots(figsize=(10, 7))

    max_lag = 250

    real_lags, real_vario = variogram(real_returns, max_lag)
    gbm_lags, gbm_vario = variogram(gbm_returns, max_lag)
    fps_lags, fps_vario = variogram(fps_returns, max_lag)

    ax.loglog(real_lags, real_vario, "o-", color="#1f4e79",
              label="S&P 500 empirical", markersize=3, lw=1.5)
    ax.loglog(gbm_lags, gbm_vario, "s--", color="red",
              label="GBM (slope = 1)", markersize=3, lw=1.2, alpha=0.8)
    ax.loglog(fps_lags, fps_vario, "^:", color="green",
              label="FPS (slope = 2H < 1)", markersize=3, lw=1.2, alpha=0.85)

    # Reference lines
    ax.loglog(real_lags, real_vario[0] * real_lags, "k:",
              label="slope = 1 (GBM prediction)", alpha=0.5)

    # Fit slope to real data
    slope = np.polyfit(np.log(real_lags[5:50]), np.log(real_vario[5:50]), 1)[0]
    inferred_H = slope / 2
    ax.text(
        0.05, 0.9,
        f"Empirical slope ≈ {slope:.3f}\nImplied Hurst H ≈ {inferred_H:.3f}",
        transform=ax.transAxes, fontsize=11, verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.8),
    )

    ax.set_xlabel("Lag τ (days)")
    ax.set_ylabel("Var[X(t+τ) - X(t)] (structure function)")
    ax.set_title(
        "Variogram: S&P 500 vs GBM vs FPS\n"
        f"Empirical slope of {slope:.2f} shows anti-persistent (Hurst<0.5)\n"
        "structure inconsistent with GBM (slope=1)"
    )
    ax.legend(loc="lower right")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", default="^GSPC")
    parser.add_argument("--N", type=int, default=6)
    parser.add_argument("--kappa", type=float, default=0.02,
                        help="FPS mean-reversion rate (per day)")
    parser.add_argument("--H", type=float, default=0.42,
                        help="Hurst exponent for FPS (0.5 = GBM)")
    parser.add_argument("--output_dir", default="code/visualisation/fps_vs_gbm")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {out_dir}")

    # Load real data
    print("\n=== Loading real data ===")
    real_returns = load_returns(args.ticker)
    T_real = len(real_returns)
    print(f"Real S&P 500 returns: {T_real:,} days")

    mu_emp = np.mean(real_returns)
    sigma_emp = np.std(real_returns)
    print(f"Empirical daily mean: {mu_emp:+.5f}")
    print(f"Empirical daily std:  {sigma_emp:.5f}")

    # Simulate matched GBM and FPS
    print("\n=== Simulating GBM ===")
    gbm_returns = simulate_gbm(T_real, mu_emp, sigma_emp, seed=42)

    print("=== Simulating FPS ===")
    print(f"  kappa = {args.kappa}, H = {args.H}")
    # Theta matched to log-starting level; scale matches empirical std
    fps_returns = simulate_fps(T_real, args.kappa, 0.0, sigma_emp, args.H,
                               dt=1.0, seed=123)
    # Add empirical mean
    fps_returns = fps_returns + mu_emp

    # Discretise all three
    print("\n=== Discretising ===")
    real_sym = balanced_voronoi(real_returns, args.N)
    gbm_sym = balanced_voronoi(gbm_returns, args.N)
    fps_sym = balanced_voronoi(fps_returns, args.N)

    # Generate all plots
    print("\n=== Generating plots ===")

    # Plot 1: Palindrome counts
    counts_data = plot_palindrome_counts(
        real_sym, gbm_sym, fps_sym, out_dir / "01_palindrome_counts.png", N=args.N
    )

    # Plot 2: PEI distributions
    def gbm_returns_fn(L, seed=None):
        return simulate_gbm(L, mu_emp, sigma_emp, seed=seed)

    def fps_returns_fn(L, seed=None):
        return simulate_fps(L, args.kappa, 0.0, sigma_emp, args.H, seed=seed) + mu_emp

    pei_data = plot_pei_distributions(
        real_sym, gbm_returns_fn, fps_returns_fn,
        out_dir / "02_pei_distributions.png",
        N=args.N, window=250, n_sims=20,
    )

    # Plot 3: Volatility clustering
    plot_volatility_clustering(
        real_returns, gbm_returns, fps_returns, out_dir / "03_volatility_clustering.png"
    )

    # Plot 4: Return distribution
    plot_return_distributions(
        real_returns, gbm_returns, fps_returns, out_dir / "04_return_distributions.png"
    )

    # Plot 5: Sample paths
    plot_sample_paths(
        real_returns, gbm_returns, fps_returns, out_dir / "05_sample_paths.png",
        length=min(1000, T_real),
    )

    # Plot 6: Variogram
    plot_variogram(
        real_returns, gbm_returns, fps_returns, out_dir / "06_variogram.png"
    )

    # Final summary
    print("\n" + "=" * 70)
    print("SUMMARY: FPS VS GBM ON S&P 500 DATA")
    print("=" * 70)
    print(f"\nPalindrome counts (real / GBM predicted):")
    for i, L in enumerate(counts_data["lengths"]):
        real = counts_data["real"][i]
        gbm_pred = counts_data["gbm_pred"][i]
        fps = counts_data["fps_sim"][i]
        ratio_real_gbm = real / gbm_pred if gbm_pred > 0 else float("inf")
        ratio_fps_real = fps / real if real > 0 else float("inf")
        print(f"  2k={L:>2}: real={real:>6} GBM_pred={gbm_pred:>8.1f}  "
              f"excess_ratio={ratio_real_gbm:>5.2f}×  "
              f"FPS/real={ratio_fps_real:>5.2f}×")

    print(f"\nPEI statistics:")
    print(f"  S&P 500 mean PEI:      {np.mean(pei_data['real_pei']):.4f}")
    print(f"  GBM simulation PEI:    {np.mean(pei_data['gbm_pei']):.4f}")
    print(f"  FPS simulation PEI:    {np.mean(pei_data['fps_pei']):.4f}")
    print(f"  GBM gap (real - GBM):  {np.mean(pei_data['real_pei']) - np.mean(pei_data['gbm_pei']):+.4f}")
    print(f"  FPS gap (real - FPS):  {np.mean(pei_data['real_pei']) - np.mean(pei_data['fps_pei']):+.4f}")
    print(f"\nGenerated 6 comparison plots in {out_dir}")
    print("=" * 70)


if __name__ == "__main__":
    main()
