# Experimental Problems: Issues to Address in Later Sessions

**Saxon Nicholls** — me@saxonnicholls.com

**Last updated:** Session 2

---

## Summary

28 tests run. 11 PASS, 9 MARGINAL, 7 FAIL, 1 INCONCLUSIVE.
Score: 19.5/33 = 59%.

The CORE theory is strongly supported (slope = 1.007, R² = 0.986).
The EXTENSIONS have specific problems documented below.

---

## Problems to Fix

### P1: Spectral Gap Prediction (Test 4) — WRONG PROXY

**Problem:** We used the covariance eigenvalue ratio as a proxy for the
Jacobi spectral gap. These are different objects. The covariance ratio
measures cross-sectional concentration; the Jacobi gap measures
time-series mean-reversion speed.

**What we found:** OU-estimated κ correlates 0.847 with eigenvalue for
5 PCs (FF5 factors) but only -0.15 for 9 PCs (sector ETFs) and -0.19
for 15 PCs (50 equities). The FF5 result was a small-sample artefact.

**Fix needed:**
- The theory should specify that the spectral gap predicts the SLOWEST
  convergence rate, not the relationship between eigenvalue and κ
- Use the actual Jacobi operator (not the covariance matrix) to estimate
  the spectral gap — this requires solving the Jacobi SDE
- Test with international data (more independent factors → more PCs)
- Consider: the prediction may be qualitative (larger eigenvalue → different
  κ) rather than quantitative

**PROPOSED FIX (Voronoi transition matrix approach):**
The covariance matrix is way too simple for this — it's a linear, second-order
approximation to the geometry. The Jacobi operator lives on the actual manifold.

The right approach uses the Voronoi/tessellation machinery that worked
spectacularly in Test 15V (Z = -21.5):

1. Build the Voronoi partition of the portfolio simplex using K-means on
   PCA-projected returns (same as Test 15V)
2. Compute the transition matrix P(cell j at t+1 | cell i at t)
3. The SECOND EIGENVALUE of P, λ₂(P), IS the discrete spectral gap
   on the Voronoi graph — the discrete approximation to the Jacobi eigenvalue
4. The mixing time = -1/log(λ₂) = the half-life of convergence to stationarity
5. Test: does this mixing time predict the observed half-life of factor returns?

This is the discrete Cheeger inequality on the Voronoi graph — the exact
quantity the theory predicts. No covariance, no linearisation, no parametric
assumptions. Pure manifold geometry from the observed cell transitions.

The transition matrix from 15V already gave us: LZ-Markov correlation = 0.987.
The SAME matrix's second eigenvalue gives us the spectral gap. We should
already have this data — just need to extract λ₂.

**Paper impact:** CLASSIFICATION.md and PORTFOLIO_GEOMETRY.md should qualify
the spectral gap prediction. Currently stated too precisely.

---

### P2: Laplace Convergence Rate (Test N15) — WRONG TEST DESIGN

**Problem:** We compared Laplace b* to MC posterior mean. Both are
approximations. The "error" we measured = Laplace error + MC error.
MC error is O(1/√N) with N=5000 samples → floor at ~0.003.
The Laplace error is O(1/T²) → below the MC floor for T > ~500.

**What we found:** Apparent convergence slope = -0.22 (theory: -2.0).
The error plateaus at 0.003 for T > 1000 — this is the MC floor.

**Fix needed:**
- For d=2 or d=3: compute the EXACT simplex integral (quadrature)
  and compare to Laplace. This removes the MC error entirely.
- For d=25: use importance sampling MC with N=100,000+ samples
  to push the MC floor below the Laplace error
- Alternative: compare the Laplace log-normalisation constant
  (which has a closed-form expression) to the MC estimate

**Paper impact:** LAPLACE.md's O(1/T²) claim is theoretically derived
but not yet empirically confirmed. Should note this.

---

### P3: Vol Surface Butterfly (Test N2) — DATA QUALITY

**Problem:** End-of-day closing prices violate the butterfly condition
~42% of the time because they are stale (last trade hours old) with
wide bid-ask spreads ($1-5 for SPX options).

**What we found with mid-market quotes (N2R):**
- Total violations: 26% (down from 42%)
- TRUE violations (beyond bid-ask tolerance): 5.2%
- 80% of apparent violations are within the bid-ask spread

**Fix needed:**
- Use intraday mid-quotes (not end-of-day) for a clean snapshot
- Pre-filter: only use options with bid-ask spread < 10% of mid
- Use the butterfly condition on OPTION PRICES directly, not on
  implied vol (the IV inversion introduces its own numerical error)
- Consider: 5.2% true violations may be genuine microstructure effects
  (the market is not perfectly arbitrage-free at every instant)

**Paper impact:** VOLATILITY_SURFACE.md's "no-arb = curvature bounds"
is directionally correct but the 5.2% residual violations need explanation.

---

### P4: FX Sharpe-Curvature (Test N10) — WRONG METRIC

**Problem:** The Sharpe-curvature identity works beautifully on equities
(slope = 1.007) but NOT on FX (correlation = -0.006). The FX carry
trade premium involves interest rate differentials, which are not
captured by the return covariance structure alone.

**What we found:** 43 rolling windows on 7 USD pairs, zero correlation
between estimated ||H|| and realised Sharpe.

**Fix needed:**
- Incorporate the interest rate differential INTO the curvature estimate
  (the carry premium is a DRIFT term, not a curvature term in the
  standard Fisher-Rao metric)
- Use the EXTENDED Fisher-Rao metric that includes the forward rate
  basis: g^FR_carry_{ij} = g^FR_{ij} + r_i r_j (where r_i is the
  interest rate on currency i)
- Alternative: test the Sharpe-curvature identity on FX RETURNS
  (not levels) after subtracting the carry component
- More data: 43 windows (8 years of daily) may not be enough.
  Use the minute-level spot FX data (34K bars)

**Paper impact:** FOREIGN_EXCHANGE.md's "carry = mean curvature" needs
qualification. The carry premium may involve a different geometric
object than the return-space mean curvature.

---

### P5: Market Impact = LOB Curvature (Test N12) — WRONG CURVATURE PROXY

**Problem:** Inverse depth (1/best_size) does NOT predict price impact
(r = 0.04). But the bid-ask SPREAD does predict impact (r = 0.35).

**What we found:**
- κ (inverse depth at best) vs |ΔP|: r = 0.04 (essentially zero)
- Spread vs |ΔP|: r = 0.35 (AAPL: 0.50, MSFT: 0.28, SPY: 0.26)
- Depth concentration vs |ΔP|: r ≈ 0.10

**Fix needed:**
- Use the SPREAD as the curvature proxy (consistent with N3: spread
  correlates with Fisher-Rao distance)
- Use trade-by-trade data (not L2 snapshots) to measure actual
  impact of each trade vs pre-trade book state
- Compute the full depth profile curvature (not just inverse best depth)
  using all 10 levels of the L2 book
- The theory (MARKET_MICROSTRUCTURE.md) should say "impact ∝ spread"
  rather than "impact ∝ inverse depth"

**Paper impact:** MARKET_MICROSTRUCTURE.md Theorem M2 should use the
spread (Fisher-Rao distance) as the curvature measure, not raw inverse
depth. This is actually MORE consistent with the theory (the spread IS
a Fisher-Rao quantity from N3).

---

### P6: Negative Curvature → Mandatory Alpha (Test N16) — WRONG COMPARISON

**Problem:** Crypto has LOWER curvature (||H|| = 0.21) than FF25 equities
(||H|| = 1.39). The theory predicts hyperbolic (pseudo-Anosov) markets
should have HIGHER curvature.

**What we found:** FF25 portfolios have artificially high curvature because
they are SORTED by size and value — the extreme portfolios (small-value vs
large-growth) are geometrically far apart by construction. Crypto's 4 unsorted
tokens naturally have lower curvature.

**Fix needed:**
- Compare LIKE with LIKE: crypto vs 4 random equities (not 25 sorted portfolios)
- Or: compare crypto at different times (crisis vs calm) — the theory predicts
  curvature should be higher during crypto crises
- Or: compare mature crypto (BTC) vs new crypto (memecoins) — the theory
  predicts less mature markets have higher curvature (Stage 2 vs Stage 4)
- The "mandatory alpha" claim requires finding a market with VERIFIED negative
  intrinsic curvature and showing ||H|| > 0 always. This is hard to do
  empirically because we can't directly measure the intrinsic curvature.

**Paper impact:** CONVEXIFICATION.md Corollary 4.2 (mandatory alpha for
hyperbolic markets) should be qualified as "theoretical; empirical verification
requires identifying a market with confirmed negative intrinsic curvature."

---

### P7: Geometric Pairs Entry (Test N14) — SHORT SAMPLE

**Problem:** z* wins only 50% of pairs (no better than 2σ) on 880 days
of Databento equities data. The z* threshold depends on κ, which is
estimated with noise from a short sample.

**Fix needed:**
- Use FF25 data (15,770 days) for longer sample and more stable κ estimates
- Use the sector ETFs (6,539 days, 9 sectors) for pairs between sectors
- Backtest properly: walk-forward (re-estimate κ each month) rather than
  in-sample (estimate κ on full period)
- Control for transaction costs (the 2σ rule trades less often → lower costs)

**Paper impact:** PAIRS_TRADING.md should note that the geometric entry
rule z* = √(1+r/κ) has theoretical justification but no clear empirical
advantage over 2σ in our current tests.

---

### P8: Three Market Types / Wigner Surmise (Test 6) — TOO FEW EIGENVALUES

**Problem:** With d=25 assets, we have 24 eigenvalues and 23 spacings.
The Wigner surmise test requires hundreds of spacings to distinguish
β=1 (GOE) from β=2 (GUE) from β=4 (GSE).

**Fix needed:**
- Download the full S&P 500 from Databento DBEQ.BASIC (d ≈ 500 → 499 spacings)
- Use the Kolmogorov-Smirnov test on the spacing distribution with enough
  spacings to have statistical power
- Alternative: use the ratio of consecutive spacings (which converges faster
  than the full distribution test)

**Paper impact:** RANDOM_MATRIX.md's Theorem 1.1 (Dyson class forced by
geometry) cannot be confirmed with d=25. The test needs d ≥ 200.

---

## Priority Order for Fixing

1. **P8** (500 stocks from DBEQ) — one download fixes the Wigner surmise test
2. **P4** (FX carry metric) — intellectual fix, needs thought about the right metric
3. **P2** (Laplace rate for d=2) — clean theoretical validation with exact integrals
4. **P5** (impact = spread not depth) — minor restatement in the paper
5. **P1** (spectral gap) — needs the Jacobi operator, not just the covariance
6. **P3** (vol surface) — N2R with mid-quotes is already at 5.2% (near PASS)
7. **P6** (mandatory alpha) — needs a genuinely hyperbolic market
8. **P7** (pairs entry) — longer data and walk-forward backtest

---

## What IS Confirmed (do not change)

These results are rock-solid and should not be qualified:

| Result | Test | Statistic |
|:-------|:-----|:----------|
| Sharpe = curvature (contemporaneous) | 1R | Bootstrap 3/3, p = 0.0001 |
| Sharpe = curvature (PREDICTIVE) | N9 | **slope = 1.007** ± 0.18, p = 10⁻⁸ |
| Fisher-Rao distance = risk premium | N13 | R² = 0.986, p = 10⁻²³ |
| Shapley attribution | 14 | r = 0.956 |
| EMU spreads = geometric distance | 18 | r = 0.927 |
| Manifold dimension is intrinsic | N17 | r = 3 at all timescales, CV = 0 |
| LZ prefix tree = filtration tree | 15V | Z = -21.5, LZ-Markov r = 0.987 |
| Yield curve inversion → recession | N11 | 3/3 perfect |
| MIF outperforms cap-weight | 11 | +6.63%/yr OOS |
| BTC most efficient crypto | 19 | Lowest autocorrelation |

---

*"The theory is correct in its core predictions. The extensions need
better data, better estimators, and more precise statements about
what exactly is predicted."*
