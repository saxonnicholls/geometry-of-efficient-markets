#!/usr/bin/env python3
"""
High Priority Tests N9, N10, N11
=================================
N9:  Curvature spike → subsequent return (PREDICTIVE test)
N10: FX Carry Sharpe = ||H_carry|| (Sharpe-curvature on FX)
N11: Yield curve inversion = winding number (recession predictor)

These three test the most important untested claims.

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
    cumsum = np.cumsum(u)
    rho = np.max(np.where(u - (cumsum - 1) / (np.arange(d) + 1) > 0))
    theta = (cumsum[rho] - 1) / (rho + 1)
    return np.maximum(v - theta, 0)


def solve_kelly(gross, max_iter=200):
    T, d = gross.shape
    b = np.ones(d) / d
    for it in range(max_iter):
        bx = np.maximum(gross @ b, 1e-12)
        grad = (gross / bx[:, None]).mean(axis=0)
        b = project_simplex(b + grad / (it + 10))
    return b


# ═══════════════════════════════════════════════════════════════
# N9: Curvature spike → subsequent return
# ═══════════════════════════════════════════════════════════════

def test_N9():
    print("\n" + "=" * 60)
    print("  TEST N9: Does curvature PREDICT future returns?")
    print("  (This is the CAUSAL test — not just contemporaneous)")
    print("=" * 60)

    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet").loc["1963-07-01":]
    ff5 = pd.read_parquet(DATA_DIR / "ff5_factors_daily.parquet")
    common = ff25.index.intersection(ff5.index)
    ff25 = ff25.loc[common]
    rf = ff5.loc[common, "RF"]
    excess = ff25.subtract(rf, axis=0)

    window = 252; step = 21; n_factors = 4; forward = 63  # predict 3 months ahead

    Hs = []; future_sharpes = []; dates = []

    for i in range(0, len(excess) - window - forward, step):
        w = excess.iloc[i:i + window].values
        if np.isnan(w).sum() > 0.05 * w.size: continue
        w = np.nan_to_num(w, 0.0)

        gross = 1.0 + w
        b_star = solve_kelly(gross)
        b_star = np.maximum(b_star, 1e-8); b_star /= b_star.sum()

        cov = np.cov(w.T)
        evals, evecs = np.linalg.eigh(cov)
        idx = np.argsort(evals)[::-1]
        V_r = evecs[:, idx[:n_factors]]
        Pi_N = np.eye(w.shape[1]) - V_r @ V_r.T

        half_inv = 1.0 / (2.0 * np.sqrt(b_star))
        H_vec = Pi_N @ half_inv
        H_norm = np.linalg.norm(H_vec)

        # FUTURE returns in the H direction (the prediction)
        future_w = excess.iloc[i + window:i + window + forward].values
        if len(future_w) < forward * 0.8: continue
        future_w = np.nan_to_num(future_w, 0.0)

        if H_norm > 1e-10:
            direction = H_vec / H_norm
            future_ret = future_w @ direction
            future_sharpe = abs(np.mean(future_ret)) / max(np.std(future_ret, ddof=1), 1e-12) * np.sqrt(252)
        else:
            future_sharpe = 0.0

        Hs.append(H_norm)
        future_sharpes.append(future_sharpe)
        dates.append(excess.index[i + window])

    H_arr = np.array(Hs); fs_arr = np.array(future_sharpes)

    # Remove outliers
    mask = (np.abs(H_arr - H_arr.mean()) < 3 * H_arr.std()) & \
           (np.abs(fs_arr - fs_arr.mean()) < 3 * fs_arr.std())
    H_c, fs_c = H_arr[mask], fs_arr[mask]

    slope, intercept, r_val, p_val, se = stats.linregress(H_c, fs_c)
    corr = r_val

    print(f"\n  {len(H_c)} windows (predict {forward}d ahead)")
    print(f"  Slope: {slope:.4f} ± {se:.4f}")
    print(f"  Correlation: {corr:.4f}")
    print(f"  p-value: {p_val:.4e}")

    if corr > 0 and p_val < 0.05:
        verdict = "PASS"
    elif corr > 0 and p_val < 0.10:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"  VERDICT: {verdict}")

    pd.Series({"test": "N9: H predicts future Sharpe", "verdict": verdict,
               "correlation": corr, "p_value": p_val, "slope": slope,
               "n_windows": len(H_c), "forward_days": forward,
               }).to_csv(OUT_DIR / "test_N9_summary.csv")

    return verdict, H_c, fs_c, corr, p_val


# ═══════════════════════════════════════════════════════════════
# N10: FX Carry Sharpe = ||H_carry||
# ═══════════════════════════════════════════════════════════════

def test_N10():
    print("\n" + "=" * 60)
    print("  TEST N10: FX Carry Sharpe = ||H_carry||")
    print("  Sharpe-curvature identity on the currency simplex")
    print("=" * 60)

    fx_path = DATA_DIR / "fx_spot_daily_returns.parquet"
    if not fx_path.exists():
        print("  SKIP: spot FX daily data not found")
        return "SKIP", None, None, 0, 1

    fx = pd.read_parquet(fx_path).dropna()
    # Keep only USD pairs (not crosses) for a clean simplex
    usd_pairs = [c for c in fx.columns if "USD" in c and not any(
        x in c for x in ["EUR-GBP", "EUR-CHF", "EUR-JPY", "GBP-JPY", "GBP-CHF", "AUD-NZD", "AUD-JPY"])]
    fx = fx[usd_pairs].dropna()
    T, d = fx.shape
    print(f"  Spot FX: {T} days × {d} USD pairs")
    print(f"  Pairs: {fx.columns.tolist()}")

    # Rolling Sharpe-curvature test (same as Test 1R but on FX)
    window = 252; step = 63; n_factors = 3
    Hs = []; Sharpes = []

    for i in range(0, T - window, step):
        w = fx.iloc[i:i + window].values
        w = np.nan_to_num(w, 0.0)

        gross = 1.0 + w
        b_star = solve_kelly(gross)
        b_star = np.maximum(b_star, 1e-8); b_star /= b_star.sum()

        cov = np.cov(w.T)
        evals, evecs = np.linalg.eigh(cov)
        idx = np.argsort(evals)[::-1]
        V_r = evecs[:, idx[:n_factors]]
        Pi_N = np.eye(d) - V_r @ V_r.T

        half_inv = 1.0 / (2.0 * np.sqrt(b_star))
        H_vec = Pi_N @ half_inv
        H_norm = np.linalg.norm(H_vec)

        if H_norm > 1e-10:
            direction = H_vec / H_norm
            strat_ret = w @ direction
            sharpe = abs(np.mean(strat_ret)) / max(np.std(strat_ret, ddof=1), 1e-12) * np.sqrt(252)
        else:
            sharpe = 0.0

        Hs.append(H_norm); Sharpes.append(sharpe)

    H_arr = np.array(Hs); S_arr = np.array(Sharpes)
    mask = (H_arr > 0) & (S_arr < S_arr.mean() + 3 * S_arr.std())
    H_c, S_c = H_arr[mask], S_arr[mask]

    if len(H_c) < 10:
        print("  Insufficient data")
        return "SKIP", None, None, 0, 1

    corr = np.corrcoef(H_c, S_c)[0, 1]
    slope, intercept, r_val, p_val, se = stats.linregress(H_c, S_c)

    print(f"  {len(H_c)} windows")
    print(f"  FX Sharpe-curvature correlation: {corr:.4f}")
    print(f"  Slope: {slope:.4f} ± {se:.4f}")
    print(f"  p-value: {p_val:.4e}")

    if corr > 0 and p_val < 0.05:
        verdict = "PASS"
    elif corr > 0 and p_val < 0.10:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"  VERDICT: {verdict}")

    pd.Series({"test": "N10: FX Sharpe = curvature", "verdict": verdict,
               "correlation": corr, "p_value": p_val,
               }).to_csv(OUT_DIR / "test_N10_summary.csv")

    return verdict, H_c, S_c, corr, p_val


# ═══════════════════════════════════════════════════════════════
# N11: Yield curve inversion = recession predictor
# ═══════════════════════════════════════════════════════════════

def test_N11():
    print("\n" + "=" * 60)
    print("  TEST N11: Yield Curve Inversion = Recession Predictor")
    print("  Does the 10Y-2Y spread going negative predict recessions?")
    print("=" * 60)

    yc_path = DATA_DIR / "treasury_yield_curve.parquet"
    if not yc_path.exists():
        print("  SKIP: yield curve data not found")
        return "SKIP", None

    yc = pd.read_parquet(yc_path)

    # The 10Y-2Y spread (the classic inversion indicator)
    if "y_10" in yc.columns and "y_2" in yc.columns:
        spread = (yc["y_10"] - yc["y_2"]).dropna()
    elif "y_10.0" in yc.columns and "y_2.0" in yc.columns:
        spread = (yc["y_10.0"] - yc["y_2.0"]).dropna()
    else:
        print(f"  Columns: {yc.columns.tolist()}")
        print("  SKIP: cannot compute 10Y-2Y spread")
        return "SKIP", None

    print(f"  Spread data: {len(spread)} days")
    print(f"  Period: {spread.index[0]} to {spread.index[-1]}")

    # NBER recession dates (approximate start dates)
    recessions = [
        ("2001-03-01", "2001 Dot-com"),
        ("2007-12-01", "2008 GFC"),
        ("2020-02-01", "2020 COVID"),
    ]

    # For each recession: was the curve inverted in the 6-18 months before?
    results = []
    for rec_date, rec_name in recessions:
        rec = pd.Timestamp(rec_date)
        if rec < spread.index[0] or rec > spread.index[-1]:
            continue

        # Look back 6-18 months before the recession
        lookback_start = rec - pd.DateOffset(months=18)
        lookback_end = rec - pd.DateOffset(months=3)

        window = spread.loc[lookback_start:lookback_end]
        if len(window) < 30:
            continue

        # Was the spread negative at any point?
        min_spread = window.min()
        days_inverted = (window < 0).sum()
        pct_inverted = days_inverted / len(window) * 100

        # Also compute the "winding number" proxy:
        # number of zero-crossings in the spread
        crossings = np.sum(np.diff(np.sign(window.values)) != 0)

        predicted = min_spread < 0

        results.append({
            "recession": rec_name,
            "date": rec_date,
            "min_spread": min_spread,
            "days_inverted": days_inverted,
            "pct_inverted": pct_inverted,
            "zero_crossings": crossings,
            "predicted": predicted,
        })

        print(f"  {rec_name}: min spread = {min_spread:.2f}%, "
              f"inverted {pct_inverted:.0f}% of lookback, "
              f"{'PREDICTED' if predicted else 'not predicted'}")

    rdf = pd.DataFrame(results)
    n_predicted = rdf["predicted"].sum()
    n_total = len(rdf)
    pct_predicted = n_predicted / max(n_total, 1) * 100

    # Also: how many FALSE inversions (inversion without subsequent recession)?
    # Check all inversions in the data
    inverted = spread < 0
    inversion_starts = inverted & ~inverted.shift(1, fill_value=False)
    n_inversions = inversion_starts.sum()

    print(f"\n  Total inversions in data: {n_inversions}")
    print(f"  Recessions predicted: {n_predicted}/{n_total}")

    if n_total > 0 and pct_predicted >= 66:
        verdict = "PASS"
    elif n_total > 0 and pct_predicted >= 50:
        verdict = "MARGINAL"
    else:
        verdict = "FAIL"

    print(f"  VERDICT: {verdict}")

    pd.Series({"test": "N11: Inversion → recession", "verdict": verdict,
               "n_predicted": int(n_predicted), "n_recessions": n_total,
               "pct_predicted": pct_predicted, "n_inversions": int(n_inversions),
               }).to_csv(OUT_DIR / "test_N11_summary.csv")

    return verdict, spread, rdf


# ═══════════════════════════════════════════════════════════════
# Main + Visualisation
# ═══════════════════════════════════════════════════════════════

def main():
    print("╔" + "═" * 58 + "╗")
    print("║  HIGH PRIORITY TESTS: N9, N10, N11                      ║")
    print("╚" + "═" * 58 + "╝")

    v9, H9, fs9, c9, p9 = test_N9()
    v10, H10, S10, c10, p10 = test_N10()
    v11, spread11, rdf11 = test_N11()

    # ── Combined visualisation ───────────────────────────────
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # N9: Curvature predicts future Sharpe
    ax = axes[0]
    if H9 is not None and len(H9) > 10:
        ax.scatter(H9, fs9, s=5, alpha=0.3, c="steelblue")
        z = np.polyfit(H9, fs9, 1)
        ax.plot(np.sort(H9), np.polyval(z, np.sort(H9)), "r-", linewidth=2)
        ax.set_xlabel("||H|| (estimated today)")
        ax.set_ylabel("Future Sharpe (next 63 days)")
        ax.set_title(f"N9: Curvature → Future Return\n(r={c9:.3f}, p={p9:.2e})\n{v9}")
    else:
        ax.text(0.5, 0.5, "Insufficient data", ha="center", va="center")

    # N10: FX Sharpe = curvature
    ax = axes[1]
    if H10 is not None and len(H10) > 5:
        ax.scatter(H10, S10, s=20, alpha=0.5, c="steelblue")
        z = np.polyfit(H10, S10, 1)
        ax.plot(np.sort(H10), np.polyval(z, np.sort(H10)), "r-", linewidth=2)
        ax.set_xlabel("||H|| (FX manifold)")
        ax.set_ylabel("Realised Sharpe")
        ax.set_title(f"N10: FX Sharpe = Curvature\n(r={c10:.3f}, p={p10:.2e})\n{v10}")
    else:
        ax.text(0.5, 0.5, "Insufficient data", ha="center", va="center")

    # N11: Yield curve inversion
    ax = axes[2]
    if spread11 is not None:
        ax.plot(spread11.index, spread11.values, linewidth=0.5, color="steelblue")
        ax.axhline(0, color="red", linewidth=1, linestyle="--")
        ax.fill_between(spread11.index, spread11.values, 0,
                          where=spread11.values < 0, alpha=0.3, color="red",
                          label="Inverted (recession signal)")
        # Mark recessions
        if rdf11 is not None:
            for _, r in rdf11.iterrows():
                ax.axvline(pd.Timestamp(r["date"]), color="darkred", linewidth=1,
                            linestyle=":", alpha=0.7)
        ax.set_xlabel("Date")
        ax.set_ylabel("10Y - 2Y spread (%)")
        ax.set_title(f"N11: Yield Curve Inversion\n{v11}")
        ax.legend(fontsize=8)
    else:
        ax.text(0.5, 0.5, "No data", ha="center", va="center")

    plt.suptitle("High Priority Tests: N9 (Predictive), N10 (FX), N11 (Recession)",
                 fontsize=13, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig(GAL_DIR / "test_N9_N10_N11.png", dpi=150)
    plt.close()

    print(f"\n{'═' * 60}")
    print(f"  SUMMARY: N9={v9}, N10={v10}, N11={v11}")
    print(f"  Gallery: {GAL_DIR / 'test_N9_N10_N11.png'}")
    print(f"{'═' * 60}")


if __name__ == "__main__":
    main()
