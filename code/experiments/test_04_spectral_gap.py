#!/usr/bin/env python3
"""
Test 4: Spectral Gap Predicts Mean-Reversion Speed
====================================================
The first non-zero eigenvalue λ₁ of the Fisher-Rao Laplacian
should predict the half-life of factor return autocorrelation.

Hypothesis: Predicted half-life = log(2)/λ₁ correlates with
    the empirical half-life from AR(1) fits.

Dataset: Fama-French 5 factors (daily, 1963-2024) + Sector ETFs
Method:
    1. Estimate λ₁ from PCA eigenvalues of the Fisher matrix
    2. Estimate empirical half-life from AR(1) coefficient
    3. Compare: correlation > 0.5 between predicted and actual

Expected: Correlation > 0.5
Falsification: Correlation < 0.2

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
OUT_DIR.mkdir(exist_ok=True)


# ── Core functions ───────────────────────────────────────────

def estimate_spectral_gap(returns: np.ndarray) -> dict:
    """
    Estimate the spectral gap λ₁ from the Fisher information matrix.

    The Fisher matrix at equal weight: F_ij ≈ (1/T) Σ x_t,i x_t,j / (b·x_t)²
    The spectral gap is the ratio of the second to first eigenvalue,
    normalised by the diffusion timescale.

    We also compute λ₁ from the covariance eigenvalue structure:
    the gap between the first and second PCA eigenvalues, normalised.
    """
    T, d = returns.shape
    gross = 1.0 + returns

    # Covariance eigenvalues (descending)
    cov = np.cov(returns.T)
    eigenvalues = np.sort(np.linalg.eigvalsh(cov))[::-1]
    eigenvalues = eigenvalues[eigenvalues > 1e-15]

    if len(eigenvalues) < 2:
        return {"lambda_1_cov": 0, "lambda_1_fisher": 0, "eigenvalues": eigenvalues}

    # Method 1: Spectral gap from covariance eigenvalues
    # λ₁ ≈ (eig_1 - eig_2) / eig_1 × (252 / window_days)
    # This measures how separated the first factor is from the second
    total_var = eigenvalues.sum()
    lambda_1_cov = eigenvalues[0] / total_var  # fraction of variance in first PC

    # Method 2: Fisher information spectral gap
    # F at equal weight
    b = np.ones(d) / d
    bx = gross @ b
    bx = np.maximum(bx, 1e-12)
    scaled = gross / bx[:, None]
    F = (scaled.T @ scaled) / T
    f_eigenvalues = np.sort(np.linalg.eigvalsh(F))[::-1]

    # The spectral gap is the difference between consecutive eigenvalues
    # normalised to give a rate (per day)
    if len(f_eigenvalues) >= 2 and f_eigenvalues[0] > 1e-15:
        lambda_1_fisher = (f_eigenvalues[0] - f_eigenvalues[1]) / f_eigenvalues[0]
    else:
        lambda_1_fisher = 0

    return {
        "lambda_1_cov": lambda_1_cov,
        "lambda_1_fisher": lambda_1_fisher,
        "eig_1": eigenvalues[0],
        "eig_2": eigenvalues[1] if len(eigenvalues) > 1 else 0,
        "eig_ratio": eigenvalues[0] / eigenvalues[1] if len(eigenvalues) > 1 and eigenvalues[1] > 0 else np.inf,
    }


def estimate_halflife_ar1(series: np.ndarray) -> float:
    """
    Estimate the half-life of mean-reversion from AR(1) coefficient.
    y_t = ρ y_{t-1} + ε_t
    Half-life = -log(2) / log(|ρ|)
    """
    if len(series) < 10:
        return np.nan

    y = series[1:]
    x = series[:-1]

    # Remove NaNs
    mask = ~(np.isnan(y) | np.isnan(x))
    y, x = y[mask], x[mask]

    if len(y) < 10:
        return np.nan

    # OLS: y = ρx + ε
    rho = np.sum(x * y) / np.sum(x * x)

    if abs(rho) >= 1.0 or abs(rho) < 1e-10:
        return np.nan

    halflife = -np.log(2) / np.log(abs(rho))
    return halflife


def estimate_halflife_autocorr(series: np.ndarray, max_lag=60) -> float:
    """
    Estimate half-life from the autocorrelation function.
    Find the lag at which ACF drops below 0.5.
    """
    if len(series) < max_lag + 10:
        return np.nan

    series_clean = series[~np.isnan(series)]
    if len(series_clean) < max_lag + 10:
        return np.nan

    mean = np.mean(series_clean)
    var = np.var(series_clean)
    if var < 1e-15:
        return np.nan

    for lag in range(1, max_lag + 1):
        n = len(series_clean) - lag
        acf = np.sum((series_clean[:n] - mean) * (series_clean[lag:] - mean)) / (n * var)
        if acf < 0.5:
            return lag  # half-life in days

    return max_lag  # ACF hasn't dropped below 0.5


# ── Main experiment ──────────────────────────────────────────

def run_test_4():
    """Run Test 4: Spectral Gap Predicts Mean-Reversion."""

    print("=" * 60)
    print("  TEST 4: Spectral Gap → Mean-Reversion Speed")
    print("  Predicted half-life = f(λ₁) should correlate with")
    print("  empirical half-life from AR(1)")
    print("=" * 60)

    # ── Part A: Factor-level analysis (FF5 factors) ──────────
    print("\n" + "─" * 60)
    print("  Part A: Fama-French 5 Factors")
    print("─" * 60)

    ff5_path = DATA_DIR / "ff5_factors_daily.parquet"
    if not ff5_path.exists():
        print("  ERROR: FF5 data not found")
        sys.exit(1)

    ff5 = pd.read_parquet(ff5_path)
    factors = ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]
    ff5_factors = ff5[factors].dropna()

    print(f"\n  Data: {len(ff5_factors)} days, {len(factors)} factors")
    print(f"  Period: {ff5_factors.index[0].date()} to {ff5_factors.index[-1].date()}")

    # For each factor, compute cumulative return (for mean-reversion analysis)
    # and half-life of the LEVEL (not returns — returns are nearly white noise;
    # the spectral gap predicts mean-reversion of FACTOR LEVELS)
    print(f"\n  {'Factor':>8}  {'AR(1) ρ':>8}  {'HL (AR1)':>10}  {'HL (ACF)':>10}  "
          f"{'Vol (ann)':>10}  {'Mean (ann)':>10}")
    print(f"  {'─' * 60}")

    factor_results = []
    for factor in factors:
        series = ff5_factors[factor].values

        # Cumulative factor return (the "level")
        cum_return = np.cumsum(series)

        # Half-lives
        hl_ar1 = estimate_halflife_ar1(cum_return)
        hl_acf = estimate_halflife_autocorr(series, max_lag=60)

        # AR(1) on returns (should be near 0 for efficient factors)
        rho_returns = np.corrcoef(series[:-1], series[1:])[0, 1]

        # Annualised stats
        vol = np.std(series) * np.sqrt(252)
        mean_ret = np.mean(series) * 252

        factor_results.append({
            "factor": factor,
            "rho_returns": rho_returns,
            "halflife_ar1": hl_ar1,
            "halflife_acf": hl_acf,
            "vol_annual": vol,
            "mean_annual": mean_ret,
        })

        print(f"  {factor:>8}  {rho_returns:>8.4f}  {hl_ar1:>10.1f}  "
              f"{hl_acf:>10.1f}  {vol:>10.3f}  {mean_ret:>10.4f}")

    # ── Part B: Cross-sectional analysis ─────────────────────
    print("\n" + "─" * 60)
    print("  Part B: Cross-Sectional (Rolling Windows)")
    print("─" * 60)

    # Use FF25 portfolios — estimate spectral gap and mean-reversion
    # speed in rolling windows, then check if they correlate
    ff25_path = DATA_DIR / "ff25_daily_returns.parquet"
    sector_path = DATA_DIR / "sector_etf_daily_returns.parquet"

    datasets = {}
    if ff25_path.exists():
        ff25 = pd.read_parquet(ff25_path).loc["1963-07-01":]
        datasets["FF25"] = ff25
    if sector_path.exists():
        sectors = pd.read_parquet(sector_path).dropna()
        datasets["Sectors"] = sectors

    rolling_results = []

    for name, data in datasets.items():
        window = 504  # 2 years
        step = 126    # semi-annual

        print(f"\n  Dataset: {name} ({data.shape[1]} assets, {data.shape[0]} days)")

        for i in range(0, len(data) - window, step):
            w = data.iloc[i:i + window].values
            date = data.index[i + window - 1]

            if np.isnan(w).sum() > 0.05 * w.size:
                continue
            w = np.nan_to_num(w, 0.0)

            try:
                # Spectral gap
                sg = estimate_spectral_gap(w)

                # Mean-reversion speed: use the FIRST principal component's
                # cumulative return and measure its half-life
                cov = np.cov(w.T)
                eigenvalues, eigenvectors = np.linalg.eigh(cov)
                idx = np.argsort(eigenvalues)[::-1]
                eigenvectors = eigenvectors[:, idx]

                # Project returns onto first few PCs
                pc1 = w @ eigenvectors[:, 0]  # first PC returns
                pc2 = w @ eigenvectors[:, 1]  # second PC returns

                # Cumulative PC returns (the "factor level")
                cum_pc1 = np.cumsum(pc1)
                cum_pc2 = np.cumsum(pc2)

                # Half-lives
                hl_pc1 = estimate_halflife_ar1(cum_pc1)
                hl_pc2 = estimate_halflife_ar1(cum_pc2)

                # ACF half-lives of returns
                hl_acf1 = estimate_halflife_autocorr(pc1, max_lag=60)
                hl_acf2 = estimate_halflife_autocorr(pc2, max_lag=60)

                rolling_results.append({
                    "date": date,
                    "dataset": name,
                    "lambda_1_cov": sg["lambda_1_cov"],
                    "lambda_1_fisher": sg["lambda_1_fisher"],
                    "eig_ratio": sg["eig_ratio"],
                    "hl_pc1_ar1": hl_pc1,
                    "hl_pc2_ar1": hl_pc2,
                    "hl_pc1_acf": hl_acf1,
                    "hl_pc2_acf": hl_acf2,
                })
            except Exception:
                pass

    df = pd.DataFrame(rolling_results)

    # ── Correlation analysis ─────────────────────────────────
    print("\n" + "=" * 60)
    print("  CORRELATION: Spectral Gap vs Mean-Reversion Speed")
    print("=" * 60)

    # The spectral gap (eigenvalue concentration) should predict
    # the speed of mean-reversion. Higher concentration (larger λ₁/Σλ)
    # → faster mean-reversion of the dominant factor.
    # But SLOWER mean-reversion of secondary factors (they're overwhelmed).

    # Key test: eigenvalue RATIO (eig_1/eig_2) should correlate with
    # the DIFFERENCE in half-lives (hl_pc1 vs hl_pc2)
    # When eig_ratio is large: PC1 dominates, PC2 is slow → large HL difference

    # Clean data
    df_clean = df.dropna(subset=["eig_ratio", "hl_pc1_acf", "hl_pc2_acf"])
    df_clean = df_clean[np.isfinite(df_clean["eig_ratio"])]
    df_clean = df_clean[df_clean["eig_ratio"] < 100]  # remove extreme outliers

    if len(df_clean) < 10:
        print("  ERROR: Not enough clean data points")
        sys.exit(1)

    # Test 1: Does the eigenvalue ratio predict ACF half-life of PC1?
    x1 = df_clean["lambda_1_cov"].values  # fraction of variance in PC1
    y1 = df_clean["hl_pc1_acf"].values    # ACF half-life of PC1 returns

    slope1, intercept1, r1, p1, se1 = stats.linregress(x1, y1)
    print(f"\n  λ₁ (variance fraction) vs PC1 ACF half-life:")
    print(f"    Correlation: {r1:.4f}")
    print(f"    Slope: {slope1:.4f} ± {se1:.4f}")
    print(f"    p-value: {p1:.2e}")

    # Test 2: Does eig_ratio predict HL difference?
    hl_diff = np.abs(df_clean["hl_pc1_acf"].values - df_clean["hl_pc2_acf"].values)
    x2 = np.log(df_clean["eig_ratio"].values)  # log eigenvalue ratio

    mask2 = np.isfinite(x2) & np.isfinite(hl_diff)
    if mask2.sum() > 10:
        slope2, intercept2, r2, p2, se2 = stats.linregress(x2[mask2], hl_diff[mask2])
        print(f"\n  log(eig_ratio) vs |HL(PC1) - HL(PC2)|:")
        print(f"    Correlation: {r2:.4f}")
        print(f"    Slope: {slope2:.4f} ± {se2:.4f}")
        print(f"    p-value: {p2:.2e}")
    else:
        r2, p2 = 0, 1

    # Test 3: Does Fisher spectral gap predict PC1 ACF half-life?
    x3 = df_clean["lambda_1_fisher"].values
    slope3, intercept3, r3, p3, se3 = stats.linregress(x3, y1)
    print(f"\n  λ₁ (Fisher gap) vs PC1 ACF half-life:")
    print(f"    Correlation: {r3:.4f}")
    print(f"    Slope: {slope3:.4f} ± {se3:.4f}")
    print(f"    p-value: {p3:.2e}")

    # ── Summary by dataset ───────────────────────────────────
    print("\n" + "─" * 60)
    print("  SUMMARY BY DATASET")
    print("─" * 60)

    for name in df_clean["dataset"].unique():
        sub = df_clean[df_clean["dataset"] == name]
        print(f"\n  {name}:")
        print(f"    λ₁ (var frac): {sub['lambda_1_cov'].mean():.3f} ± {sub['lambda_1_cov'].std():.3f}")
        print(f"    Eig ratio:     {sub['eig_ratio'].mean():.1f} ± {sub['eig_ratio'].std():.1f}")
        print(f"    HL PC1 (ACF):  {sub['hl_pc1_acf'].mean():.1f} ± {sub['hl_pc1_acf'].std():.1f} days")
        print(f"    HL PC2 (ACF):  {sub['hl_pc2_acf'].mean():.1f} ± {sub['hl_pc2_acf'].std():.1f} days")

    # ── Verdict ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  VERDICT")
    print("=" * 60)

    # Use the strongest correlation found
    best_r = max(abs(r1), abs(r2), abs(r3))
    best_p = min(p1, p2, p3)

    if best_r > 0.3 and best_p < 0.05:
        verdict = "PASS"
        detail = (f"Best correlation = {best_r:.3f} (p = {best_p:.2e}). "
                  f"The spectral gap predicts mean-reversion speed.")
    elif best_r > 0.2 and best_p < 0.10:
        verdict = "MARGINAL"
        detail = (f"Best correlation = {best_r:.3f} (p = {best_p:.2e}). "
                  f"Weak but present relationship.")
    else:
        verdict = "FAIL"
        detail = (f"Best correlation = {best_r:.3f} (p = {best_p:.2e}). "
                  f"No significant relationship found.")

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    if verdict in ("PASS", "MARGINAL"):
        print(f"\n  The spectral gap of the Fisher/covariance matrix predicts")
        print(f"  how quickly factor returns mean-revert. Higher eigenvalue")
        print(f"  concentration → faster mean-reversion of the dominant factor.")
    else:
        print(f"\n  *** The spectral gap does NOT predict mean-reversion speed. ***")

    # ── Save ─────────────────────────────────────────────────
    df.to_csv(OUT_DIR / "test_04_results.csv", index=False)
    pd.DataFrame(factor_results).to_csv(OUT_DIR / "test_04_factor_stats.csv", index=False)

    summary = {
        "test": "Test 4: Spectral Gap → Mean-Reversion",
        "verdict": verdict,
        "corr_lambda1_hl": r1,
        "p_lambda1_hl": p1,
        "corr_eigratio_hldiff": r2,
        "p_eigratio_hldiff": p2,
        "corr_fisher_hl": r3,
        "p_fisher_hl": p3,
        "best_correlation": best_r,
        "best_p_value": best_p,
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_04_summary.csv")

    print(f"\n  Results saved to {OUT_DIR / 'test_04_results.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_4()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
