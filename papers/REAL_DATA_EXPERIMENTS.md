# Empirical Geometry: Testing the Theory Against Sixty Years of Market Data
## Twenty Falsifiable Tests of the Geometric Theory of Efficient Markets

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VIII.1** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
We specify twenty precise empirical tests of the geometric theory of efficient
markets, organised from most to least central. Each test uses freely available
data (Fama-French, FRED, CBOE, yfinance), can be run on a laptop in under one
hour, and has a specific falsification criterion stated in advance. The theory
claims that a financial market is a minimal submanifold $M^r$ of the
Bhattacharyya sphere $S^{d-1}_{+}$, that portfolio weights are barycentric
coordinates on $\Delta_{d-1}$ with the Fisher-Rao metric $g^{\rm FR}_{ij} =
\delta_{ij}/b_i$, and that every important financial quantity is a computable
geometric invariant of $M^r$. These are strong claims. They deserve strong
tests. The five most important: (1) Does the realised Sharpe ratio correlate
with estimated mean curvature $\|H\|$? (2) Is the manifold dimension $r$
stable across three independent estimation methods? (3) Does the Manifold
Universal Portfolio outperform Cover's Universal Portfolio by the predicted
factor of $(d-1)/r$? (4) Does the spectral gap $\lambda_1$ of the Fisher-Rao
Laplacian predict factor mean-reversion speed? (5) Does the Cheeger constant
$h_M$ drop before financial crises? For each test we state: the falsifiable
hypothesis, the exact dataset, the exact computation, the expected result from
the theory, and the specific observation that would kill the claim. We adopt
a scoring system: if fewer than 10 of 20 tests pass, the theory needs major
revision; if fewer than 5 pass, it is wrong.

- **Twenty tests, each with a falsification criterion stated in advance**
- **All data freely available; all code open-source; all experiments run in under one hour**
- **Tests 1-5 (core theory) weighted 2x in the scoring system**
- **Honest accounting: we specify exactly what would kill the theory**

**Keywords.** Empirical validation; falsification; market manifold; Fisher-Rao
geometry; mean curvature; Sharpe ratio; manifold dimension; universal portfolio;
spectral gap; Cheeger constant; Dyson class; fat tails; crisis prediction.

**MSC 2020.** 91G10, 62P05, 53B25, 62M10, 60G46.

---

## 1. Philosophy

### 1.1 Why this paper exists

A theory that cannot be killed by data is not a theory. It is theology.

The preceding papers of this monograph develop a mathematical framework of
considerable scope: the market is a manifold, the Sharpe ratio is mean
curvature, fat tails arise from geometry, the Kelly rate equals topological
entropy, the Dyson symmetry class is forced by manifold topology. These are
beautiful claims. Beauty is not evidence.

This paper exists to make the theory vulnerable. Each of the twenty tests below
is designed to *falsify*, not to confirm. We state in advance what we expect,
and we state in advance what would make us abandon each claim. We do not
engage in post-hoc rationalisation. If the data disagrees with a prediction
consistently across multiple datasets and time periods, the theory needs
revision. If the data disagrees with the five core predictions, the theory is
wrong.

### 1.2 The standard

We adopt the following scoring system:

| Score (out of 30) | Interpretation |
|:-------------------|:---------------|
| 22.5+ | **Strong support.** The geometric framework captures something real about markets. |
| 15-22 | **Supported.** Most claims hold; some need refinement. |
| 7.5-14.5 | **Major revision needed.** The framework has some validity but significant claims fail. |
| < 7.5 | **Wrong.** The axioms need to be revisited from scratch. |

The scoring: Tests 1-5 (core theory) are weighted 2 points each; Tests 6-20
are weighted 1 point each. Each test scores full points (pass), half points
(marginal), or zero (fail). Maximum possible score: $5 \times 2 + 15 \times 1
= 25$, but we round up to 30 to allow for partial credit on the weighted tests.
More precisely: maximum $= 5(2) + 15(1) = 25$ points. The thresholds are
calibrated to this maximum.

### 1.3 What "pass" and "fail" mean

Every test specifies a **primary statistic** and a **falsification criterion**.
"Pass" means the primary statistic falls in the range predicted by the theory.
"Marginal" means it falls outside the predicted range but in the right direction
(e.g. the correlation is positive but below the threshold). "Fail" means it
falls in the falsification region (wrong sign, wrong order of magnitude, or
statistically insignificant in the wrong direction).

### 1.4 Reproducibility commitment

All code is available at `github.com/saxonnicholls/geometry-of-efficient-markets/code/experiments/`.
Python 3.10+. Random seeds fixed. Each experiment outputs: test statistic,
p-value where applicable, pass/marginal/fail verdict, and a diagnostic plot.
The total run time for all twenty experiments on a standard laptop (Apple M2,
16GB RAM) is under four hours.

---

## 2. Data Sources

All experiments draw from the following freely available datasets:

| Dataset | Source | Access | Period |
|:--------|:-------|:-------|:-------|
| Fama-French 25 portfolios (size $\times$ value) | Kenneth French Data Library | Free download | Daily, 1963-present |
| Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA) | Kenneth French Data Library | Free download | Daily, 1963-present |
| S&P 500 constituent returns | `yfinance` | `pip install yfinance` | Daily, 1990-present |
| Sector ETFs (XLK, XLF, XLE, XLV, ...) | `yfinance` | `pip install yfinance` | Daily, 1999-present |
| FRED macroeconomic series | Federal Reserve | Free API key | Various, 1950-present |
| CBOE VIX, SKEW, VVIX | CBOE | Free download | Daily, 1990-present |
| Options chains | `yfinance` | `pip install yfinance` | Near-term, current |
| Cryptocurrency prices | `yfinance` | `pip install yfinance` | Daily, 2014-present |
| UK horse racing starting prices | Betfair historical data | Free registration | 2010-present |
| Artnet auction indices | Artnet.com | Free summary data | Annual, 1985-present |
| Sovereign yield spreads | FRED (10y yields by country) | Free API | Daily, 1999-present |
| Intergenerational elasticity | Corak (2013) dataset | Published in paper | Cross-section, 22 countries |

**Standard Python environment:**
```
pip install numpy scipy pandas statsmodels scikit-learn yfinance fredapi
pip install matplotlib seaborn tqdm arch hurst pot
```

All experiments use the same random seed (`np.random.seed(42)`) and the same
rolling window conventions unless stated otherwise. Daily returns are computed
as $r_t = \log(P_t / P_{t-1})$ throughout.

---

## 3. Test Battery: Core Theory (Tests 1-5)

These five tests target the foundational claims of the monograph. If all five
fail, the theory is wrong regardless of what happens in Tests 6-20. Each is
weighted 2 points.

---

### Test 1: The Sharpe-Curvature Identity

**Theoretical claim.** $\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(M, g_M)}$ (R1 in
WHATS_NEW.md). The maximum attainable Sharpe ratio from any strategy on the
market manifold equals the $L^2$-norm of the mean curvature vector $H$ of
$M^r$ in $S^{d-1}_{+}$.

**Falsifiable hypothesis.** In a cross-sectional regression of realised Sharpe
ratios on estimated mean curvature norms, the slope $\beta_1 > 0$ with
$p < 0.05$.

**Dataset.** Fama-French 25 portfolios (size $\times$ value), daily returns,
1963-2024. Rolling 252-day (1-year) windows, stepped monthly.

**Computation.**

1. In each rolling window of $T = 252$ daily returns for $d = 25$ portfolios:
   (a) Compute the sample mean excess return vector $\hat{\mu}$ and sample
   covariance $\hat{\Sigma}$.
   (b) Solve the Kelly problem: $b^* = \arg\max_b \hat{\mu}^T b -
   \tfrac{1}{2} b^T \hat{\Sigma} b$ subject to $b \in \Delta_{d-1}$.
   (c) Perform PCA on $\hat{\Sigma}$; retain $r$ factors explaining 90% of
   variance.
   (d) Project the vector $\eta_i = 1/(2\sqrt{b^{\ast}_{i}})$ onto the normal space
   of the $r$-factor subspace. The norm of this projection estimates $\|H\|$.
   (e) Compute the realised Sharpe ratio of the $b^{\ast}$ portfolio over the
   next 63 trading days (one quarter, out-of-sample).

2. Collect all $(H_{\rm est}, \mathrm{Sharpe}_{\rm realised})$ pairs across
   all rolling windows.

3. Run OLS: $\mathrm{Sharpe}_{\rm realised} = \beta_0 + \beta_1 H_{\rm est}
   + \varepsilon$.

**Expected from theory.** $\beta_1 \approx 1.0$ (the identity is an equality,
not merely a correlation). $R^2 > 0.15$. The identity is exact on the
population manifold; estimation noise in $\hat{\Sigma}$ and finite-sample
effects will degrade it, but the signal should survive.

**Falsification criterion.** $\beta_1 \leq 0$ (wrong sign), or $\beta_1 > 0$
but $p > 0.10$ (insignificant), or $R^2 < 0.05$ (no explanatory power). Any
of these outcomes would indicate that the Sharpe-curvature identity does not
hold empirically, and the central theorem of the monograph collapses.

**What a marginal result looks like.** $\beta_1 > 0$, $p < 0.05$, but
$R^2 \in [0.05, 0.15]$. This would suggest the identity holds directionally
but with more noise than the theory predicts, pointing to estimation error
in the curvature rather than a failure of the theorem itself.

---

### Test 2: Manifold Dimension Stability

**Theoretical claim.** The market manifold $M^r$ has a well-defined, stable
intrinsic dimension $r$ that equals the number of systematic factors. Three
independent estimators should agree.

**Falsifiable hypothesis.** Three independent estimators of $r$ agree within
$\pm 1$ in more than 70% of rolling windows.

**Dataset.** S&P 500 daily returns, top 100 stocks by market capitalisation at
each rebalancing date, rolling 504-day (2-year) windows stepped quarterly,
2000-2024.

**Computation.** In each rolling window:

1. **Stable rank.** Compute the Fisher information matrix
   $\hat{I}_{ij} = \hat{\Sigma}_{ij} / (b^{\ast}_{i} b^{\ast}_{j})$ where $b^{\ast}$ is the
   equal-weight portfolio (as a neutral reference). The stable rank is
   $\mathrm{sr}(\hat{I}) = \mathrm{tr}(\hat{I}) / \|\hat{I}\|_{\rm op}$.
   Set $r_1 = \lfloor \mathrm{sr}(\hat{I}) \rceil$.

2. **Variance ratio.** Eigendecompose $\hat{\Sigma}$. Set $r_2$ = number of
   eigenvalues needed to explain 90% of total variance.

3. **Marchenko-Pastur edge.** Under the null of no factor structure, the
   largest eigenvalue of $\hat{\Sigma}$ (after standardisation) should not
   exceed $(1 + \sqrt{d/T})^2$. Set $r_3$ = number of eigenvalues exceeding
   this threshold.

4. Record the triple $(r_1, r_2, r_3)$. Agreement = $\max(r_1, r_2, r_3)
   - \min(r_1, r_2, r_3) \leq 1$.

**Expected from theory.** $r \approx 4$-$6$ for US equities. The three
estimators agree within $\pm 1$ in $> 70\%$ of windows. The coefficient of
variation of $r$ across time (excluding crisis periods) is $< 0.3$.

**Falsification criterion.** The three estimators consistently disagree by
$\geq 3$ (agreement rate $< 50\%$), or the time series of $r$ has coefficient
of variation $> 0.5$ (excluding crisis quarters). Either outcome would suggest
the market does not have a stable factor structure, undermining the manifold
assumption.

---

### Test 3: MUP vs Cover Regret Ratio

**Theoretical claim.** The Manifold Universal Portfolio (MUP) achieves regret
$r \log T / (2T)$ versus Cover's Universal Portfolio regret of
$(d-1) \log T / (2T)$, an improvement factor of $(d-1)/r$ (R2 in WHATS_NEW.md).

**Falsifiable hypothesis.** The ratio of Cover's cumulative regret to MUP's
cumulative regret converges to approximately $(d-1)/r$ as $T$ grows.

**Dataset.** Fama-French 25 portfolios ($d = 25$), daily returns, 1963-2024.

**Computation.**

1. Estimate $r$ from PCA (90% variance explained) over the first 504 days.
   Expected: $r \approx 4$.

2. Implement the MUP: integrate the Kelly-optimal portfolio over the
   $r$-dimensional factor subspace using Monte Carlo with $N = 10{,}000$
   samples from the Dirichlet prior restricted to $M^r$.

3. Implement Cover's Universal Portfolio: integrate over the full
   $(d-1)$-dimensional simplex using the same Monte Carlo approach with
   $N = 100{,}000$ samples.

4. For both, compute cumulative log-wealth $L_T = \sum_{t=1}^T \log\langle
   b_t, x_t \rangle$ where $x_t$ is the vector of gross returns.

5. Compute the cumulative regret of each: $R_T = L_T(b^*_{\rm hindsight})
   - L_T$. Form the ratio $R_T^{\rm Cover} / R_T^{\rm MUP}$.

**Expected from theory.** The regret ratio should approach $(d-1)/r =
24/4 = 6.0$ for $r = 4$. In practice, with estimation error and finite $T$,
we expect the ratio in the range $[3, 10]$.

**Falsification criterion.** MUP does not outperform Cover (ratio $< 1$), or
the ratio is $< 2$ (improvement is negligible) or $> 15$ (the theory
overestimates the improvement, suggesting something else is driving it). If
the ratio is $< 1$, the entire dimension-reduction argument fails.

---

### Test 4: Spectral Gap Predicts Mean-Reversion Speed

**Theoretical claim.** The first non-zero eigenvalue $\lambda_1$ of the
Laplacian on $(M^r, g_M)$ determines the mixing time of the market process,
and hence the half-life of factor return autocorrelation. Specifically,
$t_{1/2} = \log 2 / \lambda_1$.

**Falsifiable hypothesis.** The rank correlation between the estimated spectral
gap and the observed mean-reversion half-life exceeds 0.5 across different
factors and time periods.

**Dataset.** Fama-French 5 factors (Mkt-RF, SMB, HML, RMW, CMA), daily
returns, 1963-2024, rolling 504-day windows.

**Computation.**

1. In each window, compute the $5 \times 5$ factor covariance matrix
   $\hat{\Sigma}_{F}$.

2. Form the Fisher-Rao metric on the factor simplex: $g^{\rm FR}_{ij} =
   \hat{\Sigma}^F_{ij} / (w_i w_j)$ where $w$ is the factor loading vector
   normalised to sum to 1.

3. Compute the eigenvalues of $g^{\rm FR}$. The spectral gap is $\lambda_1$
   = smallest positive eigenvalue.

4. For each factor, estimate the AR(1) coefficient $\phi_1$ from daily returns.
   Half-life $= -\log 2 / \log |\phi_1|$.

5. Across the 5 factors in each window, compute the Spearman rank correlation
   between $\{\lambda_1^{(k)}\}$ and $\{t_{1/2}^{(k)}\}$ for $k = 1,\ldots,5$.

6. Average the rank correlations across all rolling windows.

**Expected from theory.** Rank correlation $> 0.5$. Factors with larger
spectral gaps should mean-revert faster. The theory predicts an *inverse*
relationship: larger $\lambda_1$ implies shorter half-life. So the rank
correlation between $\lambda_1$ and $t_{1/2}$ should be *negative* and exceed
$0.5$ in magnitude.

**Falsification criterion.** $|\rho_{\rm Spearman}| < 0.2$ across the
majority of rolling windows. This would indicate that the spectral gap has
no predictive power for mean-reversion timing, undermining the dynamical
content of the geometric theory.

---

### Test 5: Cheeger Constant Drops Before Crises

**Theoretical claim.** The Cheeger constant $h_M$ of the market manifold
measures the bottleneck of information flow. Before a crisis, the market
fragments into weakly connected components, and $h_M$ drops.

**Falsifiable hypothesis.** $h_M$ drops by more than 50% from its trailing
2-year mean in the 6 months preceding each of four major crises.

**Dataset.** S&P 500 sector ETFs (XLK, XLF, XLE, XLV, XLI, XLY, XLP, XLU,
XLB, XLC, XLRE — 11 sectors), daily returns, 1999-2024.

**Crises tested.** (i) Dot-com crash: peak Mar 2000, trough Oct 2002.
(ii) Global Financial Crisis: peak Oct 2007, trough Mar 2009.
(iii) Euro crisis: peak Apr 2011, trough Oct 2011.
(iv) COVID crash: peak Feb 2020, trough Mar 2020.

**Computation.**

1. In rolling 126-day (6-month) windows:
   (a) Compute the $11 \times 11$ sector correlation matrix $C$.
   (b) Threshold $C$ to form the adjacency matrix: $A_{ij} = 1$ if
   $C_{ij} > \bar{C}$ (the mean off-diagonal correlation).
   (c) Compute the Fiedler eigenvalue (second-smallest eigenvalue of the
   graph Laplacian $L = D - A$). This is the discrete Cheeger constant
   estimate: $h_M \approx \lambda_2(L) / 2$.

2. For each crisis, compare $h_M$ in the 6 months before the peak to the
   trailing 2-year mean.

3. Compute the drop ratio: $\Delta h = 1 - h_M^{\rm pre-crisis} /
   h_M^{\rm 2yr\ mean}$.

**Expected from theory.** $\Delta h > 0.5$ for all four crises (i.e., $h_M$
drops by more than half). The mechanism: before crises, sector correlations
rise, the adjacency graph becomes more connected but in a fragile way — a few
sectors become bridges, creating a bottleneck that the Fiedler eigenvalue
detects.

**Falsification criterion.** $\Delta h < 0.2$ for three or more of the four
crises. If $h_M$ does not drop meaningfully before crises, then the Cheeger
constant is not a useful crisis predictor, and the geometric interpretation
of systemic risk fails.

---

## 4. Test Battery: Classification (Tests 6-10)

These tests target the classification theorem (R3): that market structures
fall into three types — CAPM (great sphere), Clifford torus, and
pseudo-Anosov (hyperbolic) — distinguished by their Dyson symmetry class
$\beta \in \{1, 2, 4\}$.

---

### Test 6: Three Market Types Exist

**Hypothesis.** Different market sectors and asset classes exhibit
statistically distinguishable eigenvalue spacing distributions corresponding
to the three classified types.

**Dataset.** Three universes, each with daily returns 2010-2024:
(a) US large-cap (S&P 100 constituents) — expected CAPM/GOE.
(b) US equity pairs (top 20 most cointegrated pairs from S&P 500) — expected
Clifford/GUE.
(c) Cryptocurrency top 20 — expected pseudo-Anosov/GSE.

**Computation.** For each universe, in rolling 252-day windows:

1. Compute the sample covariance matrix $\hat{\Sigma}$.
2. Standardise eigenvalues: $\tilde{\lambda}_i = (\lambda_i - \bar{\lambda})
   / \mathrm{std}(\lambda)$.
3. Compute the nearest-neighbour spacing ratios: $r_i = \min(s_i, s_{i+1})
   / \max(s_i, s_{i+1})$ where $s_i = \tilde{\lambda}_{i+1} -
   \tilde{\lambda}_i$.
4. Fit the spacing ratio distribution to the Wigner surmise for $\beta = 1$
   (GOE), $\beta = 2$ (GUE), $\beta = 4$ (GSE) using maximum likelihood.
5. Select the best-fitting $\beta$ by AIC.

**Expected.** US large-cap $\to$ $\beta = 1$. Pairs $\to$ $\beta = 2$.
Crypto $\to$ $\beta = 4$. The three universes should select *different*
$\beta$ values in the majority of windows.

**Falsification.** All three universes consistently select the same $\beta$,
or none of the three Wigner surmise distributions fits any universe
($p < 0.01$ for the best fit by KS test in $> 80\%$ of windows).

---

### Test 7: Dyson Class from Eigenvalue Spacings

**Hypothesis.** The nearest-neighbour spacing distribution of Fisher matrix
eigenvalues for US equities matches the GOE Wigner surmise ($\beta = 1$).

**Dataset.** S&P 500, top 50 stocks by market cap, daily returns, rolling
504-day windows, 2000-2024.

**Computation.**

1. In each window, compute the $50 \times 50$ sample covariance matrix.
2. Extract eigenvalues. Unfold the spectrum using the Marchenko-Pastur
   distribution as the null.
3. Compute the unfolded nearest-neighbour spacings $s_i$.
4. Perform a KS test against the Wigner surmise
   $p_\beta(s) = a_\beta s^\beta \exp(-b_\beta s^2)$ for $\beta = 1, 2, 4$.
5. Report the best-fitting $\beta$ and the KS p-value.

**Expected.** $\beta = 1$ (GOE) is the best fit in $> 60\%$ of windows,
with KS $p > 0.05$.

**Falsification.** No $\beta \in \{1, 2, 4\}$ achieves KS $p > 0.05$ in
more than 40% of windows. This would mean eigenvalue spacings of real market
data do not match any of the three predicted distributions, and the Dyson
class correspondence (R21) is empirically vacuous.

---

### Test 8: Fat Tail Index $\alpha \approx r/2$

**Hypothesis.** The tail index $\alpha$ of asset return distributions is
approximately $r/2$, where $r$ is the manifold dimension (R4 in WHATS_NEW.md,
which gives the more precise formula $\alpha_i = Tb^{\ast}_{i} - 1/2$; the aggregate
prediction is $\alpha \approx r/2$).

**Dataset.** S&P 500 constituents, daily returns, 2000-2024. Estimate $r$ from
PCA; estimate $\alpha$ from tail behaviour.

**Computation.**

1. Estimate $r$ from the Marchenko-Pastur edge method (as in Test 2) over the
   full sample. Expected: $r \approx 5$.

2. For each stock, compute the Hill estimator of the tail index $\alpha$
   from the top 5% of absolute returns. Average across stocks to get
   $\bar{\alpha}$.

3. Compare $\bar{\alpha}$ to $r/2$.

**Expected.** $r \approx 5$ gives $r/2 \approx 2.5$. Empirical estimates of
$\alpha$ for US equities are typically in the range $[2.5, 4.0]$, so the
prediction is in the right ballpark. The test is whether $\bar{\alpha}$ and
$r/2$ are in the same range, and whether cross-sectional variation in
$\alpha_i$ correlates with $b^{\ast}_{i}$.

**Falsification.** $\bar{\alpha}$ and $r/2$ differ by more than a factor of
2 (i.e. $\bar{\alpha} < r/4$ or $\bar{\alpha} > r$), or the cross-sectional
rank correlation between $\alpha_i$ and $b^{\ast}_{i}$ is negative.

---

### Test 9: Jacobi Diffusion Fit

**Hypothesis.** The transition density of portfolio weight changes fits a
Jacobi diffusion better than a geometric Brownian motion.

**Dataset.** Daily rebalanced equal-weight portfolio of 10 randomly selected
S&P 500 stocks, 2010-2024. The weight of each stock drifts due to differential
returns before rebalancing.

**Computation.**

1. Track the pre-rebalancing weight $b_{i,t}$ of each stock on each day.

2. Compute the one-day weight change $\Delta b_{i,t} = b_{i,t+1} -
   b_{i,t}^{\rm post-rebalance}$ for each stock.

3. Fit two models to the conditional distribution
   $\Delta b | b_{\rm current}$:
   (a) **Jacobi:** $\Delta b \sim \mathcal{N}(\kappa(\theta - b)\Delta t,\;
   b(1-b)\sigma^2 \Delta t)$ — drift toward $\theta$, diffusion proportional
   to $b(1-b)$.
   (b) **GBM:** $\Delta b / b \sim \mathcal{N}(\mu \Delta t,\; \sigma^2
   \Delta t)$ — standard log-normal.

4. In rolling 252-day windows, perform a KS test of each model against the
   empirical $\Delta b$ distribution. Record which model has the smaller KS
   statistic.

**Expected.** Jacobi KS $<$ GBM KS in $> 70\%$ of rolling windows. The
Jacobi model captures the boundary-respecting behaviour of simplex-constrained
weights (weights cannot go below 0 or above 1), while GBM does not.

**Falsification.** GBM fits better in $> 60\%$ of windows. If the unconstrained
model fits better than the simplex-constrained model, the geometric theory's
insistence on the simplex as the natural domain is unjustified.

---

### Test 10: Stability Index of the Clifford Torus (The LTCM Test)

**Hypothesis.** Convergence/spread trading strategies cluster into
approximately 5 independent failure modes, matching the theoretical stability
index of the Clifford torus $\mathrm{ind}(T^2) = 5$ (R3 in WHATS_NEW.md).

**Dataset.** Five canonical convergence trade spreads, monthly returns,
1994-2000:
(a) On-the-run / off-the-run Treasury spread (FRED: GS10 - GS30).
(b) Swap spread (FRED: DSWP10 - GS10).
(c) Mortgage basis (FRED: MORTGAGE30US - GS30).
(d) Equity pairs: construct from largest 10 cointegrated pairs in S&P 500
using 1990-1994 in-sample.
(e) EM convergence: use FRED EM bond spread (BAMLHE00EHYIEY or similar).

**Computation.**

1. Construct the return time series for each of the 5 spread categories.

2. Compute the $5 \times 5$ correlation matrix of spread returns over
   1994-2000.

3. Eigendecompose. Count eigenvalues exceeding the Marchenko-Pastur noise
   threshold $(1 + \sqrt{5/T})^2 \cdot \bar{\lambda}$.

4. This count is the empirical stability index.

**Expected.** The number of significant eigenvalues $\approx 5$ (or more
precisely, 3-5 given the small cross-section). All spreads were hit
simultaneously during the LTCM crisis of August-September 1998, consistent
with the theoretical prediction that the Clifford torus has exactly 5
destabilising directions.

**Falsification.** Fewer than 3 or more than 8 significant eigenvalues. If
there is only 1 significant eigenvalue, it is just a common risk-on/risk-off
factor, not a structured instability. If there are 8+, the "five failure
modes" interpretation is wrong.

---

## 5. Test Battery: Applications (Tests 11-15)

These tests check whether the geometric framework yields practically useful
tools that outperform standard alternatives.

---

### Test 11: Manifold Index Fund vs Cap-Weight

**Hypothesis.** The Manifold Index Fund (MIF), which weights assets by their
Kelly-optimal weights $b^{\ast}$ restricted to $M^r$, outperforms the
capitalisation-weighted index.

**Dataset.** S&P 500 constituents, daily returns, 2000-2024. Quarterly
rebalancing.

**Computation.**

1. At each quarterly rebalancing date:
   (a) Estimate $\hat{\mu}$ and $\hat{\Sigma}$ from the trailing 504 days.
   (b) Estimate $r$ from PCA (90% variance).
   (c) Solve for $b^{\ast}$ on the $r$-dimensional factor subspace.
   (d) Construct the MIF portfolio with weights $b^{\ast}_{i}$.

2. Compute the MIF total return (with quarterly rebalancing) and the S&P 500
   total return over 2002-2024.

3. Compute annualised excess return, Sharpe ratio, and maximum drawdown for
   both.

**Expected.** MIF outperformance of 20-50 basis points per year in annualised
return. The theory predicts 47 bps for $r = 6$ and median $\|H\| = 0.15$,
but estimation noise gives a wide range. MIF Sharpe should exceed S&P 500
Sharpe by at least 0.05.

**Falsification.** MIF underperforms cap-weight over the full 22-year period.
If the geometrically-motivated weighting cannot beat the simplest possible
benchmark over two decades of data, the practical value of the theory is zero.

---

### Test 12: Geometric Pairs Entry Threshold

**Hypothesis.** The geometric entry threshold $z^*_{\rm entry} = \sqrt{1 +
r/\kappa}$ (R13 in WHATS_NEW.md) outperforms the standard $2\sigma$ rule for
pairs trading.

**Dataset.** Top 20 most cointegrated US equity pairs from the S&P 500,
identified by Engle-Granger test on 2008-2010 data, traded 2010-2024.

**Computation.**

1. For each pair, estimate the Ornstein-Uhlenbeck parameters
   $(\kappa, \sigma)$ from the spread.

2. Compute the geometric threshold: $z^{\ast} = \sigma \sqrt{1 + r/\kappa}$
   where $r$ is estimated from the pair's sector PCA dimension.

3. Backtest both strategies with the same exit rule (mean-reversion to zero):
   (a) **Standard:** Enter when spread $> 2\sigma$, exit at 0.
   (b) **Geometric:** Enter when spread $> z^{\ast}$, exit at 0.

4. For both, compute annualised Sharpe ratio, win rate, and profit factor.

**Expected.** Geometric threshold Sharpe exceeds $2\sigma$ Sharpe by at least
0.1. The geometric threshold will generally be *wider* than $2\sigma$
(entering less frequently but on higher-quality signals) when $r/\kappa > 3$.

**Falsification.** The $2\sigma$ rule outperforms the geometric rule in Sharpe
ratio across the majority of pairs ($> 60\%$). If a crude fixed threshold
beats the theory-derived threshold, the Hamiltonian free boundary analysis
does not add value.

---

### Test 13: Cheeger vs VIX for Crisis Prediction

**Hypothesis.** The Cheeger constant $h_M$ is a better crisis predictor than
the VIX.

**Dataset.** S&P 500 sector ETFs + VIX daily, 1999-2024.

**Computation.**

1. Define "crisis" as the S&P 500 experiencing a drawdown $> 10\%$ from a
   rolling 63-day high within the next 63 days (one quarter).

2. Construct two predictors:
   (a) **$h_M$:** Fiedler eigenvalue of the sector correlation graph (as in
   Test 5), lagged 63 days. Low $h_M$ predicts crisis.
   (b) **VIX:** Daily VIX close, lagged 63 days. High VIX predicts crisis.

3. Compute the ROC curve and AUC for each predictor.

**Expected.** $h_M$ AUC $>$ VIX AUC. The theory predicts that $h_M$ captures
structural fragility (graph connectivity) while VIX captures sentiment (implied
volatility). Structural fragility should be more persistent and predictive.

**Falsification.** VIX AUC exceeds $h_M$ AUC by more than 0.05. If a
model-free implied volatility index outperforms the geometrically-motivated
Cheeger constant, the additional complexity of the geometric approach is not
justified for this application. (Note: a marginal result where both are
similar suggests combining them, which is still useful.)

---

### Test 14: Kelly-Shapley Attribution

**Hypothesis.** The Shapley value $\phi_i = b^{\ast}_{i} (\mu_i - \bar{\mu})$
(R25 in WHATS_NEW.md) provides a meaningful decomposition of portfolio
performance that agrees with standard Brinson attribution on sign.

**Dataset.** Fama-French 25 portfolios, monthly returns, 1963-2024.

**Computation.**

1. Each month:
   (a) Compute the Kelly-optimal portfolio $b^{\ast}$ from the trailing 60 months.
   (b) Compute Shapley values: $\phi_i = b^{\ast}_{i} (\mu_i - \bar{\mu})$ where
   $\mu_i$ is the next month's realised return and $\bar{\mu} = \sum_j
   b^*_j \mu_j$.
   (c) Compute Brinson attribution: allocation effect + selection effect for
   each of the 25 portfolios relative to the equal-weight benchmark.

2. Across all months, compute:
   (a) The sign agreement rate: fraction of $(\phi_i, \mathrm{Brinson}_{i})$
   pairs where both have the same sign.
   (b) The variance of each attribution method across months (lower variance
   = more stable).

**Expected.** Sign agreement $> 80\%$. Shapley variance $<$ Brinson variance
(Shapley is more stable because it is axiomatically derived). The total
Shapley attribution sums to the portfolio excess return exactly (by
construction), which Brinson does not guarantee when interaction effects are
present.

**Falsification.** Sign agreement $< 60\%$. If the geometric attribution
disagrees with the standard method on the *sign* of each portfolio's
contribution more than 40% of the time, the Shapley formula is not capturing
the same economic content.

---

### Test 15: LZ Complexity Rate Tracks Kelly Growth Rate

**Hypothesis.** The LZ78 compression rate of the Voronoi symbolic sequence
of returns converges to $h_{\rm Kelly}$ (the connection between R14 and R15
in WHATS_NEW.md).

**Dataset.** S&P 500 daily returns, 1990-2024.

**Computation.**

1. **Discretise returns into symbols:** Apply $k$-means clustering ($k = 8$)
   to the daily return vector $r_t \in \mathbb{R}^{d}$. Assign each day a
   symbol $s_t \in \{0, 1, \ldots, 7\}$.

2. **LZ78 complexity rate:** Run LZ78 compression on the symbol sequence
   $s_1 s_2 \cdots s_T$. The complexity rate is
   $c_{\rm LZ} = n_{\rm phrases} \cdot \log(n_{\rm phrases}) / T$ where
   $n_{\rm phrases}$ is the number of distinct phrases in the LZ78 dictionary.

3. **Kelly growth rate:** Compute the log-optimal portfolio growth rate
   $h_{\rm Kelly} = T^{-1} \sum_t \log\langle b^{\ast}_{t}, x_t \rangle$ where
   $b^{\ast}_{t}$ is the sequentially-estimated Kelly portfolio.

4. Compute both quantities in rolling 504-day windows. Compute the Pearson
   correlation between $c_{\rm LZ}$ and $h_{\rm Kelly}$ across windows.

**Expected.** Correlation $> 0.7$. The theory predicts that the LZ complexity
rate and the Kelly growth rate are asymptotically equal (both equal the
topological entropy of the market manifold). Finite-sample and discretisation
effects will reduce the correlation, but a strong positive relationship should
be visible.

**Falsification.** Correlation $< 0.3$. If the compression rate of the
symbolic sequence is essentially unrelated to the growth rate of the
log-optimal portfolio, the filtration-entropy correspondence (the bridge
between information theory and portfolio theory) does not hold empirically.

---

## 6. Test Battery: Extensions (Tests 16-20)

These tests push the geometric framework beyond its core domain of equity
markets. They are the most speculative and the most interesting.

---

### Test 16: Favourite-Longshot Bias as Mean Curvature

**Hypothesis.** The magnitude of the favourite-longshot bias (FLB) in betting
markets correlates with the estimated mean curvature $\|H\|$ of the implied
probability manifold.

**Dataset.** UK horse racing Betfair Starting Prices, 2010-2024. Each race
provides a vector of implied probabilities $p_i = 1/\mathrm{odds}_{i}$
(normalised to sum to 1 after removing the overround).

**Computation.**

1. For each race with $d$ runners:
   (a) Compute implied probabilities $p_i$ from SP odds (normalised).
   (b) Compute $\sqrt{p_i}$ — the Bhattacharyya embedding.
   (c) Estimate $\|H\|$ as the deviation of $\sqrt{p}$ from the nearest
   great-circle arc on $S^{d-1}_{+}$, measured in the round metric.
   (d) Compute the FLB magnitude: the slope $\gamma$ in the regression
   $\mathrm{actual\ win\ rate}_{i} = \alpha + \gamma \cdot p_i + \varepsilon_i$
   across all runners in all races with the same field size $d$.
   An FLB means $\gamma < 1$ (favourites win more often than implied;
   longshots less).

2. Across different field sizes $d \in \{5, 8, 10, 12, 15, 20\}$, compute
   the correlation between mean $\|H\|$ and $(1 - \gamma)$.

**Expected.** Positive correlation. Larger fields have higher curvature (more
complex probability manifold) and stronger FLB. The theory predicts that the
overround (bookmaker's edge) is proportional to $\|H\|^2$ (the Willmore
energy).

**Falsification.** No correlation or negative correlation between $\|H\|$ and
FLB magnitude across field sizes.

---

### Test 17: Art Market Spectral Gap

**Hypothesis.** The spectral gap $\lambda_1$ of the art market is at least an
order of magnitude smaller than that of equity markets, reflecting dramatically
slower information propagation.

**Dataset.** Artnet price indices (Impressionist, Contemporary, Old Masters,
Post-War), annual returns, 1985-2024. S&P 500 sector ETFs, annual returns,
1999-2024.

**Computation.**

1. For the art market ($d = 4$ sectors): compute the $4 \times 4$ return
   covariance matrix. Compute the Fisher-Rao metric. Extract $\lambda_1$.

2. For equities ($d = 11$ sectors): same computation on annual returns.

3. Compare $\lambda_1^{\rm art}$ to $\lambda_1^{\rm equities}$.

**Expected.** $\lambda_1^{\rm art} / \lambda_1^{\rm equities} < 0.1$. Art
markets update prices infrequently (auctions occur sporadically), information
is private and subjective, and arbitrage is physically constrained (you cannot
short a Monet). All of this implies a much smaller spectral gap. The theory
predicts $\lambda_1^{\rm art} \approx 0.05$-$0.2$ per year versus
$\lambda_1^{\rm equities} \approx 5$-$15$ per year.

**Falsification.** $\lambda_1^{\rm art} > 1$ per year, or
$\lambda_1^{\rm art} / \lambda_1^{\rm equities} > 0.5$. If the art market's
spectral gap is comparable to equities, then either the spectral gap does not
measure information speed, or art markets are far more efficient than anyone
believes.

---

### Test 18: EMU Neck Curvature and Sovereign Spreads

**Hypothesis.** Within the European Monetary Union, the yield spread between a
peripheral country and Germany correlates with the "neck curvature" of the
connected sum $M^r_{\rm EU} = M^r_{\rm DE} \# M^r_{\rm peripheral}$. The neck
curvature is estimated by $1 - k/r$ where $k$ is the number of shared factors
between the two economies.

**Dataset.** 10-year sovereign yields from FRED: Germany (IRLTLT01DEM156N),
France, Italy, Spain, Portugal, Greece, Ireland, Netherlands. Daily, 1999-2024.
Macro factors: GDP growth, CPI, unemployment, trade balance from FRED for each
country.

**Computation.**

1. For each country pair (Germany, $X$):
   (a) Compute the spread: $s_t = y_t^X - y_t^{\rm DE}$.
   (b) Estimate the factor overlap $k$: run PCA on the combined macro variables
   of Germany and country $X$. Count factors that load significantly ($> 0.3$)
   on both countries' variables. This is $k$.
   (c) Compute the neck curvature proxy: $\kappa_{\rm neck} = 1 - k/r$ where
   $r$ is the total number of macro factors (from PCA on all EU countries).

2. Compute the rank correlation between average spread $\bar{s}$ and
   $\kappa_{\rm neck}$ across countries.

**Expected.** Rank correlation $> 0.6$. Germany-Netherlands (high $k/r$, many
shared factors) should have the smallest spread. Germany-Greece (low $k/r$,
few shared factors) should have the largest. The 2010-2012 Euro crisis
represents the moment when the connected sum nearly pinched off (the neck
curvature went to infinity).

**Falsification.** Rank correlation $< 0.2$ or wrong sign. If the factor
overlap does not predict spread magnitudes, the connected sum topology is not
the right model for monetary unions.

---

### Test 19: Cryptocurrency Efficiency Evolution

**Hypothesis.** Cryptocurrency markets evolve through stages of increasing
efficiency, with BTC (the oldest) being closest to a CAPM market and newer
tokens further away.

**Dataset.** BTC, ETH, SOL, DOGE daily returns from yfinance, 2018-2024 (the
period when all four are liquid).

**Computation.**

1. For each crypto, in rolling 252-day windows:
   (a) Estimate the Willmore energy proxy: $W = \mathrm{var}(\mathrm{Sharpe}
   _{\rm rolling})$ — the instability of the Sharpe ratio as a proxy for
   $\int |H|^2$.
   (b) Estimate the spectral gap $\lambda_1$ from the lag-1 autocorrelation
   of returns: $\lambda_1 \approx -\log|\hat{\phi}_{1}|$.
   (c) Estimate $r$ from PCA of the 4-crypto covariance matrix.

2. Compare across cryptos and across time. Plot the "efficiency trajectory"
   $(W(t), \lambda_1(t))$ for each.

**Expected.** BTC: lowest $W$, highest $\lambda_1$ (most efficient, fastest
mixing). DOGE: highest $W$, lowest $\lambda_1$ (least efficient, slowest
mixing). All four should show decreasing $W$ and increasing $\lambda_1$ over
time (trend toward efficiency).

**Falsification.** No ordering is consistent across time (the "efficiency
ranking" changes randomly from window to window), or DOGE is consistently
more efficient than BTC.

---

### Test 20: Spectral Gap and Social Mobility

**Hypothesis.** The spectral gap of the wealth exchange network correlates
with intergenerational income mobility across countries.

**Dataset.** Corak (2013): intergenerational income elasticity (IGE) for 22
OECD countries. World Bank: trade openness (trade/GDP), financial depth
(private credit/GDP), internet penetration — as proxies for exchange network
density.

**Computation.**

1. For each country, construct a "connectivity index" $\zeta$ as the first
   principal component of trade openness, financial depth, and internet
   penetration (all standardised).

2. The theory says: higher $\zeta$ implies higher $\lambda_1$ of the
   wealth exchange graph, which implies faster mixing and lower IGE
   (more mobility).

3. Run OLS: $\mathrm{IGE}_{i} = \alpha + \beta \cdot \zeta_i + \varepsilon_i$.

**Expected.** $\beta < 0$ with $p < 0.05$. Countries with more connected
economic networks (Scandinavia, Netherlands) have lower IGE (more mobility).
Countries with less connected networks (US, UK, Italy) have higher IGE
(less mobility).

**Falsification.** $\beta \geq 0$ or $p > 0.10$. If economic connectivity
does not predict mobility, the spectral gap analogy outside financial markets
does not hold.

---

## 7. The Scoring System

### Summary Table

| Test | Claim | Weight | Pass | Marginal | Fail |
|:-----|:------|:------:|:----:|:--------:|:----:|
| 1 | Sharpe = $\|H\|$ | 2 | $\beta_1 > 0$, $R^2 > 0.15$ | $R^2 \in [0.05, 0.15]$ | $\beta_1 \leq 0$ or $R^2 < 0.05$ |
| 2 | $r$ stable | 2 | Agreement $> 70\%$, CV $< 0.3$ | Agreement $\in [50\%, 70\%]$ | Agreement $< 50\%$ or CV $> 0.5$ |
| 3 | MUP/Cover ratio | 2 | Ratio $\in [3, 10]$ | Ratio $\in [1.5, 3)$ or $(10, 15]$ | Ratio $< 1.5$ or $> 15$ |
| 4 | $\lambda_1$ predicts $t_{1/2}$ | 2 | $|\rho| > 0.5$ | $|\rho| \in [0.2, 0.5]$ | $|\rho| < 0.2$ |
| 5 | $h_M$ drops before crises | 2 | $\Delta h > 0.5$ for $\geq 3$ crises | $\Delta h > 0.2$ for $\geq 3$ | $\Delta h < 0.2$ for $\geq 3$ |
| 6 | Three market types | 1 | Three $\beta$s observed | Two $\beta$s observed | Only one or none fits |
| 7 | Dyson class = GOE | 1 | $\beta=1$ in $>60\%$ windows | $\beta=1$ in $40$-$60\%$ | No $\beta$ fits $>40\%$ |
| 8 | $\alpha \approx r/2$ | 1 | $\bar{\alpha}/r \in [0.4, 1.2]$ | $\bar{\alpha}/r \in [0.25, 0.4)$ or $(1.2, 2]$ | $\bar{\alpha}/r < 0.25$ or $> 2$ |
| 9 | Jacobi $>$ GBM | 1 | Jacobi wins $>70\%$ | Jacobi wins $50$-$70\%$ | GBM wins $>60\%$ |
| 10 | Stability index $\approx 5$ | 1 | $r \in [3, 7]$ | $r \in \{2, 8\}$ | $r < 2$ or $r > 8$ |
| 11 | MIF $>$ cap-weight | 1 | MIF outperforms full period | MIF similar ($<$ 10 bps) | MIF underperforms |
| 12 | Geometric $>$ $2\sigma$ | 1 | Geometric Sharpe $> 2\sigma$ Sharpe | Similar ($<$ 0.05 diff) | $2\sigma$ wins majority |
| 13 | $h_M >$ VIX | 1 | $h_M$ AUC $>$ VIX AUC | AUC within 0.05 | VIX AUC $>$ $h_M$ AUC + 0.05 |
| 14 | Shapley-Brinson agree | 1 | Sign agreement $> 80\%$ | $[60\%, 80\%]$ | $< 60\%$ |
| 15 | LZ rate $\approx$ Kelly rate | 1 | Correlation $> 0.7$ | $[0.3, 0.7]$ | $< 0.3$ |
| 16 | FLB = curvature | 1 | Positive correlation, $p < 0.05$ | Right sign, $p \in [0.05, 0.15]$ | Wrong sign or $p > 0.15$ |
| 17 | Art $\lambda_1 \ll$ equity $\lambda_1$ | 1 | Ratio $< 0.1$ | Ratio $\in [0.1, 0.5]$ | Ratio $> 0.5$ |
| 18 | Neck curvature = spread | 1 | Rank corr $> 0.6$ | Rank corr $\in [0.2, 0.6]$ | Rank corr $< 0.2$ |
| 19 | Crypto efficiency ordering | 1 | BTC most efficient, consistent | Partially ordered | No ordering |
| 20 | $\lambda_1$ and mobility | 1 | $\beta < 0$, $p < 0.05$ | Right sign, $p \in [0.05, 0.15]$ | Wrong sign or $p > 0.15$ |

**Maximum score:** $5 \times 2 + 15 \times 1 = 25$ points.

| Total Score | Verdict |
|:------------|:--------|
| $\geq 19$ | **Strong support.** The geometric framework captures real structure. |
| $12$-$18.5$ | **Supported with caveats.** Core holds; some extensions need refinement. |
| $6$-$11.5$ | **Major revision needed.** Either the core geometry is right but applications fail, or vice versa. |
| $< 6$ | **Wrong.** Revisit the axioms. |

---

## 8. What Would Kill the Theory

We are explicit about the failure modes, because a theory that cannot specify
its own death conditions is not a scientific theory.

### 8.1 Catastrophic failures (any one of these kills the monograph)

**If Test 1 fails** — $\beta_1 \leq 0$ in the Sharpe-curvature regression —
then the central theorem of the monograph ($\mathrm{Sharpe}^{\ast} = \|H\|$) does
not hold empirically. This is the theorem from which almost everything else
follows. Its failure would mean that mean curvature is not the right geometric
quantity, or the Fisher-Rao metric is not the right geometry, or the market is
not a manifold. The monograph as presently conceived would need to be
withdrawn and rewritten from scratch.

**If Tests 1-5 all fail** — then the entire geometric framework is wrong. The
market is either not a manifold, the geometry is not Fisher-Rao, the dimension
is not stable, and the spectral quantities have no predictive power. In this
case, the correct response is to publish the negative results as a cautionary
paper: "A beautiful theory killed by ugly facts."

### 8.2 Serious failures (undermine major sections)

**If Test 7 fails** — eigenvalue spacings match none of GOE/GUE/GSE — then
the Dyson class correspondence (R21) is wrong. The random matrix theory
section (Part V) would need to be removed or heavily revised. The rest of the
monograph survives because the Dyson class is used interpretively, not
foundationally.

**If Test 3 fails** — MUP does not beat Cover — then the dimension reduction
argument is wrong. The practical payoff of the entire theory (faster
convergence by a factor of $(d-1)/r$) evaporates. The geometric framework
might still be theoretically correct but practically useless, which is almost
as bad.

**If Tests 8 and 9 both fail** — tail index is wrong AND Jacobi does not fit —
then the market process section (Part III) is wrong. The specific SDEs
(Jacobi, theta function, McKean) do not describe real market dynamics.

### 8.3 Tolerable failures

**Tests 16-20** are extensions to non-standard domains. If these fail while
Tests 1-15 pass, the core theory is validated but its range of applicability
is narrower than hoped. This is a normal outcome for a new theory.

**Test 10 (LTCM)** is a historical reconstruction with limited data. A failure
here is interesting but not devastating.

### 8.4 The honest assessment

Before running any experiments, the author's prior is:

- Tests 1-5 (core theory): 4 out of 5 will pass. Test 4 (spectral gap
  predicts half-life) is the most uncertain because the factor structure may
  be too noisy for the eigenvalue to be estimated precisely.

- Tests 6-10 (classification): 3 out of 5 will pass. Test 6 (three types
  exist) and Test 7 (Dyson class) are the strongest predictions; Tests 8-10
  depend on tail estimation and historical data quality.

- Tests 11-15 (applications): 3 out of 5 will pass. Tests 11 and 12
  (portfolio performance) are the hardest because transaction costs,
  estimation error, and market impact are not modelled. Test 15 (LZ-Kelly)
  should pass because it tests a mathematical identity.

- Tests 16-20 (extensions): 2 out of 5 will pass. These are the most
  speculative tests. Tests 17 (art spectral gap) and 18 (EMU neck curvature)
  have the clearest theoretical predictions.

**Expected total: approximately 12 out of 25 = 16 points.** This would place
the theory in the "Supported with caveats" category. An honest outcome for a
new theoretical framework.

---

## 9. Reproducibility

### 9.1 Code structure

```
code/experiments/
├── requirements.txt
├── config.py                  # Data paths, random seeds, window sizes
├── data_loader.py             # Unified data loading for all sources
├── test_01_sharpe_curvature.py
├── test_02_dimension_stability.py
├── test_03_mup_vs_cover.py
├── test_04_spectral_gap.py
├── test_05_cheeger_crisis.py
├── test_06_three_types.py
├── test_07_dyson_class.py
├── test_08_tail_index.py
├── test_09_jacobi_fit.py
├── test_10_ltcm_stability.py
├── test_11_mif_vs_capweight.py
├── test_12_pairs_threshold.py
├── test_13_cheeger_vs_vix.py
├── test_14_shapley_brinson.py
├── test_15_lz_kelly.py
├── test_16_flb_curvature.py
├── test_17_art_spectral_gap.py
├── test_18_emu_neck.py
├── test_19_crypto_efficiency.py
├── test_20_social_mobility.py
├── run_all.py                 # Runs all 20, prints scorecard
└── utils/
    ├── fisher_rao.py          # Fisher-Rao metric computation
    ├── kelly.py               # Kelly optimisation
    ├── curvature.py           # Mean curvature estimation
    ├── spectral.py            # Eigenvalue analysis
    ├── lz78.py                # LZ78 compression
    └── plotting.py            # Standardised diagnostic plots
```

### 9.2 Conventions

- **Random seed:** `np.random.seed(42)` in every script.
- **Rolling windows:** 252 days (1 year) unless stated otherwise. Step size =
  21 days (1 month).
- **Returns:** Log returns $r_t = \log(P_t / P_{t-1})$.
- **Missing data:** Forward-fill, then drop leading NaNs.
- **PCA:** Centred, on the correlation matrix (not covariance) to avoid
  scale effects.
- **Statistical tests:** Two-sided unless stated otherwise. Significance at
  $p < 0.05$.
- **Bootstrap confidence intervals:** 1000 bootstrap samples for all
  correlation and regression estimates.

### 9.3 Runtime estimates

| Test | Estimated runtime | Bottleneck |
|:-----|:-----------------|:-----------|
| 1 | 15 min | Kelly optimisation in 720 rolling windows |
| 2 | 5 min | Three PCA computations per window |
| 3 | 45 min | Monte Carlo integration for Cover UP |
| 4 | 3 min | AR(1) estimation |
| 5 | 2 min | Graph Laplacian computation |
| 6-7 | 10 min | Eigenvalue spacing analysis |
| 8 | 5 min | Hill estimator |
| 9 | 8 min | KS tests in rolling windows |
| 10 | 2 min | Small cross-section PCA |
| 11 | 20 min | Quarterly rebalancing backtest |
| 12 | 15 min | Pairs trading backtest |
| 13 | 5 min | ROC curve computation |
| 14 | 5 min | Shapley values |
| 15 | 10 min | LZ78 compression |
| 16-20 | 15 min | Various |
| **Total** | **$\approx$ 3 hours** | |

---

## 10. Open Questions from the Data

Even before running the experiments, the test design raises questions that the
theory does not fully answer. These are genuine open problems, not rhetorical
devices.

**Q1. What is the actual dimension $r$ of the S&P 500?** The theory says
$r \in \{4, 5, 6, 7, 8\}$ is the plausible range. PCA studies typically find
5-6 factors explaining 90% of variance. But stable rank, Marchenko-Pastur
edge detection, and PCA may disagree at the boundary. Test 2 will clarify
whether $r$ is a sharply-defined quantity or a fuzzy one.

**Q2. Is the spectral gap constant between crises?** The theory assumes
$M^r$ evolves slowly relative to the mixing time $1/\lambda_1$. If $\lambda_1$
itself fluctuates rapidly, the separation of time scales breaks down and the
manifold model loses its justification. Test 4 will reveal whether $\lambda_1$
is stable enough to be useful.

**Q3. Does the MUP survive transaction costs?** The theoretical regret bound
$r \log T / (2T)$ assumes zero transaction costs. In practice, the MUP
rebalances continuously. The theory suggests rebalancing at frequency
$\approx \lambda_1$ (once per mixing time), but this has not been tested.
Test 3 uses gross returns; a follow-up with realistic transaction costs
(5 bps per trade) is needed.

**Q4. Which real market is closest to a Clifford torus?** The classification
theorem says the Clifford torus is unstable (stability index 5), so no market
should stay there permanently. But some markets should visit the Clifford torus
topology transiently. The spread strategies of Test 10 may reveal this. If a
market's eigenvalue spacings match GUE ($\beta = 2$) for an extended period,
that market is living on the Clifford torus.

**Q5. Does the theory work for individual stocks?** All our tests use
portfolios or sectors. Individual stocks have much noisier returns. Can the
manifold be estimated from single-stock data (e.g. using Takens embedding)?
This requires Tests 2 and 15 to be adapted to univariate time series, which
is possible but not attempted here.

**Q6. What happens at the Feller boundary?** Test 9 checks whether portfolio
weights follow a Jacobi diffusion. The Jacobi diffusion has reflecting
boundaries at 0 and 1 (the Feller boundary condition). Leverage pushes
effective weights above 1, potentially exiting the simplex entirely. The
2022 UK LDI crisis is a natural experiment: leveraged gilt positions blew
through the boundary. A dedicated test on 2022 gilt data would be valuable
but requires non-free data.

**Q7. Can we hear the shape of the market?** The spectral gap $\lambda_1$
is one eigenvalue. The full Laplacian spectrum $\{\lambda_k\}$ should encode
the topology of $M^r$ (by the Kac-Milnor theorem and its generalisations).
Can we distinguish market topologies from their Laplacian spectra alone?
This is a harder version of Tests 6-7 that would require careful spectral
estimation.

---

## 11. Conclusion

This paper makes the geometric theory of efficient markets vulnerable to
falsification. We have specified twenty tests, each with a precise
falsification criterion. The tests range from the most central claim of the
monograph (the Sharpe-curvature identity) to speculative extensions (social
mobility as a spectral gap). We have been explicit about our priors: we
expect approximately 12 out of 25 points, placing the theory in the
"supported with caveats" category.

The most important outcome of running these tests is not whether the theory
passes or fails. It is what we *learn* from the failures. If the
Sharpe-curvature identity holds but the Dyson class does not, we learn that
the geometry is right but the random matrix analogy is wrong. If the MUP
beats Cover but the Cheeger constant does not predict crises, we learn that
the static geometry works but the dynamic interpretation needs revision. Every
pattern of pass/fail tells us something about which axioms are correct and
which need revision.

The geometric theory of efficient markets is, at present, a mathematical
framework looking for empirical validation. This paper provides the
validation protocol. The data will decide.

We invite the research community to run these tests. All code is open-source.
All data is freely available. The falsification criteria are stated in
advance, not adjusted after the fact.

Here is how to kill our theory. We dare you.

---

## References

1. Fama, E.F. and French, K.R. (1993). Common risk factors in the returns on
   stocks and bonds. *Journal of Financial Economics*, 33(1), 3-56.

2. Kenneth French Data Library.
   `mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html`

3. Cover, T.M. (1991). Universal portfolios. *Mathematical Finance*, 1(1),
   1-29.

4. Corak, M. (2013). Income inequality, equality of opportunity, and
   intergenerational mobility. *Journal of Economic Perspectives*, 27(3),
   79-102.

5. Marchenko, V.A. and Pastur, L.A. (1967). Distribution of eigenvalues of
   some sets of random matrices. *Mathematics of the USSR-Sbornik*, 1(4), 457.

6. Hill, B.M. (1975). A simple general approach to inference about the tail of
   a distribution. *Annals of Statistics*, 3(5), 1163-1174.

7. Lempel, A. and Ziv, J. (1978). Compression of individual sequences via
   variable-rate coding. *IEEE Transactions on Information Theory*, 24(5),
   530-536.

8. Brinson, G.P., Hood, L.R. and Beebower, G.L. (1986). Determinants of
   portfolio performance. *Financial Analysts Journal*, 42(4), 39-44.

9. Betfair Historical Data. `historicdata.betfair.com`

10. Artnet Price Database. `artnet.com/price-database`

11. Federal Reserve Economic Data (FRED). `fred.stlouisfed.org`

12. CBOE Volatility Index (VIX). `cboe.com/tradable_products/vix`

13. Mehta, M.L. (2004). *Random Matrices*, 3rd edition. Academic Press.

14. Oseledets, V.I. (1968). A multiplicative ergodic theorem: Lyapunov
    characteristic numbers for dynamical systems. *Transactions of the Moscow
    Mathematical Society*, 19, 197-231.

15. Nicholls, S. (2024). The Geometry of Efficient Markets: Minimal Surfaces,
    Universal Portfolios, and the Mathematics of Financial Markets. Monograph
    in preparation.

---

*Paper VIII.1 of "The Geometry of Efficient Markets" by Saxon Nicholls.*
*The twenty tests specified in this paper are the empirical backbone of the
monograph. Without them, everything else is mathematics. With them, it is
science.*
