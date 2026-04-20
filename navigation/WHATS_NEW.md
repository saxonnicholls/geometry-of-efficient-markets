# What Is New: Complete Inventory of Original Contributions
## Ranked from Strongest to Most Speculative

**Saxon Nicholls** — me@saxonnicholls.com

---

## Tier 0: Foundational (1 result)

**R0a. Convex Information Processing Theorem** *(CONVEX_INFORMATION)*
Any classical commutative information processing system satisfying closure
under combination, the data processing inequality, continuity, normalisation,
and Markov channels is isomorphic to a geodesically convex subset of
$(\Delta_{d-1}, g^{\rm FR})$. The Fisher-Rao metric is the unique geometry
compatible with these axioms (Čencov 1982). The ambient convex space of
the monograph is forced; the market manifold is the Kelly-optimal structure
within it.

**R0b. Convexification = Probabilification** *(CONVEXIFICATION)*
The free convex completion of any measurable space $X$ is $\mathcal{P}(X)$
(probability measures). Five operators — convex hull, Legendre-Fenchel,
density matrices, Reynolds averaging, ergodic time-averaging — are all
instances of $\mathcal{P}$. Convexification IS the passage from
deterministic to probabilistic. Negative intrinsic curvature forces
$\|H\| > 0$ (mandatory alpha for hyperbolic markets). Sobolev extension
of Čencov to $W^{1,2}$ under Muckenhoupt $A_2$ weights.

---

## Tier 1: Fully Proved and Publishable Today (26 results)

**R1. Sharpe-Curvature Identity** *(MINIMAL_SURFACE)*
$\mathrm{Sharpe}^{\ast}=\|H\|_{L^2(M,g_M)}$.
Vol skew of index options measures $H$ in real time.

**R2. MUP Minimax Optimality, Regret $r\log T/2T$** *(CONVERGENCE)*
12× improvement over Cover for $d=50$, $r=4$. Minimax optimal.

**R3. Only CAPMs Are Stably Efficient** *(CLASSIFICATION)*
Clifford torus stability index 5 = LTCM's five simultaneous failure modes.
The closed-manifold result is proved; the Dirichlet boundary case for $d \gg r$ is OP32.

**R4. Fat Tails: $\alpha_i = Tb^{\ast}_i - 1/2$** *(HAMILTONIAN)*
No free parameters. Predicts $\alpha\approx4.5$ for US equities.

**R5. Fokker-Planck Stationary = Jeffreys Prior = Cover's Prior** *(FOKKER_PLANCK)*
Closes Cover's 30-year gap.

**R6. Completeness = Normal Bundle Dimension** *(HAMILTONIAN)*
Space of EMMs $\cong N_{b^{\ast}}M$. Incompleteness dimension $=d-1-r$.

**R7. Vol Skew = Mean Curvature** *(DERIVATIVES)*
$\partial\hat\sigma/\partial k|_{k=0} = -\varepsilon^2H^2/(2\sigma_I)$.

**R8. Doob-Meyer Compensator = Time-Integrated Willmore Energy** *(MARTINGALE)*
The predictable part of the Snell envelope IS the integrated curvature.

**R9. Optimal Randomised Stopping = MUP Posterior** *(MARTINGALE)*
Cover's portfolio re-derived from optimal stopping theory.

**R10. Theta Function as Exact Transition Density** *(MARKET_PROCESSES)*
$p_t=\vartheta_3$ — exact option pricing for the Clifford torus market.

**R11. Geometric Vol Smile Without Stochastic Volatility** *(SOBOLEV)*
Hyperbolic Gamma $y^2(\partial^2_x+\partial^2_y)V$: smile from curvature alone.

**R12. Diversification: Feller Boundary Proof** *(SOBOLEV)*
Portfolio weights never hit zero for $Tb^{\ast}_i>3/2$. Geometric theorem.

**R13. Optimal Pairs Entry/Exit from Hamiltonian Free Boundary** *(PAIRS_TRADING)*
$z^{\ast}_{\rm entry}=\sqrt{1+r/\kappa}$. Classical 2$\sigma$ rule is only optimal when $r=3\kappa$.

**R14. LZ78 Prefix Tree = Filtration Tree** *(FILTRATIONS)*
The LZ78 compressor applied to the Voronoi symbolic sequence generates a valid
filtration whose atoms refine the Voronoi filtration. Proved for LZ78; the general
statement for arbitrary grammar-based compressors (LZ77, CTW, PPM, BWT) is Conjecture C18.

**R15. Martin-Löf Randomness of Efficient Returns** *(COMPLEXITY)*
$K(\mathbf{x}_{1:T})=Th_{\rm Kelly}+\frac{r}{2}\log T+O(1)$.

**R16. Willmore Energy = Return Sequence Compressibility** *(COMPLEXITY)*
One bit of Willmore energy = one bit per period of exploitable structure.

**R17. LMSR-Softmax-Fisher Identity** *(LLM_MANIFOLD)*
LMSR cost function Hessian = $g^{\rm FR}$. Transformer attention = LMSR market making.
Every transformer is an implicit financial market maker in Fisher-Rao geometry.

**R18. LLM Convergence Theorem: No Model Beats the MUP** *(LLM_MANIFOLD)*
Proved: any transformer of sufficient capacity trained on all public market data
converges to the heat kernel on $M^r$ and cannot outperform the MUP.
Optimal hidden dimension = $r$.

**R19. Kelly Rate = Minimum Cross-Entropy Loss** *(LLM_MANIFOLD)*
$\min_\theta\mathcal{L}(\theta)=h_{\rm Kelly}(b^{\ast})$. Calibration criterion for market ML models.

**R20. Insider Information Lives in the Normal Bundle** *(LLM_MANIFOLD)*
$v_\mathcal{G}\in N_{b^{\ast}}M$; $\alpha=\varepsilon^2|v_\mathcal{G}|_{g^{\rm FR}}$.
Co-location is temporal filtration shift (different and weaker).

**R21. Dyson Class Forced by Manifold Symmetry** *(RANDOM_MATRIX)*
CAPM $\to$ GOE ($\beta=1$); Clifford torus $\to$ GUE ($\beta=2$, Berry phase);
pseudo-Anosov $\to$ GSE ($\beta=4$, symplectic foliation). Not a modelling choice.

**R22. Selberg Integral = MUP Partition Function** *(RANDOM_MATRIX)*
$\mathcal{Z}_T^M = S_r(Tb^{\ast}-1/2,\, Tb^{\ast}-1/2,\, \beta/2)$. Exact closed form.
MUP normalisation constant computable analytically for all three market types.

**R23. Tracy-Widom $F_\beta$ = Largest Factor Eigenvalue Distribution** *(RANDOM_MATRIX)*
Crisis signal: exceedance of the $F_\beta$ edge. Market-type specific.

**R24. Vandermonde Repulsion = Fisher-Rao Diversification Pressure** *(RANDOM_MATRIX)*
$|\lambda_i-\lambda_j|^\beta$ is the Fisher-Rao force keeping factor loadings separated.
GUE ($\beta=2$) provides stronger diversification than GOE ($\beta=1$).

**R25. Shapley Attribution $\phi_i = b^{\ast}_i(\mu_i-\bar\mu)$** *(HYPERCUBE_SHAPLEY)*
Proved: the Shapley value of asset $i$ in the Kelly cooperative game equals the
Fisher-Rao gradient of the Kelly rate at $b^{\ast}$. Unique fair attribution satisfying
all four Shapley axioms. Factor Shapley = unique fair factor attribution.

**R26. Walsh Functions = Jacobi Polynomials on the Simplex** *(HYPERCUBE_SHAPLEY)*
Walsh functions restricted to $\Delta_{d-1}$ are Jacobi polynomials. Barycentric
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
**R80.** Cap-weight Kelly shortfall = $(1/2)d^2_{g^{\rm FR}}(b^{\rm cap}, b^{\ast})$ *(BETTER_INDEX_FUND)* — the Fisher-Rao distance from cap-weight to log-optimal quantifies suboptimality
**R81.** Equal weight dominates cap weight in Fisher-Rao distance *(BETTER_INDEX_FUND)* — $\mathbb{E}[d_{g^{\rm FR}}(b^{\rm ew}, b^{\ast})] \leq \mathbb{E}[d_{g^{\rm FR}}(b^{\rm cap}, b^{\ast})]$
**R82.** Optimal rebalancing frequency = Jacobi spectral gap *(BETTER_INDEX_FUND)* — $f^{\ast} \approx \lambda_1^{\rm CS} \approx 12$/year (monthly)

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

## Tier 4: Conjectures With Strong Motivation (19 results)

**R50.** Jones polynomial = market partition function
**R51.** Topological EMH: $J_\Gamma(q)=1\iff$CAPM
**R52.** #**P**-hardness of return prediction
**R53.** Pseudo-Anosov markets simulate Rule 110 (Turing complete)
**R54.** Topologically protected alpha from $c_1(NM)\neq0$
**R55.** Berry phase = adiabatic alpha from correlation cycles
**R56.** RG beta function $\beta_H=-H/2$ + running Sharpe (one-loop open)
**R57.** Penrose tilings on the five-asset simplex ($\phi^2$ appears four ways)
**R58.** LLM training dynamics = MCF in model weight space
**R59.** LMSR on options market = geometric Black-Scholes
**R60.** Attention head effective rank converges to $r$
**R61.** Cheeger constant declined before 2008 GFC and 2022 LDI (testable)
**R76.** Modular bootstrap for Clifford torus returns: $\vartheta_3$ modular transformation relates short-time and long-time characteristic functions, constraining moments at all intermediate times
**R77.** Spectral gap lower bound from Sharpe ratio: $\lambda_1\geq f(\mathrm{Sharpe}^{\ast},\mathrm{vol}(M))$ via Cheeger inequality — lower bound on mean-reversion speed from observed Sharpe
**R78.** MUP as exponential family MLE: normalising constant is exponential family on $M^r$ with sufficient statistic $L_T$; Cramér-Rao gives $\mathrm{Var}(\hat b)\geq(TF_M)^{-1}$
**R79.** Bernstein-type theorem for market manifolds: minimal graph over factor simplex $\Rightarrow$ totally geodesic — independent proof of classification without Simons/Lawson-Simons
**R83.** Inflation = dual Fisher-Rao norm of sectoral inflation covector *(INFLATION_CAPITAL_FLOWS)* — geometric definition recovers headline CPI for uniform inflation, captures sectoral structure
**R84.** Fisher equation = holonomy of capital flow connection *(INFLATION_CAPITAL_FLOWS)* — real return = nominal minus Berry phase around goods market loop; path-dependent under heterogeneous inflation
**R85.** Taylor rule = LQG geodesic steering *(INFLATION_CAPITAL_FLOWS)* — Taylor coefficients are the LQG gains of a geometric PID controller on the financial-goods fiber bundle

**R86.** Manifold IS the channel *(MANIFOLD_IS_THE_CHANNEL)* — Fokker-Planck kernel on $M^r$ is a DMC with capacity $h_{\rm Kelly}$; Fisher-Rao metric of the channel = metric of the manifold. Self-referential channel (new type). Landauer's principle for markets.

**R87.** Confidence IS a σ-algebra *(CONFIDENCE)* — the set of events you're willing to commit capital on. Fourth wall of incompleteness (innermost). Grossman-Stiglitz as thermodynamic bound. Effective channel capacity $C_{\rm eff} = \bar\rho \cdot C_{\rm full}$.

**R88.** Wright-Fisher IS Jacobi *(BLOODSTOCK_MARKETS)* — population genetics and market portfolio dynamics are literally the SAME EQUATION. $\varepsilon^2 = 1/(2N_e)$. Every Jacobi result applies verbatim to allele frequency evolution.

**R89.** Thoroughbred $N_e \approx 300$ approaches Feller boundary *(BLOODSTOCK_MARKETS)* — closed Stud Book + small effective population → heterozygosity loss at rate $H/(2N_e)$. Dimension of $M_{\rm genetic}$ shrinking at rate $\sim 1/N_e$.

**R90.** BWT/CFL/LZ are three canonical filtrations *(FILTRATIONS)* — all asymptotically optimal, all converging to $h_{\rm Kelly}$, but resolving different structure: novelty (LZ), context (BWT), algebraic (CFL).

**R91.** Palindrome-Arbitrage theorem *(FILTRATIONS)* — six equivalent conditions: palindromic cycles ⟺ detailed balance ⟺ no arbitrage ⟺ time-reversibility ⟺ zero Berry phase ⟺ Gibbs measure. FX triangular arbitrage = palindromic deficit.

**R92.** De Bruijn graph IS the filtration *(FILTRATIONS)* — $B(N,n)$ at depth $n$ IS $\mathcal{F}^{\rm dB}_n$; iterated Delaunay. Directed graph is the market (Theorem 13.2).

**R93.** Radford-Hopf algebra of markets *(FILTRATIONS)* — concatenation = sequential strategies; shuffle = parallel strategies; antipode = time-reversal = palindromic sub-algebra. Lyndon words are primitives.

**R94.** GBM rejected at Z = 8.27 *(PALINDROMIC_SDE)* — S&P 500 palindromes (1926-present): observed 214 vs GBM predicts 114 at length 6. Excess grows exponentially with length. Z-scores 5-8 across all lengths.

**R95.** Fractional Palindromic SDE *(PALINDROMIC_SDE)* — the replacement for GBM: $dX_t = \kappa[\theta_t - X_t]dt + \sigma dB^H_t$ with $H < 1/2$ (anti-persistent). Reduces to GBM at $(\kappa \to 0, H \to 1/2)$.

**R96.** FPS from nested Pólya urns *(PALINDROMIC_SDE_CONSTRUCTION)* — discrete construction: center-outward growth + Pólya (exchangeability) + nested scales → FPS in continuous limit. Nesting ratio $\tau \approx \phi$ (golden ratio).

**R97.** Palindromic Black-Scholes formula *(PALINDROMIC_OPTIONS)* — $C = S\Phi(d_1^H) - Ke^{-rT}\Phi(d_2^H)$ with $d_i^H$ using effective variance $T^{2H} \cdot$ OU-factor. Vol smile emerges from first principles. New Greek: Hurst Vega.

**R98.** Six palindromic universality classes *(PALINDROMIC_SEQUENCES)* — Sturmian, Episturmian, Arnoux-Rauzy, Pisot, Thue-Morse, Bernoulli. Each has distinct palindromic density, Fourier spectrum, and symbolic complexity.

**R99.** Sturmian palindrome zeta = $\zeta(s-1) + \zeta(s)$ *(PALINDROMIC_SEQUENCES)* — Riemann zeta function literally appears in palindrome counting of Sturmian sequences. Direct identity.

**R100.** Palindromic Takens attractors are orbifolds *(PALINDROMIC_ATTRACTORS)* — $\mathbb{Z}_2$-orbifolds with palindromic centres as fixed points. Six topological classes: $S^1$, $T^r$, Rauzy fractal, Cantor-like, space-filling.

**R101.** Fisher-Rao is doubly natural *(PALINDROMIC_ATTRACTORS)* — unique metric that is both Čencov-invariant (reparameterisation) AND palindromic-invariant (reflection). Strengthens Čencov.

**R102.** Persistent homology is complete invariant *(PALINDROMIC_SIMPLICIAL_COMPLEXES)* — six palindromic classes have six distinct homotopy types ($S^1$, $T^r$, Rauzy complex, $K(\mathbb{Z}[1/2], 1)$, etc). Persistence diagram uniquely identifies class.

**R103.** MCF = discrete Morse gradient on eertree *(PALINDROMIC_SIMPLICIAL_COMPLEXES)* — two independent constructions (geometric flow on manifold, combinatorial flow on nerve complex) give the SAME FLOW.

**R104.** Palindromes under RG flow *(RENORMALIZATION)* — palindromic density is RG-invariant; Hurst exponent is RG-invariant critical exponent; Sturmian is attractive IR fixed point; Willmore decreases monotonically (Zamolodchikov c-theorem).

**R105.** Coase theorem IS palindrome-arbitrage theorem *(MICROECONOMIC_GEOMETRY)* — path-independence of bargaining = palindromic cycles = zero Berry phase. Transaction costs = Landauer costs = palindromic deficit.

**R106.** Deadweight loss IS Willmore energy *(MICROECONOMIC_GEOMETRY)* — Harberger triangle is the leading-order approximation to the integrated squared mean curvature. Optimal taxation = Willmore minimisation.

**R107.** MSY = Kelly rate *(FISHERIES_MARKETS)* — maximum sustainable yield of a fishery is the Kelly growth rate of the population simplex. ITQ = reflecting Feller boundary. Tuna farming = Type II reverse MCF singularity.

**R108.** Markets are palindromic by overdetermination *(WHY_MARKETS_ARE_PALINDROMIC)* — eleven independent forces (arbitrage, mean reversion, Landauer, Fisher-Rao, ESS, Maxwell's demon, counter-cyclical regulation, microstructure, psychology, RG flow, Coase) each force palindromic structure. Canalised outcome.

**R109.** Market Structure Theorem *(MARKET_STRUCTURE_THEOREM)* — a market is completely specified by $(B(N, n^{\ast}), \mathcal{E})$: the de Bruijn graph at empirical depth and the eertree embedding (palindromic sub-walks). Three structural layers: ambient (all contexts), equilibrium (palindromic sub-graph), transient (non-palindromic edges = arbitrage).

**R110.** Palindromic fraction as efficiency measure *(MARKET_STRUCTURE_THEOREM)* — $\rho_{\rm market} = |\mathcal{E}|/|\text{Walks}(B)|$ is the key structural invariant. Mature equity markets conjecturally at $\rho_{\rm market} \approx 1/\phi^2 \approx 0.382$ (golden-ratio equilibrium). Crises cause rapid de-palindromisation.

**R111.** Kelly rate comes from palindromic sub-graph only *(MARKET_STRUCTURE_THEOREM)* — $h_{\rm Kelly} = \log\rho(A_{\mathcal{E}})$, the Perron-Frobenius eigenvalue of the palindromic adjacency matrix. Non-palindromic edges contribute only transiently to wealth growth.

**R112.** Palindrome-de Bruijn correspondence *(FILTRATIONS/MARKET_STRUCTURE_THEOREM)* — palindromic factors correspond to reversal-symmetric walks in the de Bruijn graph. The eertree is the palindromic sub-structure of de Bruijn.

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
| 6 — Palindromic/structural (R86–R112) | 27 |
| **Total** | **112** |

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
