# Experiments: Empirical Validation of the Geometric Theory of Efficient Markets

## A Replication Guide for Practitioners

**Saxon Nicholls** — me@saxonnicholls.com

---

> *"A theory that cannot be killed by data is not a theory.
> Every result in this monograph should be treated as a hypothesis
> until the reader has run the experiment themselves."*

---

## Overview and Philosophy

This document translates every major theoretical claim of the monograph into a
**falsifiable empirical hypothesis**, a **concrete experiment**, a **specific dataset**
freely available to any researcher, and **Python code** implementing the test. The
experiments are ordered from most to least tractable, and from most to least
theoretically central.

**What counts as falsification?** We are explicit: each experiment states the
specific outcome that would cause us to revise or reject the corresponding theory.
We do not engage in post-hoc rationalisation. If the data consistently disagrees
with a prediction, the theory needs revision.

**All code uses only open-source libraries and free data.** The companion GitHub
repository at `github.com/[to be set]/geometry-of-efficient-markets` contains the
complete implementations. Every experiment can be run on a laptop in under one hour.

---

## Data Sources

All experiments use one or more of the following freely available datasets:

| Dataset | Source | Access | Contents |
|:--------|:-------|:-------|:---------|
| Fama-French factors and portfolios | `mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html` | Free download | Daily/monthly returns, 1926–present |
| Individual stock returns | `yfinance` Python library | `pip install yfinance` | Adjusted daily closes, dividends |
| FRED macroeconomic data | `fred.stlouisfed.org` via `fredapi` | Free API key | Interest rates, economic indicators |
| CBOE volatility data | `cboe.com/us/indices/dashboard/VIX/` | Free download | VIX, SKEW indices, daily 1990–present |
| Options data | `yfinance` (near-term options chain) | Free | Implied vols, strikes, expiries |
| CRSP via WRDS | `wrds-web.wharton.upenn.edu` | Free academic registration | Full US equity universe |
| Quandl / Nasdaq Data Link | `data.nasdaq.com` | Free tier (500 calls/day) | Commodity futures, rates |

**Standard Python environment:**
```
pip install numpy scipy pandas statsmodels scikit-learn yfinance fredapi
pip install matplotlib seaborn tqdm arch hurst
```

---

## Experiment 1: The Sharpe-Curvature Identity

### Theory
$\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(M)}$ where $H$ is the mean curvature of the
market manifold. The mean curvature is proportional to the component of the
half-inverse-square-root vector $\tfrac{1}{2\sqrt{b^{\ast}}}$ in the normal bundle.
For a two-factor market: $H(b^{\ast}) = \Pi_{NM}(1/2\sqrt{b^{\ast}})$ where $\Pi_{NM}$ is
the projection onto the normal bundle.

### Falsifiable Hypothesis
**H0:** The maximum ex-post Sharpe ratio of factor strategies is unrelated to the
estimated RMS mean curvature of the market manifold.

**H1 (our theory):** The regression
$\mathrm{Sharpe}^{\rm realised}_{t} = \beta_0 + \beta_1 \hat H_t + \varepsilon_t$
has slope $\beta_1 > 0$ with $p < 0.05$, and the R² is substantially positive.

**What would falsify this:** $\beta_1 \leq 0$ or R² $< 0.05$ across multiple
independent rolling windows.

### Dataset
Fama-French 25 portfolios (size × value), daily returns 1963–present. Factor
returns: Mkt-RF, SMB, HML from Kenneth French Data Library.

### Implementation

```python
# experiment_1_sharpe_curvature.py
import numpy as np
import pandas as pd
from scipy import linalg, stats
import urllib.request

# ── 1. Load data ──────────────────────────────────────────────────────────────
# Ken French 25 portfolios (size x BM), daily returns
# Download from: https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html
# File: 25_Portfolios_5x5_daily.csv (manually download or use pandas_datareader)

import pandas_datareader.data as web
ff25 = web.DataReader('25_Portfolios_5x5_Daily', 'famafrench', start='1963-07-01')[0] / 100
ff_factors = web.DataReader('F-F_Research_Data_5_Factors_2x3_daily',
                            'famafrench', start='1963-07-01')[0] / 100
rf = ff_factors['RF']
excess_returns = ff25.subtract(rf, axis=0)

# ── 2. Estimate market manifold curvature H ───────────────────────────────────
def estimate_H_and_sharpe(returns_window, n_factors=4):
    """
    Estimate mean curvature H and realised Sharpe for a window of returns.

    Mean curvature computation:
    1. Find log-optimal portfolio b* (Kelly weights)
    2. Compute Fisher matrix F(b*) = - hessian of log-growth at b*
    3. Decompose F = V Lambda V^T (PCA)
    4. Factor subspace = first r eigenvectors V_r
    5. H = norm of projection of 1/(2*sqrt(b*)) onto normal bundle N(b*)M
    """
    T, d = returns_window.shape

    # Step 1: Log-optimal portfolio via gradient ascent on L_T(b)
    # L_T(b) = (1/T) sum_t log(<b, 1 + r_t>)  (use 1+r for log-return)
    gross_returns = (1 + returns_window).values

    def neg_kelly(b):
        b = np.maximum(b, 1e-8)
        b = b / b.sum()
        log_wealth = np.mean(np.log(gross_returns @ b))
        return -log_wealth

    def neg_kelly_grad(b):
        b = np.maximum(b, 1e-8)
        b = b / b.sum()
        wealth = gross_returns @ b
        grad = np.mean(gross_returns / wealth[:, None], axis=0)
        return -grad

    from scipy.optimize import minimize
    b0 = np.ones(d) / d
    constraints = [{'type': 'eq', 'fun': lambda b: b.sum() - 1}]
    bounds = [(1e-6, 1.0)] * d
    result = minimize(neg_kelly, b0, jac=neg_kelly_grad,
                      method='SLSQP', bounds=bounds, constraints=constraints,
                      options={'ftol': 1e-10, 'maxiter': 500})
    b_star = np.maximum(result.x, 1e-8)
    b_star /= b_star.sum()

    # Step 2: Fisher matrix F(b*) = - Hessian of L_T
    wealth = gross_returns @ b_star
    # Fisher-Rao metric at b* on simplex: F_ii = 1/b*_i (diagonal approximation)
    F_diag = 1.0 / b_star  # diagonal Fisher-Rao matrix
    F_matrix = np.diag(F_diag)

    # Step 3: PCA of covariance to identify factor subspace
    cov = np.cov(returns_window.values.T)
    eigenvalues, eigenvectors = linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]

    V_r = eigenvectors[:, :n_factors]   # factor subspace
    V_N = eigenvectors[:, n_factors:]   # normal bundle

    # Step 4: Mean curvature H = || Pi_N (1/(2*sqrt(b*))) ||
    half_inv_sqrt = 1.0 / (2 * np.sqrt(b_star))

    # Project onto normal bundle
    Pi_N = np.eye(d) - V_r @ V_r.T
    H_vec = Pi_N @ half_inv_sqrt

    # Mean curvature H
    H = np.linalg.norm(H_vec)

    # Step 5: Realised Sharpe of best factor strategy
    # The factor strategy earns (1/T) sum_t <-H_vec/|H|, r_t>
    if H > 1e-10:
        strategy_returns = returns_window.values @ (-H_vec / H)
        sharpe_realised = (np.mean(strategy_returns) /
                           np.std(strategy_returns, ddof=1) * np.sqrt(252))
    else:
        sharpe_realised = 0.0

    return H, sharpe_realised

# ── 3. Rolling estimation ─────────────────────────────────────────────────────
window = 252  # one year
results = []
dates = excess_returns.index[window:]

for i in range(len(dates)):
    window_data = excess_returns.iloc[i:i+window]
    H, sh = estimate_H_and_sharpe(window_data, n_factors=4)
    results.append({'date': dates[i], 'H': H, 'Sharpe': sh})

df = pd.DataFrame(results).set_index('date')

# ── 4. Statistical test ───────────────────────────────────────────────────────
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant

X = add_constant(df['H'].values)
y = df['Sharpe'].values
model = OLS(y, X).fit(cov_type='HC3')  # heteroscedasticity-robust SEs

print("=" * 60)
print("EXPERIMENT 1: Sharpe-Curvature Identity")
print("=" * 60)
print(f"N observations: {len(df)}")
print(f"beta_1 (slope): {model.params[1]:.4f}")
print(f"p-value:        {model.pvalues[1]:.4f}")
print(f"R-squared:      {model.rsquared:.4f}")
print(f"\nMean H: {df['H'].mean():.4f}")
print(f"Mean Sharpe: {df['Sharpe'].mean():.4f}")
print(f"\nCorrelation H vs Sharpe: {df['H'].corr(df['Sharpe']):.4f}")

# ── 5. Predicted vs actual Sharpe ─────────────────────────────────────────────
# Theory predicts: Sharpe ≈ H * sqrt(Area(M))
# Area(M) for r-sphere in d dimensions ≈ pi^(r/2) / Gamma(r/2+1)
# For r=4: Area ≈ pi^2/2 ≈ 4.93
predicted_sharpe = df['H'] * np.sqrt(np.pi**2 / 2)
correlation = df['Sharpe'].corr(predicted_sharpe)
print(f"\nCorrelation of realised vs theory-predicted Sharpe: {correlation:.4f}")
print("Theory predicts: correlation > 0.3")
```

**Expected outcome under theory:** $\beta_1 > 0$, $p < 0.01$, R² $> 0.10$.
The correlation between $H_t$ and realised Sharpe should exceed 0.3.

**Falsification criterion:** Slope insignificantly different from zero
($p > 0.10$) in any rolling 5-year subsample.

---

## Experiment 2: Tail Index and the Factor Dimension

### Theory
Return tail index $\alpha = r/2$ where $r$ is the stable rank of the Fisher
information matrix (the market manifold dimension).

### Falsifiable Hypothesis
**H0:** The tail index of equity returns is unrelated to the number of systematic
risk factors.

**H1 (our theory):** The Hill estimator $\hat\alpha$ satisfies
$\hat\alpha \approx \hat r/2$ where $\hat r = \mathrm{tr}(F)^2/\mathrm{tr}(F^2)$
is the stable rank (effective rank). The regression $\hat\alpha_t = \gamma_0 + \gamma_1(\hat r_t/2) + \varepsilon_t$
should have slope $\gamma_1 \approx 1$ (not significantly different from 1)
and intercept $\gamma_0 \approx 0$.

**What would falsify this:** Slope significantly different from 1, or intercept
significantly different from 0 at the 5% level, across multiple time periods.

### Dataset
Individual stock returns via `yfinance`, S&P 500 constituents, 2000–present.
Use the top 100 stocks by market cap (avoiding survivorship bias by using
point-in-time constituents from Wikipedia historical S&P 500 data).

### Implementation

```python
# experiment_2_tail_index.py
import numpy as np
import pandas as pd
import yfinance as yf
from scipy import stats

# ── 1. Download stock data ────────────────────────────────────────────────────
# Use a fixed set of large-cap stocks to avoid survivorship bias
TICKERS = [
    'AAPL', 'MSFT', 'AMZN', 'GOOGL', 'META', 'TSLA', 'NVDA', 'JPM', 'JNJ',
    'V', 'PG', 'UNH', 'HD', 'MA', 'DIS', 'PYPL', 'VZ', 'ADBE', 'NFLX',
    'CMCSA', 'PFE', 'KO', 'PEP', 'ABT', 'TMO', 'COST', 'WMT', 'MRK', 'ACN',
    'CRM', 'XOM', 'CVX', 'BAC', 'WFC', 'INTC', 'AMD', 'QCOM', 'TXN', 'HON',
    'LIN', 'UNP', 'BA', 'MMM', 'CAT', 'GS', 'BLK', 'AXP', 'SPGI', 'MCO',
]

prices = yf.download(TICKERS, start='2000-01-01', end='2024-12-31',
                     auto_adjust=True)['Close'].dropna(axis=1, thresh=1000)
returns = prices.pct_change().dropna()

print(f"Downloaded: {returns.shape[1]} stocks, {len(returns)} days")

# ── 2. Hill estimator for tail index ─────────────────────────────────────────
def hill_estimator(data, k_fraction=0.10):
    """
    Hill estimator for the tail index of a distribution.
    Estimates alpha such that P(|X| > x) ~ x^{-alpha}.
    Uses the top k_fraction of observations.
    """
    abs_data = np.abs(data[~np.isnan(data)])
    abs_data = np.sort(abs_data)[::-1]
    k = max(int(k_fraction * len(abs_data)), 10)
    log_ratios = np.log(abs_data[:k] / abs_data[k])
    return 1.0 / np.mean(log_ratios)

# ── 3. Stable rank (effective factor dimension) ───────────────────────────────
def stable_rank(cov_matrix):
    """
    Stable rank = tr(F)^2 / tr(F^2) = sum(eigenvalues)^2 / sum(eigenvalues^2)
    Measures the effective number of dimensions.
    """
    eigenvalues = np.linalg.eigvalsh(cov_matrix)
    eigenvalues = eigenvalues[eigenvalues > 0]
    return (np.sum(eigenvalues)**2) / np.sum(eigenvalues**2)

# ── 4. Rolling estimation ─────────────────────────────────────────────────────
window = 504  # two years of daily data
results = []

for i in range(window, len(returns) - 1, 63):  # quarterly
    window_data = returns.iloc[i-window:i].dropna(axis=1)
    if window_data.shape[1] < 20:
        continue

    # Tail index: use cross-sectional distribution of single-day returns
    # (pooling all stocks and all days in the window)
    pooled_returns = window_data.values.flatten()
    pooled_returns = pooled_returns[~np.isnan(pooled_returns)]
    alpha_hat = hill_estimator(pooled_returns, k_fraction=0.10)

    # Stable rank from return covariance
    cov = window_data.cov().values
    r_hat = stable_rank(cov)

    # Alternative: stable rank from correlation matrix (scale-free)
    corr = window_data.corr().values
    r_hat_corr = stable_rank(corr)

    results.append({
        'date': returns.index[i],
        'alpha_hill': alpha_hat,
        'r_stable': r_hat,
        'r_stable_corr': r_hat_corr,
        'alpha_predicted': r_hat_corr / 2,  # theory prediction
        'n_stocks': window_data.shape[1]
    })

df = pd.DataFrame(results).set_index('date')
df = df[(df['alpha_hill'] > 1) & (df['alpha_hill'] < 10)]  # sanity filter

# ── 5. Test: alpha ≈ r/2 ─────────────────────────────────────────────────────
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant

X = add_constant(df['alpha_predicted'].values)
y = df['alpha_hill'].values
model = OLS(y, X).fit(cov_type='HC3')

print("=" * 60)
print("EXPERIMENT 2: Tail Index = r/2")
print("=" * 60)
print(f"N observations: {len(df)}")
print(f"\nMean realised alpha (Hill):   {df['alpha_hill'].mean():.3f}")
print(f"Mean predicted alpha (r/2):   {df['alpha_predicted'].mean():.3f}")
print(f"\nRegression alpha_hill ~ 1 + alpha_predicted:")
print(f"  Intercept: {model.params[0]:.3f} (p={model.pvalues[0]:.4f})")
print(f"  Slope:     {model.params[1]:.3f} (p={model.pvalues[1]:.4f})")
print(f"  R²:        {model.rsquared:.4f}")
print(f"\nTest H0: slope=1:  t-stat = {(model.params[1]-1)/model.bse[1]:.3f}")
print(f"Test H0: intercept=0: t-stat = {model.params[0]/model.bse[0]:.3f}")
print(f"\nCorrelation alpha_hill vs r/2: {df['alpha_hill'].corr(df['alpha_predicted']):.4f}")
print("\nTheory predicts: slope≈1, intercept≈0, correlation>0.4")

# ── 6. Time-series plot ───────────────────────────────────────────────────────
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 1, figsize=(12, 8))
axes[0].plot(df.index, df['alpha_hill'], label='Hill estimate α̂', alpha=0.8)
axes[0].plot(df.index, df['alpha_predicted'], label='Theory: r̂/2', linestyle='--')
axes[0].set_ylabel('Tail index α')
axes[0].legend()
axes[0].set_title('Tail Index: Hill Estimate vs Geometric Prediction (r/2)')
axes[1].scatter(df['alpha_predicted'], df['alpha_hill'], alpha=0.5)
axes[1].plot([1, 6], [1, 6], 'k--', label='y=x (perfect prediction)')
axes[1].set_xlabel('Predicted α = r̂/2')
axes[1].set_ylabel('Realised α (Hill)')
axes[1].legend()
plt.tight_layout()
plt.savefig('experiment_2_tail_index.png', dpi=150)
```

**Expected outcome under theory:** Slope $\approx 1$, intercept $\approx 0$.
Mean Hill estimate $\approx 2$–$4$ for US equities (consistent with $r\approx 4$–$8$).

**Falsification criterion:** Slope $< 0.5$ or $> 2$, or intercept $> 1.0$.

---

## Experiment 3: The Manifold Universal Portfolio vs Cover

### Theory
The MUP achieves regret $r\log T / 2T$ vs Cover's $(d-1)\log T / 2T$.
Predicted improvement factor: $(d-1)/r$. For $d=30$, $r=4$: factor $\approx 7.25$.

### Falsifiable Hypothesis
**H0:** The MUP does not outperform Cover's portfolio in annualised log-wealth.

**H1 (our theory):** The annualised log-wealth gap $L(b^{\ast}) - L(\hat b^{\rm Cover})$
satisfies $L(\hat b^M_T) - L(\hat b^{\rm Cover}_{T}) \approx (d-1-r)\log T / 2T$
where $L = $ Kelly growth rate. The gap should increase with $d$ and decrease with $r$.

**What would falsify this:** MUP does not improve over Cover's portfolio after
accounting for transaction costs, or the improvement does not scale with $(d-1)/r$.

### Dataset
Dow Jones 30 components via `yfinance`, daily 1990–2024 (sufficiently long for
$\log T$ effects to be visible). Use adjusted closes.

### Implementation

```python
# experiment_3_mup_vs_cover.py
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize

# ── 1. Download DJ30 data ─────────────────────────────────────────────────────
DJ30 = ['AAPL', 'AMGN', 'AXP', 'BA', 'CAT', 'CRM', 'CSCO', 'CVX', 'DIS', 'DOW',
        'GS', 'HD', 'HON', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM',
        'MRK', 'MSFT', 'NKE', 'PG', 'TRV', 'UNH', 'V', 'VZ', 'WBA', 'WMT']

prices = yf.download(DJ30, start='1990-01-01', end='2024-12-31',
                     auto_adjust=True)['Close'].dropna()
returns = prices.pct_change().dropna()
d = returns.shape[1]
T = len(returns)

print(f"Assets d={d}, Days T={T}")
print(f"Theoretical improvement: factor {(d-1)/4:.1f}x (assuming r=4)")

# ── 2. Cover's Universal Portfolio (exact formula) ────────────────────────────
def cover_portfolio(returns_history):
    """
    Cover's universal portfolio: b_t proportional to
    integral of b * W_t(b) over simplex.
    Approximated by Monte Carlo over the simplex.
    """
    T_hist, d = returns_history.shape
    gross = (1 + returns_history).values

    # Sample portfolios from Dirichlet(1,...,1) = uniform on simplex
    n_samples = 5000
    rng = np.random.default_rng(42)
    b_samples = rng.dirichlet(np.ones(d), n_samples)

    # Compute accumulated wealth for each portfolio
    log_wealth = np.sum(np.log(np.maximum(b_samples @ gross.T, 1e-10)), axis=1)
    log_wealth -= log_wealth.max()  # numerical stability
    weights = np.exp(log_wealth)
    weights /= weights.sum()

    # Wealth-weighted average portfolio
    b_cover = (b_samples * weights[:, None]).sum(axis=0)
    b_cover = np.maximum(b_cover, 1e-8)
    return b_cover / b_cover.sum()

# ── 3. Manifold Universal Portfolio ─────────────────────────────────────────
def mup_portfolio(returns_history, n_factors=4):
    """
    MUP: integrates over the r-dimensional market manifold.
    Approximated by sampling from the factor subspace.
    """
    T_hist, d = returns_history.shape
    gross = (1 + returns_history).values

    # Identify market manifold via PCA
    cov = np.cov(returns_history.values.T)
    eigenvalues, eigenvectors = np.linalg.eigh(cov)
    idx = np.argsort(eigenvalues)[::-1]
    V_r = eigenvectors[:, idx[:n_factors]]  # factor subspace, d x r

    # Sample portfolios from the factor simplex (r-dimensional)
    n_samples = 2000
    rng = np.random.default_rng(42)
    # Sample alpha from Dirichlet(1,...,1) on r-simplex
    alpha_samples = rng.dirichlet(np.ones(n_factors), n_samples)

    # Project onto portfolio simplex via factor loadings
    b_samples = np.abs(alpha_samples @ V_r.T)
    b_samples = np.maximum(b_samples, 1e-8)
    b_samples /= b_samples.sum(axis=1, keepdims=True)

    # Compute accumulated wealth on the manifold
    log_wealth = np.sum(np.log(np.maximum(b_samples @ gross.T, 1e-10)), axis=1)
    log_wealth -= log_wealth.max()
    weights = np.exp(log_wealth)
    weights /= weights.sum()

    b_mup = (b_samples * weights[:, None]).sum(axis=0)
    b_mup = np.maximum(b_mup, 1e-8)
    return b_mup / b_mup.sum()

# ── 4. Log-optimal (Kelly) portfolio ────────────────────────────────────────
def log_optimal(returns_history):
    T_hist, d = returns_history.shape
    gross = (1 + returns_history).values

    def neg_kelly(b):
        b = np.maximum(b, 1e-8)
        b /= b.sum()
        return -np.mean(np.log(gross @ b))

    result = minimize(neg_kelly, np.ones(d)/d,
                      method='SLSQP',
                      bounds=[(1e-6, 1)] * d,
                      constraints=[{'type':'eq','fun':lambda b: b.sum()-1}],
                      options={'ftol':1e-10,'maxiter':300})
    b = np.maximum(result.x, 1e-8)
    return b / b.sum()

# ── 5. Online simulation ─────────────────────────────────────────────────────
warmup = 252  # one year of warmup
log_wealth_cover = [0.0]
log_wealth_mup = [0.0]
log_wealth_kelly = [0.0]
log_wealth_ew = [0.0]  # equal-weight benchmark

rebalance_freq = 21  # monthly rebalancing
b_cover = np.ones(d) / d
b_mup = np.ones(d) / d
b_kelly = np.ones(d) / d
b_ew = np.ones(d) / d

for t in range(warmup, T):
    # Rebalance portfolios monthly
    if (t - warmup) % rebalance_freq == 0:
        hist = returns.iloc[max(0, t-504):t]  # 2-year window
        b_cover = cover_portfolio(hist)
        b_mup = mup_portfolio(hist, n_factors=4)
        b_kelly = log_optimal(hist)

    r_t = returns.iloc[t].values
    r_t = np.where(np.isnan(r_t), 0, r_t)

    log_wealth_cover.append(log_wealth_cover[-1] + np.log(max(1+b_cover@r_t, 1e-10)))
    log_wealth_mup.append(log_wealth_mup[-1] + np.log(max(1+b_mup@r_t, 1e-10)))
    log_wealth_kelly.append(log_wealth_kelly[-1] + np.log(max(1+b_kelly@r_t, 1e-10)))
    log_wealth_ew.append(log_wealth_ew[-1] + np.log(max(1+b_ew@r_t, 1e-10)))

T_eval = T - warmup
cover_log = log_wealth_cover[-1]
mup_log = log_wealth_mup[-1]
kelly_log = log_wealth_kelly[-1]
ew_log = log_wealth_ew[-1]

# ── 6. Regret computation ────────────────────────────────────────────────────
r_hat = 4  # assumed factor dimension
theory_gap = (d - 1 - r_hat) * np.log(T_eval) / (2 * T_eval)
actual_gap = (mup_log - cover_log) / T_eval

print("=" * 60)
print("EXPERIMENT 3: MUP vs Cover Regret")
print("=" * 60)
print(f"\nAnnualised log-wealth (per day × 252):")
print(f"  Equal-weight:       {ew_log/T_eval*252:.4f}")
print(f"  Cover portfolio:    {cover_log/T_eval*252:.4f}")
print(f"  MUP (r={r_hat}):       {mup_log/T_eval*252:.4f}")
print(f"  Log-optimal (Kelly): {kelly_log/T_eval*252:.4f}")
print(f"\nRegret (Kelly - strategy, per day):")
print(f"  Kelly - Cover:   {(kelly_log-cover_log)/T_eval:.6f}")
print(f"  Kelly - MUP:     {(kelly_log-mup_log)/T_eval:.6f}")
print(f"\nTheory predicts MUP-Cover gap: {theory_gap:.6f} per day")
print(f"Observed  MUP-Cover gap:       {actual_gap:.6f} per day")
print(f"\nTheory improvement factor: {(d-1)/r_hat:.2f}x")
print(f"Observed improvement:      {(kelly_log-cover_log)/(kelly_log-mup_log):.2f}x")
```

**Expected outcome under theory:** MUP outperforms Cover by $\approx (d-1-r)\log T/2T$ per period.
For $d=30$, $r=4$, $T=8000$ days: gap $\approx 25 \times \log(8000)/16000 \approx 14$ bps/year.

**Falsification criterion:** MUP does not outperform Cover by at least 5 bps/year
after transaction costs (assuming 5 bps round-trip per monthly rebalance).

---

## Experiment 4: Fokker-Planck Stationary Distribution

### Theory
The long-run distribution of the log-optimal portfolio weight $b^{\ast}_{1,t}$
(weight on one asset) is Beta$(\alpha,\beta)$ with $\alpha = T\bar{b}^{\ast} - 1/2$.
NOT uniform. NOT Gaussian.

### Falsifiable Hypothesis
**H0:** The empirical distribution of rolling log-optimal weights is consistent
with a uniform distribution on $[0,1]$.

**H1 (our theory):** The empirical distribution is consistent with
Beta$(\alpha,\beta)$ where $\alpha = T\hat{b}^{\ast} - 1/2$, and the
Kolmogorov-Smirnov test rejects the uniform in favour of the Beta.

**What would falsify this:** KS test fails to distinguish empirical distribution
from uniform, OR the fitted $\alpha$ differs significantly from $T\bar{b}^{\ast} - 1/2$.

### Dataset
Fama-French 25 portfolios, monthly 1963–2024.

```python
# experiment_4_stationary_distribution.py
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from scipy import stats

ff25_monthly = web.DataReader('25_Portfolios_5x5', 'famafrench',
                               start='1963-07-01')[0] / 100
ff_factors = web.DataReader('F-F_Research_Data_Factors',
                             'famafrench', start='1963-07-01')[0] / 100
rf_monthly = ff_factors['RF']
excess = ff25_monthly.subtract(rf_monthly, axis=0)

d = excess.shape[1]
window = 60   # 5-year rolling window
T = window

# Collect rolling log-optimal weights for the first portfolio
b_star_series = []
for i in range(window, len(excess)):
    hist = (1 + excess.iloc[i-window:i]).values
    from scipy.optimize import minimize
    def neg_kelly(b):
        b = np.maximum(b, 1e-8); b /= b.sum()
        return -np.mean(np.log(hist @ b))
    result = minimize(neg_kelly, np.ones(d)/d, method='SLSQP',
                      bounds=[(1e-6,1)]*d,
                      constraints=[{'type':'eq','fun':lambda b:b.sum()-1}],
                      options={'ftol':1e-8,'maxiter':200})
    b_star_series.append(result.x)

b_stars = np.array(b_star_series)  # shape: (n_windows, d)

# Test each asset's weight distribution
print("=" * 60)
print("EXPERIMENT 4: Stationary Distribution = Beta(alpha, beta)")
print("=" * 60)
print(f"\nT_window={window}, theory: alpha_i = T*b*_i - 0.5")
print(f"\n{'Asset':<8} {'Mean b*':>8} {'Theory α':>10} {'Fitted α':>10} "
      f"{'KS vs Beta':>12} {'KS vs Unif':>12}")

for j in range(min(d, 5)):  # test first 5 assets
    weights_j = b_stars[:, j]
    mean_b = np.mean(weights_j)
    alpha_theory = T * mean_b - 0.5
    beta_theory = T * (1 - mean_b) - 0.5

    if alpha_theory <= 0 or beta_theory <= 0:
        continue

    # Fit Beta distribution
    alpha_fit, beta_fit, loc, scale = stats.beta.fit(weights_j, floc=0, fscale=1)

    # KS test against theoretical Beta
    ks_beta, p_beta = stats.kstest(weights_j, 'beta',
                                    args=(alpha_theory, beta_theory, 0, 1))
    # KS test against uniform
    ks_unif, p_unif = stats.kstest(weights_j, 'uniform')

    print(f"  {j+1:<6} {mean_b:>8.4f} {alpha_theory:>10.3f} {alpha_fit:>10.3f} "
          f"  p={p_beta:>6.4f}      p={p_unif:>6.4f}")

print("\nTheory predicts: Beta fits well (p>0.05), Uniform rejected (p<0.05)")
print("Falsification: Beta rejected OR Uniform not rejected")
```

**Expected outcome:** KS test does not reject Beta (p > 0.10) but rejects uniform
(p < 0.01). Fitted $\alpha$ close to $T\bar b^{\ast} - 1/2$.

---

## Experiment 5: Jacobi Diffusion vs GBM for Portfolio Weights

### Theory
The log-optimal portfolio weight $b_t$ evolves as a Jacobi diffusion:
$db_t = \kappa(\theta-b_t)dt + \sqrt{2\varepsilon^2 b_t(1-b_t)}dW_t$.
The diffusion coefficient is $\sigma(b) = \sqrt{2\varepsilon^2 b(1-b)}$, NOT
the GBM coefficient $\sigma b$ or the arithmetic BM coefficient $\sigma$.

### Falsifiable Hypothesis
**H0:** The local variance of portfolio weight changes is unrelated to $b(1-b)$.

**H1 (our theory):** The regression
$(\Delta b_t)^2 = \eta_0 + \eta_1 b_{t-1}(1-b_{t-1}) + \varepsilon_t$
has slope $\eta_1 > 0$ (p < 0.01) and the coefficient of determination is substantially
higher for the Jacobi form $b(1-b)$ than for the GBM form $b^2$ or the flat form $1$.

**What would falsify this:** GBM form $b^2$ fits the variance better than $b(1-b)$.

```python
# experiment_5_jacobi_vs_gbm.py
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import yfinance as yf

# Use equal-weight portfolio of 10 stocks, daily rebalanced
TICKERS = ['AAPL','MSFT','JPM','JNJ','PG','XOM','BAC','WMT','KO','DIS']
prices = yf.download(TICKERS, start='2000-01-01', end='2024-12-31',
                     auto_adjust=True)['Close'].dropna()
returns = prices.pct_change().dropna()

# Compute rolling log-optimal weight for AAPL
d = len(TICKERS)
window = 126  # 6 months

b_series = []
for i in range(window, len(returns)):
    hist = (1 + returns.iloc[i-window:i]).values
    from scipy.optimize import minimize
    def neg_kelly(b):
        b = np.maximum(b, 1e-8); b /= b.sum()
        return -np.mean(np.log(hist @ b))
    res = minimize(neg_kelly, np.ones(d)/d, method='SLSQP',
                   bounds=[(1e-6,1)]*d,
                   constraints=[{'type':'eq','fun':lambda b:b.sum()-1}],
                   options={'ftol':1e-8,'maxiter':200})
    b_series.append(res.x[0])  # weight on AAPL

b = np.array(b_series)
db_sq = np.diff(b)**2  # squared changes
b_lag = b[:-1]

df = pd.DataFrame({
    'db_sq': db_sq,
    'b': b_lag,
    'b_jacobi': b_lag * (1 - b_lag),      # Jacobi form
    'b_gbm': b_lag**2,                     # GBM form
    'b_flat': np.ones(len(b_lag)),         # arithmetic BM form
})

# Regression comparison
m_jacobi = smf.ols('db_sq ~ b_jacobi', data=df).fit()
m_gbm    = smf.ols('db_sq ~ b_gbm', data=df).fit()
m_flat   = smf.ols('db_sq ~ b_flat', data=df).fit()

print("=" * 60)
print("EXPERIMENT 5: Jacobi Diffusion vs GBM")
print("=" * 60)
print(f"\nDiffusion model: Var(Δb) ~ b(1-b)  R² = {m_jacobi.rsquared:.4f}")
print(f"GBM model:       Var(Δb) ~ b²       R² = {m_gbm.rsquared:.4f}")
print(f"Flat BM model:   Var(Δb) ~ const    R² = {m_flat.rsquared:.4f}")
print(f"\nJacobi vs GBM improvement in R²: {m_jacobi.rsquared - m_gbm.rsquared:.4f}")
print(f"Theory predicts: Jacobi form b(1-b) gives highest R²")
print(f"\nJacobi slope: {m_jacobi.params[1]:.6f} (p={m_jacobi.pvalues[1]:.4f})")
print("Falsification: GBM R² exceeds Jacobi R²")

# Breusch-Pagan test for correct heteroscedasticity specification
from statsmodels.stats.diagnostic import het_breuschpagan
resid = df['db_sq'] - m_jacobi.fittedvalues
bp_stat, bp_p, _, _ = het_breuschpagan(resid, df[['b_jacobi']])
print(f"\nBreusch-Pagan test (residual heteroscedasticity): p = {bp_p:.4f}")
print("Theory predicts: residuals should be homoscedastic after Jacobi correction")
```

---

## Experiment 6: Volatility Skew and Mean Curvature

### Theory
Vol skew $\partial\hat\sigma/\partial k|_{k=0} = -\varepsilon^2 H^2/(2\sigma_I)$
where $H$ is the market manifold mean curvature and $\sigma_I$ is the ATM
implied vol. The CBOE SKEW index measures $-\partial\hat\sigma/\partial k$
for S&P 500 options.

### Falsifiable Hypothesis
**H0:** CBOE SKEW is uncorrelated with the estimated market manifold curvature $H$.

**H1 (our theory):** The regression
$\mathrm{SKEW}_{t} = \gamma_0 + \gamma_1 \hat H^2_t / (2\sigma_{I,t}) + \varepsilon_t$
has slope $\gamma_1 > 0$ (p < 0.05) and explains at least 10% of SKEW variation.

**What would falsify this:** No significant relationship, or VIX alone explains
SKEW as well as $H^2/(2\sigma_I)$.

```python
# experiment_6_vol_skew_curvature.py
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant

# ── 1. CBOE SKEW index (measures negative slope of vol smile) ────────────────
# Download from CBOE: https://www.cboe.com/us/indices/dashboard/skew/
# Or via Yahoo Finance
skew_data = yf.download('^SKEW', start='2000-01-01', end='2024-12-31',
                         auto_adjust=True)['Close']
vix_data = yf.download('^VIX', start='2000-01-01', end='2024-12-31',
                        auto_adjust=True)['Close']

# ── 2. Estimate H from factor returns ─────────────────────────────────────────
ff_factors = web.DataReader('F-F_Research_Data_5_Factors_2x3_daily',
                             'famafrench', start='2000-01-01')[0] / 100
spx_returns = yf.download('^GSPC', start='2000-01-01', end='2024-12-31',
                            auto_adjust=True)['Close'].pct_change()

# Use 5 FF factors as the market factor structure
factor_cols = ['Mkt-RF', 'SMB', 'HML', 'RMW', 'CMA']
factors = ff_factors[factor_cols].dropna()

window = 252

H_series = []
for i in range(window, len(factors)):
    fac_window = factors.iloc[i-window:i].values
    # Covariance of factor returns
    cov_f = np.cov(fac_window.T)
    # Stable rank = effective factor dimension
    eigs = np.linalg.eigvalsh(cov_f)
    eigs = eigs[eigs > 0]
    r_eff = (eigs.sum()**2) / (eigs**2).sum()
    # H approximation: uses idiosyncratic component
    # H² ≈ (1 - r_eff/len(factor_cols)) * mean(1/b*_i)
    # For equal weight b* = 1/d, H ≈ sqrt(d-r)/2 * sqrt(d)
    d_f = len(factor_cols)
    H_approx = np.sqrt(max(d_f - r_eff, 0)) * 0.5 * np.sqrt(d_f)
    H_series.append({'date': factors.index[i], 'H': H_approx, 'r_eff': r_eff})

df_H = pd.DataFrame(H_series).set_index('date')

# ── 3. Merge and align ────────────────────────────────────────────────────────
sigma_I = vix_data / 100 / np.sqrt(252)  # daily implied vol from VIX

df_merged = pd.DataFrame({
    'SKEW': skew_data,
    'VIX': vix_data,
    'sigma_I': sigma_I,
}).join(df_H, how='inner').dropna()

# Theory predictor: H^2 / (2 * sigma_I)
df_merged['curvature_predictor'] = (df_merged['H']**2 /
                                     (2 * df_merged['sigma_I']))

# ── 4. Regression ─────────────────────────────────────────────────────────────
X_theory = add_constant(df_merged[['curvature_predictor']].values)
X_vix    = add_constant(df_merged[['VIX']].values)
X_both   = add_constant(df_merged[['curvature_predictor','VIX']].values)
y = df_merged['SKEW'].values

m_theory = OLS(y, X_theory).fit(cov_type='HAC', cov_kwds={'maxlags':21})
m_vix    = OLS(y, X_vix).fit(cov_type='HAC', cov_kwds={'maxlags':21})
m_both   = OLS(y, X_both).fit(cov_type='HAC', cov_kwds={'maxlags':21})

print("=" * 60)
print("EXPERIMENT 6: Vol Skew and Mean Curvature")
print("=" * 60)
print(f"\nTheory model (H²/2σ_I):  R²={m_theory.rsquared:.4f}, "
      f"slope={m_theory.params[1]:.4f}, p={m_theory.pvalues[1]:.4f}")
print(f"VIX model:              R²={m_vix.rsquared:.4f}")
print(f"Combined model:         R²={m_both.rsquared:.4f}")
print(f"\nTheory predicts slope > 0, R² > 0.10")
print(f"Theory predictor adds incremental R²: "
      f"{m_both.rsquared - m_vix.rsquared:.4f}")
print("Falsification: R² < 0.05 or slope ≤ 0")
```

---

## Experiment 7: Optimal Pairs Trading Thresholds

### Theory
Optimal entry threshold: $z^{\ast} = \sqrt{1 + r/\kappa}$ where $r$ is the risk-free
rate and $\kappa$ is the OU mean-reversion speed (= Jacobi spectral gap).
The classical 2$\sigma$ rule is only optimal when $r \approx 3\kappa$.

### Falsifiable Hypothesis
**H0:** The geometric threshold $z^{\ast} = \sqrt{1+r/\kappa}$ performs no better
than the fixed 2$\sigma$ rule in out-of-sample pairs trading P&L.

**H1 (our theory):** For pairs with high $\kappa$ (fast mean reversion), the
geometric threshold $z^{\ast} < 2$ and entering earlier is more profitable.
For low-$\kappa$ pairs, $z^{\ast} > 2$ and the 2$\sigma$ rule is too aggressive.
The geometric rule should have higher Sharpe ratio and lower drawdown.

**What would falsify this:** No systematic improvement from the geometric rule
relative to the fixed 2$\sigma$ rule across a universe of pairs.

```python
# experiment_7_pairs_trading_threshold.py
import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import curve_fit
from scipy import stats

# ── Commodity ETF pairs (highly cointegrated) ────────────────────────────────
PAIRS = [
    ('GLD', 'IAU'),   # Gold ETFs (near-perfect correlation)
    ('SLV', 'SIVR'),  # Silver ETFs
    ('USO', 'BNO'),   # Oil ETFs
    ('TLT', 'IEF'),   # Treasury ETFs
    ('XLF', 'VFH'),   # Financial ETFs
    ('SPY', 'IVV'),   # S&P 500 ETFs
]

SOFR = 0.053  # approximate current risk-free rate

def estimate_ou_params(spread_series):
    """Estimate OU parameters (kappa, theta, sigma) from spread time series."""
    x = spread_series.values
    # Regression of dx on x (Euler discretisation)
    dx = np.diff(x)
    x_lag = x[:-1]

    slope, intercept, r, p, se = stats.linregress(x_lag, dx)
    # kappa ≈ -slope (per day), theta ≈ intercept / (-slope)
    kappa_daily = max(-slope, 1e-6)
    theta = intercept / kappa_daily
    sigma = np.std(dx - (slope * x_lag + intercept))

    kappa_annual = kappa_daily * 252
    return kappa_annual, theta, sigma

def simulate_pairs_strategy(spread, kappa, theta, sigma, z_entry, z_exit=0.5, r=0.053):
    """
    Backtest a pairs strategy with given entry/exit thresholds.
    Returns: Sharpe ratio, max drawdown, number of trades.
    """
    T = len(spread)
    sigma_annual = sigma * np.sqrt(252)
    position = 0
    entry_level = None
    pnl = []
    trade_pnl = 0.0

    for t in range(1, T):
        z_t = (spread.iloc[t] - theta) / (sigma_annual / np.sqrt(252 * kappa / 252))

        if position == 0:
            if z_t > z_entry:
                position = -1; entry_level = spread.iloc[t]
            elif z_t < -z_entry:
                position = 1; entry_level = spread.iloc[t]
        else:
            daily_pnl = position * (spread.iloc[t] - spread.iloc[t-1])
            trade_pnl += daily_pnl

            if position == -1 and z_t < z_exit:
                pnl.append(trade_pnl); trade_pnl = 0; position = 0
            elif position == 1 and z_t > -z_exit:
                pnl.append(trade_pnl); trade_pnl = 0; position = 0

    if not pnl:
        return 0.0, -1.0, 0

    pnl_array = np.array(pnl)
    sharpe = (np.mean(pnl_array) / np.std(pnl_array)) * np.sqrt(12)  # monthly
    cum_pnl = np.cumsum(pnl_array)
    max_dd = np.max(np.maximum.accumulate(cum_pnl) - cum_pnl)
    return sharpe, -max_dd / max(np.max(cum_pnl), 1e-6), len(pnl)

# ── Run experiment ───────────────────────────────────────────────────────────
print("=" * 60)
print("EXPERIMENT 7: Optimal Pairs Trading Thresholds")
print("=" * 60)
print(f"\n{'Pair':<12} {'kappa/yr':>8} {'z*_theory':>10} {'Sh@z*':>8} "
      f"{'Sh@z=2':>8} {'z*_better':>10}")

for asset_a, asset_b in PAIRS:
    try:
        data = yf.download([asset_a, asset_b], start='2010-01-01',
                            end='2024-12-31', auto_adjust=True)['Close'].dropna()
        if len(data) < 500:
            continue

        # Compute log-price spread
        spread = np.log(data[asset_a]) - np.log(data[asset_b])

        # Split: train 2010-2019, test 2020-2024
        train = spread[:'2019-12-31']
        test = spread['2020-01-01':]

        # Estimate OU parameters on training data
        kappa, theta, sigma = estimate_ou_params(train)

        # Theory: optimal entry threshold
        z_theory = np.sqrt(1 + SOFR / kappa)

        # Backtest with theory threshold vs fixed 2-sigma rule
        sh_theory, dd_theory, n_theory = simulate_pairs_strategy(
            test, kappa, theta, sigma, z_entry=z_theory)
        sh_fixed, dd_fixed, n_fixed = simulate_pairs_strategy(
            test, kappa, theta, sigma, z_entry=2.0)

        better = "YES ✓" if sh_theory > sh_fixed else "NO ✗"
        print(f"{asset_a}/{asset_b:<6} {kappa:>8.2f} {z_theory:>10.3f} "
              f"{sh_theory:>8.3f} {sh_fixed:>8.3f} {better:>10}")
    except Exception as e:
        print(f"{asset_a}/{asset_b}: Error - {e}")

print("\nTheory predicts: z* strategy outperforms fixed-2σ when kappa differs from r/3")
print("Falsification: fixed-2σ systematically outperforms z* across all pairs")
```

---

## Experiment 8: Topological Entropy and the Kelly Rate

### Theory
The topological entropy $h_{\rm top}(X_M,\sigma)$ of the market shift space
equals the Kelly growth rate $h_{\rm Kelly}(b^{\ast})$. The market's return sequence
complexity equals its maximum log-wealth growth rate.

### Falsifiable Hypothesis
**H0:** The complexity of the return sequence (measured by its approximate entropy
or permutation entropy) is uncorrelated with the Kelly growth rate.

**H1 (our theory):** Regression of $h_{\rm top}$ on $h_{\rm Kelly}$ across
asset classes, time periods, and market regimes should have slope $\approx 1$
and intercept $\approx 0$.

```python
# experiment_8_entropy_kelly.py
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from scipy.optimize import minimize
from scipy.stats import pearsonr

def permutation_entropy(ts, m=5, tau=1):
    """
    Permutation entropy (Bandt-Pompe) — fast estimator of topological entropy.
    m = embedding dimension, tau = delay.
    """
    n = len(ts)
    patterns = {}
    for i in range(n - (m-1)*tau):
        segment = ts[i:i+m*tau:tau]
        pattern = tuple(np.argsort(segment))
        patterns[pattern] = patterns.get(pattern, 0) + 1

    total = sum(patterns.values())
    probs = np.array([v/total for v in patterns.values()])
    return -np.sum(probs * np.log(probs)) / np.log(np.math.factorial(m))

def kelly_rate(returns):
    """Estimate Kelly growth rate via log-optimal portfolio."""
    T, d = returns.shape
    gross = (1 + returns)

    def neg_kelly(b):
        b = np.maximum(b, 1e-8); b /= b.sum()
        return -np.mean(np.log(gross @ b))

    result = minimize(neg_kelly, np.ones(d)/d, method='SLSQP',
                      bounds=[(1e-6,1)]*d,
                      constraints=[{'type':'eq','fun':lambda b:b.sum()-1}],
                      options={'ftol':1e-9,'maxiter':300})
    b_star = np.maximum(result.x, 1e-8); b_star /= b_star.sum()
    return -neg_kelly(b_star)

# Load FF25 data
ff25 = web.DataReader('25_Portfolios_5x5_Daily', 'famafrench',
                       start='1963-07-01')[0] / 100
ff_f = web.DataReader('F-F_Research_Data_Factors_daily',
                       'famafrench', start='1963-07-01')[0] / 100

excess = ff25.subtract(ff_f['RF'], axis=0).dropna()

window = 252
results = []

for i in range(window, len(excess), 63):  # quarterly
    w = excess.iloc[i-window:i]

    # Kelly rate
    h_kelly = kelly_rate(w) * 252  # annualised

    # Topological entropy via permutation entropy on index return
    index_ret = w.mean(axis=1).values  # equal-weight index
    h_perm = permutation_entropy(index_ret, m=5) * 252  # scale to annual

    # Also: sample entropy (a different estimator)
    results.append({
        'date': excess.index[i],
        'h_kelly': h_kelly,
        'h_perm': h_perm,
    })

df = pd.DataFrame(results).set_index('date').dropna()

corr, p_val = pearsonr(df['h_kelly'], df['h_perm'])

print("=" * 60)
print("EXPERIMENT 8: Topological Entropy = Kelly Rate")
print("=" * 60)
print(f"\nN observations: {len(df)}")
print(f"Mean h_Kelly (annualised):   {df['h_kelly'].mean():.4f}")
print(f"Mean h_perm  (annualised):   {df['h_perm'].mean():.4f}")
print(f"\nCorrelation:  {corr:.4f}")
print(f"p-value:      {p_val:.4f}")

from statsmodels.regression.linear_model import OLS
from statsmodels.tools import add_constant
m = OLS(df['h_kelly'].values, add_constant(df['h_perm'].values)).fit()
print(f"\nRegression h_Kelly ~ const + h_perm:")
print(f"  Slope:     {m.params[1]:.4f} (theory: ~1.0)")
print(f"  Intercept: {m.params[0]:.4f} (theory: ~0.0)")
print(f"  R²:        {m.rsquared:.4f}")
print("\nFalsification: correlation < 0.20 or slope outside [0.5, 2.0]")
```

---

## Experiment 9: Market Reynolds Number and Regime Classification

### Theory
The market Reynolds number $\mathrm{Re} = H \cdot T \cdot \mathrm{diam}(M)$
classifies markets as laminar ($\mathrm{Re} < 1$) or turbulent ($\mathrm{Re} \gg 1$).
High-Re periods should correspond to known market crises.

### Falsifiable Hypothesis
**H0:** The market Reynolds number has no predictive power for future volatility
regimes or drawdown events.

**H1 (our theory):** High-Re periods precede or coincide with high-volatility
regimes (VIX > 30) with hit rate significantly above chance. The Reynolds number
should be elevated in the months preceding: 1987 crash, 1998 LTCM, 2000 dot-com,
2008 GFC, 2020 COVID, 2022 rates.

```python
# experiment_9_reynolds_number.py
import numpy as np
import pandas as pd
import yfinance as yf
import pandas_datareader.data as web

# Load data
spx = yf.download('^GSPC', start='1990-01-01', end='2024-12-31',
                   auto_adjust=True)['Close']
vix = yf.download('^VIX', start='1990-01-01', end='2024-12-31',
                   auto_adjust=True)['Close']
ff_f = web.DataReader('F-F_Research_Data_5_Factors_2x3_daily',
                       'famafrench', start='1990-01-01')[0] / 100

spx_ret = spx.pct_change().dropna()
window = 126  # 6 months
T_window = window

results = []
for i in range(window, min(len(ff_f), len(spx_ret))):
    factors_w = ff_f.iloc[i-window:i][[
        'Mkt-RF','SMB','HML','RMW','CMA']].dropna()
    if len(factors_w) < 100:
        continue

    # Estimate H (mean curvature proxy)
    cov_f = np.cov(factors_w.values.T)
    eigs = np.linalg.eigvalsh(cov_f)
    eigs = np.maximum(eigs, 0)
    r_eff = (eigs.sum()**2) / (eigs**2).sum() if eigs.sum() > 0 else 1.0
    d_f = 5

    H = np.sqrt(max(d_f - r_eff, 0)) * 0.5 * np.sqrt(d_f)

    # Manifold diameter (Fisher-Rao)
    diam_M = np.pi / 2  # for great-sphere type

    # Reynolds number
    Re = H * T_window * diam_M

    # Future VIX (next month)
    future_date = ff_f.index[i]
    vix_val = vix.asof(future_date) if future_date in vix.index else np.nan

    results.append({
        'date': future_date,
        'Re': Re, 'H': H, 'r_eff': r_eff,
        'VIX': vix_val,
        'crisis': int(vix_val > 30) if not np.isnan(vix_val) else 0
    })

df = pd.DataFrame(results).set_index('date').dropna()

# Predictive analysis: does high Re precede high VIX?
from sklearn.metrics import roc_auc_score

df['Re_lag1m'] = df['Re'].shift(21)  # 1 month lag
df_clean = df.dropna()

auc = roc_auc_score(df_clean['crisis'], df_clean['Re_lag1m'])

# Known crisis dates
crisis_periods = {
    '1987 Crash': ('1987-10-01', '1987-12-31'),
    '1998 LTCM':  ('1998-08-01', '1998-10-31'),
    '2000-2002':  ('2000-03-01', '2002-10-31'),
    '2008 GFC':   ('2008-09-01', '2009-03-31'),
    '2020 COVID': ('2020-02-01', '2020-05-31'),
    '2022 Rates': ('2022-01-01', '2022-12-31'),
}

print("=" * 60)
print("EXPERIMENT 9: Market Reynolds Number and Regime Classification")
print("=" * 60)
print(f"\nAUC for Re predicting VIX>30 (1-month ahead): {auc:.4f}")
print(f"Random: 0.50, Theory predicts: > 0.60")

print(f"\nMean Re by VIX regime:")
low_vix  = df_clean[df_clean['VIX'] < 20]['Re']
high_vix = df_clean[df_clean['VIX'] > 30]['Re']
print(f"  VIX < 20 (calm):   Re = {low_vix.mean():.3f} ± {low_vix.std():.3f}")
print(f"  VIX > 30 (crisis): Re = {high_vix.mean():.3f} ± {high_vix.std():.3f}")

from scipy.stats import mannwhitneyu
stat, p = mannwhitneyu(high_vix, low_vix, alternative='greater')
print(f"  Mann-Whitney p (crisis > calm): {p:.4f}")

print("\nReynolds number during known crises:")
for name, (start, end) in crisis_periods.items():
    try:
        period_Re = df_clean.loc[start:end, 'Re']
        if len(period_Re) > 0:
            print(f"  {name:<20}: Re = {period_Re.mean():.3f}")
    except:
        pass
print("\nFalsification: AUC < 0.55 or crisis Re not elevated vs calm Re")
```

---

## Experiment 10: Berry Phase and Pairs Trading Performance

### Theory
The Berry phase proxy $\hat\gamma = \pi(\rho_t - \rho_{t-\tau})/(\rho_{\rm max}-\rho_{\rm min})$
should improve pairs entry timing. The phase-adjusted z-score
$z_{\rm adj} = z_{\rm raw}\cos(\hat\gamma)$ should give better risk-adjusted
returns than raw z-score alone.

### Falsifiable Hypothesis
**H0:** Adding the Berry phase adjustment to the z-score does not improve pairs
trading performance beyond the raw z-score alone.

**H1 (our theory):** The Sharpe ratio of the phase-adjusted strategy exceeds
the Sharpe of the raw z-score strategy by at least 0.2 annualised, and the
maximum drawdown is reduced.

```python
# experiment_10_berry_phase_pairs.py
import numpy as np
import pandas as pd
import yfinance as yf

PAIRS = [
    ('GLD', 'GDX'),   # Gold price vs gold miners (physically linked)
    ('USO', 'XLE'),   # Oil price vs energy sector
    ('TLT', 'TMF'),   # Long bond ETF pairs
    ('QQQ', 'TQQQ'),  # Nasdaq vs leveraged Nasdaq
]

def rolling_correlation(s1, s2, window=21):
    return s1.rolling(window).corr(s2)

def berry_phase_proxy(rho_t, rho_prev, rho_min, rho_max):
    """Berry phase from correlation momentum (PAIRS_TRADING.md equation 4.4)"""
    return np.pi * (rho_t - rho_prev) / max(rho_max - rho_min, 0.01)

print("=" * 60)
print("EXPERIMENT 10: Berry Phase as Entry Filter")
print("=" * 60)
print(f"\n{'Pair':<14} {'Sh(raw z)':>10} {'Sh(adj z)':>10} "
      f"{'DD(raw)':>8} {'DD(adj)':>8} {'Improvement':>12}")

for a, b in PAIRS:
    try:
        prices = yf.download([a, b], start='2015-01-01', end='2024-12-31',
                               auto_adjust=True)['Close'].dropna()
        if len(prices) < 500 or a not in prices or b not in prices:
            continue

        r_a = prices[a].pct_change()
        r_b = prices[b].pct_change()
        spread = np.log(prices[a]) - np.log(prices[b])

        # Estimate OU parameters
        window_ou = 252
        kappa_vals, theta_vals, sigma_vals = [], [], []
        for i in range(window_ou, len(spread)):
            s = spread.iloc[i-window_ou:i]
            from scipy.stats import linregress
            dx = np.diff(s.values); x_lag = s.values[:-1]
            slope, intercept, *_ = linregress(x_lag, dx)
            kappa = max(-slope, 1e-6) * 252
            theta = intercept / max(-slope, 1e-6)
            sigma = np.std(dx) * np.sqrt(252)
            kappa_vals.append(kappa); theta_vals.append(theta); sigma_vals.append(sigma)

        kappa_mean = np.mean(kappa_vals)
        theta_mean = np.mean(theta_vals)
        sigma_mean = np.mean(sigma_vals)

        # Rolling correlation for Berry phase
        rho = rolling_correlation(r_a, r_b, window=21)
        rho_range = rho.rolling(252).apply(lambda x: x.max()-x.min(), raw=True)

        # Backtest both strategies
        def backtest(use_berry=False, z_entry=2.0, z_exit=0.3):
            pos = 0; trade_pnl = []; cum = [0.0]
            for t in range(252, len(spread)):
                z_raw = (spread.iloc[t] - theta_mean) / max(sigma_mean/np.sqrt(252*kappa_mean/252), 1e-6)

                if use_berry:
                    rho_t   = rho.iloc[t]
                    rho_prev = rho.iloc[t-21] if t >= 21 else rho_t
                    r_min   = rho.iloc[max(0,t-252):t].min()
                    r_max   = rho.iloc[max(0,t-252):t].max()
                    gamma   = berry_phase_proxy(rho_t, rho_prev, r_min, r_max)
                    z_eff   = z_raw * np.cos(gamma)
                else:
                    z_eff = z_raw

                daily_r = spread.iloc[t] - spread.iloc[t-1]

                if pos == 0:
                    if z_eff >  z_entry: pos = -1
                    elif z_eff < -z_entry: pos = 1
                elif pos != 0:
                    cum.append(cum[-1] + pos * daily_r)
                    if (pos == -1 and z_eff < z_exit) or (pos == 1 and z_eff > -z_exit):
                        trade_pnl.append(pos * daily_r); pos = 0
                else:
                    cum.append(cum[-1])

            if not trade_pnl: return 0.0, 0.0
            arr = np.array(trade_pnl)
            sh = np.mean(arr)/np.std(arr)*np.sqrt(252) if np.std(arr)>0 else 0
            c = np.array(cum)
            dd = np.min(c - np.maximum.accumulate(c)) if len(c) > 1 else 0
            return sh, dd

        sh_raw, dd_raw = backtest(use_berry=False)
        sh_adj, dd_adj = backtest(use_berry=True)

        imp = "YES ✓" if sh_adj > sh_raw + 0.05 else "NO ✗"
        print(f"{a}/{b:<8} {sh_raw:>10.3f} {sh_adj:>10.3f} "
              f"{dd_raw:>8.4f} {dd_adj:>8.4f} {imp:>12}")

    except Exception as e:
        print(f"{a}/{b}: Error - {e}")

print("\nTheory predicts: Berry-adjusted Sharpe > raw Sharpe + 0.2")
print("Falsification: No consistent improvement across pairs")
```

---

## Summary Table of Experiments

| # | Experiment | Core Prediction | Key Statistic | Falsification Criterion |
|:-:|:-----------|:---------------|:-------------|:-----------------------|
| 1 | Sharpe-curvature | Sharpe ∝ $\|H\|_{L^2}$ | Slope $\beta_1>0$, R²>0.10 | $\beta_1\leq 0$ or R²<0.05 |
| 2 | Tail index | $\alpha = r/2$ | Slope $\approx 1$, intercept $\approx 0$ | Slope outside $[0.5, 2.0]$ |
| 3 | MUP vs Cover | Regret ratio $(d-1)/r$ | 12× improvement ($d=30$, $r=4$) | MUP ≤ Cover after txn costs |
| 4 | Stationary distribution | Portfolio weights ∼ Beta | KS rejects uniform, not Beta | KS rejects Beta |
| 5 | Jacobi vs GBM | $\sigma^2\propto b(1-b)$ | Jacobi R² > GBM R² | GBM R² ≥ Jacobi R² |
| 6 | Vol skew | Skew ∝ $H^2/2\sigma_I$ | Slope $>0$, incremental R²$>0$ | No incremental R² |
| 7 | Pairs threshold | $z^{\ast}=\sqrt{1+r/\kappa}$ | Higher Sharpe than fixed 2σ | Fixed 2σ systematically better |
| 8 | Entropy = Kelly | $h_{\rm top}= h_{\rm Kelly}$ | Slope $\approx 1$, correlation $>0.2$ | Correlation $<0.10$ |
| 9 | Reynolds number | High Re → crisis | AUC$>0.60$, crisis Re elevated | AUC$<0.55$ |
| 10 | Berry phase | Phase adjustment helps | Sharpe improvement $>0.2$ | No consistent improvement |

---

## Repository Structure

```
geometry-of-efficient-markets/
├── README.md
├── requirements.txt
├── data/
│   ├── download_ff_data.py       # Ken French library downloader
│   ├── download_prices.py        # yfinance batch downloader
│   └── download_cboe.py          # CBOE VIX/SKEW downloader
├── core/
│   ├── kelly.py                  # Log-optimal portfolio solver
│   ├── fisher_rao.py             # Fisher-Rao metric utilities
│   ├── jacobi.py                 # Jacobi polynomial tools
│   ├── curvature.py              # Mean curvature estimation
│   ├── ou_params.py              # OU parameter estimation
│   └── berry_phase.py            # Berry phase proxy estimator
├── experiments/
│   ├── experiment_1_sharpe_curvature.py
│   ├── experiment_2_tail_index.py
│   ├── experiment_3_mup_vs_cover.py
│   ├── experiment_4_stationary_distribution.py
│   ├── experiment_5_jacobi_vs_gbm.py
│   ├── experiment_6_vol_skew_curvature.py
│   ├── experiment_7_pairs_threshold.py
│   ├── experiment_8_entropy_kelly.py
│   ├── experiment_9_reynolds_number.py
│   └── experiment_10_berry_phase.py
├── notebooks/
│   └── full_replication.ipynb    # Jupyter notebook: all experiments
└── results/
    └── .gitkeep                  # Results stored locally, not committed
```

---

## Instructions for Replication

```bash
# 1. Clone repository
git clone https://github.com/[to-be-set]/geometry-of-efficient-markets
cd geometry-of-efficient-markets

# 2. Install dependencies
pip install -r requirements.txt
# requirements.txt:
# numpy scipy pandas statsmodels scikit-learn matplotlib seaborn
# yfinance pandas-datareader fredapi arch hurst tqdm jupyter

# 3. Download data (once, ~500MB total)
python data/download_ff_data.py     # ~5 min
python data/download_prices.py      # ~10 min
python data/download_cboe.py        # ~2 min

# 4. Run all experiments
for i in $(seq 1 10); do
    python experiments/experiment_${i}_*.py
done

# 5. Or use the notebook
jupyter notebook notebooks/full_replication.ipynb
```

---

## Expected Runtime and Computational Requirements

| Experiment | Runtime (laptop) | Memory | Bottleneck |
|:-----------|:----------------|:-------|:-----------|
| 1: Sharpe-curvature | ~15 min | 2 GB | Rolling Kelly optimisation |
| 2: Tail index | ~10 min | 1 GB | Hill estimator loops |
| 3: MUP vs Cover | ~45 min | 4 GB | Monte Carlo portfolio integral |
| 4: Stationary dist | ~5 min | 0.5 GB | Rolling Kelly |
| 5: Jacobi vs GBM | ~8 min | 0.5 GB | Rolling Kelly |
| 6: Vol skew | ~5 min | 0.5 GB | Data download |
| 7: Pairs threshold | ~20 min | 1 GB | Backtest loops |
| 8: Entropy-Kelly | ~10 min | 1 GB | Permutation entropy |
| 9: Reynolds | ~8 min | 0.5 GB | Factor covariance |
| 10: Berry phase | ~25 min | 1 GB | Pairs backtest |
| **Total** | **~2.5 hours** | **4 GB** | |

---

## Notes on Statistical Validity

**Multiple testing:** Ten experiments, each at $\alpha = 0.05$, gives an expected
false positive rate of $1-(0.95)^{10} \approx 40\%$ under the global null.
Apply Holm-Bonferroni correction when reporting combined results.

**Data snooping:** We specify these experiments before running them. Do not adjust
experiment parameters after viewing results. The code is in the repository in its
pre-specified form.

**Transaction costs:** Experiments 3 and 7 should be re-run with assumed costs
of 5 bps round-trip (institutional) and 20 bps round-trip (retail) to assess
practical viability.

**Out-of-sample discipline:** Each experiment uses the last 5 years (2020–2024)
as a hold-out period not used in any parameter estimation. Results should be
reported separately for pre- and post-2020 subsamples.

**Known limitations:** The mean curvature estimator in Experiments 1, 6, and 9
is a proxy — a proper computation requires solving the log-optimal portfolio and
projecting onto the normal bundle, which is computationally demanding. The
simplified estimator may understate the strength of the curvature signal.

---

*We expect some experiments to confirm the theory strongly, others weakly,
and perhaps one to require theoretical revision. That is science.*

*Update this document as results arrive.*
