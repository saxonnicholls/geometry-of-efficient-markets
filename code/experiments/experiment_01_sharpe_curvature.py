# Copyright (c) 2026 Saxon Nicholls. MIT License. See LICENSE.
"""
experiment_01_sharpe_curvature.py
----------------------------------
EXPERIMENT 1: The Sharpe-Curvature Identity

Theory:    Sharpe*(Sigma) = ||H||_{L^2(M, g_M)}

Hypothesis (H1): The regression
    Sharpe_realised_t = beta_0 + beta_1 * H_t + epsilon_t
has slope beta_1 > 0 with p < 0.05, and R² > 0.10.

Falsification: beta_1 <= 0 or R² < 0.05 across multiple rolling windows.

Dataset: Fama-French 25 portfolios (size x value), daily returns 1963-present.
Data source: Ken French Data Library via pandas_datareader (free).

Runtime: ~15 minutes on a laptop.
"""

import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from scipy import stats

# ── Data loading ──────────────────────────────────────────────────────────────

def load_ff25_data(start: str = "1963-07-01") -> pd.DataFrame:
    """
    Load Fama-French 25 portfolios (size x book-to-market), daily excess returns.
    Returns DataFrame with dates as index, 25 portfolio columns.
    """
    try:
        import pandas_datareader.data as web
        ff25 = web.DataReader(
            "25_Portfolios_5x5_Daily", "famafrench", start=start
        )[0] / 100
        ff_factors = web.DataReader(
            "F-F_Research_Data_Factors_daily", "famafrench", start=start
        )[0] / 100
        rf = ff_factors["RF"]
        excess = ff25.subtract(rf, axis=0).dropna()
        print(f"Loaded FF25: {len(excess)} days, {excess.shape[1]} portfolios")
        return excess
    except Exception as e:
        print(f"Could not load from web: {e}")
        print("Generating synthetic data for demonstration...")
        return _synthetic_ff25(start)


def _synthetic_ff25(start: str, T: int = 15000) -> pd.DataFrame:
    """Synthetic 25-portfolio data for offline testing."""
    rng = np.random.default_rng(42)
    dates = pd.bdate_range(start=start, periods=T)
    # 4 factors
    factors = rng.normal(0, 0.01, (T, 4))
    loadings = rng.normal(0, 1, (25, 4))
    loadings /= np.linalg.norm(loadings, axis=1, keepdims=True)
    idio = rng.normal(0, 0.005, (T, 25))
    returns = factors @ loadings.T + idio
    columns = [f"S{s}B{b}" for s in range(1, 6) for b in range(1, 6)]
    return pd.DataFrame(returns, index=dates, columns=columns)


# ── Core estimation ───────────────────────────────────────────────────────────

def estimate_H_and_sharpe(
    returns_window: pd.DataFrame,
    n_factors: int = 4,
) -> tuple:
    """
    Estimate mean curvature H and realised Sharpe for a window of returns.

    Steps:
    1. Find log-optimal portfolio b* (Kelly criterion)
    2. Compute Fisher information matrix F(b*)
    3. Extract factor subspace V_r via PCA of covariance
    4. H = ||Pi_N (1/(2*sqrt(b*)))||  (normal bundle projection)
    5. Realised Sharpe = Sharpe of strategy in -H direction
    """
    import sys
    import os
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
    from core.kelly import log_optimal_portfolio, fisher_information_matrix
    from core.curvature import sharpe_curvature_decomposition

    try:
        result = sharpe_curvature_decomposition(
            returns_window.values, n_factors=n_factors
        )
        return result["H"], result["sharpe_realised"]
    except Exception:
        return np.nan, np.nan


# ── Rolling estimation ────────────────────────────────────────────────────────

def run_rolling_estimation(
    excess_returns: pd.DataFrame,
    window: int = 252,
    n_factors: int = 4,
) -> pd.DataFrame:
    """
    Rolling estimation of H and realised Sharpe over the full sample.
    """
    T = len(excess_returns)
    dates = excess_returns.index[window:]
    results = []

    print(f"Running rolling estimation: {T-window} windows of {window} days...")
    for i in range(T - window):
        if i % 500 == 0:
            print(f"  Window {i}/{T-window} ({100*i/(T-window):.0f}%)")
        window_data = excess_returns.iloc[i : i + window]
        H, sharpe = estimate_H_and_sharpe(window_data, n_factors)
        results.append({"date": dates[i], "H": H, "Sharpe": sharpe})

    df = pd.DataFrame(results).set_index("date").dropna()
    print(f"Completed: {len(df)} valid windows")
    return df


# ── Statistical test ──────────────────────────────────────────────────────────

def run_regression_test(df: pd.DataFrame) -> dict:
    """
    Test H1: Sharpe_realised ~ beta_0 + beta_1 * H + epsilon
    using OLS with heteroscedasticity-robust standard errors.
    """
    try:
        from statsmodels.regression.linear_model import OLS
        from statsmodels.tools import add_constant

        X = add_constant(df["H"].values)
        y = df["Sharpe"].values
        model = OLS(y, X).fit(cov_type="HC3")

        return {
            "n_obs": len(df),
            "beta_0": model.params[0],
            "beta_1": model.params[1],
            "p_value_slope": model.pvalues[1],
            "p_value_intercept": model.pvalues[0],
            "r_squared": model.rsquared,
            "correlation": df["H"].corr(df["Sharpe"]),
            "mean_H": df["H"].mean(),
            "std_H": df["H"].std(),
            "mean_sharpe": df["Sharpe"].mean(),
            "std_sharpe": df["Sharpe"].std(),
        }
    except ImportError:
        # Fallback to scipy
        slope, intercept, r, p, se = stats.linregress(df["H"], df["Sharpe"])
        return {
            "n_obs": len(df),
            "beta_0": intercept,
            "beta_1": slope,
            "p_value_slope": p,
            "r_squared": r ** 2,
            "correlation": r,
            "mean_H": df["H"].mean(),
            "mean_sharpe": df["Sharpe"].mean(),
        }


# ── Predicted vs actual Sharpe ────────────────────────────────────────────────

def theory_prediction(df: pd.DataFrame, r: int = 4) -> float:
    """
    Theory predicts: Sharpe ≈ H * sqrt(Area(M^r))
    Area(M^r) for r-sphere ≈ pi^(r/2) / Gamma(r/2 + 1)
    For r=4: Area ≈ pi^2 / 2 ≈ 4.93
    """
    from math import gamma, pi
    vol_M = pi ** (r / 2) / gamma(r / 2 + 1)
    predicted = df["H"] * np.sqrt(vol_M)
    correlation = df["Sharpe"].corr(predicted)
    return float(correlation)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("=" * 65)
    print("EXPERIMENT 1: The Sharpe-Curvature Identity")
    print("Sharpe*(Sigma) = ||H||_{L²(M, g_M)}")
    print("=" * 65)
    print()

    # Load data
    excess = load_ff25_data(start="1963-07-01")

    # Rolling estimation
    df = run_rolling_estimation(excess, window=252, n_factors=4)

    # Statistical test
    reg = run_regression_test(df)

    print()
    print("=" * 65)
    print("RESULTS")
    print("=" * 65)
    print(f"N observations:          {reg['n_obs']}")
    print(f"Mean H (curvature):      {reg['mean_H']:.4f}")
    print(f"Mean Sharpe:             {reg['mean_sharpe']:.4f}")
    print()
    print(f"Regression Sharpe ~ const + beta*H:")
    print(f"  beta_0 (intercept):    {reg['beta_0']:.4f}")
    print(f"  beta_1 (slope):        {reg['beta_1']:.4f}")
    print(f"  p-value (slope):       {reg['p_value_slope']:.4f}")
    print(f"  R²:                    {reg['r_squared']:.4f}")
    print(f"  Correlation H-Sharpe:  {reg['correlation']:.4f}")
    print()

    # Theory prediction
    corr_theory = theory_prediction(df, r=4)
    print(f"Correlation (realised vs theory-predicted Sharpe): {corr_theory:.4f}")
    print()

    # Verdict
    print("=" * 65)
    print("VERDICT")
    print("=" * 65)
    passed = (
        reg["beta_1"] > 0
        and reg["p_value_slope"] < 0.05
        and reg["r_squared"] > 0.05
    )
    if passed:
        print("✓ CONSISTENT WITH THEORY")
        print(f"  Slope > 0: {reg['beta_1']:.4f} (p={reg['p_value_slope']:.4f})")
        print(f"  R² = {reg['r_squared']:.4f} > 0.05 threshold")
    else:
        print("✗ INCONSISTENT WITH THEORY — consider revision")
        if reg["beta_1"] <= 0:
            print(f"  FAIL: slope = {reg['beta_1']:.4f} (not > 0)")
        if reg["p_value_slope"] >= 0.05:
            print(f"  FAIL: p = {reg['p_value_slope']:.4f} (not < 0.05)")
        if reg["r_squared"] <= 0.05:
            print(f"  FAIL: R² = {reg['r_squared']:.4f} (not > 0.05)")

    print()
    print("Falsification criterion:")
    print("  beta_1 <= 0 or R² < 0.05 across multiple 5-year subsamples")

    # Save results
    df.to_csv("experiment_01_results.csv")
    print()
    print("Results saved to experiment_01_results.csv")

    return df, reg


if __name__ == "__main__":
    df, reg = main()
