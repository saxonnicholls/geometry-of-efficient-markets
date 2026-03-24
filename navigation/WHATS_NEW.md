# What Is New: Complete Inventory of Original Contributions
## Ranked from Strongest to Most Speculative

**Saxon Nicholls** — me@saxonnicholls.com

---

## Tier 1: Fully Proved and Publishable Today (26 results)

**R1. Sharpe-Curvature Identity** *(MINIMAL\_SURFACE)*
$\mathrm{Sharpe}^{\ast}=\|H\|\_{L^2(M,g\_M)}$.
Vol skew of index options measures $H$ in real time.

**R2. MUP Minimax Optimality, Regret $r\log T/2T$** *(CONVERGENCE)*
12× improvement over Cover for $d=50$, $r=4$. Minimax optimal.

**R3. Only CAPMs Are Stably Efficient** *(CLASSIFICATION)*
Clifford torus stability index 5 = LTCM's five simultaneous failure modes.
The closed-manifold result is proved; the Dirichlet boundary case for $d \gg r$ is OP32.

**R4. Fat Tails: $\alpha\_i = Tb^{\ast}\_i - 1/2$** *(HAMILTONIAN)*
No free parameters. Predicts $\alpha\approx4.5$ for US equities.

**R5. Fokker-Planck Stationary = Jeffreys Prior = Cover's Prior** *(FOKKER\_PLANCK)*
Closes Cover's 30-year gap.

**R6. Completeness = Normal Bundle Dimension** *(HAMILTONIAN)*
Space of EMMs $\cong N\_{b^{\ast}}M$. Incompleteness dimension $=d-1-r$.

**R7. Vol Skew = Mean Curvature** *(DERIVATIVES)*
$\partial\hat\sigma/\partial k|\_{k=0} = -\varepsilon^2H^2/(2\sigma\_I)$.

**R8. Doob-Meyer Compensator = Time-Integrated Willmore Energy** *(MARTINGALE)*
The predictable part of the Snell envelope IS the integrated curvature.

**R9. Optimal Randomised Stopping = MUP Posterior** *(MARTINGALE)*
Cover's portfolio re-derived from optimal stopping theory.

**R10. Theta Function as Exact Transition Density** *(MARKET\_PROCESSES)*
$p\_t=\vartheta\_3$ — exact option pricing for the Clifford torus market.

**R11. Geometric Vol Smile Without Stochastic Volatility** *(SOBOLEV)*
Hyperbolic Gamma $y^2(\partial^2\_x+\partial^2\_y)V$: smile from curvature alone.

**R12. Diversification: Feller Boundary Proof** *(SOBOLEV)*
Portfolio weights never hit zero for $Tb^{\ast}\_i>3/2$. Geometric theorem.

**R13. Optimal Pairs Entry/Exit from Hamiltonian Free Boundary** *(PAIRS\_TRADING)*
$z^{\ast}\_{\rm entry}=\sqrt{1+r/\kappa}$. Classical 2$\sigma$ rule is only optimal when $r=3\kappa$.

**R14. LZ78 Prefix Tree = Filtration Tree** *(FILTRATIONS)*
The LZ78 compressor applied to the Voronoi symbolic sequence generates a valid
filtration whose atoms refine the Voronoi filtration. Proved for LZ78; the general
statement for arbitrary grammar-based compressors (LZ77, CTW, PPM, BWT) is Conjecture C18.

**R15. Martin-Löf Randomness of Efficient Returns** *(COMPLEXITY)*
$K(\mathbf{x}\_{1:T})=Th\_{\rm Kelly}+\frac{r}{2}\log T+O(1)$.

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
$\min\_\theta\mathcal{L}(\theta)=h\_{\rm Kelly}(b^{\ast})$. Calibration criterion for market ML models.

**R20. Insider Information Lives in the Normal Bundle** *(LLM\_MANIFOLD)*
$v\_\mathcal{G}\in N\_{b^{\ast}}M$; $\alpha=\varepsilon^2|v\_\mathcal{G}|\_{g^{\rm FR}}$.
Co-location is temporal filtration shift (different and weaker).

**R21. Dyson Class Forced by Manifold Symmetry** *(RANDOM\_MATRIX)*
CAPM $\to$ GOE ($\beta=1$); Clifford torus $\to$ GUE ($\beta=2$, Berry phase);
pseudo-Anosov $\to$ GSE ($\beta=4$, symplectic foliation). Not a modelling choice.

**R22. Selberg Integral = MUP Partition Function** *(RANDOM\_MATRIX)*
$\mathcal{Z}\_T^M = S\_r(Tb^{\ast}-1/2,\, Tb^{\ast}-1/2,\, \beta/2)$. Exact closed form.
MUP normalisation constant computable analytically for all three market types.

**R23. Tracy-Widom $F\_\beta$ = Largest Factor Eigenvalue Distribution** *(RANDOM\_MATRIX)*
Crisis signal: exceedance of the $F\_\beta$ edge. Market-type specific.

**R24. Vandermonde Repulsion = Fisher-Rao Diversification Pressure** *(RANDOM\_MATRIX)*
$|\lambda\_i-\lambda\_j|^\beta$ is the Fisher-Rao force keeping factor loadings separated.
GUE ($\beta=2$) provides stronger diversification than GOE ($\beta=1$).

**R25. Shapley Attribution $\phi\_i = b^{\ast}\_i(\mu\_i-\bar\mu)$** *(HYPERCUBE\_SHAPLEY)*
Proved: the Shapley value of asset $i$ in the Kelly cooperative game equals the
Fisher-Rao gradient of the Kelly rate at $b^{\ast}$. Unique fair attribution satisfying
all four Shapley axioms. Factor Shapley = unique fair factor attribution.

**R26. Walsh Functions = Jacobi Polynomials on the Simplex** *(HYPERCUBE\_SHAPLEY)*
Walsh functions restricted to $\Delta\_{d-1}$ are Jacobi polynomials. Barycentric
subdivision = Voronoi Delaunay triangulation (proved). Banzhaf = Walsh-Fourier coefficient.

---

## Tier 2: Proved Under Mild Additional Assumptions (20 results)

**R27.** Full EMH: $H\neq0\Rightarrow$ exploitable alpha (proved for dynamic strategies)
**R28.** Yang-Baxter = no braiding arbitrage
**R29.** Contagion network = Delaunay graph (endogenous)
**R30.** Cheeger constant = systemic risk measure
**R31.** Hawkes criticality = market efficiency
**R32.** Parallel transport = optimal hedge update (Weingarten)
**R33.** Alexander polynomial roots = factor rotation eigenvalues
**R34.** Chaos ≡ stochastic on $M^r$ (Oseledets, $\varepsilon\to0$)
**R35.** Feigenbaum constants govern CAPM-to-pseudo-Anosov bifurcation
**R68.** Heat kernel comparison orders option prices by topology: $C_{\rm CAPM}\leq C_{\rm Clifford}\leq C_{\rm hyperbolic}$ for any convex payoff (Cheeger-Yau)
**R69.** Gauss-Bonnet constraint on Sharpe ratio: $\int_M K\,d\mathrm{vol}=2\pi\chi(M)$ constrains achievable Sharpe distribution by topology
**R70.** Manifold Kalman filter achieves Cramér-Rao bound: $P_\infty = F(b^{\ast})^{-1}$, statistically efficient estimator of $b^{\ast}$
**R71.** Witten index = 1 for pairs trading: OU/QHO isomorphism gives topological guarantee of exactly one equilibrium
**R72.** BSDE representation of Sharpe ratio: $(\mathrm{Sharpe}^{\ast})^2=(Y_0^{\rm ineff}-Y_0^{\rm eff})/(\varepsilon^2 T)$
**R73.** Replicator-diffusion linearisation = Jacobi operator: five unstable Clifford torus modes = five directions where posterior is repelled
**R74.** Symbolic market dynamics on Voronoi partition is a subshift of finite type (SFT), strictly stronger than sofic
**R75.** Euler characteristic in sub-leading regret: $O(1/T)$ correction to universal portfolio wealth contains $-\pi/6\cdot\chi(M)$ via Gauss-Bonnet
**R80.** Cap-weight Kelly shortfall = $(1/2)d^2\_{g^{\rm FR}}(b^{\rm cap}, b^{\ast})$ *(BETTER\_INDEX\_FUND)* — the Fisher-Rao distance from cap-weight to log-optimal quantifies suboptimality
**R81.** Equal weight dominates cap weight in Fisher-Rao distance *(BETTER\_INDEX\_FUND)* — $\mathbb{E}[d\_{g^{\rm FR}}(b^{\rm ew}, b^{\ast})] \leq \mathbb{E}[d\_{g^{\rm FR}}(b^{\rm cap}, b^{\ast})]$
**R82.** Optimal rebalancing frequency = Jacobi spectral gap *(BETTER\_INDEX\_FUND)* — $f^{\ast} \approx \lambda\_1^{\rm CS} \approx 12$/year (monthly)

---

## Tier 3: New Frameworks and Reinterpretations (14 results)

**R36.** SMB=Kelly: six equivalent characterisations of efficiency
**R37.** Portfolio weights as barycentric coordinates (unifying framework)
**R38.** Föllmer-Schweizer MMM = geometric CAPM pricing
**R39.** Voronoi filtration as a finite automaton (sofic shift)
**R40.** H3/S2 geospatial indexing on the Bhattacharyya sphere
**R41.** Hilbert curve minimises LZ complexity on $M$
**R42.** Stochastic Stokes theorem on $\Delta\_{d-1}$
**R43.** Manifold Black-Litterman: tangential vs normal views
**R44.** Rebalancing frequency from Jacobi spectral gap
**R45.** LMSR on the market manifold = MUP gradient
**R46.** Market manifold = minimal sufficient statistic (Neyman-Fisher)
**R47.** Takens embedding recovers $M^r$ from a single return series
**R48.** Optimal Takens delay $\tau=1/\lambda\_1$ (Jacobi spectral gap)
**R49.** Path integral: incompleteness premium from normal bundle integration

---

## Tier 4: Conjectures With Strong Motivation (19 results)

**R50.** Jones polynomial = market partition function
**R51.** Topological EMH: $J\_\Gamma(q)=1\iff$CAPM
**R52.** #**P**-hardness of return prediction
**R53.** Pseudo-Anosov markets simulate Rule 110 (Turing complete)
**R54.** Topologically protected alpha from $c\_1(NM)\neq0$
**R55.** Berry phase = adiabatic alpha from correlation cycles
**R56.** RG beta function $\beta\_H=-H/2$ + running Sharpe (one-loop open)
**R57.** Penrose tilings on the five-asset simplex ($\phi^2$ appears four ways)
**R58.** LLM training dynamics = MCF in model weight space
**R59.** LMSR on options market = geometric Black-Scholes
**R60.** Attention head effective rank converges to $r$
**R61.** Cheeger constant declined before 2008 GFC and 2022 LDI (testable)
**R76.** Modular bootstrap for Clifford torus returns: $\vartheta_3$ modular transformation relates short-time and long-time characteristic functions, constraining moments at all intermediate times
**R77.** Spectral gap lower bound from Sharpe ratio: $\lambda_1\geq f(\mathrm{Sharpe}^{\ast},\mathrm{vol}(M))$ via Cheeger inequality — lower bound on mean-reversion speed from observed Sharpe
**R78.** MUP as exponential family MLE: normalising constant is exponential family on $M^r$ with sufficient statistic $L_T$; Cramér-Rao gives $\mathrm{Var}(\hat b)\geq(TF_M)^{-1}$
**R79.** Bernstein-type theorem for market manifolds: minimal graph over factor simplex $\Rightarrow$ totally geodesic — independent proof of classification without Simons/Lawson-Simons
**R83.** Inflation = dual Fisher-Rao norm of sectoral inflation covector *(INFLATION\_CAPITAL\_FLOWS)* — geometric definition recovers headline CPI for uniform inflation, captures sectoral structure
**R84.** Fisher equation = holonomy of capital flow connection *(INFLATION\_CAPITAL\_FLOWS)* — real return = nominal minus Berry phase around goods market loop; path-dependent under heterogeneous inflation
**R85.** Taylor rule = LQG geodesic steering *(INFLATION\_CAPITAL\_FLOWS)* — Taylor coefficients are the LQG gains of a geometric PID controller on the financial-goods fiber bundle

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
| 2 — Proved with mild assumptions | 20 |
| 3 — New frameworks | 14 |
| 4 — Conjectures | 19 |
| 5 — Reinterpretations | 6 |
| **Total** | **85** |

## Top Five

1. **R1** (Sharpe=curvature) — central theorem, proved, observable
2. **R3** (Only CAPMs stable; closed manifolds proved, boundary case $d \gg r$ is OP32) — explains LTCM, factor anomalies, structural instability
3. **R17** (LMSR=softmax=Fisher) — bridges market microstructure and ML
4. **R21** (Dyson forced by geometry) — eliminates modelling ambiguity in RMT
5. **R25** (Shapley=Fisher-Rao gradient) — unique fair attribution, proved from axioms

## Most Surprising

- **R14** (LZ78 compressor = filtration) — compression IS filtration
- **R17** (transformer = market maker) — every LLM is a financial exchange
- **R22** (Selberg = MUP) — ancient mathematics = modern portfolio theory
- **R34** (chaos ≡ stochastic) — the deepest debate in market dynamics is moot
- **R47** (Takens from one series) — the whole manifold hides in one return series
