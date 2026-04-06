#!/usr/bin/env python3
"""
Test 15R: LZ Complexity of Symbolic Market Sequences
=====================================================
Convert returns to L/S (up/down) symbolic sequences, measure LZ78
compression rate, compare to null (permuted) and Kelly growth rate
across multiple asset classes.

The theory: LZ complexity of the L/S sequence measures predictability.
Departure from maximal entropy = exploitable alpha ≈ Kelly growth rate.

Copyright Saxon Nicholls 2026 MIT Licence
"""

import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats

sys.path.insert(0, str(Path(__file__).parent))
from bootstrap import permutation_test

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)


# ── LZ78 complexity ─────────────────────────────────────────

def lz78_complexity(seq):
    """
    LZ78 phrase count. Returns (n_phrases, dictionary_size).
    """
    dictionary = {"": 0}
    w = ""
    c = 0
    for s in seq:
        ws = w + s
        if ws not in dictionary:
            dictionary[ws] = len(dictionary)
            c += 1
            w = ""
        else:
            w = ws
    if w:
        c += 1
    return c


def lz_compression_rate(seq):
    """
    Normalised LZ78 compression rate.
    Rate = c(T) · log₂(c(T)) / T
    Converges to entropy rate h for ergodic sources.
    """
    T = len(seq)
    if T < 10:
        return np.nan
    c = lz78_complexity(seq)
    if c < 2:
        return 0.0
    return c * np.log2(c) / T


def binary_entropy(p):
    """H(p) = -p log₂(p) - (1-p) log₂(1-p)"""
    if p <= 0 or p >= 1:
        return 0.0
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)


# ── Return → Symbol conversion ──────────────────────────────

def returns_to_symbols(returns, threshold=0.0):
    """
    Convert return series to L/S symbolic sequence.
    L = return > threshold (Long/Up)
    S = return ≤ threshold (Short/Down)
    """
    return "".join(["L" if r > threshold else "S" for r in returns])


def returns_to_ternary(returns, sigma=None):
    """
    Convert to L/N/S (up/neutral/down) with ±0.5σ threshold.
    Captures the distinction between noise and signal.
    """
    if sigma is None:
        sigma = np.std(returns)
    thresh = 0.5 * sigma
    symbols = []
    for r in returns:
        if r > thresh:
            symbols.append("L")
        elif r < -thresh:
            symbols.append("S")
        else:
            symbols.append("N")
    return "".join(symbols)


# ── Analysis per asset ───────────────────────────────────────

def analyse_asset(returns, name, n_null=1000, seed=42):
    """
    Full LZ analysis for one asset's return series.

    Returns dict with:
    - lz_rate: LZ78 compression rate of L/S sequence
    - null_rate: mean LZ78 rate of permuted (null) sequences
    - excess_predictability: lz_rate - null_rate (negative = more predictable than null)
    - kelly_rate: estimated Kelly growth rate
    - p_up: probability of L
    - binary_entropy: H(p_up)
    - autocorr_1: first-order autocorrelation of L/S sequence
    """
    rng = np.random.default_rng(seed)
    returns = returns[~np.isnan(returns)]
    T = len(returns)

    if T < 100:
        return None

    # Binary L/S sequence
    seq = returns_to_symbols(returns)
    p_up = seq.count("L") / T

    # LZ rate of actual sequence
    lz_rate = lz_compression_rate(seq)

    # Null distribution: permute the L/S sequence (destroy temporal structure)
    null_rates = []
    seq_list = list(seq)
    for _ in range(n_null):
        rng.shuffle(seq_list)
        null_rates.append(lz_compression_rate("".join(seq_list)))
    null_mean = np.mean(null_rates)
    null_std = np.std(null_rates)

    # Excess predictability (negative = real sequence more predictable than null)
    excess = lz_rate - null_mean
    z_score = excess / max(null_std, 1e-10)

    # Kelly growth rate
    gross = 1.0 + returns
    # Simple Kelly: log-growth of equal-weight vs cash
    kelly = np.mean(np.log(np.maximum(gross, 1e-15)))

    # Autocorrelation of the binary sequence (1 = L, 0 = S)
    binary = np.array([1 if c == "L" else 0 for c in seq], dtype=float)
    if len(binary) > 10:
        ac1 = np.corrcoef(binary[:-1], binary[1:])[0, 1]
    else:
        ac1 = 0

    # Ternary analysis
    seq3 = returns_to_ternary(returns)
    lz_rate3 = lz_compression_rate(seq3)

    # Ternary null
    seq3_list = list(seq3)
    null3_rates = []
    for _ in range(n_null):
        rng.shuffle(seq3_list)
        null3_rates.append(lz_compression_rate("".join(seq3_list)))
    null3_mean = np.mean(null3_rates)
    excess3 = lz_rate3 - null3_mean

    return {
        "name": name,
        "T": T,
        "p_up": p_up,
        "binary_entropy": binary_entropy(p_up),
        "lz_rate_binary": lz_rate,
        "null_rate_binary": null_mean,
        "excess_binary": excess,
        "z_score_binary": z_score,
        "lz_rate_ternary": lz_rate3,
        "null_rate_ternary": null3_mean,
        "excess_ternary": excess3,
        "kelly_rate": kelly,
        "autocorr_1": ac1,
        "annual_return": np.mean(returns) * 252 if T > 252 else np.mean(returns) * T,
        "annual_vol": np.std(returns) * np.sqrt(252) if T > 252 else np.std(returns) * np.sqrt(T),
    }


# ── Rolling analysis ─────────────────────────────────────────

def rolling_lz_kelly(returns, window=504, step=63):
    """Compute rolling LZ rate and Kelly rate for time series comparison."""
    T = len(returns)
    results = []
    for i in range(0, T - window, step):
        w = returns[i:i + window]
        seq = returns_to_symbols(w)
        lz = lz_compression_rate(seq)
        kelly = np.mean(np.log(np.maximum(1.0 + w, 1e-15)))

        # Null for this window
        rng = np.random.default_rng(42 + i)
        seq_list = list(seq)
        null_rates = [lz_compression_rate("".join(rng.permutation(list(seq_list))))
                      for _ in range(200)]
        excess = lz - np.mean(null_rates)

        results.append({
            "window_end": i + window,
            "lz_rate": lz,
            "null_rate": np.mean(null_rates),
            "excess": excess,
            "kelly_rate": kelly,
        })
    return pd.DataFrame(results)


# ── Main experiment ──────────────────────────────────────────

def run_test_15R():
    print("=" * 70)
    print("  TEST 15R: LZ Complexity of L/S Symbolic Sequences")
    print("  Across Multiple Asset Classes")
    print("=" * 70)

    # ── Load all available asset classes ──────────────────────
    assets = {}

    # Equities (FF25 → market portfolio)
    ff5_path = DATA_DIR / "ff5_factors_daily.parquet"
    if ff5_path.exists():
        ff5 = pd.read_parquet(ff5_path)
        assets["US Equity (Mkt-RF)"] = ff5["Mkt-RF"].dropna().values
        assets["US Small-Big (SMB)"] = ff5["SMB"].dropna().values
        assets["US Value (HML)"] = ff5["HML"].dropna().values

    # Sector ETFs
    sec_path = DATA_DIR / "sector_etf_9_daily_returns.parquet"
    if sec_path.exists():
        sec = pd.read_parquet(sec_path)
        for col in ["XLK", "XLF", "XLE"]:
            if col in sec.columns:
                assets[f"Sector {col}"] = sec[col].dropna().values

    # Futures
    fut_path = DATA_DIR / "futures_daily_returns.parquet"
    if fut_path.exists():
        fut = pd.read_parquet(fut_path)
        for col in fut.columns:
            short = col.replace(".c.0", "")
            assets[f"Futures {short}"] = fut[col].dropna().values

    # Crypto
    cr_path = DATA_DIR / "crypto_daily_returns.parquet"
    if cr_path.exists():
        cr = pd.read_parquet(cr_path)
        for col in cr.columns:
            short = col.replace("-USD", "")
            assets[f"Crypto {short}"] = cr[col].dropna().values

    # Treasury yields → daily changes as "returns"
    yc_path = DATA_DIR / "treasury_yield_curve.parquet"
    if yc_path.exists():
        yc = pd.read_parquet(yc_path)
        if "y_10" in yc.columns:
            changes = yc["y_10"].diff().dropna().values
            assets["US 10Y Yield Δ"] = changes

    print(f"\n  Loaded {len(assets)} asset series")

    # ── Analyse each asset ───────────────────────────────────
    results = []
    for name, ret in assets.items():
        r = analyse_asset(ret, name)
        if r:
            results.append(r)

    df = pd.DataFrame(results)

    # ── Print results table ──────────────────────────────────
    print(f"\n  {'Asset':>25}  {'T':>6}  {'P(L)':>5}  {'H(p)':>5}  "
          f"{'LZ rate':>7}  {'Null':>6}  {'Excess':>7}  {'Z':>5}  "
          f"{'Kelly':>8}  {'AC(1)':>6}")
    print(f"  {'─' * 100}")

    for _, r in df.sort_values("excess_binary").iterrows():
        print(f"  {r['name']:>25}  {r['T']:>6.0f}  {r['p_up']:>.3f}  {r['binary_entropy']:>.3f}  "
              f"{r['lz_rate_binary']:>7.4f}  {r['null_rate_binary']:>6.4f}  "
              f"{r['excess_binary']:>+7.4f}  {r['z_score_binary']:>+5.1f}  "
              f"{r['kelly_rate']:>8.6f}  {r['autocorr_1']:>+6.3f}")

    # ── Key test: does excess predictability correlate with Kelly? ─
    print(f"\n" + "=" * 70)
    print(f"  CORRELATION: Excess Predictability vs Kelly Rate")
    print(f"=" * 70)

    x = -df["excess_binary"].values  # negative excess = more predictable = more alpha
    y = df["kelly_rate"].values

    mask = np.isfinite(x) & np.isfinite(y)
    x_clean, y_clean = x[mask], y[mask]

    corr_binary = np.corrcoef(x_clean, y_clean)[0, 1] if len(x_clean) > 3 else 0
    print(f"\n  Binary (L/S):")
    print(f"    Correlation(-excess, kelly): {corr_binary:.4f}")

    # Ternary
    x3 = -df["excess_ternary"].values
    corr_ternary = np.corrcoef(x3[mask], y_clean)[0, 1] if len(x_clean) > 3 else 0
    print(f"  Ternary (L/N/S):")
    print(f"    Correlation(-excess, kelly): {corr_ternary:.4f}")

    # Also: does LZ rate correlate with autocorrelation?
    ac = df["autocorr_1"].values
    corr_ac_lz = np.corrcoef(df["excess_binary"].values[mask],
                              ac[mask])[0, 1] if len(ac[mask]) > 3 else 0
    print(f"\n  Excess predictability vs autocorrelation: {corr_ac_lz:.4f}")

    # ── Rolling analysis on US equity ────────────────────────
    print(f"\n" + "─" * 70)
    print(f"  Rolling LZ-Kelly analysis (US Equity, 2-year windows)")
    print(f"─" * 70)

    if "US Equity (Mkt-RF)" in assets:
        mkt = assets["US Equity (Mkt-RF)"]
        rolling = rolling_lz_kelly(mkt, window=504, step=63)

        if len(rolling) > 10:
            rc = np.corrcoef(-rolling["excess"].values, rolling["kelly_rate"].values)[0, 1]
            print(f"  {len(rolling)} windows")
            print(f"  Rolling correlation(-excess, kelly): {rc:.4f}")
        else:
            rc = 0
            print(f"  Insufficient rolling windows")
    else:
        rc = 0

    # ── Asset class comparison ───────────────────────────────
    print(f"\n" + "─" * 70)
    print(f"  ASSET CLASS COMPARISON")
    print(f"─" * 70)

    # Group by asset class
    for prefix in ["US ", "Sector", "Futures", "Crypto", "US 10Y"]:
        subset = df[df["name"].str.startswith(prefix)]
        if len(subset) > 0:
            mean_excess = subset["excess_binary"].mean()
            mean_kelly = subset["kelly_rate"].mean()
            mean_ac = subset["autocorr_1"].mean()
            print(f"  {prefix:>10}: excess={mean_excess:+.4f}, "
                  f"kelly={mean_kelly:.6f}, AC(1)={mean_ac:+.4f} "
                  f"({'more predictable' if mean_excess < -0.001 else 'near random'})")

    # ── Visualisation ────────────────────────────────────────
    fig = plt.figure(figsize=(16, 10))
    gs = gridspec.GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.3)

    # 1. Excess predictability by asset (bar chart)
    ax1 = fig.add_subplot(gs[0, 0])
    sorted_df = df.sort_values("excess_binary")
    colors = ["red" if e < -0.002 else "steelblue" if e < 0.002 else "green"
              for e in sorted_df["excess_binary"]]
    ax1.barh(range(len(sorted_df)), sorted_df["excess_binary"], color=colors)
    ax1.set_yticks(range(len(sorted_df)))
    ax1.set_yticklabels([n[:15] for n in sorted_df["name"]], fontsize=6)
    ax1.axvline(0, color="black", linewidth=0.5)
    ax1.set_xlabel("Excess LZ (negative = predictable)")
    ax1.set_title("Predictability by Asset")

    # 2. LZ rate vs null rate (scatter)
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.scatter(df["null_rate_binary"], df["lz_rate_binary"],
                c="steelblue", s=50, alpha=0.7)
    lim = [df[["null_rate_binary", "lz_rate_binary"]].min().min() - 0.01,
           df[["null_rate_binary", "lz_rate_binary"]].max().max() + 0.01]
    ax2.plot(lim, lim, "r--", linewidth=1, label="LZ = Null (random)")
    ax2.set_xlabel("Null LZ rate (permuted)")
    ax2.set_ylabel("Actual LZ rate")
    ax2.set_title("Actual vs Null Compression Rate")
    ax2.legend(fontsize=8)
    for _, r in df.iterrows():
        if abs(r["excess_binary"]) > 0.003:
            ax2.annotate(r["name"][:10], (r["null_rate_binary"], r["lz_rate_binary"]),
                         fontsize=5)

    # 3. Excess predictability vs Kelly rate (scatter)
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.scatter(-df["excess_binary"], df["kelly_rate"] * 252,
                c="steelblue", s=50, alpha=0.7)
    ax3.set_xlabel("-Excess LZ (more predictable →)")
    ax3.set_ylabel("Kelly rate (annualised)")
    ax3.set_title(f"Predictability vs Kelly (r={corr_binary:.3f})")
    if len(x_clean) > 2:
        z = np.polyfit(-df["excess_binary"].values[mask], y_clean * 252, 1)
        ax3.plot(np.sort(-df["excess_binary"].values),
                 np.polyval(z, np.sort(-df["excess_binary"].values)), "r--")

    # 4. Binary entropy vs LZ rate
    ax4 = fig.add_subplot(gs[1, 0])
    ax4.scatter(df["binary_entropy"], df["lz_rate_binary"],
                c="steelblue", s=50, alpha=0.7)
    ax4.set_xlabel("Binary entropy H(p)")
    ax4.set_ylabel("LZ compression rate")
    ax4.set_title("Entropy vs Compression Rate")
    ax4.plot([0.9, 1.0], [0.9, 1.0], "r--", linewidth=1)

    # 5. Autocorrelation vs excess
    ax5 = fig.add_subplot(gs[1, 1])
    ax5.scatter(df["autocorr_1"], df["excess_binary"],
                c="steelblue", s=50, alpha=0.7)
    ax5.set_xlabel("Autocorrelation AC(1)")
    ax5.set_ylabel("Excess LZ (neg = predictable)")
    ax5.set_title(f"Autocorrelation vs Predictability (r={corr_ac_lz:.3f})")
    ax5.axhline(0, color="black", linewidth=0.5)
    ax5.axvline(0, color="black", linewidth=0.5)

    # 6. Rolling LZ excess vs Kelly for US equity
    ax6 = fig.add_subplot(gs[1, 2])
    if "US Equity (Mkt-RF)" in assets and len(rolling) > 5:
        ax6.scatter(-rolling["excess"], rolling["kelly_rate"] * 252,
                    c="steelblue", s=20, alpha=0.5)
        ax6.set_xlabel("-Excess LZ")
        ax6.set_ylabel("Kelly rate (ann)")
        ax6.set_title(f"Rolling US Equity (r={rc:.3f})")
        if len(rolling) > 3:
            z = np.polyfit(-rolling["excess"].values, rolling["kelly_rate"].values * 252, 1)
            xs = np.sort(-rolling["excess"].values)
            ax6.plot(xs, np.polyval(z, xs), "r--")
    else:
        ax6.text(0.5, 0.5, "Insufficient data", ha="center", va="center")
        ax6.set_title("Rolling US Equity")

    plt.suptitle("Test 15R: LZ Symbolic Complexity Across Asset Classes",
                 fontsize=14, fontweight="bold")
    plt.savefig(GAL_DIR / "test_15R_lz_symbolic.png", dpi=150, bbox_inches="tight")
    plt.close()

    # ── Verdict ──────────────────────────────────────────────
    print(f"\n" + "=" * 70)
    print(f"  VERDICT")
    print(f"=" * 70)

    best_corr = max(abs(corr_binary), abs(corr_ternary), abs(rc))

    # Most assets should have LZ rate BELOW null (more predictable than random)
    n_predictable = (df["excess_binary"] < -0.001).sum()
    pct_predictable = n_predictable / len(df) * 100

    print(f"\n  Assets more predictable than null: {n_predictable}/{len(df)} ({pct_predictable:.0f}%)")
    print(f"  Best correlation (excess vs kelly): {best_corr:.3f}")

    if pct_predictable > 60 and best_corr > 0.3:
        verdict = "PASS"
        detail = f"{pct_predictable:.0f}% predictable, best corr = {best_corr:.3f}"
    elif pct_predictable > 40 or best_corr > 0.2:
        verdict = "MARGINAL"
        detail = f"{pct_predictable:.0f}% predictable, best corr = {best_corr:.3f}"
    else:
        verdict = "FAIL"
        detail = f"{pct_predictable:.0f}% predictable, best corr = {best_corr:.3f}"

    print(f"\n  Result: {verdict}")
    print(f"  {detail}")

    # Save
    df.to_csv(OUT_DIR / "test_15R_results.csv", index=False)
    summary = {
        "test": "Test 15R: LZ Symbolic (L/S) Across Asset Classes",
        "verdict": verdict,
        "n_assets": len(df),
        "pct_predictable": pct_predictable,
        "corr_binary": corr_binary,
        "corr_ternary": corr_ternary,
        "corr_rolling": rc,
        "best_corr": best_corr,
    }
    pd.Series(summary).to_csv(OUT_DIR / "test_15R_summary.csv")
    print(f"\n  Results: {OUT_DIR / 'test_15R_results.csv'}")
    print(f"  Gallery: {GAL_DIR / 'test_15R_lz_symbolic.png'}")

    return verdict, summary


if __name__ == "__main__":
    verdict, _ = run_test_15R()
    sys.exit(0 if verdict in ("PASS", "MARGINAL") else 1)
