# The Geometry of Efficient Markets

**Saxon Nicholls** — me@saxonnicholls.com

*Minimal Surfaces, Universal Portfolios, and the Mathematics of Financial Markets*

**51 papers · ~281,000 words · 85+ results · 30 conjectures · 34 open problems**

> **PREPRINT** — This is a working draft. None of these papers have been peer-reviewed.
> Comments, corrections, and collaboration inquiries welcome: me@saxonnicholls.com

---

## The Three Market Types

<p align="center">
  <img src="code/visualisation/market_manifolds.png" width="100%" alt="The three classified market manifold types in the Bhattacharyya sphere"/>
</p>

**The classification theorem in one picture.** Every efficient market falls into one of three geometric types, each living as a submanifold of the Bhattacharyya sphere $S^{d-1}_+$. *Top left:* the ambient space — the positive octant of the unit sphere, where $\sqrt{b}$ coordinates give the Fisher-Rao isometry. *Top right:* **Type I (CAPM)** — a great circle (geodesic) with a Jacobi diffusion path mean-reverting around the log-optimal portfolio. This is the only stably efficient type. *Bottom left:* **Type II (Clifford torus)** — a flat torus with two generating circles, carrying $\vartheta_3$ transition densities and GUE statistics. Stability index = 5. *Bottom right:* **Type III (Pseudo-Anosov)** — a saddle surface with negative curvature. Five Brownian paths launched from the same point diverge exponentially, illustrating the chaotic dynamics governed by the McKean kernel and GSE statistics.

---

<p align="center">
  <img src="code/visualisation/curvature_profiles.png" width="100%" alt="Mean curvature profiles across the three market types"/>
</p>

**The Sharpe ratio is curvature.** The mean curvature $|H|^2$ profile across each manifold type determines the exploitable alpha. *Left:* CAPM — an efficient market ($H = 0$, blue line) versus an inefficient perturbation (blue shading). *Centre:* Clifford torus — curvature is periodic (the torus winding), creating rhythmic alpha opportunities. *Right:* Pseudo-Anosov — curvature varies exponentially due to geodesic divergence. The central identity: $\mathrm{Sharpe}^{\ast} = \|H\|_{L^2}$.

---

<p align="center">
  <img src="code/visualisation/classification_table.png" width="100%" alt="Classification table of the three market types"/>
</p>

**Everything is determined by the geometry.** The manifold type forces the stochastic process, the transition density, the random matrix ensemble ($\beta \in \{1,2,4\}$), the tail behaviour, and the entropy. The S&P 500 is a CAPM great sphere. A balanced two-sector economy is a Clifford torus. A crisis or regime change is pseudo-Anosov.

---

## The Central Theorem

$$\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(M,\, g_M)}$$

The maximum achievable Sharpe ratio equals the RMS mean curvature of the
market manifold. The vol skew of index options measures $H$ in real time.

---

## Five Key Results

1. **Sharpe = curvature** — the alpha budget is observable from options data now
2. **Only CAPMs are stably efficient** (closed manifolds; boundary case is OP32) — explains why LTCM had exactly five simultaneous failure modes (the Clifford torus stability index is 5)
3. **MUP regret $r \log T / 2T$** — 12× improvement over Cover's universal portfolio, minimax optimal
4. **Dyson class is forced by geometry** (conditional — see RANDOM_MATRIX.md Theorem 1.1) — the random matrix ensemble for an efficient market is a theorem, not a modelling choice
5. **No LLM beats the MUP** — on an efficient market, more compute and more data never help (proved)

---

## The Foundation: Convex Information Processing

> *Any system that communicates (closure), that cannot create information from
> nothing (data processing inequality), and that responds continuously to its
> inputs must operate on a geodesically convex subset of the Fisher-Rao simplex.
> The geometry is not a choice — it is a mathematical necessity.*

This is Paper 0.1 (CONVEX_INFORMATION.md). The market manifold, the
Fisher-Rao metric, and the Bhattacharyya sphere are **theorems**, not
assumptions. They are forced by five axioms (three information axioms plus
normalisation and Markov channels) that no reasonable information processing
system can violate.

## The Single Organising Principle

> *A financial market is a minimal submanifold $M^r$ of the Bhattacharyya sphere
> $S^{d-1}_+$. Portfolio weights are barycentric coordinates on $\Delta_{d-1}$.
> Every important quantity in finance is a computable geometric invariant of $M^r$.*

This single sentence — now a theorem, not an axiom — explains: why Cover's
prior works; why only CAPMs are stable; why fat tails are power-law with
exponent $\alpha = r/2$; why LTCM had exactly five failure modes; why no
LLM can beat the MUP; why the appropriate random matrix ensemble is
determined by the manifold; and why the path integral for derivative pricing
was using the wrong measure.

---

## Complete Paper Inventory (51 papers)

### Part 0: Foundations (6 papers)

| Paper | Core result |
|:------|:-----------|
| `CONVEX_INFORMATION.md` | **Convex Information Processing Theorem** — five axioms force the Fisher-Rao simplex |
| `CONVEXIFICATION.md` | Free convex completion $\mathcal{P}(X)$; Sobolev Čencov; mandatory alpha for hyperbolic markets |
| `DUAL_TOWER.md` | Giry tower, spectral duals, finite group constructions; factor structure = representation theory |
| `INCOMPLETENESS.md` | Three walls of market knowledge: σ-algebra, Turing, Gödel; filtration incompleteness theorem |
| `HOPF_FIBRATION_MIXING.md` | Hopf fibration = factor projection; Dyson class = Hopf type; pseudo-Anosov is most efficiently mixing |
| `INFORMATION_INTELLIGENCE_KNOWING.md` | All computation on manifolds; intelligence = dimension; consciousness = Giry tower; five limits of knowing |

### Part I: Core Theory (5 papers)

| Paper | Core result |
|:------|:-----------|
| `LAPLACE.md` | WKB = Laplace; $O(1/T^2)$ accuracy for posterior mean (ratio cancellation); Van Vleck = Fisher matrix |
| `FK_SIMPLEX.md` | Feynman-Kac on the simplex; stochastic Stokes theorem; replicator-diffusion equation |
| `MINIMAL_SURFACE.md` | **Sharpe\* = ‖H‖ (leading order, exact for classified types)**; EMH = minimal surface; Willmore = inefficiency |
| `CLASSIFICATION.md` | Only CAPMs stably efficient (closed manifolds; boundary case OP32); Clifford torus index = 5; Veronese |
| `CONVERGENCE.md` | MUP regret $r\log T/2T$; minimax optimal; weak form unconditional, strong form under regularity |

### Part II: Physics and Processes (7 papers)

| Paper | Core result |
|:------|:-----------|
| `INFORMATION_THEORY.md` | SMB = Kelly; six equivalent characterisations of efficiency; mixing = Jacobi eigenvalue |
| `HAMILTONIAN_TAILS_COMPLETENESS.md` | Market Hamiltonian; three distinct tail exponents (portfolio/return/RG); completeness = normal bundle |
| `MARKET_PROCESSES.md` | Exact SDEs per topology: Jacobi, $\vartheta_3$ torus BM, McKean hyperbolic BM |
| `DERIVATIVES_CONVEXITY.md` | Geometric Black-Scholes; vol skew = curvature; heat kernel orders option prices by topology |
| `RENORMALIZATION.md` | Market = RG critical point; MCF = RG flow; Willmore = $c$-function; CAPM = IR fixed point |
| `FOKKER_PLANCK_CFD.md` | FP stationary = Jeffreys prior; Voronoi = Markov partition; Reynolds number for markets |
| `WHY_MARKETS_DO_EVOLVE...md` | **Five stages of market efficiency; crises = MCF singularities; why central planning fails** |

### Part III: Topology and Computation (5 papers)

| Paper | Core result |
|:------|:-----------|
| `FIBER_BUNDLES.md` | Parallel transport = optimal hedge update; Berry phase; topological alpha (codimension ≥ 2) |
| `KNOT_THEORY.md` | Jones polynomial = market partition function; Alexander = factor rotation (d=4 only) |
| `BRAIDS.md` | Market as braiding machine; Yang-Baxter = no-arbitrage; Turing completeness; #**P** oracle |
| `COMPLEXITY.md` | #**P**-hardness; Martin-Löf randomness; prediction complexity hierarchy |
| `FILTRATIONS.md` | **General prefix trie = filtration (proved for prefixwise compressors)**; SFT; LZ78 = Kelly rate |

### Part IV: New Domains (10 papers)

| Paper | Core result |
|:------|:-----------|
| `LLM_MANIFOLD.md` | LMSR = softmax = Fisher; LLM ≤ MUP (proved); Kelly = min cross-entropy loss |
| `RANDOM_MATRIX.md` | Dyson class correspondence (conditional); Selberg = MUP; Tracy-Widom edge fluctuations |
| `PATH_INTEGRAL.md` | Constrained geometric Wiener measure on $M^r$; WKB = LAPLACE; $\vartheta_3$ = winding sum |
| `CHAOS_TAKENS.md` | Chaos ≡ stochastic on $M^r$; Takens $m^{\ast}=2r+1$; diffusion maps algorithm |
| `HYPERCUBE_SHAPLEY.md` | **Shapley $\phi_i = b^{\ast}_i(\mu_i - \bar\mu)$ (proved)**; Walsh = Jacobi polynomials |
| `GRASSBERGER_PERCOLATION_GENERATING.md` | Correlation dim $\nu=r$; percolation threshold (conjecture); transfer matrix = everything |
| `SVD_MANIFOLD.md` | SVD preserves mean curvature locally; pseudoinverse duality |
| `STOCHASTIC_CONTROL_KALMAN.md` | Manifold Kalman filter; Riccati = Fisher; geodesic execution; two-fund separation |
| `CREDIT_RISK.md` | **Default = Feller boundary; credit spread = 1/(2d²_FR); CDOs = fiber bundles; 2008 = mass absorption** |
| `NETWORK_INFORMATION_THEORY.md` | **R_conv = min(λ₁, C); insider trading accelerates efficiency; misinformation costs double** |

### Part V: Financial Applications (8 papers)

| Paper | Core result |
|:------|:-----------|
| `PORTFOLIO_GEOMETRY.md` | Portfolio construction from surface type; manifold Black-Litterman; rebalancing from spectral gap |
| `SOBOLEV_OPTIONS_GREEKS.md` | Weighted Sobolev; mollifiers; exact option pricing; geometric Greeks; Feller = diversification |
| `MARTINGALE_GEOMETRY.md` | EMM space = normal bundle; Doob-Meyer = Willmore; BSDE driver = Kelly |
| `PAIRS_TRADING.md` | Geometric entry $z^{\ast} = \sqrt{1+r/\kappa}$; OU = Jacobi projected to spread |
| `BETTER_INDEX_FUND.md` | Cap-weighting is suboptimal; Manifold Index Fund; optimal rebalancing = spectral gap |
| `INTERMARKET_GEOMETRY.md` | **Parity manifold; spreads = O'Neill curvature; mergers = connected sums; payback formula** |
| `FIXED_INCOME_YIELD_CURVES.md` | **Nelson-Siegel = Jacobi eigenmodes; term premium = curvature; inversion = winding number transition** |
| `VOLATILITY_SURFACE.md` | **Vol surface as Riemannian manifold; no-arb = curvature bounds; VVIX = Willmore energy** |

### Part VI: Accessible (4 papers)

| Paper | Core result |
|:------|:-----------|
| `HORSE_RACING_SPORTS_BETTING_GAMBLING.md` | Edge = Fisher-Rao displacement; Kelly on races = MUP; card counting = Kalman filter |
| `PREDICTION_MARKETS.md` | LMSR = softmax = Fisher-Rao; marginal polytopes; scoring rule uniqueness |
| `ART_MARKET.md` | Permanently inefficient manifold (negative curvature forces ‖H‖ > 0); fractionalisation theorem |
| `INFLATION_CAPITAL_FLOWS.md` | Geometric inflation; capital flows = connection; Fisher equation = holonomy |

### Part VII: Political Economy (3 papers)

| Paper | Core result |
|:------|:-----------|
| `TOPOLOGY_OF_PRICE.md` | **Price = graph Laplacian eigenvector; deadweight loss = Willmore; famine = Cheeger failure** |
| `EMU_CASE_STUDY.md` | **The Euro as connected sum; k/r payback formula; the Greek crisis was a theorem** |
| `SECURITIES_LAW_REFORM.md` | **Ten geometric reforms; insider trading helps; misinformation costs double; regulatory inversion** |

### Part VIII: Empirical (2 papers)

| Paper | Core result |
|:------|:-----------|
| `REAL_DATA_EXPERIMENTS.md` | **20 falsifiable tests with free data; scoring system; "here's how to kill the theory"** |
| `MARKET_MICROSTRUCTURE.md` | **LOB = measure-valued process; bid-ask = Fisher-Rao distance; flash crash = MCF singularity** |

---

### `navigation/` — Reference Documents

- `ABSTRACT.md` — publisher overview
- `EXECUTIVE_SUMMARY.md` — complete six-layer summary
- `WHATS_NEW.md` — 85+ numbered results across six tiers (including Tier 0: Foundational)
- `CONJECTURES.md` — 30 graded conjectures (C18 general trie now partially proved)
- `OPEN_PROBLEMS.md` — 34 open problems with difficulty ratings
- `SERIES_PLAN.md` — publication strategy and monograph chapter map

### `book/` — Accessible Content

- `EXPERIMENTS.md` — 10 detailed replication experiments with Python code
- `ANECDOTES.md` — two centuries of financial history through the geometric lens
- `SO_WHATS.md` — plain English guide for portfolio managers (no equations), including the insider trading vignettes and Ten Geometric Reforms
- `ADDENDUM.md` — 46 additional lemmas from systematic review
- `MASTER_PLAN.md` — roadmap, publication pipeline, and monograph structure

### `code/` — Open-Source Implementation

```
code/
├── core/            kelly.py, fisher_rao.py, curvature.py
├── shapley/         kelly_shapley.py
├── experiments/     experiment_01 through experiment_17
├── visualisation/   market_manifolds.py (generates the figures above)
├── mup/             Manifold Universal Portfolio
├── processes/       Jacobi, theta function, McKean diffusions
├── kalman/          Manifold Kalman-Bucy filter
├── takens/          Delay embedding, FNN, diffusion maps
├── filtrations/     LZ78, CTW, Voronoi automaton
├── pairs/           Geometric pairs trading (C++)
├── contagion/       Cheeger constant, crisis detection
├── rmt/             Dyson class test, Tracy-Widom
└── cpp/             C++20 Universal Portfolio engine (Laplace/MC/QMC/Factor/EG)
                     with ImGui dashboard and paper trading execution
```

---

## Quick Start

```bash
# Install dependencies
pip install -r code/requirements.txt

# Test the core
python code/core/kelly.py
python code/core/fisher_rao.py
python code/core/curvature.py

# Run the central experiment
# Tests: Sharpe*(Sigma) = ||H||_{L^2}
python code/experiments/experiment_01_sharpe_curvature.py

# Kelly attribution
python code/shapley/kelly_shapley.py

# Generate the visualisations
python code/visualisation/market_manifolds.py
```

---

## For the Non-Mathematician

Start with `book/SO_WHATS.md` — a plain-English guide written in the style
of Buffett and Munger's investing vignettes. No equations. Actionable things
a portfolio manager can do differently on Monday morning. Includes:
why the market has a shape, why your index fund is suboptimal, why LTCM had
exactly five ways to fail, and why insider trading laws are geometrically
backwards.

---

## For the Practitioner

The five most immediately useful results:

| Result | What to do with it |
|:-------|:------------------|
| $\phi_i = b^{\ast}_i(\mu_i - \bar\mu)$ | Fair attribution of P&L to assets — `code/shapley/` |
| Cheeger constant $h_M \to 0$ before crises | Early warning systemic risk indicator — `code/contagion/` |
| Optimal entry $z^{\ast} = \sqrt{1 + r/\kappa}$ | Replace the 2σ pairs trading rule — `code/pairs/` |
| Kalman gain $K = F(b^{\ast})^{-1}V_r^TR_N^{-1}$ | Optimal signal extraction — `code/kalman/` |
| Kelly rate = minimum ML loss | Calibrate any market model — `code/transformer/` |

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

## Key Identities (Quick Reference)

```
Sharpe-curvature:    Sharpe* = ||H||_{L²(M)}
Fat tails:           α_return = r/2    (α_portfolio = Tb*_i - 1/2)
MUP regret:          r·log(T) / (2T)        vs Cover: (d-1)·log(T)/(2T)
Pairs entry:         z* = sqrt(1 + r/κ)
Shapley:             φ_i = b*_i · (μ_i - μ̄)
Kelly loss:          min_θ L(θ) = h_Kelly   [for any ML model on public data]
Insider alpha:       α = ε²|v_G|_{g^FR}    where v_G ∈ N_{b*}M
Selberg = MUP:       Z_T^M = S_r(T·b*-½, T·b*-½, β/2)
Dyson class:         CAPM→GOE, Clifford T²→GUE, pseudo-Anosov→GSE
Credit spread:       s ≈ 1/(2·d²_FR(b, ∂Δ))  (inverse square of distance to default)
Term premium:        TP(τ) = H(γ_t, τ)  (mean curvature of yield curve)
Vol smile:           σ(k) ∝ |H|² in strike direction
Bid-ask spread:      s_FR = d_{g^FR}(b^bid, b^ask)
Convergence rate:    R_conv = min(λ₁, C)   (geometric vs network bottleneck)
Contagion network:   = Delaunay graph of M^r  (endogenous, not exogenous)
Takens dimension:    m* = 2r+1              (from single return series)
Merger payback:      T_payback ≈ W_neck · 2T / (k · log T)
Euler eligibility:   V - E + F = χ(M)      (lattice constraint on contagion graph)
```

---

## The Scope: From Axioms to Milliseconds

| Level | Papers | What it covers |
|:------|:------:|:---------------|
| **Axioms** | 0.1–0.6 | Why the geometry is forced; convexification; duality; incompleteness; intelligence |
| **Core theory** | I.1–I.5 | Laplace, Sharpe=curvature, classification, MUP regret, information theory |
| **Physics** | II.1–II.6 | Hamiltonians, processes, derivatives, RG flow, Fokker-Planck, market evolution |
| **Topology** | III.1–III.5 | Fiber bundles, knots, braids, complexity, filtrations, Hopf fibration |
| **New domains** | IV.1–IV.10 | LLMs, random matrices, path integrals, chaos, Shapley, credit, yield curves, vol surface, microstructure, network information |
| **Applications** | V.1–V.8 | Portfolios, options, martingales, pairs, index funds, intermarket spreads, fixed income, volatility |
| **Accessible** | VI.1–VI.4 | Gambling, prediction markets, art, inflation |
| **Political economy** | VII.1–VII.3 | Topology of price, EMU autopsy, securities law reform |
| **Empirical** | VIII.1 | 20 falsifiable tests on real data |

---

## Citation

```bibtex
@book{nicholls2026geometry,
  author    = {Nicholls, Saxon},
  title     = {The Geometry of Efficient Markets},
  subtitle  = {Minimal Surfaces, Universal Portfolios, and the
               Mathematics of Financial Markets},
  year      = {2026},
  note      = {Preprint. Available at github.com/saxonnicholls/geometry-of-efficient-markets}
}
```

---

## Status

| Metric | Count |
|:-------|:-----:|
| Mathematical papers | 51 |
| Total words | ~281,000 |
| Foundational results (Tier 0) | 2 |
| Proved results (Tier 1) | 26 |
| Proved with mild assumptions (Tier 2) | 17+ |
| Conjectures (graded A/B/C) | 30 |
| Open problems | 34 |
| Falsifiable empirical tests | 20 |
| Historical case studies | 8 |
| Policy reforms derived | 10 |
| Code modules (Python) | 11 |
| Code modules (C++20) | 6 |

---

## What Would Kill the Theory

We are explicit about falsification (REAL_DATA_EXPERIMENTS.md):

- If Sharpe does NOT correlate with estimated mean curvature → the central theorem is wrong
- If the manifold dimension $r$ is unstable across estimation methods → the manifold model is too rigid
- If the MUP does NOT outperform Cover → the dimension reduction doesn't work in practice
- If eigenvalue spacings match NONE of GOE/GUE/GSE → the Dyson correspondence is wrong

Twenty tests. Free data. Open code. The theory stands or falls on the evidence.

---

*"The geometry of efficient markets is not about markets. It is about the
geometry of knowing — the unique mathematical structure compatible with the
processing of information by any system, biological or artificial, that
communicates, that cannot create something from nothing, and that responds
continuously to the world."*
