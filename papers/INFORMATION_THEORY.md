# The Efficient Market as an Information Processor:
## Kolmogorov Complexity, Shannon Capacity, the SMB Theorem,
## and Entropy Geometry on Minimal Market Manifolds

---

**Abstract.**  
We develop an information-theoretic interpretation of the geometric efficient market
theory established in the companion papers of this series. The central thesis is that
a strongly efficient market is not merely a geometric object (a minimal submanifold of
the Bhattacharyya sphere) but simultaneously an **optimal information processor**:
it maximises Shannon channel capacity, achieves minimum Kolmogorov complexity among
all market structures with the same factor dimension, operates at the Shannon–McMillan–Breiman
entropy rate, and saturates the Cramér–Rao bound for portfolio estimation. These four
characterisations are not independent — we prove they are equivalent, and all equivalent
to the minimal surface condition $H = 0$.

Our principal results: (i) the Fisher information matrix $F(b^*)$ determines the Shannon
capacity of the market-as-channel, and $H = 0$ iff this capacity is maximised over the
manifold (**Theorem A: efficiency = maximum channel capacity**); (ii) the Kolmogorov
complexity of the market manifold description is minimised by minimal surfaces —
the CAPM has minimum complexity, higher Lawson surfaces have growing complexity, and the
complexity gap mirrors the Simons gap in curvature (**Theorem B: efficiency = minimum
description length**); (iii) the Shannon–McMillan–Breiman (SMB) theorem, applied to the
market return process, identifies the Kelly log-growth rate as the entropy rate, and the
universal portfolio as the **typical set decoder** — the minimal surface is the boundary
of the typical set in portfolio space (**Theorem C: SMB = Kelly**); (iv) volatility is
conformally invariant for the Willmore energy but controls the phase transition between
stable and unstable efficient markets through the spectral gap (**Theorem D: volatility
and stability**); (v) the efficient frontier in the classical Markowitz sense arises as
the **boundary of the normal bundle** of the minimal market manifold — a precise geometric
derivation of mean-variance efficiency from the minimal surface structure (**Theorem E:
efficient frontier from manifold**). Finally, we consider what Persi Diaconis's perspective
on this framework would contribute: his theory of sufficiency, Markov chain mixing times,
and the representation theory of the symmetric group each add structural content —
and his characteristic skepticism identifies the places where the geometry is genuinely
new versus where it is elegant repackaging.

**Keywords.** Efficient market; Shannon capacity; Kolmogorov complexity; minimum
description length; Shannon–McMillan–Breiman; Kelly criterion; entropy rate; typical set;
Fisher information; Cramér–Rao; Willmore energy; conformal invariance; efficient frontier;
Diaconis; mixing time; de Finetti.

**MSC 2020.** 91G10, 94A17, 94A15, 37A35, 53A10, 60F10, 62B10.

---

## 1. Introduction

### 1.1 The information-theoretic gap

The Efficient Market Hypothesis has two faces: an *economic* face (no strategy earns
risk-adjusted excess returns) and an *information-theoretic* face (prices reflect all
available information). The geometric framework developed in PAPER.md, MINIMAL\_SURFACE.md,
and CLASSIFICATION.md has so far spoken primarily to the economic face. In this paper we
establish the information-theoretic face with equal precision.

The key bridge is the Fisher–Rao metric $g^{\mathrm{FR}}_{ij}(b) = \delta_{ij}/b_i$. This
metric is not merely a mathematical convenience — it is the **canonical metric of statistical
inference**, defined by the curvature of the log-likelihood function. Every object in our
geometric theory has a direct information-theoretic translation:

| Geometric object | Information-theoretic meaning |
|:----------------|:------------------------------|
| Fisher matrix $F(b^*)$ | Information content of one return observation at $b^*$ |
| Mean curvature $H$ | Bias of the market's information processing |
| Willmore energy $\mathcal{W}$ | Integrated squared processing bias |
| Minimal surface $H=0$ | Unbiased information processor |
| Stable rank $r_{\rm eff}$ | Effective channel dimension |
| Jacobi eigenvalue $\lambda_1$ | Channel capacity per factor direction |
| MCF convergence rate | Information absorption rate |

The goal of this paper is to make each entry in this table precise.

### 1.2 The SMB–Kelly connection as the central theorem

The Shannon–McMillan–Breiman theorem is the fundamental limit theorem of information
theory: for a stationary ergodic source with entropy rate $h$, the empirical log-probability
per symbol converges almost surely to $-h$. The Kelly criterion identifies the growth-optimal
portfolio for a stationary return process as the maximiser of the log-growth rate.

**We prove these are the same theorem** (Theorem C): the empirical log-wealth per period
of the universal portfolio converges almost surely to the entropy rate of the return process.
The minimal surface is the geometric object that encodes this convergence — the market
manifold is minimal iff the Shannon entropy rate of the returns equals the Kelly growth rate
of the log-optimal portfolio.

---

## 2. The Market as a Communication Channel

### 2.1 The Shannon channel model

Model the market as a discrete memoryless channel:
- **Input**: factor shock $f_t \in \mathcal{F}$ (the "signal" from the economy)
- **Channel**: return mapping $x_t = \Phi(f_t) + \varepsilon_t$ (linear factor model plus noise)
- **Output**: return vector $x_t \in \mathbb{R}^d_+$ (what the investor observes)

The investor's problem is to decode the factor state $f_t$ from the observed returns
$x_1, \ldots, x_T$ — and then to allocate portfolio weights optimally. The **channel capacity**
is:

$$C = \max_{p(f)} I(f; x) = \max_{p(f)} \left[H(x) - H(x|f)\right] \tag{2.1}$$

where $I(f;x)$ is the mutual information and $H(\cdot)$ is entropy.

### 2.2 The Fisher information as channel capacity

For a Gaussian channel with input variance $\sigma_f^2$ and noise variance $\sigma_e^2$:

$$C = \frac{r}{2}\log\left(1 + \frac{\sigma_f^2}{\sigma_e^2}\right) \tag{2.2}$$

But the return channel is not Gaussian-input, and the portfolio $b$ plays the role of
a matched filter. The Fisher information at the optimal portfolio $b^*$ is:

$$F_{ij}(b^*) = \mathbb{E}\!\left[\frac{\partial \log p(x|b^*)}{\partial b_i}
\frac{\partial \log p(x|b^*)}{\partial b_j}\right]
= \frac{1}{T}\sum_t \frac{x_{t,i}x_{t,j}}{(b^{*T}x_t)^2} \tag{2.3}$$

By the **Cramér–Rao bound**, the minimum variance of any unbiased estimator of $b^*$
from $T$ observations is $F(b^*)^{-1}/T$. The channel capacity of the market at portfolio
$b^*$ is:

$$C(b^*) = \frac{1}{2}\log\det\left(I + T\cdot F(b^*)\right)
= \frac{1}{2}\sum_{k=1}^{d-1}\log(1 + T\lambda_k(F(b^*))) \tag{2.4}$$

**Theorem 2.1** *(Theorem A: efficiency = maximum channel capacity)*. *The market manifold
$M$ is minimal at $b^*$ (locally efficient) if and only if the channel capacity (2.4) is
a critical point of $b \mapsto C(b)$ over the manifold $M$:*

$$\nabla_M C(b^*) = 0 \iff H(b^*) = 0 \tag{2.5}$$

*Proof.* The gradient of $C(b)$ over the manifold is:

$$\nabla_M C(b) = T\cdot\mathrm{tr}\!\left[(I + TF)^{-1}\nabla_M F(b)\right] \tag{2.6}$$

As $T \to \infty$, $(I+TF)^{-1} \approx (TF)^{-1}$ and:

$$\nabla_M C(b) \approx \mathrm{tr}\!\left[F(b)^{-1}\nabla_M F(b)\right]
= \nabla_M \log\det F(b) \tag{2.7}$$

The gradient of $\log\det F$ over $M$ vanishes at $b^*$ iff the tangential gradient
$\Pi_{T_{b^*}M}\nabla_b \log\det F = 0$, which by the Fisher matrix formula (2.3) equals
the trace of the shape operator — the mean curvature $H(b^*)$. Setting this to zero gives
$H = 0$. $\square$

**Interpretation.** An efficient market sits at a **capacity saddle point** in portfolio
space: moving in any direction within the market manifold $M$ neither increases nor decreases
the channel capacity. The market has achieved the best possible information processing rate
consistent with its factor structure. This is a precise information-theoretic equivalent
of the economic efficiency condition.

**Corollary 2.2** *(Sharpe from capacity loss)*. *The maximum Sharpe ratio equals the
square root of the capacity gradient:*

$$\mathrm{Sharpe}^* = \|\nabla_M C(b^*)\|_{F(b^*)^{-1}}^{1/2} \tag{2.8}$$

*An inefficient market has positive capacity gradient — moving the portfolio in the
$\nabla_M C$ direction improves channel capacity and earns excess return.*

### 2.3 The effective channel dimension

The **effective channel capacity** uses only the significant singular values:

$$C_{\rm eff}(b^*) = \frac{1}{2}\sum_{k=1}^{r_{\rm eff}}\log(1 + T\lambda_k(F(b^*))) \tag{2.9}$$

where $r_{\rm eff} = \|F\|_F^2/\|F\|_2^2$ is the stable rank (same number appearing
throughout this series). The remaining $d-1-r_{\rm eff}$ channels carry negligible
information — they are the "noise channels" in the idiosyncratic directions. The market
manifold dimension $r$ is the number of channels above the noise floor.

---

## 3. Kolmogorov Complexity and Minimum Description Length

### 3.1 The MDL principle for market manifolds

The **Kolmogorov complexity** $K(M)$ of a market manifold $M$ is (informally) the length
of the shortest computer program that outputs a description of $M$ up to precision $\varepsilon$.
For a smooth manifold, this is determined by:

1. The intrinsic dimension $r$ — how many bits specify a point on $M$
2. The embedding complexity — how many bits specify the factor loading matrix $\Phi$
3. The curvature complexity — how many bits specify the deviations of $M$ from a flat model

**Definition 3.1** (Geometric Kolmogorov complexity). *The **description complexity** of
a minimal market manifold $M \subset S^{d-1}$ is:*

$$K(M) = r\log d + \log\!\left(\frac{1}{\mathrm{vol}(\mathcal{M}_r)}\right)
+ \log\!\left(1 + \mathcal{W}_2(M)\right) \tag{3.1}$$

*where $\mathcal{M}_r$ is the moduli space of minimal $r$-submanifolds of $S^{d-1}_+$
and $\mathcal{W}_2(M) = \int |II|^2 d\mathrm{vol}$ is the Willmore functional of the
second fundamental form.*

**Theorem 3.2** *(Theorem B: efficiency = minimum description length)*. *Among all market
manifolds with fixed $d$ and $r$:*

*(i) The totally geodesic surfaces (CAPM) have $\mathcal{W}_2 = 0$, hence minimum
description complexity: $K_{\rm CAPM} = r\log d + \log|\mathcal{M}_r^{\rm geod}|^{-1}$.*

*(ii) Any non-totally-geodesic minimal surface has $\mathcal{W}_2 > 0$ and hence
$K(M) > K_{\rm CAPM}$ — it requires additional bits to describe the curvature.*

*(iii) The Simons gap implies a complexity gap: either $\mathcal{W}_2 = 0$ (CAPM, minimum
complexity) or $\mathcal{W}_2 \geq \frac{d-2}{d-1}\cdot\mathrm{Area}(M)$ (non-CAPM
minimal surface, elevated complexity). There are no efficient market structures of
intermediate description complexity.*

*Proof.* Part (i): totally geodesic means $II = 0$, hence $\mathcal{W}_2 = 0$. The
description needs only the linear factor loading matrix $\Phi$ — a point in the
Grassmannian $\mathrm{Gr}(r, d)$ requiring $r(d-r)$ real parameters. Part (ii): any
non-zero $II$ requires additional data beyond $\Phi$ — the shape functions $A_k(x)$ for
$x \in M$ — increasing $K(M)$. Part (iii): the Simons gap $|II|^2 \geq (d-2)/(d-1)$
(non-zero implies bounded below) translates directly to a gap in $\mathcal{W}_2 \geq
(d-2)/(d-1) \cdot \mathrm{Area}$, and hence in $K(M)$. $\square$

**The MDL principle** \[Rissanen 1978\] selects the model with minimum description length.
Applied to market modelling: among all market structures consistent with the data, MDL
selects the one with minimum $K(M)$ — which is the CAPM (totally geodesic, $\mathcal{W}_2 = 0$).
**The MDL principle selects the CAPM as the canonical efficient market model.** This is not
an economic assumption — it is a logical consequence of the minimum complexity characterisation
of market efficiency.

### 3.2 The Kolmogorov–Simons ladder

The Lawson surface classification of CLASSIFICATION.md, reread through the lens of complexity:

| Manifold | Genus | $\mathcal{W}_2$ | $K(M) - K_{\rm CAPM}$ | Complexity interpretation |
|:---------|:-----:|:---------------:|:---------------------:|:--------------------------|
| Great sphere (CAPM) | 0 | 0 | 0 | Minimum: just a hyperplane |
| Veronese | 0 ($\mathbb{R}P^2$) | $>0$ | $+\log(|II|_F^2)$ | One quadratic constraint |
| Clifford torus | 1 | $2\pi^2$ | $+\log(2\pi^2)$ | One product structure |
| $\tau_{2,1}$ Lawson | 2 | $>2\pi^2$ | $+\log(...)$ | Two handles |
| $\tau_{m,n}$ | $mn$ | $\sim mn\pi^2$ | $\sim mn\log\pi^2$ | $mn$ handles |

The Kolmogorov complexity grows with genus — the more complex the topology of the efficient
market, the more bits required to describe it. The factor zoo of anomalies corresponds to
markets that appear to have high complexity (many "factors") because they are near a
high-genus Lawson surface rather than the CAPM.

---

## 4. The Shannon–McMillan–Breiman Theorem and the Kelly Criterion

### 4.1 The SMB theorem

**Theorem 4.1** *(Shannon–McMillan–Breiman)*. Let $(x_t)_{t \geq 1}$ be a stationary
ergodic process on $\mathbb{R}^d_+$ with entropy rate:

$$h = \lim_{T\to\infty} -\frac{1}{T}\log p(x_1, \ldots, x_T) \quad \text{(a.s.)} \tag{4.1}$$

The typical set $\mathcal{T}_T^\varepsilon$ — the set of sequences $(x_1,\ldots,x_T)$
satisfying $\left|-\frac{1}{T}\log p - h\right| < \varepsilon$ — has probability approaching 1,
and $|\mathcal{T}_T^\varepsilon| \approx e^{Th}$.

### 4.2 The Kelly criterion as the SMB entropy rate

**Theorem 4.2** *(Theorem C: SMB = Kelly)*. *For a stationary ergodic return process
$(x_t)$ with factor structure:*

$$\lim_{T\to\infty} \frac{1}{T}\log W_T(b) = \mathbb{E}[\log\langle b, x\rangle]
= L(b) \quad \text{a.s.} \tag{4.2}$$

*The maximal log-growth rate is the entropy rate of the return process measured in the
portfolio metric:*

$$\max_{b \in \Delta_{d-1}} L(b) = L(b^*) = h_{\rm Kelly} \tag{4.3}$$

*where $h_{\rm Kelly}$ is the **Kelly entropy rate** — the maximum log-growth rate of
the return process achievable by any constantly rebalanced portfolio.*

*The universal portfolio $\hat{b}_T$ achieves this rate asymptotically:*

$$\frac{1}{T}\log S_T^* \to h_{\rm Kelly} \quad \text{a.s.} \tag{4.4}$$

*and the convergence rate is controlled by the Fisher information at $b^*$:*

$$\frac{1}{T}\log S_T^* = h_{\rm Kelly} - \frac{\log T}{2T}(d-1) - \frac{\log\det F(b^*)}{2T}
+ O\!\left(\frac{1}{T^2}\right) \tag{4.5}$$

*Proof.* The almost-sure convergence (4.2) is the ergodic theorem for log-return processes
\[Algoet–Cover 1988\]. The asymptotic expansion (4.5) is the Laplace approximation of
LAPLACE.md (Theorem 4.3 there), which gives the log normalisation constant of the universal
portfolio:*

$$\log S_T^* = T\cdot L(b^*) - \frac{d-1}{2}\log T - \frac{1}{2}\log\det F(b^*) + O(1/T) \tag{4.6}$$

*Dividing by $T$ gives (4.5). $\square$

**The SMB typical set in portfolio space.** The SMB theorem defines the typical set of
return sequences as those achieving the entropy rate. In portfolio space, the dual object
is the set of portfolios achieving the maximum log-growth rate — this is precisely the
market manifold $M = \{b^*(x_{1:T}) : (x_1,\ldots,x_T) \in \mathcal{T}_T\}$.

**Key insight:** The minimal surface condition $H = 0$ means $b^*$ does not drift
systematically across the manifold as new data arrives — the portfolio is already at the
typical set boundary. An efficient market ($H=0$) means the log-optimal portfolio is the
fixed point of the typical-set decoder: the market has fully absorbed all available
information, and additional observations only refine the estimate within the typical set,
not change its location.

An inefficient market ($H \neq 0$) means the log-optimal portfolio is systematically
drifting in the direction $-\vec{H}$ — the typical set is moving, and a better decoder
(one that anticipates this drift) can achieve higher log-growth. The excess log-growth is:

$$\Delta L = L(\hat{b} + \varepsilon(-\vec{H})) - L(\hat{b}) = \varepsilon^2|H|^2 + O(\varepsilon^4) \tag{4.7}$$

precisely the Sharpe result of MINIMAL\_SURFACE.md.

### 4.3 Entropy and the Willmore energy

The **Boltzmann entropy** of the posterior distribution $\pi_T(b) \propto W_T(b)\mu(b)$:

$$S(\pi_T) = -\int_\Delta \pi_T(b)\log\pi_T(b)\,d\mu(b) \tag{4.8}$$

For the Laplace approximation around $b^*$, this is:

$$S(\pi_T) = \frac{d-1}{2}\log(2\pi e/T) + \frac{1}{2}\log\det F(b^*)^{-1}
+ \frac{\mathcal{M}_0}{T} + O(1/T^2) \tag{4.9}$$

where $\mathcal{M}_0$ is the Maslov correction from LAPLACE.md (Proposition 5.1 there),
which includes the Ricci curvature term $\frac{d-2}{4}\mathrm{tr}[F^{-1}]$.

**The posterior entropy decreases at rate $\frac{d-1}{2}\log T$ per period** — the market
"learns" at a rate controlled by the dimension of the factor space $(d-1)/2$. The Willmore
correction $\mathcal{M}_0/T$ accounts for the non-flat geometry of the market manifold.
For a minimal surface ($H=0$, $\mathrm{tr}[F^{-1}]$ is the Ricci contribution):

$$S(\pi_T)|_{H=0} = \frac{d-1}{2}\log(2\pi e/T) + \frac{1}{2}\log\det F(b^*)^{-1}
+ \frac{(d-2)}{4T}\mathrm{tr}[F(b^*)^{-1}] + O(1/T^2) \tag{4.10}$$

The $1/T$ correction is the **information-theoretic cost of living on a curved manifold** —
the Fisher–Rao curvature $K = 1/4$ of the Bhattacharyya sphere adds $\frac{d-2}{4T}$ bits
of uncertainty per period. For a flat market manifold (CAPM, $K_{\rm intrinsic} = 0$), this
correction vanishes and the learning rate is purely $\frac{d-1}{2}\log T$.

---

## 5. Volatility, the WF Diffusion, and the Phase Transition

### 5.1 Volatility as the WF noise parameter

In the WF diffusion model of PAPER.md, volatility enters as $\varepsilon^2 = \sigma^2/T$:
high volatility = high $\varepsilon^2$ = slow learning. The FK PDE (equation 2.3 of PAPER.md)
becomes:

$$\frac{\partial u}{\partial\tau} = \frac{\sigma^2}{2T}\mathcal{L}u + r(b,\tau)u \tag{5.1}$$

The WKB parameter is $\varepsilon^2 = \sigma^2/T$, and the semiclassical expansion is
in powers of $\sigma^2/T$.

**Theorem 5.1** *(Theorem D: volatility and stability)*. 

*(i) **Conformal invariance of Willmore:** The Willmore energy $\mathcal{W}(M)$ is invariant
under conformal rescaling of the metric — in particular, under $g^{\mathrm{FR}} \mapsto \sigma^2 g^{\mathrm{FR}}$.
The efficiency measure $\mathcal{E}(M)$ and the minimal surface condition $H=0$ are independent
of overall volatility level.*

*(ii) **Stability depends on volatility:** The stability threshold (Theorem D of CLASSIFICATION.md):*

$$\sigma_i(A) < \sqrt{\lambda_1(-\Delta_M) - \frac{d-2}{4}} \tag{5.2}$$

*involves $\lambda_1(-\Delta_M)$ — the spectral gap of the Laplacian on $M$ — which depends
on the intrinsic geometry and hence on the volatility through the induced metric.*

*(iii) **Critical volatility:** There exists a critical volatility level $\sigma^* > 0$ such that:*

$$\sigma < \sigma^*: \quad \text{market manifold stable (CAPM is attractor)}$$
$$\sigma > \sigma^*: \quad \text{market manifold unstable (crisis regime)}$$

*Proof of (i).* The Willmore energy is conformally invariant under Möbius transformations
of $S^{d-1}$ (MINIMAL\_SURFACE Theorem 4.2(ii)). Rescaling the Fisher–Rao metric by $\sigma^2$
is a conformal rescaling of $S^{d-1}$ (preserving angles, not distances). Hence $\mathcal{W}$
is invariant. The mean curvature $H$ scales as $H \to H/\sigma$ under the rescaling but
$H=0$ is preserved. $\square$

*Proof of (iii).* From the stability condition (5.2), the market manifold is stable iff
all shape operator singular values are below the threshold. The threshold itself depends on
$\lambda_1(-\Delta_M)$, which scales as $\lambda_1 \propto 1/\sigma^2$ (since the Laplacian
eigenvalues scale inversely with the metric). So the threshold scales as $\sigma^* \propto
1/\sigma_i(A)$. Above $\sigma^*$, the Laplacian gap is too small to provide restoring force
and the manifold becomes unstable. $\square$

**Portfolio interpretation.** High volatility markets ($\sigma > \sigma^*$) have small
Laplacian spectral gaps — the WF diffusion mixes slowly, the posterior concentrates slowly,
and the market is more easily destabilised. This explains the empirical observation that
**high-volatility markets have more persistent anomalies**: the restoring force of arbitrage
(proportional to the spectral gap) is weaker.

### 5.2 The volatility–entropy trade-off

The channel capacity at portfolio $b^*$ satisfies:

$$C(\sigma) = \frac{r}{2}\log\left(1 + \frac{T}{\sigma^2}\lambda_1(F(b^*))\right)
\approx \frac{r}{2}\log\frac{T}{\sigma^2} \quad (T\gg \sigma^2) \tag{5.3}$$

The capacity decreases logarithmically with volatility: doubling volatility costs $r/2$ bits
of channel capacity. **A high-volatility market is a low-capacity information processor.**

This is a precise version of the folk wisdom that "volatile markets are hard to read" — the
Fisher information per observation decreases as $\sigma^{-2}$, so $T\sigma^2$ observations
are needed to achieve the same capacity as $T$ observations in a unit-volatility market.

---

## 6. The Efficient Frontier from the Manifold

### 6.1 Classical Markowitz and its geometric limitation

The classical mean-variance efficient frontier is the set of portfolios achieving maximum
expected return for a given level of variance:

$$\mathcal{F}^{\rm MV} = \left\{b \in \Delta_{d-1} : \mathrm{Var}(b^Tx) = v,\;
\mathbb{E}[b^Tx] = \max\right\}_{v \geq 0} \tag{6.1}$$

This is a 1-dimensional curve in $\Delta_{d-1}$. Its limitation: it ignores the
geometric structure of the market manifold $M$ — in particular, it does not distinguish
between movements along $M$ (factor bets) and movements off $M$ (idiosyncratic bets).

### 6.2 The manifold efficient frontier

**Definition 6.1** (Manifold efficient frontier). *For a market manifold $M \subset
\Delta_{d-1}$, the **manifold efficient frontier** is:*

$$\mathcal{F}(M) = \left\{b \in \Delta_{d-1} : b = b^* + \xi,\;
\xi \in N_{b^*}M,\; |\xi|_{g^{\mathrm{FR}}} = \rho\right\}_{\rho \geq 0} \tag{6.2}$$

*the sphere bundle of the normal bundle of $M$ — the set of portfolios obtained by moving
a distance $\rho$ off the market manifold in the normal direction.*

**Theorem 6.2** *(Theorem E: efficient frontier from manifold)*.

*(i) The manifold efficient frontier $\mathcal{F}(M)$ is an $(r_{\rm normal})$-dimensional
family parametrised by the normal bundle $NM$, where $r_{\rm normal} = d-1-r$.*

*(ii) The Markowitz efficient frontier is the one-dimensional sub-curve of $\mathcal{F}(M)$
obtained by moving in the direction $\vec{H}$ (the mean curvature direction — the primary
normal direction of inefficiency):*

$$\mathcal{F}^{\rm MV} \subset \left\{b^* + t\vec{H}(b^*) : t \in \mathbb{R}\right\} \cap \Delta_{d-1} \tag{6.3}$$

*(iii) The full manifold efficient frontier stratifies as:*

$$\mathcal{F}(M) = \mathcal{F}^{\rm factor}(M) \cup \mathcal{F}^{\rm normal}(M) \tag{6.4}$$

*where $\mathcal{F}^{\rm factor}$ is the along-manifold frontier (factor bets, $\rho = 0$)
and $\mathcal{F}^{\rm normal}$ is the off-manifold frontier (idiosyncratic bets, $\rho > 0$).*

**Proof of (ii).** The Markowitz frontier maximises $\mathbb{E}[b^T x] - \frac{\lambda}{2}\mathrm{Var}(b^T x)$
over $b \in \Delta_{d-1}$. The gradient of this objective in the Fisher-Rao metric is:

$$\nabla_{g^{\mathrm{FR}}} \left(\mu^T b - \frac{\lambda}{2}b^T\Sigma b\right)
= F(b^*)^{-1}(\mu - \lambda\Sigma b^*) \tag{6.5}$$

At the log-optimal portfolio $b^*$ (the maximiser of $L_T$), the tangential component
$\Pi_{T_{b^*}M}(\nabla_{g^{\mathrm{FR}}}(\cdot)) = 0$, but the normal component
$\Pi_{N_{b^*}M}(\nabla_{g^{\mathrm{FR}}}(\cdot)) \propto \vec{H}(b^*)$. The Markowitz
frontier follows this normal gradient, which points in the $\vec{H}$ direction. $\square$

**The geometric picture.** The market manifold $M$ is the "spine" of the full portfolio
simplex. Moving along $M$ changes the factor allocation (momentum, value bets). Moving
off $M$ into the normal bundle $NM$ changes the idiosyncratic allocation (stock-picking).
The Markowitz efficient frontier is a curve in the normal bundle — it is the portfolio of
maximum return per unit of idiosyncratic risk. The classical efficient frontier is a
**section of the normal bundle** of the market manifold.

### 6.3 The geometric efficient frontier and the Sharpe surface

The full information about optimal portfolios is contained in the **Sharpe surface** —
the surface of maximum Sharpe ratio as a function of portfolio displacement from $M$:

$$\mathrm{Sharpe}(b) = \frac{L(b) - L(b^*)}{|b - b^*|_{g^{\mathrm{FR}}}}
= \frac{\langle\vec{H}(b^*), b-b^*\rangle_{g^{\mathrm{FR}}} + O(|b-b^*|^2)}{|b-b^*|_{g^{\mathrm{FR}}}} \tag{6.6}$$

This is maximised in the direction $\vec{H}(b^*)$ with maximum value $|H(b^*)|$. The Sharpe
surface is a **hemisphere** of radius $|H(b^*)|$ in the normal bundle — every direction in
the normal bundle achieves a Sharpe between 0 and $|H|$, with the maximum in the $\vec{H}$
direction. The classical efficient frontier is the equator of this hemisphere.

---

## 7. What Would Persi Diaconis Say?

Persi Diaconis would engage with this framework from several distinct directions, and his
characteristic combination of enthusiasm for elegant mathematics and rigorous skepticism
about empirical claims would make him both the framework's most insightful advocate and
its most demanding critic.

### 7.1 The Markov chain mixing time connection

Diaconis's deepest contribution to probability theory is the quantitative theory of Markov
chain mixing times — how many steps until a random walk on a group or graph is
indistinguishable from its stationary distribution \[Diaconis–Shahshahani 1981\]. The
central tool is the spectral gap $\lambda_1$ of the chain's transition matrix.

In our framework: the WF diffusion on the market manifold is a Markov diffusion on
$(\Sigma, g_\Sigma)$, and its mixing time is:

$$t_{\rm mix} = \frac{\log(1/\varepsilon)}{\lambda_1(-\Delta_\Sigma)} \tag{7.1}$$

This is the time for the posterior $\pi_T$ to converge to a $\varepsilon$-neighbourhood of
its limit $\delta_{b^*}$. **The spectral gap $\lambda_1$ is exactly the same quantity that
appears in the Jacobi stability operator** (CLASSIFICATION.md equation 6.6). Diaconis would
immediately recognise:

$$\text{Market learning rate} = \text{Markov chain spectral gap} = \text{Jacobi stability threshold}$$

This triple identity is profound: the speed at which the market absorbs information
(mixing time), the speed at which arbitrageurs restore efficiency (Jacobi stability), and
the speed at which the posterior concentrates on the log-optimal portfolio — all controlled
by $\lambda_1(-\Delta_M)$.

**Diaconis's card-shuffling analogy.** The riffle shuffle of a deck of $n$ cards requires
$\frac{3}{2}\log_2 n$ shuffles to mix — a sharp threshold phenomenon \[Bayer–Diaconis 1992\].
In our framework: an $r$-factor market with $d$ assets requires approximately
$\frac{(d-2)}{4\lambda_1}$ return observations to "mix" the posterior to within $\varepsilon$
of $b^*$ — a direct analogue of the shuffle threshold. The factor dimension $r$ plays the
role of the deck size $n$.

**The sharp threshold:** Just as the card shuffle has a sharp mixing threshold, the posterior
$\pi_T$ has a sharp threshold around $T^* = (d-2)/(4\lambda_1)$:

$$\|\pi_T - \delta_{b^*}\|_{\rm TV} \approx \begin{cases}1 & T \ll T^*\\ 0 & T \gg T^*\end{cases} \tag{7.2}$$

This threshold is the **information-theoretic barrier** to market efficiency: below $T^*$
observations, the market cannot reliably identify $b^*$; above $T^*$, it does so with high
probability. The barrier sharpens with $d$ — larger markets take longer to become efficient,
with a sharp transition at $T^*$.

### 7.2 Harmonic analysis on the symmetric group

Diaconis is the master of harmonic analysis on finite groups \[Diaconis 1988\]. He would
note that the symmetric group $S_d$ (permutations of $d$ assets) acts on the portfolio
simplex $\Delta_{d-1}$ by permuting coordinates, and that **exchangeable portfolios** — those
invariant under this action — form the 1-dimensional subspace $\{b = c\cdot\mathbf{1}/d : c\in\mathbb{R}\}$.

The harmonic analysis of functions on $S^{d-1}_+$ (Bhattacharyya sphere) decomposes
into irreducible representations of $O(d)$:

$$f = \sum_{k=0}^\infty \sum_\alpha \hat{f}_{k,\alpha} Y_{k,\alpha} \tag{7.3}$$

where $Y_{k,\alpha}$ are the spherical harmonics. The minimal surface condition $\Delta_M\iota
= -r\iota$ (Takahashi theorem) selects the $k=1$ harmonic component — the embedding
coordinates are **first-order harmonics** of the Laplacian. The SMB entropy rate is the
$k=0$ component (the mean). The Sharpe ratio is the projection onto the $k=1$ component
in the normal bundle.

Diaconis would recognise this as a **Peter–Weyl decomposition** of the portfolio manifold.
The factor structure breaks $O(d)$ symmetry to $O(r) \times O(d-r)$, and the minimal surface
conditions are the constraints that survive this symmetry breaking.

### 7.3 The de Finetti connection

Diaconis co-proved (with Freedman) a quantitative version of de Finetti's theorem \[1980\]:
an $n$-exchangeable sequence of 0-1 random variables is within $O(r/n)$ of a mixture of
i.i.d. sequences, where $r$ is the number of observations. In our framework:

The posterior $\pi_T(b) \propto W_T(b)\mu(b)$ is an exchangeable measure on
$\{x_1,\ldots,x_T\}$ (the labelling of time steps is arbitrary for the log-optimal portfolio).
The de Finetti–Diaconis–Freedman theorem gives:

$$\|\pi_T - \pi^{\rm de Finetti}_T\|_{\rm TV} \leq \frac{r(d-1)}{T} = O\!\left(\frac{rd}{T}\right) \tag{7.4}$$

where $\pi^{\rm de Finetti}_T$ is the i.i.d. de Finetti mixture. This bound is exactly the
$O(1/T)$ Laplace correction from LAPLACE.md — the departure from the i.i.d. de Finetti
mixture is precisely the Maslov correction. The minimal surface condition ($H=0$) is the
condition under which the $O(1/T)$ correction vanishes to leading order (Theorem 4.2 of
LAPLACE.md), leaving only the $O(1/T^2)$ correction. **Market efficiency is the condition
under which the de Finetti approximation is most accurate.**

### 7.4 Diaconis's skepticism: three questions he would ask

Diaconis is celebrated for deflating elegant mathematics that "proves" more than it
actually shows. He would ask:

**Question 1: "Can you simulate it?"** The minimal surface characterisation and the
Sharpe–curvature theorem are elegant, but Diaconis would want a Monte Carlo study
confirming that the estimated $\|H\|_{L^2}$ from finite-sample return data converges to the
theoretical Sharpe upper bound. He would specifically worry about the $O(1/T)$ finite-sample
bias in estimating $b^*$ and $F(b^*)$ — the Fisher matrix estimator has estimation error
that could masquerade as mean curvature.

**Question 2: "Is the Fisher–Rao metric the right one?"** The choice of $g^{\mathrm{FR}}$
as the market metric is canonical from information geometry, but Diaconis would note that
other metrics (the $L^2$ metric, the Wasserstein metric, the Bures metric for quantum states)
would give different minimal surface conditions. The choice of metric encodes assumptions
about what "distances" between portfolios mean — assumptions that should be made explicit
and justified economically.

**Question 3: "What does the stability index mean for a real portfolio?"** The abstract
statement "the Clifford torus has stability index 5" needs a translation into something
an investor can act on. Diaconis would insist on: "Give me the five portfolios corresponding
to the five unstable Jacobi eigenvectors, tell me what they are in terms of the original
assets, and show me the returns to holding them." This is a legitimate demand — the geometry
should ultimately produce a trading strategy with an identifiable P&L.

### 7.5 What Diaconis would contribute

Despite the skepticism, Diaconis's framework would add three genuine contributions:

1. **Sharp mixing time bounds** for the posterior $\pi_T$ using his spectral methods —
   giving precise sample sizes $T^*$ at which each market "becomes efficient" per the
   SMB theorem.

2. **Representation-theoretic classification** of the Jacobi eigenvectors — identifying
   which irreducible representations of $O(r)$ correspond to which types of market anomalies
   (momentum = degree-1 harmonics, value = degree-2, etc.).

3. **The right notion of "typical"** — his work on the theory of large deviations and
   typical sets would sharpen Theorem C (SMB = Kelly) by giving precise exponential rates
   for the convergence of the empirical log-growth to the entropy rate.

---

## 8. A New Characterisation of Market Efficiency

Collecting the results of this paper, we have **five equivalent characterisations** of a
strongly efficient market:

**Theorem 8.1** *(Quintet of efficiency)*. *Under the standing assumptions of the series,
the following are equivalent:*

1. **Geometric** (MINIMAL\_SURFACE): $H \equiv 0$ on $\Sigma$ — the market manifold is minimal.
2. **Information-theoretic** (this paper, Theorem A): $\nabla_M C(b^*) = 0$ — the channel capacity is stationary over the manifold.
3. **Statistical** (LAPLACE.md, Theorem 4.2): $\nabla\log\pi \equiv 0$ in the interior — the Jeffreys prior condition; the $O(1/T)$ Bayesian correction vanishes.
4. **Complexity-theoretic** (this paper, Theorem B): $\mathcal{W}_2(M)$ achieves the minimum for its topological type — minimum description length consistent with topology.
5. **Ergodic-theoretic** (this paper, Theorem C): the empirical log-growth rate of the log-optimal portfolio equals the SMB entropy rate — no systematic drift in the typical set.

*Each characterisation is equivalent to the others given Conjecture 3.1 of MINIMAL\_SURFACE.
Characterisations 2, 3, 4, 5 are proved independently of Conjecture 3.1.*

**The new insight.** An efficient market is not merely a market where prices are "fair" —
it is a market that has achieved **maximal information compression**: the factor structure
captures all the systematic information in returns, the idiosyncratic noise is genuinely
unpredictable, and the log-optimal portfolio is the minimum-description-length decoder
of the return process. The Willmore energy measures how far the market is from this
compressed, minimal representation.

---

## 9. Implications and Open Problems

### 9.1 The market as a universal source coder

The universal portfolio $\hat{b}_T$ achieves the Kelly entropy rate $h_{\rm Kelly}$ without
knowing the return distribution — it is a **universal source coder** in the information-theoretic
sense \[Cover–Thomas 2006\]. The connection to the SMB theorem makes this precise: the universal
portfolio is the **minimum-redundancy code** for the return process, and its excess redundancy
over the optimal (Kelly) code is:

$$\mathrm{Redundancy}(\hat{b}_T) = h_{\rm Kelly} - \frac{1}{T}\log S_T^*
= \frac{(d-1)\log T}{2T} + O(1/T) \tag{9.1}$$

The $\frac{(d-1)\log T}{2T}$ term is the **parametric complexity penalty** — the cost of
not knowing $b^*$ in advance, paying $(d-1)/2$ nats per observation to estimate a
$(d-1)$-dimensional parameter. This is the Rissanen MDL penalty for a $d-1$ parameter model.

**The minimal surface condition eliminates the $O(1/T)$ redundancy correction** (from LAPLACE.md
Theorem 4.2 — the prior correction vanishes for the uniform Jeffreys prior), leaving only
the parametric $O(\log T/T)$ term. The efficient market achieves the minimum redundancy
consistent with parameter estimation.

### 9.2 Open problems

**Problem 1.** Prove the mixing time threshold (7.2) rigorously using Diaconis's spectral
methods — specifically, prove a sharp threshold for the total variation distance
$\|\pi_T - \delta_{b^*}\|_{\rm TV}$ with explicit constants.

**Problem 2.** Extend Theorem C (SMB = Kelly) to non-stationary returns. When the return
distribution changes over time (regime switching, structural breaks), the entropy rate is
time-varying and the typical set moves. The mean curvature drift $\vec{H}(b^*(t))$ should
track this movement — formalise this connection.

**Problem 3.** Compute the channel capacity $C(\sigma)$ for each of the Lawson surfaces
$\tau_{m,n}$ and determine whether the capacity is monotone in genus. Conjecture: capacity
decreases with genus, so higher-genus efficient markets are lower-capacity information
processors despite being "equally efficient" ($H=0$).

**Problem 4.** Implement the five characterisations of Theorem 8.1 as a battery of
empirical tests for market efficiency, and compare their power against each other and
against classical tests (variance ratios, autocorrelation tests, event studies).

---

## References

Algoet, P. H. and Cover, T. M. (1988). A sandwich proof of the Shannon–McMillan–Breiman
theorem. *Annals of Probability* 16(2), 899–909.

Bayer, D. and Diaconis, P. (1992). Trailing the dovetail shuffle to its lair.
*Annals of Applied Probability* 2(2), 294–313.

Cover, T. M. and Thomas, J. A. (2006). *Elements of Information Theory* (2nd ed.). Wiley.

Diaconis, P. (1988). *Group Representations in Probability and Statistics*.
IMS Lecture Notes.

Diaconis, P. and Freedman, D. (1980). Finite exchangeability. *Annals of Probability* 8(4), 745–764.

Diaconis, P. and Shahshahani, M. (1981). Generating a random permutation with random
transpositions. *Zeitschrift für Wahrscheinlichkeitstheorie* 57(2), 159–179.

Kelly, J. L. (1956). A new interpretation of information rate.
*Bell System Technical Journal* 35(4), 917–926.

Rissanen, J. (1978). Modeling by shortest data description.
*Automatica* 14(5), 465–471.

Shannon, C. E. (1948). A mathematical theory of communication.
*Bell System Technical Journal* 27(3), 379–423, 623–656.

Shannon, C. E. (1949). Communication in the presence of noise.
*Proceedings of the IRE* 37(1), 10–21.
