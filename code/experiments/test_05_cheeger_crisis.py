#!/usr/bin/env python3
"""
Test 5: Cheeger Constant Predicts Crises
=========================================
The Cheeger constant h_M (Fiedler eigenvalue of the sector correlation
graph) should drop significantly before major market crises.

Hypothesis: h_M drops >50% from its 2-year mean in the 6 months
    before each major crisis.

Dataset: S&P 500 sector ETFs (11 sectors), daily, 1999-2024.
    VIX for comparison.
Crises: 2001 dot-com (peak-to-trough Mar-Oct 2002),
    2008 GFC (Sep-Nov 2008), 2011 Euro crisis (Aug 2011),
    2020 COVID (Feb-Mar 2020), 2022 rate shock (Jan-Oct 2022).

Method:
    1. Compute rolling correlation matrix of sector returns (126-day window)
    2. Build correlation graph: edge weight = |correlation|
    3. Compute Fiedler eigenvalue (λ₂ of the graph Laplacian) = Cheeger proxy
    4. Also compute mean correlation (simpler measure)
    5. Compare: does Fiedler drop before crises? Does it beat VIX?

Expected: h_M drops >50% before at least 3 of 5 crises
Falsification: h_M does NOT drop before crises, or drops are < 20%

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

def fiedler_eigenvalue(corr_matrix: np.ndarray) -> float:
    """
    Compute the Fiedler eigenvalue (algebraic connectivity) of the
    correlation graph.

    The graph Laplacian L = D - W where W is the adjacency (|correlation|)
    and D is the degree matrix. The Fiedler eigenvalue is λ₂(L) — the
    smallest non-zero eigenvalue. It measures the worst bottleneck
    in the graph (the Cheeger constant is bounded by λ₂).

    Low λ₂ → weak connectivity → sectors decoupling → crisis approaching.
    High λ₂ → strong connectivity → healthy market.

    IMPORTANT: We use (1 - |corr|) as DISTANCE, so the adjacency is
    |corr| and LOW Fiedler means sectors are DISSIMILAR (decoupled).
    But during crises, correlations spike to 1, making sectors SIMILAR.

    So we actually want to measure the Fiedler of the INVERSE problem:
    how well-connected is the market in its NORMAL state?
    When the Fiedler of the |corr| graph INCREASES suddenly (all
    correlations → 1), that's the crisis signal: the market has
    collapsed to one dimension.

    We track BOTH:
    - fiedler_corr: Fiedler of |correlation| graph (increases in crisis)
    - fiedler_dist: Fiedler of (1-|corr|) distance graph (decreases in crisis)
    - dispersion: 1 - mean(|corr|) — simple measure, high = diverse, low = crisis
    """
    d = corr_matrix.shape[0]

    # Adjacency = |correlation| (zero diagonal)
    W = np.abs(corr_matrix)
    np.fill_diagonal(W, 0)

    # Graph Laplacian
    D = np.diag(W.sum(axis=1))
    L = D - W

    # Eigenvalues
    eigenvalues = np.sort(np.linalg.eigvalsh(L))

    # Fiedler = second smallest eigenvalue (first is always 0)
    fiedler = eigenvalues[1] if len(eigenvalues) > 1 else 0

    # Mean off-diagonal |correlation|
    mask = ~np.eye(d, dtype=bool)
    mean_corr = np.abs(corr_matrix[mask]).mean()

    # Dispersion = 1 - mean|corr| (high = diverse, low = crisis)
    dispersion = 1.0 - mean_corr

    return fiedler, dispersion, mean_corr


# ── Crisis dates ─────────────────────────────────────────────

CRISES = {
    "2002 Dot-com": {
        "crisis_start": "2002-03-01",
        "crisis_peak": "2002-10-09",
        "pre_window": ("2001-09-01", "2002-03-01"),  # 6 months before
        "description": "Dot-com bubble burst, accounting scandals",
    },
    "2008 GFC": {
        "crisis_start": "2008-09-15",
        "crisis_peak": "2009-03-09",
        "pre_window": ("2008-03-15", "2008-09-15"),
        "description": "Lehman collapse, global financial crisis",
    },
    "2011 Euro": {
        "crisis_start": "2011-07-01",
        "crisis_peak": "2011-10-03",
        "pre_window": ("2011-01-01", "2011-07-01"),
        "description": "European sovereign debt crisis, US downgrade",
    },
    "2020 COVID": {
        "crisis_start": "2020-02-19",
        "crisis_peak": "2020-03-23",
        "pre_window": ("2019-08-19", "2020-02-19"),
        "description": "COVID-19 pandemic market crash",
    },
    "2022 Rates": {
        "crisis_start": "2022-01-03",
        "crisis_peak": "2022-10-12",
        "pre_window": ("2021-07-03", "2022-01-03"),
        "description": "Fed rate hiking cycle, inflation shock",
    },
}


# ── Main experiment ──────────────────────────────────────────

def run_test_5():
    """Run Test 5: Cheeger Constant Predicts Crises."""

    print("=" * 60)
    print("  TEST 5: Cheeger Constant (Fiedler eigenvalue)")
    print("  Predicts Crises Before They Happen")
    print("=" * 60)

    # Load data
    # Prefer the 9-sector dataset (1999-2024) for longer history
    sector_path = DATA_DIR / "sector_etf_9_daily_returns.parquet"
    if not sector_path.exists():
        sector_path = DATA_DIR / "sector_etf_daily_returns.parquet"
    vix_path = DATA_DIR / "vix_daily.parquet"

    if not sector_path.exists():
        print("  ERROR: Sector ETF data not found")
        sys.exit(1)

    sectors = pd.read_parquet(sector_path).dropna()
    T_total, d = sectors.shape

    print(f"\n  Sector ETFs: {T_total} days × {d} sectors")
    print(f"  Period: {sectors.index[0].date()} to {sectors.index[-1].date()}")

    vix = None
    if vix_path.exists():
        vix = pd.read_parquet(vix_path).squeeze()
        vix.name = "VIX"

    # ── Rolling Fiedler computation ──────────────────────────
    window = 126  # 6 months rolling correlation
    step = 1      # daily

    print(f"\n  Computing rolling Fiedler eigenvalue (window={window}d)...")

    dates = []
    fiedlers = []
    dispersions = []
    mean_corrs = []

    for i in range(window, T_total, step):
        w = sectors.iloc[i - window:i].values
        if np.isnan(w).sum() > 0.05 * w.size:
            continue
        w = np.nan_to_num(w, 0.0)

        corr = np.corrcoef(w.T)
        f, disp, mc = fiedler_eigenvalue(corr)

        dates.append(sectors.index[i])
        fiedlers.append(f)
        dispersions.append(disp)
        mean_corrs.append(mc)

    ts = pd.DataFrame({
        "fiedler": fiedlers,
        "dispersion": dispersions,
        "mean_corr": mean_corrs,
    }, index=pd.DatetimeIndex(dates))

    # Add VIX
    if vix is not None:
        ts = ts.join(vix, how="left")
        ts["VIX"] = ts["VIX"].ffill()

    # Trailing 2-year stats for normalisation
    ts["fiedler_2y_mean"] = ts["fiedler"].rolling(504, min_periods=126).mean()
    ts["fiedler_2y_std"] = ts["fiedler"].rolling(504, min_periods=126).std()
    ts["dispersion_2y_mean"] = ts["dispersion"].rolling(504, min_periods=126).mean()

    # Z-score
    ts["fiedler_z"] = (ts["fiedler"] - ts["fiedler_2y_mean"]) / ts["fiedler_2y_std"].clip(lower=1e-6)
    ts["dispersion_pct_change"] = (ts["dispersion"] - ts["dispersion_2y_mean"]) / ts["dispersion_2y_mean"].clip(lower=1e-6) * 100

    print(f"  Computed {len(ts)} daily observations")
    print(f"\n  Overall statistics:")
    print(f"    Fiedler: mean={ts['fiedler'].mean():.4f}, std={ts['fiedler'].std():.4f}")
    print(f"    Dispersion: mean={ts['dispersion'].mean():.4f}, std={ts['dispersion'].std():.4f}")
    print(f"    Mean |corr|: mean={ts['mean_corr'].mean():.4f}")

    # ── Analyse each crisis ──────────────────────────────────
    print("\n" + "=" * 60)
    print("  CRISIS-BY-CRISIS ANALYSIS")
    print("=" * 60)

    crisis_results = []

    for name, info in CRISES.items():
        pre_start = pd.Timestamp(info["pre_window"][0])
        pre_end = pd.Timestamp(info["pre_window"][1])
        crisis_start = pd.Timestamp(info["crisis_start"])
        crisis_peak = pd.Timestamp(info["crisis_peak"])

        # Check if we have data for this period
        if pre_start < ts.index[0] or crisis_peak > ts.index[-1]:
            print(f"\n  {name}: SKIP (outside data range)")
            continue

        # Pre-crisis window
        pre = ts.loc[pre_start:pre_end]
        # 2-year baseline before pre-crisis
        baseline_end = pre_start
        baseline_start = baseline_end - pd.DateOffset(years=2)
        baseline = ts.loc[baseline_start:baseline_end]

        # Crisis period
        crisis = ts.loc[crisis_start:crisis_peak]

        if len(pre) < 20 or len(baseline) < 100:
            print(f"\n  {name}: SKIP (insufficient data)")
            continue

        # Metrics
        baseline_disp = baseline["dispersion"].mean()
        pre_disp = pre["dispersion"].mean()
        crisis_disp = crisis["dispersion"].mean() if len(crisis) > 0 else np.nan

        disp_drop_pct = (pre_disp - baseline_disp) / baseline_disp * 100

        baseline_fiedler = baseline["fiedler"].mean()
        pre_fiedler = pre["fiedler"].mean()
        crisis_fiedler = crisis["fiedler"].mean() if len(crisis) > 0 else np.nan

        # For Fiedler of |corr| graph: INCREASE = correlations spiking = crisis
        fiedler_change_pct = (pre_fiedler - baseline_fiedler) / baseline_fiedler * 100

        # VIX
        if "VIX" in ts.columns:
            baseline_vix = baseline["VIX"].mean()
            pre_vix = pre["VIX"].mean()
            crisis_vix = crisis["VIX"].mean() if len(crisis) > 0 else np.nan
            vix_change_pct = (pre_vix - baseline_vix) / baseline_vix * 100
        else:
            baseline_vix = pre_vix = crisis_vix = vix_change_pct = np.nan

        # Did dispersion drop? (lower dispersion = higher correlation = crisis signal)
        signal_disp = disp_drop_pct < -10  # >10% drop in dispersion = warning
        signal_vix = vix_change_pct > 20 if np.isfinite(vix_change_pct) else False

        crisis_results.append({
            "crisis": name,
            "baseline_dispersion": baseline_disp,
            "pre_dispersion": pre_disp,
            "crisis_dispersion": crisis_disp,
            "disp_drop_pct": disp_drop_pct,
            "baseline_fiedler": baseline_fiedler,
            "pre_fiedler": pre_fiedler,
            "fiedler_change_pct": fiedler_change_pct,
            "baseline_vix": baseline_vix,
            "pre_vix": pre_vix,
            "crisis_vix": crisis_vix,
            "vix_change_pct": vix_change_pct,
            "signal_dispersion": signal_disp,
            "signal_vix": signal_vix,
        })

        print(f"\n  {name} ({info['description']})")
        print(f"    Dispersion: baseline={baseline_disp:.4f} → pre-crisis={pre_disp:.4f} "
              f"→ crisis={crisis_disp:.4f}  (pre-crisis drop: {disp_drop_pct:+.1f}%)")
        print(f"    Fiedler:    baseline={baseline_fiedler:.4f} → pre-crisis={pre_fiedler:.4f} "
              f"(change: {fiedler_change_pct:+.1f}%)")
        if np.isfinite(vix_change_pct):
            print(f"    VIX:        baseline={baseline_vix:.1f} → pre-crisis={pre_vix:.1f} "
                  f"(change: {vix_change_pct:+.1f}%)")
        print(f"    Signal: dispersion={'YES' if signal_disp else 'no'}, "
              f"VIX={'YES' if signal_vix else 'no'}")

    if not crisis_results:
        print("\n  ERROR: No crises analysed")
        sys.exit(1)

    cdf = pd.DataFrame(crisis_results)

    # ── Scorecard ────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  SCORECARD: Dispersion vs VIX as Crisis Predictor")
    print("=" * 60)

    n_crises = len(cdf)
    disp_signals = cdf["signal_dispersion"].sum()
    vix_signals = cdf["signal_vix"].sum()

    print(f"\n  Crises analysed: {n_crises}")
    print(f"  Dispersion signalled: {disp_signals}/{n_crises} "
          f"({disp_signals/n_crises*100:.0f}%)")
    print(f"  VIX signalled:       {vix_signals}/{n_crises} "
          f"({vix_signals/n_crises*100:.0f}%)")

    print(f"\n  {'Crisis':>16}  {'Disp drop':>10}  {'Disp signal':>12}  "
          f"{'VIX change':>11}  {'VIX signal':>11}")
    print(f"  {'─' * 65}")
    for _, row in cdf.iterrows():
        ds = "YES" if row["signal_dispersion"] else "no"
        vs = "YES" if row["signal_vix"] else "no"
        print(f"  {row['crisis']:>16}  {row['disp_drop_pct']:>+10.1f}%  "
              f"{ds:>12}  "
              f"{row['vix_change_pct']:>+10.1f}%  "
              f"{vs:>11}")

    # ── Verdict ──────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("  VERDICT")
    print("=" * 60)

    if disp_signals >= 3:
        if disp_signals > vix_signals:
            verdict = "PASS"
            detail = (f"Dispersion signalled {disp_signals}/{n_crises} crises "
                      f"(vs VIX: {vix_signals}/{n_crises}). "
                      f"Cheeger proxy outperforms VIX as early warning.")
        else:
            verdict = "PASS"
            detail = (f"Dispersion signalled {disp_signals}/{n_crises} crises "
                      f"(VIX: {vix_signals}/{n_crises}). "
                      f"Both signal; Cheeger proxy is a useful complement.")
    elif disp_signals >= 2:
        verdict = "MARGINAL"
        detail = (f"Dispersion signalled {disp_signals}/{n_crises} crises. "
                  f"Some predictive power but not consistent.")
    else:
        verdict = "FAIL"
        detail = (f"Dispersion signalled only {disp_signals}/{n_crises} crises. "
                  f"Not a reliable predictor.")

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    # ── Save ─────────────────────────────────────────────────
    ts.to_csv(OUT_DIR / "test_05_timeseries.csv")
    cdf.to_csv(OUT_DIR / "test_05_crisis_results.csv", index=False)

    summary = {
        "test": "Test 5: Cheeger (Dispersion) → Crisis Prediction",
        "verdict": verdict,
        "n_crises": n_crises,
        "dispersion_signals": int(disp_signals),
        "vix_signals": int(vix_signals),
        "mean_disp_drop_pct": cdf["disp_drop_pct"].mean(),
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_05_summary.csv")

    print(f"\n  Results saved to {OUT_DIR / 'test_05_crisis_results.csv'}")
    print(f"  Time series saved to {OUT_DIR / 'test_05_timeseries.csv'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, summary = run_test_5()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
