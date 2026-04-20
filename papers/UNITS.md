# Units, Dimensions, and Dimensionless Numbers
## A Complete Reference for the Geometric Theory of Efficient Markets

**Saxon Nicholls** — me@saxonnicholls.com

**Paper 0.7** — Foundation

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
Every quantity in this monograph has a unit, a dimension, and a scaling behaviour
under time aggregation. Some quantities are dimensionless invariants — they have
the same value whether you measure daily, weekly, or monthly. Others scale with
the measurement period. Confusing the two has caused errors in our own experimental
programme (the spectral hierarchy exponent β mixed invariant ratios with
non-invariant absolute rates). This paper catalogues every quantity, its units,
its scaling, and whether it is a geometric invariant. We define six dimensionless
market numbers analogous to the Reynolds, Mach, and Prandtl numbers of fluid
dynamics.

---

## 1. The Fundamental Quantities

### 1.1 The base units

The theory has three independent base units:

| Base unit | Symbol | Meaning |
|:----------|:------:|:--------|
| **Asset** | — | An index $i \in \{1, \ldots, d\}$. Dimensionless count. |
| **Time** | $[T]$ | Measured in periods (days, weeks, months). |
| **Return** | $[R]$ | Log-return per period. Dimensionless ratio. |

Note: returns are already dimensionless ($r = \log(P_{t+1}/P_t)$, a ratio of
prices). There is no "price unit" in the theory — all prices appear as ratios.

### 1.2 Derived units

| Quantity | Symbol | Unit | Definition |
|:---------|:------:|:----:|:-----------|
| Portfolio weight | $b_i$ | dimensionless | $b_i \in [0,1]$, $\sum b_i = 1$ |
| Return | $r_{t,i}$ | $[R]$ per $[T]$ | Log-return of asset $i$ in period $t$ |
| Growth rate | $L_T(b)$ | $[R]$ per $[T]$ | $(1/T)\sum_t \log\langle b, x_t\rangle$ |
| Covariance | $\Sigma_{ij}$ | $[R]^2$ per $[T]$ | Scales as $c(n)$ under aggregation |
| Eigenvalue | $\lambda_k$ | $[R]^2$ per $[T]$ | Same scaling as covariance |
| Fisher-Rao metric | $g^{\rm FR}_{ij}$ | $1/b_i$ | Dimensionless (weights are dimensionless) |
| Mean curvature | $H$ | $1/\sqrt{[R]^2 \cdot [T]}$ | Depends on both metric and embedding |
| Willmore energy | $\mathcal{W}$ | dimensionless | $\int \|H\|^2 d\mathrm{vol}$ (integral of squared curvature) |
| Spectral gap | $\lambda_1(L)$ | $1/[T]$ | Rate (per period) |
| Mean-reversion speed | $\kappa$ | $1/[T]$ | Rate (per period) |
| Half-life | $t_{1/2}$ | $[T]$ | Time (in periods) |
| Cheeger constant | $h_M$ | dimensionless | Ratio of flow to probability (no units) |
| Channel capacity | $C$ | bits per $[T]$ | Information rate |

---

## 2. The Dimensionless Numbers

### 2.1 Numbers that are ALWAYS dimensionless

These have no units regardless of how you measure them:

| Number | Symbol | Formula | Value (US equities) | Meaning |
|:-------|:------:|:--------|:-------------------:|:--------|
| **Concentration** | $\mathcal{C}$ | $\lambda_1 / \sum\lambda_k$ | 0.84 | Fraction of variance in the dominant factor |
| **Entropy** | $\mathcal{E}$ | $H(\lambda)/\log d$ | 0.26 | Evenness of the eigenvalue spectrum |
| **Effective rank** | $r_{\rm eff}$ | $\exp(H(\lambda))$ | 2.35 | Continuous manifold dimension |
| **Stable rank** | $r_{\rm stable}$ | $\|\Sigma\|_F^2/\|\Sigma\|_2^2$ | 1.01 | Participation ratio |
| **Dimension** | $r$ | $\min\{k : \sum_{i=1}^{k} \lambda_i / \sum\lambda > 0.9\}$ | 3 | Manifold dimension (integer) |
| **Sharpe ratio** | $\mathrm{Sharpe}$ | $\mu / \sigma$ | — | Return per unit risk (dimensionless) |
| **Eigenvalue ratio** | $\lambda_i/\lambda_j$ | — | — | Relative factor importance |

### 2.2 Numbers that become dimensionless by construction

These require combining dimensional quantities to cancel units:

| Number | Symbol | Formula | Meaning |
|:-------|:------:|:--------|:--------|
| **Sharpe-curvature** | $\mathcal{S}$ | $\mathrm{Sharpe}^{\ast}/\|H\|_{L^2}$ | Should equal 1.0 (the central theorem) |
| **Reynolds** | $\mathrm{Re}_{M}$ | $\|H\| \cdot T^2 \cdot \mathrm{diam}(M)$ | Laminar (<1) vs turbulent (>10) |
| **Cheeger** | $\mathcal{H}$ | $h_M \cdot \mathrm{diam}(M)$ | Connectivity relative to size |
| **Mixing** | $\mathcal{M}$ | $t_{\rm mix} / T$ | Mixing time relative to observation |
| **Regret ratio** | $\rho$ | $(d-1)/r$ | Dimension reduction factor |
| **Merger payback** | $\tau_{\rm pay}$ | $T_{\rm payback} / T_{\rm observation}$ | How long until a merger pays for itself |
| **Overround** | $\Omega$ | $\sum(1/o_i) - 1$ | Bookmaker's margin (dimensionless) |

### 2.3 The six principal dimensionless numbers

These are the "Reynolds numbers" of the geometric theory — the numbers that
characterise a market's geometric state completely:

| # | Name | Symbol | Formula | Range | Interpretation |
|:-:|:-----|:------:|:--------|:-----:|:---------------|
| 1 | **Sharpe-curvature** | $\mathcal{S}$ | $\mathrm{Sharpe}^{\ast}/\|H\|_{L^2}$ | $(0, \infty)$ | 1.0 = theory exact |
| 2 | **Concentration** | $\mathcal{C}$ | $\lambda_1/\sum\lambda$ | $(1/d, 1)$ | 1 = one factor; 1/d = uniform |
| 3 | **Entropy** | $\mathcal{E}$ | $H(\lambda)/\log d$ | $(0, 1)$ | 0 = concentrated; 1 = uniform |
| 4 | **Reynolds** | $\mathrm{Re}_{M}$ | $\|H\|T^2\mathrm{diam}$ | $(0, \infty)$ | <1 efficient; >10 inefficient |
| 5 | **Cheeger** | $\mathcal{H}$ | $h_M\cdot\mathrm{diam}$ | $(0, \infty)$ | 0 = crisis; large = healthy |
| 6 | **Mixing** | $\mathcal{M}$ | $t_{\rm mix}/T$ | $(0, \infty)$ | ≪1 = ergodic; ≫1 = non-ergodic |

Together, $(\mathcal{S}, \mathcal{C}, \mathcal{E}, \mathrm{Re}_{M}, \mathcal{H}, \mathcal{M})$
characterise the geometric state of any market. Two markets with the same six
numbers have the same geometric structure — regardless of the number of assets,
the time period, or the currency.

---

## 3. Scaling Under Time Aggregation

### 3.1 The aggregation theorem

**Theorem 3.1** *(Aggregation scaling)*. *Under $n$-period aggregation of a
stationary process, each quantity scales as follows:*

| Quantity | Scaling | Invariant? |
|:---------|:--------|:----------:|
| Covariance $\Sigma$ | $\times\, c(n)$ | No |
| Eigenvalue $\lambda_k$ | $\times\, c(n)$ | No |
| Eigenvalue ratio $\lambda_i/\lambda_j$ | $\times\, 1$ | **Yes** |
| Eigenvalue fraction $\lambda_k/\sum\lambda$ | $\times\, 1$ | **Yes** |
| Eigenvectors $v_k$ | unchanged | **Yes** |
| Spectral entropy $H$ | unchanged | **Yes** |
| Effective rank $r_{\rm eff}$ | unchanged | **Yes** |
| Manifold dimension $r$ | unchanged | **Yes** |
| Mean-reversion speed $\kappa$ | $\times\, 1/n$ | No |
| Half-life $t_{1/2}$ | $\times\, n$ | No |
| Sharpe ratio | $\times\, 1$ (annualised) | **Yes** (if annualised) |
| $\|H\|$ | $\times\, 1/\sqrt{c(n)}$ | No |
| Willmore energy $\mathcal{W}$ | $\times\, 1$ (integrated) | **Yes** (if integrated over the manifold) |
| Cheeger constant $h_M$ | unchanged | **Yes** |

*where $c(n) \approx n$ for i.i.d. and $c(n) = n(1 + 2\rho/(1-\rho))$ for AR(1).*

### 3.2 The invariance principle

**The dimensionless numbers $\mathcal{S}, \mathcal{C}, \mathcal{E}, \mathrm{Re}_M,
\mathcal{H}, \mathcal{M}$ are invariant under time aggregation** because they are
constructed from ratios and normalised quantities. Any empirical test should be
formulated in terms of these invariants, never in terms of absolute quantities
like $\lambda_k$ or $\kappa$.

---

## 4. Units by Paper

### Part 0: Foundations

| Paper | Key quantity | Unit | Dimensionless? |
|:------|:-----------|:-----|:--------------:|
| CONVEX_INFORMATION | Divergence $D(p,q)$ | dimensionless (radians) | Yes |
| CONVEXIFICATION | Convexification dimension $N$ | count | Yes |
| DUAL_TOWER | Giry level $k$ | count | Yes |
| INCOMPLETENESS | Kolmogorov complexity $K$ | bits | No (depends on encoding) |

### Part I: Core Theory

| Paper | Key quantity | Unit | Dimensionless? |
|:------|:-----------|:-----|:--------------:|
| LAPLACE | Approximation error | dimensionless (ratio) | Yes |
| MINIMAL_SURFACE | Sharpe ratio $\mathrm{Sharpe}^{\ast}$ | dimensionless | **Yes** |
| MINIMAL_SURFACE | Mean curvature $\|H\|$ | $1/\sqrt{[R]^2[T]}$ | No |
| MINIMAL_SURFACE | Willmore energy $\mathcal{W}$ | dimensionless | **Yes** |
| CLASSIFICATION | Stability index $\mathrm{ind}(\Sigma)$ | count | Yes |
| CLASSIFICATION | Spectral gap $\lambda_1(L)$ | $1/[T]$ | No |
| CLASSIFICATION | $\mathcal{C}, \mathcal{E}, r$ | dimensionless | **Yes** |
| CONVERGENCE | Regret $r\log T/(2T)$ | $[R]$ (cumulative) | No |
| CONVERGENCE | Regret ratio $(d-1)/r$ | dimensionless | **Yes** |

### Part II: Physics and Processes

| Paper | Key quantity | Unit | Dimensionless? |
|:------|:-----------|:-----|:--------------:|
| INFORMATION_THEORY | Kelly rate $h_{\rm Kelly}$ | $[R]/[T]$ | No |
| HAMILTONIAN | Tail index $\alpha$ | dimensionless | **Yes** |
| MARKET_PROCESSES | Jacobi parameter $\alpha_i$ | dimensionless | **Yes** |
| DERIVATIVES | Option price | currency | No |
| DERIVATIVES | Implied vol $\sigma_{\rm impl}$ | $\sqrt{[R]^2/[T]}$ | No |
| RENORMALIZATION | $\mathrm{Re}_{M}$ | dimensionless | **Yes** |
| FOKKER_PLANCK | Stationary density $\rho$ | $1/\mathrm{vol}$ | No |

### Part III: Topology

| Paper | Key quantity | Unit | Dimensionless? |
|:------|:-----------|:-----|:--------------:|
| FIBER_BUNDLES | Chern class $c_1$ | integer | Yes |
| FIBER_BUNDLES | Berry phase $\gamma$ | radians | Yes |
| BRAIDS | Braid word length $\ell(\beta)$ | count | Yes |
| FILTRATIONS | LZ complexity $c_{\rm LZ}$ | count | Yes |
| FILTRATIONS | Compression rate $c\log c/T$ | bits/$[T]$ | No |

### Part IV: New Domains

| Paper | Key quantity | Unit | Dimensionless? |
|:------|:-----------|:-----|:--------------:|
| RANDOM_MATRIX | Dyson class $\beta$ | $\{1,2,4\}$ | Yes |
| SHAPLEY | $\phi_i = b^{\ast}_{i}(\mu_i - \bar\mu)$ | $[R]/[T]$ | No |
| CREDIT_RISK | Credit spread $s$ | $[R]/[T]$ | No |
| CREDIT_RISK | Distance to default $d_{\rm FR}$ | dimensionless (radians) | **Yes** |
| YIELD_CURVES | Nelson-Siegel $\lambda$ | $1/[T]$ | No |
| VOL_SURFACE | Butterfly $\partial^2\sigma/\partial k^2$ | $1/[R]^2$ | No |
| MICROSTRUCTURE | Bid-ask spread $s$ | currency | No |
| MICROSTRUCTURE | $d_{\rm FR}(b^{\rm bid}, b^{\rm ask})$ | dimensionless | **Yes** |
| NETWORK_INFO | Channel capacity $C$ | bits/$[T]$ | No |
| NETWORK_INFO | $R_{\rm conv} = \min(\lambda_1, C)$ | $1/[T]$ | No |

### Part V-VII: Applications and Political Economy

| Paper | Key quantity | Unit | Dimensionless? |
|:------|:-----------|:-----|:--------------:|
| BETTER_INDEX | MIF excess return | $[R]/[T]$ | No |
| INTERMARKET | Neck cost $\mathcal{W}_{\rm neck}$ | dimensionless | **Yes** |
| INTERMARKET | Payback period $T_{\rm payback}$ | $[T]$ | No |
| INTERMARKET | $k/r$ (shared factor ratio) | dimensionless | **Yes** |
| TOPOLOGY_PRICE | Deadweight loss $= \mathcal{W}$ | dimensionless | **Yes** |
| EMU_CASE | Spread $\propto (1-k/r)$ | dimensionless | **Yes** |

---

## 5. Rules for Empirical Tests

Based on the invariance analysis:

**Rule 1:** Always test DIMENSIONLESS predictions. If the theory predicts
$\mathcal{S} = 1$, test that. Don't test $\mathrm{Sharpe} = \|H\|$ directly
(both sides have units that cancel in the ratio).

**Rule 2:** If a quantity is NOT dimensionless, NORMALISE it before comparing
across datasets or frequencies. Divide by the appropriate power of $\sum\lambda$
or $T$ to make it dimensionless.

**Rule 3:** The spectral hierarchy exponent $\beta$ is NOT dimensionless (it
relates $\kappa_k/\kappa_1$, which has units $[T]^0$ but depends on the time
unit through $\kappa$, to $\lambda_1/\lambda_k$, which is dimensionless). To
make a dimensionless prediction, express the hierarchy as:
```math
\frac{t_{1/2}^{(k)} / t_{1/2}^{(1)}}{\lambda_k / \lambda_1} = \text{const?}
```
Both sides are dimensionless. This is the correctly formulated test.

**Rule 4:** When comparing across asset classes, only compare dimensionless numbers.
$\mathcal{C} = 0.84$ (US equities) vs $\mathcal{C} = 0.67$ (sectors) is a meaningful
comparison. $\lambda_1 = 0.068$ (US equities) vs $\lambda_1 = 0.017$ (sectors) is
meaningless without knowing the time period and units.

---

## References

Buckingham, E. (1914). On physically similar systems.
*Physical Review* 4(4), 345–376. (The Pi theorem.)

Barenblatt, G. I. (1996). *Scaling, Self-Similarity, and Intermediate
Asymptotics*. Cambridge University Press.

*[All other references as per companion papers.]*
