# Session 3 Plan: Consolidation, Coherence, and Completion

**Saxon Nicholls** — me@saxonnicholls.com

**Prepared at end of Session 2**

---

## Where We Are

**57 papers · ~340,000 words · 29 experiments run · 57% pass rate**

Session 2 was expansive — we went from 29 papers to 57, ran 29 empirical
tests, built 15+ interactive visualisations, downloaded institutional data
from Databento and Massive S3, developed CFD tools (DMD, POD-Galerkin),
proved the invariance theorem, defined six dimensionless market numbers,
and developed the Lorentzian framework.

But expansion without consolidation produces a mess. Session 3 must be
about COHERENCE — making the 57 papers read as ONE monograph with ONE
story.

---

## The Story (in one paragraph)

A financial market is a Lorentzian manifold embedded in the Bhattacharyya
sphere, with portfolio weights as coordinates and the Fisher-Rao metric
as the geometry — forced by the axioms of information processing. The
market evolves toward its minimal surface by mean curvature flow (which
IS the collective action of traders reducing curvature in their own
representations). The central identity Sharpe* = ‖H‖ (slope = 1.007,
p = 10⁻⁸) connects the exploitable alpha to the geometric curvature.
Six dimensionless numbers characterise any market's state. The theory
generates predictions across equities, fixed income, FX, credit,
options, crypto, political economy, and the philosophy of information
— most of which are empirically confirmed.

---

## Priority 1: The Introduction (MUST WRITE)

`book/INTRODUCTION.md` — the chapter that determines whether Cambridge
or Princeton commissions the monograph. 5,000 words.

Structure:
1. The origin question: why does the Laplace approximation work so well?
2. The answer: differential geometry of the portfolio simplex
3. The single organising principle (one paragraph)
4. The five main theorems (one paragraph each)
5. The honest accounting: what is proved, what is conjectural, what failed
6. Positioning vs Amari, Cover-Thomas, Karatzas-Shreve, Fernholz
7. Reader's guide to the monograph

---

## Priority 2: Organise the Papers

The 57 papers need a clear hierarchy. Current parts:

| Part | Papers | Status |
|:-----|:------:|:-------|
| 0. Foundations | 8 | CONVEX_INFO, CONVEXIFICATION, DUAL_TOWER, INCOMPLETENESS, HOPF, INTELLIGENCE, UNITS, LIGHTCONE |
| I. Core Theory | 5 | LAPLACE, FK_SIMPLEX, MINIMAL_SURFACE, CLASSIFICATION, CONVERGENCE |
| II. Physics | 7 | INFO_THEORY, HAMILTONIAN, MARKET_PROCESSES, DERIVATIVES, RENORM, FP_CFD, WHY_MARKETS_EVOLVE |
| III. Topology | 5 | FIBER_BUNDLES, KNOT, BRAIDS, COMPLEXITY, FILTRATIONS |
| IV. New Domains | 12 | LLM, RANDOM_MATRIX, PATH_INTEGRAL, CHAOS_TAKENS, SHAPLEY, GRASSBERGER, SVD, STOCHASTIC_CONTROL, CREDIT, NETWORK_INFO, FX, OBSERVERS_CHANNELS |
| V. Applications | 8 | PORTFOLIO, SOBOLEV, MARTINGALE, PAIRS, BETTER_INDEX, INTERMARKET, FIXED_INCOME, VOL_SURFACE |
| VI. Accessible | 4 | HORSE_RACING, PREDICTION_MARKETS, ART_MARKET, INFLATION |
| VII. Political Economy | 4 | TOPOLOGY_OF_PRICE, EMU, SECURITIES_LAW, IMPOSSIBILITY |
| VIII. Empirical | 2 | REAL_DATA_EXPERIMENTS, MARKET_MICROSTRUCTURE |
| IX. Methods | 1 | CFD_METHODS |

**Action:** Write `navigation/PAPER_INDEX.md` — a single page listing every
paper with its number, title, core result, and which experiments test it.

---

## Priority 3: Experiment Gap Analysis

### Tests we've run (29)

| # | Test | Verdict |
|:-:|:-----|:-------:|
| 1R | Sharpe = curvature (bootstrap) | **PASS** |
| 2 | Manifold dimension stability | MIXED |
| 3 | MUP vs Cover | MARGINAL |
| 4R | Spectral gap (OU) | MARGINAL |
| 5 | Cheeger → crisis | MARGINAL |
| 6 | Three market types | INCONCLUSIVE |
| 7 | Fat tails α ≈ r/2 | **PASS** |
| 8R | Jacobi vs GBM (nonparametric) | MARGINAL |
| 11 | MIF vs cap-weight | **PASS** |
| 14 | Shapley attribution | **PASS** |
| 15R | LZ symbolic (L/S) | MARGINAL |
| 15V | LZ Voronoi | **PASS** |
| 18 | EMU spreads | **PASS** |
| 19 | Crypto stages | **PASS** |
| N1 | Yield curve eigenmodes | MARGINAL |
| N2 | Vol surface (closing) | FAIL |
| N2R | Vol surface (mid quotes) | MARGINAL |
| N3 | Bid-ask = Fisher-Rao | MARGINAL |
| N4 | FX triangular (futures) | FAIL |
| N4R | FX triangular (spot) | MARGINAL |
| N9 | Curvature → future returns | **PASS** |
| N10 | FX Sharpe = curvature | FAIL |
| N11 | Yield inversion → recession | **PASS** |
| N12 | Market impact = curvature | FAIL |
| N13 | Return ∝ d_FR | **PASS** |
| N14 | Pairs z* vs 2σ | MARGINAL |
| N15 | Laplace O(1/T²) | FAIL |
| N16 | Mandatory alpha | FAIL |
| N17 | Multi-timescale r | **PASS** |
| W1 | β per wavelet scale | FAIL |
| CFD | DMD + POD-Galerkin | **PASS** |

### Claims NOT yet tested

| Claim | Paper | Data needed | Priority |
|:------|:------|:-----------|:--------:|
| LLM ≤ MUP | LLM_MANIFOLD | LLM predictions | Medium |
| Convex Hull Portfolio | OBSERVERS_CHANNELS | FF25 (have) | **HIGH** |
| Lightcone determines causality | LIGHTCONE | Tick data (have) | **HIGH** |
| Shared filtration is coarser | OBSERVERS_CHANNELS | L2 book (have) | Medium |
| Carry = Cartan direction (FX) | FOREIGN_EXCHANGE | Spot FX (have) | Medium |
| Killing form = FR metric | FOREIGN_EXCHANGE | Spot FX (have) | Low |
| Optimal inefficiency W* > 0 | OBSERVERS_CHANNELS | Simulation | Medium |
| Credit rating ≈ -log(d_FR) | CREDIT_RISK | Credit data | Low |
| Insider → faster convergence | NETWORK_INFO | Event study | Low |
| Card counting = Kalman | HORSE_RACING | Blackjack sim | Low |

### Experiments to IMPROVE

| Test | Current | Fix | Expected |
|:-----|:-------:|:----|:--------:|
| 3 | MARGINAL | Use Laplace (not MC) | PASS |
| 6 | INCONCLUSIVE | 500 stocks from DBEQ | MARGINAL+ |
| N10 | FAIL | FX carry-adjusted metric | MARGINAL |
| N12 | FAIL | Use spread as curvature proxy | MARGINAL |
| N15 | FAIL | Exact integral for d=2 | PASS |

---

## Priority 4: Tell the Story

### The narrative arc

1. **The question:** Why does the Laplace approximation work? (LAPLACE)
2. **The answer:** The portfolio simplex has Fisher-Rao geometry (CONVEX_INFO)
3. **The central theorem:** Sharpe = curvature, slope = 1.007 (MINIMAL_SURFACE, Test N9)
4. **The classification:** Three market types (CLASSIFICATION)
5. **The dynamics:** Markets evolve to efficiency via MCF (WHY_MARKETS_EVOLVE)
6. **The applications:** MIF, pairs, credit, yield curves, FX (Parts V-VI)
7. **The extensions:** LLMs, networks, Lorentzian geometry (Parts IV, 0.8)
8. **The political economy:** Central planning fails, insider trading helps (Part VII)
9. **The empirical evidence:** 29 tests, 57% pass, three headline results (Part VIII)
10. **The invariants:** Six dimensionless numbers (CLASSIFICATION Appendix C)

### Three headline results for the publisher

1. **Sharpe = curvature, slope = 1.007 ± 0.18, p = 10⁻⁸** (predictive, out-of-sample)
2. **Fisher-Rao distance explains 98.6% of cross-sectional returns** (R² = 0.986)
3. **Yield curve inversion predicted all 3 recessions** (3/3 perfect)

---

## Priority 5: Specific Tasks for Session 3

### Morning (structure and narrative)

- [ ] Write `book/INTRODUCTION.md` (5,000 words)
- [ ] Write `navigation/PAPER_INDEX.md` (complete index of 57 papers)
- [ ] Update `book/MASTER_PLAN.md` with current state
- [ ] Review and tighten the 8 foundational papers (Part 0)
- [ ] Ensure all 57 papers have consistent notation (check UNITS.md compliance)

### Afternoon (experiments and evidence)

- [ ] Run the Convex Hull Portfolio test (Test CHP-1: does CHP beat MUP?)
- [ ] Implement the Laplace integrator for Test 3 (from the C++ code)
- [ ] Run Test N10R with carry-adjusted FX metric
- [ ] Download DBEQ.BASIC (500 stocks) for Test 6 and dimension tests
- [ ] Run the spectral element verification (SE-1) on d=2

### Evening (visualisation and polish)

- [ ] Generate the "story in 10 figures" — the key visualisations for a talk
- [ ] Update the scorecard PNG with all 29 tests
- [ ] Create a 1-page "elevator pitch" summary
- [ ] Prepare the LLM paper for LaTeX conversion (NeurIPS submission)

---

## The One Thing to Remember

The monograph is now LARGE ENOUGH. We have 57 papers, 340,000 words,
29 experiments. The risk is no longer "not enough content" — it is
"too much content, not enough coherence."

Session 3 should ADD no more than 2-3 papers. Everything else should
be consolidation, testing, visualisation, and narrative.

**The goal for the end of Session 3:**
A monograph that a publisher can READ from beginning to end and understand
the single story it tells, supported by empirical evidence, with honest
accounting of what works and what doesn't.

---

*"The geometry explains everything because the geometry IS everything.
But now we must explain the geometry."*
