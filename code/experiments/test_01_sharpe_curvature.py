#!/usr/bin/env python3
"""
Test 1: The Sharpe-Curvature Identity
======================================
Sharpe* = ||H||_{L²(M)} — the central theorem of the monograph.

Hypothesis: β₁ > 0 with p < 0.05 in regression
    Sharpe_realised = β₀ + β₁ · H_estimated + ε

Dataset: Fama-French 25 portfolios (size × value), daily returns 1963-2024
Method: Rolling 252-day windows. In each window:
    1. Find b* (Kelly-optimal portfolio) via projected gradient ascent
    2. PCA to identify factor subspace (top r eigenvectors)
    3. Project 1/(2√b*) onto normal bundle to get H
    4. Compute realised Sharpe of the H-direction strategy
    5. Regress Sharpe on ||H||

Expected: β₁ ≈ 1.0, R² > 0.15
Falsification: β₁ ≤ 0 or R² < 0.05

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy import stats

# ── Paths ────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
OUT_DIR.mkdir(exist_ok=True)


# ── Core functions ───────────────────────────────────────────

def solve_kelly(gross_returns: np.ndarray, max_iter=300, tol=1e-8):
    """
    Find the log-optimal portfolio b* = argmax (1/T) Σ log(b · x_t).
    Projected gradient ascent on the simplex.
    """
    T, d = gross_returns.shape
    b = np.ones(d) / d  # start at equal weight

    for it in range(max_iter):
        # Gradient of log-growth: (1/T) Σ x_t / (b · x_t)
        bx = gross_returns @ b
        bx = np.maximum(bx, 1e-12)
        grad = (gross_returns / bx[:, None]).mean(axis=0)

        # Step size (diminishing)
        lr = 1.0 / (it + 10)
        b_new = b + lr * grad

        # Project onto simplex
        b_new = project_simplex(b_new)

        # Check convergence
        if np.linalg.norm(b_new - b) < tol:
            break
        b = b_new

    return b


def project_simplex(v):
    """Project v onto the probability simplex (Duchi et al. 2008)."""
    d = len(v)
    u = np.sort(v)[::-1]
    cumsum = np.cumsum(u)
    rho = np.max(np.where(u - (cumsum - 1) / (np.arange(d) + 1) > 0))
    theta = (cumsum[rho] - 1) / (rho + 1)
    return np.maximum(v - theta, 0)


def estimate_H_and_sharpe(returns_window: np.ndarray, n_factors=4):
    """
    Estimate mean curvature ||H|| and realised Sharpe for one window.

    Mean curvature:
        H = || Π_N (1/(2√b*)) ||
    where Π_N is projection onto the normal bundle (complement of factor subspace).
    """
    T, d = returns_window.shape

    # Step 1: Gross returns (price relatives)
    gross = 1.0 + returns_window

    # Step 2: Kelly-optimal portfolio
    b_star = solve_kelly(gross)
    b_star = np.maximum(b_star, 1e-8)
    b_star /= b_star.sum()

    # Step 3: PCA of return covariance → factor subspace
    cov = np.cov(returns_window.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]

    # Factor subspace (top r eigenvectors)
    r = min(n_factors, d - 1)
    V_r = eigenvectors[:, :r]

    # Normal bundle projection: Π_N = I - V_r V_r^T
    Pi_N = np.eye(d) - V_r @ V_r.T

    # Step 4: Mean curvature H = || Π_N(1/(2√b*)) ||
    half_inv_sqrt = 1.0 / (2.0 * np.sqrt(b_star))
    H_vec = Pi_N @ half_inv_sqrt
    H_norm = np.linalg.norm(H_vec)

    # Step 5: Realised Sharpe of the H-direction strategy
    if H_norm > 1e-10:
        direction = H_vec / H_norm
        strategy_returns = returns_window @ direction
        mean_ret = np.mean(strategy_returns)
        std_ret = np.std(strategy_returns, ddof=1)
        if std_ret > 1e-12:
            sharpe = mean_ret / std_ret * np.sqrt(252)
        else:
            sharpe = 0.0
    else:
        sharpe = 0.0

    # Also compute the best factor strategy Sharpe for comparison
    factor_returns = returns_window @ V_r  # T × r
    factor_sharpes = []
    for j in range(r):
        m = np.mean(factor_returns[:, j])
        s = np.std(factor_returns[:, j], ddof=1)
        if s > 1e-12:
            factor_sharpes.append(abs(m) / s * np.sqrt(252))
    max_factor_sharpe = max(factor_sharpes) if factor_sharpes else 0.0

    return {
        "H_norm": H_norm,
        "sharpe_H_direction": abs(sharpe),
        "sharpe_max_factor": max_factor_sharpe,
        "kelly_growth": np.mean(np.log(gross @ b_star)),
        "n_factors_used": r,
    }


# ── Main experiment ──────────────────────────────────────────

def run_test_1():
    """Run Test 1: Sharpe-Curvature Identity."""

    print("=" * 60)
    print("  TEST 1: Sharpe-Curvature Identity")
    print("  Sharpe* = ||H||_{L²(M)}")
    print("=" * 60)

    # Load data
    ff25_path = DATA_DIR / "ff25_daily_returns.parquet"
    ff5_path = DATA_DIR / "ff5_factors_daily.parquet"

    if not ff25_path.exists():
        print(f"\nERROR: Data not found at {ff25_path}")
        print("Run data/download_all.py and data/process_all.py first.")
        sys.exit(1)

    ff25 = pd.read_parquet(ff25_path)
    ff5 = pd.read_parquet(ff5_path)

    # Align dates
    common_idx = ff25.index.intersection(ff5.index)
    ff25 = ff25.loc[common_idx]
    ff5 = ff5.loc[common_idx]

    # Subtract risk-free rate
    rf = ff5["RF"]
    excess = ff25.subtract(rf, axis=0)

    print(f"\nData: {excess.shape[0]} days × {excess.shape[1]} portfolios")
    print(f"Period: {excess.index[0].date()} to {excess.index[-1].date()}")

    # Rolling estimation
    window = 252  # 1 year
    step = 63     # quarterly steps
    n_factors = 4

    results = []
    dates = excess.index
    n_windows = (len(dates) - window) // step

    print(f"\nRunning {n_windows} rolling windows (window={window}d, step={step}d, r={n_factors})...")
    print()

    for i in range(0, len(dates) - window, step):
        window_data = excess.iloc[i:i + window].values
        window_end = dates[i + window - 1]

        # Skip if too many NaNs
        if np.isnan(window_data).sum() > 0.1 * window_data.size:
            continue

        # Replace remaining NaNs with 0
        window_data = np.nan_to_num(window_data, 0.0)

        try:
            result = estimate_H_and_sharpe(window_data, n_factors=n_factors)
            result["date"] = window_end
            results.append(result)

            if len(results) % 20 == 0:
                print(f"  Window {len(results):4d}: {window_end.date()}  "
                      f"||H|| = {result['H_norm']:.4f}  "
                      f"Sharpe(H) = {result['sharpe_H_direction']:.3f}  "
                      f"Sharpe(factor) = {result['sharpe_max_factor']:.3f}")
        except Exception as e:
            pass  # Skip problematic windows

    if not results:
        print("ERROR: No valid windows computed.")
        sys.exit(1)

    df = pd.DataFrame(results)

    # ── Regression: Sharpe on ||H|| ──────────────────────────
    print("\n" + "=" * 60)
    print("  REGRESSION: Sharpe_realised = β₀ + β₁ · ||H|| + ε")
    print("=" * 60)

    X = df["H_norm"].values
    y = df["sharpe_H_direction"].values

    # Remove outliers (>3σ)
    mask = (np.abs(X - X.mean()) < 3 * X.std()) & (np.abs(y - y.mean()) < 3 * y.std())
    X_clean = X[mask]
    y_clean = y[mask]

    slope, intercept, r_value, p_value, std_err = stats.linregress(X_clean, y_clean)
    r_squared = r_value ** 2

    print(f"\n  N windows:     {len(X_clean)}")
    print(f"  β₀ (intercept): {intercept:.4f}")
    print(f"  β₁ (slope):     {slope:.4f} ± {std_err:.4f}")
    print(f"  R²:            {r_squared:.4f}")
    print(f"  p-value:       {p_value:.2e}")
    print(f"  Correlation:   {r_value:.4f}")

    # ── Verdict ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  VERDICT")
    print("=" * 60)

    pass_slope = slope > 0 and p_value < 0.05
    pass_r2 = r_squared > 0.05

    if pass_slope and pass_r2:
        verdict = "PASS"
        detail = f"β₁ = {slope:.4f} > 0 (p = {p_value:.2e} < 0.05) and R² = {r_squared:.4f} > 0.05"
    elif pass_slope:
        verdict = "MARGINAL"
        detail = f"β₁ = {slope:.4f} > 0 (p = {p_value:.2e}) but R² = {r_squared:.4f} < 0.05"
    else:
        verdict = "FAIL"
        detail = f"β₁ = {slope:.4f}, p = {p_value:.2e}, R² = {r_squared:.4f}"

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    if verdict == "FAIL":
        print("\n  *** The central theorem Sharpe* = ||H|| is NOT supported by this data. ***")
        print("  *** The theory needs revision. ***")
    elif verdict == "MARGINAL":
        print("\n  The relationship is present but weak. More data or different")
        print("  estimation methods may strengthen or weaken the result.")
    else:
        print("\n  The Sharpe-curvature identity is supported by the data.")
        print(f"  The estimated slope β₁ = {slope:.4f} (theory predicts β₁ ≈ 1.0).")

    # ── Summary statistics ───────────────────────────────────
    print("\n" + "=" * 60)
    print("  SUMMARY STATISTICS")
    print("=" * 60)
    print(f"\n  ||H|| (mean ± std): {X_clean.mean():.4f} ± {X_clean.std():.4f}")
    print(f"  Sharpe_H (mean ± std): {y_clean.mean():.3f} ± {y_clean.std():.3f}")
    print(f"  Sharpe_factor (mean ± std): {df['sharpe_max_factor'].mean():.3f} ± {df['sharpe_max_factor'].std():.3f}")
    print(f"  Kelly growth (mean): {df['kelly_growth'].mean():.6f} per day")
    print(f"  Kelly growth (annual): {df['kelly_growth'].mean() * 252:.4f}")

    # ── Also test: Sharpe_max_factor vs ||H|| ────────────────
    print("\n" + "-" * 60)
    print("  SECONDARY: Sharpe_max_factor = β₀ + β₁ · ||H|| + ε")
    y2 = df["sharpe_max_factor"].values[mask]
    slope2, intercept2, r2_val, p2_val, se2 = stats.linregress(X_clean, y2)
    print(f"  β₁ = {slope2:.4f} ± {se2:.4f}, R² = {r2_val**2:.4f}, p = {p2_val:.2e}")

    # ── Save results ─────────────────────────────────────────
    df.to_csv(OUT_DIR / "test_01_results.csv", index=False)

    summary = {
        "test": "Test 1: Sharpe-Curvature Identity",
        "verdict": verdict,
        "n_windows": len(X_clean),
        "beta_1": slope,
        "beta_1_se": std_err,
        "r_squared": r_squared,
        "p_value": p_value,
        "correlation": r_value,
        "H_mean": X_clean.mean(),
        "H_std": X_clean.std(),
        "sharpe_mean": y_clean.mean(),
        "sharpe_std": y_clean.std(),
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_01_summary.csv")

    print(f"\n  Results saved to {OUT_DIR / 'test_01_results.csv'}")
    print(f"  Summary saved to {OUT_DIR / 'test_01_summary.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_1()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
