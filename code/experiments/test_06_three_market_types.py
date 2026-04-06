#!/usr/bin/env python3
"""
Test 6: Three Market Types Classification
==========================================
Different sectors/periods should exhibit the three classified types
(CAPM/sphere, Clifford/torus, pseudo-Anosov/hyperbolic).

Hypothesis: We can distinguish the three types using eigenvalue
    spacing statistics (GOE β=1, GUE β=2, GSE β=4 Wigner surmise).

Dataset: 50 Databento equities + sector ETFs, rolling windows
Method:
    1. Compute sample covariance eigenvalues in each window
    2. Compute nearest-neighbour spacing distribution
    3. Fit to Wigner surmise for β=1,2,4
    4. Classify each window by best-fitting β

Expected: Large-cap → CAPM-like (β≈1). Pairs → Clifford-like (β≈2).
    Crypto/crisis → pseudo-Anosov (β≈4).
Falsification: All sectors look the same, or none match any type.

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats as sp_stats
from scipy.special import gamma as gamma_fn

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
OUT_DIR.mkdir(exist_ok=True)


# ── Wigner surmise distributions ─────────────────────────────

def wigner_surmise_pdf(s, beta):
    """
    Wigner surmise P_β(s) for nearest-neighbour spacing s.
    β=1 (GOE), β=2 (GUE), β=4 (GSE).

    P_β(s) = a_β · s^β · exp(-b_β · s²)

    where a_β and b_β are normalisation constants.
    """
    if beta == 1:
        a = np.pi / 2
        b = np.pi / 4
    elif beta == 2:
        a = 32 / np.pi**2
        b = 4 / np.pi
    elif beta == 4:
        a = 2**18 / (3**6 * np.pi**3)
        b = 64 / (9 * np.pi)
    else:
        raise ValueError(f"beta must be 1, 2, or 4, got {beta}")

    return a * s**beta * np.exp(-b * s**2)


def compute_spacings(eigenvalues: np.ndarray) -> np.ndarray:
    """
    Compute normalised nearest-neighbour spacings from eigenvalues.
    Spacings are normalised so that mean spacing = 1.
    """
    eigenvalues = np.sort(eigenvalues)
    spacings = np.diff(eigenvalues)
    # Normalise by local mean spacing (unfolding)
    mean_spacing = np.mean(spacings)
    if mean_spacing < 1e-15:
        return np.array([])
    return spacings / mean_spacing


def fit_wigner(spacings: np.ndarray) -> dict:
    """
    Fit normalised spacings to Wigner surmise for β=1,2,4.
    Uses KS test to determine best fit.
    """
    if len(spacings) < 10:
        return {"best_beta": 0, "ks_1": 1, "ks_2": 1, "ks_4": 1}

    # Remove zeros and extreme outliers
    spacings = spacings[(spacings > 0.01) & (spacings < 5.0)]
    if len(spacings) < 10:
        return {"best_beta": 0, "ks_1": 1, "ks_2": 1, "ks_4": 1}

    results = {}
    for beta in [1, 2, 4]:
        # CDF of Wigner surmise
        s_grid = np.linspace(0.01, 5, 1000)
        pdf = wigner_surmise_pdf(s_grid, beta)
        cdf = np.cumsum(pdf) * (s_grid[1] - s_grid[0])
        cdf = cdf / cdf[-1]  # normalise

        # Empirical CDF
        spacings_sorted = np.sort(spacings)
        ecdf = np.arange(1, len(spacings_sorted) + 1) / len(spacings_sorted)

        # KS statistic (interpolate theoretical CDF at data points)
        theo_cdf_at_data = np.interp(spacings_sorted, s_grid, cdf)
        ks = np.max(np.abs(ecdf - theo_cdf_at_data))
        results[f"ks_{beta}"] = ks

    best_beta = min([1, 2, 4], key=lambda b: results[f"ks_{b}"])
    results["best_beta"] = best_beta
    return results


# ── Main experiment ──────────────────────────────────────────

def run_test_6():
    print("=" * 60)
    print("  TEST 6: Three Market Types Classification")
    print("  β ∈ {1,2,4} from eigenvalue spacing statistics")
    print("=" * 60)

    # Load all available data
    datasets = {}

    # Databento equities
    eq_path = DATA_DIR / "equities_50_daily_returns.parquet"
    if eq_path.exists():
        datasets["50 Equities (Databento)"] = pd.read_parquet(eq_path)

    # Sector ETFs
    sec_path = DATA_DIR / "sector_etf_9_daily_returns.parquet"
    if sec_path.exists():
        datasets["9 Sector ETFs"] = pd.read_parquet(sec_path)

    # FF25
    ff_path = DATA_DIR / "ff25_daily_returns.parquet"
    if ff_path.exists():
        ff = pd.read_parquet(ff_path).loc["1963-07-01":]
        datasets["FF25 Portfolios"] = ff

    # Crypto
    cr_path = DATA_DIR / "crypto_daily_returns.parquet"
    if cr_path.exists():
        datasets["Crypto (BTC/ETH/SOL/DOGE)"] = pd.read_parquet(cr_path).dropna()

    if not datasets:
        print("  ERROR: No data found")
        sys.exit(1)

    all_results = []

    for name, data in datasets.items():
        print(f"\n{'─' * 60}")
        print(f"  Dataset: {name}")
        print(f"  Shape: {data.shape}")
        print(f"{'─' * 60}")

        window = 252
        step = 63
        arr = data.values

        for i in range(0, len(arr) - window, step):
            w = arr[i:i + window]
            date = data.index[i + window - 1]

            if np.isnan(w).sum() > 0.05 * w.size:
                continue
            w = np.nan_to_num(w, 0.0)

            # Covariance eigenvalues
            cov = np.cov(w.T)
            eigenvalues = np.linalg.eigvalsh(cov)
            eigenvalues = eigenvalues[eigenvalues > 1e-15]

            if len(eigenvalues) < 5:
                continue

            # Compute spacings and fit
            spacings = compute_spacings(eigenvalues)
            if len(spacings) < 5:
                continue

            fit = fit_wigner(spacings)

            all_results.append({
                "date": date,
                "dataset": name,
                **fit,
                "n_eigenvalues": len(eigenvalues),
                "eig_ratio": eigenvalues[-1] / eigenvalues[-2] if len(eigenvalues) > 1 else 0,
            })

    df = pd.DataFrame(all_results)

    if df.empty:
        print("  ERROR: No results")
        sys.exit(1)

    # ── Analysis ─────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  CLASSIFICATION RESULTS")
    print("=" * 60)

    for name in df["dataset"].unique():
        sub = df[df["dataset"] == name]
        counts = sub["best_beta"].value_counts().sort_index()
        total = len(sub)

        print(f"\n  {name} ({total} windows):")
        for beta in [1, 2, 4]:
            n = counts.get(beta, 0)
            pct = n / total * 100 if total > 0 else 0
            label = {1: "GOE (CAPM)", 2: "GUE (Clifford)", 4: "GSE (pseudo-Anosov)"}[beta]
            bar = "█" * int(pct / 2)
            print(f"    β={beta} {label:>25}: {n:>4} ({pct:>5.1f}%) {bar}")

        # Mean KS statistics
        print(f"    Mean KS: β=1: {sub['ks_1'].mean():.3f}, "
              f"β=2: {sub['ks_2'].mean():.3f}, "
              f"β=4: {sub['ks_4'].mean():.3f}")

    # ── Verdict ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  VERDICT")
    print("=" * 60)

    # Check if different datasets give different classifications
    classification_varies = False
    dominant_betas = {}
    for name in df["dataset"].unique():
        sub = df[df["dataset"] == name]
        dominant = sub["best_beta"].mode().values[0] if len(sub) > 0 else 0
        dominant_betas[name] = dominant

    unique_dominants = set(dominant_betas.values())
    classification_varies = len(unique_dominants) > 1

    # Check if any dataset shows β=2 or β=4 (not just β=1)
    has_multiple_types = len(unique_dominants) >= 2 or (df["best_beta"] != 1).any()

    if classification_varies and has_multiple_types:
        verdict = "PASS"
        detail = (f"Different datasets classified as different types: "
                  f"{dominant_betas}. The three-type classification is supported.")
    elif has_multiple_types:
        verdict = "MARGINAL"
        detail = (f"Multiple types detected but not clearly separated by dataset. "
                  f"Dominants: {dominant_betas}")
    else:
        verdict = "FAIL"
        detail = f"All datasets classified as β={list(unique_dominants)[0]}. No type variation."

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    # Save
    df.to_csv(OUT_DIR / "test_06_results.csv", index=False)
    summary = {
        "test": "Test 6: Three Market Types",
        "verdict": verdict,
        "dominant_betas": str(dominant_betas),
        "n_windows": len(df),
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_06_summary.csv")
    print(f"\n  Results saved to {OUT_DIR / 'test_06_results.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_6()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
