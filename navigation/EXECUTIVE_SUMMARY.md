# The Geometry of Efficient Markets — Executive Summary
## 35 Papers · ~145,000 Words · 25+ Proved Results

**Saxon Nicholls** — me@saxonnicholls.com

---

## The Single Organising Principle

A financial market is a minimal submanifold $M^r$ of the Bhattacharyya sphere
$S^{d-1}\_+$. Portfolio weights are barycentric coordinates on $\Delta\_{d-1}$.
Every important quantity in finance is a computable geometric invariant of $M^r$.

This single sentence explains: why Cover's prior works; why only CAPMs are stable;
why fat tails are power-law; why LTCM had exactly five failure modes; why no LLM
can beat the MUP; why the appropriate random matrix ensemble is determined by the
manifold, not the modeller; and why the path integral you priced derivatives with
was using the wrong measure.

---

## Six Layers of the Theory

### 1 · FK-WKB Foundation *(LAPLACE, PAPER)*
Cover's integral is a Feynman-Kac functional on $(\Delta\_{d-1},g^{\rm FR})$.
WKB saddle = geodesic. Van Vleck determinant = Fisher information matrix.
$O(1/T^2)$ accuracy = Jeffreys prior = stationary distribution of the market diffusion.
This closes a 30-year gap in Cover's theory.

### 2 · The Market Manifold and Its Classification *(MINIMAL\_SURFACE, CLASSIFICATION, CONVERGENCE)*
Bhattacharyya isometry: $b\mapsto\sqrt{b}\in S^{d-1}\_+$, curvature $K=1/4$.
**Sharpe = curvature** (proved): $\mathrm{Sharpe}^{\ast}=\|H\|\_{L^2(M)}$.
**Only CAPMs stable** (proved): Simons-Lawson-Simons, stability index of Clifford torus = 5.
**MUP minimax** (proved): regret $r\log T/2T$ vs Cover's $(d-1)\log T/2T$.

### 3 · Physics, Processes, Measure Theory *(HAMILTONIAN, FOKKER\_PLANCK, MARKET\_PROCESSES, SOBOLEV, MARTINGALE, DERIVATIVES, RENORMALIZATION, INFORMATION\_THEORY)*
Fat tails $\alpha=r/2$ (three independent proofs). FP stationary = Jeffreys prior.
Exact processes: Jacobi (CAPM), $\vartheta\_3$ (Clifford torus), McKean (hyperbolic).
Doob-Meyer compensator = Willmore energy. Optimal stopping = MUP posterior.
Diversification proved via Feller boundary. Geometric vol smile without SV.
RG: CAPM = IR fixed point; Willmore = $c$-function; running Sharpe formula.

### 4 · Topology, Computation, Filtrations *(KNOT\_THEORY, BRAIDS, FIBER\_BUNDLES, COMPLEXITY, FILTRATIONS)*
Knot type classifies markets. Jones polynomial = market partition function.
Alexander roots = factor rotation eigenvalues. Yang-Baxter = no braiding arbitrage.
**P**/#**P**/Π₂⁰/PPAD prediction hierarchy.
LZ prefix tree = filtration tree (proved; any compressor = valid filtration).
Clifford torus winding number = momentum vs contrarian (topological classifier).

### 5 · Geospatial, Contagion, LLMs, RMT, Path Integrals *(GEOSPATIAL, LLM\_MANIFOLD, RANDOM\_MATRIX, PATH\_INTEGRAL)*
H3/S2/Hilbert on $S^{d-1}\_+$; contagion network = Delaunay graph (endogenous);
Cheeger = systemic risk.
LMSR = softmax = Fisher (transformer attention = market making in Fisher-Rao geometry).
LLM≤MUP (no architecture beats the MUP); optimal dim = $r$; Kelly rate = min loss.
Dyson $\beta\in\{1,2,4\}$ forced by manifold symmetry; Selberg = MUP partition function;
TW $F\_\beta$ = largest eigenvalue; Vandermonde = diversification pressure.
Path integral on $M^r$: WKB=LAPLACE, $\vartheta\_3$=winding sum, McKean=unique geodesic,
$\mathbb{P}=\mathbb{Q}$ on efficient $M$, normal bundle integral = incompleteness premium.

### 6 · Chaos, Embedding, Hypercubes, Shapley *(CHAOS\_TAKENS, HYPERCUBE\_SHAPLEY)*
Chaos $\equiv$ stochastic on $M^r$ (Oseledets — unobservable and irrelevant distinction).
Feigenbaum $\delta=4.669$ governs CAPM-to-pA bifurcation.
Takens: single return series in $\mathbb{R}^{2r+1}$ recovers $M^r$ topology.
Optimal delay $\tau=1/\lambda\_1$. Three-step algorithm: embed→diffusion maps→$M^r$.
$\Delta\_{d-1}\subset[0,1]^d$; Walsh functions = Jacobi polynomials; barycentric = Voronoi.
**Shapley** $\phi\_i = b^{\ast}\_i(\mu\_i-\bar\mu)$ (proved — unique fair Kelly attribution).
Banzhaf = Walsh-Fourier coefficient. Normal bundle Shapley = unexplained alpha.

---

## Complete Paper Inventory (35 documents)

| # | Document | Layer | Status |
|:-:|:---------|:-----:|:------:|
| 1 | LAPLACE | 1 | Proved |
| 2 | PAPER | 1 | Proved |
| 3 | MINIMAL\_SURFACE | 2 | Proved |
| 4 | CLASSIFICATION | 2 | Proved |
| 5 | CONVERGENCE | 2 | Proved |
| 6 | INFORMATION\_THEORY | 3 | Proved |
| 7 | SVD\_MANIFOLD | 3 | Proved |
| 8 | DERIVATIVES\_CONVEXITY | 3 | Proved |
| 9 | HAMILTONIAN\_TAILS\_COMPLETENESS | 3 | Proved |
| 10 | RENORMALIZATION | 3 | Conjectural elements |
| 11 | PORTFOLIO\_GEOMETRY | 3 | Proved |
| 12 | FIBER\_BUNDLES | 4 | Proved/Conjectural |
| 13 | KNOT\_THEORY | 4 | Conjectural elements |
| 14 | BRAIDS | 4 | Proved/Conjectural |
| 15 | COMPLEXITY | 4 | Proved |
| 16 | MARTINGALE\_GEOMETRY | 3 | Proved |
| 17 | FOKKER\_PLANCK\_CFD | 3 | Proved |
| 18 | MARKET\_PROCESSES | 3 | Proved |
| 19 | SOBOLEV\_OPTIONS\_GREEKS | 3 | Proved |
| 20 | PAIRS\_TRADING | 5 | Proved |
| 21 | FILTRATIONS | 4 | Proved |
| 22 | GEOSPATIAL\_CONTAGION | 5 | Proved/Conjectural |
| 23 | LLM\_MANIFOLD | 5 | Proved |
| 24 | RANDOM\_MATRIX | 5 | Proved |
| 25 | PATH\_INTEGRAL | 5 | Proved |
| 26 | CHAOS\_TAKENS | 6 | Proved/Conjectural |
| 27 | HYPERCUBE\_SHAPLEY | 6 | Proved |
| 28 | EXPERIMENTS | App | Open-source |
| 29 | ANECDOTES | App | Historical |
| 30 | WHATS\_NEW | Nav | Reference |
| 31 | CONJECTURES | Nav | Reference |
| 32 | OPEN\_PROBLEMS | Nav | Reference |
| 33 | SERIES\_PLAN | Nav | Reference |
| 34 | ABSTRACT | Nav | Publisher |
| 35 | EXECUTIVE\_SUMMARY | Nav | This doc |

---

## The Five Most Important Results

1. **Sharpe = curvature** — the alpha budget is observable from options data, now
2. **Only CAPMs stable** — LTCM's five failure modes were a theorem from 1973
3. **LLM ≤ MUP** — no compute or architecture can beat the MUP on an efficient market
4. **Dyson class is forced** — the random matrix ensemble is a geometric theorem, not a choice
5. **Shapley = Fisher-Rao gradient** — unique fair attribution of Kelly growth to assets, proved

## The Five Most Surprising

1. **LZ tree = filtration** — running a compressor builds the filtration atom by atom
2. **Transformer = market maker** — the LMSR and transformer attention are the same equation
3. **Selberg = MUP** — one of the deepest integrals in mathematics IS the portfolio partition function
4. **Chaos ≡ stochastic on $M$** — the distinction between deterministic and random markets is unobservable
5. **Takens from one series** — the whole market manifold hides in a single stock's return series

---

## Tomorrow's Agenda

Organise the 35 papers into their final monograph structure. Add results from the
first author's unpublished notes (filtration extensions, symbolic dynamics, others).
Update SERIES\_PLAN with the new Part V and Part VI structure.
Begin drafting the monograph Part I introduction connecting all layers.

*"The market teaches the same lessons over and over.
The geometry tells us why."*
