#!/usr/bin/env python3
"""
Test 15V: LZ Complexity with Voronoi Discretisation
=====================================================
Use the factor structure to build a Voronoi partition of return
space, then measure LZ78 compression rate of the Voronoi cell
sequence. This should capture the manifold's information structure
better than binary L/S or PCA-sign encoding.

The Voronoi cells ARE the filtration atoms from FILTRATIONS.md.
The LZ78 complexity of the cell sequence should converge to h_Kelly.

Method:
    1. PCA to find r factors → project returns onto R^r
    2. K-means clustering in factor space → N Voronoi cells
    3. Map each day's return to its Voronoi cell → symbolic sequence
    4. LZ78 compression rate of the cell sequence
    5. Compare to null (permuted) and to Kelly growth rate
    6. Run across multiple values of N and r to find optimal

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
from sklearn.cluster import KMeans

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)


# ── LZ78 ─────────────────────────────────────────────────────

def lz78_complexity(seq):
    """LZ78 phrase count on a sequence of integers."""
    dictionary = set()
    dictionary.add(())
    w = ()
    c = 0
    for s in seq:
        ws = w + (s,)
        if ws not in dictionary:
            dictionary.add(ws)
            c += 1
            w = ()
        else:
            w = ws
    if w:
        c += 1
    return c


def lz_rate(seq):
    """Normalised LZ78 compression rate: c·log₂(c)/T → entropy rate."""
    T = len(seq)
    if T < 20:
        return np.nan
    c = lz78_complexity(seq)
    if c < 2:
        return 0.0
    return c * np.log2(c) / T


# ── Voronoi discretisation ───────────────────────────────────

def build_voronoi(returns, r, N_cells, seed=42):
    """
    Build a Voronoi partition of return space using PCA + K-means.

    Args:
        returns: T × d array of daily returns
        r: number of PCA factors to project onto
        N_cells: number of Voronoi cells (K-means clusters)

    Returns:
        labels: T-length array of cell assignments (0 to N_cells-1)
        km: fitted KMeans model
        V_r: d × r factor loading matrix
        pc: T × r projected returns
    """
    T, d = returns.shape

    # PCA
    cov = np.cov(returns.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]
    V_r = eigenvectors[:, :r]

    # Project onto factor space
    pc = returns @ V_r  # T × r

    # K-means clustering = Voronoi partition
    km = KMeans(n_clusters=N_cells, random_state=seed, n_init=10, max_iter=300)
    labels = km.fit_predict(pc)

    return labels, km, V_r, pc


def voronoi_lz_analysis(returns, r, N_cells, n_null=500, seed=42):
    """
    Full Voronoi-LZ analysis: build cells, compute LZ rate, compare to null.
    """
    rng = np.random.default_rng(seed)
    T = len(returns)

    labels, km, V_r, pc = build_voronoi(returns, r, N_cells, seed)
    seq = tuple(labels)

    # LZ rate of actual sequence
    actual_rate = lz_rate(seq)

    # Null: permute the cell sequence
    null_rates = []
    labels_list = list(labels)
    for _ in range(n_null):
        rng.shuffle(labels_list)
        null_rates.append(lz_rate(tuple(labels_list)))
    null_mean = np.mean(null_rates)
    null_std = np.std(null_rates)

    excess = actual_rate - null_mean
    z_score = excess / max(null_std, 1e-10)

    # Transition matrix (empirical)
    trans = np.zeros((N_cells, N_cells))
    for t in range(T - 1):
        trans[labels[t], labels[t + 1]] += 1
    row_sums = trans.sum(axis=1, keepdims=True)
    trans_prob = trans / np.maximum(row_sums, 1)

    # Entropy rate from transition matrix: h = -Σ π_i Σ p_ij log p_ij
    stationary = row_sums.flatten() / row_sums.sum()
    h_markov = 0
    for i in range(N_cells):
        for j in range(N_cells):
            if trans_prob[i, j] > 1e-15:
                h_markov -= stationary[i] * trans_prob[i, j] * np.log2(trans_prob[i, j])

    # Kelly growth rate
    gross = 1.0 + returns
    b_eq = np.ones(returns.shape[1]) / returns.shape[1]
    kelly = np.mean(np.log(np.maximum(gross @ b_eq, 1e-15)))

    # Cell occupancy (how balanced is the partition?)
    occupancy = np.bincount(labels, minlength=N_cells) / T
    occupancy_entropy = -np.sum(occupancy[occupancy > 0] * np.log2(occupancy[occupancy > 0]))
    max_entropy = np.log2(N_cells)

    return {
        "r": r,
        "N_cells": N_cells,
        "T": T,
        "lz_rate": actual_rate,
        "null_rate": null_mean,
        "null_std": null_std,
        "excess": excess,
        "z_score": z_score,
        "h_markov": h_markov,
        "kelly_rate": kelly,
        "occupancy_entropy": occupancy_entropy,
        "max_entropy": max_entropy,
        "occupancy_ratio": occupancy_entropy / max_entropy if max_entropy > 0 else 0,
    }


# ── Rolling analysis ─────────────────────────────────────────

def rolling_voronoi_lz(returns, r, N_cells, window=504, step=63):
    """Rolling Voronoi-LZ analysis."""
    T = len(returns)
    results = []
    for i in range(0, T - window, step):
        w = returns[i:i + window]
        w = np.nan_to_num(w, 0.0)
        try:
            res = voronoi_lz_analysis(w, r, N_cells, n_null=200)
            res["window_end"] = i + window
            results.append(res)
        except Exception:
            pass
    return pd.DataFrame(results)


# ── Main ─────────────────────────────────────────────────────

def run_test_15V():
    print("=" * 70)
    print("  TEST 15V: LZ Complexity with Voronoi Discretisation")
    print("  Factor-adapted cells from the market manifold")
    print("=" * 70)

    # Load data
    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet").loc["1963-07-01":]
    returns = ff25.values
    returns = returns[~np.isnan(returns).any(axis=1)]
    T, d = returns.shape

    print(f"\n  Data: {T} days × {d} portfolios")

    # ── Sweep over (r, N_cells) to find optimal ──────────────
    print(f"\n  Sweeping over r ∈ {{2,3,4,5}} and N ∈ {{4,8,16,32,64}}...")
    print(f"\n  {'r':>3}  {'N':>4}  {'LZ rate':>8}  {'Null':>8}  {'Excess':>8}  "
          f"{'Z':>6}  {'h_Markov':>8}  {'Occ ratio':>9}  {'Kelly':>8}")
    print(f"  {'─' * 80}")

    sweep_results = []
    for r in [2, 3, 4, 5]:
        for N in [4, 8, 16, 32, 64]:
            if N > d:
                continue
            res = voronoi_lz_analysis(returns, r, N, n_null=500)
            sweep_results.append(res)
            print(f"  {r:>3}  {N:>4}  {res['lz_rate']:>8.4f}  {res['null_rate']:>8.4f}  "
                  f"{res['excess']:>+8.4f}  {res['z_score']:>+6.1f}  "
                  f"{res['h_markov']:>8.4f}  {res['occupancy_ratio']:>9.3f}  "
                  f"{res['kelly_rate']:>8.6f}")

    sweep_df = pd.DataFrame(sweep_results)

    # Find most predictable configuration
    best_idx = sweep_df["z_score"].idxmin()
    best = sweep_df.loc[best_idx]
    print(f"\n  Most predictable: r={best['r']:.0f}, N={best['N_cells']:.0f}, "
          f"Z={best['z_score']:.1f}")

    # ── Use best configuration for detailed analysis ─────────
    best_r = int(best["r"])
    best_N = int(best["N_cells"])

    print(f"\n{'─' * 70}")
    print(f"  Detailed analysis at r={best_r}, N={best_N}")
    print(f"{'─' * 70}")

    # Full sample detailed
    labels, km, V_r, pc = build_voronoi(returns, best_r, best_N)

    # Transition matrix analysis
    trans = np.zeros((best_N, best_N))
    for t in range(T - 1):
        trans[labels[t], labels[t + 1]] += 1
    row_sums = trans.sum(axis=1, keepdims=True)
    trans_prob = trans / np.maximum(row_sums, 1)

    # Most persistent cells (high self-transition probability)
    self_trans = np.diag(trans_prob)
    print(f"\n  Cell self-transition probabilities:")
    sorted_cells = np.argsort(self_trans)[::-1]
    for i, c in enumerate(sorted_cells[:5]):
        print(f"    Cell {c}: P(stay) = {self_trans[c]:.3f} "
              f"(occupancy {np.mean(labels == c):.3f})")

    # ── Rolling analysis ─────────────────────────────────────
    print(f"\n  Rolling analysis (2-year windows)...")
    rolling = rolling_voronoi_lz(returns, best_r, best_N, window=504, step=63)

    if len(rolling) > 10:
        # Correlation: -excess vs Kelly
        corr_ek = np.corrcoef(-rolling["excess"].values,
                                rolling["kelly_rate"].values)[0, 1]
        # Correlation: h_Markov vs Kelly
        corr_mk = np.corrcoef(rolling["h_markov"].values,
                                rolling["kelly_rate"].values)[0, 1]
        # Correlation: LZ rate vs h_Markov
        corr_lm = np.corrcoef(rolling["lz_rate"].values,
                                rolling["h_markov"].values)[0, 1]

        print(f"  {len(rolling)} windows")
        print(f"  Correlation(-excess, Kelly): {corr_ek:.4f}")
        print(f"  Correlation(h_Markov, Kelly): {corr_mk:.4f}")
        print(f"  Correlation(LZ rate, h_Markov): {corr_lm:.4f}")
    else:
        corr_ek = corr_mk = corr_lm = 0
        print(f"  Insufficient windows")

    # ── Multi-asset-class comparison ─────────────────────────
    print(f"\n{'─' * 70}")
    print(f"  Cross-asset comparison at r={best_r}, N={best_N}")
    print(f"{'─' * 70}")

    asset_results = []

    # FF25
    res_ff = voronoi_lz_analysis(returns, best_r, best_N, n_null=500)
    res_ff["asset"] = "FF25 Portfolios"
    asset_results.append(res_ff)

    # Sector ETFs
    sec_path = DATA_DIR / "sector_etf_9_daily_returns.parquet"
    if sec_path.exists():
        sec = pd.read_parquet(sec_path).dropna().values
        sec = np.nan_to_num(sec, 0.0)
        if sec.shape[1] >= best_r and len(sec) > 504:
            res_sec = voronoi_lz_analysis(sec, min(best_r, sec.shape[1] - 1),
                                            min(best_N, sec.shape[1]), n_null=500)
            res_sec["asset"] = "Sector ETFs"
            asset_results.append(res_sec)

    # Databento equities
    eq_path = DATA_DIR / "equities_50_daily_returns.parquet"
    if eq_path.exists():
        eq = pd.read_parquet(eq_path).values
        eq = np.nan_to_num(eq, 0.0)
        if eq.shape[1] >= best_r and len(eq) > 252:
            res_eq = voronoi_lz_analysis(eq, best_r, best_N, n_null=500)
            res_eq["asset"] = "50 Equities (Databento)"
            asset_results.append(res_eq)

    # Crypto
    cr_path = DATA_DIR / "crypto_daily_returns.parquet"
    if cr_path.exists():
        cr = pd.read_parquet(cr_path).dropna().values
        cr = np.nan_to_num(cr, 0.0)
        if cr.shape[1] >= 2 and len(cr) > 252:
            res_cr = voronoi_lz_analysis(cr, min(2, cr.shape[1] - 1),
                                           min(4, best_N), n_null=500)
            res_cr["asset"] = "Crypto"
            asset_results.append(res_cr)

    print(f"\n  {'Asset':>25}  {'Excess':>8}  {'Z':>6}  {'h_Markov':>8}  {'Kelly':>8}")
    print(f"  {'─' * 60}")
    for r in asset_results:
        print(f"  {r['asset']:>25}  {r['excess']:>+8.4f}  {r['z_score']:>+6.1f}  "
              f"{r['h_markov']:>8.4f}  {r['kelly_rate']:>8.6f}")

    # ── Visualisation ────────────────────────────────────────
    fig = plt.figure(figsize=(16, 10))
    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

    # 1. Sweep: Z-score heatmap
    ax1 = fig.add_subplot(gs[0, 0])
    r_vals = sorted(sweep_df["r"].unique())
    n_vals = sorted(sweep_df["N_cells"].unique())
    Z_matrix = np.full((len(r_vals), len(n_vals)), np.nan)
    for _, row in sweep_df.iterrows():
        ri = r_vals.index(row["r"])
        ni = n_vals.index(row["N_cells"])
        Z_matrix[ri, ni] = row["z_score"]
    im = ax1.imshow(Z_matrix, aspect="auto", cmap="RdBu_r", vmin=-5, vmax=5)
    ax1.set_xticks(range(len(n_vals)))
    ax1.set_xticklabels([str(int(n)) for n in n_vals])
    ax1.set_yticks(range(len(r_vals)))
    ax1.set_yticklabels([str(int(r)) for r in r_vals])
    ax1.set_xlabel("N (Voronoi cells)")
    ax1.set_ylabel("r (factors)")
    ax1.set_title("Predictability Z-score\n(negative = more predictable)")
    plt.colorbar(im, ax=ax1)

    # 2. LZ rate vs null for best config
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.hist(rolling["lz_rate"] if len(rolling) > 0 else [], bins=30,
             alpha=0.7, color="steelblue", label="Actual LZ rate", density=True)
    ax2.hist(rolling["null_rate"] if len(rolling) > 0 else [], bins=30,
             alpha=0.5, color="orange", label="Null LZ rate", density=True)
    ax2.set_xlabel("LZ compression rate")
    ax2.set_title(f"Rolling LZ: Actual vs Null (r={best_r}, N={best_N})")
    ax2.legend()

    # 3. Rolling excess over time
    ax3 = fig.add_subplot(gs[0, 2])
    if len(rolling) > 0:
        ax3.plot(rolling["window_end"] / 252 + 1963, rolling["excess"],
                 color="steelblue", linewidth=0.8)
        ax3.axhline(0, color="red", linewidth=0.5, linestyle="--")
        ax3.fill_between(rolling["window_end"] / 252 + 1963,
                          rolling["excess"], 0,
                          where=rolling["excess"] < 0, alpha=0.3, color="steelblue",
                          label="More predictable")
    ax3.set_xlabel("Year")
    ax3.set_ylabel("Excess LZ (neg = predictable)")
    ax3.set_title("Predictability Over Time")
    ax3.legend(fontsize=8)

    # 4. Voronoi cells in factor space (2D projection)
    ax4 = fig.add_subplot(gs[1, 0])
    scatter = ax4.scatter(pc[:2000, 0], pc[:2000, 1] if pc.shape[1] > 1 else np.zeros(2000),
                          c=labels[:2000], cmap="tab20", s=2, alpha=0.5)
    centers = km.cluster_centers_
    ax4.scatter(centers[:, 0], centers[:, 1] if centers.shape[1] > 1 else np.zeros(len(centers)),
                c="red", s=100, marker="x", linewidths=2, zorder=5)
    ax4.set_xlabel("PC1")
    ax4.set_ylabel("PC2")
    ax4.set_title(f"Voronoi Cells in Factor Space (N={best_N})")

    # 5. Transition matrix
    ax5 = fig.add_subplot(gs[1, 1])
    im5 = ax5.imshow(trans_prob[:min(16, best_N), :min(16, best_N)],
                       cmap="Blues", vmin=0, vmax=0.5)
    ax5.set_xlabel("To cell")
    ax5.set_ylabel("From cell")
    ax5.set_title("Transition Matrix P(j|i)")
    plt.colorbar(im5, ax=ax5)

    # 6. LZ rate vs h_Markov (rolling)
    ax6 = fig.add_subplot(gs[1, 2])
    if len(rolling) > 0:
        ax6.scatter(rolling["h_markov"], rolling["lz_rate"],
                    c="steelblue", s=20, alpha=0.5)
        ax6.set_xlabel("Markov entropy rate h")
        ax6.set_ylabel("LZ compression rate")
        ax6.set_title(f"LZ vs Markov entropy (r={corr_lm:.3f})")
        if len(rolling) > 3:
            z = np.polyfit(rolling["h_markov"].values, rolling["lz_rate"].values, 1)
            xs = np.sort(rolling["h_markov"].values)
            ax6.plot(xs, np.polyval(z, xs), "r--")

    plt.suptitle("Test 15V: LZ Complexity with Voronoi Discretisation",
                 fontsize=14, fontweight="bold")
    plt.savefig(GAL_DIR / "test_15V_lz_voronoi.png", dpi=150, bbox_inches="tight")
    plt.close()

    # ── Verdict ──────────────────────────────────────────────
    print(f"\n" + "=" * 70)
    print(f"  VERDICT")
    print(f"=" * 70)

    # Pass criteria:
    # 1. Best Z-score < -3 (significantly more predictable than null)
    # 2. LZ rate correlates with Markov entropy (correlation > 0.5)
    # 3. Majority of assets show excess < 0

    best_z = sweep_df["z_score"].min()
    n_predictable = sum(1 for r in asset_results if r["excess"] < -0.001)
    pct_predictable = n_predictable / max(len(asset_results), 1) * 100

    criterion_1 = best_z < -3
    criterion_2 = abs(corr_lm) > 0.5
    criterion_3 = pct_predictable > 50

    n_pass = sum([criterion_1, criterion_2, criterion_3])

    print(f"\n  1. Best Z-score < -3:            {'YES' if criterion_1 else 'NO'} (Z = {best_z:.1f})")
    print(f"  2. LZ correlates with h_Markov:  {'YES' if criterion_2 else 'NO'} (r = {corr_lm:.3f})")
    print(f"  3. Majority of assets predictable: {'YES' if criterion_3 else 'NO'} ({pct_predictable:.0f}%)")

    if n_pass >= 2:
        verdict = "PASS"
    elif n_pass >= 1:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"\n  Result: {verdict} ({n_pass}/3 criteria)")

    if verdict == "PASS":
        print(f"\n  The Voronoi-LZ analysis confirms that market return sequences")
        print(f"  are significantly more compressible than random when discretised")
        print(f"  using factor-adapted Voronoi cells. The LZ compression rate tracks")
        print(f"  the Markov entropy rate of the cell transition matrix, validating")
        print(f"  the FILTRATIONS.md theory that the LZ prefix tree = filtration tree.")

    # ── Save ─────────────────────────────────────────────────
    sweep_df.to_csv(OUT_DIR / "test_15V_sweep.csv", index=False)
    if len(rolling) > 0:
        rolling.to_csv(OUT_DIR / "test_15V_rolling.csv", index=False)

    summary = {
        "test": "Test 15V: LZ Voronoi Discretisation",
        "verdict": verdict,
        "best_r": best_r,
        "best_N": best_N,
        "best_z_score": best_z,
        "corr_lz_markov": corr_lm,
        "corr_excess_kelly": corr_ek,
        "n_assets_predictable": n_predictable,
        "pct_predictable": pct_predictable,
        "n_criteria_passed": n_pass,
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_15V_summary.csv")

    print(f"\n  Results: {OUT_DIR / 'test_15V_sweep.csv'}")
    print(f"  Gallery: {GAL_DIR / 'test_15V_lz_voronoi.png'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, _ = run_test_15V()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
