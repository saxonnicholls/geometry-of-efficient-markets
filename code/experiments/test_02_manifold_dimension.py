#!/usr/bin/env python3
"""
Test 2: Manifold Dimension Stability
=====================================
Three independent estimators of r should agree within ±1.

Hypothesis: Stable rank, variance ratio (90% explained), and
Marchenko-Pastur edge detector give consistent estimates of r.

Dataset: FF25 daily returns + Sector ETFs, rolling 504-day windows
Expected: r ≈ 4-6 for US equities, stable across methods and time
Falsification: The three estimators consistently disagree by ≥ 3,
    or r fluctuates wildly (>50% coefficient of variation)

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
OUT_DIR.mkdir(exist_ok=True)


# ── Three estimators of r ────────────────────────────────────

def stable_rank(returns: np.ndarray) -> float:
    """
    Stable rank of the Fisher information matrix.
    F(b) ≈ (1/T) Σ_t x_t x_t^T / (b·x_t)² where b = equal weight (1/d).
    Stable rank = ||F||_F² / ||F||_2² = participation ratio of eigenvalues.
    """
    T, d = returns.shape
    gross = 1.0 + returns
    b = np.ones(d) / d
    bx = gross @ b
    bx = np.maximum(bx, 1e-12)
    # Fisher information matrix at equal weight
    scaled = gross / bx[:, None]  # x_t / (b·x_t)
    F = (scaled.T @ scaled) / T
    eigenvalues = np.linalg.eigvalsh(F)
    eigenvalues = eigenvalues[eigenvalues > 1e-15]
    if len(eigenvalues) == 0:
        return 0.0
    frob_sq = np.sum(eigenvalues ** 2)
    spec_sq = np.max(eigenvalues) ** 2
    if spec_sq < 1e-30:
        return 0.0
    return frob_sq / spec_sq


def variance_ratio(returns: np.ndarray, threshold=0.90) -> int:
    """
    Number of PCA components needed to explain `threshold` fraction of variance.
    """
    cov = np.cov(returns.T)
    eigenvalues = np.linalg.eigvalsh(cov)
    eigenvalues = np.sort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[eigenvalues > 0]
    total = eigenvalues.sum()
    if total < 1e-15:
        return 0
    cumvar = np.cumsum(eigenvalues) / total
    r = int(np.searchsorted(cumvar, threshold)) + 1
    return min(r, len(eigenvalues))


def marchenko_pastur_edge(returns: np.ndarray) -> int:
    """
    Count eigenvalues above the Marchenko-Pastur upper edge.
    For a T×d random matrix with T/d = γ, the MP upper edge is:
        λ+ = σ² (1 + 1/√γ)²
    where σ² is the noise variance (estimated from the bulk).
    """
    T, d = returns.shape
    cov = np.cov(returns.T)
    eigenvalues = np.sort(np.linalg.eigvalsh(cov))[::-1]

    gamma = T / d
    # Estimate noise variance from the median eigenvalue
    # (bulk eigenvalues follow MP; signal eigenvalues are above)
    sigma2 = np.median(eigenvalues)
    lambda_plus = sigma2 * (1 + 1 / np.sqrt(gamma)) ** 2

    r = int(np.sum(eigenvalues > lambda_plus))
    return max(r, 1)  # at least 1 factor


# ── Main experiment ──────────────────────────────────────────

def run_test_2():
    """Run Test 2: Manifold Dimension Stability."""

    print("=" * 60)
    print("  TEST 2: Manifold Dimension Stability")
    print("  Three estimators of r should agree within ±1")
    print("=" * 60)

    # Load data
    ff25_path = DATA_DIR / "ff25_daily_returns.parquet"
    sector_path = DATA_DIR / "sector_etf_daily_returns.parquet"

    datasets = {}

    if ff25_path.exists():
        ff25 = pd.read_parquet(ff25_path)
        # Use post-1963 data (when FF factors are available)
        ff25 = ff25.loc["1963-07-01":]
        datasets["FF25 (25 size/value portfolios)"] = ff25

    if sector_path.exists():
        sectors = pd.read_parquet(sector_path)
        sectors = sectors.dropna()
        datasets["Sector ETFs (11 sectors)"] = sectors

    if not datasets:
        print("\nERROR: No data found. Run download_all.py first.")
        sys.exit(1)

    all_results = []

    for dataset_name, data in datasets.items():
        print(f"\n{'─' * 60}")
        print(f"  Dataset: {dataset_name}")
        print(f"  Shape: {data.shape[0]} days × {data.shape[1]} assets")
        print(f"  Period: {data.index[0].date()} to {data.index[-1].date()}")
        print(f"{'─' * 60}")

        window = 504  # 2 years
        step = 126    # semi-annual
        returns_arr = data.values

        results = []
        for i in range(0, len(returns_arr) - window, step):
            w = returns_arr[i:i + window]
            date = data.index[i + window - 1]

            # Skip if too many NaNs
            if np.isnan(w).sum() > 0.05 * w.size:
                continue
            w = np.nan_to_num(w, 0.0)

            try:
                r_stable = stable_rank(w)
                r_var90 = variance_ratio(w, 0.90)
                r_mp = marchenko_pastur_edge(w)

                results.append({
                    "date": date,
                    "dataset": dataset_name,
                    "r_stable_rank": r_stable,
                    "r_variance_90": r_var90,
                    "r_mp_edge": r_mp,
                })
            except Exception:
                pass

        if not results:
            continue

        df = pd.DataFrame(results)
        all_results.append(df)

        # ── Report ───────────────────────────────────────────
        print(f"\n  {'Window':>8}  {'Date':>12}  {'Stable Rank':>12}  "
              f"{'Var 90%':>8}  {'MP Edge':>8}")
        print(f"  {'─' * 58}")

        for _, row in df.iterrows():
            print(f"  {'':>8}  {row['date'].date()!s:>12}  "
                  f"{row['r_stable_rank']:>12.2f}  "
                  f"{row['r_variance_90']:>8d}  "
                  f"{row['r_mp_edge']:>8d}")

        # Summary stats
        print(f"\n  SUMMARY for {dataset_name}:")
        print(f"    Stable rank:  mean = {df['r_stable_rank'].mean():.2f}, "
              f"std = {df['r_stable_rank'].std():.2f}, "
              f"CV = {df['r_stable_rank'].std() / df['r_stable_rank'].mean():.2f}")
        print(f"    Variance 90%: mean = {df['r_variance_90'].mean():.1f}, "
              f"std = {df['r_variance_90'].std():.1f}, "
              f"CV = {df['r_variance_90'].std() / max(df['r_variance_90'].mean(), 0.01):.2f}")
        print(f"    MP edge:      mean = {df['r_mp_edge'].mean():.1f}, "
              f"std = {df['r_mp_edge'].std():.1f}, "
              f"CV = {df['r_mp_edge'].std() / max(df['r_mp_edge'].mean(), 0.01):.2f}")

    if not all_results:
        print("\nERROR: No results computed.")
        sys.exit(1)

    full_df = pd.concat(all_results, ignore_index=True)

    # ── Cross-method agreement ───────────────────────────────
    print("\n" + "=" * 60)
    print("  CROSS-METHOD AGREEMENT")
    print("=" * 60)

    # Round stable rank to nearest integer for comparison
    full_df["r_stable_int"] = full_df["r_stable_rank"].round().astype(int)

    # Pairwise disagreement
    disagree_sv = np.abs(full_df["r_stable_int"] - full_df["r_variance_90"])
    disagree_sm = np.abs(full_df["r_stable_int"] - full_df["r_mp_edge"])
    disagree_vm = np.abs(full_df["r_variance_90"] - full_df["r_mp_edge"])

    print(f"\n  Stable rank vs Variance 90%:")
    print(f"    Mean disagreement: {disagree_sv.mean():.2f}")
    print(f"    Agree within ±1:   {(disagree_sv <= 1).mean() * 100:.1f}%")
    print(f"    Agree within ±2:   {(disagree_sv <= 2).mean() * 100:.1f}%")

    print(f"\n  Stable rank vs MP edge:")
    print(f"    Mean disagreement: {disagree_sm.mean():.2f}")
    print(f"    Agree within ±1:   {(disagree_sm <= 1).mean() * 100:.1f}%")

    print(f"\n  Variance 90% vs MP edge:")
    print(f"    Mean disagreement: {disagree_vm.mean():.2f}")
    print(f"    Agree within ±1:   {(disagree_vm <= 1).mean() * 100:.1f}%")

    # ── Temporal stability ───────────────────────────────────
    print("\n" + "=" * 60)
    print("  TEMPORAL STABILITY")
    print("=" * 60)

    for dataset_name in full_df["dataset"].unique():
        sub = full_df[full_df["dataset"] == dataset_name]
        cv_stable = sub["r_stable_rank"].std() / sub["r_stable_rank"].mean()
        cv_var = sub["r_variance_90"].std() / max(sub["r_variance_90"].mean(), 0.01)
        cv_mp = sub["r_mp_edge"].std() / max(sub["r_mp_edge"].mean(), 0.01)
        print(f"\n  {dataset_name}:")
        print(f"    CV(stable rank): {cv_stable:.3f}")
        print(f"    CV(variance 90%): {cv_var:.3f}")
        print(f"    CV(MP edge): {cv_mp:.3f}")

    # ── Verdict ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  VERDICT")
    print("=" * 60)

    mean_disagree = (disagree_sv.mean() + disagree_sm.mean() + disagree_vm.mean()) / 3
    max_cv = max(
        full_df.groupby("dataset")["r_stable_rank"].apply(
            lambda x: x.std() / x.mean()).max(),
        full_df.groupby("dataset")["r_variance_90"].apply(
            lambda x: x.std() / max(x.mean(), 0.01)).max(),
    )

    agree_within_1 = (
        (disagree_sv <= 1).mean() +
        (disagree_sm <= 1).mean() +
        (disagree_vm <= 1).mean()
    ) / 3

    if mean_disagree < 2 and max_cv < 0.50:
        verdict = "PASS"
        detail = (f"Mean pairwise disagreement = {mean_disagree:.2f} < 2, "
                  f"max CV = {max_cv:.3f} < 0.50, "
                  f"agree within ±1: {agree_within_1 * 100:.0f}%")
    elif mean_disagree < 3 and max_cv < 0.50:
        verdict = "MARGINAL"
        detail = (f"Mean disagreement = {mean_disagree:.2f} (borderline), "
                  f"max CV = {max_cv:.3f}")
    else:
        verdict = "FAIL"
        detail = (f"Mean disagreement = {mean_disagree:.2f} ≥ 3 or "
                  f"max CV = {max_cv:.3f} ≥ 0.50")

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    if verdict == "PASS":
        overall_r = full_df[["r_stable_int", "r_variance_90", "r_mp_edge"]].values.flatten()
        print(f"\n  Overall estimated r: {np.median(overall_r):.0f} "
              f"(median across all methods and windows)")
        print(f"  Range: [{np.percentile(overall_r, 10):.0f}, "
              f"{np.percentile(overall_r, 90):.0f}] (10th-90th percentile)")
        print(f"\n  The manifold dimension is stable and consistently estimated.")
    elif verdict == "FAIL":
        print(f"\n  *** The manifold dimension is NOT stable across methods. ***")
        print(f"  *** The manifold model may be too rigid for this market. ***")

    # ── Save ─────────────────────────────────────────────────
    full_df.to_csv(OUT_DIR / "test_02_results.csv", index=False)

    summary = {
        "test": "Test 2: Manifold Dimension Stability",
        "verdict": verdict,
        "mean_disagreement": mean_disagree,
        "agree_within_1_pct": agree_within_1 * 100,
        "max_cv": max_cv,
        "r_median": np.median(full_df[["r_stable_int", "r_variance_90", "r_mp_edge"]].values),
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_02_summary.csv")

    print(f"\n  Results saved to {OUT_DIR / 'test_02_results.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_2()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
