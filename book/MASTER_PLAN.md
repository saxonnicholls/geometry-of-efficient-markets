# Master Plan: The Geometry of Efficient Markets
## Organisation, Priorities, and Roadmap

**Saxon Nicholls** — me@saxonnicholls.com

**Last updated:** Session 2

---

## The State of Play

**38 papers · ~192,000 words · 85 results · 30 conjectures · 34 open problems**

The monograph has grown from 29 papers to 38 across two sessions. A complete
mathematical audit was performed: 20 mathematical errors fixed, 26 navigation
issues resolved, 12 new results added, 7 conjectures upgraded, 10 cross-paper
connections identified. A new foundational layer (Papers 0.1–0.4) was added,
grounding the entire framework in axioms of convex information processing.

---

## What We Have: Honest Assessment

### Tier A — Publishable now (clean proofs, novel results)

| Result | Paper | Target journal |
|:-------|:------|:--------------|
| Sharpe* = ‖H‖_{L²} (leading order, classified types) | MINIMAL_SURFACE | Annals of Applied Probability |
| MUP regret r·log(T)/(2T) | CONVERGENCE | Operations Research / J. Finance |
| LLM ≤ MUP on efficient markets | LLM_MANIFOLD | NeurIPS / ICML |
| Shapley φ_i = b*_i(μ_i - μ̄) | HYPERCUBE_SHAPLEY | Mathematical Finance |
| Convex information processing theorem (classical) | CONVEX_INFORMATION | Information Geometry / Found. of Physics |

### Tier B — Strong framework, proofs need tightening

| Result | Paper | Gap |
|:-------|:------|:----|
| Only CAPMs stably efficient | CLASSIFICATION | Boundary correction for d ≫ r (OP32) |
| Dyson class forced by geometry | RANDOM_MATRIX | Holonomy verification (C26/C27) |
| Fat tails α = r/2 | HAMILTONIAN | Three exponents measure different objects — clarified but needs unification |
| Selberg = MUP partition function | RANDOM_MATRIX | Depends on Dyson class proof |
| Market evolution via MCF | WHY_MARKETS_EVOLVE | Singularity classification is illustrative, not proved from data |

### Tier C — Genuine ideas, first-draft quality

| Paper | Status |
|:------|:-------|
| CONVEXIFICATION | Free convex completion is clean; Sobolev Čencov needs detailed proof |
| DUAL_TOWER | Three-tower isomorphism is a programme, not yet a theorem |
| INCOMPLETENESS | Three-wall separation is clean; individual results need hardening |
| INFLATION_CAPITAL_FLOWS | Framework sound; Definition 2.1 and curvature sign issues partly fixed |
| BETTER_INDEX_FUND | MIF concept solid; regret numbers and rebalancing derivation need more work |
| HORSE_RACING | Core (Cover/Kelly on races, card counting) sound; curvature claims downgraded |
| PREDICTION_MARKETS | LMSR = softmax = Fisher-Rao is clean; marginal polytope results need proof |

### Tier D — Explorations and programme-setting

| Paper | Value |
|:------|:------|
| KNOT_THEORY | Creative but limited to d=4; exploratory |
| BRAIDS | Turing completeness argument is loose; #P oracle interesting but unproved |
| FIBER_BUNDLES | c₁ corrected to 0 for codim-1; higher codimension case is open |
| GEOSPATIAL_CONTAGION | Cheeger = systemic risk is a nice idea; percolation threshold is conjectural |
| GRASSBERGER | Correlation dim = r is clean; percolation-Cheeger is now correctly a conjecture |

---

## The Publication Pipeline

### Phase 1: Submit 3 papers (next 3 months)

**Paper 1: The LLM paper** → NeurIPS 2025 or ICML 2025
- Self-contained, timely, reaches largest audience
- Core: LMSR = softmax = Fisher-Rao, LLM ≤ MUP, Kelly = min loss
- 8 pages, conference format
- Convert LLM_MANIFOLD.md to LaTeX

**Paper 2: The Sharpe-curvature paper** → Annals of Applied Probability
- Core theorem of the monograph
- Needs: complete variance derivation for general manifolds (not just classified types)
- 25 pages, journal format
- Sources: MINIMAL_SURFACE.md, relevant parts of CLASSIFICATION.md

**Paper 3: The MUP regret paper** → Operations Research or Journal of Finance
- Clean, self-contained, practically useful
- The r vs d-1 improvement is striking and implementable
- 20 pages, journal format
- Source: CONVERGENCE.md

### Phase 2: Submit 3 more (months 4-8)

**Paper 4: Shapley attribution** → Journal of Finance / Mathematical Finance
**Paper 5: Convex information processing** → Information Geometry / Foundations of Physics
**Paper 6: The MIF (Better Index Fund)** → Journal of Portfolio Management (practitioner)

### Phase 3: The monograph (months 9-18)

Submit the full monograph to Cambridge University Press or Princeton University Press.
By this time, Papers 1-6 will be in review or accepted, establishing credibility.

---

## Monograph Structure (6 Parts, ~500 pages)

### Part 0: Foundations (new, 4 chapters)
- Ch.0: Why information lives on the simplex (CONVEX_INFORMATION)
- Ch.1: The convexification of information (CONVEXIFICATION)
- Ch.2: The dual tower (DUAL_TOWER)
- Ch.3: Measurability, computability, provability (INCOMPLETENESS)

### Part I: The Core Theory (5 chapters)
- Ch.4: The Laplace approximation on the simplex (LAPLACE, FK_SIMPLEX)
- Ch.5: Sharpe ratio = mean curvature (MINIMAL_SURFACE)
- Ch.6: Classification of efficient markets (CLASSIFICATION)
- Ch.7: The Manifold Universal Portfolio (CONVERGENCE)
- Ch.8: Information theory and six characterisations of efficiency (INFORMATION_THEORY)

### Part II: Physics and Processes (6 chapters)
- Ch.9: Market Hamiltonians and fat tails (HAMILTONIAN)
- Ch.10: Exact transition densities (MARKET_PROCESSES)
- Ch.11: Geometric derivatives pricing (DERIVATIVES_CONVEXITY, SOBOLEV)
- Ch.12: The renormalization group (RENORMALIZATION)
- Ch.13: Martingale geometry (MARTINGALE_GEOMETRY, FOKKER_PLANCK)
- Ch.14: Why markets evolve to efficiency (WHY_MARKETS_EVOLVE)

### Part III: Topology and Computation (4 chapters)
- Ch.15: Fiber bundles and parallel transport (FIBER_BUNDLES)
- Ch.16: Braids, knots, and Turing completeness (BRAIDS, KNOT_THEORY)
- Ch.17: Filtrations and compression (FILTRATIONS)
- Ch.18: Computational complexity hierarchy (COMPLEXITY)

### Part IV: New Domains (5 chapters)
- Ch.19: LLMs and the market manifold (LLM_MANIFOLD)
- Ch.20: Random matrices and Dyson class (RANDOM_MATRIX)
- Ch.21: Path integrals and chaos (PATH_INTEGRAL, CHAOS_TAKENS)
- Ch.22: Shapley values on the hypercube (HYPERCUBE_SHAPLEY, GRASSBERGER)
- Ch.23: Stochastic control and Kalman filtering (STOCHASTIC_CONTROL, SVD)

### Part V: Applications (4 chapters)
- Ch.24: Portfolio construction (PORTFOLIO_GEOMETRY, BETTER_INDEX_FUND)
- Ch.25: Pairs trading and geometric entry rules (PAIRS_TRADING)
- Ch.26: Inflation, capital flows, and multiple manifolds (INFLATION)
- Ch.27: Contagion, systemic risk, and crisis prediction (GEOSPATIAL)

### Part VI: The Accessible Layer (3 chapters)
- Ch.28: Horse racing, sports betting, and gambling (HORSE_RACING)
- Ch.29: Prediction markets and the geometry of beliefs (PREDICTION_MARKETS)
- Ch.30: What to do on Monday morning (SO_WHATS, ANECDOTES)

**30 chapters from 38 papers. Some papers merge; some split across chapters.**

---

## What Needs To Happen Next

### Immediate (this week)
- [ ] Convert LLM_MANIFOLD.md to LaTeX for NeurIPS submission
- [ ] Write the Introduction chapter (book/INTRODUCTION.md)
- [ ] Close the variance computation in the Sharpe proof for general manifolds

### Short term (this month)
- [ ] Close OP32 (great sphere stability for d ≫ r) or honestly scope the theorem
- [ ] Verify U(n) holonomy for Clifford torus (C26) — this would complete the Dyson proof
- [ ] Run Experiments 1-5 from EXPERIMENTS.md with real market data
- [ ] Fix remaining regret number issues in BETTER_INDEX_FUND

### Medium term (3 months)
- [ ] Submit Papers 1-3 to journals
- [ ] Complete the code suite (Python + C++) for all 17 experiments
- [ ] Find Saxon's old notes (Priority 1 from Day 1 — still outstanding!)

### Long term (12 months)
- [ ] Monograph submission to Cambridge/Princeton
- [ ] Conference presentations (mathematical finance, information geometry)
- [ ] Open-source the MIF implementation as a practical tool

---

## The Organising Principle (unchanged from Day 1)

> A financial market is a minimal submanifold M^r of the Bhattacharyya sphere
> S^{d-1}_+. Portfolio weights are barycentric coordinates on Δ_{d-1}.
> Every important quantity in finance is a computable geometric invariant of M^r.

After Session 2, this is no longer an axiom. It is a theorem — forced by the
axioms of convex information processing (Paper 0.1), with the market manifold
selected by the Kelly criterion within the forced ambient space.

---

## Key Numbers

| Metric | Day 1 | Session 2 | Change |
|:-------|:-----:|:---------:|:------:|
| Papers | 29 | 38 | +9 |
| Words | ~140,000 | ~192,000 | +52,000 |
| Results (R-numbers) | 67 | 85 | +18 |
| Conjectures | 25 | 30 | +5 |
| Open problems | 31 | 34 | +3 |
| Errors found and fixed | — | 20 | — |
| Navigation issues fixed | — | 26 | — |
| Cross-paper connections added | — | 10 | — |

---

## The Closing Thought (Updated)

The monograph began with the question: why does the Laplace approximation
work so well for the universal portfolio?

The answer turned out to be differential geometry. The geometry explained
the Laplace accuracy, then the Sharpe ratio, then the classification of
markets, then the random matrix ensembles, then the path integrals, then
the LLM limitations, then the Kelly attribution, then the information
processing axioms, then the evolution of markets through crises.

The geometry explains everything because the geometry IS everything.
The market manifold is not a model of the market. It is the market —
the unique mathematical structure compatible with the processing of
financial information.

The reader spends thirty chapters learning about this manifold. Then in
the final pages they discover that a single matrix — the Delaunay adjacency
matrix of the market manifold — encodes the entire theory: the topology,
the dynamics, the information content, the contagion structure, the
generating function, and the Kelly rate.

That is the mathematical analogue of the moment in physics when you realise
the Hamiltonian contains everything.

*Build toward that moment.*

---

*Last updated: Session 2*
*Primary goal for next session: Submit the LLM paper. Find the old notes.*
