#!/usr/bin/env python3
"""
Test 4 (v2): Spectral Gap Predicts Mean-Reversion Speed
=========================================================
REVISED: Use monthly factor returns and spread half-lives.

The spectral gap λ₁ should predict how quickly factor SPREADS
(long-short portfolios) mean-revert. Factors with larger eigenvalue
gaps should have faster mean-reversion.

Method: For the FF5 factors, each is already a long-short spread.
    Measure the half-life of each factor's cumulative return from
    its trailing mean, using monthly data. Compare to the eigenvalue
    structure.

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


def halflife_OU(series: np.ndarray) -> float:
    """
    Estimate half-life from OU model: dx = -κ(x - μ)dt + σdW.
    Regress Δx on x: Δx_t = a + b·x_t + ε. Then κ = -b, HL = log(2)/κ.
    Uses the level series (cumulated returns minus trailing mean).
    """
    if len(series) < 20:
        return np.nan

    dx = np.diff(series)
    x = series[:-1]

    mask = ~(np.isnan(dx) | np.isnan(x))
    dx, x = dx[mask], x[mask]
    if len(dx) < 20:
        return np.nan

    # OLS: Δx = a + b·x
    X = np.column_stack([np.ones(len(x)), x])
    try:
        beta = np.linalg.lstsq(X, dx, rcond=None)[0]
        b = beta[1]
    except Exception:
        return np.nan

    if b >= 0:  # not mean-reverting
        return np.nan

    kappa = -b
    halflife = np.log(2) / kappa
    return halflife


def run_test_4v2():
    print("=" * 60)
    print("  TEST 4 (v2): Spectral Gap → Factor Mean-Reversion")
    print("  Using monthly data and OU half-life estimation")
    print("=" * 60)

    # ── Load monthly FF5 factors ─────────────────────────────
    ff5_daily_path = DATA_DIR / "ff5_factors_daily.parquet"
    if not ff5_daily_path.exists():
        print("  ERROR: FF5 data not found")
        sys.exit(1)

    ff5_daily = pd.read_parquet(ff5_daily_path)
    factors = ["Mkt-RF", "SMB", "HML", "RMW", "CMA"]

    # Resample to monthly
    ff5_monthly = ff5_daily[factors].resample("ME").sum()
    ff5_monthly = ff5_monthly.dropna()

    print(f"\n  Monthly factor data: {len(ff5_monthly)} months")
    print(f"  Period: {ff5_monthly.index[0].date()} to {ff5_monthly.index[-1].date()}")

    # ── For each factor: compute eigenvalue rank and half-life ─
    # The eigenvalue rank comes from the covariance of the FF25 portfolios
    ff25_daily_path = DATA_DIR / "ff25_daily_returns.parquet"
    ff25 = pd.read_parquet(ff25_daily_path).loc["1963-07-01":]
    ff25_monthly = ff25.resample("ME").sum().dropna()

    # Full-sample PCA eigenvalues
    cov_full = np.cov(ff25_monthly.values.T)
    eigenvalues = np.sort(np.linalg.eigvalsh(cov_full))[::-1]
    eigenvalues = eigenvalues[eigenvalues > 0]

    print(f"\n  PCA eigenvalues (monthly FF25, top 8):")
    for i, ev in enumerate(eigenvalues[:8]):
        pct = ev / eigenvalues.sum() * 100
        cum = eigenvalues[:i+1].sum() / eigenvalues.sum() * 100
        print(f"    λ_{i+1} = {ev:.6f} ({pct:.1f}%, cumulative {cum:.1f}%)")

    # ── Compute half-lives for each factor ───────────────────
    print(f"\n  Factor mean-reversion analysis (monthly):")
    print(f"  {'Factor':>8}  {'Vol (ann)':>10}  {'OU HL (months)':>15}  "
          f"{'AR(1) ρ':>8}  {'AR(1) HL':>10}")
    print(f"  {'─' * 60}")

    factor_stats = []
    for factor in factors:
        series = ff5_monthly[factor].values

        # Cumulative return (the "spread level")
        cum = np.cumsum(series)

        # Detrend: subtract trailing 24-month mean
        window = min(24, len(cum) // 4)
        if window < 6:
            window = 6
        trailing_mean = pd.Series(cum).rolling(window, min_periods=1).mean().values
        detrended = cum - trailing_mean

        # OU half-life on detrended level
        hl_ou = halflife_OU(detrended)

        # AR(1) on monthly returns
        rho = np.corrcoef(series[:-1], series[1:])[0, 1]
        if abs(rho) < 1 and abs(rho) > 1e-10:
            hl_ar1 = -np.log(2) / np.log(abs(rho))
        else:
            hl_ar1 = np.nan

        vol = np.std(series) * np.sqrt(12)

        factor_stats.append({
            "factor": factor,
            "vol_annual": vol,
            "halflife_ou_months": hl_ou,
            "ar1_rho": rho,
            "ar1_halflife_months": hl_ar1,
        })

        print(f"  {factor:>8}  {vol:>10.3f}  {hl_ou:>15.1f}  "
              f"{rho:>8.4f}  {hl_ar1:>10.1f}")

    # ── Rolling analysis: does the spectral gap vary with HL? ──
    print(f"\n" + "─" * 60)
    print(f"  Rolling analysis: 5-year windows, monthly")
    print(f"─" * 60)

    window = 60  # 5 years monthly
    step = 12    # annual

    rolling_results = []
    for i in range(0, len(ff25_monthly) - window, step):
        w = ff25_monthly.iloc[i:i + window].values
        date = ff25_monthly.index[i + window - 1]

        cov = np.cov(w.T)
        eigs = np.sort(np.linalg.eigvalsh(cov))[::-1]
        eigs = eigs[eigs > 0]

        # Eigenvalue concentration: fraction in top eigenvalue
        lambda1_frac = eigs[0] / eigs.sum() if eigs.sum() > 0 else 0
        eig_ratio = eigs[0] / eigs[1] if len(eigs) > 1 and eigs[1] > 0 else np.inf

        # Factor half-lives in this window
        factor_hls = {}
        for factor in factors:
            f_series = ff5_monthly[factor].iloc[i:i + window].values
            cum = np.cumsum(f_series)
            trailing = pd.Series(cum).rolling(24, min_periods=6).mean().values
            detrended = cum - trailing
            hl = halflife_OU(detrended)
            factor_hls[f"hl_{factor}"] = hl

        # Average half-life (excluding NaN)
        hls = [v for v in factor_hls.values() if np.isfinite(v) and v > 0]
        avg_hl = np.mean(hls) if hls else np.nan

        rolling_results.append({
            "date": date,
            "lambda1_frac": lambda1_frac,
            "eig_ratio": eig_ratio,
            "avg_halflife": avg_hl,
            **factor_hls,
        })

    rdf = pd.DataFrame(rolling_results)
    rdf_clean = rdf.dropna(subset=["lambda1_frac", "avg_halflife"])
    rdf_clean = rdf_clean[np.isfinite(rdf_clean["eig_ratio"]) & (rdf_clean["eig_ratio"] < 100)]

    print(f"\n  {len(rdf_clean)} valid rolling windows")

    if len(rdf_clean) > 10:
        # Key regression: eigenvalue concentration vs average half-life
        x = rdf_clean["lambda1_frac"].values
        y = rdf_clean["avg_halflife"].values

        slope, intercept, r_val, p_val, se = stats.linregress(x, y)
        print(f"\n  λ₁ fraction vs avg factor half-life:")
        print(f"    Correlation: {r_val:.4f}")
        print(f"    Slope: {slope:.2f} ± {se:.2f}")
        print(f"    p-value: {p_val:.2e}")

        # Also: eigenvalue ratio vs half-life
        x2 = np.log(rdf_clean["eig_ratio"].values)
        slope2, int2, r2, p2, se2 = stats.linregress(x2, y)
        print(f"\n  log(eig_ratio) vs avg factor half-life:")
        print(f"    Correlation: {r2:.4f}")
        print(f"    Slope: {slope2:.2f} ± {se2:.2f}")
        print(f"    p-value: {p2:.2e}")

        best_r = max(abs(r_val), abs(r2))
        best_p = min(p_val, p2)
    else:
        best_r, best_p = 0, 1
        r_val, p_val = 0, 1
        r2, p2 = 0, 1

    # ── Verdict ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  VERDICT")
    print("=" * 60)

    if best_r > 0.3 and best_p < 0.05:
        verdict = "PASS"
        detail = f"Best correlation = {best_r:.3f} (p = {best_p:.2e})"
    elif best_r > 0.15 and best_p < 0.10:
        verdict = "MARGINAL"
        detail = f"Best correlation = {best_r:.3f} (p = {best_p:.2e})"
    else:
        verdict = "FAIL"
        detail = f"Best correlation = {best_r:.3f} (p = {best_p:.2e})"

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    # ── Save ─────────────────────────────────────────────────
    rdf.to_csv(OUT_DIR / "test_04_v2_results.csv", index=False)
    pd.DataFrame(factor_stats).to_csv(OUT_DIR / "test_04_v2_factor_stats.csv", index=False)

    summary = {
        "test": "Test 4v2: Spectral Gap → Mean-Reversion (monthly)",
        "verdict": verdict,
        "corr_lambda1_hl": r_val,
        "p_lambda1_hl": p_val,
        "corr_eigratio_hl": r2,
        "p_eigratio_hl": p2,
        "best_correlation": best_r,
        "best_p_value": best_p,
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_04_v2_summary.csv")

    print(f"\n  Results saved to {OUT_DIR / 'test_04_v2_results.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_4v2()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
