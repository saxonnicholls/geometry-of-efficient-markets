#!/usr/bin/env python3
"""
Medium Priority Tests N14, N15, N16, N17
==========================================
N14: Geometric pairs entry z* > 2σ rule (backtest)
N15: O(1/T²) Laplace accuracy
N16: Negative curvature → mandatory alpha (crypto)
N17: Multi-timescale r consistency

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)


def project_simplex(v):
    d = len(v)
    u = np.sort(v)[::-1]
    cs = np.cumsum(u)
    rho = np.max(np.where(u - (cs - 1) / (np.arange(d) + 1) > 0))
    return np.maximum(v - (cs[rho] - 1) / (rho + 1), 0)


def solve_kelly(gross, max_iter=200):
    T, d = gross.shape
    b = np.ones(d) / d
    for it in range(max_iter):
        bx = np.maximum(gross @ b, 1e-12)
        grad = (gross / bx[:, None]).mean(axis=0)
        b = project_simplex(b + grad / (it + 10))
    return b


# ═══════════════════════════════════════════════════════════════
# N14: Geometric Pairs Entry z* vs 2σ Rule
# ═══════════════════════════════════════════════════════════════

def test_N14():
    print("\n" + "=" * 60)
    print("  TEST N14: Geometric Pairs Entry z* vs 2σ Rule")
    print("  z* = √(1 + r/κ) should outperform the standard 2σ entry")
    print("=" * 60)

    eq_path = DATA_DIR / "equities_50_daily_returns.parquet"
    if not eq_path.exists():
        # Fall back to sector ETFs for pairs
        eq_path = DATA_DIR / "sector_etf_9_daily_returns.parquet"
    if not eq_path.exists():
        print("  SKIP: no equity data")
        return "SKIP"

    eq = pd.read_parquet(eq_path).dropna()
    T, d = eq.shape
    print(f"  Data: {T} days × {d} assets")

    # Find the most cointegrated pairs (highest correlation)
    corr_matrix = eq.corr()
    pairs = []
    for i in range(d):
        for j in range(i + 1, d):
            pairs.append((eq.columns[i], eq.columns[j], abs(corr_matrix.iloc[i, j])))
    pairs.sort(key=lambda x: x[2], reverse=True)
    top_pairs = pairs[:10]
    print(f"  Top {len(top_pairs)} correlated pairs")

    # Backtest both entry rules on each pair
    results = []
    for a_name, b_name, corr in top_pairs:
        a = eq[a_name].values
        b = eq[b_name].values

        # Spread = log(A/B)
        spread = np.log((1 + a).cumprod()) - np.log((1 + b).cumprod())
        spread_mean = pd.Series(spread).rolling(63, min_periods=20).mean().values
        spread_std = pd.Series(spread).rolling(63, min_periods=20).std().values
        z_score = (spread - spread_mean) / np.maximum(spread_std, 1e-10)

        # Estimate κ (OU mean-reversion) and r (manifold dimension ≈ 1 for pairs)
        dx = np.diff(spread)
        x = spread[:-1]
        mask = ~(np.isnan(dx) | np.isnan(x))
        if mask.sum() < 50:
            continue
        dx_c, x_c = dx[mask], x[mask]
        X = np.column_stack([np.ones(len(x_c)), x_c])
        try:
            beta = np.linalg.lstsq(X, dx_c, rcond=None)[0]
        except:
            continue
        kappa = -beta[1]
        if kappa <= 0:
            continue

        r_dim = 1  # pairs = 1-dimensional manifold
        z_star = np.sqrt(1 + r_dim / kappa) if kappa > 0 else 2.0

        # Backtest: entry when |z| > threshold, exit when |z| < 0.5
        for label, threshold in [("2σ", 2.0), ("z*", z_star)]:
            position = 0
            pnl = []
            for t in range(63, T - 1):
                if np.isnan(z_score[t]):
                    pnl.append(0)
                    continue
                # Entry
                if position == 0:
                    if z_score[t] > threshold:
                        position = -1  # short the spread
                    elif z_score[t] < -threshold:
                        position = 1  # long the spread
                # Exit
                elif position != 0 and abs(z_score[t]) < 0.5:
                    position = 0

                # P&L
                if position != 0:
                    spread_return = (a[t + 1] - b[t + 1])
                    pnl.append(position * spread_return)
                else:
                    pnl.append(0)

            pnl = np.array(pnl)
            if len(pnl) > 100 and np.std(pnl) > 1e-10:
                sharpe = np.mean(pnl) / np.std(pnl) * np.sqrt(252)
            else:
                sharpe = 0

            results.append({
                "pair": f"{a_name[:4]}/{b_name[:4]}",
                "corr": corr,
                "kappa": kappa,
                "z_star": z_star,
                "rule": label,
                "sharpe": sharpe,
                "n_trades": np.sum(np.diff(np.sign(pnl)) != 0),
            })

    rdf = pd.DataFrame(results)

    # Compare
    if len(rdf) > 0:
        zs_sharpes = rdf[rdf["rule"] == "z*"]["sharpe"].values
        two_sig = rdf[rdf["rule"] == "2σ"]["sharpe"].values
        n_pairs = min(len(zs_sharpes), len(two_sig))
        wins = np.sum(zs_sharpes[:n_pairs] > two_sig[:n_pairs])
        pct_wins = wins / max(n_pairs, 1) * 100

        print(f"\n  z* wins {wins}/{n_pairs} pairs ({pct_wins:.0f}%)")
        print(f"  Mean Sharpe (z*): {zs_sharpes.mean():.3f}")
        print(f"  Mean Sharpe (2σ): {two_sig.mean():.3f}")

        if pct_wins > 60:
            verdict = "PASS"
        elif pct_wins > 45:
            verdict = "MARGINAL"
        else:
            verdict = "FAIL"
    else:
        verdict = "SKIP"
        pct_wins = 0

    print(f"  VERDICT: {verdict}")
    pd.Series({"test": "N14: z* vs 2σ", "verdict": verdict,
               "pct_wins": pct_wins}).to_csv(OUT_DIR / "test_N14_summary.csv")
    return verdict


# ═══════════════════════════════════════════════════════════════
# N15: O(1/T²) Laplace Accuracy
# ═══════════════════════════════════════════════════════════════

def test_N15():
    print("\n" + "=" * 60)
    print("  TEST N15: O(1/T²) Laplace Accuracy")
    print("  Laplace posterior mean error should scale as 1/T²")
    print("=" * 60)

    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet").loc["1990-01-01":]
    returns = ff25.dropna().values
    T_total, d = returns.shape
    print(f"  Data: {T_total} days × {d} portfolios")

    # For increasing T: compute Laplace b* and MC b*, measure the difference
    # The difference should scale as O(1/T²)
    T_values = [126, 252, 504, 1008, 2016, 4032]
    errors = []
    n_mc = 5000

    for T in T_values:
        if T > T_total:
            break

        w = returns[:T]
        gross = 1.0 + w

        # Laplace: b* = Kelly optimal (this IS the Laplace posterior mean
        # for uniform prior, to O(1/T²))
        b_laplace = solve_kelly(gross)
        b_laplace = np.maximum(b_laplace, 1e-8)
        b_laplace /= b_laplace.sum()

        # MC: sample from Dirichlet, wealth-weight, average
        rng = np.random.default_rng(42)
        samples = rng.dirichlet(np.ones(d), n_mc)
        log_W = np.array([np.sum(np.log(np.maximum(gross @ s, 1e-15))) for s in samples])
        log_W -= log_W.max()
        weights = np.exp(log_W)
        weights /= weights.sum()
        b_mc = (samples * weights[:, None]).sum(axis=0)
        b_mc /= b_mc.sum()

        # Error = ||b_laplace - b_mc||
        error = np.linalg.norm(b_laplace - b_mc)
        errors.append({"T": T, "error": error, "log_T": np.log(T), "log_error": np.log(max(error, 1e-15))})

        print(f"  T={T:>5}: error = {error:.6f}")

    edf = pd.DataFrame(errors)

    # Fit: log(error) = a + b·log(T)
    # Theory predicts b ≈ -2 (O(1/T²))
    if len(edf) >= 3:
        slope, intercept, r_val, p_val, se = stats.linregress(edf["log_T"], edf["log_error"])
        print(f"\n  log(error) = {intercept:.2f} + {slope:.2f}·log(T)")
        print(f"  Slope: {slope:.2f} ± {se:.2f} (theory: -2.0)")
        print(f"  R² = {r_val**2:.3f}")

        # Is the slope near -2?
        if abs(slope - (-2)) < 1:
            verdict = "PASS"
        elif abs(slope - (-2)) < 1.5:
            verdict = "MARGINAL"
        else:
            verdict = "FAIL"
    else:
        slope = 0
        verdict = "SKIP"

    print(f"  VERDICT: {verdict}")
    pd.Series({"test": "N15: Laplace O(1/T²)", "verdict": verdict,
               "slope": slope}).to_csv(OUT_DIR / "test_N15_summary.csv")
    return verdict, edf


# ═══════════════════════════════════════════════════════════════
# N16: Negative Curvature → Mandatory Alpha
# ═══════════════════════════════════════════════════════════════

def test_N16():
    print("\n" + "=" * 60)
    print("  TEST N16: Negative Curvature → Mandatory Alpha")
    print("  Markets with high curvature variation should always have ||H||>0")
    print("=" * 60)

    # Use crypto (expected: pseudo-Anosov / high curvature) vs
    # large-cap equities (expected: CAPM / low curvature)
    datasets = {}

    cr_path = DATA_DIR / "crypto_daily_returns.parquet"
    if cr_path.exists():
        cr = pd.read_parquet(cr_path).dropna()
        if len(cr) > 252:
            datasets["Crypto"] = cr.values

    ff25_path = DATA_DIR / "ff25_daily_returns.parquet"
    if ff25_path.exists():
        ff = pd.read_parquet(ff25_path).loc["2000-01-01":].dropna().values
        datasets["FF25 Equities"] = ff

    sec_path = DATA_DIR / "sector_etf_9_daily_returns.parquet"
    if sec_path.exists():
        sec = pd.read_parquet(sec_path).dropna().values
        datasets["Sector ETFs"] = sec

    results = []
    for name, returns in datasets.items():
        T, d = returns.shape
        if T < 252 or d < 3:
            continue

        # Rolling H estimation
        window = 252
        step = 63
        H_values = []

        for i in range(0, T - window, step):
            w = returns[i:i + window]
            w = np.nan_to_num(w, 0.0)
            gross = 1.0 + w
            b = solve_kelly(gross)
            b = np.maximum(b, 1e-8); b /= b.sum()

            cov = np.cov(w.T)
            evals, evecs = np.linalg.eigh(cov)
            idx = np.argsort(evals)[::-1]
            r = min(3, d - 1)
            V_r = evecs[:, idx[:r]]
            Pi_N = np.eye(d) - V_r @ V_r.T

            half_inv = 1.0 / (2.0 * np.sqrt(b))
            H_vec = Pi_N @ half_inv
            H_values.append(np.linalg.norm(H_vec))

        H_arr = np.array(H_values)
        pct_positive = np.mean(H_arr > 0.1) * 100
        mean_H = H_arr.mean()
        min_H = H_arr.min()

        results.append({
            "market": name,
            "mean_H": mean_H,
            "min_H": min_H,
            "pct_H_positive": pct_positive,
            "n_windows": len(H_arr),
        })

        print(f"  {name}: mean ||H|| = {mean_H:.4f}, "
              f"min ||H|| = {min_H:.4f}, "
              f"||H|| > 0.1 in {pct_positive:.0f}% of windows")

    rdf = pd.DataFrame(results)

    # The theory: crypto should have higher ||H|| (more inefficient)
    # than equities (more efficient)
    if len(rdf) >= 2:
        # Is crypto's min H > equities' min H?
        crypto_h = rdf[rdf["market"] == "Crypto"]["mean_H"].values
        equity_h = rdf[rdf["market"].str.contains("FF25|Sector")]["mean_H"].values

        if len(crypto_h) > 0 and len(equity_h) > 0:
            crypto_more = crypto_h[0] > equity_h.mean()
            print(f"\n  Crypto mean ||H||: {crypto_h[0]:.4f}")
            print(f"  Equity mean ||H||: {equity_h.mean():.4f}")
            print(f"  Crypto more inefficient: {'YES' if crypto_more else 'NO'}")

            # Does ||H|| > 0 always? (mandatory alpha)
            all_positive = all(r["pct_H_positive"] > 95 for _, r in rdf.iterrows())

            if crypto_more and all_positive:
                verdict = "PASS"
            elif crypto_more or all_positive:
                verdict = "MARGINAL"
            else:
                verdict = "FAIL"
        else:
            verdict = "MARGINAL"
    else:
        verdict = "SKIP"

    print(f"  VERDICT: {verdict}")
    pd.Series({"test": "N16: Neg curvature → mandatory alpha", "verdict": verdict,
               }).to_csv(OUT_DIR / "test_N16_summary.csv")
    return verdict


# ═══════════════════════════════════════════════════════════════
# N17: Multi-Timescale r Consistency
# ═══════════════════════════════════════════════════════════════

def test_N17():
    print("\n" + "=" * 60)
    print("  TEST N17: Multi-Timescale r Consistency")
    print("  Is the manifold dimension r the same at daily, weekly, monthly?")
    print("=" * 60)

    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet").loc["1990-01-01":].dropna()

    freqs = {
        "Daily": ff25,
        "Weekly": ff25.resample("W").sum().dropna(),
        "Monthly": ff25.resample("ME").sum().dropna(),
    }

    results = []
    for freq_name, data in freqs.items():
        returns = data.values
        T, d = returns.shape

        # Estimate r via variance ratio (90%)
        cov = np.cov(returns.T)
        evals = np.sort(np.linalg.eigvalsh(cov))[::-1]
        cumvar = np.cumsum(evals) / evals.sum()
        r_90 = int(np.searchsorted(cumvar, 0.90)) + 1

        # Also: Marchenko-Pastur edge
        gamma = T / d
        sigma2 = np.median(evals)
        lambda_plus = sigma2 * (1 + 1 / np.sqrt(gamma)) ** 2
        r_mp = int(np.sum(evals > lambda_plus))

        results.append({
            "frequency": freq_name,
            "T": T,
            "r_var90": r_90,
            "r_mp": r_mp,
            "var_explained_3": cumvar[2] * 100 if len(cumvar) > 2 else 0,
        })

        print(f"  {freq_name}: T={T}, r(90%)={r_90}, r(MP)={r_mp}, "
              f"3PC={cumvar[2]*100:.1f}%")

    rdf = pd.DataFrame(results)

    # Is r consistent across timescales?
    r_values = rdf["r_var90"].values
    r_range = r_values.max() - r_values.min()
    r_cv = np.std(r_values) / np.mean(r_values)

    print(f"\n  r(90%) across timescales: {r_values}")
    print(f"  Range: {r_range}")
    print(f"  CV: {r_cv:.3f}")

    if r_range <= 2:
        verdict = "PASS"
    elif r_range <= 4:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"  VERDICT: {verdict}")
    pd.Series({"test": "N17: Multi-timescale r", "verdict": verdict,
               "r_range": int(r_range), "r_cv": r_cv,
               }).to_csv(OUT_DIR / "test_N17_summary.csv")
    return verdict


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def main():
    print("╔" + "═" * 58 + "╗")
    print("║  MEDIUM PRIORITY: N14, N15, N16, N17                    ║")
    print("╚" + "═" * 58 + "╝")

    v14 = test_N14()
    v15, edf15 = test_N15()
    v16 = test_N16()
    v17 = test_N17()

    # Visualisation
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # N14: pairs
    ax = axes[0, 0]
    ax.text(0.5, 0.5, f"N14: Geometric Pairs Entry\nz* vs 2σ rule\n\nVerdict: {v14}",
            ha="center", va="center", fontsize=14, transform=ax.transAxes)
    ax.set_title("N14: Pairs Trading")

    # N15: Laplace convergence
    ax = axes[0, 1]
    if edf15 is not None and len(edf15) > 2:
        ax.scatter(edf15["log_T"], edf15["log_error"], s=60, c="steelblue", zorder=5)
        z = np.polyfit(edf15["log_T"], edf15["log_error"], 1)
        x_fit = np.linspace(edf15["log_T"].min(), edf15["log_T"].max(), 50)
        ax.plot(x_fit, np.polyval(z, x_fit), "r--", linewidth=2,
                label=f"Fit: slope = {z[0]:.2f} (theory: -2)")
        ax.set_xlabel("log(T)")
        ax.set_ylabel("log(error)")
        ax.set_title(f"N15: Laplace Convergence Rate\nslope = {z[0]:.2f} (theory: -2)\n{v15}")
        ax.legend()

    # N16: mandatory alpha
    ax = axes[1, 0]
    ax.text(0.5, 0.5, f"N16: Mandatory Alpha\n(Neg curvature → ||H|| > 0)\n\nVerdict: {v16}",
            ha="center", va="center", fontsize=14, transform=ax.transAxes)
    ax.set_title("N16: Mandatory Alpha")

    # N17: multi-timescale
    ax = axes[1, 1]
    ax.text(0.5, 0.5, f"N17: Multi-Timescale r\n(daily/weekly/monthly should agree)\n\nVerdict: {v17}",
            ha="center", va="center", fontsize=14, transform=ax.transAxes)
    ax.set_title("N17: Dimension Consistency")

    plt.suptitle("Medium Priority Tests: N14-N17", fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig(GAL_DIR / "test_N14_N15_N16_N17.png", dpi=150)
    plt.close()

    print(f"\n{'═' * 60}")
    print(f"  SUMMARY: N14={v14}, N15={v15}, N16={v16}, N17={v17}")
    print(f"  Gallery: {GAL_DIR / 'test_N14_N15_N16_N17.png'}")
    print(f"{'═' * 60}")


if __name__ == "__main__":
    main()
