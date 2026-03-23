# The Geometry of Efficient Markets
## Extended Abstract and Publisher Overview

*Minimal Surfaces, Universal Portfolios, and the Mathematics of Financial Markets*

---

> *"We asked why a Laplace approximation works unusually well.
> The answer was differential geometry. The geometry explained everything —
> and then proved that no AI can beat it, that the path integral you priced
> derivatives with constrains to a manifold, and that the appropriate random
> matrix ensemble is not a choice but a theorem."*

---

## The Origin

A single technical question opened a chain of mathematical connections that
became a monograph: why does Cover's universal portfolio \[1991\] achieve
$O(1/T^2)$ accuracy in its Laplace approximation rather than the $O(1/T)$
that Bayesian approximation theory predicts?

The answer — Cover's prior is the Jeffreys prior, the unique stationary
distribution of the natural diffusion on the efficient market manifold — led
to 35 papers, approximately 145,000 words, and a complete geometric theory
of financial markets connecting to differential geometry, information theory,
quantum field theory, random matrix theory, knot theory, braids, computation,
filtrations, geospatial indexing, machine learning, chaos theory, cooperative
game theory, and two centuries of financial history.

The organising principle throughout: **a financial market is a minimal submanifold
of the Bhattacharyya sphere; portfolio weights are barycentric coordinates on a
simplex; and every important quantity in finance is a computable geometric invariant
of this submanifold.**

---

## Part I: The Core — Simplex, Manifold, Central Theorems

**The FK-WKB identity.** Cover's simplex integral satisfies a Feynman-Kac PDE on
$(\Delta_{d-1}, g^{\rm FR})$. The WKB expansion identifies the Fisher information
matrix as the action Hessian; the Van Vleck-Morette determinant equals $F(b^*)$;
the $O(1/T^2)$ accuracy follows from Cover's prior being the Jeffreys prior.

**The Sharpe-curvature theorem** (proved): $\mathrm{Sharpe}^* = \|H\|_{L^2(M)}$.
The vol skew of index options measures $H$ in real time.

**Classification** (proved): only CAPMs are stably efficient.
The Clifford torus has stability index 5 — LTCM had five convergence strategies.

**MUP** (proved): regret $r\log T/2T$ — minimax optimal, 12× improvement for $d=50$, $r=4$.

## Part II: Physics, Processes, and Measure Theory

Exact stochastic processes forced by topology: Jacobi diffusion (CAPM), theta function
$\vartheta_3$ (Clifford torus — exact closed-form option pricing), McKean hyperbolic
BM (pseudo-Anosov — geometric vol smile without stochastic volatility, Cauchy tails).
Fat tails proved three ways: $\alpha=r/2$. Fokker-Planck stationary distribution =
Jeffreys prior (closes Cover's 30-year gap). Doob-Meyer compensator = Willmore energy.
Optimal randomised stopping = MUP posterior. Feller boundary = geometric proof of
diversification.

## Part III: Topology, Computation, Filtrations

Knot theory classifies markets: Jones polynomial = market partition function; topological
EMH $J_\Gamma=1\iff$CAPM; Alexander polynomial roots = factor rotation eigenvalues.
Braids: Yang-Baxter = no braiding arbitrage; pseudo-Anosov = chaotic efficient market;
market is a $\#\mathbf{P}$ oracle. Prediction complexity hierarchy:
$\mathbf{P}$ (sign) $\to$ $\#\mathbf{P}$ (exact return) $\to$ $\Pi_2^0$ (long-run)
$\to$ $\mathbf{PPAD}$ (equilibrium). Filtrations: Voronoi atoms explicitly constructed;
LZ prefix tree = filtration tree (general: any grammar-based compressor = valid
filtration); Clifford torus winding number = momentum/contrarian classification.

## Part IV: Geospatial, Contagion, LLMs, Random Matrices, Path Integrals

**Geospatial** (new): H3/S2/Hilbert on $S^{d-1}_+$; contagion = Delaunay graph
(endogenous, not exogenous); Cheeger constant = systemic risk; Hawkes criticality =
efficiency.

**LLMs** (new): LMSR-softmax-Fisher identity (transformer attention = LMSR market
making); LLM convergence theorem (no model beats the MUP on an efficient market,
regardless of architecture or compute); optimal transformer dimension = $r$; Kelly
rate = minimum cross-entropy loss; insider information lives in the normal bundle.

**Random matrices** (new): Dyson class $\beta\in\{1,2,4\}$ forced by manifold symmetry —
not a modelling choice. CAPM $\to$ GOE ($\beta=1$); Clifford torus $\to$ GUE
($\beta=2$, Berry phase breaks time-reversal); pseudo-Anosov $\to$ GSE ($\beta=4$,
symplectic foliation). Selberg integral = MUP partition function (exact, closed form).
Tracy-Widom $F_\beta$ = distribution of largest factor eigenvalue. Vandermonde repulsion
= Fisher-Rao diversification pressure. Dyson BM = factor eigenvalue dynamics.

**Path integrals** (new): constrained geometric Wiener measure on $M^r$ rather than
all of $\mathbb{R}^d$. WKB saddle = geodesic = LAPLACE.md (Van Vleck = Fisher matrix).
Theta function = winding sum over $\pi_1(T^2)=\mathbb{Z}^2$. McKean = unique geodesic
on $\mathbb{H}^2$. Risk-neutral measure on $M$: efficient market means $\mathbb{P}=\mathbb{Q}$.
Novikov condition = finite Willmore energy. Normal bundle integration = incompleteness
premium. Langevin equation generates the same diffusion via Parisi-Wu stochastic quantisation.

## Part V: Chaos, Embedding, Hypercubes, Shapley

**Chaos/Takens** (new): deterministic chaos and stochastic processes on $M^r$ generate
the same statistics (Oseledets equivalence — whether the market is "really" chaotic
or stochastic is unobservable and irrelevant). Feigenbaum constants $\delta=4.669$
and $\alpha=2.502$ govern the period-doubling bifurcation from CAPM to pseudo-Anosov
dynamics. Takens embedding theorem: the delay embedding of a single return series
into $\mathbb{R}^{2r+1}$ recovers $M^r$ topologically. Optimal delay $\tau = 1/\lambda_1$
(Jacobi spectral gap). Practical three-step algorithm for market manifold estimation
from one observable using diffusion maps.

**Hypercubes/Shapley** (new): $\Delta_{d-1}\subset[0,1]^d$ (simplex inside hypercube);
Walsh-Hadamard functions on $[0,1]^d$ restricted to $\Delta_{d-1}$ = Jacobi polynomials;
barycentric subdivision = Voronoi Delaunay (proved); Walsh ANOVA = Shapley decomposition.
Shapley value of asset $i$ in Kelly game = $\phi_i = b^*_i(\mu_i-\bar\mu)$ (proved —
the unique fair attribution of Kelly growth satisfying efficiency, symmetry, dummy, linearity).
Factor Shapley = unique fair factor attribution. Normal bundle projection of Shapley =
unexplained alpha. Banzhaf power index = Walsh-Fourier coefficient.

---

## The 25+ Proved Results

The monograph contains at least 25 fully proved new results. The five most important:

1. $\mathrm{Sharpe}^* = \|H\|_{L^2}$ — the alpha budget is observable from vol skew
2. Only CAPMs stably efficient — explains LTCM (stability index 5)
3. MUP regret $r\log T/2T$ — 12× practical improvement, minimax optimal
4. Dyson class forced by manifold symmetry — not a modelling choice
5. Shapley attribution $\phi_i = b^*_i(\mu_i-\bar\mu)$ — unique fair attribution proved

---

## Historical Grounding

A dedicated chapter reads two centuries of financial history through the geometric
lens — LTCM (Clifford torus stability index 5 = five simultaneous failure modes,
predictable from the 1973 Lawson-Simons theorem), 2008 GFC (Cheeger constant
collapse), Flash Crash (Hawkes supercriticality), Rothschild at Waterloo (normal
bundle information advantage), Buffett (optimal stopping on the great sphere,
"circle of competence" = Voronoi cell), LDI crisis 2022 (Feller boundary failure
from leverage). Scholarly grounding via Kindleberger, Ferguson, Minsky, Shiller.

---

## Practical Impact

**For the quant practitioner:** MUP algorithm (12× regret improvement), geometric
pairs trading thresholds ($z^*=\sqrt{1+r/\kappa}$), optimal transformer dimension
for market ML ($d_{\rm model}=r$), Kelly rate as ML loss calibration benchmark,
Shapley attribution of portfolio alpha to assets and factors.

**For the risk manager:** Cheeger constant as leading crisis indicator, Dyson class
as model-free symmetry test, Tracy-Widom $F_\beta$ as largest eigenvalue crisis signal.

**For the theorist:** A complete geometric framework unifying portfolio theory,
information geometry, stochastic processes, topology, random matrices, and path integrals.

---

## For the Publisher

**The work is new.** 25+ proved results not in the existing literature.
The LMSR=softmax=Fisher identity alone justifies a paper in a top ML venue.
The Dyson-manifold correspondence, Selberg=MUP, Shapley=Fisher-Rao gradient,
and Takens embedding of market manifolds are all independently publishable.

**The scope is managed.** Single organising principle. Five-part structure.
Speculative results clearly labelled. Historical chapter explicitly interpretive.

**Three distinct audiences:** mathematical finance, ML/AI, mathematical physics.
A fourth — sophisticated practitioners — is served by the anecdotes, experiments,
and open-source code.

**35 documents, approximately 145,000 words of draft material available for review.**
Open-source replication suite ready for public release.

---

*"The market teaches the same lessons over and over.
The geometry tells us why. The path integral shows us how.
Takens' theorem says we could have seen the manifold all along —
hiding in a single return series."*
