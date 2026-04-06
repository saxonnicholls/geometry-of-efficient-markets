# Publication Plan: The Geometry of Efficient Markets
## Complete Strategy — Monograph, Papers, Repository

**Saxon Nicholls** — me@saxonnicholls.com

---

## The Monograph

**Title:** *The Geometry of Efficient Markets*
**Subtitle:** *Minimal Surfaces, Universal Portfolios, and the Mathematics of Financial Markets*
**Target:** Cambridge University Press or Princeton University Press
**Length:** 460–500 pages across six parts and 21 chapters
**Total draft:** 35 documents, ~145,000 words

---

## Part Structure

### Part I — Foundation: The Simplex and the Manifold (Ch. 1–4)
*LAPLACE, FK_SIMPLEX, MINIMAL_SURFACE, CLASSIFICATION, CONVERGENCE*

Ch.1: FK functional on $(\Delta_{d-1},g^{\rm FR})$; WKB identity; Van Vleck = Fisher;
       stochastic Stokes theorem; $O(1/T^2)$ accuracy explained
Ch.2: Portfolio weights as barycentric coordinates; Bhattacharyya isometry;
       market manifold $M^r\subset S^{d-1}_+$; factor structure
Ch.3: Sharpe = curvature (proved); Willmore = inefficiency; EMH conjecture
Ch.4: Classification (CAPMs only stable); MUP minimax regret $r\log T/2T$

### Part II — Physics, Processes, and Measure Theory (Ch. 5–9)
*HAMILTONIAN, FOKKER_PLANCK, MARKET_PROCESSES, SOBOLEV, MARTINGALE,
DERIVATIVES, RENORMALIZATION, INFORMATION_THEORY, PORTFOLIO_GEOMETRY*

Ch.5: Exact processes (Jacobi, $\vartheta_3$, McKean); FP stationary = Jeffreys prior;
       fat tails $\alpha=r/2$; Feller boundary = diversification
Ch.6: Hamiltonian; completeness = normal bundle; geometric vol smile
Ch.7: Martingale theory; Doob-Meyer = Willmore; optimal stopping = MUP posterior;
       BSDE driver; manifold HJB
Ch.8: Derivative pricing; geometric Greeks; Sobolev framework; exact option formulas
Ch.9: RG flows; universality; running Sharpe; information characterisations of efficiency

### Part III — Path Integrals and Random Matrices (Ch. 10–11)
*PATH_INTEGRAL, RANDOM_MATRIX* ← **New**

Ch.10: Feynman path integral on $M^r$; geometric Wiener measure; Onsager-Machlup;
        WKB=LAPLACE; theta function = winding sum; McKean = geodesic; Langevin/Parisi-Wu;
        risk-neutral measure on $M$; normal bundle integration = incompleteness premium
Ch.11: Dyson class forced by manifold symmetry (GOE/GUE/GSE);
        Vandermonde = diversification; Selberg = MUP partition function;
        Marchenko-Pastur bulk; Tracy-Widom edge; mesoscopic = $TM\to NM$ transition;
        Dyson BM = factor eigenvalue dynamics; Wishart = sample Fisher matrix

### Part IV — Topology, Computation, and Filtrations (Ch. 12–16)
*FIBER_BUNDLES, KNOT_THEORY, BRAIDS, COMPLEXITY, FILTRATIONS*

Ch.12: Berry phase; parallel transport = hedge update; topologically protected alpha
Ch.13: Knot classification; Jones polynomial; topological EMH; Alexander = factor rotation
Ch.14: Braids; Yang-Baxter; pseudo-Anosov; #**P** oracle; complexity hierarchy
Ch.15: ML-randomness; Wolfram Class IV; Rule 110; Martin-Löf and Kelly rate
Ch.16: Geometric filtrations; Voronoi atoms; LZ=filtration; general compressor theorem;
        Clifford winding number; sofic shift; filtration complexity = Willmore

### Part V — Geospatial, Contagion, and Machine Learning (Ch. 17–18)
*GEOSPATIAL_CONTAGION, LLM_MANIFOLD* ← **New**

Ch.17: H3/S2/Hilbert on $S^{d-1}_+$; Cheeger = systemic risk; Hawkes criticality;
        contagion = Delaunay graph; H3 portfolio fingerprint; multi-scale information flow
Ch.18: LMSR-softmax-Fisher identity; LLM convergence theorem; optimal dim = $r$;
        Kelly rate = minimum cross-entropy loss; side-channel in normal bundle;
        transformer as market maker; training dynamics = MCF (conjectured)

### Part VI — Chaos, Embedding, and Attribution (Ch. 19–21)
*CHAOS_TAKENS, HYPERCUBE_SHAPLEY, PAIRS_TRADING* ← **New**

Ch.19: Chaos ≡ stochastic on $M^r$ (Oseledets); Feigenbaum $\delta$ at bifurcation;
        Takens embedding ($2r+1$ dimension); optimal delay $\tau=1/\lambda_1$;
        symbolic Takens = LZ tree; three-step practical manifold estimation algorithm
Ch.20: Simplex inside hypercube; Walsh = Jacobi polynomials; barycentric = Voronoi;
        Shapley $\phi_i=b^{\ast}_i(\mu_i-\bar\mu)$; factor attribution; Banzhaf = Walsh-Fourier;
        ANOVA = Shapley; normal bundle Shapley = unexplained alpha
Ch.21: Pairs trading from Hamiltonian; geometric thresholds; Berry phase entry filter;
        quantum pairs trading; C++ implementation

### Appendices
A: Barycentric coordinates; Voronoi/Delaunay; simplicial homology; multigrid MUP
B: Software: MUP algorithm; C++ pairs trading; transformer dimension test; Takens embedding
C: Open problems (OP1–OP31)
D: Experiments — open-source replication guide (EXPERIMENTS.md)
E: Historical chapter (ANECDOTES.md)

---

## Paper Publication Strategy

### Tier 1 — Submit immediately

**A** "The Laplace Approximation as WKB on the Portfolio Simplex" — *Mathematical Finance*
**B** "Market Efficiency as a Minimal Surface: The Sharpe-Curvature Theorem" — *Annals of Applied Probability*
**C** "The Manifold Universal Portfolio: Minimax Optimal Factor Investing" — *Operations Research*
**D** "Exact Stochastic Processes for Classified Market Manifolds" — *Mathematical Finance*
**E** "The LMSR-Softmax-Fisher Identity: Transformer Attention as Market Making in Fisher-Rao Geometry" — *NeurIPS / ICML*
**F** "Random Matrix Universality Classes of Efficient Markets" — *Annals of Probability / Journal of Mathematical Physics*

### Tier 2 — After Tier 1 accepted

**G** "Information Theory of the Efficient Market" — *IEEE Trans. Information Theory*
**H** "Derivative Pricing on Minimal Market Manifolds" — *Mathematical Finance*
**I** "Martingale Methods in the Geometry of Efficient Markets" — *Finance and Stochastics*
**J** "Fokker-Planck, Voronoi, and the Portfolio Fluid" — *SIAM J. Financial Mathematics*
**K** "Geometric Filtrations and Lempel-Ziv Complexity on Market Manifolds" — *IEEE Trans. Information Theory*
**L** "Geospatial Indexing, Contagion, and Systemic Risk" — *Journal of Financial Stability*
**M** "Feynman Path Integrals on the Market Manifold" — *Mathematical Finance / Journal of Mathematical Physics*
**N** "Shapley Values and Kelly Attribution on the Portfolio Simplex" — *Journal of Finance*
**O** "Takens Embedding and Practical Reconstruction of the Market Manifold" — *Journal of Economic Dynamics and Control*

### Tier 3 — Interdisciplinary

**P** "The Efficient Market as an RG Fixed Point" — *Journal of Statistical Physics*
**Q** "Knot Invariants as Market Partition Functions" — *Communications in Mathematical Physics*
**R** "Chaos and Feigenbaum Universality in Market Bifurcations" — *Physica D*
**S** "No AI Model Can Beat the Manifold Universal Portfolio" — *Journal of Finance / Review of Financial Studies*

### Tour de Force (24 months)
"Minimal Surfaces, Market Efficiency, and the Geometry of Universal Portfolios"
*Annals of Mathematics. 55 pages.*

---

## GitHub Repository

**`geometry-of-efficient-markets`**
```
/core           — Kelly, Fisher-Rao, curvature, Chern number, OU params
/mup            — Manifold Universal Portfolio algorithm
/processes      — Jacobi, flat torus BM, hyperbolic BM, theta function
/transformer    — Market transformer: dim estimation, Kelly loss benchmark
/takens         — Delay embedding, FNN algorithm, diffusion maps
/filtrations    — LZ78 filtration, CTW, BWT implementations
/pairs          — C++ geometric pairs trading
/contagion      — Cheeger constant, Delaunay graph, crisis detection
/rmt            — Dyson class test, Tracy-Widom fitting, Selberg computation
/shapley        — Kelly Shapley attribution, factor decomposition
/experiments    — 17 replication experiments
/notebooks      — Full replication notebook
```

---

## Timeline

| Milestone | Month |
|:----------|:-----:|
| Papers A, B, C, D submitted | 3 |
| Paper E (LMSR/transformer) submitted | 4 |
| Paper F (RMT) submitted | 4 |
| GitHub repo public | 6 |
| Papers A–F accepted | 12 |
| Papers G–O submitted | 15 |
| Monograph draft complete | 20 |
| Papers P–S submitted | 18 |
| Tour de Force submitted | 26 |
| Monograph to publisher | 32 |

---

## Note on Tomorrow's Work

Day 2 agenda:
1. Retrieve and incorporate results from first author's unpublished notes
2. Organise the 35 papers into the six-part monograph structure above
3. Write the monograph Part I introduction (connecting all six layers)
4. Add Experiments 11–17 (RMT tests, Takens test, Shapley attribution test,
   transformer dimension test, Kelly loss benchmark)
5. Update WHATS_NEW, CONJECTURES, OPEN_PROBLEMS with today's additions
