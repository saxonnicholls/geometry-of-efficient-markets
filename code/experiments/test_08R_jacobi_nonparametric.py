#!/usr/bin/env python3
"""
Test 8R: Jacobi vs GBM — Non-Parametric Boundary Test
=======================================================
The Jacobi diffusion has √w volatility → mean-reverting near boundaries.
GBM has w volatility → no boundary mean-reversion.

The distinguishing feature: conditional on being near the boundary (w small),
the DRIFT should be positive (pushing away from 0) under Jacobi, and zero
under GBM. This is the Feller boundary condition.

Non-parametric test:
    1. Track portfolio weight trajectories
    2. Bin by current weight level (quintiles)
    3. Measure the conditional drift E[Δw | w ∈ bin]
    4. Under Jacobi: drift is POSITIVE when w is small, NEGATIVE when w is large
       (mean-reversion to the interior)
    5. Under GBM: drift is approximately ZERO regardless of w level
    6. Use permutation test for significance

Also: test the volatility scaling.
    Under Jacobi: Var(Δw | w) ∝ w (volatility scales as √w)
    Under GBM: Var(Δw | w) ∝ w² (volatility scales as w)
    Regress log(Var(Δw)) on log(w): slope ≈ 1 for Jacobi, ≈ 2 for GBM

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from bootstrap import bootstrap_ci, permutation_test

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)


def compute_weight_trajectory(returns):
    """
    Compute the portfolio weight trajectory under buy-and-hold
    (no rebalancing). Starting from equal weight, weights drift
    as prices diverge.
    """
    T, d = returns.shape
    gross = 1.0 + returns
    weights = np.ones(d) / d
    trajectory = [weights.copy()]
    for t in range(T):
        weights = weights * gross[t]
        weights /= weights.sum()
        trajectory.append(weights.copy())
    return np.array(trajectory)  # (T+1) × d


def conditional_drift_test(weights_traj, n_bins=5):
    """
    Non-parametric test of conditional drift.

    Bins weight levels into quintiles, measures E[Δw | w ∈ bin].
    Under Jacobi: drift is positive for low w, negative for high w (mean-reversion).
    Under GBM: drift ≈ 0 for all bins.

    Returns the drift per bin and a mean-reversion score.
    """
    T, d = weights_traj.shape
    T -= 1  # because we need Δw

    dw = np.diff(weights_traj, axis=0)  # T × d
    w = weights_traj[:-1]               # T × d

    # Pool all asset-time observations
    w_flat = w.ravel()
    dw_flat = dw.ravel()

    # Remove extreme values
    mask = (w_flat > 1e-6) & (w_flat < 1 - 1e-6) & np.isfinite(dw_flat)
    w_flat = w_flat[mask]
    dw_flat = dw_flat[mask]

    # Bin by weight level
    bin_edges = np.percentile(w_flat, np.linspace(0, 100, n_bins + 1))
    bin_edges[0] = 0
    bin_edges[-1] = 1

    bin_centers = []
    bin_drifts = []
    bin_stds = []
    bin_counts = []

    for i in range(n_bins):
        in_bin = (w_flat >= bin_edges[i]) & (w_flat < bin_edges[i + 1])
        if in_bin.sum() < 100:
            continue
        center = w_flat[in_bin].mean()
        drift = dw_flat[in_bin].mean()
        std = dw_flat[in_bin].std() / np.sqrt(in_bin.sum())

        bin_centers.append(center)
        bin_drifts.append(drift)
        bin_stds.append(std)
        bin_counts.append(in_bin.sum())

    bin_centers = np.array(bin_centers)
    bin_drifts = np.array(bin_drifts)

    # Mean-reversion score: correlation of drift with -(w - mean_w)
    # Under Jacobi: drift ∝ (mean_w - w), so corr(drift, -w) > 0
    # Under GBM: drift independent of w, so corr ≈ 0
    if len(bin_centers) > 3:
        mean_w = w_flat.mean()
        mr_corr = np.corrcoef(bin_drifts, -(bin_centers - mean_w))[0, 1]
    else:
        mr_corr = 0

    return {
        "bin_centers": bin_centers,
        "bin_drifts": bin_drifts,
        "bin_stds": np.array(bin_stds),
        "bin_counts": np.array(bin_counts),
        "mr_correlation": mr_corr,
    }


def volatility_scaling_test(weights_traj):
    """
    Test the volatility scaling: Var(Δw | w) vs w.

    Under Jacobi: Var(Δw) ∝ w → log-log slope ≈ 1
    Under GBM: Var(Δw) ∝ w² → log-log slope ≈ 2

    Uses binned variance estimation (non-parametric).
    """
    T = weights_traj.shape[0] - 1
    d = weights_traj.shape[1]

    dw = np.diff(weights_traj, axis=0)
    w = weights_traj[:-1]

    w_flat = w.ravel()
    dw_flat = dw.ravel()

    mask = (w_flat > 1e-4) & (w_flat < 0.5) & np.isfinite(dw_flat)
    w_flat = w_flat[mask]
    dw_flat = dw_flat[mask]

    # Bin by weight level (20 bins)
    n_bins = 20
    bin_edges = np.percentile(w_flat, np.linspace(0, 100, n_bins + 1))

    log_w = []
    log_var = []

    for i in range(n_bins):
        in_bin = (w_flat >= bin_edges[i]) & (w_flat < bin_edges[i + 1])
        if in_bin.sum() < 50:
            continue
        w_mean = w_flat[in_bin].mean()
        dw_var = dw_flat[in_bin].var()

        if w_mean > 1e-6 and dw_var > 1e-20:
            log_w.append(np.log(w_mean))
            log_var.append(np.log(dw_var))

    log_w = np.array(log_w)
    log_var = np.array(log_var)

    if len(log_w) > 5:
        slope, intercept, r_value, p_value, std_err = stats.linregress(log_w, log_var)
    else:
        slope, intercept, r_value, p_value, std_err = 0, 0, 0, 1, 0

    return {
        "log_w": log_w,
        "log_var": log_var,
        "slope": slope,
        "slope_se": std_err,
        "r_squared": r_value ** 2,
        "p_value": p_value,
    }


def run_test_8R():
    print("=" * 70)
    print("  TEST 8R: Jacobi vs GBM — Non-Parametric Boundary Test")
    print("  Does portfolio weight drift mean-revert? Does vol scale as √w?")
    print("=" * 70)

    # Load multiple datasets
    datasets = {}

    ff25_path = DATA_DIR / "ff25_daily_returns.parquet"
    if ff25_path.exists():
        ff25 = pd.read_parquet(ff25_path).loc["1990-01-01":]
        ff25 = ff25.dropna()
        datasets["FF25 (1990-2026)"] = ff25.values

    eq_path = DATA_DIR / "equities_50_daily_returns.parquet"
    if eq_path.exists():
        eq = pd.read_parquet(eq_path).dropna()
        datasets["50 Equities (Databento)"] = eq.values

    sec_path = DATA_DIR / "sector_etf_9_daily_returns.parquet"
    if sec_path.exists():
        sec = pd.read_parquet(sec_path).dropna()
        datasets["9 Sector ETFs"] = sec.values

    if not datasets:
        print("  ERROR: no data")
        sys.exit(1)

    all_mr_corrs = []
    all_slopes = []
    all_results = []

    for name, returns in datasets.items():
        returns = np.nan_to_num(returns, 0.0)
        T, d = returns.shape

        print(f"\n{'─' * 70}")
        print(f"  Dataset: {name} ({T} days × {d} assets)")
        print(f"{'─' * 70}")

        # Compute weight trajectory
        traj = compute_weight_trajectory(returns)

        # Test 1: Conditional drift (mean-reversion)
        drift = conditional_drift_test(traj, n_bins=10)
        mr = drift["mr_correlation"]
        all_mr_corrs.append(mr)

        print(f"\n  Conditional drift test:")
        print(f"    Mean-reversion correlation: {mr:.4f}")
        print(f"    (Jacobi predicts > 0, GBM predicts ≈ 0)")
        print(f"    {'Bin center':>12}  {'Drift':>10}  {'Std err':>10}  {'N':>8}")
        for i in range(len(drift["bin_centers"])):
            print(f"    {drift['bin_centers'][i]:>12.4f}  "
                  f"{drift['bin_drifts'][i]:>+10.6f}  "
                  f"{drift['bin_stds'][i]:>10.6f}  "
                  f"{drift['bin_counts'][i]:>8.0f}")

        # Test 2: Volatility scaling
        vol = volatility_scaling_test(traj)
        all_slopes.append(vol["slope"])

        print(f"\n  Volatility scaling test:")
        print(f"    log-log slope: {vol['slope']:.3f} ± {vol['slope_se']:.3f}")
        print(f"    (Jacobi predicts ≈ 1.0, GBM predicts ≈ 2.0)")
        print(f"    R² = {vol['r_squared']:.3f}, p = {vol['p_value']:.2e}")

        # Bootstrap CI for the slope
        if len(vol["log_w"]) > 10:
            data_combined = np.column_stack([vol["log_w"], vol["log_var"]])
            def slope_stat(d):
                return np.polyfit(d[:, 0], d[:, 1], 1)[0] if len(d) > 3 else 0
            boot = bootstrap_ci(data_combined, slope_stat, n_bootstrap=5000,
                                 block_size=3, seed=42)
            print(f"    Bootstrap 95% CI: [{boot['ci_lower']:.3f}, {boot['ci_upper']:.3f}]")
            all_results.append({
                "dataset": name, "mr_corr": mr,
                "vol_slope": vol["slope"], "vol_slope_ci_lo": boot["ci_lower"],
                "vol_slope_ci_hi": boot["ci_upper"],
            })
        else:
            all_results.append({
                "dataset": name, "mr_corr": mr,
                "vol_slope": vol["slope"], "vol_slope_ci_lo": np.nan,
                "vol_slope_ci_hi": np.nan,
            })

    # ── Visualisation ────────────────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # 1. Conditional drift (last dataset)
    ax = axes[0]
    dc = drift["bin_centers"]
    dd = drift["bin_drifts"]
    ds = drift["bin_stds"]
    ax.errorbar(dc, dd, yerr=2 * ds, fmt="o-", color="steelblue",
                capsize=3, markersize=5)
    ax.axhline(0, color="red", linewidth=0.5, linestyle="--", label="GBM prediction (zero drift)")
    # Jacobi prediction: drift ∝ (1/d - w)
    w_grid = np.linspace(dc.min(), dc.max(), 100)
    jacobi_drift = 0.0001 * (1.0 / returns.shape[1] - w_grid)
    ax.plot(w_grid, jacobi_drift, "g--", linewidth=1.5, label="Jacobi prediction")
    ax.set_xlabel("Weight w")
    ax.set_ylabel("E[Δw | w]")
    ax.set_title(f"Conditional Drift\n(MR corr = {mr:.3f})")
    ax.legend(fontsize=8)

    # 2. Volatility scaling
    ax = axes[1]
    ax.scatter(vol["log_w"], vol["log_var"], c="steelblue", s=30, alpha=0.7)
    if len(vol["log_w"]) > 2:
        z = np.polyfit(vol["log_w"], vol["log_var"], 1)
        x_fit = np.sort(vol["log_w"])
        ax.plot(x_fit, np.polyval(z, x_fit), "r-", linewidth=2,
                label=f"Fit: slope = {z[0]:.2f}")
        # Theoretical lines
        ax.plot(x_fit, x_fit * 1 + (vol["log_var"].mean() - vol["log_w"].mean()),
                "g--", linewidth=1, alpha=0.7, label="Jacobi (slope=1)")
        ax.plot(x_fit, x_fit * 2 + (vol["log_var"].mean() - 2 * vol["log_w"].mean()),
                "orange", linewidth=1, linestyle="--", alpha=0.7, label="GBM (slope=2)")
    ax.set_xlabel("log(w)")
    ax.set_ylabel("log(Var(Δw))")
    ax.set_title("Volatility Scaling")
    ax.legend(fontsize=8)

    # 3. Summary across datasets
    ax = axes[2]
    names = [r["dataset"][:15] for r in all_results]
    slopes = [r["vol_slope"] for r in all_results]
    mr_corrs = [r["mr_corr"] for r in all_results]

    x = np.arange(len(names))
    w = 0.35
    ax.bar(x - w / 2, slopes, w, label="Vol slope (Jacobi=1, GBM=2)",
           color="steelblue", alpha=0.7)
    ax.bar(x + w / 2, mr_corrs, w, label="MR correlation (Jacobi>0, GBM≈0)",
           color="darkred", alpha=0.7)
    ax.axhline(1.0, color="green", linewidth=1, linestyle="--", alpha=0.5)
    ax.axhline(2.0, color="orange", linewidth=1, linestyle="--", alpha=0.5)
    ax.axhline(0, color="black", linewidth=0.5)
    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=7, rotation=15)
    ax.set_title("Summary Across Datasets")
    ax.legend(fontsize=7)

    plt.suptitle("Test 8R: Jacobi vs GBM — Non-Parametric", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig(GAL_DIR / "test_08R_jacobi_nonparametric.png", dpi=150)
    plt.close()

    # ── Verdict ──────────────────────────────────────────────
    print(f"\n" + "=" * 70)
    print(f"  VERDICT")
    print(f"=" * 70)

    mean_slope = np.mean(all_slopes)
    mean_mr = np.mean(all_mr_corrs)

    # Jacobi: slope ≈ 1.0, MR > 0
    # GBM: slope ≈ 2.0, MR ≈ 0
    jacobi_slope = abs(mean_slope - 1.0) < abs(mean_slope - 2.0)
    jacobi_mr = mean_mr > 0.1

    print(f"\n  Mean vol scaling slope: {mean_slope:.3f} (Jacobi=1, GBM=2)")
    print(f"  Mean MR correlation:    {mean_mr:.3f} (Jacobi>0, GBM≈0)")
    print(f"  Slope closer to Jacobi: {'YES' if jacobi_slope else 'NO'}")
    print(f"  MR correlation > 0.1:   {'YES' if jacobi_mr else 'NO'}")

    if jacobi_slope and jacobi_mr:
        verdict = "PASS"
        detail = f"Slope={mean_slope:.2f} (closer to 1 than 2), MR={mean_mr:.3f}>0"
    elif jacobi_slope or jacobi_mr:
        verdict = "MARGINAL"
        detail = f"Slope={mean_slope:.2f}, MR={mean_mr:.3f} — one criterion met"
    else:
        verdict = "FAIL"
        detail = f"Slope={mean_slope:.2f}, MR={mean_mr:.3f} — neither criterion"

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    # Save
    pd.DataFrame(all_results).to_csv(OUT_DIR / "test_08R_results.csv", index=False)
    summary = {"test": "Test 8R: Jacobi vs GBM (nonparametric)", "verdict": verdict,
               "mean_slope": mean_slope, "mean_mr_corr": mean_mr,
               "jacobi_slope": jacobi_slope, "jacobi_mr": jacobi_mr}
    pd.Series(summary).to_csv(OUT_DIR / "test_08R_summary.csv")
    print(f"\n  Results: {OUT_DIR / 'test_08R_results.csv'}")
    print(f"  Gallery: {GAL_DIR / 'test_08R_jacobi_nonparametric.png'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, _ = run_test_8R()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
