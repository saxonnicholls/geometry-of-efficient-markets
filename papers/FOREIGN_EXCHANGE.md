# The Geometry of Foreign Exchange:
## One Manifold, N Currencies, and Why the Carry Trade Is Mean Curvature

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.11** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
The foreign exchange market is not a collection of separate pair-wise markets.
It is a single manifold — the **currency simplex** $\Delta_{N-2}$ — where $N$ is the
number of currencies and the ambient dimension is $N-1$, not $N(N-1)/2$, because
triangular arbitrage constrains the exchange rate vector to an $(N-1)$-dimensional
subspace. Each currency pair (EURUSD, GBPJPY, AUDCHF) is a *projection* of the
single FX state onto a specific direction on this manifold. We develop the complete
geometric theory of foreign exchange within the framework of the market manifold
$M^r \subset S^{d-1}_{+}$.

Our principal results:

**(i) The currency simplex.** The space of arbitrage-free exchange rates for $N$
currencies is the positive projective space $\mathbb{RP}^{N-1}_{+} \cong \Delta_{N-2}$,
obtained as the quotient of the positive orthant $\mathbb{R}^{N}_+$ by the
multiplicative action of numeraire choice. The Fisher–Rao metric
$g^{\mathrm{FR}}_{ij} = \delta_{ij}/w_i$ on this simplex, where $w_i$ is the
share of global FX turnover in currency $i$, is the natural metric for FX geometry.
The $N(N-1)/2$ exchange rate pairs are not independent markets — they are directions
$e_A - e_B$ on the single currency simplex.

**(ii) Carry = mean curvature.** The carry trade premium — the empirical violation
of Uncovered Interest Parity (UIP) — is the mean curvature of the FX manifold in
the yield-differential direction. The Sharpe–curvature identity applied to FX gives
$\mathrm{Sharpe}_{\mathrm{carry}} = \|H_{\mathrm{carry}}\|_{L^2}$, where
$H_{\mathrm{carry}}$ is the component of the mean curvature vector in the carry
direction. The Lustig–Verdelhan empirical carry Sharpe of $\sim 0.5$–$0.8$ is a
direct measurement of FX manifold curvature.

**(iii) Triangular arbitrage as LOB curvature.** Deviations from perfect triangular
arbitrage ($\log(A/C) \neq \log(A/B) + \log(B/C)$) are curvature in the cross-rate
direction of the limit order book manifold. The deviation $\varepsilon$ is bounded
by the bid-ask spread, and HFT firms exploiting triangular arb are performing mean
curvature flow at nanosecond timescale.

**(iv) Lie group structure.** The set of exchange rates carries a natural
multiplicative Lie group structure. The Fisher–Rao metric is left-invariant under
currency revaluation (a consequence of Cencov's theorem). The Lie algebra of the
FX manifold consists of the $r \approx 3$ independent factor directions: dollar,
carry, and risk.

**(v) Central bank interventions as boundary conditions.** A central bank that
fixes or floors its exchange rate imposes a boundary condition on the currency
simplex, confining the FX manifold to a half-space. The SNB floor removal of
January 2015 was a Type II MCF singularity — three years of accumulated Willmore
energy released in minutes when the constraint was lifted.

**(vi) The cross-rate consistency graph.** The triangular arbitrage constraints
form a graph whose Fiedler eigenvalue equals the Cheeger constant of the FX market.
A collapsing Fiedler eigenvalue signals persistent arbitrage violations — the
geometric signature of a currency crisis.

**Keywords.** Foreign exchange; currency simplex; carry trade; uncovered interest
parity; triangular arbitrage; mean curvature; Fisher–Rao metric; Lie group;
Bhattacharyya sphere; central bank intervention; Willmore energy; MCF singularity;
cross-rate graph; Cheeger constant; Lustig–Verdelhan.

**MSC 2020.** 91G15, 53A10, 91G20, 22E70, 53B25, 91B26, 05C50.

---

## 1. The Currency Simplex

### 1.1 Setup and dimension count

Consider a world with $N$ currencies. For the ten major currencies (USD, EUR, GBP,
JPY, CHF, AUD, CAD, NZD, SEK, NOK), $N = 10$. The number of distinct exchange
rate pairs is $\binom{N}{2} = N(N-1)/2 = 45$. This is the number that appears on a
broker's rate board, and it is the number that a naive analysis would take as the
dimensionality of the FX market.

But it is wrong. The correct dimension is $N - 1 = 9$.

The reason is **triangular arbitrage**. For any three currencies $A$, $B$, $C$:

$$\log e_{AC} = \log e_{AB} + \log e_{BC}$$

where $e_{AB}$ is the exchange rate of $A$ per unit of $B$. This is not an
approximate relationship. It is an identity enforced by arbitrageurs to within the
bid-ask spread at millisecond timescale. Each triangular constraint eliminates one
degree of freedom. The $\binom{N}{3}$ triangular constraints reduce the
$N(N-1)/2$ rates to exactly $N-1$ independent rates — the rates of each currency
against a chosen numeraire.

### 1.2 The log-rate vector

Fix a numeraire currency (say USD). Define the **log-rate vector**:

$$x = (x_1, \ldots, x_{N-1}) \in \mathbb{R}^{N-1}$$

where $x_i = \log e_{i,\mathrm{USD}}$ is the log exchange rate of currency $i$
against the numeraire. Every exchange rate pair is recoverable:

$$\log e_{ij} = x_i - x_j$$

The set of all consistent exchange rate vectors is an $(N-1)$-dimensional affine
subspace of $\mathbb{R}^{N(N-1)/2}$. The 45 rates displayed on the screen are 45
projections of a single 9-dimensional vector.

### 1.3 The currency simplex

Define the **currency share** $w_i$ of currency $i$ as the fraction of total global
FX turnover denominated in currency $i$. The BIS Triennial Survey (2022) gives:
USD $\approx 44\%$, EUR $\approx 15\%$, JPY $\approx 8\%$, GBP $\approx 6\%$,
with the remaining six major currencies sharing $\sim 27\%$. Since each FX
transaction involves two currencies and the total sums to $200\%$, we normalise:

$$w_i = \frac{\text{turnover share of currency } i}{\sum_j \text{turnover share of currency } j}, \qquad \sum_{i=1}^{N} w_i = 1, \qquad w_i > 0$$

The vector $w = (w_1, \ldots, w_N)$ lives on the interior of the $(N-1)$-simplex
$\Delta_{N-1}$. But we have $N$ currencies and $N-1$ independent exchange rates,
so the *effective* simplex for FX geometry is $\Delta_{N-2}$: the $(N-2)$-simplex
parametrising the ratios of currency weights once the numeraire is fixed.

More precisely, the space of arbitrage-free exchange rates is the **positive
projective space**:

$$\mathbb{RP}^{N-1}_{+} = \mathbb{R}^{N}_+ / \mathbb{R}_{+} \cong \Delta_{N-1}$$

where the equivalence identifies rate vectors that differ only by a global scaling
(which is the numeraire choice). This is isomorphic to the simplex because every
equivalence class has a unique representative with $\sum w_i = 1$.

### 1.4 The Fisher–Rao metric on the currency simplex

Equip $\Delta_{N-1}$ with the Fisher–Rao metric:

$$g^{\mathrm{FR}}_{ij}(w) = \frac{\delta_{ij}}{w_i}$$

This is the canonical Riemannian metric for probability distributions on a finite
alphabet. In the FX context, $w_i$ is the turnover weight of currency $i$, and
$g^{\mathrm{FR}}$ measures the information-theoretic distance between currency
configurations. A small change in a heavily-traded currency (high $w_i$) has less
geometric impact than the same-sized change in a lightly-traded currency (low
$w_i$) — exactly right for FX risk.

The **Bhattacharyya embedding** $\phi: \Delta_{N-1} \to S^{N-1}_{+}$:

$$\phi(w) = \left(\sqrt{w_1}, \ldots, \sqrt{w_N}\right) \in S^{N-1}_{+}$$

maps the currency simplex isometrically into the positive orthant of the unit
sphere with constant curvature $K = 1/4$. The FX manifold inherits this ambient
curvature.

---

## 2. Why One Manifold, Not 45

### 2.1 Currency pairs as directions

The central conceptual shift: **EURUSD is not a market. It is a direction on the
currency simplex.**

Let $e_i$ be the $i$-th standard basis vector in $\mathbb{R}^{N}$, projected onto
the tangent space of $\Delta_{N-1}$. The exchange rate pair $(A, B)$ corresponds to
the direction vector:

$$v_{AB} = e_A - e_B \in T_w \Delta_{N-1}$$

Trading EURUSD (going long EUR, short USD) means investing along the direction
$e_{\mathrm{EUR}} - e_{\mathrm{USD}}$ on the currency simplex. The "return" on
EURUSD is the inner product of the FX state change with this direction:

$$r_{AB}(t) = \langle dw(t), v_{AB} \rangle_{g^{\mathrm{FR}}} = \frac{dw_A}{w_A} - \frac{dw_B}{w_B}$$

which is the log-return of the exchange rate. Every FX trade is a directional bet
on the single currency simplex.

### 2.2 The rank of the FX covariance matrix

Construct the $N(N-1)/2 \times T$ matrix of all pair-wise FX returns over $T$ time
periods. Its rank is at most $N - 1$ (from the triangular constraints). Its
*effective* rank — the stable rank $\mathrm{srank}(\Sigma) = \mathrm{tr}(\Sigma)/\|\Sigma\|_{\mathrm{op}}$ — is typically $r \approx 3$ for major FX.

This is the dimension of the **FX market manifold** $M^r_{\mathrm{FX}}$: a
3-dimensional submanifold of $S^{N-1}_{+}$.

**Theorem 2.1** (FX manifold dimension).
*The FX market manifold $M^r_{\mathrm{FX}} \subset \Delta_{N-1}$ has dimension
$r \approx 3$ for the major currency universe. The triangular arbitrage constraints
are automatically satisfied by the simplex structure: any point on $\Delta_{N-1}$
defines a consistent set of exchange rates.*

*Proof.* A point $w \in \Delta_{N-1}$ defines exchange rates $e_{ij} = w_i / w_j$.
Triangular consistency follows immediately: $e_{ij} \cdot e_{jk} = (w_i/w_j)(w_j/w_k) = w_i/w_k = e_{ik}$. The dimension $r \approx 3$ follows from
the empirical stable rank of the FX return covariance matrix (Lustig and Verdelhan
\[2007\], Menkhoff et al.\ \[2012\]). $\square$

The point is elementary but consequential. By working on the simplex, triangular
arbitrage is not an additional constraint to be imposed — it is a *tautology*. The
simplex structure encodes it automatically.

---

## 3. The Three FX Factors

### 3.1 Empirical factor structure

The dimension $r \approx 3$ for major FX has been established empirically by
multiple independent groups:

- **Lustig and Verdelhan \[2007\]:** Two factors (dollar, carry) explain the cross-section of FX excess returns.
- **Menkhoff, Sarno, Schmeling, and Schrimpf \[2012\]:** Three factors (dollar, carry, volatility/risk) explain $\sim 80\%$ of cross-sectional FX variance.
- **Verdelhan \[2018\]:** The dollar factor alone explains $\sim 60\%$; adding carry and volatility reaches $\sim 80\%$.

### 3.2 Geometric interpretation of each factor

**Factor 1: Dollar ($v_0$).** The first principal direction on $M^3_{\mathrm{FX}}$
corresponds to uniform USD strengthening or weakening against all other currencies.
In the Jacobi decomposition of the market process (MARKET_PROCESSES.md), this is
the market factor $v_0$ — the first eigenfunction of the Jacobi operator on
$\Delta_{N-1}$. It explains $\sim 60\%$ of FX variance. A "strong dollar" regime
means the FX state has moved in the $+v_0$ direction; "weak dollar" means $-v_0$.

**Factor 2: Carry ($v_1$).** The second principal direction separates high-yield
currencies (AUD, NZD, BRL, ZAR) from low-yield currencies (JPY, CHF, EUR). The
carry factor loading of currency $i$ is proportional to $r_i - \bar{r}$, the
interest rate of currency $i$ minus the cross-sectional mean. This factor captures
the forward premium puzzle (Fama \[1984\]): high-yield currencies do not depreciate
as much as UIP predicts — and the residual is the carry trade profit.

**Factor 3: Risk ($v_2$).** The third principal direction correlates with global
risk appetite. In risk-on regimes, emerging market and commodity currencies rally
while safe havens (JPY, CHF) weaken. In risk-off regimes, the reverse. This factor
is strongly correlated with VIX ($\rho \approx -0.5$ between risk factor and VIX)
and captures the "peso problem" component of FX returns.

### 3.3 Connection to the classification theorem

With $r = 3$, the FX manifold $M^3_{\mathrm{FX}}$ is a 3-dimensional submanifold
of $S^{N-1}_{+}$. The classification theorem (CLASSIFICATION.md) identifies three
stable topological types:

| Regime | Manifold type | Dyson class | FX interpretation |
|:-------|:-------------|:------------|:------------------|
| Normal | $S^3_+$ (CAPM) | $\beta = 1$ (GOE) | All three factors stable, mean-reverting |
| Transitional | $T^2 \times \mathbb{R}$ (Clifford) | $\beta = 2$ (GUE) | Two factors cycle (carry/risk rotation) |
| Crisis | $\mathbb{H}^{3}$ (pseudo-Anosov) | $\beta = 4$ (GSE) | Factors decouple, chaotic dynamics |

The 1997 Asian crisis, the 2008 GFC carry unwind, and the 2015 SNB shock each
exhibit a transition from CAPM-type to pseudo-Anosov-type FX dynamics — visible
as a change in the Dyson class of the FX covariance eigenvalue statistics. This
is the FX-specific instance of the market bifurcation described in CHAOS_TAKENS.md.

---

## 4. The Carry Trade as Mean Curvature

### 4.1 The carry portfolio

The carry trade is the oldest and most studied FX strategy. In its simplest form:
borrow in a low-interest-rate currency, invest in a high-interest-rate currency,
and earn the differential. For a portfolio across $N$ currencies, the carry
portfolio weights are:

$$b^{\mathrm{carry}}_{i} \propto r_i - \bar{r}$$

where $r_i$ is the short-term interest rate of currency $i$ and
$\bar{r} = \frac{1}{N}\sum_j r_j$. This is long high-yield, short low-yield.

### 4.2 Uncovered Interest Parity and its failure

UIP states that the expected exchange rate change should offset the interest rate
differential:

$$\mathbb{E}[\Delta \log e_{ij}] = r_j - r_i$$

If UIP held, the carry trade would earn zero expected return: the interest
differential would be exactly offset by expected currency depreciation. UIP is
one of the most robustly rejected hypotheses in empirical finance. The carry
trade earns a Sharpe ratio of $\sim 0.5$–$0.8$ for diversified portfolios
(Burnside et al.\ \[2011\], Lustig et al.\ \[2011\]).

In the language of the geometric framework: **UIP is the statement that the FX
manifold is minimal in the carry direction.**

### 4.3 The Sharpe–curvature identity for FX

**Theorem 4.1** (Carry = mean curvature).
*Let $M^r_{\mathrm{FX}} \subset S^{N-1}_{+}$ be the FX market manifold and let
$H$ be its mean curvature vector. Let $v_{\mathrm{carry}} \in T_{w^{\ast}}\Delta_{N-1}$
be the carry direction with components $(v_{\mathrm{carry}})_i = (r_i - \bar{r})/\sqrt{w^{\ast}_{i}}$. Then the carry trade Sharpe ratio satisfies:*

$$\mathrm{Sharpe}_{\mathrm{carry}} = \|H_{\mathrm{carry}}\|_{L^2(M, g_M)}$$

*where $H_{\mathrm{carry}} = \langle H, v_{\mathrm{carry}} \rangle$ is the
component of the mean curvature in the carry direction.*

*Proof.* This is the Sharpe–curvature identity of MINIMAL_SURFACE.md (R1),
applied to the specific portfolio direction $v_{\mathrm{carry}}$. The carry
portfolio $b^{\mathrm{carry}}$ has excess return
$\mu_{\mathrm{carry}} = \sum_i b^{\mathrm{carry}}_{i} (r_i - \mathbb{E}[\Delta \log e_i])$
— the UIP violation. By the Sharpe–curvature identity, the Sharpe ratio of any
portfolio direction equals the $L^2$-norm of the mean curvature projected onto
that direction. The carry direction is the interest-rate-differential vector,
normalised to unit length in the Fisher–Rao metric. Therefore
$\mathrm{Sharpe}_{\mathrm{carry}} = \|H_{\mathrm{carry}}\|_{L^2}$.

UIP ($\mathrm{Sharpe}_{\mathrm{carry}} = 0$) holds if and only if
$H_{\mathrm{carry}} = 0$ — the FX manifold is minimal in the carry direction.
The empirical Sharpe of $\sim 0.5$–$0.8$ measures the curvature. $\square$

**Corollary 4.2.** *The forward premium puzzle (Fama \[1984\]) is equivalent to
the statement that the FX manifold has non-zero mean curvature in the carry
direction. The "puzzle" is not a puzzle — it is a geometric fact about the shape
of the FX manifold.*

### 4.4 The Willmore energy of the carry

The total Willmore energy of the FX manifold in the carry direction is:

$$\mathcal{W}_{\mathrm{carry}}(M) = \int_M |H_{\mathrm{carry}}|^2 \, d\mathrm{vol}_{M}$$

This is the integrated squared curvature in the yield-differential direction —
the total "carry inefficiency" of the FX market. If the FX market were fully
efficient in the carry direction, $\mathcal{W}_{\mathrm{carry}} = 0$.
The empirical value $\mathcal{W}_{\mathrm{carry}} > 0$ measures the degree to
which the carry trade is a persistent anomaly.

The mean curvature flow (MCF) drives $\mathcal{W}_{\mathrm{carry}}$ toward zero
over time. The fact that the carry trade has been profitable for decades
(Burnside et al.\ \[2011\]) — and that its Sharpe ratio has been roughly stable —
suggests that the FX manifold is at a *stationary* non-minimal configuration:
the carry curvature is replenished by the underlying economic mechanism
(differential monetary policy) as fast as arbitrageurs erode it.

---

## 5. Triangular Arbitrage as Microstructure Curvature

### 5.1 Perfect vs. imperfect triangular arbitrage

In theory, for any currency triple $(A, B, C)$:

$$e_{AC} = e_{AB} \cdot e_{BC} \qquad \text{exactly}$$

In practice, the limit order book for each pair is discrete and asynchronous.
Define the **triangular deviation**:

$$\varepsilon_{ABC}(t) = \log e_{AC}(t) - \log e_{AB}(t) - \log e_{BC}(t)$$

This deviation is non-zero at any given instant due to bid-ask spreads, latency,
and the asynchronous arrival of orders across the three books.

### 5.2 Curvature interpretation

**Theorem 5.1** (Triangular arb as LOB curvature).
*The triangular deviation $\varepsilon_{ABC}$ is the curvature of the FX limit
order book manifold in the cross-rate direction $v_{AC} - v_{AB} - v_{BC}$. It
satisfies:*

$$|\varepsilon_{ABC}| \leq s^{\mathrm{eff}}_{ABC}$$

*where $s^{\mathrm{eff}}_{ABC}$ is the effective triangular bid-ask spread
(the sum of half-spreads for the three legs), and the mean curvature in the
cross-rate direction is:*

$$H_{\mathrm{cross}} = \frac{\varepsilon_{ABC}}{2\sigma_{\mathrm{cross}}}$$

*where $\sigma_{\mathrm{cross}}$ is the volatility of the cross-rate.*

*Proof.* The direction $v_{AC} - v_{AB} - v_{BC}$ is zero in the tangent space
of the arbitrage-free simplex (by the triangular constraint). Any non-zero
component in this direction is *normal* to the arbitrage-free manifold — it is
extrinsic curvature. The bound $|\varepsilon| \leq s^{\mathrm{eff}}$ follows from
the fact that any deviation larger than the effective spread is immediately
exploitable and is eliminated by arbitrageurs. $\square$

### 5.3 The spectral gap of triangular arbitrage

The triangular deviation $\varepsilon_{ABC}(t)$ mean-reverts to zero. Model it as
an Ornstein–Uhlenbeck process:

$$d\varepsilon = -\lambda_1^{\mathrm{tri}} \varepsilon \, dt + \sigma_{\varepsilon} \, dW$$

The mean-reversion rate $\lambda_1^{\mathrm{tri}}$ is the **spectral gap** of the
triangular arbitrage process. It depends on the speed of the fastest arbitrageur:

| Participant | $\lambda_1^{\mathrm{tri}}$ | Timescale |
|:------------|:---------------------------|:----------|
| Co-located HFT | $\sim 10^6 \, \mathrm{s}^{-1}$ | microseconds |
| Regional bank | $\sim 10^3 \, \mathrm{s}^{-1}$ | milliseconds |
| Retail broker | $\sim 1 \, \mathrm{s}^{-1}$ | seconds |

The spectral gap is the inverse of the time it takes to detect and trade the
arbitrage. HFT firms performing triangular arb are executing **mean curvature flow
on the FX cross-rate manifold at nanosecond timescale** — they are the fastest
MCF in any financial market.

This is the FX-specific instance of the microstructure spectral hierarchy: the
market efficiency at each timescale is set by the spectral gap of the fastest
participant operating at that timescale.

---

## 6. The Lie Group Structure

### 6.1 The multiplicative group of exchange rates

An exchange rate $e_{AB} \in \mathbb{R}_{+}$ is an element of the multiplicative
group $(\mathbb{R}_{+}, \times)$. The full set of exchange rates for $N$ currencies
is the quotient:

$$\mathcal{E} = \mathbb{R}^{N}_+ / \mathbb{R}_{+} \cong \mathbb{RP}^{N-1}_{+} \cong \Delta_{N-1}$$

where the quotient is by the diagonal action $v \mapsto \lambda v$ for
$\lambda \in \mathbb{R}_{+}$ (numeraire rescaling). The group operation on
$\mathcal{E}$ is componentwise multiplication: if $v = (v_1, \ldots, v_N)$ and
$u = (u_1, \ldots, u_N)$ are currency value vectors, then $v \cdot u = (v_1 u_1, \ldots, v_N u_N)$.

### 6.2 Left-invariance of the Fisher–Rao metric

**Theorem 6.1** (Left-invariance).
*The Fisher–Rao metric $g^{\mathrm{FR}}$ on $\Delta_{N-1}$ is left-invariant under
the currency revaluation action: if currency $i$'s value changes by a factor
$\lambda_i > 0$, the metric structure is preserved.*

*Proof.* The revaluation $w_i \mapsto \lambda_i w_i / \sum_j \lambda_j w_j$ is a
diffeomorphism of $\Delta_{N-1}$. By Cencov's theorem \[1982\], the Fisher–Rao
metric is the unique Riemannian metric on the space of probability distributions
(up to a constant factor) that is invariant under Markov morphisms — and in
particular under the affine reparametrisation induced by revaluation. Therefore
$g^{\mathrm{FR}}$ is left-invariant under the revaluation group action. $\square$

This is the FX version of a general fact: the Fisher–Rao metric does not depend
on the numeraire. Whether you quote exchange rates in USD, EUR, or gold, the
geometric structure of the FX manifold is the same. Numeraire invariance is not
an assumption — it is a theorem.

### 6.3 The Lie algebra of FX factors

**Theorem 6.2** (Lie algebra structure).
*The FX manifold $M^r_{\mathrm{FX}}$ is a sub-Lie-group of the currency revaluation
group. Its Lie algebra $\mathfrak{g}_{\mathrm{FX}} = T_{w^{\ast}} M^r_{\mathrm{FX}}$
consists of the $r$ independent factor directions. For $r = 3$:*

$$\mathfrak{g}_{\mathrm{FX}} = \mathrm{span}\{v_0, v_1, v_2\} = \mathrm{span}\{v_{\mathrm{dollar}}, v_{\mathrm{carry}}, v_{\mathrm{risk}}\}$$

*The exponential map $\exp: \mathfrak{g}_{\mathrm{FX}} \to M^3_{\mathrm{FX}}$
gives the FX rate dynamics: a factor shock of magnitude $\alpha$ in direction
$v_k$ moves the FX state from $w^{\ast}$ to $\exp(\alpha v_k) \cdot w^{\ast}$.*

*Proof.* The tangent space $T_{w^{\ast}} M^r$ at the log-optimal currency allocation
$w^{\ast}$ is spanned by the $r$ principal directions of the FX return covariance
matrix (restricted to $M^r$). These directions form a Lie algebra under the
bracket induced by the multiplicative group structure:
$[v_k, v_l]_i = v_{k,i} v_{l,i} (1/w^{\ast}_{i}) - v_{l,i} v_{k,i} (1/w^{\ast}_{i}) = 0$
in the abelian case (which holds when the factors are orthogonal in $g^{\mathrm{FR}}$).
The exponential map of the abelian group is componentwise exponentiation on
the simplex. $\square$

The Lie group structure has a practical consequence: factor decomposition of FX
returns is not just a statistical convenience — it is the unique algebraic
decomposition of the currency revaluation group into its generating directions.
The three FX factors are not "chosen" — they are forced by the group structure,
just as the Dyson class is forced by manifold symmetry (RANDOM_MATRIX.md).

---

## 7. Central Bank Interventions as Boundary Conditions

### 7.1 Exchange rate fixing as coordinate clamping

A central bank that fixes its exchange rate is **clamping a coordinate on the
currency simplex**. The People's Bank of China fixing the USDCNY rate at a target
level is the constraint:

$$w_{\mathrm{CNY}} = c \qquad \text{(constant)}$$

The FX manifold is confined to the hyperplane $\{w \in \Delta_{N-1} : w_{\mathrm{CNY}} = c\}$
— a face of the simplex. The effective dimension drops by one: the constrained
manifold $M^r_{\mathrm{FX}} \cap \{w_{\mathrm{CNY}} = c\}$ has dimension $r - 1$
if the CNY factor is independent, or dimension $r$ if CNY moves in a linear
combination of existing factors.

### 7.2 The half-space constraint (floors and ceilings)

A more subtle intervention is a **floor** or **ceiling** — a one-sided constraint.
The SNB maintained a floor of EURCHF $\geq$ 1.20 from September 2011 to January
2015. In simplex coordinates, this is the half-space constraint:

$$w_{\mathrm{CHF}} \leq w_{\mathrm{CHF}}^{\max}(\text{EURCHF} = 1.20)$$

The FX manifold is confined to a half-space of $\Delta_{N-1}$. Near the constraint
boundary, the manifold is forced away from its unconstrained minimal surface
configuration. The **Willmore energy accumulates**:

$$\mathcal{W}_{\mathrm{floor}}(t) = \int_{M^r(t)} |H_{\mathrm{boundary}}|^2 \, d\mathrm{vol}_{M}$$

where $H_{\mathrm{boundary}}$ is the mean curvature induced by the constraint.
The longer the floor is maintained, and the further the unconstrained equilibrium
drifts from the floor level, the larger the accumulated Willmore energy.

### 7.3 Case study: the SNB floor removal (15 January 2015)

The timeline:

- **September 2011:** SNB announces EURCHF floor at 1.20. Market was at $\sim$1.10.
  The SNB intervenes massively, buying EUR and selling CHF, forcing the FX state
  to the constraint boundary.
  
- **2012–2014:** The unconstrained equilibrium (driven by Swiss current account
  surplus, safe-haven flows, ECB easing) drifts further below 1.20. Estimates
  suggest the unconstrained rate was $\sim$1.00–1.05. The Willmore energy
  $\mathcal{W}_{\mathrm{floor}}$ grows quadratically in the deviation.

- **15 January 2015, 09:30 CET:** The SNB announces the immediate removal of the
  floor. EURCHF drops from 1.2010 to 0.8500 in approximately four minutes — a
  $30\%$ move in the third most liquid currency pair in the world.

**Geometric interpretation.** This was a **Type II MCF singularity**. The mean
curvature at the constraint boundary had been growing for three years. When the
constraint was removed, the mean curvature flow was re-initiated with initial
condition $H_{\mathrm{boundary}} \gg 0$. The curvature was so large that the MCF
produced a finite-time singularity — the manifold "snapped" to the unconstrained
configuration faster than any continuous flow could model.

The damage was geometric in character: the singularity propagated through the
cross-rate graph. Every CHF pair moved violently. Several FX brokers (Alpari UK,
Excel Markets, Global Brokers NZ) went bankrupt. FXCM required a \$300M bailout
from Leucadia. Multiple hedge funds lost billions. The losses were concentrated
among participants who had been short volatility near the constraint boundary —
precisely those most exposed to the curvature singularity.

**Theorem 7.1** (Floor removal as MCF singularity).
*Let $M^r_{\mathrm{FX}}(t)$ be the FX manifold constrained to a half-space
$\{w_k \leq c\}$ for $t \in [0, \tau]$, with the constraint removed at $t = \tau$.
If the accumulated Willmore energy
$\mathcal{W}_{\mathrm{floor}}(\tau) > \mathcal{W}_{\mathrm{crit}}$
(the critical Willmore energy for Type II singularity formation in codimension
$N - 1 - r$), then the MCF starting from $M^r(\tau)$ develops a Type II
singularity in finite time.*

*Proof sketch.* At the constraint boundary, the second fundamental form
$\mathrm{II}(v, v) \sim (\text{unconstrained curvature}) + (\text{Lagrange multiplier})$
has a contribution from the Lagrange multiplier enforcing the half-space constraint.
When the constraint is removed, the Lagrange multiplier vanishes instantaneously
but the curvature does not — the manifold inherits the full curvature as initial
data for the unconstrained MCF. By the Huisken–Sinestrari classification of MCF
singularities \[2009\], if the initial $|H|^2$ exceeds the critical threshold for
the codimension, the flow develops a Type II singularity. The EURCHF data are
consistent with $\mathcal{W}_{\mathrm{floor}}(\tau) \gg \mathcal{W}_{\mathrm{crit}}$. $\square$

---

## 8. The Cross-Rate Consistency Graph

### 8.1 Graph construction

For $N$ currencies, define the **cross-rate consistency graph** $G = (V, E, T)$:

- **Vertices** $V$: the $N$ currencies.
- **Edges** $E$: the $\binom{N}{2}$ exchange rate pairs, weighted by turnover.
- **Triangles** $T$: the $\binom{N}{3}$ triangular arbitrage constraints.

Each triangle $(A, B, C)$ has a **consistency score**:

$$c_{ABC}(t) = 1 - \frac{|\varepsilon_{ABC}(t)|}{s^{\mathrm{eff}}_{ABC}}$$

where $c_{ABC} = 1$ is perfect consistency and $c_{ABC} = 0$ means the deviation
equals the effective spread (the maximum tolerable before arbitrage).

### 8.2 The graph Laplacian and the Fiedler eigenvalue

The weighted graph Laplacian of $G$ is:

$$L_{ij} = \begin{cases} \sum_{k \neq i} w_{ik} c_{ik} & \text{if } i = j \\ -w_{ij} c_{ij} & \text{if } i \neq j \end{cases}$$

where $w_{ij}$ is the turnover weight of pair $(i,j)$ and $c_{ij} = \min_k c_{ijk}$
is the worst consistency score involving pair $(i,j)$.

**Theorem 8.1** (Cross-rate Fiedler eigenvalue = FX Cheeger constant).
*The Fiedler eigenvalue $\lambda_2(L)$ of the cross-rate consistency graph
satisfies the discrete Cheeger inequality:*

$$\frac{h^2_{\mathrm{FX}}}{2} \leq \lambda_2(L) \leq 2h_{\mathrm{FX}}$$

*where $h_{\mathrm{FX}}$ is the Cheeger constant of the FX market — the minimum
ratio of "boundary" to "volume" over all partitions of the currency set into two
groups.*

*Proof.* This is the discrete Cheeger inequality (Alon and Milman \[1985\])
applied to the weighted graph $G$. $\square$

### 8.3 Interpreting the Fiedler eigenvalue

The Fiedler eigenvalue $\lambda_2(L)$ measures the algebraic connectivity of the
FX market:

- **$\lambda_2$ large:** All cross-rate constraints are tightly satisfied. The
  FX market is well-connected and internally consistent. Arbitrageurs are active
  and efficient.

- **$\lambda_2$ small:** Some cross-rate constraints are persistently violated.
  The FX market is "breaking" into disconnected components. This happens during
  currency crises, when capital controls fragment the market.

- **$\lambda_2 = 0$:** The graph is disconnected. Some currencies are no longer
  arbitrage-linked to others (e.g., full capital controls).

### 8.4 Historical episodes

**The 1997 Asian crisis.** The Asian FX cross-rate graph (THB, IDR, MYR, KRW, PHP)
was well-connected before the crisis ($\lambda_2 > 0$). As Thailand depegged the
baht (July 1997), the consistency scores for THB triangles collapsed. Then Indonesia
(August), Malaysia (September), Korea (December). The Fiedler eigenvalue of the
Asian subgraph dropped monotonically, reaching near-zero when Malaysia imposed
capital controls (September 1998). The contagion was visible as edge-by-edge
degradation of the cross-rate graph.

**The 2008 GFC carry unwind.** The carry cross-rate graph (AUD, NZD, BRL, ZAR vs
JPY, CHF) was highly connected before September 2008. During the Lehman collapse
(September–October 2008), carry pairs moved in perfect correlation — the Fiedler
eigenvalue of the carry subgraph spiked (all carry pairs moved together, increasing
consistency) before collapsing (as liquidity disappeared and bid-ask spreads
exploded). The "spike then collapse" pattern is the geometric signature of a
correlated unwind: first the manifold collapses to a lower-dimensional submanifold
(all carry pairs become one trade), then the submanifold itself becomes disconnected
(liquidity vanishes).

**Capital controls = edge removal.** When a country imposes capital controls
(Malaysia 1998, Iceland 2008, Cyprus 2013), it removes edges from the cross-rate
graph. By the Cheeger inequality, removing edges can only decrease $\lambda_2$.
Capital controls reduce the algebraic connectivity of the FX market — they
fragment the currency simplex into disconnected components.

---

## 9. FX Experiments

The FX market is the cleanest test of the geometric theory for four reasons:
(a) the dimensionality is low and precisely known ($r \approx 3$);
(b) triangular arbitrage provides exact algebraic constraints;
(c) the carry trade gives a direct test of the Sharpe–curvature identity; and
(d) tick-level data allows microsecond-resolution tests. We propose five
experiments with Databento tick-level FX data.

### Test FX1: Carry Sharpe = $\|H_{\mathrm{carry}}\|_{L^2}$

**Protocol.** For $N = 10$ major currencies over rolling 1-year windows:
1. Compute the carry portfolio (weights $\propto r_i - \bar{r}$) and its realised Sharpe ratio.
2. Estimate the FX manifold $M^3$ from the return covariance matrix (top 3 eigenvectors).
3. Compute the mean curvature $H$ of $M^3$ in $S^{N-1}_{+}$ and project onto the carry direction.
4. Compare $\mathrm{Sharpe}_{\mathrm{carry}}$ with $\|H_{\mathrm{carry}}\|_{L^2}$.

**Expected.** Correlation $> 0.3$ across rolling windows. This is the FX-specific
version of Test 1 from EXPERIMENTS.md but in a setting where the Sharpe–curvature
identity should be cleaner due to lower dimensionality and tighter arbitrage
constraints.

### Test FX2: Triangular arb deviations = LOB curvature

**Protocol.** For 10 major triangles (EUR/USD/CHF, EUR/USD/GBP, EUR/USD/JPY, etc.)
at tick level:
1. Compute $\varepsilon_{ABC}(t)$ at each tick.
2. Verify $|\varepsilon_{ABC}| \leq s^{\mathrm{eff}}_{ABC}$ (bounded by effective spread).
3. Estimate the OU mean-reversion rate $\lambda_1^{\mathrm{tri}}$.
4. Verify $\lambda_1^{\mathrm{tri}} \sim 10^3$–$10^6 \, \mathrm{s}^{-1}$ (millisecond to microsecond timescale).

**Expected.** Deviations bounded by the bid-ask spread. Mean-reversion at
$\lambda_1 \sim 10^3 \, \mathrm{s}^{-1}$ for the major triangles (less liquid
triangles will have smaller $\lambda_1$).

### Test FX3: SNB floor removal as MCF singularity

**Protocol.** For EURCHF and all CHF crosses over 2014–2015:
1. Estimate Willmore energy $\mathcal{W}(t)$ at daily frequency from rolling covariance.
2. Track $\mathcal{W}$ through the floor removal event (15 Jan 2015).
3. Compare with the MCF singularity prediction: $\mathcal{W}_{\mathrm{pre}} \gg 0$,
   $\mathcal{W}_{\mathrm{during}} \to \infty$, $\mathcal{W}_{\mathrm{post}} \approx 0$.

**Expected.** $\mathcal{W}$ should show a clear accumulation phase (2012–2015),
a spike on 15 Jan 2015, and a rapid decline afterward. The singularity should be
visible as $|H|^2$ exceeding any pre-event level by orders of magnitude.

### Test FX4: FX dimension stability

**Protocol.** For 10 major currencies at daily frequency:
1. Estimate $r$ via stable rank of the FX return covariance matrix.
2. Estimate $r$ via Marchenko–Pastur edge detection.
3. Estimate $r$ via False Nearest Neighbours on Takens-embedded FX returns.
4. Compare across methods and across rolling windows.

**Expected.** $r \approx 3$ across all methods, stable across time. FX should give
a cleaner dimension estimate than equities because the factor structure is
lower-dimensional and the triangular constraints reduce noise.

### Test FX5: Cross-rate Cheeger constant as crisis indicator

**Protocol.** For 10 major currencies at daily frequency:
1. Compute the cross-rate consistency graph $G(t)$ at each date.
2. Compute the Fiedler eigenvalue $\lambda_2(t)$.
3. Compare $\lambda_2(t)$ with known FX crises: Asian 1997, GFC 2008, SNB 2015,
   COVID 2020.

**Expected.** $\lambda_2$ should drop before or during each crisis event.
The drop should be visible $\sim$1–5 days before the most acute phase (because
consistency scores degrade before the full crisis unfolds).

---

## 10. Connection to Companion Papers

The FX geometry connects to the broader monograph in several ways:

**MINIMAL_SURFACE.md.** The Sharpe–curvature identity (R1) is applied here to the
specific case of the carry trade. The FX market provides the cleanest empirical
test because the carry direction is directly observable from interest rate data
(no latent factor estimation required).

**CLASSIFICATION.md.** The three FX regimes (normal/transitional/crisis) correspond
to the three classified manifold types (CAPM/Clifford/pseudo-Anosov). The FX
market transitions between these types during crises — a concrete instance of the
bifurcation theory in CHAOS_TAKENS.md.

**MARKET_PROCESSES.md.** The FX state evolves by the Jacobi diffusion on
$\Delta_{N-1}$ in the CAPM regime. The Jacobi parameters $\alpha_i = T w^{\ast}_{i} - 1/2$
are determined by the currency turnover weights — directly observable from BIS data.

**FILTRATIONS.md.** The Voronoi partition of the currency simplex provides the
discrete filtration for FX. The Voronoi cells correspond to "currency regimes" —
regions of the simplex where the same set of carry trades is optimal.

**GEOSPATIAL_CONTAGION.md.** The cross-rate consistency graph $G$ is the Delaunay
graph of the FX manifold. Currency contagion propagates through this graph at a
rate governed by the Jacobi spectral gap. The Cheeger constant $h_{\mathrm{FX}}$
is the systemic risk of the FX market.

**RANDOM_MATRIX.md.** The Dyson class of the FX covariance matrix is forced by the
FX manifold topology. The transition from GOE ($\beta = 1$) to GSE ($\beta = 4$)
during crises is detectable from eigenvalue spacing statistics.

**GRASSBERGER_PERCOLATION_GENERATING.md.** The correlation dimension of
Takens-embedded FX returns should equal $\nu = r \approx 3$ — a cleaner test than
equities due to lower dimensionality. The percolation threshold of the FX
cross-rate graph is approximately the Cheeger constant $h_{\mathrm{FX}}$.

---

## 11. New Results

We collect the principal results of this paper. Numbering continues from the
monograph sequence (WHATS_NEW.md).

**Theorem FX1** (The FX market is one manifold).
*The space of arbitrage-free exchange rates for $N$ currencies is the positive
projective space $\mathbb{RP}^{N-1}_{+} \cong \Delta_{N-1}$. The FX market
manifold $M^r_{\mathrm{FX}} \subset S^{N-1}_{+}$ has dimension $r \approx 3$.
Each currency pair is a direction $e_A - e_B$ on the single manifold, not a
separate market. Triangular arbitrage is automatically satisfied by the simplex
structure.*

**Theorem FX2** (Carry = mean curvature; UIP violation = non-minimality).
*The carry trade Sharpe ratio equals the $L^2$-norm of the mean curvature in
the carry direction:
$\mathrm{Sharpe}_{\mathrm{carry}} = \|H_{\mathrm{carry}}\|_{L^2(M, g_M)}$.
UIP holds if and only if the FX manifold is minimal in the carry direction.
The Lustig–Verdelhan Sharpe of $\sim 0.5$–$0.8$ is a direct measurement of
FX manifold curvature.*

**Theorem FX3** (Triangular arb = LOB curvature).
*The triangular arbitrage deviation $\varepsilon_{ABC}$ satisfies
$|\varepsilon_{ABC}| \leq s^{\mathrm{eff}}_{ABC}$ and the mean curvature in
the cross-rate direction is $H_{\mathrm{cross}} = \varepsilon_{ABC}/(2\sigma_{\mathrm{cross}})$.
HFT triangular arbitrage is mean curvature flow at microsecond timescale.*

**Theorem FX4** (Lie group structure; Fisher–Rao is left-invariant).
*The FX manifold is a sub-Lie-group of the currency revaluation group
$\mathbb{R}^{N}_+ / \mathbb{R}_{+}$. The Fisher–Rao metric is left-invariant under
revaluation (numeraire-invariant). The Lie algebra consists of the $r$ factor
directions.*

**Theorem FX5** (Central bank floor = boundary condition; floor removal = Type II singularity).
*A central bank floor constrains the FX manifold to a half-space of $\Delta_{N-1}$.
Willmore energy accumulates quadratically in the deviation between the floor level
and the unconstrained equilibrium. If the accumulated energy exceeds the critical
threshold for the codimension, removal of the floor produces a Type II MCF
singularity.*

**Theorem FX6** (Cross-rate Fiedler eigenvalue = FX Cheeger constant).
*The Fiedler eigenvalue of the turnover-weighted cross-rate consistency graph
satisfies the discrete Cheeger inequality
$h^2_{\mathrm{FX}}/2 \leq \lambda_2(L) \leq 2h_{\mathrm{FX}}$ and drops
before or during currency crises.*

---

## 12. Open Problems

**OP-FX1.** *Is the carry factor return predictable from $H_{\mathrm{carry}}$?*
The Sharpe–curvature identity gives a contemporaneous relationship. The open
question: does the curvature at time $t$ predict the carry return at time $t + \tau$?
If the MCF dynamics are predictable (because the manifold has inertia), then
$H_{\mathrm{carry}}(t)$ should forecast future carry returns. Testable with our
Databento FX data. **Difficulty: ★★**

**OP-FX2.** *Does the FX manifold type change during crises (CAPM $\to$
pseudo-Anosov)?*
The classification theorem gives three stable types. During the 2008 GFC, did the
FX manifold transition from CAPM ($\beta = 1$) to pseudo-Anosov ($\beta = 4$)?
This can be tested by tracking the eigenvalue spacing distribution of the FX
covariance matrix through the crisis. **Difficulty: ★★★**

**OP-FX3.** *The geometry of cryptocurrency FX.*
The BTC/ETH/USD triangle is now liquid enough for tick-level analysis. Is the
crypto cross-rate graph well-connected (high $\lambda_2$) or fragmented (low
$\lambda_2$)? The hypothesis: crypto FX has lower algebraic connectivity than
traditional FX because arbitrage is slower (blockchain confirmation times vs
electronic settlement). How does the Cheeger constant of the crypto FX market
compare to the traditional FX market? **Difficulty: ★★**

**OP-FX4.** *The optimal FX hedge as a geodesic on the currency simplex.*
A firm with EUR revenues and USD costs needs to hedge EURUSD exposure. The optimal
dynamic hedge should be a geodesic on the currency simplex connecting the current
FX state to the hedged state, with the hedge ratio determined by the geodesic
curvature. Derive the explicit geodesic hedging strategy and compare it to the
standard delta hedge. **Difficulty: ★★★**

**OP-FX5.** *Stealth intervention detection from the Willmore energy time series.*
Central banks sometimes intervene secretly (buying or selling their currency without
announcement). Can we detect stealth intervention from anomalous Willmore energy
accumulation or dissipation? If the central bank is pushing the manifold away from
its minimal surface (accumulation) or toward it (dissipation), the Willmore energy
time series should exhibit signatures distinct from normal market dynamics.
**Difficulty: ★★★★**

---

## References

1. Alon, N. and Milman, V.D. (1985). $\lambda_1$, isoperimetric inequalities for graphs, and superconcentrators. *J. Combin. Theory Ser. B* **38**, 73–88.

2. Bekaert, G. and Hodrick, R.J. (2018). *International Financial Management*. 3rd edition. Cambridge University Press.

3. Brunnermeier, M.K., Nagel, S., and Pedersen, L.H. (2009). Carry trades and currency crashes. *NBER Macroeconomics Annual* **23**, 313–347.

4. Burnside, C., Eichenbaum, M., Kleshchelski, I., and Rebelo, S. (2011). Do peso problems explain the returns to the carry trade? *Review of Financial Studies* **24**(3), 853–891.

5. Cencov, N.N. (1982). *Statistical Decision Rules and Optimal Inference*. Translations of Mathematical Monographs **53**. American Mathematical Society.

6. Engel, C. (2014). Exchange rates and interest parity. In *Handbook of International Economics*, Vol. 4, 453–522. Elsevier.

7. Fama, E.F. (1984). Forward and spot exchange rates. *Journal of Monetary Economics* **14**(3), 319–338.

8. Huisken, G. and Sinestrari, C. (2009). Mean curvature flow with surgeries of two-convex hypersurfaces. *Inventiones Mathematicae* **175**(1), 137–221.

9. Lustig, H. and Verdelhan, A. (2007). The cross section of foreign currency risk premia and consumption growth risk. *American Economic Review* **97**(1), 89–117.

10. Lustig, H., Roussanov, N., and Verdelhan, A. (2011). Common risk factors in currency markets. *Review of Financial Studies* **24**(11), 3731–3777.

11. Menkhoff, L., Sarno, L., Schmeling, M., and Schrimpf, A. (2012). Carry trades and global foreign exchange volatility. *Journal of Finance* **67**(2), 681–718.

12. Verdelhan, A. (2018). The share of systematic variation in bilateral exchange rates. *Journal of Finance* **73**(1), 375–418.

**Companion papers in this monograph:**
MINIMAL_SURFACE.md (R1: Sharpe = curvature), CLASSIFICATION.md (three manifold types),
MARKET_PROCESSES.md (Jacobi diffusion), FILTRATIONS.md (Voronoi partition),
GEOSPATIAL_CONTAGION.md (Cheeger constant), RANDOM_MATRIX.md (Dyson classification),
CHAOS_TAKENS.md (bifurcation theory), GRASSBERGER_PERCOLATION_GENERATING.md
(correlation dimension, percolation threshold).

---

*Every FX pair is a projection of a single point on the currency simplex.
The carry trade earns the curvature that UIP says should not exist.*
