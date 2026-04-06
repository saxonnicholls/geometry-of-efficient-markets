#!/usr/bin/env python3
"""
Test 3: MUP vs Cover Regret
============================
MUP regret ≈ r·log(T)/(2T), Cover regret ≈ (d-1)·log(T)/(2T).
Ratio should be ≈ (d-1)/r.

Hypothesis: MUP outperforms Cover by approximately (d-1)/r in regret.

Dataset: FF25 portfolios (d=25), daily, 1963-2024. Run MUP with r=4
    and full Cover (r=d-1=24).
Method: Monte Carlo integration for both. Compare cumulative log-wealth.

Expected: MUP outperforms Cover by factor ≈ 24/4 = 6× in regret reduction
Falsification: MUP does NOT outperform Cover, or ratio < 2× or > 15×

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
OUT_DIR.mkdir(exist_ok=True)


# ── Core functions ───────────────────────────────────────────

def project_simplex(v):
    """Project v onto the probability simplex."""
    d = len(v)
    u = np.sort(v)[::-1]
    cumsum = np.cumsum(u)
    rho = np.max(np.where(u - (cumsum - 1) / (np.arange(d) + 1) > 0))
    theta = (cumsum[rho] - 1) / (rho + 1)
    return np.maximum(v - theta, 0)


def solve_kelly(gross_returns: np.ndarray, max_iter=300, tol=1e-8):
    """Find the log-optimal portfolio b*."""
    T, d = gross_returns.shape
    b = np.ones(d) / d

    for it in range(max_iter):
        bx = gross_returns @ b
        bx = np.maximum(bx, 1e-12)
        grad = (gross_returns / bx[:, None]).mean(axis=0)
        lr = 1.0 / (it + 10)
        b = project_simplex(b + lr * grad)
        if np.linalg.norm(grad - grad.mean()) < tol:
            break

    return b


def log_wealth(b: np.ndarray, gross_returns: np.ndarray) -> float:
    """Compute log-wealth of portfolio b over the return series."""
    bx = gross_returns @ b
    bx = np.maximum(bx, 1e-15)
    return np.sum(np.log(bx))


def cover_universal_portfolio(gross_returns: np.ndarray, n_samples=5000,
                               seed=42):
    """
    Cover's universal portfolio: integrate over the FULL simplex Δ_{d-1}.
    Uses Monte Carlo with Dirichlet(1,...,1) samples.
    Returns the wealth-weighted posterior mean portfolio.
    """
    T, d = gross_returns.shape
    rng = np.random.default_rng(seed)

    # Sample portfolios uniformly from the simplex
    samples = rng.dirichlet(np.ones(d), n_samples)  # (N, d)

    # Compute log-wealth for each sample
    log_wealths = np.zeros(n_samples)
    for i in range(n_samples):
        log_wealths[i] = log_wealth(samples[i], gross_returns)

    # Numerical stability
    log_wealths -= log_wealths.max()
    weights = np.exp(log_wealths)
    weights /= weights.sum()

    # Posterior mean
    b_cover = (samples * weights[:, None]).sum(axis=0)
    b_cover /= b_cover.sum()

    # Log normalisation constant (Cover's wealth)
    log_Z = np.log(np.mean(np.exp(log_wealths))) + log_wealths.max()

    return b_cover, log_Z


def mup_portfolio(gross_returns: np.ndarray, n_factors=4, n_samples=5000,
                   seed=42):
    """
    Manifold Universal Portfolio: integrate over the r-dimensional
    factor subspace only (not the full simplex).

    1. Find b* and the factor subspace via PCA
    2. Sample portfolios from the factor manifold
    3. Wealth-weight and average
    """
    T, d = gross_returns.shape
    rng = np.random.default_rng(seed)

    # Step 1: PCA to find factor subspace
    returns = gross_returns - 1.0  # excess returns
    cov = np.cov(returns.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]

    r = min(n_factors, d - 1)
    V_r = eigenvectors[:, :r]  # d × r factor loadings

    # Step 2: Sample factor weights from Dirichlet(1,...,1) on r-simplex
    alpha_samples = rng.dirichlet(np.ones(r), n_samples)  # (N, r)

    # Project onto portfolio simplex via factor loadings
    # b = |α · V_r^T| (take absolute value, then normalise)
    b_samples = np.abs(alpha_samples @ V_r.T)  # (N, d)
    row_sums = b_samples.sum(axis=1, keepdims=True)
    row_sums = np.maximum(row_sums, 1e-15)
    b_samples = b_samples / row_sums

    # Step 3: Compute log-wealth for each sample
    log_wealths = np.zeros(n_samples)
    for i in range(n_samples):
        log_wealths[i] = log_wealth(b_samples[i], gross_returns)

    # Numerical stability
    log_wealths -= log_wealths.max()
    weights = np.exp(log_wealths)
    weights /= weights.sum()

    # Posterior mean
    b_mup = (b_samples * weights[:, None]).sum(axis=0)
    b_mup /= b_mup.sum()

    # Log normalisation constant (MUP's wealth)
    log_Z = np.log(np.mean(np.exp(log_wealths))) + log_wealths.max()

    return b_mup, log_Z


# ── Main experiment ──────────────────────────────────────────

def run_test_3():
    """Run Test 3: MUP vs Cover Regret."""

    print("=" * 60)
    print("  TEST 3: MUP vs Cover Regret")
    print("  MUP regret ≈ r·log(T)/(2T) vs Cover ≈ (d-1)·log(T)/(2T)")
    print("=" * 60)

    # Load data
    ff25_path = DATA_DIR / "ff25_daily_returns.parquet"
    if not ff25_path.exists():
        print(f"\nERROR: Data not found at {ff25_path}")
        sys.exit(1)

    ff25 = pd.read_parquet(ff25_path)
    ff25 = ff25.loc["1963-07-01":]

    # Use gross returns (price relatives)
    gross = (1.0 + ff25).values
    T_total, d = gross.shape

    print(f"\nData: {T_total} days × {d} portfolios")
    print(f"Period: {ff25.index[0].date()} to {ff25.index[-1].date()}")

    # Run on multiple subperiods to get a distribution of regret ratios
    n_factors = 4
    n_samples = 10000
    window_sizes = [252, 504, 1260, 2520]  # 1yr, 2yr, 5yr, 10yr
    n_trials = 10  # random starting points per window size

    print(f"\nr = {n_factors}, d = {d}, theoretical ratio = (d-1)/r = {(d-1)/n_factors:.1f}")
    print(f"MC samples: {n_samples}")
    print(f"\nRunning {len(window_sizes)} window sizes × {n_trials} trials...")

    results = []
    rng = np.random.default_rng(42)

    for T in window_sizes:
        if T > T_total:
            continue

        for trial in range(n_trials):
            # Random start point
            start = rng.integers(0, T_total - T)
            window = gross[start:start + T]

            # Kelly optimal (the benchmark)
            b_star = solve_kelly(window)
            lw_star = log_wealth(b_star, window)

            # Cover's universal portfolio (full simplex integration)
            _, lw_cover = cover_universal_portfolio(
                window, n_samples=n_samples, seed=42 + trial
            )

            # MUP (factor subspace integration)
            _, lw_mup = mup_portfolio(
                window, n_factors=n_factors, n_samples=n_samples,
                seed=42 + trial
            )

            # Regret = log-wealth of optimal - log-wealth of strategy
            regret_cover = lw_star - lw_cover
            regret_mup = lw_star - lw_mup

            # Theoretical regret
            theo_cover = (d - 1) * np.log(T) / (2 * T)
            theo_mup = n_factors * np.log(T) / (2 * T)

            # Ratio
            if regret_mup > 1e-10:
                ratio = regret_cover / regret_mup
            else:
                ratio = float('inf')

            results.append({
                "T": T,
                "trial": trial,
                "lw_star": lw_star,
                "lw_cover": lw_cover,
                "lw_mup": lw_mup,
                "regret_cover": regret_cover,
                "regret_mup": regret_mup,
                "ratio_empirical": ratio,
                "theo_cover": theo_cover,
                "theo_mup": theo_mup,
                "theo_ratio": (d - 1) / n_factors,
            })

        # Print progress
        trial_results = [r for r in results if r["T"] == T]
        mean_ratio = np.mean([r["ratio_empirical"] for r in trial_results
                             if np.isfinite(r["ratio_empirical"])])
        mean_reg_c = np.mean([r["regret_cover"] for r in trial_results])
        mean_reg_m = np.mean([r["regret_mup"] for r in trial_results])
        print(f"\n  T = {T:5d} ({T/252:.0f} yr):  "
              f"Regret_Cover = {mean_reg_c:.4f}  "
              f"Regret_MUP = {mean_reg_m:.4f}  "
              f"Ratio = {mean_ratio:.2f}  "
              f"(theory: {(d-1)/n_factors:.1f})")

    df = pd.DataFrame(results)

    # ── Overall analysis ─────────────────────────────────────
    print("\n" + "=" * 60)
    print("  RESULTS BY WINDOW SIZE")
    print("=" * 60)

    print(f"\n  {'T':>6}  {'Years':>5}  {'Regret_Cover':>13}  {'Regret_MUP':>11}  "
          f"{'Ratio':>7}  {'Theory':>7}  {'MUP wins?':>10}")
    print(f"  {'─' * 70}")

    for T in window_sizes:
        sub = df[df["T"] == T]
        if len(sub) == 0:
            continue
        rc = sub["regret_cover"].mean()
        rm = sub["regret_mup"].mean()
        finite_ratios = sub["ratio_empirical"][np.isfinite(sub["ratio_empirical"])]
        ratio = finite_ratios.mean() if len(finite_ratios) > 0 else float('nan')
        mup_wins = (sub["regret_mup"] < sub["regret_cover"]).mean() * 100

        print(f"  {T:>6}  {T/252:>5.0f}  {rc:>13.4f}  {rm:>11.4f}  "
              f"{ratio:>7.2f}  {(d-1)/n_factors:>7.1f}  "
              f"{mup_wins:>9.0f}%")

    # ── Verdict ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  VERDICT")
    print("=" * 60)

    # MUP should outperform Cover in majority of trials
    mup_wins_overall = (df["regret_mup"] < df["regret_cover"]).mean()

    finite_ratios = df["ratio_empirical"][np.isfinite(df["ratio_empirical"])]
    mean_ratio = finite_ratios.mean() if len(finite_ratios) > 0 else 0
    theoretical_ratio = (d - 1) / n_factors

    if mup_wins_overall > 0.6 and 2 < mean_ratio < 15:
        verdict = "PASS"
        detail = (f"MUP outperforms Cover in {mup_wins_overall*100:.0f}% of trials. "
                  f"Mean ratio = {mean_ratio:.2f} "
                  f"(theory: {theoretical_ratio:.1f}, within [2, 15] range)")
    elif mup_wins_overall > 0.5:
        verdict = "MARGINAL"
        detail = (f"MUP outperforms Cover in {mup_wins_overall*100:.0f}% of trials "
                  f"(barely above 50%). Ratio = {mean_ratio:.2f}")
    else:
        verdict = "FAIL"
        detail = (f"MUP outperforms Cover in only {mup_wins_overall*100:.0f}% of trials. "
                  f"Ratio = {mean_ratio:.2f}")

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    if verdict == "PASS":
        print(f"\n  The MUP's dimension reduction (d-1={d-1} → r={n_factors}) is confirmed.")
        print(f"  Integrating over the {n_factors}-dim factor manifold beats")
        print(f"  integrating over the full {d-1}-dim simplex.")
    elif verdict == "FAIL":
        print(f"\n  *** MUP does NOT reliably outperform Cover. ***")
        print(f"  *** The dimension reduction may not work in practice. ***")

    # ── Save ─────────────────────────────────────────────────
    df.to_csv(OUT_DIR / "test_03_results.csv", index=False)

    summary = {
        "test": "Test 3: MUP vs Cover Regret",
        "verdict": verdict,
        "mup_wins_pct": mup_wins_overall * 100,
        "mean_ratio": mean_ratio,
        "theoretical_ratio": theoretical_ratio,
        "n_factors": n_factors,
        "d": d,
        "n_samples": n_samples,
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_03_summary.csv")

    print(f"\n  Results saved to {OUT_DIR / 'test_03_results.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_3()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
