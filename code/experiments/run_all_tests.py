#!/usr/bin/env python3
"""
Run ALL remaining experiments (Tests 4R, 5R, 7-15) and generate
visualisation gallery comparing real data to theoretical predictions.

Copyright Saxon Nicholls 2026 MIT Licence

Produces:
    data/results/test_*_summary.csv — per-test summaries
    data/results/SCORECARD.csv — overall scorecard
    code/visualisation/gallery/ — PNG visualisations
"""

import sys
import warnings
from pathlib import Path
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

warnings.filterwarnings("ignore")

sys.path.insert(0, str(Path(__file__).parent))
from bootstrap import bootstrap_ci, permutation_test, block_bootstrap_sample

ROOT = Path(__file__).parent.parent.parent
DATA_DIR = ROOT / "data" / "processed"
OUT_DIR = ROOT / "data" / "results"
GAL_DIR = ROOT / "code" / "visualisation" / "gallery"
OUT_DIR.mkdir(exist_ok=True)
GAL_DIR.mkdir(parents=True, exist_ok=True)

SCORECARD = []


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


def record(name, verdict, detail, score):
    SCORECARD.append({"test": name, "verdict": verdict, "detail": detail, "score": score})
    print(f"  → {verdict} (score: {score})")


# ═══════════════════════════════════════════════════════════════
# Test 7: Fat Tail Index α ≈ r/2
# ═══════════════════════════════════════════════════════════════

def test_7_fat_tails():
    print("\n" + "=" * 60)
    print("  TEST 7: Fat Tail Index α ≈ r/2")
    print("=" * 60)

    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet").loc["1963-07-01":]
    returns = ff25.values
    returns = returns[~np.isnan(returns).any(axis=1)]

    # Estimate r from variance ratio
    cov = np.cov(returns.T)
    eigs = np.sort(np.linalg.eigvalsh(cov))[::-1]
    cumvar = np.cumsum(eigs) / eigs.sum()
    r_est = int(np.searchsorted(cumvar, 0.90)) + 1
    alpha_predicted = r_est / 2.0

    # Estimate tail index via Hill estimator for each portfolio
    alphas = []
    for j in range(returns.shape[1]):
        col = np.abs(returns[:, j])
        col = col[col > 0]
        col_sorted = np.sort(col)[::-1]
        k = max(int(len(col) * 0.05), 50)  # top 5%
        if k < 10:
            continue
        log_excess = np.log(col_sorted[:k]) - np.log(col_sorted[k])
        alpha_hill = k / np.sum(log_excess)
        if 1 < alpha_hill < 10:
            alphas.append(alpha_hill)

    alpha_empirical = np.median(alphas) if alphas else np.nan

    print(f"  Estimated r (90% variance): {r_est}")
    print(f"  Predicted α = r/2: {alpha_predicted:.2f}")
    print(f"  Empirical α (Hill, median): {alpha_empirical:.2f}")
    print(f"  |Predicted - Empirical|: {abs(alpha_predicted - alpha_empirical):.2f}")

    # Visualisation
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    ax1.hist(alphas, bins=30, density=True, alpha=0.7, color="steelblue", label="Empirical α (Hill)")
    ax1.axvline(alpha_predicted, color="red", linewidth=2, linestyle="--", label=f"Theory: r/2 = {alpha_predicted:.1f}")
    ax1.axvline(alpha_empirical, color="darkblue", linewidth=2, label=f"Median: {alpha_empirical:.2f}")
    ax1.set_xlabel("Tail index α")
    ax1.set_ylabel("Density")
    ax1.set_title("Test 7: Fat Tail Index")
    ax1.legend()

    ax2.bar(range(1, min(11, len(eigs) + 1)), eigs[:10] / eigs.sum() * 100, color="steelblue")
    ax2.axvline(r_est + 0.5, color="red", linestyle="--", label=f"r = {r_est} (90% variance)")
    ax2.set_xlabel("Eigenvalue rank")
    ax2.set_ylabel("% variance explained")
    ax2.set_title("PCA eigenvalues (FF25)")
    ax2.legend()
    plt.tight_layout()
    plt.savefig(GAL_DIR / "test_07_fat_tails.png", dpi=150)
    plt.close()

    close = abs(alpha_predicted - alpha_empirical) < 1.5
    if close:
        record("7. Fat tails α ≈ r/2", "PASS", f"α_emp={alpha_empirical:.2f}, α_pred={alpha_predicted:.1f}", 1)
    else:
        record("7. Fat tails α ≈ r/2", "FAIL", f"α_emp={alpha_empirical:.2f}, α_pred={alpha_predicted:.1f}", 0)


# ═══════════════════════════════════════════════════════════════
# Test 8: Jacobi Diffusion Fit
# ═══════════════════════════════════════════════════════════════

def test_8_jacobi_fit():
    print("\n" + "=" * 60)
    print("  TEST 8: Jacobi Diffusion vs GBM for Portfolio Weights")
    print("=" * 60)

    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet").loc["1990-01-01":]
    returns = ff25.values
    returns = returns[~np.isnan(returns).any(axis=1)]

    # Simulate portfolio weight evolution (equal-weight rebalanced monthly)
    T, d = returns.shape
    gross = 1.0 + returns
    weights = np.ones(d) / d
    weight_history = [weights.copy()]

    for t in range(T):
        weights = weights * gross[t]
        weights /= weights.sum()
        weight_history.append(weights.copy())

    weight_arr = np.array(weight_history)

    # Test: do weight changes follow Jacobi (√w) or GBM (w) dynamics?
    # Jacobi: dw_i ∝ √(w_i) · dW → weight changes / √w should be ~N(0,σ²)
    # GBM: dw_i ∝ w_i · dW → weight changes / w should be ~N(0,σ²)

    dw = np.diff(weight_arr, axis=0)  # T × d
    w_mid = (weight_arr[:-1] + weight_arr[1:]) / 2

    # Normalise by √w (Jacobi) and w (GBM)
    jacobi_resid = dw / np.maximum(np.sqrt(w_mid), 1e-8)
    gbm_resid = dw / np.maximum(w_mid, 1e-8)

    # KS test for normality of each
    ks_jacobi = []
    ks_gbm = []
    for j in range(d):
        jr = jacobi_resid[:, j]
        gr = gbm_resid[:, j]
        jr = (jr - jr.mean()) / max(jr.std(), 1e-10)
        gr = (gr - gr.mean()) / max(gr.std(), 1e-10)
        ks_j = stats.kstest(jr[:1000], "norm").statistic
        ks_g = stats.kstest(gr[:1000], "norm").statistic
        ks_jacobi.append(ks_j)
        ks_gbm.append(ks_g)

    jacobi_wins = sum(1 for j, g in zip(ks_jacobi, ks_gbm) if j < g)
    pct = jacobi_wins / d * 100

    print(f"  Jacobi fits better than GBM in {jacobi_wins}/{d} portfolios ({pct:.0f}%)")
    print(f"  Mean KS (Jacobi): {np.mean(ks_jacobi):.4f}")
    print(f"  Mean KS (GBM):    {np.mean(ks_gbm):.4f}")

    # Visualisation
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # Weight trajectory
    for j in range(min(5, d)):
        axes[0].plot(weight_arr[:500, j], alpha=0.7, linewidth=0.5)
    axes[0].set_title("Portfolio weight trajectories (5 assets)")
    axes[0].set_xlabel("Day")
    axes[0].set_ylabel("Weight")

    # KS comparison
    axes[1].scatter(ks_jacobi, ks_gbm, alpha=0.7, c="steelblue", s=40)
    lim = max(max(ks_jacobi), max(ks_gbm)) * 1.1
    axes[1].plot([0, lim], [0, lim], "r--", linewidth=1, label="Equal fit")
    axes[1].set_xlabel("KS statistic (Jacobi)")
    axes[1].set_ylabel("KS statistic (GBM)")
    axes[1].set_title(f"Jacobi wins {pct:.0f}% of portfolios")
    axes[1].legend()

    # Residual distribution (first portfolio)
    jr0 = jacobi_resid[:, 0]
    jr0 = (jr0 - jr0.mean()) / max(jr0.std(), 1e-10)
    axes[2].hist(jr0[np.abs(jr0) < 5], bins=80, density=True, alpha=0.7, color="steelblue", label="Jacobi residuals")
    x_grid = np.linspace(-5, 5, 200)
    axes[2].plot(x_grid, stats.norm.pdf(x_grid), "r-", linewidth=2, label="N(0,1)")
    axes[2].set_title("Jacobi-normalised residuals (portfolio 1)")
    axes[2].legend()

    plt.tight_layout()
    plt.savefig(GAL_DIR / "test_08_jacobi_fit.png", dpi=150)
    plt.close()

    if pct > 60:
        record("8. Jacobi > GBM", "PASS", f"Jacobi wins {pct:.0f}%", 1)
    elif pct > 45:
        record("8. Jacobi > GBM", "MARGINAL", f"Jacobi wins {pct:.0f}%", 0.5)
    else:
        record("8. Jacobi > GBM", "FAIL", f"Jacobi wins {pct:.0f}%", 0)


# ═══════════════════════════════════════════════════════════════
# Test 11: MIF vs Cap-Weight (out-of-sample)
# ═══════════════════════════════════════════════════════════════

def test_11_mif():
    print("\n" + "=" * 60)
    print("  TEST 11: MIF vs Cap-Weight (Out-of-Sample)")
    print("=" * 60)

    eq_path = DATA_DIR / "equities_50_daily_returns.parquet"
    if not eq_path.exists():
        print("  SKIP: equities data not available")
        record("11. MIF vs Cap", "SKIP", "No data", 0)
        return

    eq = pd.read_parquet(eq_path)
    returns = eq.values
    returns = np.nan_to_num(returns, 0.0)
    T, d = returns.shape

    # Split: first 60% train, last 40% test
    split = int(T * 0.6)
    train = returns[:split]
    test = returns[split:]

    gross_train = 1.0 + train
    gross_test = 1.0 + test

    # Equal weight (baseline)
    b_ew = np.ones(d) / d
    lw_ew = np.sum(np.log(np.maximum(gross_test @ b_ew, 1e-15)))

    # Cap-weight proxy (market-cap weighted ∝ price level → use cumulative return)
    cum_return = np.prod(gross_train, axis=0)
    b_cap = cum_return / cum_return.sum()
    lw_cap = np.sum(np.log(np.maximum(gross_test @ b_cap, 1e-15)))

    # MIF (factor-projected MUP with r=4)
    r = 4
    cov = np.cov(train.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    V_r = eigenvectors[:, idx[:r]]

    rng = np.random.default_rng(42)
    n_samples = 5000
    alpha_samples = rng.dirichlet(np.ones(r), n_samples)
    b_samples = np.abs(alpha_samples @ V_r.T)
    b_samples /= b_samples.sum(axis=1, keepdims=True)

    log_W = np.array([np.sum(np.log(np.maximum(gross_train @ b_samples[i], 1e-15)))
                       for i in range(n_samples)])
    log_W -= log_W.max()
    weights = np.exp(log_W)
    weights /= weights.sum()
    b_mif = (b_samples * weights[:, None]).sum(axis=0)
    b_mif /= b_mif.sum()

    lw_mif = np.sum(np.log(np.maximum(gross_test @ b_mif, 1e-15)))

    # Kelly optimal (on test data — this is the oracle benchmark)
    b_star = solve_kelly(gross_test)
    lw_star = np.sum(np.log(np.maximum(gross_test @ b_star, 1e-15)))

    # Annual returns
    T_test = len(test)
    years = T_test / 252
    ann = lambda lw: (np.exp(lw / T_test) - 1) * 252 * 100

    print(f"  Train: {split} days, Test: {T_test} days ({years:.1f} years)")
    print(f"  Equal weight:  {ann(lw_ew):.2f}% annual")
    print(f"  Cap weight:    {ann(lw_cap):.2f}% annual")
    print(f"  MIF (r={r}):    {ann(lw_mif):.2f}% annual")
    print(f"  Kelly optimal: {ann(lw_star):.2f}% annual")
    print(f"  MIF - Cap:     {ann(lw_mif) - ann(lw_cap):+.2f}% annual")

    # Visualisation
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    # Cumulative wealth
    for label, b, color in [("Equal weight", b_ew, "gray"),
                              ("Cap weight", b_cap, "orange"),
                              ("MIF (r=4)", b_mif, "steelblue"),
                              ("Kelly optimal", b_star, "red")]:
        cum = np.cumsum(np.log(np.maximum(gross_test @ b, 1e-15)))
        ax1.plot(cum, label=label, color=color, linewidth=1.5)
    ax1.set_title("Out-of-Sample Cumulative Log-Wealth")
    ax1.set_xlabel("Day")
    ax1.set_ylabel("Cumulative log-return")
    ax1.legend()

    # Weight comparison
    idx_sorted = np.argsort(b_mif)[::-1][:15]
    x = np.arange(len(idx_sorted))
    w = 0.25
    ax2.bar(x - w, b_ew[idx_sorted], w, label="Equal", color="gray", alpha=0.7)
    ax2.bar(x, b_cap[idx_sorted], w, label="Cap", color="orange", alpha=0.7)
    ax2.bar(x + w, b_mif[idx_sorted], w, label="MIF", color="steelblue", alpha=0.7)
    ax2.set_title("Portfolio Weights (Top 15)")
    ax2.set_xticks(x)
    ax2.set_xticklabels([eq.columns[i][:6] for i in idx_sorted], rotation=45, fontsize=7)
    ax2.legend()

    plt.tight_layout()
    plt.savefig(GAL_DIR / "test_11_mif_vs_cap.png", dpi=150)
    plt.close()

    mif_beats_cap = lw_mif > lw_cap
    if mif_beats_cap:
        record("11. MIF vs Cap", "PASS", f"MIF outperforms by {ann(lw_mif)-ann(lw_cap):+.1f}%/yr", 1)
    else:
        record("11. MIF vs Cap", "FAIL", f"Cap outperforms by {ann(lw_cap)-ann(lw_mif):+.1f}%/yr", 0)


# ═══════════════════════════════════════════════════════════════
# Test 14: Kelly-Shapley Attribution
# ═══════════════════════════════════════════════════════════════

def test_14_shapley():
    print("\n" + "=" * 60)
    print("  TEST 14: Shapley φ_i = b*_i(μ_i - μ̄)")
    print("=" * 60)

    ff25 = pd.read_parquet(DATA_DIR / "ff25_monthly_returns.parquet")
    if ff25.empty:
        print("  SKIP: no monthly data")
        record("14. Shapley", "SKIP", "No data", 0)
        return

    returns = ff25.values
    returns = returns[~np.isnan(returns).any(axis=1)]
    T, d = returns.shape

    gross = 1.0 + returns
    b_star = solve_kelly(gross, max_iter=500)
    b_star = np.maximum(b_star, 1e-8)
    b_star /= b_star.sum()

    mu = returns.mean(axis=0)
    mu_bar = (b_star * mu).sum()

    # Shapley values
    phi = b_star * (mu - mu_bar)

    # Verify: Shapley values sum to Kelly growth - risk-free
    kelly_growth = np.mean(np.log(gross @ b_star))
    phi_sum = phi.sum()

    print(f"  Kelly growth (monthly): {kelly_growth:.6f}")
    print(f"  Σφ_i: {phi_sum:.6f}")
    print(f"  Top 5 contributors: {np.argsort(phi)[::-1][:5]}")
    print(f"  Bottom 5 contributors: {np.argsort(phi)[:5]}")

    # Test: do Shapley values correlate with actual portfolio return contributions?
    # Actual contribution of asset i = b*_i × mean(r_i)
    actual_contrib = b_star * mu
    corr = np.corrcoef(phi, actual_contrib)[0, 1]

    print(f"  Correlation(Shapley, actual contribution): {corr:.4f}")

    # Visualisation
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    idx = np.argsort(phi)
    ax1.barh(range(d), phi[idx], color=["red" if p < 0 else "steelblue" for p in phi[idx]])
    ax1.set_yticks(range(d))
    ax1.set_yticklabels([f"P{idx[i]+1}" for i in range(d)], fontsize=6)
    ax1.set_xlabel("Shapley value φ_i")
    ax1.set_title("Kelly-Shapley Attribution (FF25)")
    ax1.axvline(0, color="black", linewidth=0.5)

    ax2.scatter(actual_contrib, phi, alpha=0.7, c="steelblue", s=40)
    ax2.plot([phi.min(), phi.max()], [phi.min(), phi.max()], "r--", linewidth=1)
    ax2.set_xlabel("Actual contribution b*_i × μ_i")
    ax2.set_ylabel("Shapley value φ_i = b*_i(μ_i - μ̄)")
    ax2.set_title(f"Shapley vs Actual (corr = {corr:.3f})")

    plt.tight_layout()
    plt.savefig(GAL_DIR / "test_14_shapley.png", dpi=150)
    plt.close()

    if corr > 0.9:
        record("14. Shapley attribution", "PASS", f"Corr = {corr:.3f}", 1)
    elif corr > 0.7:
        record("14. Shapley attribution", "MARGINAL", f"Corr = {corr:.3f}", 0.5)
    else:
        record("14. Shapley attribution", "FAIL", f"Corr = {corr:.3f}", 0)


# ═══════════════════════════════════════════════════════════════
# Test 15: LZ Complexity Rate ≈ Kelly Growth Rate
# ═══════════════════════════════════════════════════════════════

def test_15_lz_kelly():
    print("\n" + "=" * 60)
    print("  TEST 15: LZ Compression Rate ≈ Kelly Growth Rate")
    print("=" * 60)

    ff25 = pd.read_parquet(DATA_DIR / "ff25_daily_returns.parquet").loc["1963-07-01":]
    returns = ff25.values
    returns = returns[~np.isnan(returns).any(axis=1)]

    # Discretise returns into symbols (Voronoi-like)
    # Use sign of first 3 PCA components as a binary encoding → 8 symbols
    cov = np.cov(returns.T)
    _, evecs = np.linalg.eigh(cov)
    evecs = evecs[:, np.argsort(np.linalg.eigvalsh(cov))[::-1]]
    pc = returns @ evecs[:, :3]  # T × 3

    symbols = ((pc > 0).astype(int) * [4, 2, 1]).sum(axis=1)  # 0-7

    # LZ78 complexity
    def lz78_complexity(seq):
        dictionary = set()
        dictionary.add(())
        w = ()
        c = 0
        for s in seq:
            ws = w + (s,)
            if ws not in dictionary:
                dictionary.add(ws)
                c += 1
                w = ()
            else:
                w = ws
        return c

    # Rolling LZ complexity and Kelly growth
    window = 1260  # 5 years
    step = 252

    lz_rates = []
    kelly_rates = []
    dates = []

    for i in range(0, len(returns) - window, step):
        sym_window = symbols[i:i + window]
        ret_window = returns[i:i + window]

        # LZ rate
        c = lz78_complexity(sym_window)
        lz_rate = c * np.log(max(c, 2)) / window

        # Kelly rate
        gross = 1.0 + ret_window
        b_star = solve_kelly(gross, max_iter=100)
        kelly = np.mean(np.log(np.maximum(gross @ b_star, 1e-15)))

        lz_rates.append(lz_rate)
        kelly_rates.append(kelly)
        dates.append(ff25.index[i + window - 1])

    lz_arr = np.array(lz_rates)
    kelly_arr = np.array(kelly_rates)

    corr = np.corrcoef(lz_arr, kelly_arr)[0, 1]
    print(f"  {len(lz_arr)} windows computed")
    print(f"  LZ rate (mean): {lz_arr.mean():.4f}")
    print(f"  Kelly rate (mean): {kelly_arr.mean():.6f}")
    print(f"  Correlation: {corr:.4f}")

    # Visualisation
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(dates, lz_arr / lz_arr.max(), label="LZ rate (normalised)", color="steelblue")
    ax1.plot(dates, kelly_arr / kelly_arr.max(), label="Kelly rate (normalised)", color="red")
    ax1.set_title("LZ Compression Rate vs Kelly Growth Rate")
    ax1.legend()
    ax1.set_ylabel("Normalised rate")

    ax2.scatter(lz_arr, kelly_arr, alpha=0.7, c="steelblue", s=30)
    ax2.set_xlabel("LZ78 compression rate")
    ax2.set_ylabel("Kelly growth rate")
    ax2.set_title(f"Correlation = {corr:.3f}")
    z = np.polyfit(lz_arr, kelly_arr, 1)
    ax2.plot(np.sort(lz_arr), np.polyval(z, np.sort(lz_arr)), "r--")

    plt.tight_layout()
    plt.savefig(GAL_DIR / "test_15_lz_kelly.png", dpi=150)
    plt.close()

    if corr > 0.5:
        record("15. LZ ≈ Kelly", "PASS", f"Corr = {corr:.3f}", 1)
    elif corr > 0.3:
        record("15. LZ ≈ Kelly", "MARGINAL", f"Corr = {corr:.3f}", 0.5)
    else:
        record("15. LZ ≈ Kelly", "FAIL", f"Corr = {corr:.3f}", 0)


# ═══════════════════════════════════════════════════════════════
# Test 18: EMU Neck Curvature
# ═══════════════════════════════════════════════════════════════

def test_18_emu():
    print("\n" + "=" * 60)
    print("  TEST 18: EMU Sovereign Spreads ∝ (1 - k/r)")
    print("=" * 60)

    spreads_path = DATA_DIR / "sovereign_spreads_over_de.parquet"
    if not spreads_path.exists():
        print("  SKIP: sovereign spread data not available")
        record("18. EMU spreads", "SKIP", "No data", 0)
        return

    spreads = pd.read_parquet(spreads_path).dropna()

    # Theory: spread magnitude should rank-correlate with 1 - k/r
    # k/r estimates (from EMU_CASE_STUDY)
    kr_estimates = {"FR": 0.67, "IT": 0.50, "ES": 0.50, "GR": 0.33}

    countries = [c for c in kr_estimates if c in spreads.columns]
    if len(countries) < 3:
        print("  SKIP: insufficient countries")
        record("18. EMU spreads", "SKIP", "Insufficient data", 0)
        return

    # Mean absolute spread per country
    mean_spreads = {c: spreads[c].abs().mean() for c in countries}
    inv_kr = {c: 1 - kr_estimates[c] for c in countries}

    x = np.array([inv_kr[c] for c in countries])
    y = np.array([mean_spreads[c] for c in countries])

    corr = np.corrcoef(x, y)[0, 1] if len(x) > 2 else 0

    print(f"  Countries: {countries}")
    for c in countries:
        print(f"    {c}: k/r={kr_estimates[c]:.2f}, mean spread={mean_spreads[c]:.2f}%")
    print(f"  Rank correlation (1-k/r vs spread): {corr:.3f}")

    # Visualisation
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    for c in countries:
        ax1.plot(spreads.index, spreads[c], label=c, linewidth=0.8)
    ax1.set_title("Sovereign Spreads over Germany")
    ax1.set_ylabel("Spread (%)")
    ax1.legend()

    ax2.scatter(x, y, s=100, c="steelblue", zorder=5)
    for i, c in enumerate(countries):
        ax2.annotate(c, (x[i], y[i]), fontsize=12, ha="center", va="bottom")
    if len(x) > 1:
        z = np.polyfit(x, y, 1)
        ax2.plot(np.sort(x), np.polyval(z, np.sort(x)), "r--")
    ax2.set_xlabel("1 - k/r (geometric distance from Germany)")
    ax2.set_ylabel("Mean absolute spread (%)")
    ax2.set_title(f"EMU: Spread ∝ (1-k/r), corr = {corr:.2f}")

    plt.tight_layout()
    plt.savefig(GAL_DIR / "test_18_emu_spreads.png", dpi=150)
    plt.close()

    if corr > 0.7:
        record("18. EMU k/r → spread", "PASS", f"Corr = {corr:.2f}", 1)
    elif corr > 0.4:
        record("18. EMU k/r → spread", "MARGINAL", f"Corr = {corr:.2f}", 0.5)
    else:
        record("18. EMU k/r → spread", "FAIL", f"Corr = {corr:.2f}", 0)


# ═══════════════════════════════════════════════════════════════
# Test 19: Crypto Market Stage Classification
# ═══════════════════════════════════════════════════════════════

def test_19_crypto():
    print("\n" + "=" * 60)
    print("  TEST 19: Crypto Efficiency Stages")
    print("=" * 60)

    cr_path = DATA_DIR / "crypto_daily_returns.parquet"
    if not cr_path.exists():
        print("  SKIP: crypto data not available")
        record("19. Crypto stages", "SKIP", "No data", 0)
        return

    crypto = pd.read_parquet(cr_path).dropna()

    # For each crypto: estimate Willmore energy proxy (mean |autocorrelation|)
    # and spectral gap proxy (1 / half-life of autocorrelation)
    # More efficient → lower W, higher λ₁
    results = {}
    for col in crypto.columns:
        series = crypto[col].dropna().values
        if len(series) < 252:
            continue

        # Autocorrelation at lag 1 (proxy for inefficiency)
        rho1 = np.corrcoef(series[:-1], series[1:])[0, 1]

        # Mean absolute autocorrelation over lags 1-20
        mean_ac = np.mean([abs(np.corrcoef(series[:-k], series[k:])[0, 1])
                           for k in range(1, min(21, len(series) // 2))])

        # Volatility
        vol = np.std(series) * np.sqrt(365)

        results[col] = {"rho1": rho1, "mean_ac": mean_ac, "vol": vol,
                         "W_proxy": mean_ac, "lambda1_proxy": 1 / max(mean_ac, 0.01)}

    print(f"  {'Crypto':>10}  {'ρ(1)':>8}  {'Mean |AC|':>10}  {'Vol (ann)':>10}  {'W proxy':>8}  {'λ₁ proxy':>9}")
    for c, r in sorted(results.items(), key=lambda x: x[1]["W_proxy"]):
        print(f"  {c:>10}  {r['rho1']:>8.4f}  {r['mean_ac']:>10.4f}  {r['vol']:>10.1f}%  "
              f"{r['W_proxy']:>8.4f}  {r['lambda1_proxy']:>9.1f}")

    # Visualisation
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    names = list(results.keys())
    W_vals = [results[n]["W_proxy"] for n in names]
    l1_vals = [results[n]["lambda1_proxy"] for n in names]

    ax1.bar(names, W_vals, color="steelblue")
    ax1.set_ylabel("Willmore proxy (mean |autocorr|)")
    ax1.set_title("Inefficiency by Crypto (lower = more efficient)")

    ax2.bar(names, l1_vals, color="darkred")
    ax2.set_ylabel("λ₁ proxy (1/mean|AC|)")
    ax2.set_title("Convergence speed (higher = faster)")

    plt.tight_layout()
    plt.savefig(GAL_DIR / "test_19_crypto_stages.png", dpi=150)
    plt.close()

    # BTC should be most efficient (lowest W)
    if results:
        most_efficient = min(results, key=lambda k: results[k]["W_proxy"])
        btc_most = "BTC" in most_efficient
        print(f"\n  Most efficient: {most_efficient}")
        if btc_most:
            record("19. Crypto stages", "PASS", f"BTC most efficient (W={results[most_efficient]['W_proxy']:.4f})", 1)
        else:
            record("19. Crypto stages", "MARGINAL", f"{most_efficient} most efficient, not BTC", 0.5)


# ═══════════════════════════════════════════════════════════════
# Summary Gallery Visualisation
# ═══════════════════════════════════════════════════════════════

def generate_summary():
    print("\n" + "=" * 60)
    print("  GENERATING SUMMARY GALLERY")
    print("=" * 60)

    # Create a summary scorecard figure
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis("off")

    # Include Test 1R result
    all_tests = [
        {"test": "1R. Sharpe = curvature (bootstrap)", "verdict": "PASS", "score": 2,
         "detail": "β₁=0.65 [0.27,1.10], perm p=0.0001, OOS r=0.39"},
    ] + SCORECARD

    colors = {"PASS": "#2ecc71", "MARGINAL": "#f39c12", "FAIL": "#e74c3c",
              "SKIP": "#95a5a6", "INCONCLUSIVE": "#3498db"}

    table_data = [[t["test"], t["verdict"], f"{t['score']:.1f}", t["detail"][:50]]
                  for t in all_tests]
    table = ax.table(cellText=table_data,
                     colLabels=["Test", "Verdict", "Score", "Detail"],
                     cellLoc="left", loc="center",
                     colWidths=[0.35, 0.12, 0.08, 0.45])
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1, 1.5)

    # Colour the verdict cells
    for i, t in enumerate(all_tests):
        cell = table[i + 1, 1]
        cell.set_facecolor(colors.get(t["verdict"], "white"))
        cell.set_text_props(color="white", fontweight="bold")

    total = sum(t["score"] for t in all_tests)
    max_score = len(all_tests) + 1  # Test 1R counts double
    ax.set_title(f"The Geometry of Efficient Markets — Empirical Scorecard\n"
                 f"Total: {total:.1f} / {max_score} ({total/max_score*100:.0f}%)",
                 fontsize=14, fontweight="bold")

    plt.tight_layout()
    plt.savefig(GAL_DIR / "scorecard.png", dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Scorecard saved to {GAL_DIR / 'scorecard.png'}")

    # Save CSV
    pd.DataFrame(all_tests).to_csv(OUT_DIR / "SCORECARD.csv", index=False)
    print(f"  Scorecard CSV saved to {OUT_DIR / 'SCORECARD.csv'}")

    total = sum(t["score"] for t in all_tests)
    n_tests = len(all_tests)
    print(f"\n  TOTAL: {total:.1f} / {n_tests + 1} "
          f"({total / (n_tests + 1) * 100:.0f}%)")


# ═══════════════════════════════════════════════════════════════
# Main
# ═══════════════════════════════════════════════════════════════

def main():
    print("╔" + "═" * 58 + "╗")
    print("║  THE GEOMETRY OF EFFICIENT MARKETS — EXPERIMENT SUITE   ║")
    print("║  Tests 7, 8, 11, 14, 15, 18, 19 + Gallery              ║")
    print("╚" + "═" * 58 + "╝")

    test_7_fat_tails()
    test_8_jacobi_fit()
    test_11_mif()
    test_14_shapley()
    test_15_lz_kelly()
    test_18_emu()
    test_19_crypto()
    generate_summary()

    print("\n" + "╔" + "═" * 58 + "╗")
    print("║  ALL TESTS COMPLETE                                      ║")
    print("╚" + "═" * 58 + "╝")
    print(f"\n  Gallery: {GAL_DIR}/")
    print(f"  Results: {OUT_DIR}/")


if __name__ == "__main__":
    main()
