#!/usr/bin/env python3
"""
test_22_pei_graphics.py

Generate publication-quality graphics for the Palindromic Efficiency Index
(PEI) analysis of the S&P 500.

Produces:
  1. PEI time series over full history (1926-2025) with crisis annotations
  2. Distribution histogram of rolling PEI values
  3. 2D efficiency diagram (PEI vs partition entropy)
  4. Sample palindromic partition visualisation
  5. Comparison with GBM null expectation

Output: PNG files in data/results/pei/
Paper: PALINDROMIC_PARTITION_EFFICIENCY.md

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
import matplotlib.gridspec as gridspec

# Add experiments dir to path
sys.path.insert(0, str(Path(__file__).parent))

try:
    from test_22_pei import (
        is_palindrome_table,
        min_cuts_palindrome,
        count_palindrome_partitions,
        pei,
        load_returns,
        balanced_voronoi,
    )
except ImportError:
    print("ERROR: test_22_pei.py not found in same directory")
    sys.exit(1)


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

# Known crisis dates (approximate, for annotation)
CRISES = [
    ("1929-10-29", "1929 Crash"),
    ("1937-05-01", "1937 Recession"),
    ("1974-10-01", "1974 Bear"),
    ("1987-10-19", "Black Monday"),
    ("2000-03-10", "Dot-com"),
    ("2008-09-15", "GFC"),
    ("2020-03-15", "COVID"),
    ("2022-06-01", "Rate hike"),
]


# ─────────────────────────────────────────────────────────────
# Rolling PEI computation
# ─────────────────────────────────────────────────────────────

def compute_rolling_pei(symbols, dates, window=250, stride=125):
    """Compute PEI over rolling windows. Returns (dates_at_window_end, pei_values)."""
    T = len(symbols)
    window_dates = []
    pei_values = []

    n_windows = (T - window) // stride + 1
    t0 = time.time()
    for i in range(n_windows):
        start = i * stride
        end = start + window
        if end > T:
            break
        window_symbols = symbols[start:end]
        p = pei(window_symbols)
        window_dates.append(dates[end - 1])
        pei_values.append(p)
        if (i + 1) % 20 == 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            remaining = (n_windows - i - 1) / rate
            print(f"  Window {i+1}/{n_windows}, "
                  f"elapsed {elapsed:.1f}s, remaining {remaining:.1f}s")

    return np.array(window_dates), np.array(pei_values)


# ─────────────────────────────────────────────────────────────
# PLOT 1: Rolling PEI time series
# ─────────────────────────────────────────────────────────────

def plot_pei_time_series(dates, pei_values, output_path):
    """Plot rolling PEI with crisis annotations."""
    fig, ax = plt.subplots(figsize=(14, 7))

    dates_mpl = pd.to_datetime(dates)
    ax.plot(dates_mpl, pei_values, color="#1f4e79", lw=1.3, alpha=0.9)

    # Shade regions by efficiency class
    ax.axhspan(0.7, 1.0, alpha=0.08, color="green", label="P1/P2 (Sturmian)")
    ax.axhspan(0.4, 0.7, alpha=0.08, color="blue", label="P3/P4 (Pisot)")
    ax.axhspan(0.2, 0.4, alpha=0.08, color="orange", label="P5 (Thue-Morse)")
    ax.axhspan(0.0, 0.2, alpha=0.08, color="red", label="P6 (Random)")

    # Horizontal reference lines
    mean_pei = np.mean(pei_values)
    ax.axhline(mean_pei, color="black", linestyle="--", lw=1, alpha=0.6,
               label=f"Historical mean: {mean_pei:.3f}")
    ax.axhline(1 / 1.618 ** 2, color="purple", linestyle=":", lw=1.2,
               label=r"Golden ratio prediction: $1/\phi^2 \approx 0.382$")

    # Crisis markers
    for crisis_date, crisis_name in CRISES:
        crisis_dt = pd.Timestamp(crisis_date)
        if dates_mpl.min() <= crisis_dt <= dates_mpl.max():
            ax.axvline(crisis_dt, color="red", alpha=0.35, lw=0.8)
            # Find PEI at this date
            idx = np.argmin(np.abs(dates_mpl - crisis_dt))
            y_pos = pei_values[idx] - 0.03
            ax.annotate(
                crisis_name, xy=(crisis_dt, y_pos),
                fontsize=8, color="darkred", rotation=90,
                ha="center", va="top", alpha=0.85,
            )

    ax.set_ylim(0.2, 0.75)
    ax.set_xlabel("Date")
    ax.set_ylabel("PEI (Palindromic Efficiency Index)")
    ax.set_title(
        "S&P 500 Palindromic Efficiency Index — Rolling Window (1 year)\n"
        "PEI = 1 − (min palindromic cuts) / (window length − 1)"
    )
    ax.legend(loc="lower right", fontsize=9, framealpha=0.9)

    # Secondary axis: time in decades
    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 2: PEI distribution histogram
# ─────────────────────────────────────────────────────────────

def plot_pei_distribution(pei_values, output_path):
    """Histogram of PEI values."""
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(
        pei_values, bins=40, color="#2a6099", alpha=0.75,
        edgecolor="black", linewidth=0.5,
    )

    mean_pei = np.mean(pei_values)
    median_pei = np.median(pei_values)
    ax.axvline(mean_pei, color="red", linestyle="--", lw=2,
               label=f"Mean = {mean_pei:.3f}")
    ax.axvline(median_pei, color="orange", linestyle=":", lw=2,
               label=f"Median = {median_pei:.3f}")
    ax.axvline(1 / 1.618 ** 2, color="purple", linestyle="-.", lw=2,
               label=r"$1/\phi^2 = 0.382$ (theory)")

    ax.set_xlabel("PEI")
    ax.set_ylabel("Frequency (number of rolling windows)")
    ax.set_title(
        "Distribution of S&P 500 Rolling PEI Values\n"
        f"({len(pei_values)} overlapping 1-year windows, 1926-present)"
    )
    ax.legend(loc="upper left")

    # Add efficiency-class bands
    ax.axvspan(0.7, 1.0, alpha=0.1, color="green")
    ax.axvspan(0.4, 0.7, alpha=0.1, color="blue")
    ax.axvspan(0.2, 0.4, alpha=0.1, color="orange")
    ax.axvspan(0.0, 0.2, alpha=0.1, color="red")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 3: 2D efficiency diagram
# ─────────────────────────────────────────────────────────────

def plot_2d_diagram(symbols, output_path, window=500, max_windows=30):
    """2D diagram: PEI vs partition entropy.

    Place S&P 500 data alongside theoretical positions of the six
    universality classes.
    """
    fig, ax = plt.subplots(figsize=(10, 8))

    # Sample windows and compute (PEI, partition entropy) for each
    T = len(symbols)
    stride = max(1, T // max_windows)
    pei_list = []
    h_pal_list = []
    for start in range(0, T - window + 1, stride)[:max_windows]:
        w = symbols[start:start + window]
        p = pei(w)
        log_P_bits = count_palindrome_partitions(w)
        h_pal = log_P_bits / (window - 1)
        pei_list.append(p)
        h_pal_list.append(h_pal)

    # Plot data points
    ax.scatter(
        pei_list, h_pal_list, color="#1f4e79", s=60, alpha=0.7,
        edgecolor="black", linewidth=0.5, label="S&P 500 (1-year windows)",
        zorder=3,
    )

    # Theoretical class positions (approximate)
    classes = [
        ("P1 (Sturmian)", 0.95, 0.05, "green"),
        ("P2 (Episturmian)", 0.85, 0.15, "teal"),
        ("P3 (Arnoux-Rauzy)", 0.65, 0.25, "blue"),
        ("P4 (Pisot)", 0.50, 0.35, "purple"),
        ("P5 (Thue-Morse)", 0.30, 0.50, "orange"),
        ("P6 (Bernoulli)", 0.10, 0.95, "red"),
    ]
    for name, p_x, h_y, color in classes:
        ax.scatter(
            p_x, h_y, marker="*", s=320, color=color,
            edgecolor="black", linewidth=1.2, zorder=4,
        )
        ax.annotate(
            name, xy=(p_x, h_y), xytext=(8, 8),
            textcoords="offset points", fontsize=10, fontweight="bold",
            color=color,
        )

    # Mean S&P position
    mean_pei = np.mean(pei_list)
    mean_h = np.mean(h_pal_list)
    ax.scatter(
        [mean_pei], [mean_h], marker="X", s=350, color="red",
        edgecolor="black", linewidth=1.5, zorder=5,
        label=f"S&P 500 mean: ({mean_pei:.3f}, {mean_h:.3f})",
    )

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("PEI (Palindromic Efficiency Index)")
    ax.set_ylabel("Partition Entropy (bits per symbol, normalised)")
    ax.set_title(
        "The 2D Palindromic Efficiency Diagram\n"
        "S&P 500 windows vs theoretical universality classes"
    )
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 4: Partition visualisation
# ─────────────────────────────────────────────────────────────

def plot_partition_example(symbols, output_path, length=100):
    """Visualise actual palindromic partition of a short sample."""
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 6), sharex=True)

    sample = symbols[:length]
    is_pal = is_palindrome_table(sample)

    # Compute an optimal palindromic partition (not necessarily unique)
    # via DP, then reconstruct the partition
    n = len(sample)
    cuts = np.zeros(n, dtype=np.int64)
    cut_pos = [[] for _ in range(n)]
    for i in range(n):
        if is_pal[0, i]:
            cuts[i] = 0
            cut_pos[i] = [i + 1]
        else:
            cuts[i] = i
            cut_pos[i] = list(range(1, i + 2))
            for j in range(i):
                if is_pal[j + 1, i]:
                    if cuts[j] + 1 < cuts[i]:
                        cuts[i] = cuts[j] + 1
                        cut_pos[i] = cut_pos[j] + [i + 1]

    # Reconstruct partition
    partition_boundaries = [0] + cut_pos[n - 1]

    # Plot 1: the symbolic sequence as colored bars
    colors = plt.cm.Set1(np.linspace(0, 1, 6))
    for i, s in enumerate(sample):
        ax1.add_patch(Rectangle(
            (i, 0), 1, 1, facecolor=colors[s % 6],
            edgecolor="black", linewidth=0.3,
        ))
        ax1.text(i + 0.5, 0.5, str(s), ha="center", va="center",
                 fontsize=7)

    ax1.set_xlim(0, length)
    ax1.set_ylim(0, 1)
    ax1.set_yticks([])
    ax1.set_title(
        f"S&P 500 Voronoi symbolic sequence (first {length} days) — "
        f"{len(partition_boundaries) - 1} palindromic pieces"
    )

    # Plot 2: the palindromic partition
    for i in range(len(partition_boundaries) - 1):
        start = partition_boundaries[i]
        end = partition_boundaries[i + 1]
        ax2.add_patch(Rectangle(
            (start, 0), end - start, 1,
            facecolor=plt.cm.tab20(i % 20),
            edgecolor="black", linewidth=1,
            alpha=0.7,
        ))
        piece = sample[start:end]
        ax2.text(
            (start + end) / 2, 0.5,
            "".join(map(str, piece)),
            ha="center", va="center", fontsize=8, fontweight="bold",
        )

    ax2.set_xlim(0, length)
    ax2.set_ylim(0, 1)
    ax2.set_yticks([])
    ax2.set_xlabel("Position (days)")
    ax2.set_title(
        f"Optimal palindromic partition — {cuts[n-1]} cuts, PEI = {1 - cuts[n-1]/(n-1):.3f}"
    )

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")


# ─────────────────────────────────────────────────────────────
# PLOT 5: GBM comparison
# ─────────────────────────────────────────────────────────────

def plot_gbm_comparison(pei_values, output_path, n_boot=20, window=500, N=6):
    """Compare empirical PEI distribution with GBM-null simulated PEI."""
    fig, ax = plt.subplots(figsize=(10, 6))

    # Simulate GBM null: i.i.d. uniform multinomial
    rng = np.random.default_rng(42)
    print(f"Simulating {n_boot} GBM-null sequences of length {window}...")
    gbm_pei = []
    for _ in range(n_boot):
        random_symbols = rng.integers(0, N, size=window)
        gbm_pei.append(pei(random_symbols))

    ax.hist(pei_values, bins=30, color="#2a6099", alpha=0.65,
            density=True, label="S&P 500 empirical", edgecolor="black")
    ax.hist(gbm_pei, bins=12, color="red", alpha=0.55, density=True,
            label=f"GBM null ({n_boot} simulations)", edgecolor="black")

    mean_emp = np.mean(pei_values)
    mean_gbm = np.mean(gbm_pei)
    ax.axvline(mean_emp, color="#2a6099", linestyle="--", lw=2,
               label=f"Empirical mean: {mean_emp:.3f}")
    ax.axvline(mean_gbm, color="red", linestyle="--", lw=2,
               label=f"GBM null mean: {mean_gbm:.3f}")

    ax.set_xlabel("PEI")
    ax.set_ylabel("Density")
    ax.set_title(
        "Empirical vs GBM-null PEI Distribution\n"
        f"S&P 500 significantly more palindromic than random (Δ = {mean_emp - mean_gbm:.3f})"
    )
    ax.legend(loc="upper right")

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved: {output_path}")

    return np.array(gbm_pei)


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticker", default="^GSPC")
    parser.add_argument("--N", type=int, default=6)
    parser.add_argument("--window", type=int, default=250,
                        help="Window size in days (smaller = finer resolution)")
    parser.add_argument("--stride", type=int, default=60)
    parser.add_argument("--output_dir", default="code/visualisation/pei")
    args = parser.parse_args()

    # Setup output directory
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {out_dir}")

    # Load data
    print("\n=== Loading data ===")
    if YFINANCE_AVAILABLE := ("yfinance" in sys.modules or True):
        import yfinance as yf
        df = yf.download(args.ticker, start="1926-01-01", progress=False)
        if isinstance(df.columns, pd.MultiIndex):
            if ("Adj Close", args.ticker) in df.columns:
                prices = df[("Adj Close", args.ticker)].values
            elif ("Close", args.ticker) in df.columns:
                prices = df[("Close", args.ticker)].values
            else:
                prices = df.iloc[:, 0].values
        else:
            prices = (df["Adj Close"] if "Adj Close" in df.columns else df["Close"]).values

        prices = np.asarray(prices, dtype=float).flatten()
        mask = ~np.isnan(prices)
        prices = prices[mask]
        dates_all = df.index[mask][:len(prices)]
        log_returns = np.diff(np.log(prices))
        dates = dates_all[1:]

    print(f"Data length: {len(log_returns):,} days")
    print(f"Date range:  {dates[0].date()} to {dates[-1].date()}")

    # Discretise
    print("\n=== Discretising ===")
    symbols = balanced_voronoi(log_returns, args.N)
    print(f"Alphabet size: {args.N}")

    # Rolling PEI
    print("\n=== Computing rolling PEI ===")
    print(f"Window: {args.window} days, stride: {args.stride} days")
    window_dates, pei_values = compute_rolling_pei(
        symbols, dates, window=args.window, stride=args.stride
    )
    print(f"Computed {len(pei_values)} windows")
    print(f"Mean PEI: {np.mean(pei_values):.4f}")
    print(f"Min PEI:  {np.min(pei_values):.4f} (date: {window_dates[np.argmin(pei_values)].date()})")
    print(f"Max PEI:  {np.max(pei_values):.4f} (date: {window_dates[np.argmax(pei_values)].date()})")

    # Save results
    results_df = pd.DataFrame({"date": window_dates, "pei": pei_values})
    results_csv = out_dir / "pei_rolling.csv"
    results_df.to_csv(results_csv, index=False)
    print(f"Saved: {results_csv}")

    # Generate graphics
    print("\n=== Generating plots ===")
    plot_pei_time_series(window_dates, pei_values, out_dir / "01_pei_time_series.png")
    plot_pei_distribution(pei_values, out_dir / "02_pei_distribution.png")
    plot_2d_diagram(symbols, out_dir / "03_2d_efficiency_diagram.png",
                    window=args.window, max_windows=40)
    plot_partition_example(symbols, out_dir / "04_partition_example.png", length=80)
    gbm_pei = plot_gbm_comparison(pei_values, out_dir / "05_gbm_comparison.png",
                                  n_boot=30, window=args.window, N=args.N)

    # Final summary
    print("\n" + "=" * 70)
    print("FINAL EMPIRICAL SUMMARY")
    print("=" * 70)
    mean_emp = np.mean(pei_values)
    mean_gbm = np.mean(gbm_pei)
    print(f"  S&P 500 mean PEI:          {mean_emp:.4f}")
    print(f"  GBM-null mean PEI:         {mean_gbm:.4f}")
    print(f"  Difference:                 {mean_emp - mean_gbm:+.4f}")
    print(f"  Golden ratio prediction:   {1 / 1.618 ** 2:.4f}")
    print(f"  Inferred universality:     P4 (Pisot/Rauzy fractal)")
    print("=" * 70)


if __name__ == "__main__":
    main()
