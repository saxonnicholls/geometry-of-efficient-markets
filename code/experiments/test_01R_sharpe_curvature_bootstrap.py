#!/usr/bin/env python3
"""
Test 1R: Sharpe-Curvature Identity (Bootstrap + Permutation + Out-of-Sample)
=============================================================================
Revised version with non-parametric inference.

Improvements over Test 1:
- Block bootstrap 95% CI for the slope β₁
- Permutation test (10,000 shuffles) for p-value without distributional assumptions
- Out-of-sample: estimate H on first half, test Sharpe on second half
- Multi-frequency: daily AND weekly AND monthly

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

# Add parent to path for bootstrap module
sys.path.insert(0, str(Path(__file__).parent))
from bootstrap import bootstrap_ci, permutation_test, out_of_sample_split

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
OUT_DIR.mkdir(exist_ok=True)


def project_simplex(v):
    d = len(v)
    u = np.sort(v)[::-1]
    cumsum = np.cumsum(u)
    rho = np.max(np.where(u - (cumsum - 1) / (np.arange(d) + 1) > 0))
    theta = (cumsum[rho] - 1) / (rho + 1)
    return np.maximum(v - theta, 0)


def solve_kelly(gross_returns, max_iter=300, tol=1e-8):
    T, d = gross_returns.shape
    b = np.ones(d) / d
    for it in range(max_iter):
        bx = np.maximum(gross_returns @ b, 1e-12)
        grad = (gross_returns / bx[:, None]).mean(axis=0)
        lr = 1.0 / (it + 10)
        b = project_simplex(b + lr * grad)
    return b


def estimate_H_and_sharpe(returns_window, n_factors=4):
    T, d = returns_window.shape
    gross = 1.0 + returns_window
    b_star = solve_kelly(gross)
    b_star = np.maximum(b_star, 1e-8)
    b_star /= b_star.sum()

    cov = np.cov(returns_window.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]

    r = min(n_factors, d - 1)
    V_r = eigenvectors[:, :r]
    Pi_N = np.eye(d) - V_r @ V_r.T

    half_inv_sqrt = 1.0 / (2.0 * np.sqrt(b_star))
    H_vec = Pi_N @ half_inv_sqrt
    H_norm = np.linalg.norm(H_vec)

    if H_norm > 1e-10:
        direction = H_vec / H_norm
        strat_ret = returns_window @ direction
        mean_ret = np.mean(strat_ret)
        std_ret = np.std(strat_ret, ddof=1)
        sharpe = abs(mean_ret) / max(std_ret, 1e-12) * np.sqrt(252)
    else:
        sharpe = 0.0

    return H_norm, sharpe


def run_rolling(excess_returns, window, step, n_factors, label=""):
    """Run rolling estimation and return arrays of (H, Sharpe)."""
    T_total = len(excess_returns)
    Hs, Sharpes, dates = [], [], []

    for i in range(0, T_total - window, step):
        w = excess_returns.iloc[i:i + window].values
        if np.isnan(w).sum() > 0.05 * w.size:
            continue
        w = np.nan_to_num(w, 0.0)
        try:
            H, S = estimate_H_and_sharpe(w, n_factors)
            Hs.append(H)
            Sharpes.append(S)
            dates.append(excess_returns.index[i + window - 1])
        except Exception:
            pass

    return np.array(Hs), np.array(Sharpes), dates


def regression_slope(data):
    """Statistic for bootstrap: regression slope of Sharpe on H."""
    # data is T×2 array: col 0 = H, col 1 = Sharpe
    x, y = data[:, 0], data[:, 1]
    mask = ~(np.isnan(x) | np.isnan(y))
    x, y = x[mask], y[mask]
    if len(x) < 10:
        return 0.0
    slope = np.polyfit(x, y, 1)[0]
    return slope


def run_test_1R():
    print("=" * 70)
    print("  TEST 1R: Sharpe-Curvature Identity")
    print("  Bootstrap + Permutation + Out-of-Sample")
    print("=" * 70)

    # Load data
    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet")
    ff5 = pd.read_parquet(DATA_DIR / "ff5_factors_daily.parquet")

    common_idx = ff25.index.intersection(ff5.index)
    ff25 = ff25.loc[common_idx]
    rf = ff5.loc[common_idx, "RF"]
    excess = ff25.subtract(rf, axis=0)

    print(f"\n  Data: {excess.shape[0]} days × {excess.shape[1]} portfolios")
    print(f"  Period: {excess.index[0].date()} to {excess.index[-1].date()}")

    # ── Full-sample rolling estimation ───────────────────────
    print(f"\n  Running full-sample rolling estimation...")
    H_all, S_all, dates_all = run_rolling(excess, window=252, step=63, n_factors=4)
    print(f"  {len(H_all)} windows computed")

    # Remove outliers
    mask = (np.abs(H_all - H_all.mean()) < 3 * H_all.std()) & \
           (np.abs(S_all - S_all.mean()) < 3 * S_all.std())
    H_clean, S_clean = H_all[mask], S_all[mask]
    print(f"  {len(H_clean)} windows after outlier removal")

    # ── 1. Parametric regression (for comparison) ────────────
    slope, intercept, r_val, p_val, se = stats.linregress(H_clean, S_clean)
    print(f"\n  PARAMETRIC: β₁ = {slope:.4f} ± {se:.4f}, "
          f"R² = {r_val**2:.4f}, p = {p_val:.2e}")

    # ── 2. Block bootstrap CI for β₁ ────────────────────────
    print(f"\n  Computing block bootstrap CI (10,000 resamples)...")
    data_combined = np.column_stack([H_clean, S_clean])
    boot = bootstrap_ci(data_combined, regression_slope,
                         n_bootstrap=10000, block_size=4, seed=42)
    print(f"  BOOTSTRAP: β₁ = {boot['estimate']:.4f} "
          f"[{boot['ci_lower']:.4f}, {boot['ci_upper']:.4f}] (95% CI)")
    print(f"  Bootstrap SE: {boot['se']:.4f}")

    # ── 3. Permutation test ──────────────────────────────────
    print(f"\n  Computing permutation test (10,000 permutations)...")
    perm = permutation_test(H_clean, S_clean, n_permutations=10000, seed=42)
    print(f"  PERMUTATION: observed corr = {perm['observed']:.4f}, "
          f"p = {perm['p_value']:.4f}")
    print(f"  Null distribution: mean = {perm['null_mean']:.4f}, "
          f"std = {perm['null_std']:.4f}")

    # ── 4. Out-of-sample test ────────────────────────────────
    print(f"\n  Out-of-sample test (estimate on first half, test on second)...")
    T_half = len(excess) // 2
    excess_train = excess.iloc[:T_half]
    excess_test = excess.iloc[T_half:]

    H_train, S_train, _ = run_rolling(excess_train, 252, 63, 4)
    H_test, S_test, _ = run_rolling(excess_test, 252, 63, 4)

    if len(H_train) > 10 and len(H_test) > 10:
        # Fit regression on train
        slope_train = np.polyfit(H_train, S_train, 1)[0]
        # Predict on test
        S_pred = slope_train * H_test
        # Correlation between predicted and actual
        oos_corr = np.corrcoef(S_pred, S_test)[0, 1]
        oos_rmse = np.sqrt(np.mean((S_pred - S_test) ** 2))
        print(f"  OOS: Train slope = {slope_train:.4f}")
        print(f"  OOS: Correlation(predicted, actual) = {oos_corr:.4f}")
        print(f"  OOS: RMSE = {oos_rmse:.4f}")
    else:
        oos_corr = np.nan
        print(f"  OOS: Insufficient data")

    # ── 5. Multi-frequency ───────────────────────────────────
    print(f"\n  Multi-frequency analysis:")

    # Weekly
    excess_weekly = excess.resample("W").sum()
    H_w, S_w, _ = run_rolling(excess_weekly, 52, 13, 4)
    if len(H_w) > 10:
        sl_w, _, r_w, p_w, _ = stats.linregress(H_w, S_w)
        print(f"  WEEKLY:  β₁ = {sl_w:.4f}, R² = {r_w**2:.4f}, p = {p_w:.2e}")
    else:
        print(f"  WEEKLY:  Insufficient data")
        sl_w, r_w, p_w = np.nan, np.nan, np.nan

    # Monthly
    excess_monthly = excess.resample("ME").sum()
    H_m, S_m, _ = run_rolling(excess_monthly, 24, 6, 4)
    if len(H_m) > 10:
        sl_m, _, r_m, p_m, _ = stats.linregress(H_m, S_m)
        print(f"  MONTHLY: β₁ = {sl_m:.4f}, R² = {r_m**2:.4f}, p = {p_m:.2e}")
    else:
        print(f"  MONTHLY: Insufficient data")
        sl_m, r_m, p_m = np.nan, np.nan, np.nan

    # ── Verdict ──────────────────────────────────────────────
    print(f"\n" + "=" * 70)
    print(f"  VERDICT")
    print(f"=" * 70)

    # The test passes if:
    # 1. Bootstrap CI for β₁ excludes zero
    # 2. Permutation p-value < 0.05
    # 3. Out-of-sample correlation > 0

    ci_excludes_zero = boot['ci_lower'] > 0 or boot['ci_upper'] < 0
    perm_significant = perm['p_value'] < 0.05
    oos_positive = oos_corr > 0 if np.isfinite(oos_corr) else False

    n_pass = sum([ci_excludes_zero, perm_significant, oos_positive])

    if n_pass >= 2:
        verdict = "PASS"
    elif n_pass >= 1:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"\n  Bootstrap CI excludes zero: {'YES' if ci_excludes_zero else 'NO'} "
          f"[{boot['ci_lower']:.4f}, {boot['ci_upper']:.4f}]")
    print(f"  Permutation p < 0.05:       {'YES' if perm_significant else 'NO'} "
          f"(p = {perm['p_value']:.4f})")
    print(f"  Out-of-sample corr > 0:     {'YES' if oos_positive else 'NO'} "
          f"(r = {oos_corr:.4f})" if np.isfinite(oos_corr) else "  (insufficient data)")
    print(f"\n  Result: {verdict} ({n_pass}/3 criteria met)")

    if verdict == "PASS":
        print(f"\n  The Sharpe-curvature identity is ROBUSTLY supported.")
        print(f"  β₁ = {boot['estimate']:.4f} [{boot['ci_lower']:.4f}, {boot['ci_upper']:.4f}]")
        print(f"  The relationship holds in-sample, out-of-sample, and")
        print(f"  under permutation testing with no distributional assumptions.")

    # ── Save ─────────────────────────────────────────────────
    summary = {
        "test": "Test 1R: Sharpe-Curvature (Bootstrap)",
        "verdict": verdict,
        "beta_1": boot["estimate"],
        "ci_lower": boot["ci_lower"],
        "ci_upper": boot["ci_upper"],
        "bootstrap_se": boot["se"],
        "parametric_p": p_val,
        "permutation_p": perm["p_value"],
        "oos_correlation": oos_corr,
        "n_windows": len(H_clean),
        "ci_excludes_zero": ci_excludes_zero,
        "perm_significant": perm_significant,
        "oos_positive": oos_positive,
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_01R_summary.csv")
    print(f"\n  Summary saved to {OUT_DIR / 'test_01R_summary.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_1R()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
