# TO DO: Papers Needed for a Definitive Monograph

**Saxon Nicholls** — me@saxonnicholls.com

**Last updated:** Session 2

---

## Current State

**45 papers · ~226,000 words · 85 results · 30 conjectures · 34 open problems**

---

## Tier 1 — Major Gaps (a reviewer would flag these immediately)

### 1. CREDIT_RISK.md
Default = hitting the Feller boundary of the firm's asset simplex. The credit
spread IS the distance from the boundary. CDO = fiber bundle over the
correlation structure. Recovery rate = re-entry point after boundary absorption.
CDS pricing in Fisher-Rao geometry. The 2008 crisis as a mass Feller boundary
event. Merton model, reduced-form models, and structural models all as special
cases of the manifold framework.

### 2. FIXED_INCOME_YIELD_CURVES.md
The yield curve is an infinite-dimensional manifold (a curve in the space of
discount factors). Nelson-Siegel = 3-factor model (level, slope, curvature) =
$r = 3$ on a 3-dimensional manifold. HJM as a stochastic PDE on the yield
manifold. Short-rate models (Vasicek, CIR, Hull-White) as Jacobi-type
diffusions on the rate simplex. Yield curve inversion as a topological signal
(the curve crosses itself = a self-intersection of the manifold). The term
premium as mean curvature of the yield manifold.

### 3. VOLATILITY_SURFACE.md
The vol surface = a 2D manifold in the space of option prices, parameterised
by (strike, maturity). SVI parameterisation as a coordinate system. No-arbitrage
constraints (Gatheral) as curvature conditions on the manifold. The vol smile
as mean curvature in the strike direction. The vol term structure as mean
curvature in the maturity direction. Vol-of-vol = Willmore energy of the vol
surface. The SABR model as a stochastic process on the vol manifold.

### 4. REAL_DATA_EXPERIMENTS.md
Empirical validation on real market data. Priority experiments:
- Estimate $r$ from S&P 500 daily returns (stable rank, FNN, Grassberger)
- Compute Sharpe-curvature identity empirically: does $\mathrm{Sharpe}^*$
  correlate with estimated $\|H\|_{L^2}$?
- Measure the spectral gap $\lambda_1$ from autocorrelation of factor returns
- Test the three market types: which sectors are CAPM/Clifford/pseudo-Anosov?
- Verify MUP regret bound: does the MUP outperform Cover by the predicted ratio?
- Compute Cheeger constant before and during the 2008 and 2020 crises
- Estimate the AH premium parity manifold Jacobi eigenvalue
- Test the FLB Sharpe prediction from HORSE_RACING against Pinnacle odds data
Without real data, the theory floats. This is the most important gap.

### 5. MARKET_MICROSTRUCTURE.md
The limit order book (LOB) as a measure-valued process on the price axis. The
bid-ask spread = Fisher-Rao distance between buy and sell distributions. Market
impact = curvature of the LOB manifold. Kyle's lambda = Fisher information of
the informed trader's signal. The Almgren-Chriss optimal execution model
(already in STOCHASTIC_CONTROL) reinterpreted as geodesic execution on the LOB
manifold. High-frequency trading as fast MCF on a microstructure manifold with
tiny spectral gap.

---

## Tier 2 — Important for Completeness

### 6. RISK_MEASURES.md
VaR, CVaR, expected shortfall, coherent risk measures (Artzner et al. 1999)
as convex functionals on $\Delta_{d-1}$. A coherent risk measure IS a convex
function on the information simplex (direct connection to Paper 0.1). Spectral
risk measures as weighted integrals over the return distribution. The dual
representation of coherent risk measures via the Fenchel conjugate (connecting
to CONVEXIFICATION Legendre-Fenchel section). Risk budgeting as a simplex
allocation problem with Fisher-Rao constraints.

### 7. OPTIMAL_TRANSPORT.md
Wasserstein distance vs Fisher-Rao distance: both metrics on probability
distributions, measuring different things. Fisher-Rao = local information
distinguishability. Wasserstein = global transport cost. The Wasserstein-Fisher-Rao
(WFR) metric as the natural hybrid. Portfolio rebalancing as optimal transport
on the simplex: moving from current weights to target weights at minimum cost.
The Benamou-Brenier formula for the Wasserstein distance as a fluid dynamics
problem on the simplex. Connection to FOKKER_PLANCK (the FP equation IS the
gradient flow of KL divergence in the Wasserstein metric).

### 8. MEAN_FIELD_GAMES.md
Large populations of interacting agents on the simplex. Each agent does local
MCF; collective behaviour is a mean-field game. Nash equilibria on the market
manifold. The MFG PDE = Fokker-Planck + Hamilton-Jacobi coupled system.
Formalises "traders as curvature reducers" from WHY_MARKETS_EVOLVE Section 3.
The representative agent IS the MUP. Heterogeneous agents give a distribution
over strategies = an element of $\mathcal{P}(\Delta_{d-1})$ = Level 2 of the
Giry tower. Connection to PREDICTION_MARKETS (the LMSR is the mean-field limit
of many interacting Bayesian agents).

### 9. CATEGORY_THEORY.md
The Giry monad developed properly. The category of Markov kernels. The Fisher
metric as a natural transformation. The MUP as a universal construction. Functorial
properties of the Bhattacharyya embedding. The Kleisli category and its role in
the data processing inequality. String diagrams for market interactions. This is
the paper for the pure mathematicians and the applied category theory community.

### 10. QUANTUM_FINANCE.md
Develop the quantum case properly rather than leaving it as "future work." The
Bures metric replacing Fisher-Rao. Density matrices as the quantum state space.
CPTP maps as quantum channels. The Petz classification of monotone metrics
(the quantum Čencov). Quantum game theory on the density matrix space. Quantum
computing for portfolio optimisation (the Grover speedup for simplex search).
The non-commutative Giry monad. Scope: either develop it or explicitly scope it
out with a clear statement of what would be needed.

---

## Tier 3 — Would Make It Truly Comprehensive

### 11. CLIMATE_ESG.md
Climate risk as a manifold deformation (the market manifold changes shape as
climate policy tightens). Carbon pricing as an external force on MCF. ESG scores
as projections of the Fisher matrix onto a sustainability basis. Stranded assets
= Feller boundary absorption (fossil fuel assets hitting zero). The transition
risk manifold. Green bonds as a new neck connecting the climate and financial
manifolds.

### 12. CRYPTOCURRENCY_DEFI.md
AMMs (Uniswap) as geometric market makers on the simplex — the constant product
formula $xy = k$ is a specific curve on $\Delta_1$. Liquidity pools as fiber
bundles. Impermanent loss = Willmore energy of the AMM curve relative to the
minimal surface. DeFi as market microstructure without intermediaries. MEV
(maximum extractable value) as curvature exploitation by validators. The five
stages applied to crypto: Bitcoin (Stage 4), Ethereum (Stage 3), DeFi tokens
(Stage 2), memecoins (Stage 1-2).

### 13. NETWORK_EFFECTS_PLATFORMS.md
Platform economics as network graph theory. Metcalfe's law ($V \propto n^2$)
as a Cheeger constant result (the value of a network is proportional to its
connectivity). Platform monopoly = star-graph topology. Two-sided markets as
bipartite graphs with the platform as the Cheeger bottleneck. Antitrust for
platforms = Cheeger surgery (add edges that bypass the platform). Connection to
TOPOLOGY_OF_PRICE.

### 14. BEHAVIORAL_FINANCE.md
Prospect theory in geometric terms. Kahneman-Tversky probability weighting
$w(p)$ is a MAP from $\Delta_{d-1}$ to $\Delta_{d-1}$ — a distortion of the
simplex. Loss aversion = asymmetric Fisher-Rao metric (different curvature for
gains vs losses). Overconfidence = underestimation of the spectral gap (the
agent thinks information is priced faster than it is). Herding = agents clustering
on the manifold (Cheeger constant dropping). The FLB (HORSE_RACING) as a specific
instance of probability distortion.

### 15. HISTORICAL_DATA.md
Deep historical case studies using the five-stage framework:
- Amsterdam stock exchange (1602-): the first modern market, all five stages
- South Sea Bubble (1720): Type II singularity, topology change (South Sea Co dissolved)
- Railroad mania (1840s): Stage 2 → Stage 5 → Stage 3 in one decade
- Long Depression (1873-96): a 23-year MCF convergence after the railroad singularity
- Bretton Woods (1944-71): a forced manifold (fixed exchange rates) that accumulated
  Willmore energy until Nixon severed the neck
- The Asian crisis (1997): contagion as Cheeger failure across the Asian market graph
- Dot-com bubble (2000): the tech sector as a local curvature blowup

---

## Tier 4 — Would Distinguish It from All Competitors

### 16. INSURANCE.md
Insurance as a market on the loss distribution simplex. The insurance premium =
Fisher-Rao distance from the insured's loss distribution to the insurer's portfolio
distribution. Reinsurance as a fiber bundle (primary → reinsurer → retrocessionaire).
Lloyd's of London as a connected sum of specialty market manifolds. Catastrophe
bonds as necks connecting insurance and financial manifolds. Actuarial science
meets information geometry.

### 17. REAL_ESTATE.md
Real estate as an extremely illiquid market manifold (like art but with cash flows).
Hedonic pricing = factor projection (location, size, age, quality → $r \approx 4$).
The housing bubble as MCF singularity (2006-2008 US). REITs as fractionalisation
(like the art market theorem). The cap rate as the spectral gap of the property
manifold. Rental yield as the Kelly growth rate of the property simplex.

### 18. ENERGY_MARKETS.md
The full energy complex beyond Brent-WTI: crude, products, natural gas, power,
renewables, carbon. Each with its own manifold, connected by refining/conversion
correspondence maps. The crack spread, spark spread, and dark spread as parity
manifold displacements (INTERMARKET_GEOMETRY Cases 2-3). The energy transition
as a manifold deformation: the factor structure shifts from fossil to renewable
over decades. Storage (contango/backwardation) as the convenience yield on the
temporal fiber bundle.

### 19. AGRICULTURAL_COMMODITIES.md
Food markets connecting to TOPOLOGY_OF_PRICE (famine as Cheeger failure). The
agricultural simplex with seasonal factors as the cyclic group $\mathbb{Z}_{12}$
from DUAL_TOWER. Storage, spoilage, and harvest cycles. The green revolution as
a manifold expansion (more goods, higher r). Food speculation and its effect on
Cheeger constants of the food distribution graph. Connection to the enclosure
analysis.

### 20. MACHINE_LEARNING_GEOMETRY.md
The geometry of ML beyond the LLM result. The loss landscape as a Riemannian
manifold (the Hessian of the loss = the metric tensor). SGD as MCF on the loss
surface (gradient descent IS mean curvature flow on the weight manifold).
Batch normalisation = Fisher-Rao normalisation (proven by several authors). The
natural gradient (Amari 1998) as the geometrically correct optimiser — it uses
the Fisher-Rao metric instead of Euclidean. Adam/AdaGrad as approximations to
the natural gradient. This is the bridge paper to the ML community.

---

## Priority Order for Writing

1. **REAL_DATA_EXPERIMENTS** — without this, the theory floats
2. **CREDIT_RISK** — largest gap for a finance monograph
3. **FIXED_INCOME_YIELD_CURVES** — essential for fixed-income completeness
4. **VOLATILITY_SURFACE** — essential for derivatives completeness
5. **MARKET_MICROSTRUCTURE** — essential for trading applications
6. **RISK_MEASURES** — connects to the convexity foundations
7. **OPTIMAL_TRANSPORT** — connects to rebalancing and FP equation
8. **MEAN_FIELD_GAMES** — formalises the trader-as-curvature-reducer story
9. **MACHINE_LEARNING_GEOMETRY** — bridge to the ML community
10. **BEHAVIORAL_FINANCE** — bridge to the economics community

---

## The Test for "Definitive"

A monograph is definitive when a researcher in ANY area of mathematical finance,
information geometry, or economic theory can open it and find their topic treated
geometrically with original results. We are approximately 60% there. The Tier 1
papers would bring us to ~80%. Tiers 2-3 would bring us to ~95%.

The remaining 5% is empirical validation — which requires REAL_DATA_EXPERIMENTS
more than any additional theory.

---

*"The geometry explains everything because the geometry IS everything."*
