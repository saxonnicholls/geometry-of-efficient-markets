# Conjectures: The Unproved but Believed
## Graded A (near-certain) or B (probable)

**Saxon Nicholls** — me@saxonnicholls.com

---

## Part I: Market Efficiency

**C1. Full EMH (Grade A)**
$H\neq0\Rightarrow$ exploitable alpha for all strategies.
*Approach:* BSDE comparison under completeness; mean-field game for general case.

**C2. Topological EMH (Grade B)**
$J\_\Gamma(q)=1$ for generic $q$ $\iff$ market is topologically CAPM.
*Open step:* Identify the Chern-Simons level $k$ in the portfolio action.

**C3. Alexander Polynomial = Factor Rotation Speed (Grade A)**
Roots of $\Delta\_\Gamma(t)$ = eigenvalues of factor rotation matrix after one
business cycle. Seifert matrix = normal bundle monodromy (proved).
Trefoil: $60°$/cycle. Figure-eight: $\phi^2$.

**C4. Trefoil Markets Cannot Become CAPM (Grade A)**
Topologically locked — trefoil is not ribbon (Fox-Milnor, proved).

**C5. Market Concordance Group Has Infinite Rank (Grade B)**
From Milnor independence of torus knots.

---

## Part II: Computation and Information Theory

**C6. #**P**-Hardness of Return Prediction (Grade B)**
*Open step:* Identify $q\_0=e^{2\pi i/(k+2)}$ is not at an exceptional easy value.

**C7. Pseudo-Anosov Markets Simulate Rule 110 (Grade B)**
*Open step:* Explicit embedding of Fibonacci substitution into Rule 110.

**C8. Market Equilibrium: $\mathbf{PPAD}$ but $\mathbf{P}$ for Kelly (Grade B)**
Kelly optimality is convex with unique solution — likely $\mathbf{P}$.

---

## Part III: Topology and Geometry

**C9. Market Chern Number Computable from Return Data (Grade A)**
$c\_1(NM)\in\mathbb{Z}$ computable quarterly from rolling covariance.
Expected to jump at structural breaks.

**C10. Topologically Protected Alpha Is Quantised (Grade B)**
When $c\_1(NM)\neq0$: alpha $= c\_1/T$ per cycle.

**C11. Market Phase Transitions = Chern Number Changes (Grade B)**
Major structural breaks = integer jumps in $c\_1(NM)$ with spectral gap closure.

**C12. Voronoi Symbolic Dynamics Sofic for All Compact $M$ (Grade A)**
*Status: SFT part now proved as R74. CTW posterior = MUP posterior remains conjectural.*
Any grammar-based compressor generates a valid filtration.
Extension of R14 (LZ case proved). CTW posterior = MUP posterior;
BWT sorted order = filtration atoms by entropy.

**C13. Penrose Tilings on the Five-Asset Simplex (Grade B)**
Voronoi tessellation of $\Delta\_4$ with five factor vertices has Penrose-tiling
combinatorial structure with $\phi^2$ growth rate. The same $\phi^2$ appears in:
pseudo-Anosov, figure-eight Alexander roots, Fibonacci substitution, Penrose tiling.
All four are the same mathematical fact.

---

## Part IV: Stochastic Processes and Chaos

**C14. Jacobi Diffusion Is the Correct CAPM Model (Grade A)**
Portfolio weights have Beta stationary distribution. Empirically testable:
KS test on rolling log-optimal weights (EXPERIMENTS Experiment 4).

**C15. Hyperbolic Market Long-Run Tails Are Cauchy (Grade A)**
During crises, $\alpha\to1$. Hill estimator should decline toward 1
in months following Cheeger collapse.

**C16. McKean Formula Prices Long-Dated Options Better Than BS (Grade B)**
$C\_{\rm McKean}>C\_{\rm BS}$ for maturity $T>1$ year. Testable on LEAPS.

**C17. Feigenbaum Constants at the CAPM-to-pA Bifurcation (Grade B)**
The period-doubling cascade from CAPM to pseudo-Anosov dynamics exhibits
universal Feigenbaum constants $\delta=4.669$, $\alpha=2.502$. The
Jacobi eigenvalue spacings at successive bifurcations should converge
to ratio $\delta$.

---

## Part V: LLMs and Machine Learning

**C18. General Prefix Trie = Filtration (Grade A) — PROVED (main part)**
*Status: Theorem 4.2 in FILTRATIONS.md proves that ANY prefixwise compressor
(satisfying monotonicity, prefix closure, determinism) generates a valid
subfiltration. This covers LZ78, LZW, CTW, PPM. LZ77 does NOT qualify
(violates monotonicity — sliding window deletes old phrases).*
*STILL CONJECTURAL: CTW posterior = MUP posterior. BWT = filtration atoms
by entropy. These are stronger claims about specific compressor-market
correspondences that go beyond the general filtration property.*

**C19. LLM Training Dynamics = MCF in Model Weight Space (Grade B)**
Natural gradient descent on cross-entropy IS gradient flow of area functional.
Training a market model IS doing mean curvature flow.

**C20. LMSR on Options Market = Geometric Black-Scholes (Grade B)**
LMSR on the options market manifold reproduces the manifold pricing PDE.
Liquidity parameter $b$ corresponds to market depth $\sim1/H$.

**C21. Attention Head Effective Rank Converges to $r$ (Grade A)**
Under spectral regularisation, the stable rank of transformer attention
weight matrices converges to $r$ when trained on efficient market data.

---

## Part VI: Random Matrices

**C22. $E\_8$ Symmetry in 9-Asset Markets (Grade C)**
The Voronoi tessellation of $\Delta\_8$ may have $E\_8$ Weyl group symmetry.
If true: optimal diversification in 8 dimensions has exceptional symmetry.
Connection to Viazovska's 2016 sphere packing proof.

**C23. Dyson BM Eigenvalue Collisions = Cheeger Constant Collapse (Grade B)**
Factor eigenvalue collisions (Dyson BM touching the boundary) correspond
to the Cheeger constant $h\_M\to0$ and MCF singularity formation.
Near a crisis: the Dyson BM hits the Vandermonde wall simultaneously with
the manifold developing a bottleneck.

---

## Part VII: History and Applications

**C24. LTCM Failure Was Predicted by Stability Index Theorem (Grade A)**
Mathematical claim: Clifford torus stability index = 5 (proved).
Historical interpretation: LTCM's five strategy clusters = five unstable Jacobi modes.
Predictable from the 1973 Lawson-Simons theorem.

**C25. Cheeger Constant Declined Before 2008 and 2022 (Grade B)**
Empirically testable. Predicted to be a 3-6 month leading indicator of VIX spikes.

---

## Part VIII: New Connections

**C26. Clifford Torus U(n) Holonomy (Grade A) ★★**
The Berry phase on the Clifford torus normal bundle provides a complex structure,
placing the holonomy in $U(n)$ and forcing GUE statistics. Required for full proof
of Dyson class correspondence (Theorem 1.1(ii) of RANDOM\_MATRIX).

**C27. Pseudo-Anosov Sp(n) Holonomy (Grade A) ★★★**
The foliation pairing of the pseudo-Anosov map provides a symplectic structure on
the normal bundle, placing holonomy in $Sp(n)$ and forcing GSE statistics. Required
for Theorem 1.1(iii) of RANDOM\_MATRIX.

**C28. Selberg Derivative = Shapley Value (Grade A) ★★**
$\partial/\partial a\_i \log S\_r(a,b,\gamma) = \phi\_i = b^{\ast}\_i(\mu\_i - \bar\mu)$.
The derivative of the log Selberg integral with respect to the $i$-th parameter equals
the Shapley value. Would connect RANDOM\_MATRIX to HYPERCUBE\_SHAPLEY.

**C29. Kalman Innovation = LZ Phrase Boundaries (Grade B) ★★**
LZ phrase boundaries correspond to times when Kalman innovation exceeds a threshold.
LZ complexity rate = Kalman innovation variance rate. Would connect
STOCHASTIC\_CONTROL\_KALMAN to FILTRATIONS.

**C30. Percolation Threshold = Hawkes Criticality (Grade B) ★★**
$p\_c$ on the Delaunay graph and $\rho(A\_{\rm Hawkes})=1$ are the same condition.
Would connect GRASSBERGER\_PERCOLATION\_GENERATING to GEOSPATIAL\_CONTAGION.

---

## Summary

| Grade | Count |
|:-----:|:-----:|
| A | 13 |
| B | 16 |
| C | 1 |
| **Total** | **30** |

**Three most important to prove next:**
1. C1 (Full EMH) — BSDE approach is close
2. C18 (General trie filtration) — ★★, extends existing proof immediately
3. C21 (Attention rank = $r$) — ★★, high practical impact for ML

**Most surprising if true:**
- C13 (Penrose tilings) — $\phi^2$ appears four independent times
- C19 (LLM training = MCF) — training and arbitrage are the same flow
- C22 ($E\_8$ markets) — exceptional mathematics inside 9-asset portfolios
