# Experiment Plan v2: Institutional Data with Bootstrap Methods

**Saxon Nicholls** — me@saxonnicholls.com

## Design Principles

1. **Bootstrap everything** — block bootstrap (Politis-Romano 1994) for time series.
   Report 95% CIs, not p-values. No distributional assumptions.
2. **Corporate-action adjusted** — use Databento's adjustment factors for splits,
   dividends, mergers. Raw returns are corrupted by actions.
3. **Multi-timescale** — each test run at daily, weekly, monthly. If it only works
   at one frequency, it's fragile.
4. **d >> r for eigenvalue tests** — use 200+ assets (S&P 500) for Wigner surmise.
5. **Out-of-sample** — split data into estimation half and test half. No in-sample
   overfitting.
6. **Nanosecond resolution** — Databento PCAPs for microstructure tests.

## Data Requirements (Revised)

### Batch A: Equities Universe (for Tests 1-10)
- **Source:** Databento DBEQ.BASIC, ohlcv-1d
- **Symbols:** S&P 500 constituents (~500 stocks)
- **Period:** 2023-04-01 to 2024-12-31 (DBEQ.BASIC available from 2023-03)
- **Schema:** ohlcv-1d with corporate action adjustment
- **Est. size:** ~200MB, ~$0.10
- **Why:** 500 eigenvalues → robust Wigner surmise; broad universe for dimension test

### Batch B: Long History (for Tests 1, 3, 14)
- **Source:** Fama-French (already downloaded, free)
- **Period:** 1963-2026
- **Why:** 60+ years for rolling-window regressions, long-run MUP performance

### Batch C: Futures Cross-Asset (for intermarket tests)
- **Source:** Databento GLBX.MDP3, ohlcv-1d (already downloaded)
- **Symbols:** ES, CL, ZN, ZB, ZF, ZT, GC
- **Period:** 2010-2024
- **Why:** intermarket spreads, cross-asset correlations, yield curve factors

### Batch D: FX Tick Data (for FX tests)
- **Source:** Databento (FX venue TBD — check if they cover FX spot)
- **Symbols:** EURUSD, GBPUSD, USDJPY, USDCHF, AUDUSD, USDCAD, NZDUSD
- **Schema:** trades or mbp-1
- **Period:** 1 month of tick data for triangular arb test
- **Alt:** Massive S3 for FX if Databento doesn't cover spot FX

### Batch E: Options (for vol surface tests)
- **Source:** Databento OPRA.PILLAR, ohlcv-1d
- **Symbols:** SPX, SPY options (all strikes and expiries)
- **Period:** 2023-2024
- **Est. size:** ~500MB
- **Why:** reconstruct the implied vol surface, test curvature conditions

### Batch F: L2/L3 Order Book (for microstructure tests)
- **Source:** Databento XNAS.ITCH, mbp-10 (L2) and mbo (L3)
- **Symbols:** AAPL, MSFT, SPY
- **Period:** 1 week (Dec 2024)
- **Why:** bid-ask as Fisher-Rao distance, market impact as curvature

### Batch G: PCAPs (for nanosecond tests)
- **Source:** Databento AWS S3 / rsync
- **Format:** Raw packet captures with hardware timestamps
- **Symbols:** AAPL on NASDAQ
- **Period:** 1 day
- **Why:** triangular arb timing, latency analysis, true MCF speed measurement

## Redesigned Tests

### Core Tests (Revised)

**Test 1R: Sharpe-Curvature Identity (Bootstrap)**
- Same as Test 1 but with block bootstrap (block size = 21 days)
- 10,000 bootstrap resamples → 95% CI for β₁
- Run at daily AND weekly AND monthly frequency
- Out-of-sample: estimate H on first half, test Sharpe on second half
- Add: permutation test (shuffle H assignments across windows, check if
  the real β₁ exceeds 95th percentile of shuffled)
- Data: FF25 daily (Batch B)

**Test 2R: Manifold Dimension (Multiple Estimators, Large Universe)**
- Use S&P 500 (d ≈ 500) from Batch A
- Four estimators: (a) variance ratio 90%, (b) Marchenko-Pastur edge,
  (c) parallel analysis (compare to random matrix eigenvalues),
  (d) cross-validation (hold out assets, predict returns from r factors)
- Drop stable rank (doesn't work for concentrated spectra)
- Add: bootstrap CI for each estimator
- Multi-timescale: daily, weekly, monthly
- Crisis vs non-crisis: compute r separately for 2008, 2020, 2022

**Test 3R: MUP vs Cover (Laplace, Not MC)**
- Replace MC integration with LAPLACE APPROXIMATION (which the theory is about!)
- The C++ code already implements this (LaplaceIntegrator)
- Compare: Laplace-MUP, MC-MUP, Cover, equal-weight, Kelly b*
- Out-of-sample: estimate on 252-day windows, test on next 63 days
- Bootstrap CI for the regret ratio
- Data: FF25 (Batch B) + S&P 500 (Batch A)

**Test 4R: Spectral Gap → Mean-Reversion (Corrected)**
- The WRONG approach: correlate eigenvalue ratio with half-life
- The RIGHT approach: estimate the Jacobi spectral gap DIRECTLY from the
  transition density of the portfolio weight process
- Method: fit a Jacobi diffusion (or OU process) to the principal component
  time series. The fitted κ IS the spectral gap.
- Then test: does κ predict the out-of-sample half-life?
- Block bootstrap CIs for both κ and the half-life
- Data: FF5 factors monthly + sector ETFs weekly (Batch B + existing)

**Test 5R: Cheeger → Crisis (Expanded, Bootstrap)**
- Use S&P 500 (500 assets) for a much richer correlation graph
- Compute: Fiedler eigenvalue, average correlation, dispersion, spectral gap
- Run on DAILY frequency (not just 126-day rolling windows)
- Block bootstrap CI for the Fiedler time series
- Add crises: 1998 LTCM, 2001 dot-com, 2008 GFC, 2011 Euro, 2015 CNY,
  2018 volmageddon, 2020 COVID, 2022 rates
- Receiver Operating Characteristic (ROC) analysis: does Fiedler predict
  >5% drawdown within 3 months? Compute AUC with bootstrap CI.
- Compare: Fiedler vs VIX vs SKEW vs credit spread as crisis predictors
- Data: S&P 500 (Batch A) + VIX (existing)

### New Tests Using Institutional Data

**Test N1: Corporate Action Impact on Fisher Matrix**
- Download Databento reference data (corporate actions, adjustment factors)
- Compute Fisher matrix WITH and WITHOUT corporate action adjustment
- Hypothesis: unadjusted Fisher matrix has spurious eigenvalues from splits/dividends
- This tests whether our core computation (Fisher matrix) is robust to data quality
- Data: Databento DBEQ.BASIC reference data

**Test N2: Multi-Timescale Consistency**
- Estimate r, ||H||, λ₁, h_M at five timescales: 1-second, 1-minute, 1-hour, 1-day, 1-week
- Theory predicts: r should be the SAME at all timescales (the manifold dimension is intrinsic)
- ||H|| should decrease at shorter timescales (HFT removes short-term curvature)
- λ₁ should INCREASE at shorter timescales (faster mean-reversion)
- h_M should be approximately constant (the Cheeger constant is topological)
- Data: Databento ohlcv-1s through ohlcv-1d for 50 equities

**Test N3: Information Channel Capacity**
- From NETWORK_INFORMATION_THEORY: R_conv = min(λ₁, C)
- Estimate C from the Shannon entropy rate of the price process (using LZ compression)
- Estimate λ₁ from the spectral gap (using the corrected Test 4R method)
- Hypothesis: the bottleneck switches from C to λ₁ around 2005-2010
  (when electronic trading made C >> λ₁)
- Data: Batch B (FF, long history) + Batch A (recent, high C)

**Test N4: Triangular FX Arbitrage at Tick Level**
- Compute the triangular deviation ε = log(EURUSD × USDCHF) - log(EURCHF) at each tick
- Hypothesis: |ε| is bounded by the bid-ask spread, mean-reverts at rate λ₁ ~ milliseconds
- Compute the Fisher-Rao distance between the bid and ask distributions at each tick
- Block bootstrap CI for the mean-reversion speed
- Data: Batch D (FX tick data)

**Test N5: Vol Surface Curvature**
- Reconstruct the SPX implied vol surface from options data
- Compute: Gaussian curvature K, mean curvature H at each (strike, maturity) point
- Test no-arbitrage conditions as curvature bounds (butterfly ↔ H bounded, calendar ↔ K bounded)
- Hypothesis: curvature is lower for near-term ATM options (most liquid) and higher for wings/far-dated
- Compute VVIX from our own data and compare to CBOE published VVIX
- Data: Batch E (SPX options)

**Test N6: LOB Bid-Ask = Fisher-Rao Distance**
- From L2 order book data: normalise bid and ask side to distributions
- Compute Fisher-Rao distance d_FR(b_bid, b_ask) at each snapshot
- Compare to the dollar bid-ask spread
- Hypothesis: d_FR correlates with the dollar spread (correlation > 0.8)
- The Fisher-Rao spread should be MORE stable than the dollar spread
  (because it's normalised by volume at each level)
- Data: Batch F (L2 order book for AAPL, MSFT, SPY)

**Test N7: Market Impact = LOB Curvature**
- From L2/L3 order book: compute the curvature κ_LOB at the best bid and ask
- After each trade, measure the price impact ΔP
- Hypothesis: ΔP ∝ κ_LOB × trade_size (impact is curvature × size)
- The square-root law ΔP ~ √Q should emerge from the Jacobi boundary behaviour
- Block bootstrap CI for the curvature-impact regression
- Data: Batch F

### Non-Parametric Methods

**Block Bootstrap Protocol:**
For every test statistic θ̂:
1. Compute θ̂ on the full sample
2. Generate B = 10,000 bootstrap resamples using circular block bootstrap
   (block size = max(√T, 21) for daily data)
3. Compute θ̂* on each resample
4. Report: θ̂ with 95% CI = [θ̂*_{0.025}, θ̂*_{0.975}]
5. Report: bootstrap p-value = fraction of θ̂* that are more extreme than θ̂

**Permutation Tests:**
For correlation tests (e.g., Sharpe vs H):
1. Compute the test statistic (correlation) on the real data
2. Permute one variable (shuffle H across windows) 10,000 times
3. Compute the test statistic on each permuted dataset
4. p-value = fraction of permuted statistics ≥ observed statistic

**Cross-Validation:**
For dimension estimation:
1. Split assets into 5 folds
2. For each fold: estimate r on 4/5 of assets, predict returns of held-out 1/5
   using the r-factor model
3. Choose r that minimises mean cross-validated prediction error
4. This gives a MODEL-FREE estimate of r (no distributional assumptions)

## Execution Order (v2)

**Phase 1 (now):** Run Tests 1R, 4R, 5R with existing data (bootstrap versions)
**Phase 2:** Download Batch A (S&P 500). Run Tests 2R, 3R, 6R.
**Phase 3:** Download Batch D (FX tick). Run Test N4.
**Phase 4:** Download Batch E (options). Run Test N5.
**Phase 5:** Download Batch F (L2 book). Run Tests N6, N7.
**Phase 6:** Run multi-timescale test (N2) and information channel test (N3).

## What We Can and Cannot Prove

### CAN prove empirically (with current data + Databento):
- Sharpe correlates with estimated curvature (Test 1R — already PASSED)
- MUP outperforms Cover out-of-sample (Test 3R)
- Dispersion/Fiedler drops before some crises (Test 5R)
- Bid-ask spread correlates with Fisher-Rao distance (Test N6)
- Market impact correlates with LOB curvature (Test N7)
- Triangular FX arb mean-reverts at measurable speed (Test N4)

### CANNOT prove empirically (would need infinite data or counterfactual):
- That the manifold IS M^r (we can only estimate r and test consistency)
- That the Fisher-Rao metric IS the correct metric (we can test predictions derived from it)
- That MCF IS the convergence mechanism (we can observe convergence and test the rate)
- That the three types exist as distinct categories (we can test spacing statistics)

### The honest gap:
The theory makes GEOMETRIC claims (the market IS a submanifold, the metric IS Fisher-Rao,
curvature IS the Sharpe ratio). Empirical tests can only check PREDICTIONS derived from
these claims. If the predictions hold, the theory is CONSISTENT with the data. It is
not PROVED by the data. Multiple theories could generate the same predictions. The
geometric theory's advantage is its UNITY — one framework generates many predictions
across different markets, timescales, and asset classes.
