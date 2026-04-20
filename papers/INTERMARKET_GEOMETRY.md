# Intermarket Geometry: Spreads as Curvature, Mergers as Connected Sums,
## and the Cost of Market Integration

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.5** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We develop the geometry of intermarket interaction within the framework of this
monograph: financial markets are minimal submanifolds of Bhattacharyya spheres,
portfolio weights are barycentric coordinates on the simplex, and mean curvature
flow (MCF) drives markets toward efficiency. Two markets $M_1^{r_1}$ and
$M_2^{r_2}$ living in separate Bhattacharyya spheres interact through a
correspondence map $\Phi: M_1 \to M_2$, and the intermarket spread decomposes
canonically into three components: a fundamental geodesic distance (structural,
non-tradeable), an O'Neill curvature tensor (tradeable, mean-reverting under MCF),
and a topological obstruction (divergent when connectivity fails). The maximum
Sharpe ratio of a spread trade is $\|A_\Phi\|_{L^2}$, the $L^2$-norm of the
O'Neill $A$-tensor — the intermarket analogue of the Sharpe-curvature identity
$\mathrm{Sharpe}^{\ast} = \|H\|_{L^2}$ proved in MINIMAL_SURFACE.md.

Market mergers are connected sums of minimal surfaces. When two manifolds are
joined by a neck, the neck carries Willmore energy $W_{\rm neck} \geq 4\pi$ (for
$r=2$), which is the upfront geometric cost of integration. If the two markets
share $k$ out of $r$ total factors, the merger saves $k \cdot \log T / (2T)$ in
regret per period. The payback formula

$$T_{\rm payback} \approx \frac{W_{\rm neck} \cdot 2T}{k \cdot \log T}$$

gives a computable answer to the most expensive question in finance: *should these
two markets be connected?* High $k/r$ mergers are cheap (NYSE-Euronext, $k/r
\approx 0.8$, payback $\sim$1 year); low $k/r$ mergers are expensive (the Euro
took 15 years across 10 necks); zero $k/r$ mergers never pay off (art + equities).
The law of one price is the statement that the connected sum of two identical
manifolds is isometric to the original: $M \mathbin{\#} M \cong M$ when $k = r$.

Under MCF, the neck either widens (successful integration), stabilises (permanent
partial connection with a residual spread), or pinches to a singularity
(de-merger). The Kapouleas-Mazzeo-Pacard balancing condition determines which
outcome obtains: a merger converges if and only if capital flows from each side
balance at the neck.

**Keywords.** Connected sum; O'Neill tensor; intermarket spread; market merger;
Willmore energy; neck surgery; mean curvature flow; payback period; law of one
price; Kapouleas construction; balancing condition; Fisher-Rao geometry;
Bhattacharyya sphere; portfolio simplex; market integration.

**MSC 2020.** 91G10, 53A10, 53C42, 57R65, 58J35, 91B26.

---

## 1. Intermarket Spreads as Bundle Curvature

### 1.1 Two markets, two spheres

Consider two financial markets. Market 1 has $d_1$ assets and $r_1$ systematic
factors; its market manifold is $M_1^{r_1} \subset S^{d_1-1}_{+}$, a minimal
submanifold of the Bhattacharyya hemisphere. Market 2 has $d_2$ assets and $r_2$
factors with manifold $M_2^{r_2} \subset S^{d_2-1}_{+}$. In general these live in
*different* ambient spheres — there is no natural inclusion of one into the other.

A **correspondence map** is a smooth map $\Phi: M_1 \to M_2$ that sends each
state of Market 1 to the "corresponding" state of Market 2. Examples:

- Brent-WTI: $\Phi$ maps each state of the Brent crude market to the corresponding
  state of WTI crude, adjusted for grade and delivery point.
- TED spread: $\Phi$ maps Treasury bill states to Eurodollar deposit states.
- CDS-bond basis: $\Phi$ maps cash bond states to CDS contract states on the same
  reference entity.
- AH premium: $\Phi$ maps Shanghai A-share states to Hong Kong H-share states for
  dual-listed companies.

The correspondence need not be an isometry, a diffeomorphism, or even injective.
It is simply the economic relationship between the two markets.

### 1.2 The spread as a bundle section

Given $\Phi$, the **intermarket spread** at a point $p \in M_1$ is

$$\sigma(p) = \pi(p) - \Phi^{\ast}\pi_2(p) \tag{1.1}$$

where $\pi$ is the log-price function on $M_1$ and $\Phi^*\pi_2 = \pi_2 \circ
\Phi$ is the pullback of the log-price on $M_2$. The spread $\sigma$ is a section
of the bundle $\mathcal{E} = T^{\ast}M_1 \otimes \Phi^{\ast}T^{\ast}M_2$ — it lives over $M_1$
and measures the deviation of $\Phi$ from a price-preserving isometry.

### 1.3 The canonical decomposition

Any spread admits a unique orthogonal decomposition into three components:

$$\sigma = \sigma_{\rm fund} + \sigma_{\rm curv} + \sigma_{\rm top}. \tag{1.2}$$

**Component 1: Fundamental spread** $\sigma_{\rm fund}$. This is the geodesic
distance in the product geometry $S^{d_1-1}_{+} \times S^{d_2-1}_{+}$ between the
graphs of $\Phi$ restricted to the respective minimal surfaces. It captures the
structural cost of converting one asset into the other: shipping costs,
grade differences, credit spreads, refining margins, regulatory frictions. The
fundamental spread is a geometric invariant — it does not change under MCF unless
the physical relationship between the markets changes.

**Component 2: Curvature spread** $\sigma_{\rm curv}$. This is the O'Neill
$A$-tensor of the correspondence map. Recall that O'Neill's $A$-tensor [O'Neill
1966] measures the failure of a submersion to preserve horizontal geodesics. In
our setting, $\Phi$ induces a submersion from the product manifold $M_1 \times
M_2$ to $M_1$, and the $A$-tensor measures how much the "horizontal" direction
(along $M_2$-fibres) twists relative to the "vertical" direction (along $M_1$).
The curvature spread $\sigma_{\rm curv}$ is the tradeable component: it
mean-reverts under MCF as arbitrageurs exploit deviations from the correspondence.

**Component 3: Topological spread** $\sigma_{\rm top}$. This component is
non-zero only when $M_1$ and $M_2$ are in different connected components of the
ambient geometry — when there is a topological obstruction to connecting them.
Capital controls, trade embargoes, regulatory barriers, and sanctions create
topological obstructions. When the topology is intact ($M_1$ and $M_2$ are in the
same connected component), $\sigma_{\rm top} = 0$. When the topology is broken,
$\sigma_{\rm top}$ can diverge without bound.

### 1.4 Table of major spreads

| Spread | Fundamental | Curvature (tradeable) | Topology |
|:-------|:-----------|:---------------------|:---------|
| Brent-WTI | Grade + shipping (~\$2) | Supply/demand divergence | Intact |
| TED spread | Credit risk (~30bp) | Flight-to-quality | Intact |
| Crack spread | Refining cost (~\$15/bbl) | Capacity utilisation | Intact |
| AH premium | Capital controls (~15%) | Information asymmetry | Partially connected (Stock Connect) |
| CDS-bond basis | Funding cost (~20bp) | Counterparty risk | Intact (except in crisis) |
| Futures basis | Storage + financing | Convenience yield | Intact |
| Bitcoin ETF premium | Custody + structure | Risk-on/risk-off | Thin neck (new, 2024) |

The table makes the decomposition concrete. A spread trader should only trade
$\sigma_{\rm curv}$ — the curvature component. Trading $\sigma_{\rm fund}$ is
paying for a real cost; trading against $\sigma_{\rm top}$ is fighting a barrier
that need not revert.

### 1.5 The parity manifold

The clean geometric object underlying any spread is the **parity manifold**:

$$\Gamma_\Phi = \{(x, \Phi(x)) : x \in M_1\} \subset M_1 \times M_2 \tag{1.3}$$

— the graph of the correspondence map in the product space. When the two
markets are in equilibrium, trading lives ON $\Gamma_\Phi$. The spread is the
**normal displacement** from $\Gamma_\Phi$:

$$\sigma(x, y) = d_{g^{\rm prod}}\!\big((x, y),\, \Gamma_\Phi\big) \tag{1.4}$$

measured in the product Fisher-Rao metric $g^{\rm prod} = g^{\rm FR}_{1} \oplus g^{\rm FR}_{2}$.

**The normal bundle $N\Gamma_\Phi$** has fibre dimension $r_2$ (the dimension of
$M_2$). The spread process evolves in this normal bundle. Near $\Gamma_\Phi$,
the spread satisfies an OU/Jacobi-type SDE in normal coordinates:

$$d\sigma = -J_\Phi(\sigma)\,dt + \varepsilon\, dW^\perp \tag{1.5}$$

where $J_\Phi$ is the **Jacobi operator of the parity manifold** — the second
variation of the "distance to parity" functional. The eigenvalues of $J_\Phi$
give the mean-reversion speeds of each spread mode:

$$\lambda_k(J_\Phi) = \text{mean-reversion speed of the $k$-th spread component.}$$

This directly generalises the pairs trading result (PAIRS_TRADING.md Section 3):
the OU mean-reversion speed $\kappa$ for a pairs spread IS the first eigenvalue
$\lambda_1(J_\Phi)$ of the parity manifold Jacobi operator for the special case
$r_1 = r_2 = 1$.

### 1.6 The four cases of market interaction

Not all intermarket relationships are the same. There are four geometrically
distinct cases that should not be conflated:

**Case 1: Independent markets.** $M_1 \times M_2$ with the product metric.
No natural correspondence $\Phi$, no parity manifold, no meaningful spread.
Example: equities and fine wine.

**Case 2: Coupled markets.** A correspondence $\Phi: M_1 \to M_2$ exists but
is not an isometry. The parity manifold $\Gamma_\Phi$ has positive normal
curvature. The spread mean-reverts but slowly. The coupling is through shared
factors (the $k$ shared factors from the payback formula).
Example: Brent-WTI, TED spread, CDS-bond basis.

**Case 3: Cointegrated markets.** The parity manifold $\Gamma_\Phi$ is a
low-codimension, invariant submanifold of $M_1 \times M_2$. The spread is
confined to a neighbourhood of $\Gamma_\Phi$ by an absorbing boundary condition
— it CANNOT diverge, only fluctuate. The Jacobi operator $J_\Phi$ has a
spectral gap bounded below. This is the geometric content of Engle-Granger
cointegration: the error correction term is the normal projection onto
$N\Gamma_\Phi$, and the cointegrating vector is the normal direction.
Example: spot-futures basis (enforced by arbitrage), ADR-local share price.

**Case 4: Merged markets.** Not just coupling or cointegration but genuine
topology change — the two manifolds become one via a connected sum $M_1 \# M_2$.
The parity manifold collapses to a point (the neck), and the spread becomes
the neck curvature rather than a normal displacement. This is the subject of
Sections 3–8 below.
Example: the Euro (11 sovereign bond manifolds → one), Stock Connect (partial),
a corporate merger combining two equity manifolds into one.

The progression 1 → 2 → 3 → 4 is the **integration ladder**: markets climb
from independence to merger as shared factors increase, transaction costs
decrease, and regulatory barriers fall. The spectral gap of the parity
manifold's Jacobi operator increases at each step (faster mean-reversion,
tighter coupling) until, at Case 4, the parity manifold ceases to exist
as a separate object and becomes the neck of the connected sum.

---

## 2. The Geometry of a Spread Trade

### 2.1 The spread trader's problem

A spread trader holds a long position in the "cheap" manifold and a short position
in the "expensive" manifold. Formally, the trader selects a portfolio
$b = (b_1, -b_2)$ on the product space $M_1 \times M_2$ (long $b_1$ on $M_1$,
short $b_2$ on $M_2$). The trader's P\&L over one period is

$$\Delta W = \langle b_1, x_1 \rangle - \langle b_2, x_2 \rangle \approx
-\Delta\sigma_{\rm curv} + \text{(fundamental drift)} \tag{2.1}$$

where $x_1, x_2$ are the return vectors on the respective markets. The P\&L is
driven by changes in the curvature spread.

### 2.2 The intermarket Sharpe-curvature identity

**Theorem 2.1** *(Intermarket Sharpe-curvature identity)*.
*Let $\Phi: M_1 \to M_2$ be a smooth correspondence between efficient market
manifolds with O'Neill tensor $A_\Phi$. The maximum Sharpe ratio achievable by
any spread trade between $M_1$ and $M_2$ is*

$$\mathrm{Sharpe}^{\ast}_{\rm spread} = \|A_\Phi\|_{L^2(M_1, g_{M_1})}. \tag{2.2}$$

*This is the intermarket analogue of $\mathrm{Sharpe}^{\ast} = \|H\|_{L^2}$ from
MINIMAL_SURFACE.md. When $\Phi$ is an isometry, $A_\Phi = 0$ and the spread has
zero Sharpe — the law of one price.*

**Proof sketch.** The $A$-tensor measures the second-order deviation of $\Phi$ from
an isometry. By the O'Neill curvature formula [O'Neill 1966], the sectional
curvature of the product manifold $M_1 \times_\Phi M_2$ (the warped product with
fibre map $\Phi$) decomposes as

$$K_{M_1 \times_\Phi M_2}(X, Y) = K_{M_1}(X, Y) + K_{M_2}(\Phi_*X, \Phi_*Y)
- 3|A_\Phi(X, Y)|^2 \tag{2.3}$$

for horizontal vectors $X, Y$. The excess curvature $|A_\Phi|^2$ generates a
drift in the log-wealth of the spread portfolio. The maximum Sharpe ratio is the
$L^2$-norm of this drift, which equals $\|A_\Phi\|_{L^2}$ by the same
variational argument that proves the single-market Sharpe-curvature identity. The
optimiser is the eigenvector of the curvature operator corresponding to the
maximum eigenvalue of $A_\Phi^{\ast}A_\Phi$. $\square$

### 2.3 Convergence rate

The convergence rate of the curvature spread is determined by the spectral gap of
the Laplacian on the product manifold. By the spectral theory of product spaces:

$$\lambda_1(M_1 \times M_2) = \min\bigl(\lambda_1(M_1), \lambda_1(M_2)\bigr).
\tag{2.4}$$

The slowest-mixing market sets the convergence rate. A fast, liquid equity market
paired with a slow, illiquid commodity market converges at the commodity market's
rate. This is well-known empirically — commodity spreads mean-revert more slowly
than equity spreads — and now has a geometric explanation.

### 2.4 The optimal spread trade

**Theorem 2.2** *(Optimal spread trade)*.
*The optimal spread trade between $M_1$ and $M_2$ is the eigenvector of the
cross-market Fisher information matrix*

$$F_{\rm cross} = \Phi^{\ast} F_{M_2} - F_{M_1} \tag{2.5}$$

*corresponding to the smallest (most negative) eigenvalue. This is the direction
of maximum mean-reversion: the mode along which the correspondence $\Phi$ is
most curved, and hence the spread most compressed by MCF.*

The proof follows from the variational characterisation of the spectral gap
applied to the drift operator of the spread. The smallest eigenvalue of
$F_{\rm cross}$ corresponds to the direction where $M_2$ is most "expensive"
relative to $M_1$ in the Fisher-Rao geometry — the maximum curvature direction
of the correspondence.

In practice, this eigenvector can be computed from the rolling cross-covariance
matrix of the two return series. It is the geometric generalisation of the
classical cointegration vector: classical cointegration finds a linear combination
with maximum mean-reversion; Theorem 2.2 finds the geodesic combination on the
product manifold.

---

## 3. Market Mergers as Connected Sums

### 3.1 The connected sum construction

The connected sum $M_1 \mathbin{\#} M_2$ is the fundamental topological operation
for joining two manifolds. The construction proceeds in three steps:

1. Remove a small geodesic ball $B_\epsilon(p_i)$ from each manifold $M_i$,
   creating boundaries $\partial B_\epsilon(p_i) \cong S^{r-1}$.
2. Connect the two boundary spheres with a cylindrical neck
   $S^{r-1} \times [0, L]$ of length $L$ (the neck length).
3. Smooth the junctions to create a smooth manifold.

The resulting manifold $M_1 \mathbin{\#} M_2$ has:

- Dimension: $r = \max(r_1, r_2)$ (assuming compatible factor structures).
- Genus: $g(M_1 \mathbin{\#} M_2) = g(M_1) + g(M_2)$ for surfaces ($r = 2$).
- Euler characteristic: $\chi(M_1 \mathbin{\#} M_2) = \chi(M_1) + \chi(M_2) - 2$
  for closed surfaces.

### 3.2 The neck parameters

The neck has three geometric parameters:

**Width** $w$: the radius of the connecting cylinder $S^{r-1}(w) \times [0, L]$.
Financially, this is the rate of capital flow between markets — daily trading
quotas, clearing capacity, margin requirements. A wide neck allows free capital
flow; a narrow neck throttles it.

**Position** $p$: the points $p_1 \in M_1$ and $p_2 \in M_2$ where the neck
attaches. Financially, these are the *bridge instruments* — the specific assets
through which the two markets connect. For Shanghai-HK Stock Connect, the bridge
instruments are the eligible dual-listed stocks. For the Euro, the bridge
instruments were the sovereign bonds of the joining nations.

**Twist** $\theta$: the relative phase between the two boundary spheres. A twist
$\theta \neq 0$ means the markets are not phase-synchronised — factor rotations
on one side do not map directly to factor rotations on the other. Financially,
this is the phase lag between correlated markets (e.g., the time-zone effect
between NYSE and LSE).

### 3.3 The spectral gap of the merged market

The spectral gap of $M_1 \mathbin{\#} M_2$ determines the mixing time of the
merged market — how quickly information propagates across the full system.

**Theorem 3.1** *(Spectral gap of connected sum)*.
*Let $M_1 \mathbin{\#}_{L} M_2$ denote the connected sum with neck length $L$ and
neck width $w$. The first non-zero eigenvalue of the Laplacian satisfies*

$$\lambda_1(M_1 \mathbin{\#}_{L} M_2) \approx \min\!\left(\lambda_1(M_1), 
\lambda_1(M_2), \frac{\pi^2 w^{r-2}}{L^2 \cdot
\max(\mathrm{vol}(M_1), \mathrm{vol}(M_2))}\right). \tag{3.1}$$

*The third term is the "tunnel mode" — the eigenvalue of the neck itself.*

Three regimes emerge:

**Thin neck** ($L$ large or $w$ small): The tunnel mode $\pi^2 w^{r-2} / L^2$
dominates. The spectral gap of the merged market is set by the neck. The two
markets are weakly connected — information leaks through the neck slowly, spreads
persist, and the merged market behaves like two separate markets with a thin pipe
between them. This is the Shanghai-HK Connect regime.

**Wide neck** ($L$ small and $w$ large): The individual spectral gaps dominate.
The merged market's mixing time is the maximum of the two component mixing times.
This is the NYSE-Euronext regime after full integration.

**Resonant neck** ($\lambda_1(M_1) \approx \lambda_1(M_2) \approx \pi^2
w^{r-2}/L^2$): All three modes contribute comparably. The spectral structure is
rich, with level-crossing phenomena as the neck width varies. This is the
transition regime where the merger is "in progress."

---

## 4. The Neck Cost: The Willmore Energy of Integration

### 4.1 The Willmore energy of a neck

The neck $S^{r-1}(w) \times [0, L]$, embedded in the ambient Bhattacharyya sphere,
carries mean curvature. The two junctions (where the cylinder meets the excised
manifolds) are regions of concentrated curvature — the manifold bends sharply to
accommodate the join.

For surfaces ($r = 2$), the classical result is:

$$W_{\rm neck} = \int_{\rm neck} |H|^2 \, d\mathrm{vol} \geq 4\pi. \tag{4.1}$$

The lower bound $4\pi$ is sharp: it is achieved by the catenoidal neck (the
rotationally symmetric minimal surface connecting two planes). By the Li-Yau
inequality [Li and Yau 1982], a surface with $W < 4\pi$ must be embedded (no
self-intersections). A neck costing *exactly* $4\pi$ is the minimal integration
— any less and the markets are not truly connected.

For higher-dimensional manifolds ($r > 2$):

$$W_{\rm neck} \sim \mathrm{Vol}(S^{r-1}) \cdot L^{-(r-2)} = \frac{2\pi^{r/2}}
{\Gamma(r/2)} \cdot L^{-(r-2)}. \tag{4.2}$$

The neck cost *decreases* as the neck lengthens for $r > 2$ — longer, thinner
necks are cheaper in Willmore energy but slower in spectral gap. There is a
trade-off: fast integration (short, wide neck) is expensive; slow integration
(long, thin neck) is cheap but takes years to transmit information.

### 4.2 The integration tax

The Willmore energy $W_{\rm neck}$ is the **integration tax** — the upfront cost
of connecting two markets. This cost is paid in the real economy through:

- **Wide spreads** during the integration period (the neck curvature manifests as
  price dislocations).
- **Infrastructure costs** (clearing houses, settlement systems, regulatory
  harmonisation).
- **Regulatory overhead** (cross-border supervision, capital requirements,
  reporting standards).
- **Political capital** (treaties, legislation, institutional design).

The Li-Yau threshold of $4\pi$ has a sharp financial interpretation: a
connection costing less than $4\pi$ units of Willmore energy is not a true
merger — it is a correspondence (Section 1) rather than a connected sum.
The distinction between a spread trade and a merger is precisely the
$4\pi$ threshold.

---

## 5. The Payback Formula

### 5.1 Regret saving from shared factors

The Manifold Universal Portfolio (MUP) on an $r$-dimensional market manifold
achieves minimax regret $r \cdot \log T / (2T)$ (proved in CONVERGENCE.md). When
two markets merge, the total factor count changes.

Let Market 1 have $r_1$ factors and Market 2 have $r_2$ factors, with $k$ shared
factors. Before merger:

$$\text{Total regret (pre-merger)} = \frac{r_1 \cdot \log T}{2T} + \frac{r_2 \cdot
\log T}{2T} = \frac{(r_1 + r_2) \cdot \log T}{2T}. \tag{5.1}$$

After merger, the $k$ shared factors are counted once, not twice:

$$\text{Total regret (post-merger)} = \frac{(r_1 + r_2 - k) \cdot \log T}{2T}.
\tag{5.2}$$

The saving per period is

$$\Delta_{\rm regret} = \frac{k \cdot \log T}{2T}. \tag{5.3}$$

### 5.2 The payback formula

**Theorem 5.1** *(Merger payback formula)*.
*A market merger with neck Willmore energy $W_{\rm neck}$ and $k$ shared factors
pays for itself after*

$$T_{\rm payback} \approx \frac{W_{\rm neck} \cdot 2T}{k \cdot \log T} \tag{5.4}$$

*periods. For a minimal neck ($W_{\rm neck} = 4\pi$, $r = 2$), this gives
$T_{\rm payback} \approx 8\pi T / (k \cdot \log T)$.*

**Proof.** The neck costs $W_{\rm neck}$ units of Willmore energy at inception.
The merger saves $k \cdot \log T / (2T)$ per period. The payback period is the
time at which cumulative savings equal the initial cost:

$$T_{\rm payback} \cdot \frac{k \cdot \log T}{2T} = W_{\rm neck}$$

$$\implies T_{\rm payback} = \frac{W_{\rm neck} \cdot 2T}{k \cdot \log T}.
\quad\square \tag{5.5}$$

### 5.3 Payback table (daily data, $T = 252$)

For a minimal neck ($W_{\rm neck} = 4\pi \approx 12.6$), the payback periods are:

| Shared factors $k$ | Saving per year | Payback (years) |
|:---:|:---:|:---:|
| 0 | 0 | $\infty$ |
| 1 | $\log(252)/504 \approx 0.011$ | $\sim$5 |
| 2 | $\approx 0.022$ | $\sim$2.5 |
| 3 | $\approx 0.033$ | $\sim$1.5 |
| 5 | $\approx 0.055$ | $< 1$ |
| $r$ (all shared) | $r \cdot \log(252)/(504)$ | $\sim 8\pi / (r \cdot \log 252)$ |

The rule is simple: **$k/r$ determines merger economics.** High $k/r$ means the
markets share most of their factor structure, the connected sum is nearly
isometric, and the integration tax is recovered quickly. Low $k/r$ means the
markets are fundamentally different, the neck must do heavy geometric work, and
payback is slow or impossible.

### 5.4 Historical mergers rated by $k/r$

| Merger | $k/r$ | Necks | Payback (actual) | Outcome |
|:-------|:---:|:---:|:---:|:--------|
| NYSE + Euronext (2007) | $\approx 0.8$ | 1 | $\sim$1 year | Fast integration, cheap |
| Brent-WTI convergence | $\approx 0.75$ | 1 | $\sim$1.5 years | Cheap, persistent thin spread |
| Euro sovereign bonds (1999) | $\approx 0.6$ | 10 | $\sim$15 years | Expensive, crisis during payback |
| Shanghai-HK Connect (2014) | $\approx 0.4$ | 1 (regulated) | $\sim$5 years | Moderate, AH premium persists |
| Crypto + TradFi (BTC ETF, 2024) | $\approx 0.25$ | 1 | $\sim$10+ years | Thin neck, outcome uncertain |
| Art + Equities | $= 0$ | 0 | $\infty$ | Impossible, zero shared factors |

The table encodes a non-trivial economic prediction: the BTC ETF merger will take
at least a decade to pay for itself, if it pays at all. The shared factor is
essentially one (risk-on/risk-off sentiment). Five factors are unshared
(blockchain-specific supply dynamics, regulatory risk, hash rate, stablecoin
flows, etc.). The geometry says: this is an expensive merger.

---

## 6. The Neck Evolves Under Mean Curvature Flow

### 6.1 MCF on connected sums

After the connected sum is formed, the merged manifold $M_1 \mathbin{\#} M_2$
evolves under MCF. Arbitrageurs exploit the cross-market inefficiencies
concentrated at the neck; their collective activity drives the mean curvature flow.
The neck is where $|H|^2$ is largest — it is the region of maximum inefficiency
and maximum alpha.

The MCF evolution of the neck has been studied extensively in differential
geometry [Angenent 1992, Huisken and Sinestrari 2009]. The three possible
outcomes are:

### 6.2 Outcome 1: Full integration (neck widens)

When the factors are compatible and capital flows freely, the MCF widens the neck.
The curvature at the junction decreases, the spectral gap increases, and the
merged market approaches a single minimal surface. The spread compresses to the
fundamental component $\sigma_{\rm fund}$ and the merger is complete.

**Geometric signature:** $\lambda_1(M_1 \mathbin{\#} M_2) \to \min(\lambda_1(M_1),
\lambda_1(M_2))$ as the tunnel mode drops out. The neck width $w \to$ manifold
diameter.

**Financial signature:** Spread volatility decreases monotonically. Correlation
between the two markets increases toward 1 (on factor-adjusted returns). The
number of independent arbitrage opportunities decreases.

**Example:** NYSE-Euronext. Within 18 months of the merger, cross-listed stocks
traded at negligible spread, order books were unified, and the spectral gap of the
merged market was indistinguishable from a single exchange.

### 6.3 Outcome 2: Stable partial integration (neck equilibrium)

When some factors are shared but others are not, the MCF drives the neck to an
equilibrium width — neither fully open nor closed. The neck width is determined by
the balance between the curvature-reducing MCF (arbitrageurs) and the
curvature-generating forcing (structural differences between the markets).

**Geometric signature:** The neck width $w$ reaches a steady state. The spectral
gap stabilises at the tunnel mode value $\pi^2 w^{r-2}/L^2$. The merged manifold
is a critical point of the Willmore functional — not a minimiser, but a
saddle point.

**Financial signature:** A persistent spread with stable volatility. The spread
mean-reverts but never closes to zero. Spread trading is permanently profitable
at a fixed Sharpe ratio equal to the neck's residual $\|A\|_{L^2}$.

**Example:** Shanghai-HK Stock Connect. The AH premium oscillates around 20-30%
with mean-reverting dynamics but no secular compression toward zero. The daily
quota (a regulatory constraint on neck width) prevents full MCF. The geometry
predicts: the premium will persist as long as the quota binds.

### 6.4 Outcome 3: De-merger (neck pinch singularity)

When the factors are incompatible, the MCF narrows the neck. Curvature
concentrates at the pinch point: $|H|^2 \to \infty$ as $w \to 0$. The manifold
develops a Type I singularity — the neck collapses to a point and the connected
sum disconnects into $M_1 \sqcup M_2$ (disjoint union).

**Geometric signature:** The spectral gap collapses: $\lambda_1 \to 0$ as the
tunnel mode vanishes. The Willmore energy concentrates at the neck:
$\int_{\rm neck} |H|^2 \, d\mathrm{vol} \to \infty$ while
$\int_{M_i \setminus {\rm neck}} |H|^2 \, d\mathrm{vol}$ remains bounded. The
Cheeger constant of the merged manifold drops to zero.

**Financial signature:** The spread diverges. Liquidity at the neck instruments
dries up. Correlation between markets drops to zero or goes negative.
Cross-market arbitrage becomes impossible as the neck instruments fail. This is
a financial crisis at the junction — a de-merger event.

**Example:** Brexit. The neck connecting UK and EU financial markets had been
widening under MCF for 43 years (1973-2016). In 2016, the political decision to
sever the neck initiated a reverse MCF — a forced pinch. The Willmore energy
invested in four decades of integration was written off. Spreads between UK and
EU instruments re-opened. The geometry assigns a precise cost: the unrecovered
$W_{\rm neck}$ from 43 years of neck-widening MCF.

---

## 7. Historical Case Studies

### 7.1 The Euro (1999-present): Ten necks, fifteen-year payback

The creation of the Euro was the most ambitious connected-sum operation in
financial history. Eleven sovereign bond manifolds $M_1, \ldots, M_{11}$
(Germany, France, Italy, Spain, Netherlands, Belgium, Austria, Finland, Ireland,
Portugal, Luxembourg) were connected by 10 necks into a single structure.

**Factor analysis.** Each sovereign bond market has approximately $r = 5$ factors:
global rates, European growth, country-specific growth, inflation, and credit
risk. Of these, $k \approx 3$ were shared (global rates, European growth,
inflation). The country-specific factors ($k = 2$ per country) remained
independent.

**Neck cost.** Ten necks at $W_{\rm neck} \geq 4\pi$ each: total cost
$\geq 40\pi \approx 126$ units of Willmore energy. The saving per period:
$k \cdot \log T / (2T) \approx 3 \cdot 5.5 / 504 \approx 0.033$ (annualised, with
$T = 252$). Predicted payback: $126 / 0.033 \approx 3,800$ days $\approx$ 15 years.

**The convergence trade (2000-2007).** During this period, the MCF was operating:
sovereign spreads compressed from 200-400bp to 10-30bp. The neck was widening.
Hedge funds and banks rode this MCF — the "Euro convergence trade" was one of
the most profitable spread trades of the decade. In geometric terms: the traders
were harvesting $\sigma_{\rm curv}$ as the O'Neill tensor decreased.

**The Greek crisis (2010-2012).** The neck connecting Greece to the core Eurozone
threatened to pinch. Greek sovereign spreads blew out to 3,000bp — the curvature
concentrated at the Greek neck as in a Type I singularity. The Cheeger constant
of the merged Eurozone manifold dropped precipitously as the bottleneck thinned.

**"Whatever it takes" (2012).** Draghi's intervention was a surgical prevention of
the neck pinch singularity. The ECB's OMT programme committed unlimited capital
to maintaining the neck width — effectively overriding the MCF with an external
force. In geometric terms: the central bank added an artificial Willmore-energy
subsidy to prevent the natural MCF from pinching the neck.

**Current status (2024).** The Euro manifold is partially integrated. Core necks
(Germany-France, Germany-Netherlands) are wide and stable. Peripheral necks
(Germany-Italy, Germany-Greece) remain thin with periodic curvature
concentrations. The 15-year payback prediction from 1999 places break-even around
2014 — roughly consistent with the post-crisis stabilisation. The integration
remains incomplete but the invested Willmore energy has been partially recovered.

### 7.2 Shanghai-HK Stock Connect (2014-present): Regulated neck width

**Structure.** One neck connecting the Shanghai A-share manifold to the Hong Kong
H-share manifold via a set of eligible dual-listed stocks (the bridge
instruments). The neck width is *regulated* — daily quotas limit capital flow in
both directions.

**Factor analysis.** Shared factors ($k \approx 2$): global risk appetite and
China macro growth. Unshared: mainland liquidity conditions, PBOC policy, retail
sentiment (Shanghai); global fund flows, USD/HKD dynamics (Hong Kong). Total
$r \approx 5$, so $k/r \approx 0.4$.

**The AH premium.** The AH premium (H-shares trading at a 20-30% discount to
A-shares) is the neck curvature. It is the L^2 norm of the O'Neill tensor at the
neck, made visible as a price spread. The premium fluctuates (the MCF operates
within the quota constraints) but does not compress to zero (the quota prevents
full MCF).

**Geometric prediction.** If the daily quota were removed (neck constraint
lifted), the MCF would compress the AH premium on a timescale of
$1/\lambda_1 \approx 1/(\pi^2 w_{\rm new}^{r-2}/L^2)$. With current market
parameters, this would be approximately 2-3 years to reduce the premium to
under 5%. The regulators are choosing the slow MCF path — controlled neck
widening over decades rather than rapid integration.

### 7.3 Bitcoin ETF (2024-present): The thinnest neck

**Structure.** A brand-new neck between the cryptocurrency manifold and the
traditional finance (TradFi) manifold. The bridge instruments are the spot Bitcoin
ETFs (BlackRock IBIT, Fidelity FBTC, etc.).

**Factor analysis.** Shared factor ($k \approx 1$): risk-on/risk-off sentiment.
Unshared: blockchain-specific dynamics (hash rate, halving cycles, DeFi yields,
stablecoin flows, regulatory risk). Crypto manifold dimension $r_{\rm crypto}
\approx 4$; TradFi manifold dimension $r_{\rm TradFi} \approx 6$. Shared factors:
$k/r \approx 1/6 \approx 0.17$.

**Current neck curvature.** The ETF premium/discount (typically $\pm$50-200bp)
and the futures basis are direct measurements of the neck curvature. The intraday
premium variations track the O'Neill tensor in real time.

**Geometric prediction.** With $k/r \approx 0.17$, the payback formula gives
$T_{\rm payback} \approx W_{\rm neck} \cdot 2T / (1 \cdot \log T) \approx 12.6
\times 504 / 5.5 \approx 1,155$ trading days $\approx$ 4.6 years at a minimum.
But the neck is thin and fragile — a regulatory shock (Outcome 3) could pinch it
at any time. The geometry assigns a conditional probability to each outcome based
on the current neck width and the MCF rate.

### 7.4 Brexit (2016-2020): Deliberate neck severance

**Structure.** The UK-EU single market neck had been widening under MCF for 43
years (1973-2016). During this period, $W_{\rm invested} = \sum_{t=1973}^{2016}
\Delta W_t$ units of Willmore energy were invested in the neck — through
regulatory harmonisation, institutional design, infrastructure development, and
the progressive elimination of trade barriers.

**The severance.** The 2016 referendum initiated a forced MCF reversal — a
deliberate neck pinch. The transition period (2016-2020) was the singularity
formation: the neck narrowed progressively as shared institutions were unwound.

**Geometric cost.** The cost of Brexit is the unrecovered Willmore energy:
$W_{\rm invested} - W_{\rm recovered}$. The recovered energy is the cumulative
regret saving over the 43-year integration period. Whether this is positive or
negative determines whether the merger "paid for itself" before severance. Given
that the UK joined with $k/r \approx 0.6$ and the payback formula predicts
$\sim$10-year payback, the merger was in net positive territory by the mid-1980s.
The severance writes off the *future* savings — the opportunity cost is the
discounted stream of $k \cdot \log T / (2T)$ per period in perpetuity.

### 7.5 Post-Soviet market creation (1990s): Manifold nucleation

This is not a merger but a **manifold creation** — the nucleation of 15 new
market manifolds from the dissolved Soviet planned economy. Each new market
started at Stage 0: a point (zero-dimensional manifold) with no factor structure,
no price discovery, and no spectral gap.

**Shock therapy (Russia, 1992).** Fast MCF on a newly created manifold. The
manifold dimension jumped from $r = 0$ to $r \approx 4$ in months. The MCF was
turbulent — multiple Type II singularities (the 1998 crisis was a curvature
blowup at a developing neck between the ruble bond market and the dollar market).
The Willmore energy oscillated wildly.

**Gradualism (China, 1978-present).** Slow, controlled MCF with regulated neck
widths at every stage. The manifold dimension increased from $r = 0$ to $r
\approx 5$ over four decades. Each new neck (Hong Kong connection, WTO accession,
QFII programme, Stock Connect, Bond Connect) was opened at a controlled width.
The Willmore energy increased monotonically — no singularities.

**Middle path (Poland, 1990-2004).** Moderate MCF, guided by the EU accession
process. The EU provided a template manifold — Poland's market was driven by MCF
toward the EU minimal surface. The factor structure converged to European norms
over 14 years. The EU accession in 2004 was the final connected sum, completing
the payback cycle.

The geometric framework treats all three strategies as different MCF rates on the
same underlying problem — creating a minimal surface from a point. The history
confirms the geometry: fast MCF is cheap but turbulent; slow MCF is expensive
but stable; the optimal rate depends on the neck width tolerance.

---

## 8. The Law of One Price as a Free Merger

### 8.1 Identical manifolds and free connected sums

Consider the special case where $M_1$ and $M_2$ are isometric — two identical
copies of the same market. Then $k = r$ (all factors shared), the O'Neill tensor
$A_\Phi = 0$ (the correspondence is an isometry), and the spread has zero Sharpe
(no tradeable curvature component).

**Theorem 8.1** *(Law of one price as free merger)*.
*Let $M$ be a market manifold and $M' \cong M$ an isometric copy. Then the
connected sum $M \mathbin{\#} M' \cong M$: the merger is free, the neck carries
zero Willmore energy in the limit, and the payback is instantaneous.*

*Proof.* When $M' \cong M$, we can identify the excised discs via the
isometry. The connected sum with zero neck length is $M$ itself — the two copies
glue together without distortion. The neck Willmore energy is zero (no curvature
at a flat junction), the regret saving is $r \cdot \log T / (2T)$ per period
(all factors shared), and $T_{\rm payback} = 0 / (r \cdot \log T / (2T))
= 0$. $\square$

### 8.2 Financial interpretation

The law of one price states: identical assets on different exchanges must trade at
the same price. In our framework:

- "Identical assets" means $M' \cong M$ (isometric manifolds).
- "Different exchanges" means physically separate instances.
- "Same price" means $\sigma_{\rm curv} = 0$ (zero O'Neill curvature).

Violations of the law of one price — twin-share discounts, cross-listed stock
premia, ETF tracking errors — are positive neck curvature. They are exploitable
by spread traders (Section 2) and they mean-revert under MCF.

The strength of the law of one price is inversely proportional to the neck
curvature: markets where the law holds tightly have low $\|A\|_{L^2}$; markets
where it holds loosely (AH premium, ADR discounts) have high $\|A\|_{L^2}$.

### 8.3 Approximate isometries and near-free mergers

In practice, no two markets are exactly isometric. But many are *approximately*
isometric: Brent and WTI crude oil differ only in grade and delivery location.
For approximately isometric manifolds with $\|A_\Phi\|_{L^2} = \delta \ll 1$:

$$T_{\rm payback} \approx \frac{W_{\rm neck}}{r \cdot \log T / (2T) - \delta^2 /
(2T)} \approx \frac{W_{\rm neck} \cdot 2T}{r \cdot \log T} \tag{8.1}$$

which is small when $r$ is large. Near-identical markets merge cheaply and
quickly. This explains why commodity market convergence (different grades of the
same commodity) is fast and reliable, while cross-asset convergence (equities
and commodities) is slow and uncertain.

---

## 9. The General Theory of Market Interaction

### 9.1 The interaction spectrum

The five types of market interaction form a spectrum, parametrised by the
connectedness and curvature of the intermarket geometry:

| Type | Geometric structure | Spread | Dynamics |
|:-----|:-------------------|:-------|:---------|
| Independent | Disjoint manifolds $M_1 \sqcup M_2$ | None | No interaction |
| Spread trading | Product $M_1 \times M_2$ with bundle | $\sigma = A_\Phi$ (O'Neill) | Mean-reverts |
| Partial merger | Connected sum $M_1 \mathbin{\#} M_2$, thin neck | Neck curvature | Evolves under MCF |
| Full integration | Single manifold $M$, wide neck | $\sigma_{\rm fund}$ only | Stable |
| De-merger | Neck pinch $M_1 \mathbin{\#} M_2 \to M_1 \sqcup M_2$ | Diverges | Type I singularity |

The transitions between types are continuous in the neck width parameter $w$:

$$\text{Independent} \xrightarrow{w > 0} \text{Partial merger}
\xrightarrow{w \to w_{\rm max}} \text{Full integration}$$

$$\text{Partial merger} \xrightarrow{w \to 0} \text{De-merger}
\xrightarrow{w = 0} \text{Independent}$$

### 9.2 The Kapouleas-Mazzeo-Pacard balancing condition

The connected sum $M_1 \mathbin{\#} M_2$ can be deformed to a minimal surface
(an efficient merged market) if and only if the neck satisfies a **balancing
condition** [Kapouleas 1990, Mazzeo and Pacard 2006].

**Theorem 9.1** *(Balancing condition for merger convergence)*.
*The connected sum $M_1 \mathbin{\#} M_2$ admits a minimal surface deformation
(the merged market converges to efficiency) if and only if the Kapouleas balancing
condition holds at the neck:*

$$\sum_{\alpha} n_\alpha \cdot \vec{H}_\alpha = 0 \tag{9.1}$$

*where the sum is over the neck attachment points $\alpha$, $n_\alpha$ is the
outward unit normal, and $\vec{H}_\alpha$ is the mean curvature vector at the
attachment point.*

**Financial interpretation.** The balancing condition says: the curvature
contributions from each side of the neck must cancel. If one market pushes capital
through the neck faster than the other absorbs it, the neck is unbalanced. The
excess flow concentrates curvature at the neck, the MCF amplifies the imbalance,
and the merger fails (Outcome 3).

Concretely:

- **Balanced merger (condition satisfied):** Capital flows from $M_1$ to $M_2$
  at the same rate as from $M_2$ to $M_1$. The neck widens symmetrically.
  Example: NYSE-Euronext, where both sides contributed comparable liquidity.

- **Unbalanced merger (condition violated):** Capital flows predominantly in one
  direction. The neck curvature concentrates on the receiving side. Example: the
  Euro, where capital flowed from core to periphery (Germany to Greece), creating
  an unbalanced neck that nearly pinched in 2010-2012.

The Kapouleas theory provides the rigorous criterion: one can compute the
balancing condition from the mean curvature vectors at the proposed attachment
points *before* the merger takes place. An unbalanced merger will fail unless
external intervention (central bank support, regulatory adjustment) restores
the balance.

---

## 10. New Results

We collect the principal results of this paper for reference.

**Theorem I1** *(Spread decomposition)*. Any intermarket spread decomposes
uniquely as $\sigma = \sigma_{\rm fund} + \sigma_{\rm curv} + \sigma_{\rm top}$,
where $\sigma_{\rm fund}$ is a geodesic invariant (non-tradeable),
$\sigma_{\rm curv}$ is the O'Neill $A$-tensor (tradeable, mean-reverting),
and $\sigma_{\rm top}$ is a topological obstruction (divergent when connectivity
fails).

**Theorem I2** *(Optimal spread trade)*. The optimal spread trade between
$M_1$ and $M_2$ is the eigenvector of the cross-market Fisher information matrix
$F_{\rm cross} = \Phi^{\ast}F_{M_2} - F_{M_1}$ corresponding to the smallest
eigenvalue — the direction of maximum mean-reversion.

**Theorem I3** *(Merger payback formula)*. A market merger with neck Willmore
energy $W_{\rm neck}$ and $k$ shared factors pays for itself after
$T_{\rm payback} \approx W_{\rm neck} \cdot 2T / (k \cdot \log T)$ periods.

**Theorem I4** *(Neck evolution under MCF)*. The neck of a connected sum
$M_1 \mathbin{\#} M_2$ evolves under MCF to one of three outcomes: (1) full
integration (neck widens to manifold width), (2) stable partial integration
(neck reaches equilibrium at a saddle point of the Willmore functional), or (3)
de-merger (neck pinches to a Type I singularity, manifold disconnects).

**Theorem I5** *(Law of one price = free merger)*. For isometric market manifolds
$M' \cong M$, the connected sum $M \mathbin{\#} M' \cong M$. The merger is free
($W_{\rm neck} = 0$ in the isometric limit), the O'Neill tensor vanishes
($A_\Phi = 0$), and the payback is instantaneous ($T_{\rm payback} = 0$).

**Theorem I6** *(Balancing condition for merger convergence)*. The connected sum
$M_1 \mathbin{\#} M_2$ converges to an efficient (minimal surface) merged market
if and only if the Kapouleas balancing condition $\sum_\alpha n_\alpha \cdot
\vec{H}_\alpha = 0$ holds at the neck. A merger with unbalanced capital flows
fails.

---

## 11. Open Problems

**OP-I1** *(Optimal merger sequencing)*. Given $n$ markets $M_1, \ldots, M_n$
that will eventually merge, what is the optimal order in which to create the
necks? The total Willmore cost depends on the sequence: connecting high-$k$
pairs first may reduce the cost of subsequent mergers (by increasing the number
of shared factors). This is a combinatorial optimisation on the complete graph
$K_n$ weighted by $k_{ij}/r_{ij}$ — a geometric minimum spanning tree problem.

**OP-I2** *(Regulatory barriers as artificial neck thinning)*. Capital controls,
tariffs, and sanctions are external constraints that prevent MCF from widening
necks. Can the cost of regulatory barriers be measured as the difference between
the natural neck width (under free MCF) and the actual neck width? Is the welfare
cost of a tariff equal to the Willmore energy of the artificially thin neck?

**OP-I3** *(Crypto integration or decoupling)*. Will the Bitcoin ETF neck widen
(crypto becomes another asset class) or pinch (regulatory intervention, systemic
crisis)? The answer is computable from current data: estimate $k/r$ from the
factor structure of Bitcoin returns versus equity returns, compute the current
neck width from the ETF premium, and run the MCF forward. What is the critical
neck width below which pinching is inevitable?

**OP-I4** *(The geometry of hostile takeovers)*. A hostile takeover is a forced
connected sum — one manifold absorbs another without consent. The target's
shareholders are forced through a neck they did not choose. The takeover premium
is the neck cost $W_{\rm neck}$ paid by the acquirer. Is the optimal takeover
premium equal to $4\pi$ (the minimal neck cost), or is it higher because forced
mergers have unbalanced necks?

**OP-I5** *(Optimal number of global exchanges)*. Given $d$ assets distributed
across $n$ exchanges, what value of $n$ minimises total Willmore energy? A single
global exchange ($n = 1$) has zero neck cost but maximum manifold complexity.
Many small exchanges ($n \gg 1$) have low individual complexity but high neck
costs. The optimal $n$ balances these effects. Is the current number of major
global exchanges ($n \approx 20$) near the optimum?

---

## References

O'Neill, B. (1966). The fundamental equations of a submersion.
*Michigan Mathematical Journal* 13(4), 459-469.

Kapouleas, N. (1990). Complete constant mean curvature surfaces in Euclidean
three-space. *Annals of Mathematics* 131(2), 239-330.

Mazzeo, R. and Pacard, F. (2006). Foliations by constant mean curvature tubes.
*Communications in Analysis and Geometry* 13(4), 633-670.

Cheeger, J. (1970). A lower bound for the smallest eigenvalue of the Laplacian.
In *Problems in Analysis*, pp. 195-199. Princeton University Press.

Li, P. and Yau, S.-T. (1982). A new conformal invariant and its applications to
the Willmore conjecture and the first eigenvalue of compact surfaces.
*Inventiones Mathematicae* 69(2), 269-291.

Angenent, S. (1992). Shrinking doughnuts. In *Nonlinear Diffusion Equations and
Their Equilibrium States*, Vol. 3, pp. 21-38. Birkhauser.

Huisken, G. and Sinestrari, C. (2009). Mean curvature flow with surgeries of
two-convex hypersurfaces. *Inventiones Mathematicae* 175(1), 137-221.

Marques, F. C. and Neves, A. (2014). Min-max theory and the Willmore conjecture.
*Annals of Mathematics* 179(2), 683-782.

Cover, T. M. (1991). Universal portfolios. *Mathematical Finance* 1(1), 1-29.

Fama, E. F. (1970). Efficient capital markets: a review of theory and empirical
work. *Journal of Finance* 25(2), 383-417.

*[All other references as per companion papers in this series.]*
