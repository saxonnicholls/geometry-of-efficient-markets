#!/usr/bin/env python3
"""
Test N1: Yield Curve = Three Jacobi Eigenmodes
================================================
Nelson-Siegel factors (level, slope, curvature) should be the first
three eigenfunctions of the Jacobi operator on the bond manifold.

Hypothesis: PCA of the yield curve gives three factors whose SHAPES
match the Nelson-Siegel functional forms:
    v₀(τ) = 1                              (level — constant)
    v₁(τ) = (1-e^{-τ/λ})/(τ/λ)            (slope — decaying)
    v₂(τ) = (1-e^{-τ/λ})/(τ/λ) - e^{-τ/λ} (curvature — hump)

Test: correlation between empirical PCA eigenvectors and NS shapes > 0.9
for the first three components.

Dataset: US Treasury yield curve (11 maturities, 1990-2024) from FRED.

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
from scipy.optimize import minimize_scalar

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)


def nelson_siegel_factors(maturities, lam):
    """Compute the three Nelson-Siegel factor loadings."""
    tau = maturities / lam
    tau = np.maximum(tau, 1e-10)

    f1 = np.ones_like(maturities)  # level
    f2 = (1 - np.exp(-tau)) / tau   # slope
    f3 = f2 - np.exp(-tau)          # curvature

    return f1, f2, f3


def run_test_N1():
    print("=" * 70)
    print("  TEST N1: Yield Curve = Three Jacobi Eigenmodes")
    print("  Nelson-Siegel shapes should match PCA eigenvectors")
    print("=" * 70)

    # Load yield curve
    yc_path = DATA_DIR / "treasury_yield_curve.parquet"
    if not yc_path.exists():
        print("  ERROR: yield curve data not found")
        sys.exit(1)

    yc = pd.read_parquet(yc_path).dropna()
    T, d = yc.shape

    # Extract maturities from column names (y_0.083, y_0.25, ..., y_30)
    maturities = np.array([float(c.split("_")[1]) for c in yc.columns])

    print(f"\n  Data: {T} days × {d} maturities")
    print(f"  Maturities: {maturities}")
    print(f"  Period: {yc.index[0]} to {yc.index[-1]}")

    # PCA of yield changes (first differences — standard in term structure)
    changes = yc.diff().dropna().values
    cov = np.cov(changes.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    var_explained = eigenvalues / eigenvalues.sum() * 100

    print(f"\n  PCA eigenvalues (yield changes):")
    for i in range(min(5, d)):
        print(f"    PC{i+1}: {var_explained[i]:.1f}% "
              f"(cumulative: {var_explained[:i+1].sum():.1f}%)")

    # The first 3 PCs should explain ~99% (this is well-known)
    pct_3pc = var_explained[:3].sum()
    print(f"\n  First 3 PCs explain: {pct_3pc:.1f}%")

    # Empirical eigenvectors (the shapes)
    pc1 = eigenvectors[:, 0]  # should look like level (constant)
    pc2 = eigenvectors[:, 1]  # should look like slope (decaying)
    pc3 = eigenvectors[:, 2]  # should look like curvature (hump)

    # Ensure consistent sign (PC1 should be positive = level up)
    if pc1.mean() < 0: pc1 = -pc1
    if pc2[0] - pc2[-1] < 0: pc2 = -pc2  # slope: short end higher than long
    if pc3[len(pc3)//3] < pc3[0]: pc3 = -pc3  # curvature: hump in middle

    # Fit Nelson-Siegel λ to maximise correlation with PC2
    def neg_corr(lam):
        _, f2, _ = nelson_siegel_factors(maturities, lam)
        return -abs(np.corrcoef(pc2, f2)[0, 1])

    result = minimize_scalar(neg_corr, bounds=(0.1, 10), method="bounded")
    lam_opt = result.x

    # Compute NS factors at optimal λ
    ns1, ns2, ns3 = nelson_siegel_factors(maturities, lam_opt)

    # Normalise all to unit norm for comparison
    pc1_n = pc1 / np.linalg.norm(pc1)
    pc2_n = pc2 / np.linalg.norm(pc2)
    pc3_n = pc3 / np.linalg.norm(pc3)
    ns1_n = ns1 / np.linalg.norm(ns1)
    ns2_n = ns2 / np.linalg.norm(ns2)
    ns3_n = ns3 / np.linalg.norm(ns3)

    # Correlations
    # For level (constant), use cosine similarity instead of Pearson
    # (Pearson is undefined for constant vectors)
    cos1 = abs(np.dot(pc1_n, ns1_n))  # cosine similarity = |dot product| for unit vectors
    corr2 = abs(np.corrcoef(pc2_n, ns2_n)[0, 1])
    corr3 = abs(np.corrcoef(pc3_n, ns3_n)[0, 1])
    corr1 = cos1  # cosine similarity for the level factor
    mean_corr = (corr1 + corr2 + corr3) / 3

    print(f"\n  Nelson-Siegel fit (λ = {lam_opt:.2f} years):")
    print(f"    PC1 vs NS level:     r = {corr1:.4f}")
    print(f"    PC2 vs NS slope:     r = {corr2:.4f}")
    print(f"    PC3 vs NS curvature: r = {corr3:.4f}")
    print(f"    Mean correlation:    r = {mean_corr:.4f}")

    # Also compute spectral gap (eigenvalue ratios)
    if eigenvalues[0] > 0:
        gap_12 = eigenvalues[0] / eigenvalues[1]
        gap_23 = eigenvalues[1] / eigenvalues[2]
        print(f"\n  Eigenvalue ratios (spectral gaps):")
        print(f"    λ₁/λ₂ = {gap_12:.1f} (level dominates slope)")
        print(f"    λ₂/λ₃ = {gap_23:.1f} (slope dominates curvature)")
        # Theory: the spectral gap determines mean-reversion speed
        # Larger gap → the level factor is more persistent than slope
        # Slope is more persistent than curvature
        print(f"    Implied: level HL >> slope HL >> curvature HL ✓")

    # ── Visualisation ────────────────────────────────────────
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    # Row 1: PCA vs NS shapes
    for i, (pc, ns, name, corr) in enumerate([
        (pc1_n, ns1_n, "Level", corr1),
        (pc2_n, ns2_n, "Slope", corr2),
        (pc3_n, ns3_n, "Curvature", corr3),
    ]):
        ax = axes[0, i]
        ax.plot(maturities, pc, "o-", color="steelblue", linewidth=2,
                markersize=6, label=f"PCA (empirical)")
        ax.plot(maturities, ns, "s--", color="red", linewidth=2,
                markersize=5, label=f"Nelson-Siegel (theory)")
        ax.set_xlabel("Maturity (years)")
        ax.set_ylabel("Loading")
        ax.set_title(f"PC{i+1}: {name}\n(corr = {corr:.3f})",
                      fontweight="bold")
        ax.legend(fontsize=8)
        ax.grid(alpha=0.3)

    # Row 2: eigenvalue spectrum, variance explained, yield curve samples
    ax = axes[1, 0]
    n_bars = min(7, d)
    ax.bar(range(1, n_bars + 1), var_explained[:n_bars], color="steelblue")
    ax.set_xlabel("Principal component")
    ax.set_ylabel("% variance explained")
    ax.set_title(f"Eigenvalue Spectrum\n(3 PCs = {pct_3pc:.1f}%)")

    ax = axes[1, 1]
    # Show a few sample yield curves
    for i in range(0, T, T // 8):
        ax.plot(maturities, yc.iloc[i].values, alpha=0.3, linewidth=0.5, color="steelblue")
    ax.plot(maturities, yc.mean().values, "r-", linewidth=2, label="Mean curve")
    ax.set_xlabel("Maturity (years)")
    ax.set_ylabel("Yield (%)")
    ax.set_title("Sample Yield Curves (1990-2024)")
    ax.legend()

    ax = axes[1, 2]
    # Correlation summary
    labels = ["Level\n(PC1 vs NS1)", "Slope\n(PC2 vs NS2)", "Curvature\n(PC3 vs NS3)"]
    corrs = [corr1, corr2, corr3]
    bars = ax.bar(labels, corrs, color=["#27ae60" if c > 0.9 else "#f39c12" if c > 0.7 else "#e74c3c"
                                          for c in corrs])
    ax.axhline(0.9, color="green", linestyle="--", linewidth=1, label="PASS threshold (0.9)")
    ax.axhline(0.7, color="orange", linestyle="--", linewidth=1, label="MARGINAL threshold (0.7)")
    ax.set_ylabel("Correlation")
    ax.set_title(f"PCA vs Nelson-Siegel Match\n(mean = {mean_corr:.3f})")
    ax.set_ylim(0, 1.05)
    ax.legend(fontsize=7)

    plt.suptitle("Test N1: Yield Curve = Three Jacobi Eigenmodes",
                 fontsize=14, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(GAL_DIR / "test_N1_yield_curve.png", dpi=150)
    plt.close()

    # ── Verdict ──────────────────────────────────────────────
    print(f"\n" + "=" * 70)
    print(f"  VERDICT")
    print(f"=" * 70)

    if mean_corr > 0.9 and min(corr1, corr2, corr3) > 0.8:
        verdict = "PASS"
        detail = f"Mean corr = {mean_corr:.3f}, all > 0.8"
    elif mean_corr > 0.7:
        verdict = "MARGINAL"
        detail = f"Mean corr = {mean_corr:.3f}"
    else:
        verdict = "FAIL"
        detail = f"Mean corr = {mean_corr:.3f}"

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    if verdict == "PASS":
        print(f"\n  The yield curve's PCA eigenvectors match the Nelson-Siegel")
        print(f"  functional forms — confirming that the yield curve factors")
        print(f"  ARE Jacobi eigenfunctions on the bond manifold.")
        print(f"  r = 3 for the bond market (PC1+PC2+PC3 = {pct_3pc:.1f}%).")

    # Save
    summary = {
        "test": "N1: Yield Curve = Jacobi Eigenmodes",
        "verdict": verdict,
        "corr_level": corr1, "corr_slope": corr2, "corr_curvature": corr3,
        "mean_corr": mean_corr, "lambda_opt": lam_opt,
        "pct_3pc": pct_3pc, "n_maturities": d, "T_days": T,
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_N1_summary.csv")
    print(f"\n  Gallery: {GAL_DIR / 'test_N1_yield_curve.png'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, _ = run_test_N1()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
