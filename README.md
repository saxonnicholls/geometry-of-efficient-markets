# The Geometry of Efficient Markets

**Saxon Herschel Nicholls** — me@saxonnicholls.com

*Minimal Surfaces, Universal Portfolios, and the Mathematics of Financial Markets*

**62 papers · ~400,000 words · 130+ results · 30 conjectures · 50+ open problems**

> **PREPRINT** — This is a working draft. None of these papers have been peer-reviewed.
> Comments, corrections, and collaboration inquiries welcome: me@saxonnicholls.com

---

## Origin

This monograph began in Port Lincoln, South Australia — a fishing town on the
edge of the desert and the Southern Ocean. The author grew up watching
markets: tuna boats coming in, quota holders negotiating, livestock at
auction, grain in silos. The directed graph of a market was visible to the
naked eye before there were words for it. The palindromic structure was in
the seasons. The Feller boundary was in the collapsed fish stocks. The
self-referential channel was in the feedback loop between catch, price,
effort, and stock.

The mathematics came later. The geometry was always there.

---

## The Three Market Types

<p align="center">
  <img src="code/visualisation/market_manifolds.png" width="100%" alt="The three classified market manifold types in the Bhattacharyya sphere"/>
</p>

**The classification theorem in one picture.** Every efficient market falls into one of three geometric types, each living as a submanifold of the Bhattacharyya sphere $S^{d-1}_+$. *Top left:* the ambient space — the positive octant of the unit sphere, where $\sqrt{b}$ coordinates give the Fisher-Rao isometry. *Top right:* **Type I (CAPM)** — a great circle with a Jacobi diffusion path mean-reverting around the log-optimal portfolio. The only stably efficient type. *Bottom left:* **Type II (Clifford torus)** — a flat torus with two generating circles, carrying $\vartheta_3$ transition densities and GUE statistics. *Bottom right:* **Type III (Pseudo-Anosov)** — a saddle surface with negative curvature. Five Brownian paths launched from the same point diverge exponentially.

---

<p align="center">
  <img src="code/visualisation/curvature_profiles.png" width="100%" alt="Mean curvature profiles across the three market types"/>
</p>

**The Sharpe ratio is curvature.** The central identity: $\mathrm{Sharpe}^{\ast} = \|H\|_{L^2}$.

---

## The Central Identity

$$\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(M,\, g_M)}$$

The maximum achievable Sharpe ratio equals the RMS mean curvature of the
market manifold. Slope = 1.007 ± 0.18, p = 10⁻⁸ on empirical data.

---

## The Single Organising Principle

> *A financial market is a minimal submanifold $M^r$ of the Bhattacharyya sphere
> $S^{d-1}_+$. Portfolio weights are barycentric coordinates on $\Delta_{d-1}$.
> Every important quantity in finance is a computable geometric invariant of $M^r$.*

This is now a theorem, not an axiom. Five axioms of convex information
processing (closure, data processing inequality, continuity, normalisation,
Markov compatibility) force the Fisher-Rao metric as the unique geometry.
The market manifold, the Bhattacharyya sphere, and the simplex are
**mathematical necessities**.

---

## Five Headline Results

1. **Sharpe = curvature** — the alpha budget is the mean curvature of the market manifold
2. **Only CAPMs are stably efficient** — Clifford torus stability index = 5 (explains LTCM's five simultaneous failure modes)
3. **MUP regret $r \log T / 2T$** — 12× improvement over Cover's universal portfolio, minimax optimal
4. **Palindromic = No Arbitrage** — six equivalent conditions: palindromic cycles ⟺ detailed balance ⟺ no arbitrage ⟺ time-reversibility ⟺ zero Berry phase ⟺ Gibbs measure
5. **The manifold IS the channel** — the Fokker-Planck kernel is a DMC with capacity $h_{\rm Kelly}$; the Fisher-Rao metric of the channel equals the metric of the manifold

---

## Three Results for the Publisher

1. **Sharpe = curvature, slope = 1.007 ± 0.18, p = 10⁻⁸** (predictive, out-of-sample)
2. **Fisher-Rao distance explains 98.6% of cross-sectional returns** (R² = 0.986)
3. **Yield curve inversion predicted all 3 recessions** (3/3 perfect)

---

## The Full Algebraic Chain

The deepest structure in the monograph. Every arrow is canonical — no choices, no parameters:

```
Voronoi cells → de Bruijn graph (= the filtration at depth n)
    → de Bruijn sequence (= optimal exploration of the simplex)
    → Chen-Fox-Lyndon factorisation (= unique decomposition into Lyndon words)
    → Free Lie algebra (= Lyndon words are the basis)
    → Shuffle Hopf algebra (= Radford's theorem: sequential ⊗ parallel strategies)
    → Palindromic sub-algebra (= fixed points of the antipode = time-reversal)
    → Detailed balance (= no arbitrage)
```

The directed graph IS the market. The Hopf algebra IS the space of all
strategies. The palindromic condition IS efficiency.

---

## Complete Paper Inventory (62 papers)

### Part 0: Foundations (9 papers)

| Paper | Core result |
|:------|:-----------|
| `CONVEX_INFORMATION.md` | **Convex Information Processing Theorem** — five axioms force the Fisher-Rao simplex |
| `CONVEXIFICATION.md` | Six convexification operators including palindromic completion; mandatory alpha for hyperbolic markets |
| `DUAL_TOWER.md` | Giry monad tower; spectral duals; factor structure = representation theory |
| `INCOMPLETENESS.md` | Three walls of market knowledge: σ-algebra, Turing, Gödel; filtration incompleteness theorem |
| `HOPF_FIBRATION_MIXING.md` | Hopf fibration = factor projection; Dyson class = Hopf type |
| `INFORMATION_INTELLIGENCE_KNOWING.md` | All computation on manifolds; intelligence = dimension; five limits of knowing |
| `UNITS.md` | Complete catalogue of units and scaling; rules for empirical tests |
| `LIGHTCONE_OF_PRICE.md` | **Lorentzian market spacetime; lightcones; insider = wider lightcone; proper time = risk-adjusted return** |
| `MANIFOLD_IS_THE_CHANNEL.md` | **The manifold IS the channel; self-referential channels; Gödelian tower; Landauer bound; geometry-information-logic triangle** |

### Part I: Core Theory (5 papers)

| Paper | Core result |
|:------|:-----------|
| `LAPLACE.md` | WKB = Laplace; $O(1/T^2)$ accuracy; Van Vleck = Fisher matrix |
| `FK_SIMPLEX.md` | Feynman-Kac on the simplex; stochastic Stokes theorem; replicator-diffusion equation |
| `MINIMAL_SURFACE.md` | **Sharpe* = ‖H‖**; EMH = minimal surface; Willmore = inefficiency |
| `CLASSIFICATION.md` | Only CAPMs stably efficient; Clifford torus index = 5; six dimensionless market numbers |
| `CONVERGENCE.md` | MUP regret $r\log T/2T$; minimax optimal via Shtarkov NML |

### Part II: Physics and Processes (7 papers)

| Paper | Core result |
|:------|:-----------|
| `INFORMATION_THEORY.md` | SMB = Kelly; six equivalent characterisations of efficiency |
| `HAMILTONIAN_TAILS_COMPLETENESS.md` | Market Hamiltonian; fat tails $\alpha = r/2$; completeness = normal bundle |
| `MARKET_PROCESSES.md` | Exact SDEs per topology: Jacobi, $\vartheta_3$ torus BM, McKean hyperbolic BM |
| `DERIVATIVES_CONVEXITY.md` | Geometric Black-Scholes; vol skew = curvature |
| `RENORMALIZATION.md` | Market = RG critical point; MCF = RG flow; Willmore = $c$-function |
| `FOKKER_PLANCK_CFD.md` | FP stationary = Jeffreys prior; Voronoi = Markov partition; Reynolds number |
| `WHY_MARKETS_DO_EVOLVE...md` | **Five stages of market efficiency; crises = MCF singularities** |

### Part III: Topology and Computation (5 papers)

| Paper | Core result |
|:------|:-----------|
| `FIBER_BUNDLES.md` | Parallel transport = optimal hedge update; Berry phase; topological alpha |
| `KNOT_THEORY.md` | Jones polynomial = market partition function; Alexander = factor rotation |
| `BRAIDS.md` | Yang-Baxter = no-arbitrage; Turing completeness |
| `COMPLEXITY.md` | #**P**-hardness; Martin-Löf randomness; prediction complexity hierarchy |
| `FILTRATIONS.md` | **LZ78/BWT/CFL three canonical filtrations; palindrome-arbitrage theorem; de Bruijn = filtration; Radford-Hopf algebra; everything is a directed graph** |

### Part IV: New Domains (12 papers)

| Paper | Core result |
|:------|:-----------|
| `LLM_MANIFOLD.md` | LMSR = softmax = Fisher; LLM ≤ MUP (proved); Kelly = min cross-entropy |
| `RANDOM_MATRIX.md` | Dyson class forced by geometry; Selberg = MUP; Tracy-Widom |
| `PATH_INTEGRAL.md` | Constrained geometric Wiener measure on $M^r$; WKB = LAPLACE |
| `CHAOS_TAKENS.md` | Chaos ≡ stochastic on $M^r$; Takens $m^{\ast}=2r+1$ |
| `HYPERCUBE_SHAPLEY.md` | **Shapley $\phi_i = b^{\ast}_i(\mu_i - \bar\mu)$ (proved)** |
| `GRASSBERGER_PERCOLATION_GENERATING.md` | Correlation dim $\nu=r$; transfer matrix = everything |
| `SVD_MANIFOLD.md` | SVD preserves mean curvature locally |
| `STOCHASTIC_CONTROL_KALMAN.md` | Manifold Kalman filter; Riccati = Fisher |
| `CREDIT_RISK.md` | **Default = Feller boundary; credit spread = $1/(2d^2_{\rm FR})$** |
| `NETWORK_INFORMATION_THEORY.md` | **$R_{\rm conv} = \min(\lambda_1, C)$; insider trading accelerates efficiency** |
| `OBSERVERS_AND_CHANNELS.md` | **Shared filtrations; ambient shortcuts; optimal inefficiency $\mathcal{W}^{\ast} > 0$** |
| `FOREIGN_EXCHANGE.md` | **One manifold, $N$ currencies; carry = mean curvature; triangular arb = palindromic deficit** |

### Part V: Financial Applications (8 papers)

| Paper | Core result |
|:------|:-----------|
| `PORTFOLIO_GEOMETRY.md` | Portfolio construction from surface type; manifold Black-Litterman |
| `SOBOLEV_OPTIONS_GREEKS.md` | Weighted Sobolev; geometric Greeks; Feller = diversification |
| `MARTINGALE_GEOMETRY.md` | EMM space = normal bundle; Doob-Meyer = Willmore |
| `PAIRS_TRADING.md` | Geometric entry $z^{\ast} = \sqrt{1+r/\kappa}$ |
| `BETTER_INDEX_FUND.md` | Cap-weighting is suboptimal; Manifold Index Fund |
| `INTERMARKET_GEOMETRY.md` | **Mergers = connected sums; payback = neck width × regret** |
| `FIXED_INCOME_YIELD_CURVES.md` | **Nelson-Siegel = Jacobi eigenmodes; inversion = winding number** |
| `VOLATILITY_SURFACE.md` | **Vol surface as Riemannian manifold; VVIX = Willmore energy** |

### Part VI: Accessible (7 papers)

| Paper | Core result |
|:------|:-----------|
| `HORSE_RACING_SPORTS_BETTING_GAMBLING.md` | Edge = Fisher-Rao displacement; Kelly on races = MUP |
| `PREDICTION_MARKETS.md` | LMSR = softmax = Fisher-Rao; scoring rule uniqueness |
| `ART_MARKET.md` | Permanently inefficient: negative curvature forces $\|H\| > 0$ |
| `INFLATION_CAPITAL_FLOWS.md` | Geometric inflation; Fisher equation = holonomy |
| `CONFIDENCE.md` | **Confidence IS a σ-algebra; fourth wall of incompleteness; fear = σ-algebra contraction** |
| `BLOODSTOCK_MARKETS.md` | **Wright-Fisher = Jacobi (identity, not analogy); BWT/CFL on genomes; palindromes on DNA; discipline projections** |
| `FISHERIES_MARKETS.md` | **Coupled simplices; MSY = Kelly rate; ITQ = reflecting boundary; UNCLOS = Voronoi; the Port Lincoln case** |

### Part VII: Political Economy (4 papers)

| Paper | Core result |
|:------|:-----------|
| `TOPOLOGY_OF_PRICE.md` | **Price = graph Laplacian eigenvector; deadweight loss = Willmore** |
| `EMU_CASE_STUDY.md` | **The Euro as connected sum; the Greek crisis was a theorem** |
| `SECURITIES_LAW_REFORM.md` | **Ten geometric reforms; insider trading helps; regulatory inversion** |
| `IMPOSSIBILITY_OF_CENTRAL_ALLOCATION.md` | **Central planning fails because it collapses the σ-algebra** |

### Part VIII: Empirical (2 papers) + Methods

| Paper | Core result |
|:------|:-----------|
| `REAL_DATA_EXPERIMENTS.md` | **29 tests, 57% pass rate; three headline results; "here's how to kill the theory"** |
| `MARKET_MICROSTRUCTURE.md` | **LOB = measure-valued process; bid-ask = Fisher-Rao distance** |
| `CFD_METHODS.md` | DMD, POD-Galerkin, spectral elements for market simulation |

---

### `navigation/` — Reference Documents

- `ABSTRACT.md` — publisher overview
- `EXECUTIVE_SUMMARY.md` — complete six-layer summary
- `WHATS_NEW.md` — 130+ numbered results across six tiers
- `CONJECTURES.md` — 30 graded conjectures
- `OPEN_PROBLEMS.md` — 50+ open problems with difficulty ratings
- `SERIES_PLAN.md` — publication strategy and monograph chapter map

### `book/` — Accessible Content

- `EXPERIMENTS.md` — replication experiments with Python code
- `ANECDOTES.md` — two centuries of financial history through the geometric lens
- `SO_WHATS.md` — plain English guide for portfolio managers (no equations)
- `ADDENDUM.md` — 46 additional lemmas
- `MASTER_PLAN.md` — roadmap and monograph structure
- `SESSION_3_PLAN.md` — plan for next working session

### `tools/` — Infrastructure

- `fix_markdown.py` — fixes GitHub rendering issues (escaped underscores, bare asterisks, #P notation); run after writing any new paper

### `code/` — Open-Source Implementation

```
code/
├── core/            kelly.py, fisher_rao.py, curvature.py
├── shapley/         kelly_shapley.py
├── experiments/     29 replication experiments
├── visualisation/   market_manifolds.py, simplex_explorer.py, 8 interactive HTMLs
├── cfd/             DMD, POD-Galerkin
├── mup/             Manifold Universal Portfolio
├── processes/       Jacobi, theta function, McKean diffusions
├── kalman/          Manifold Kalman-Bucy filter
├── takens/          Delay embedding, FNN, diffusion maps
├── filtrations/     LZ78, CTW, Voronoi automaton
├── pairs/           Geometric pairs trading (C++)
├── contagion/       Cheeger constant, crisis detection
├── rmt/             Dyson class test, Tracy-Widom
└── cpp/             C++20 Universal Portfolio engine
```

---

## Key Identities (Quick Reference)

```
Sharpe-curvature:    Sharpe* = ||H||_{L²(M)}
Palindrome-arb:      ∀ cycles γ: δ(γ) = 0  ⟺  no arbitrage  ⟺  detailed balance
Channel capacity:    C(market) = h_Kelly   (the manifold IS the channel)
Fat tails:           α = r/2
MUP regret:          r·log(T) / (2T)
Pairs entry:         z* = sqrt(1 + r/κ)
Shapley:             φ_i = b*_i · (μ_i - μ̄)
Kelly = min loss:    min_θ L(θ) = h_Kelly   [any ML model on public data]
Insider alpha:       α = ε²|v_G|            [v_G ∈ normal bundle]
MSY = Kelly:         H_MSY = h_Kelly(Δ^P)   [fisheries]
Wright-Fisher:       = Jacobi diffusion      [ε² = 1/(2N_e)]
Credit spread:       s ≈ 1/(2·d²_FR)
Willmore decomp:     W = W_structural + W_Landauer + W_confidence + W_excess
Confidence:          C_eff = ρ̄ · C_full     [ρ̄ = aggregate confidence ratio]
De Bruijn depth:     n* = ⌊log_N T⌋         [max testable memory depth]
Relay capacity:      C_relay = ½log(1 + W/W_min)   [Willmore = SNR]
Berry phase:         ∮_γ A = palindromic deficit δ(γ)
```

---

## For the Non-Mathematician

Start with `book/SO_WHATS.md` — a plain-English guide with no equations.
Why the market has a shape. Why your index fund is suboptimal. Why LTCM had
exactly five ways to fail. Why insider trading laws are geometrically
backwards. Why confidence is the most important variable in economics and
it's a σ-algebra.

---

## For the Practitioner

| Result | What to do with it |
|:-------|:------------------|
| $\phi_i = b^{\ast}_i(\mu_i - \bar\mu)$ | Fair attribution of P&L to assets |
| Cheeger constant $h_M \to 0$ before crises | Early warning systemic risk indicator |
| Palindrome ratio $\mathcal{P}_k$ | Model-free efficiency test at any timescale |
| Optimal entry $z^{\ast} = \sqrt{1 + r/\kappa}$ | Replace the 2σ pairs trading rule |
| De Bruijn depth $n^{\ast} = \lfloor\log_N T\rfloor$ | Maximum testable memory depth for your data |
| Willmore decomposition | Separate tradeable alpha from structural/Landauer/confidence costs |

---

## For the Regulator

The **Ten Geometric Reforms** from `SECURITIES_LAW_REFORM.md`:

1. Deprioritise insider trading prosecution (it accelerates efficiency)
2. Mandate 60-second disclosure (every hour of delay costs Willmore energy)
3. Never ban short-selling (it's MCF in the negative curvature direction)
4. Dynamic circuit breakers calibrated to the spectral gap
5. Consolidated real-time order books across all venues
6. Tax latency arbitrage, not market-making speed
7. Open IPOs to all investors from day one
8. Heavy penalties for misinformation (double the damage of insider trading)
9. Mandatory machine-readable ESG (one number: tonnes CO2e)
10. Stage-dependent crypto regulation (classify by geometric maturity)

---

## Empirical Scorecard

**29 tests run · 57% pass rate · Three headline results**

| Verdict | Count | Examples |
|:--------|:-----:|:--------|
| **PASS** | 12 | Sharpe = curvature (bootstrap), Fisher-Rao distance explains returns (R² = 0.986), yield inversion → recession (3/3) |
| MARGINAL | 10 | Spectral gap, LZ symbolic, bid-ask = Fisher-Rao, FX spot triangular |
| FAIL | 7 | Vol surface (stale data), FX carry (needs carry adjustment), Laplace rate |

Full details: `data/results/RESULTS.md` and `REAL_DATA_EXPERIMENTS.md`.

---

## What Would Kill the Theory

We are explicit about falsification:

- If Sharpe does NOT correlate with estimated mean curvature → the central theorem is wrong
- If the manifold dimension $r$ is unstable across estimation methods → the manifold model is too rigid
- If the MUP does NOT outperform Cover → the dimension reduction doesn't work
- If eigenvalue spacings match NONE of GOE/GUE/GSE → the Dyson correspondence is wrong
- If every cycle on the Voronoi partition is palindromic but arbitrage exists → the palindrome theorem is wrong

29 tests. Free data. Open code. The theory stands or falls on the evidence.

---

## Status

| Metric | Count |
|:-------|:-----:|
| Papers | 62 |
| Total words | ~400,000 |
| Proved results (Tier 1-2) | 50+ |
| Conjectures (graded A/B/C) | 30 |
| Open problems | 50+ |
| Falsifiable empirical tests | 29 |
| Policy reforms derived | 10 |
| Interactive visualisations | 8 |
| Code modules | 15+ |

---

## Citation

```bibtex
@book{nicholls2026geometry,
  author    = {Nicholls, Saxon Herschel},
  title     = {The Geometry of Efficient Markets},
  subtitle  = {Minimal Surfaces, Universal Portfolios, and the
               Mathematics of Financial Markets},
  year      = {2026},
  note      = {Preprint. github.com/saxonnicholls/geometry-of-efficient-markets}
}
```

---

*"The geometry was always there. In the fish market. In the cattle yards.
In the grain silos. In the desert, where there is nothing between you and
the thing itself. The mathematics gave it a name. The simplex gave it
coordinates. The Fisher-Rao metric gave it a distance. The directed graph
gave it a skeleton. But the skeleton was always there."*

*— For Port Lincoln*
