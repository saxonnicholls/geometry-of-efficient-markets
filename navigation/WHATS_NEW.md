# What Is New: Complete Inventory of Original Contributions
## Ranked from Strongest to Most Speculative

**Saxon Nicholls** — me@saxonnicholls.com

---

## Tier 1: Fully Proved and Publishable Today (26 results)

**R1. Sharpe-Curvature Identity** *(MINIMAL\_SURFACE)*
$\mathrm{Sharpe}^*=\|H\|_{L^2(M,g_M)}$.
Vol skew of index options measures $H$ in real time.

**R2. MUP Minimax Optimality, Regret $r\log T/2T$** *(CONVERGENCE)*
12× improvement over Cover for $d=50$, $r=4$. Minimax optimal.

**R3. Only CAPMs Are Stably Efficient** *(CLASSIFICATION)*
Clifford torus stability index 5 = LTCM's five simultaneous failure modes.

**R4. Fat Tails: $\alpha_i = Tb^*_i - 1/2$** *(HAMILTONIAN)*
No free parameters. Predicts $\alpha\approx4.5$ for US equities.

**R5. Fokker-Planck Stationary = Jeffreys Prior = Cover's Prior** *(FOKKER\_PLANCK)*
Closes Cover's 30-year gap.

**R6. Completeness = Normal Bundle Dimension** *(HAMILTONIAN)*
Space of EMMs $\cong N_{b^*}M$. Incompleteness dimension $=d-1-r$.

**R7. Vol Skew = Mean Curvature** *(DERIVATIVES)*
$\partial\hat\sigma/\partial k|_{k=0} = -\varepsilon^2H^2/(2\sigma_I)$.

**R8. Doob-Meyer Compensator = Time-Integrated Willmore Energy** *(MARTINGALE)*
The predictable part of the Snell envelope IS the integrated curvature.

**R9. Optimal Randomised Stopping = MUP Posterior** *(MARTINGALE)*
Cover's portfolio re-derived from optimal stopping theory.

**R10. Theta Function as Exact Transition Density** *(MARKET\_PROCESSES)*
$p_t=\vartheta_3$ — exact option pricing for the Clifford torus market.

**R11. Geometric Vol Smile Without Stochastic Volatility** *(SOBOLEV)*
Hyperbolic Gamma $y^2(\partial^2_x+\partial^2_y)V$: smile from curvature alone.

**R12. Diversification: Feller Boundary Proof** *(SOBOLEV)*
Portfolio weights never hit zero for $Tb^*_i>3/2$. Geometric theorem.

**R13. Optimal Pairs Entry/Exit from Hamiltonian Free Boundary** *(PAIRS\_TRADING)*
$z^*_{\rm entry}=\sqrt{1+r/\kappa}$. Classical 2$\sigma$ rule is only optimal when $r=3\kappa$.

**R14. General Prefix Trie = Filtration Tree** *(FILTRATIONS)*
Any grammar-based compressor (LZ77, LZW, CTW, PPM, BWT) applied to the
Voronoi sequence generates a valid filtration on the return path space.
LZ78 case proved (original proof due to first author, ~15 years prior).

**R15. Martin-Löf Randomness of Efficient Returns** *(COMPLEXITY)*
$K(\mathbf{x}_{1:T})=Th_{\rm Kelly}+\frac{r}{2}\log T+O(1)$.

**R16. Willmore Energy = Return Sequence Compressibility** *(COMPLEXITY)*
One bit of Willmore energy = one bit per period of exploitable structure.

**R17. LMSR-Softmax-Fisher Identity** *(LLM\_MANIFOLD)*
LMSR cost function Hessian = $g^{\rm FR}$. Transformer attention = LMSR market making.
Every transformer is an implicit financial market maker in Fisher-Rao geometry.

**R18. LLM Convergence Theorem: No Model Beats the MUP** *(LLM\_MANIFOLD)*
Proved: any transformer of sufficient capacity trained on all public market data
converges to the heat kernel on $M^r$ and cannot outperform the MUP.
Optimal hidden dimension = $r$.

**R19. Kelly Rate = Minimum Cross-Entropy Loss** *(LLM\_MANIFOLD)*
$\min_\theta\mathcal{L}(\theta)=h_{\rm Kelly}(b^*)$. Calibration criterion for market ML models.

**R20. Insider Information Lives in the Normal Bundle** *(LLM\_MANIFOLD)*
$v_\mathcal{G}\in N_{b^*}M$; $\alpha=\varepsilon^2|v_\mathcal{G}|_{g^{\rm FR}}$.
Co-location is temporal filtration shift (different and weaker).

**R21. Dyson Class Forced by Manifold Symmetry** *(RANDOM\_MATRIX)*
CAPM $\to$ GOE ($\beta=1$); Clifford torus $\to$ GUE ($\beta=2$, Berry phase);
pseudo-Anosov $\to$ GSE ($\beta=4$, symplectic foliation). Not a modelling choice.

**R22. Selberg Integral = MUP Partition Function** *(RANDOM\_MATRIX)*
$\mathcal{Z}_T^M = S_r(Tb^*-1/2,\, Tb^*-1/2,\, \beta/2)$. Exact closed form.
MUP normalisation constant computable analytically for all three market types.

**R23. Tracy-Widom $F_\beta$ = Largest Factor Eigenvalue Distribution** *(RANDOM\_MATRIX)*
Crisis signal: exceedance of the $F_\beta$ edge. Market-type specific.

**R24. Vandermonde Repulsion = Fisher-Rao Diversification Pressure** *(RANDOM\_MATRIX)*
$|\lambda_i-\lambda_j|^\beta$ is the Fisher-Rao force keeping factor loadings separated.
GUE ($\beta=2$) provides stronger diversification than GOE ($\beta=1$).

**R25. Shapley Attribution $\phi_i = b^*_i(\mu_i-\bar\mu)$** *(HYPERCUBE\_SHAPLEY)*
Proved: the Shapley value of asset $i$ in the Kelly cooperative game equals the
Fisher-Rao gradient of the Kelly rate at $b^*$. Unique fair attribution satisfying
all four Shapley axioms. Factor Shapley = unique fair factor attribution.

**R26. Walsh Functions = Jacobi Polynomials on the Simplex** *(HYPERCUBE\_SHAPLEY)*
Walsh functions restricted to $\Delta_{d-1}$ are Jacobi polynomials. Barycentric
subdivision = Voronoi Delaunay triangulation (proved). Banzhaf = Walsh-Fourier coefficient.

---

## Tier 2: Proved Under Mild Additional Assumptions (9 results)

**R27.** Full EMH: $H\neq0\Rightarrow$ exploitable alpha (proved for dynamic strategies)
**R28.** Yang-Baxter = no braiding arbitrage
**R29.** Contagion network = Delaunay graph (endogenous)
**R30.** Cheeger constant = systemic risk measure
**R31.** Hawkes criticality = market efficiency
**R32.** Parallel transport = optimal hedge update (Weingarten)
**R33.** Alexander polynomial roots = factor rotation eigenvalues
**R34.** Chaos ≡ stochastic on $M^r$ (Oseledets, $\varepsilon\to0$)
**R35.** Feigenbaum constants govern CAPM-to-pseudo-Anosov bifurcation

---

## Tier 3: New Frameworks and Reinterpretations (14 results)

**R36.** SMB=Kelly: six equivalent characterisations of efficiency
**R37.** Portfolio weights as barycentric coordinates (unifying framework)
**R38.** Föllmer-Schweizer MMM = geometric CAPM pricing
**R39.** Voronoi filtration as a finite automaton (sofic shift)
**R40.** H3/S2 geospatial indexing on the Bhattacharyya sphere
**R41.** Hilbert curve minimises LZ complexity on $M$
**R42.** Stochastic Stokes theorem on $\Delta_{d-1}$
**R43.** Manifold Black-Litterman: tangential vs normal views
**R44.** Rebalancing frequency from Jacobi spectral gap
**R45.** LMSR on the market manifold = MUP gradient
**R46.** Market manifold = minimal sufficient statistic (Neyman-Fisher)
**R47.** Takens embedding recovers $M^r$ from a single return series
**R48.** Optimal Takens delay $\tau=1/\lambda_1$ (Jacobi spectral gap)
**R49.** Path integral: incompleteness premium from normal bundle integration

---

## Tier 4: Conjectures With Strong Motivation (12 results)

**R50.** Jones polynomial = market partition function
**R51.** Topological EMH: $J_\Gamma(q)=1\iff$CAPM
**R52.** $\#\mathbf{P}$-hardness of return prediction
**R53.** Pseudo-Anosov markets simulate Rule 110 (Turing complete)
**R54.** Topologically protected alpha from $c_1(NM)\neq0$
**R55.** Berry phase = adiabatic alpha from correlation cycles
**R56.** RG beta function $\beta_H=-H/2$ + running Sharpe (one-loop open)
**R57.** Penrose tilings on the five-asset simplex ($\phi^2$ appears four ways)
**R58.** LLM training dynamics = MCF in model weight space
**R59.** LMSR on options market = geometric Black-Scholes
**R60.** Attention head effective rank converges to $r$
**R61.** Cheeger constant declined before 2008 GFC and 2022 LDI (testable)

---

## Tier 5: Existing Results Reread Geometrically (6 results)

**R62.** Cover's universal portfolio — geometrically explained
**R63.** CAPM — the unique stable attractor of MCF
**R64.** Markowitz frontier — Fisher-Rao ellipse
**R65.** Minsky's instability hypothesis — Feller boundary dynamics
**R66.** Fed contagion models (Acemoglu, Glasserman, Adrian) — endogenised
**R67.** EMH (Fama 1970) — three new equivalent statements

---

## Summary

| Tier | Count |
|:----:|:-----:|
| 1 — Fully proved | 26 |
| 2 — Proved with mild assumptions | 9 |
| 3 — New frameworks | 14 |
| 4 — Conjectures | 12 |
| 5 — Reinterpretations | 6 |
| **Total** | **67** |

## Top Five

1. **R1** (Sharpe=curvature) — central theorem, proved, observable
2. **R3** (Only CAPMs stable) — explains LTCM, factor anomalies, structural instability
3. **R17** (LMSR=softmax=Fisher) — bridges market microstructure and ML
4. **R21** (Dyson forced by geometry) — eliminates modelling ambiguity in RMT
5. **R25** (Shapley=Fisher-Rao gradient) — unique fair attribution, proved from axioms

## Most Surprising

- **R14** (any compressor = filtration) — compression IS filtration
- **R17** (transformer = market maker) — every LLM is a financial exchange
- **R22** (Selberg = MUP) — ancient mathematics = modern portfolio theory
- **R34** (chaos ≡ stochastic) — the deepest debate in market dynamics is moot
- **R47** (Takens from one series) — the whole manifold hides in one return series
