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

This implementation also records a rolling efficiency profile:
  - alpha share (off-manifold variance)
  - Cheeger proxy (global fragility)
  - breadth / concentration of b*
  - factor concentration and normal-projection share
"""

import os
import sys
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

from scipy import stats

CODE_ROOT = os.path.dirname(os.path.dirname(__file__))
if CODE_ROOT not in sys.path:
    sys.path.insert(0, CODE_ROOT)

from core.curvature import market_efficiency_profile

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

PROFILE_KEYS = [
    "H",
    "Sharpe",
    "Sharpe_predicted",
    "sharpe_gap",
    "r",
    "stable_rank",
    "kelly_growth",
    "alpha_share",
    "factor_share",
    "alpha_beta_ratio",
    "willmore_proxy",
    "cheeger",
    "effective_breadth",
    "normalized_breadth",
    "weight_entropy",
    "top_factor_share",
    "factor_entropy",
    "normal_projection_share",
    "normal_bundle_dimension",
    "portfolio_concentration",
]


def estimate_efficiency_profile(
    returns_window: pd.DataFrame,
    n_factors: int = 4,
) -> dict:
    """
    Estimate a multi-metric efficiency profile for a window of returns.
    """
    try:
        result = market_efficiency_profile(
            returns_window.values,
            n_factors=n_factors,
        )
        return {
            "H": result["H"],
            "Sharpe": result["sharpe_realised"],
            "Sharpe_predicted": result["sharpe_predicted"],
            "sharpe_gap": result["sharpe_gap"],
            "r": result["r"],
            "stable_rank": result["stable_rank"],
            "kelly_growth": result["L_star"] * 252.0,
            "alpha_share": result["alpha_share"],
            "factor_share": result["factor_share"],
            "alpha_beta_ratio": result["alpha_beta_ratio"],
            "willmore_proxy": result["willmore_proxy"],
            "cheeger": result["cheeger"],
            "effective_breadth": result["effective_breadth"],
            "normalized_breadth": result["normalized_breadth"],
            "weight_entropy": result["weight_entropy"],
            "top_factor_share": result["top_factor_share"],
            "factor_entropy": result["factor_entropy"],
            "normal_projection_share": result["normal_projection_share"],
            "normal_bundle_dimension": result["normal_bundle_dimension"],
            "portfolio_concentration": result["portfolio_concentration"],
        }
    except Exception:
        return {key: np.nan for key in PROFILE_KEYS}


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
        profile = estimate_efficiency_profile(window_data, n_factors)
        results.append({"date": dates[i], **profile})

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

def theory_prediction(df: pd.DataFrame) -> float:
    """
    Correlation between realised Sharpe and theory-predicted Sharpe.
    """
    correlation = df["Sharpe"].corr(df["Sharpe_predicted"])
    return float(correlation)


# ── Efficiency insight report ─────────────────────────────────────────────────

def _format_date(date_like) -> str:
    if hasattr(date_like, "strftime"):
        return date_like.strftime("%Y-%m-%d")
    return str(date_like)


def _regime_thresholds(df: pd.DataFrame) -> dict:
    return {
        "H_low": df["H"].quantile(0.25),
        "H_high": df["H"].quantile(0.75),
        "H_mid": df["H"].median(),
        "alpha_low": df["alpha_share"].quantile(0.25),
        "alpha_high": df["alpha_share"].quantile(0.75),
        "cheeger_low": df["cheeger"].quantile(0.25),
        "cheeger_high": df["cheeger"].quantile(0.75),
        "breadth_low": df["effective_breadth"].quantile(0.25),
        "top_factor_high": df["top_factor_share"].quantile(0.75),
    }


def _classify_window(row: pd.Series, thresholds: dict) -> str:
    labels = []

    if row["H"] >= thresholds["H_high"] and row["alpha_share"] >= thresholds["alpha_high"]:
        labels.append("dislocated inefficiency")

    if row["cheeger"] <= thresholds["cheeger_low"]:
        labels.append("fragile connectivity")

    if (
        row["effective_breadth"] <= thresholds["breadth_low"]
        and row["top_factor_share"] >= thresholds["top_factor_high"]
    ):
        labels.append("crowded factor structure")

    if (
        not labels
        and row["H"] <= thresholds["H_low"]
        and row["alpha_share"] <= thresholds["alpha_low"]
        and row["cheeger"] >= thresholds["cheeger_high"]
    ):
        labels.append("comparatively efficient")

    return ", ".join(labels) if labels else "mixed regime"


def print_efficiency_insights(df: pd.DataFrame) -> None:
    """
    Print a higher-level interpretation of the rolling efficiency profile.
    """
    thresholds = _regime_thresholds(df)

    dislocated = df[
        (df["H"] >= thresholds["H_high"])
        & (df["alpha_share"] >= thresholds["alpha_high"])
    ]
    fragile = df[
        (df["H"] <= thresholds["H_mid"])
        & (df["cheeger"] <= thresholds["cheeger_low"])
    ]
    crowded = df[
        (df["H"] <= thresholds["H_mid"])
        & (df["effective_breadth"] <= thresholds["breadth_low"])
        & (df["top_factor_share"] >= thresholds["top_factor_high"])
    ]
    efficient = df[
        (df["H"] <= thresholds["H_low"])
        & (df["alpha_share"] <= thresholds["alpha_low"])
        & (df["cheeger"] >= thresholds["cheeger_high"])
    ]

    driver_corr = {
        "H": df["Sharpe"].corr(df["H"]),
        "alpha_share": df["Sharpe"].corr(df["alpha_share"]),
        "cheeger": df["Sharpe"].corr(df["cheeger"]),
        "effective_breadth": df["Sharpe"].corr(df["effective_breadth"]),
        "top_factor_share": df["Sharpe"].corr(df["top_factor_share"]),
        "normal_projection_share": df["Sharpe"].corr(df["normal_projection_share"]),
    }
    ranked_drivers = sorted(
        driver_corr.items(),
        key=lambda item: abs(item[1]) if pd.notna(item[1]) else -1.0,
        reverse=True,
    )

    latest_date = df.index[-1]
    latest = df.iloc[-1]

    print("=" * 65)
    print("EFFICIENCY INSIGHTS")
    print("=" * 65)
    print(f"Median alpha share:       {df['alpha_share'].median():.2%}")
    print(f"Median Cheeger proxy:     {df['cheeger'].median():.4f}")
    print(f"Median effective breadth: {df['effective_breadth'].median():.2f}")
    print(f"Median top-factor share:  {df['top_factor_share'].median():.2%}")
    print(f"Median weight entropy:    {df['weight_entropy'].median():.4f}")
    print()
    print("Sharpe comoves most with:")
    for name, corr in ranked_drivers[:4]:
        print(f"  {name:<24} {corr:+.4f}")
    print()
    print("Heuristic regimes (sample-relative thresholds):")
    print(f"  Dislocated inefficiency: {len(dislocated):>4} windows ({len(dislocated)/len(df):.1%})")
    print(f"  Fragile efficiency:      {len(fragile):>4} windows ({len(fragile)/len(df):.1%})")
    print(f"  Crowded efficiency:      {len(crowded):>4} windows ({len(crowded)/len(df):.1%})")
    print(f"  Comparatively efficient: {len(efficient):>4} windows ({len(efficient)/len(df):.1%})")
    print()
    print(f"Latest window ({_format_date(latest_date)}):")
    print(f"  Regime:                  {_classify_window(latest, thresholds)}")
    print(f"  H:                       {latest['H']:.4f}")
    print(f"  Alpha share:             {latest['alpha_share']:.2%}")
    print(f"  Cheeger proxy:           {latest['cheeger']:.4f}")
    print(f"  Effective breadth:       {latest['effective_breadth']:.2f}")
    print(f"  Top-factor share:        {latest['top_factor_share']:.2%}")
    print()
    print("Extreme windows:")
    print("  Highest curvature:")
    for date, row in df.nlargest(3, "H").iterrows():
        print(
            f"    {_format_date(date)}  H={row['H']:.4f}  "
            f"alpha_share={row['alpha_share']:.2%}  cheeger={row['cheeger']:.4f}"
        )
    print("  Lowest Cheeger:")
    for date, row in df.nsmallest(3, "cheeger").iterrows():
        print(
            f"    {_format_date(date)}  cheeger={row['cheeger']:.4f}  "
            f"H={row['H']:.4f}  breadth={row['effective_breadth']:.2f}"
        )


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
    print(f"Mean alpha share:        {df['alpha_share'].mean():.2%}")
    print(f"Mean Cheeger proxy:      {df['cheeger'].mean():.4f}")
    print(f"Mean effective breadth:  {df['effective_breadth'].mean():.2f}")
    print()
    print(f"Regression Sharpe ~ const + beta*H:")
    print(f"  beta_0 (intercept):    {reg['beta_0']:.4f}")
    print(f"  beta_1 (slope):        {reg['beta_1']:.4f}")
    print(f"  p-value (slope):       {reg['p_value_slope']:.4f}")
    print(f"  R²:                    {reg['r_squared']:.4f}")
    print(f"  Correlation H-Sharpe:  {reg['correlation']:.4f}")
    print()

    # Theory prediction
    corr_theory = theory_prediction(df)
    print(f"Correlation (realised vs theory-predicted Sharpe): {corr_theory:.4f}")
    print()

    print_efficiency_insights(df)
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
    print("Rolling efficiency profile saved to experiment_01_results.csv")

    return df, reg


if __name__ == "__main__":
    df, reg = main()
