# CLAUDE.md
## Complete Context for Continuing "The Geometry of Efficient Markets"
## VS Code + GitHub Session — Day 2 and Beyond

---

## Who You Are Talking To

Saxon is an investor, entrepreneur, and mathematician based in the Southern
Highlands of NSW, Australia. He has deep expertise in mathematical finance,
derivatives pricing (including Feynman path integrals), and has been working
on this monograph across an extended session. He is direct, technically fluent,
and prefers frank assessment over validation. He will tell you when something
is wrong.

**Critical fact:** Saxon has unpublished notes from approximately 15 years ago
that contain, at minimum, the general prefix trie / filtration theorem (the
LZ78 case of which is incorporated as R14 in this monograph). These notes may
contain additional results in filtration theory and symbolic dynamics. Finding
and incorporating these notes is **Priority 1** for Day 2.

---

## What This Project Is

A mathematical monograph titled **"The Geometry of Efficient Markets"** with
subtitle *"Minimal Surfaces, Universal Portfolios, and the Mathematics of
Financial Markets."* 

**The single organising principle:**
A financial market is a minimal submanifold $M^r$ of the Bhattacharyya sphere
$S^{d-1}_+$. Portfolio weights are barycentric coordinates on the simplex
$\Delta_{d-1}$. Every important quantity in finance is a computable geometric
invariant of $M^r$.

**Current state:** 36 documents, ~143,000 words, 67 numbered results (26 fully
proved), 25 conjectures, 31 open problems.

**Target publication:** Cambridge University Press or Princeton University Press.
~460-500 pages, six parts, 21 chapters.

---

## The Repository Structure

All papers are Markdown files. On Day 1 they were created in a Claude computer
environment. They should now live in a GitHub repository. Suggested structure:

```
geometry-of-efficient-markets/
├── CLAUDE.md                    ← THIS FILE (project context for AI)
├── README.md                    ← Public-facing description
├── papers/
│   ├── LAPLACE.md
│   ├── PAPER.md
│   ├── MINIMAL_SURFACE.md
│   ├── CLASSIFICATION.md
│   ├── CONVERGENCE.md
│   ├── INFORMATION_THEORY.md
│   ├── SVD_MANIFOLD.md
│   ├── DERIVATIVES_CONVEXITY.md
│   ├── HAMILTONIAN_TAILS_COMPLETENESS.md
│   ├── RENORMALIZATION.md
│   ├── PORTFOLIO_GEOMETRY.md
│   ├── FIBER_BUNDLES.md
│   ├── KNOT_THEORY.md
│   ├── BRAIDS.md
│   ├── COMPLEXITY.md
│   ├── MARTINGALE_GEOMETRY.md
│   ├── FOKKER_PLANCK_CFD.md
│   ├── MARKET_PROCESSES.md
│   ├── SOBOLEV_OPTIONS_GREEKS.md
│   ├── PAIRS_TRADING.md
│   ├── FILTRATIONS.md
│   ├── GEOSPATIAL_CONTAGION.md
│   ├── LLM_MANIFOLD.md
│   ├── RANDOM_MATRIX.md
│   ├── PATH_INTEGRAL.md
│   ├── CHAOS_TAKENS.md
│   ├── HYPERCUBE_SHAPLEY.md
│   └── GRASSBERGER_PERCOLATION_GENERATING.md
├── navigation/
│   ├── ABSTRACT.md
│   ├── EXECUTIVE_SUMMARY.md
│   ├── SERIES_PLAN.md
│   ├── WHATS_NEW.md
│   ├── CONJECTURES.md
│   └── OPEN_PROBLEMS.md
├── book/
│   ├── ANECDOTES.md
│   ├── EXPERIMENTS.md
│   └── INTRODUCTION.md          ← TO BE WRITTEN DAY 2
├── code/
│   ├── core/                    ← Kelly, Fisher-Rao, curvature
│   ├── mup/                     ← Manifold Universal Portfolio
│   ├── processes/               ← Jacobi, theta function, McKean
│   ├── transformer/             ← Dimension estimation, Kelly benchmark
│   ├── takens/                  ← Delay embedding, FNN, diffusion maps
│   ├── filtrations/             ← LZ78, CTW, BWT
│   ├── pairs/                   ← Geometric pairs trading
│   ├── contagion/               ← Cheeger, Delaunay, crisis detection
│   ├── rmt/                     ← Dyson class test, Tracy-Widom
│   ├── shapley/                 ← Kelly Shapley attribution
│   └── experiments/             ← 17 replication experiments
└── CLAUDE.md
```

---

## The Mathematical Framework (Essential Reference)

### Setup
- $d$ assets, $r$ systematic factors ($r \ll d$, typically $r\approx4$–$8$)
- Portfolio simplex: $\Delta_{d-1} = \{b\in\mathbb{R}^d_+ : \sum b_i = 1\}$
- Fisher-Rao metric: $g^{\rm FR}_{ij}(b) = \delta_{ij}/b_i$
- Bhattacharyya isometry: $\phi: b\mapsto\sqrt{b}\in S^{d-1}_+$ (curvature $K=1/4$)
- Market manifold: $M^r\subset S^{d-1}_+$, the $r$-dimensional submanifold of log-optimal portfolios over all factor shock realisations
- WF diffusion parameter: $\varepsilon^2 = 1/T$
- Log-optimal portfolio: $b^* = \arg\max_{b\in M^r}L_T(b)$ where $L_T(b) = \frac{1}{T}\sum_t\log\langle b,x_t\rangle$

### The Three Market Types (Proved Classification)
| Type | Manifold | Process | Transition density | $\beta$ |
|:-----|:---------|:--------|:-------------------|:-------:|
| CAPM | $S^r_+$ (great sphere) | Jacobi diffusion | Jacobi polynomial series | 1 (GOE) |
| Two-factor balanced | $T^2$ (Clifford torus) | Flat torus BM | $\vartheta_3$ (theta function) | 2 (GUE) |
| Pseudo-Anosov | $\mathbb{H}^2$ (hyperbolic) | Hyperbolic BM | McKean kernel | 4 (GSE) |

### The Five Most Important Proved Results
1. $\mathrm{Sharpe}^* = \|H\|_{L^2(M,g_M)}$ — Sharpe ratio = RMS mean curvature
2. Only CAPMs are stably efficient (Clifford torus stability index = 5)
3. MUP regret $r\log T/(2T)$ — minimax optimal, 12× improvement over Cover
4. Dyson class $\beta\in\{1,2,4\}$ is forced by manifold symmetry — not a modelling choice
5. Shapley attribution $\phi_i = b^*_i(\mu_i-\bar\mu)$ — unique fair Kelly attribution

### Key Equations (Quick Reference)
```
Sharpe-curvature:    Sharpe* = ||H||_{L²}
Fat tails:           α_i = T·b*_i - 1/2  (also α = r/2)
MUP regret:          r·log(T)/(2T)  vs Cover: (d-1)·log(T)/(2T)
Pairs entry:         z* = sqrt(1 + r/κ)
Kelly loss:          min_θ L(θ) = h_Kelly(b*)  [for any ML model]
Insider alpha:       α = ε²|v_G|_{g^FR}  where v_G ∈ N_{b*}M
Selberg = MUP:       Z_T^M = S_r(T·b*-1/2, T·b*-1/2, β/2)
Shapley:             φ_i = b*_i · (μ_i - μ̄)
Connective const:    μ_SAW = exp(h_Kelly)
GF pole:             x_c = exp(-h_Kelly)
Grassberger dim:     ν = r  (correlation dimension = manifold dimension)
Percolation:         p_c ≈ h_M  (threshold ≈ Cheeger constant)
Euler eligibility:   V - E + F = χ(M)  (lattice constraint)
Takens dimension:    m* = 2r+1  (minimum faithful embedding)
Optimal delay:       τ = 1/λ₁  (Jacobi spectral gap)
```

---

## Complete Paper Inventory with One-Line Summaries

### Core Theory
**LAPLACE.md** — WKB = Laplace; FK on simplex; $O(1/T^2)$ accuracy from Jeffreys prior = stationary distribution

**PAPER.md** — FK formula on simplex; stochastic Stokes theorem with curvature correction $\varepsilon^2(d-2)/4$

**MINIMAL\_SURFACE.md** — $\mathrm{Sharpe}^* = \|H\|_{L^2}$ (proved); EMH conjecture; Willmore = inefficiency

**CLASSIFICATION.md** — Only CAPMs stably efficient (Simons-Lawson-Simons); Clifford torus stability index = 5

**CONVERGENCE.md** — MUP regret $r\log T/2T$; minimax optimal via Shtarkov NML; 12× improvement

### Physics and Processes
**INFORMATION\_THEORY.md** — SMB = Kelly; 6 equivalent characterisations of efficiency; mixing = Jacobi eigenvalue

**SVD\_MANIFOLD.md** — SVD preserves mean curvature locally; pseudoinverse duality for minimal surfaces

**DERIVATIVES\_CONVEXITY.md** — Geometric Black-Scholes; vol skew = $H^2$; vol-of-vol = Willmore energy

**HAMILTONIAN\_TAILS\_COMPLETENESS.md** — Market Hamiltonian; fat tails 3 ways ($\alpha=r/2$); completeness = normal bundle

**RENORMALIZATION.md** — Market = RG critical point; MCF = RG flow; Willmore = $c$-function; CAPM = IR fixed point

**PORTFOLIO\_GEOMETRY.md** — Portfolio construction from surface type; manifold Black-Litterman; rebalancing from spectral gap

**FOKKER\_PLANCK\_CFD.md** — FP stationary = Jeffreys prior; Voronoi = Markov partition; Reynolds number for markets

**MARKET\_PROCESSES.md** — Exact SDEs per topology: Jacobi, $\vartheta_3$ torus BM, McKean hyperbolic BM

**SOBOLEV\_OPTIONS\_GREEKS.md** — Weighted Sobolev; mollifiers; exact option pricing; geometric Greeks; Feller = diversification

**MARTINGALE\_GEOMETRY.md** — EMM space = normal bundle; Doob-Meyer = Willmore; BSDE driver = Kelly; optimal stopping = MUP

**DERIVATIVES\_CONVEXITY.md** — Geometric BS; vol skew = curvature; geometric vol smile (hyperbolic)

### Topology and Computation
**FIBER\_BUNDLES.md** — Parallel transport = optimal hedge update; Berry phase; Chern classes; topological alpha

**KNOT\_THEORY.md** — Jones polynomial = market partition function; topological EMH; Alexander = factor rotation

**BRAIDS.md** — Market as braiding machine; Yang-Baxter = no-arbitrage; pseudo-Anosov; Turing completeness

**COMPLEXITY.md** — #P-hardness; Martin-Löf randomness; Rule 110; prediction complexity hierarchy

**FILTRATIONS.md** — Geometric filtration; Voronoi atoms explicitly constructed; LZ prefix tree = filtration tree; Clifford winding number

### New Domains (Day 1 Afternoon/Evening)
**GEOSPATIAL\_CONTAGION.md** — H3/S2/Hilbert on $S^{d-1}_+$; contagion = Delaunay graph; Cheeger = systemic risk; Hawkes criticality

**LLM\_MANIFOLD.md** — LMSR = softmax = Fisher; LLM ≤ MUP (proved); optimal dim = $r$; Kelly loss = min cross-entropy; insider in normal bundle

**RANDOM\_MATRIX.md** — Dyson class forced by manifold symmetry; Selberg = MUP; Tracy-Widom $F_\beta$; Vandermonde = diversification

**PATH\_INTEGRAL.md** — Constrained geometric Wiener measure on $M^r$; WKB = LAPLACE; $\vartheta_3$ = winding sum; McKean = geodesic; $\mathbb{P}=\mathbb{Q}$ on efficient $M$

**CHAOS\_TAKENS.md** — Chaos ≡ stochastic on $M^r$ (Oseledets); Feigenbaum $\delta$ at bifurcation; Takens $m^*=2r+1$; diffusion maps algorithm

**HYPERCUBE\_SHAPLEY.md** — $\Delta_{d-1}\subset[0,1]^d$; Walsh = Jacobi polynomials; barycentric = Voronoi; Shapley $\phi_i = b^*_i(\mu_i-\bar\mu)$ (proved)

**GRASSBERGER\_PERCOLATION\_GENERATING.md** — Correlation dim $\nu=r$; percolation threshold $p_c\approx h_M$; Euler eligibility; Wilf GF pole at $e^{-h_{\rm Kelly}}$; transfer matrix IS everything

### Navigation and Book
**ABSTRACT.md** — Publisher overview (~1200 words)  
**EXECUTIVE\_SUMMARY.md** — Complete summary with all 6 layers  
**SERIES\_PLAN.md** — Publication strategy: 6 parts, 21 chapters, 19 papers, timeline  
**WHATS\_NEW.md** — 67 numbered results across 5 tiers  
**CONJECTURES.md** — 25 graded conjectures (12 Grade A, 12 Grade B, 1 Grade C)  
**OPEN\_PROBLEMS.md** — 31 open problems with difficulty ratings  
**ANECDOTES.md** — Historical episodes: LTCM, 2008, Buffett, Rothschild, LDI, etc.  
**EXPERIMENTS.md** — 10 (soon 17) open-source replication experiments  

---

## Day 2 Priority List

### Priority 1 — Non-negotiable
**Find and incorporate Saxon's old notes.**
Expected content: general prefix trie filtration proof, symbolic dynamics results.
When found: each result goes into WHATS\_NEW.md (Tier 1 if proved, CONJECTURES otherwise).
The general trie filtration theorem (C17 in CONJECTURES.md) is Grade A and ★★ difficulty
— the LZ78 proof in FILTRATIONS.md guides it directly.

### Priority 2 — High value, doable in hours
**Write INTRODUCTION.md** — the Part I opening chapter (~3,000 words).
This is what determines whether a publisher commissions the book.
Structure:
1. The Laplace approximation question (the origin)
2. The single organising principle
3. Reader's guide to six parts
4. Five main theorems, one paragraph each
5. What is proved vs conjectural (honest accounting)
6. Positioning relative to Amari, Cover-Thomas, Karatzas-Shreve, Fernholz

### Priority 3 — Important for submission
**Add Experiments 11–17** to EXPERIMENTS.md:
11: Dyson class ratio test; 12: Tracy-Widom fit; 13: Takens FNN;
14: Diffusion maps manifold estimation; 15: Shapley attribution;
16: Grassberger correlation dimension; 17: Transformer dimension test.

### Priority 4 — Structural
**Write MONOGRAPH\_STRUCTURE.md** — chapter-by-chapter outline with:
- Which papers contribute to which chapter
- Word count targets per chapter
- Content that needs to be merged (e.g. PATH\_INTEGRAL overlaps LAPLACE)
- Identified gaps

### Priority 5 — Submission prep
**Draft Paper E** (LLM/LMSR) for NeurIPS/ICML — 8-page conference paper.
This is the most immediately submittable paper and reaches the largest audience.

---

## Results That Might Be in the Old Notes

Based on what Saxon has described, the old notes likely contain one or more of:

1. **General prefix trie = filtration (C17):** Proved for any grammar-based
   compressor — LZ77, LZW, CTW, PPM, BWT. The key argument: any dictionary
   compressor maintains a set of "seen phrases" = non-empty filtration atoms.
   
2. **CTW posterior = MUP posterior:** The Rissanen-Willems Context Tree Weighting
   algorithm is the Bayesian optimal sequence compressor. Its posterior weights
   on context trees = MUP posterior restricted to Markov model class.

3. **Symbolic dynamics results:** Possibly including the symbolic Takens embedding
   or results on the sofic shift structure of specific market types.

4. **Other filtration theory:** Possibly results on the winding number filtration,
   the relation between filtration complexity and Kolmogorov complexity, or
   connections to symbolic dynamics on non-compact manifolds.

When reading old notes: if a result is proved, assign it an R-number in WHATS\_NEW.md.
If it is a conjecture with evidence, assign it a C-number in CONJECTURES.md.
If it opens a new direction, assign it an OP-number in OPEN\_PROBLEMS.md.

---

## Key Connections That Should Not Be Lost

These are conceptual connections that emerged during Day 1 that are not yet fully
formalised but are important:

**1. The transfer matrix IS everything (Section 4.2, GRASSBERGER):**
The Delaunay adjacency matrix $A$ simultaneously IS: the Voronoi automaton of
FILTRATIONS.md; the Guttman-Brak transfer matrix; the Wilf generating function
coefficient matrix; the Markov chain linearisation. Its Perron-Frobenius eigenvalue
$\rho(A) = e^{h_{\rm Kelly}}$ appears identically in all traditions.

**2. Three independent estimators of $r$:**
(i) Stable rank of Fisher information matrix (rolling covariance);
(ii) False Nearest Neighbours algorithm on delay-embedded return series (Takens);
(iii) Grassberger-Procaccia correlation dimension of embedded return series.
All three should converge to the same $r$. Comparing them is a practical test.

**3. Three independent estimators of $h_{\rm Kelly}$:**
(i) Direct log-wealth maximisation (the MUP);
(ii) LZ complexity rate (from FILTRATIONS.md);
(iii) Grassberger $K_2$ correlation entropy.
All three should converge to the same value. A paper comparing these would be valuable.

**4. The LDI crisis as Feller boundary failure:**
Leverage pushes effective portfolio weights above 1, exiting the simplex, removing
the Jacobi restoring force. The Bank of England's intervention = pushing the process
back inside the simplex. Clean, precise, and testable on 2022 gilt data.

**5. The Feigenbaum bifurcation as a leading indicator:**
The ratio of successive Jacobi eigenvalue spacings should approach $\delta=4.669$
as the market approaches the CAPM-to-pseudo-Anosov bifurcation. This is a
theoretically-motivated early warning indicator not yet tested empirically.

**6. The path integral and the original practitioner experience:**
Saxon priced derivatives using Feynman path integrals. The key insight from
PATH\_INTEGRAL.md: the measure was correct in structure but wrong — it was over
all of $\mathbb{R}^d$ rather than $M^r$. The Van Vleck prefactor = Fisher matrix
is the precise connection between the old calculation and the new theory.

---

## Mathematical Notation Conventions

Used consistently throughout all papers:

| Symbol | Meaning |
|:-------|:--------|
| $d$ | Number of assets |
| $r$ | Market manifold dimension (number of factors) |
| $T$ | Number of time periods |
| $\varepsilon^2 = 1/T$ | WF diffusion parameter |
| $b = (b_1,\ldots,b_d)$ | Portfolio weights |
| $b^*$ | Log-optimal portfolio |
| $M^r$ | Market manifold |
| $g^{\rm FR}$ | Fisher-Rao metric |
| $g_M$ | Induced metric on $M^r$ |
| $H$ | Mean curvature vector of $M^r$ in $S^{d-1}_+$ |
| $\vec{H}$ | Mean curvature vector (normal direction) |
| $\mathcal{W}(M) = \int H^2 d\mathrm{vol}_M$ | Willmore energy |
| $\lambda_1(L_M)$ | Jacobi spectral gap (= Fiedler eigenvalue of $L_M$) |
| $h_M$ | Cheeger constant of $M^r$ |
| $h_{\rm Kelly}$ | Kelly growth rate = topological entropy |
| $L_T(b)$ | Kelly growth rate function |
| $W_T(b) = e^{TL_T(b)}$ | Wealth function |
| $\hat{b}^M_T$ | MUP portfolio |
| $TM$, $NM$ | Tangent and normal bundles of $M^r$ |
| $\Pi_{TM}$, $\Pi_{NM}$ | Projections onto $TM$ and $NM$ |
| $\mathcal{F}^M_t$ | Manifold filtration |
| $\mathcal{F}^{\rm Vor}_t$ | Voronoi filtration |
| $\mathcal{F}^{\rm oracle}_t$ | Oracle (insider) filtration |
| $\beta \in \{1,2,4\}$ | Dyson symmetry class |
| $F_\beta$ | Tracy-Widom distribution |
| $S_n(a,b,\gamma)$ | Selberg integral |
| $\vartheta_3$ | Jacobi theta function |
| $K_{T^2}$ | Flat torus heat kernel |
| $K_{\mathbb{H}^2}$ | McKean hyperbolic heat kernel |
| $\phi_i$ | Shapley value of asset $i$ |
| $\chi(M)$ | Euler characteristic of $M^r$ |
| $\mathcal{D}(M)$ | Delaunay graph of market manifold |
| $A_{ij}$ | Delaunay adjacency matrix |
| $\rho(A)$ | Perron-Frobenius eigenvalue of $A$ |
| $c_{\rm LZ}$ | Lempel-Ziv complexity |
| $\nu$ | Grassberger-Procaccia correlation dimension |

---

## Papers Most Ready for Submission

In rough priority order:

1. **Paper E (LLM/LMSR)** → NeurIPS 2025 / ICML 2025
   Core results: R17 (LMSR=softmax=Fisher), R18 (LLM≤MUP), R19 (Kelly=min loss)
   Dependencies: Self-contained, requires only LLM\_MANIFOLD.md
   
2. **Paper A (LAPLACE/WKB)** → Mathematical Finance
   Core results: WKB=Laplace, Van Vleck=Fisher, $O(1/T^2)$ accuracy
   Dependencies: LAPLACE.md, PAPER.md

3. **Paper B (Sharpe=curvature)** → Annals of Applied Probability
   Core result: R1 ($\mathrm{Sharpe}^*=\|H\|_{L^2}$)
   Dependencies: MINIMAL\_SURFACE.md, CLASSIFICATION.md

4. **Paper C (MUP minimax)** → Operations Research / Journal of Finance
   Core result: R2 (MUP regret $r\log T/2T$)
   Dependencies: CONVERGENCE.md

5. **Paper F (Random matrices)** → Annals of Probability / J. Math. Physics
   Core results: R21 (Dyson forced), R22 (Selberg=MUP), R23 (TW)
   Dependencies: RANDOM\_MATRIX.md

6. **Paper N (Shapley)** → Journal of Finance / Mathematical Finance
   Core result: R25 (Shapley=$b^*_i(\mu_i-\bar\mu)$)
   Dependencies: HYPERCUBE\_SHAPLEY.md

---

## How to Interact With This Project in VS Code

**Reading papers:** Each paper is self-contained. Cross-references use the format
"(PAPER\_NAME.md Section X.Y)" or "(R-number from WHATS\_NEW.md)".

**Adding new results:** 
1. Write the result in the appropriate paper file
2. Add to WHATS\_NEW.md with the next R-number
3. If proved: Tier 1 or 2. If conjectural: Tier 4. If reinterpretation: Tier 5.
4. If it opens a new problem: add to OPEN\_PROBLEMS.md
5. If it is a conjecture: add to CONJECTURES.md with grade A/B/C

**Incorporating old notes:**
1. Read the old note carefully
2. Identify which paper it belongs to (or create a new paper)
3. Check if it is already partially captured in existing papers
4. Write it up in full mathematical precision
5. Add to WHATS\_NEW.md and update CONJECTURES.md / OPEN\_PROBLEMS.md as appropriate

**Writing new papers:**
Follow the template of existing papers: Abstract with bullet points for main results,
numbered sections, theorems in bold with proofs, references at end.
File naming: ALL\_CAPS\_WITH\_UNDERSCORES.md

**The CLAUDE.md file (this file):**
Update this file whenever:
- A new paper is added (add to inventory)
- A new proved result is found (add to key equations)
- A new connection is identified (add to "Key Connections" section)
- A priority changes (update Day 2 priority list)

---

## What NOT to Do

- Do not restart the mathematical framework from scratch. The geometry is settled.
- Do not change notation conventions mid-project. They are set.
- Do not second-guess whether the market is "really" a manifold. That is the axiom.
- Do not conflate the Dyson $\beta$ (symmetry class) with the portfolio $b$ (weights).
- Do not assume Tier 4 conjectures are proved — they are labelled carefully.
- Do not lose the historical grounding. ANECDOTES.md is part of the monograph.

---

## The Closing Thought (From Day 1)

The result that emerged at the end of Day 1 — that the Delaunay adjacency matrix
of the market manifold is simultaneously the Voronoi automaton, the Guttman-Brak
transfer matrix, the Wilf generating function coefficient matrix, and the Markov
chain linearisation, with its Perron-Frobenius eigenvalue encoding the Kelly rate —
is the kind of unification that a monograph introduction can build toward as its
climax.

The reader spends six chapters learning about the market manifold. Then in Part IV
they discover that a single matrix encodes the entire theory: the topology, the
dynamics, the information content, the contagion structure, the generating function,
and the Kelly rate.

That is the mathematical analogue of the moment in physics when you realise the
Hamiltonian contains everything.

*Build toward that moment.*

---

*Last updated: End of Day 1*
*Next session: VS Code + GitHub, Day 2*
*Primary goal: Find the old notes. Everything else follows.*
