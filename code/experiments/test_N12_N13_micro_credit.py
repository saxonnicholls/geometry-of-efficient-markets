#!/usr/bin/env python3
"""
Tests N12 and N13
==================
N12: Market impact ∝ LOB curvature κ_LOB
N13: Credit spread ∝ 1/d²_FR (distance from Feller boundary)

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
DATA_DIR = ROOT / "data"
PROC_DIR = DATA_DIR / "processed"
RAW_DIR = DATA_DIR / "raw" / "databento"
OUT_DIR = DATA_DIR / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)


# ═══════════════════════════════════════════════════════════════
# N12: Market Impact ∝ LOB Curvature
# ═══════════════════════════════════════════════════════════════

def test_N12():
    print("\n" + "=" * 60)
    print("  TEST N12: Market Impact ∝ LOB Curvature")
    print("  After a trade, ΔP should correlate with κ_LOB × size")
    print("=" * 60)

    book_path = RAW_DIR / "l2_book_sample.parquet"
    if not book_path.exists():
        print("  SKIP: L2 book data not found")
        return "SKIP", 0

    df = pd.read_parquet(book_path)
    print(f"  L2 data: {df.shape}")

    # Identify bid/ask columns
    bid_sz = [c for c in df.columns if c.startswith("bid_sz")][:10]
    ask_sz = [c for c in df.columns if c.startswith("ask_sz")][:10]
    bid_px = [c for c in df.columns if c.startswith("bid_px")][:10]
    ask_px = [c for c in df.columns if c.startswith("ask_px")][:10]

    n_levels = min(len(bid_sz), len(ask_sz), 5)

    results_by_sym = {}

    for sym in df["symbol"].unique():
        sub = df[df["symbol"] == sym].copy()
        if len(sub) < 1000:
            continue

        # Compute midprice
        sub["mid"] = (sub[bid_px[0]] + sub[ask_px[0]]) / 2

        # Price change (proxy for trade impact — each L2 update often follows a trade)
        sub["dp"] = sub["mid"].diff()
        sub["abs_dp"] = sub["dp"].abs()

        # LOB curvature: how quickly depth falls off from best price
        # κ_LOB ∝ 1 / depth_at_best (thinner book = higher curvature)
        sub["best_bid_sz"] = sub[bid_sz[0]].astype(float)
        sub["best_ask_sz"] = sub[ask_sz[0]].astype(float)
        sub["total_top3_bid"] = sum(sub[bid_sz[i]].astype(float) for i in range(min(3, n_levels)))
        sub["total_top3_ask"] = sum(sub[ask_sz[i]].astype(float) for i in range(min(3, n_levels)))

        # Curvature proxy: inverse of depth at best level
        sub["kappa_bid"] = 1.0 / sub["best_bid_sz"].clip(lower=1)
        sub["kappa_ask"] = 1.0 / sub["best_ask_sz"].clip(lower=1)
        sub["kappa"] = (sub["kappa_bid"] + sub["kappa_ask"]) / 2

        # More sophisticated: depth imbalance
        sub["imbalance"] = (sub["best_bid_sz"] - sub["best_ask_sz"]) / \
                           (sub["best_bid_sz"] + sub["best_ask_sz"]).clip(lower=1)

        # Spread as another LOB measure
        sub["spread"] = (sub[ask_px[0]] - sub[bid_px[0]]).astype(float)

        # Depth profile curvature: how much depth changes between levels
        # A "curved" book has depth concentrated at the best level
        # A "flat" book has equal depth at all levels
        if n_levels >= 3:
            total_depth = sum(sub[bid_sz[i]].astype(float) + sub[ask_sz[i]].astype(float)
                              for i in range(n_levels))
            best_depth = sub[bid_sz[0]].astype(float) + sub[ask_sz[0]].astype(float)
            sub["depth_concentration"] = best_depth / total_depth.clip(lower=1)

        # Sample every 10th row (L2 updates are very frequent)
        sampled = sub.iloc[::10].dropna(subset=["abs_dp", "kappa"]).copy()
        sampled = sampled[sampled["abs_dp"] > 0]  # only when price moved
        sampled = sampled[sampled["abs_dp"] < sampled["abs_dp"].quantile(0.99)]  # remove outliers

        if len(sampled) < 100:
            continue

        # Test: does κ (inverse depth) correlate with |ΔP|?
        corr_kappa = np.corrcoef(sampled["kappa"], sampled["abs_dp"])[0, 1]
        corr_spread = np.corrcoef(sampled["spread"], sampled["abs_dp"])[0, 1]

        # Also: depth concentration vs impact
        if "depth_concentration" in sampled.columns:
            corr_conc = np.corrcoef(sampled["depth_concentration"].fillna(0),
                                     sampled["abs_dp"])[0, 1]
        else:
            corr_conc = 0

        results_by_sym[sym] = {
            "n": len(sampled),
            "corr_kappa_impact": corr_kappa,
            "corr_spread_impact": corr_spread,
            "corr_concentration_impact": corr_conc,
            "mean_kappa": sampled["kappa"].mean(),
            "mean_impact": sampled["abs_dp"].mean(),
        }

        print(f"\n  {sym}: {len(sampled)} samples")
        print(f"    κ vs |ΔP|:     r = {corr_kappa:.4f}")
        print(f"    spread vs |ΔP|: r = {corr_spread:.4f}")
        print(f"    concentration vs |ΔP|: r = {corr_conc:.4f}")

    if not results_by_sym:
        print("  No valid results")
        return "FAIL", 0

    # Average correlation across symbols
    mean_corr = np.mean([r["corr_kappa_impact"] for r in results_by_sym.values()])
    mean_spread_corr = np.mean([r["corr_spread_impact"] for r in results_by_sym.values()])

    print(f"\n  Mean correlation(κ, |ΔP|): {mean_corr:.4f}")
    print(f"  Mean correlation(spread, |ΔP|): {mean_spread_corr:.4f}")

    if mean_corr > 0.3:
        verdict = "PASS"
    elif mean_corr > 0.15:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"  VERDICT: {verdict}")

    pd.Series({"test": "N12: Impact ∝ LOB curvature", "verdict": verdict,
               "mean_corr_kappa": mean_corr, "mean_corr_spread": mean_spread_corr,
               }).to_csv(OUT_DIR / "test_N12_summary.csv")

    return verdict, mean_corr


# ═══════════════════════════════════════════════════════════════
# N13: Credit Spread ∝ 1/d²_FR (distance from Feller boundary)
# ═══════════════════════════════════════════════════════════════

def test_N13():
    print("\n" + "=" * 60)
    print("  TEST N13: Credit Spread ∝ 1/d²_FR")
    print("  (distance from the Feller boundary)")
    print("=" * 60)

    # We don't have direct corporate credit data, but we can test
    # the SOVEREIGN version: sovereign spread should correlate with
    # distance from the "default boundary" in the fiscal simplex.
    #
    # Proxy: use equity volatility as a proxy for distance from default
    # (Merton model: high vol = close to boundary = wide spread)
    # The Fisher-Rao version: d_FR ∝ √(equity_value/total_value)
    # So spread ∝ 1/(equity_value/total_value) ∝ 1/d²_FR

    # Approach: use sector ETFs as different "firms" with different
    # volatilities, and test: does higher vol (closer to boundary)
    # correspond to higher "spread" (lower Sharpe, more risk)?

    # Actually, let's use the FF25 portfolios:
    # Small-cap value portfolios have the highest default risk
    # Large-cap growth portfolios have the lowest
    # The "spread" is the return differential between high and low default risk

    ff25 = pd.read_parquet(PROC_DIR / "ff25_daily_returns.parquet").loc["1963-07-01":]
    returns = ff25.dropna().values
    T, d = returns.shape
    print(f"  FF25: {T} days × {d} portfolios")

    # For each portfolio: compute volatility (proxy for distance from boundary)
    # and average return (proxy for credit spread / risk premium)
    vols = np.std(returns, axis=0) * np.sqrt(252)
    means = np.mean(returns, axis=0) * 252

    # Fisher-Rao distance from boundary: d_FR ∝ 2·arcsin(√b)
    # For equal-weight b = 1/d, all portfolios have same d_FR
    # BUT: we can use the portfolio WEIGHT in the optimal portfolio as the proxy
    # Portfolios with small b* are closer to the boundary

    gross = 1.0 + returns
    from test_N9_N10_N11_high_priority import solve_kelly
    b_star = solve_kelly(gross)
    b_star = np.maximum(b_star, 1e-8)
    b_star /= b_star.sum()

    # Fisher-Rao distance from boundary for each portfolio
    d_fr = 2.0 * np.arcsin(np.sqrt(b_star))

    # The theory: spread (excess return for bearing risk) ∝ 1/d²_FR
    # Portfolios closer to the boundary (small d_FR) should have higher returns
    # (compensation for default risk)
    inv_d2 = 1.0 / (d_fr ** 2)

    # Correlations
    corr_vol_return = np.corrcoef(vols, means)[0, 1]
    corr_dfr_return = np.corrcoef(d_fr, means)[0, 1]
    corr_inv_d2_return = np.corrcoef(inv_d2, means)[0, 1]
    corr_vol_dfr = np.corrcoef(vols, d_fr)[0, 1]

    print(f"\n  Cross-sectional analysis ({d} portfolios):")
    print(f"    Vol vs Return:        r = {corr_vol_return:.4f}")
    print(f"    d_FR vs Return:       r = {corr_dfr_return:.4f}")
    print(f"    1/d²_FR vs Return:    r = {corr_inv_d2_return:.4f}")
    print(f"    Vol vs d_FR:          r = {corr_vol_dfr:.4f}")

    # The key test: does 1/d²_FR predict cross-sectional returns
    # better than volatility alone?
    slope, intercept, r_val, p_val, se = stats.linregress(inv_d2, means)
    print(f"\n  Regression: Return = β₀ + β₁ · (1/d²_FR) + ε")
    print(f"    β₁ = {slope:.4f} ± {se:.4f}")
    print(f"    R² = {r_val**2:.4f}")
    print(f"    p = {p_val:.4e}")

    # Also: the Fama-French known result: small-value earns more
    # Our geometric version: small-value has small b* → small d_FR → large 1/d²_FR → large return
    print(f"\n  Portfolio weight extremes:")
    sorted_idx = np.argsort(b_star)
    print(f"    Smallest b* (closest to boundary):")
    for i in sorted_idx[:3]:
        print(f"      Portfolio {i+1}: b*={b_star[i]:.4f}, d_FR={d_fr[i]:.4f}, "
              f"vol={vols[i]:.1f}%, ret={means[i]:.1f}%")
    print(f"    Largest b* (farthest from boundary):")
    for i in sorted_idx[-3:]:
        print(f"      Portfolio {i+1}: b*={b_star[i]:.4f}, d_FR={d_fr[i]:.4f}, "
              f"vol={vols[i]:.1f}%, ret={means[i]:.1f}%")

    if abs(corr_inv_d2_return) > 0.5 and p_val < 0.05:
        verdict = "PASS"
    elif abs(corr_inv_d2_return) > 0.3:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"\n  VERDICT: {verdict}")

    pd.Series({"test": "N13: Return ∝ 1/d²_FR", "verdict": verdict,
               "corr_inv_d2_return": corr_inv_d2_return,
               "corr_vol_return": corr_vol_return,
               "corr_dfr_return": corr_dfr_return,
               "p_value": p_val,
               }).to_csv(OUT_DIR / "test_N13_summary.csv")

    return verdict, inv_d2, means, d_fr, vols, corr_inv_d2_return


# ═══════════════════════════════════════════════════════════════
# Main + Visualisation
# ═══════════════════════════════════════════════════════════════

def main():
    print("╔" + "═" * 58 + "╗")
    print("║  TESTS N12 (Microstructure) and N13 (Credit)            ║")
    print("╚" + "═" * 58 + "╝")

    v12, corr12 = test_N12()
    v13, inv_d2, means, d_fr, vols, corr13 = test_N13()

    # Visualisation
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # N12
    ax = axes[0]
    ax.text(0.5, 0.5, f"N12: Impact ∝ LOB Curvature\n\n"
            f"κ (inverse depth) vs |ΔP|:\nr = {corr12:.3f}\n\nVerdict: {v12}",
            ha="center", va="center", fontsize=14, transform=ax.transAxes)
    ax.set_title("N12: Market Impact = LOB Curvature")

    # N13
    ax = axes[1]
    if inv_d2 is not None:
        ax.scatter(1.0 / (d_fr ** 2), means * 100, s=40, c=vols, cmap="hot",
                    edgecolors="black", linewidth=0.5)
        z = np.polyfit(inv_d2, means * 100, 1)
        x_fit = np.sort(inv_d2)
        ax.plot(x_fit, np.polyval(z, x_fit), "r--", linewidth=2)
        ax.set_xlabel("1/d²_FR (inverse squared Fisher-Rao distance)")
        ax.set_ylabel("Annual return (%)")
        ax.set_title(f"N13: Return ∝ 1/d²_FR\n(r = {corr13:.3f})\nColor = volatility")
        plt.colorbar(ax.collections[0], ax=ax, label="Vol (%)")

    plt.suptitle("Tests N12 (Microstructure) and N13 (Credit/Risk Premium)",
                 fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig(GAL_DIR / "test_N12_N13.png", dpi=150)
    plt.close()

    print(f"\n{'═' * 60}")
    print(f"  SUMMARY: N12={v12}, N13={v13}")
    print(f"  Gallery: {GAL_DIR / 'test_N12_N13.png'}")
    print(f"{'═' * 60}")


if __name__ == "__main__":
    main()
