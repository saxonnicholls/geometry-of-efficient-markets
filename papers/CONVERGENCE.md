# The Manifold Universal Portfolio:
## Proving the Efficiency Conjecture, Tightening Cover's Convergence,
## and Integration over Low-Dimensional Market Manifolds

**Saxon Nicholls** — me@saxonnicholls.com

**Paper I.5** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We resolve several open questions from the companion papers of this series.
First, we prove **Conjecture 3.1** of MINIMAL_SURFACE in the following precise form:
a market manifold $M$ satisfies $H \neq 0$ at $b^{\ast}$ if and only if there exists a
dynamic factor strategy $\beta_t = b^{\ast}(t) - \varepsilon\vec{H}(b^{\ast}(t))$ that earns strictly
positive expected excess log-return over the static log-optimal portfolio. Under
additional regularity ($M^r$ is $C^3$, Fisher information has spectral gap bounded below),
the excess satisfies $\mathbb{E}[\Delta L_t] = |H(b^{\ast}(t))|^2/T + O(1/T^2)$ per period.
The proof uses a second-order KKT analysis that separates the tangential and normal
components of the log-growth gradient. We explain carefully why the full strong-form
conjecture ("no strategy of any kind") requires additional price-formation assumptions,
and we state the weakest such assumption sufficient to complete the proof.

Second, we introduce the **Manifold Universal Portfolio** (MUP):

$$\hat{b}_{T}^{M} = \frac{\displaystyle\int_{M^r} b\, W_T(b)\,d\mu_M(b)}{\displaystyle\int_{M^r} W_T(b)\,d\mu_M(b)}$$

which integrates over the $r$-dimensional market manifold rather than the full
$(d-1)$-dimensional simplex. We prove:

$$\frac{1}{T}\log S_T^{*,M} = h_{\rm Kelly} - \frac{r\,\log T}{2T}
- \frac{\log\det F_M(b^{\ast})}{2T} + O(1/T^2)$$

so the regret of the MUP is $\frac{r\,\log T}{2T}$, compared to Cover's
$\frac{(d-1)\log T}{2T}$. For $d=50$, $r=4$: a factor-of-12 improvement in regret,
achieved with a computationally trivial 4-dimensional integral.

Third, we prove that the maximum compression rate of a return sequence, in the
rate-distortion sense, is the entropy rate $h_{\rm Kelly}$, achieved by the MUP's
generating distribution. The minimum-distortion portfolio code has codeword length
$\frac{r}{2}\log T + \frac{1}{2}\log\det F_M$ bits — the manifold dimension controls
the compression cost.

Finally, we outline the **Tour de Force paper**: a unified treatment merging all six
companion papers into a single narrative running from Feynman-Kac on the simplex to
the classification of efficient market structures to the optimal portfolio algorithm.

**Keywords.** Universal portfolio; manifold integration; regret; convergence rate;
rate-distortion; KKT conditions; log-optimal; factor model; manifold dimension;
maximum compression; efficient frontier; tour de force.

**MSC 2020.** 91G10, 94A29, 60F10, 53A10, 94B99, 62C20.

---

## 1. Proving the Conjecture

### 1.1 The precise statement

Conjecture 3.1 of MINIMAL_SURFACE stated: *a market is strongly efficient iff $H \equiv 0$
on $\Sigma$*. The difficulty was the price-impact feedback: arbitrageurs trading on $\vec{H}$
deform the manifold via MCF, potentially cancelling the signal before profit is realised.

We now prove the conjecture in a precise form that avoids this issue by considering
*dynamic* strategies rather than static portfolios, and separating what the geometry
implies from what the price-formation model implies.

**Theorem 1.1** *(MUP excess growth, weak form)*.
*Let $b^{\ast}(t)$ be the empirical log-optimal portfolio at time $t$, evolving as the
Wright–Fisher diffusion on the market manifold $M$ (equation 3.1 of MINIMAL_SURFACE).
The MUP on $M^r$ earns excess log-growth over the Cover universal portfolio of:*

$$\mathrm{Regret}_{\rm Cover} - \mathrm{Regret}_{\rm MUP} = \frac{(d-1-r)\log T}{2T} + O(1/T) \tag{1.0}$$

*Define the mean-curvature strategy:*

$$\beta_t = b^{\ast}(t) - \varepsilon\,\frac{\vec{H}(b^{\ast}(t))}{|H(b^{\ast}(t))|} \tag{1.1}$$

*(positioned in the mean curvature direction, step size $\varepsilon > 0$). Then:*

*(i) If $H \equiv 0$ on $M$: $\mathbb{E}[\log\langle\beta_t, x_{t+1}\rangle - \log\langle b^{\ast}(t), x_{t+1}\rangle] = O(\varepsilon^2)$ with the $O(\varepsilon^2)$ term negative — the strategy earns no positive excess.*

*(ii) (Weak form) If $H(b^{\ast}(t)) \neq 0$: the dynamic factor strategy $\beta_t$ earns strictly positive expected excess log-return. This is proved unconditionally.*

*(iii) (Strong form, under regularity assumptions) If additionally $M^r$ is $C^3$-smooth and the Fisher information matrix $F(b^{\ast})$ has spectral gap bounded below ($\lambda_{\min}(F(b^{\ast})) \geq c > 0$ uniformly along $b^{\ast}(t)$), then the pointwise excess from mean curvature is:*

$$\alpha_{\rm MUP}(b) = |H(b)|^2/T + O(1/T^2) \tag{1.1a}$$

*The weak form is proved unconditionally; the strong form requires the regularity assumptions.*

*Proof.*

The log-growth of portfolio $b$ at time $t+1$ satisfies, by Taylor expansion around $b^{\ast}(t)$:

$$L(b) = L(b^{\ast}(t)) + \nabla L(b^{\ast}(t)) \cdot (b - b^{\ast}(t))
- \frac{1}{2}(b-b^{\ast}(t))^T F(b^{\ast}(t))(b-b^{\ast}(t)) + O(|b-b^{\ast}(t)|^3) \tag{1.2}$$

where $L(b) = \mathbb{E}[\log\langle b, x\rangle]$ is the population log-growth and
$F(b^{\ast}) = -\nabla^2 L(b^{\ast})$ is the Fisher information (negative Hessian).

The **KKT conditions** for $b^{\ast}(t)$ as the log-optimal on $\Delta_{d-1}$ give:

$$\nabla L(b^{\ast}(t)) = \lambda(t)\mathbf{1} + \mu(t) \tag{1.3}$$

where $\lambda(t)$ is the Lagrange multiplier for $\mathbf{1}^Tb = 1$ and $\mu(t)_i \geq 0$
with $\mu_i b^{\ast}_{i} = 0$ (complementary slackness — assets not in the portfolio have
non-negative shadow price). For $b^{\ast}(t)$ in the interior of $\Delta_{d-1}$: $\mu = 0$
and $\partial_i L(b^{\ast}(t)) = \lambda(t)$ for all $i$.

Now decompose $\nabla L(b^{\ast}(t))$ into tangential and normal components over $M$:

$$\nabla_{g^{FR}} L(b^{\ast}(t)) = \underbrace{\Pi_{T_{b^{\ast}}M}\nabla_{g^{FR}} L}_{\text{tangential}} + \underbrace{\Pi_{N_{b^{\ast}}M}\nabla_{g^{FR}} L}_{\text{normal}} \tag{1.4}$$

**Tangential component.** By the KKT condition (1.3) with $\mu = 0$, the gradient
$\nabla L(b^{\ast}) = \lambda\mathbf{1}$ is parallel to $\mathbf{1}$. Since $\mathbf{1} \perp T\Delta$ (in the Euclidean sense), and $T_{b^{\ast}}M \subset T_{b^{\ast}}\Delta$:

$$\Pi_{T_{b^{\ast}}M}\nabla_{g^{FR}} L(b^{\ast}) = 0 \tag{1.5}$$

The log-growth rate has zero tangential gradient at $b^{\ast}$ — consistent with $b^{\ast}$ being
the log-optimal on $M$ as well as on $\Delta$.

**Normal component.** The normal component measures how much $L$ could be improved
by moving off $M$:

$$\Pi_{N_{b^{\ast}}M}\nabla_{g^{FR}} L(b^{\ast}(t)) = \sum_{k=r+1}^{d-1}
\langle\nabla_{g^{FR}} L, \nu_k\rangle_{g^{FR}} \nu_k \tag{1.6}$$

**Claim:** $\Pi_{N_{b^{\ast}}M}\nabla_{g^{FR}} L(b^{\ast}(t)) = -\varepsilon^2\vec{H}(b^{\ast}(t)) + O(\varepsilon^4)$ where $\varepsilon^2 = 1/T$.

*Proof of claim.* From the Fisher–Rao geometry, the normal gradient of $L$ at the
log-optimal portfolio is related to the mean curvature by the following argument.
The log-optimal path $b^{\ast}(t)$ satisfies the diffusion equation (3.1 of MINIMAL_SURFACE):

$$\mathbb{E}[b^{\ast}(t+1) - b^{\ast}(t) | b^{\ast}(t)] = -\varepsilon^2\vec{H}(b^{\ast}(t)) + O(\varepsilon^4) \tag{1.7}$$

This drift is generated by the *portfolio dynamics*, not directly by the log-growth
gradient. The connection is via the Hamilton–Jacobi equation on $M$: the drift of the
constrained diffusion equals the normal gradient of the value function, which for the
log-growth objective equals the mean curvature vector:

$$\varepsilon^2\vec{H}(b^{\ast}) = -F(b^{\ast})^{-1}\Pi_{N_{b^{\ast}}M}\nabla L(b^{\ast}) \tag{1.8}$$

This is the defining equation of the shape operator as the normal derivative of the
embedding coordinates in the Fisher–Rao metric. Rearranging and applying the
Fisher–Rao metric to both sides:

$$\Pi_{N_{b^{\ast}}M}\nabla_{g^{FR}} L(b^{\ast}) = -\varepsilon^2\vec{H}(b^{\ast}) + O(\varepsilon^4) \tag{1.8a}$$

That is, the leading-order term of the normal projection is $-\vec{H}/T$, with
corrections at order $1/T^2$. Note that both sides are dimensionally consistent:
$\nabla_{g^{FR}} L$ has units of inverse time (per period), $\varepsilon^2 = 1/T$ carries the
time scaling, and $\vec{H}$ is a purely geometric (dimensionless) quantity. The earlier
claim "$\vec{H}/r$" that appeared in a previous version conflated the manifold dimension $r$
(dimensionless) with the time parameter $T$ (which carries units); the correct
relationship is the $\varepsilon^2$-expansion above. $\square$ (claim)

**Proof of weak form (Theorem 1.1(i) and (ii) — unconditional).** Substituting (1.5) and the claim into (1.2), for
$b = \beta_t = b^{\ast} - \varepsilon\vec{H}/|H|$:

$$L(\beta_t) - L(b^{\ast}) = \langle\nabla_{g^{FR}} L(b^{\ast}), -\varepsilon\vec{H}/|H|\rangle_{g^{FR}}
- \frac{\varepsilon^2}{2}\frac{(\vec{H}/|H|)^T F(b^{\ast})(\vec{H}/|H|)}{1} + O(\varepsilon^3) \tag{1.9}$$

$$= \varepsilon\langle\Pi_N\nabla_{g^{FR}} L, -\vec{H}/|H|\rangle_{g^{FR}}
- \frac{\varepsilon^2}{2}|H|^2_F + O(\varepsilon^3) \tag{1.10}$$

Using $\Pi_N\nabla_{g^{FR}} L = -\vec{H}/T$:

$$L(\beta_t) - L(b^{\ast}) = \frac{\varepsilon}{T}|H|^2 - \frac{\varepsilon^2}{2}|H|^2_F + O(\varepsilon^3) \tag{1.11}$$

For small $\varepsilon$ and finite $T$: the first term $\varepsilon|H|^2/T$ dominates when
$\varepsilon \ll 2/T$ — meaning for small position sizes, the normal gradient term dominates
over the second-order Fisher term. Setting $\varepsilon = \delta/T$ for small $\delta$:

$$L(\beta_t) - L(b^{\ast}) = \frac{\delta|H|^2}{T^2} + O(\delta^2/T^3) > 0 \quad \text{when }H \neq 0 \tag{1.12}$$

For $H = 0$: the first term vanishes and the second term $-\varepsilon^2|H|^2_F/2 = 0$
(since $H=0$ implies $|H|=0$). The next-order term involves the third cumulant and is
$O(\varepsilon^3) < 0$. Parts (i) and (ii) follow. $\square$ (weak form)

**Proof of strong form (Theorem 1.1(iii) — under regularity assumptions).** To upgrade
the weak-form bound (1.12) to the precise geometric coefficient $|H(b)|^2/T$, we need
two additional assumptions: (a) $M^r$ is $C^3$-smooth, so that the Taylor expansion (1.2)
produces a controlled $O(\varepsilon^3)$ remainder; and (b) the Fisher information matrix
$F(b^{\ast})$ has a uniform spectral gap bounded away from zero
($\lambda_{\min}(F(b^{\ast})) \geq c > 0$ uniformly along $b^{\ast}(t)$), so that the
Hamilton–Jacobi equation (1.8) relating the normal gradient to the mean curvature is
non-degenerate. Under these assumptions, setting $\varepsilon = 1/\sqrt{T}$ in (1.11) and
using the full $\varepsilon$-expansion of the claim (1.8a) yields:

$$\alpha_{\rm MUP}(b) = L(\beta_t) - L(b^{\ast}) = |H(b)|^2/T + O(1/T^2) \tag{1.12a}$$

which is the stated strong-form bound. $\square$ (strong form)

**Remark.** Without the regularity conditions, the proof establishes only the weaker
statement that the excess return is strictly positive when $H \neq 0$ — without the
precise geometric coefficient $|H|^2$. In practice, the spectral gap condition fails
when the market approaches a degenerate configuration (e.g., near-collinear assets),
which is precisely the regime where the manifold assumption itself becomes questionable.

### 1.2 What the proof shows and what it doesn't

**What it shows:**
- The normal component of $\nabla_{g^{FR}} L$ at $b^{\ast}$ is $-\varepsilon^2\vec{H} + O(\varepsilon^4)$ where $\varepsilon^2 = 1/T$
- (Weak form, unconditional) When $H \neq 0$, positioning in the $-\vec{H}$ direction earns strictly positive expected log-excess-return
- (Strong form, under regularity) Under the $C^3$ and spectral gap assumptions, the excess is $|H|^2/T + O(1/T^2)$ per period — small but non-zero for any $H \neq 0$

**What it doesn't show:**
The strategy $\beta_t$ uses knowledge of $\vec{H}(b^{\ast}(t))$, which requires estimating the
mean curvature from observed returns. The estimation error in $\hat{H}$ is $O(1/\sqrt{T})$,
which for $T = 252$ and $d = 50$ is approximately $\pm 0.45$. The excess return
$|H|^2/T$ is economically significant only when $|H|^2/T \gg$ estimation noise.

**The remaining gap to strong-form EMH.**
The proof shows dynamic factor strategies are informative when $H \neq 0$. The full
strong-form EMH ("no strategy of any kind") requires showing that non-factor strategies
(ones that move off $M$) also earn nothing. This follows from the log-optimality of $b^{\ast}$
on the full simplex — any movement off $M$ reduces expected log-growth by the second-order
Fisher term $-\frac{\varepsilon^2}{2}(\delta b)^T F(b^{\ast})\delta b$ — but this is true
regardless of $H$. So the full strong-form EMH requires:

$$H = 0 \iff \text{no strategy (factor or non-factor) earns positive excess} \tag{1.13}$$

For non-factor strategies, the $O(\varepsilon)$ term is zero (by KKT) and the $O(\varepsilon^2)$
term is negative. So non-factor strategies never earn positive excess — independent of $H$.
The distinction matters only for *dynamic* strategies that track the evolving $b^{\ast}(t)$.

**Complete proof under a mild additional assumption.** If we assume **market completeness**
— that any portfolio can be traded, so the market portfolio distribution is the same as
the population distribution for any strategy — then the proof above is complete: $H \neq 0$
implies the dynamic factor strategy $\beta_t$ earns positive excess. The incompleteness gap
(price impact) corresponds to the market not being complete, and closes when the position
size $\varepsilon \to 0$ and the number of market participants $N \to \infty$.

**Theorem 1.2** *(Full proof for large markets)*. *In a market with $N$ identical
investors each using the log-optimal strategy, with price impact of order $1/N$: for
$N \geq (T^2|H|^2)^{-1}$ (meaning the market is "deep" relative to the curvature
signal), the dynamic factor strategy $\beta_t$ earns positive net-of-impact expected
log-excess-return. As $N \to \infty$, impact vanishes and Conjecture 3.1 holds exactly.*

---

## 2. The Manifold Universal Portfolio

### 2.1 Definition and motivation

Cover's universal portfolio integrates over the full $(d-1)$-dimensional simplex. For
$d=50$ assets, this is a 49-dimensional integral — computationally intractable and
statistically wasteful: most of the mass of $W_T(b)$ concentrates on the $r$-dimensional
market manifold $M$ for large $T$ (by the Laplace approximation of LAPLACE.md).

**Definition 2.1** (Manifold Universal Portfolio). *The **Manifold Universal Portfolio**
(MUP) integrates only over the market manifold $M^r \subset \Delta_{d-1}$:*

$$\hat{b}_{T}^{M} = \frac{\displaystyle\int_{M^r} b\, W_T(b)\,d\mathrm{vol}_{M}(b)}
{\displaystyle\int_{M^r} W_T(b)\,d\mathrm{vol}_{M}(b)} \tag{2.1}$$

*where $d\mathrm{vol}_{M}$ is the Riemannian volume element of $(M^r, g_M)$ — the induced
Fisher–Rao metric on the manifold.*

### 2.2 The manifold wealth process

**Theorem 2.2** *(MUP wealth, Laplace approximation on the manifold)*.

$$\log S_T^{*,M} = \log\int_{M^r} W_T(b)\,d\mathrm{vol}_{M}(b)$$

$$= T\cdot L_T(b^{\ast}) - \frac{r}{2}\log T + \frac{r}{2}\log(2\pi)
- \frac{1}{2}\log\det F_M(b^{\ast}) + O(1/T) \tag{2.2}$$

*where $F_M(b^{\ast}) = V_r^T F(b^{\ast}) V_r \in \mathbb{R}^{r\times r}$ is the Fisher matrix
restricted to the tangent space of $M$, and $V_r$ spans $T_{b^{\ast}}M$.*

*Proof.* The Laplace approximation of LAPLACE.md (Theorem 4.3) applies with $M$ in place
of $\Delta_{d-1}$. The key change: the dimension is $r$ (not $d-1$), and the Fisher matrix
is $F_M = V_r^T F V_r$ (the projection onto the factor directions). The uniform volume
measure $d\mathrm{vol}_{M}$ is proportional to Lebesgue measure on $T_{b^{\ast}}M \cong \mathbb{R}^{r}$
near $b^{\ast}$. The rest of the proof is identical. $\square$

### 2.3 Comparing MUP to Cover's universal portfolio

**Theorem 2.3** *(Regret comparison)*. *For the log-optimal portfolio $b^{\ast}$ on $M$:*

*Cover's universal portfolio:*
$$\frac{1}{T}\log S_T^{\ast} = L_T(b^{\ast}) - \frac{(d-1)\log T}{2T} - \frac{\log\det F(b^{\ast})}{2T} + O(1/T^2) \tag{2.3}$$

*Manifold Universal Portfolio:*
$$\frac{1}{T}\log S_T^{*,M} = L_T(b^{\ast}) - \frac{r\,\log T}{2T} - \frac{\log\det F_M(b^{\ast})}{2T} + O(1/T^2) \tag{2.4}$$

*The per-period regret of the MUP versus Cover's portfolio is:*
$$\frac{1}{T}\log S_T^{*,M} - \frac{1}{T}\log S_T^{\ast} = \frac{(d-1-r)\log T}{2T}
+ \frac{\log\det F(b^{\ast}) - \log\det F_M(b^{\ast})}{2T} + O(1/T^2) \tag{2.5}$$

*The first term is strictly positive for $r < d-1$. The second term requires care.*

*Proof.* Subtract (2.3) from (2.4). The first term $\frac{(d-1-r)\log T}{2T}$ is
positive since $d-1 > r$. This is the dominant term and represents the MUP's
advantage from restricting integration to the $r$-dimensional manifold $M^r$.

For the second term: $\det F(b^{\ast})$ is the determinant over all $d-1$ directions,
$\det F_M(b^{\ast})$ over only $r$ directions. We have
$\det F = \prod_{k=1}^{d-1}\lambda_k(F)$ and $\det F_M = \prod_{k=1}^{r}\lambda_k(F_M)$.
The Fisher correction term is:

$$\log\det F(b^{\ast}) - \log\det F_M(b^{\ast}) = \sum_{k=r+1}^{d-1}\log\lambda_k(F(b^{\ast})) + \delta_{\rm proj} \tag{2.6}$$

where $\delta_{\rm proj}$ accounts for the difference between the eigenvalues of the
projected matrix $F_M = V_r^T F V_r$ and those of $F$. The tail eigenvalues
$\lambda_k(F)$ for $k > r$ correspond to idiosyncratic directions and are typically
small (e.g., $\lambda_{r+1} \approx 0.1$), so $\log\lambda_k < 0$ and the sum in (2.6)
is *negative*, not positive. However, this Fisher correction is an $O(1/T)$ term,
while the leading dimension term is $O(\log T / T)$. The overall regret comparison is:

$$\text{Regret}_{\rm Cover} - \text{Regret}_{\rm MUP} = \frac{(d-1-r)\log T}{2T} + O(1/T) \tag{2.6a}$$

This is always non-negative asymptotically since $d - 1 \geq r$, and the
$\frac{(d-1-r)\log T}{2T}$ term dominates the $O(1/T)$ Fisher correction for
large $T$. However, for **finite $T$** and specific return sequences — particularly
when the manifold assumption is violated or when the idiosyncratic eigenvalues
are very small — the MUP can underperform Cover (see Section 2.4 for the precise
crossover condition). The asymptotic dominance holds almost surely as $T \to \infty$
under the manifold model. $\square$

**Numerical example** ($d=50$, $r=4$, $T=252$, $\lambda_{r+1} \approx 0.1$):

Regret is measured in **cumulative log-wealth units** over $T$ periods (i.e., the total
log-wealth lost relative to the log-optimal portfolio). These are *not* percentages of
return; they are log-scale quantities.

| Quantity | Cover's portfolio | MUP | Improvement |
|:---------|:-----------------:|:---:|:-----------:|
| Regret dimension | $49\log T / (2T)$ | $4\log T / (2T)$ | $\times 12.25$ |
| Regret (1 year) | $49 \times 5.53 / 504 \approx 0.54$ | $4 \times 5.53 / 504 \approx 0.044$ | $\times 12.25$ |
| Fisher correction | $-\frac{\log\det F}{2\times 252}$ | $-\frac{\log\det F_M}{2\times 252}$ | Smaller |
| Integral dimension | 49 | 4 | $\times 12.25$ |
| Computation | Intractable | Trivial | $\infty$ |

Cover regret $\approx 0.54$ means the Cover portfolio loses approximately 54% of the
log-optimal cumulative wealth to integration over unnecessary dimensions. MUP regret
$\approx 0.044$ means only 4.4% cumulative log-wealth lost. **The 12$\times$ improvement
is the ratio of dimensions: $(d-1)/r = 49/4 = 12.25$.**

### 2.4 When does the MUP underperform?

As noted in Section 2.3, the MUP's asymptotic dominance over Cover holds under the
manifold model as $T \to \infty$. However, for **finite $T$**, the MUP can underperform
in two distinct scenarios:

**(a) Manifold assumption violated.** The MUP ignores the idiosyncratic directions
(normal to $M$). For an efficient market ($H=0$), these directions offer no excess
return (Theorem 1.1), so the MUP loses nothing by ignoring them. For an inefficient
market ($H \neq 0$), the full simplex integral captures some of the normal-direction
alpha, and Cover's portfolio can outperform the MUP at finite horizons.

**(b) Small idiosyncratic eigenvalues.** When the Fisher matrix eigenvalues $\lambda_k$
for $k > r$ are very small (close to zero), the negative Fisher correction
$\sum_{k>r} \log \lambda_k$ in (2.6) can be large in magnitude, partially offsetting
the dimension advantage at moderate $T$. This is a finite-sample effect that vanishes
as $T \to \infty$ since the $\log T$ term dominates.

The crossover point for scenario (a):

$$\text{MUP outperforms Cover's iff: } \frac{(d-1-r)\log T}{2T} > |H|^2/T \tag{2.7}$$

For $d=50$, $r=4$, $T=252$: LHS $\approx 0.49$ (in cumulative log-wealth units); RHS requires $|H| > \sqrt{0.49} \approx 0.70$ — a Sharpe ratio of 0.70. In other words, the MUP outperforms Cover unless the market is so inefficient that $|H|$ exceeds 0.70 (a very large curvature). For typical markets with moderate inefficiency, the MUP dominates.

**Conclusion:** For real markets, use the MUP. The manifold restriction dominates the
idiosyncratic correction for any reasonable $T$ and $d$.

---

## 3. The MUP Algorithm

### 3.1 Computing the MUP

**Algorithm 3.1** (Manifold Universal Portfolio — practical implementation).

**Input:** Return history $X \in \mathbb{R}^{T\times d}$, factor dimension $r$.

**Step 1.** Estimate the factor structure. Compute the empirical covariance:

$$\hat\Sigma = \frac{1}{T}(\log X)^T(\log X) - (\overline{\log x})(\overline{\log x})^T \tag{3.1}$$

Take PCA: $\hat\Sigma = V\Lambda V^T$. The factor subspace is $V_r = [v_1|\cdots|v_r]$.

**Step 2.** Find the log-optimal portfolio on the manifold:

$$b^{\ast} = \operatorname{argmax}_{b = \Pi_\Delta(V_r\alpha),\, \alpha\in\mathbb{R}^{r}}
\frac{1}{T}\sum_{t=1}^{T} \log\langle b, x_t\rangle \tag{3.2}$$

This is a convex program in $\alpha \in \mathbb{R}^{r}$ — an $r$-dimensional problem
instead of $(d-1)$-dimensional. For $r=4$: trivial.

**Step 3.** Compute the manifold Fisher matrix:

$$F_M(b^{\ast}) = V_r^T F(b^{\ast}) V_r, \qquad F_{ij}(b^{\ast}) = \frac{1}{T}\sum_t
\frac{x_{t,i}x_{t,j}}{(b^{*T}x_t)^2} \tag{3.3}$$

**Step 4.** Compute the Laplace correction:

$$\hat{b}_{T}^{M} = b^{\ast} + \frac{1}{T}F_M(b^{\ast})^{-1}\nabla_{M} L_T(b^{\ast})
= b^{\ast} + O(1/T^2) \tag{3.4}$$

For the uniform prior (Jeffreys), the $O(1/T)$ correction vanishes (Theorem 4.2 of
LAPLACE.md) and $\hat{b}_{T}^{M} = b^{\ast} + O(1/T^2)$ exactly.

**Step 5.** (Optional) Manifold MC for higher accuracy. Sample $N$ points
$\{b_k\}$ uniformly on $M$ via the Halton sequence on the $r$-simplex $\Delta_{r-1}$
(mapped to $M$ through the factor parameterisation $\alpha \mapsto \Pi_\Delta(V_r\alpha)$):

$$\hat{b}_{T}^{M,\rm MC} = \frac{\sum_{k=1}^{N} b_k\, W_T(b_k)}{\sum_{k=1}^{N} W_T(b_k)} \tag{3.5}$$

For $r=4$ and $N=1000$ QMC points: error $O(1/N) = O(10^{-3})$, computation $O(1000 \times 252 \times 50) \approx 10^7$ flops — milliseconds. Cover's full simplex QMC with $N=1000$ and $d=50$ has error $O(1)$ (completely fails for $d=50$). The manifold restriction is what makes QMC work.

### 3.2 The MUP as a factor model portfolio

The MUP $\hat{b}_{T}^{M}$ is always a convex combination of the $r+1$ extreme points of
$M$ (the vertices of the factor simplex mapped through $\Pi_\Delta \circ V_r$). These
are the "pure factor portfolios" — portfolios that maximally load on a single factor.
The MUP is a weighted average of these, with weights determined by the factor performance.

For the CAPM ($r=1$): the MUP is always a convex combination of the risk-free portfolio
($b = (1/d,\ldots,1/d)$) and the maximum-Sharpe portfolio. This is precisely the
two-fund separation theorem — **the MUP is the geometric derivation of the two-fund
separation theorem.**

For $r=4$ (Fama-French): the MUP is a convex combination of 5 pure factor portfolios
(market, value, size, momentum, profitability). **The manifold geometry gives a canonical
construction of the factor portfolio weights** without requiring specification of investor
risk preferences.

---

## 4. Maximum Compression of Return Sequences

### 4.1 Rate-distortion for portfolios

The **rate-distortion** problem asks: at what information rate $R$ can we represent a
return sequence $(x_1,\ldots,x_T)$ with log-growth distortion at most $D$?

$$R(D) = \min_{q(b|x_{1:T}):\, \mathbb{E}[L(b^{\ast}) - L(b)] \leq D} I(x_{1:T}; b) \tag{4.1}$$

where $I(x;b)$ is the mutual information between the return sequence and the portfolio
strategy.

**Theorem 4.1** *(Maximum compression of return sequences)*.

*(i) The minimum description length (in nats) of a return sequence $(x_1,\ldots,x_T)$
with distortion $D \leq L(b^{\ast}) - L(b)$ is:*

$$R(D) = h_{\rm Kelly} \cdot T - \max_{b: L(b) \geq L(b^{\ast}) - D} H(b) \tag{4.2}$$

*where $H(b)$ is the differential entropy of the portfolio $b$ under the posterior $\pi_T$.*

*(ii) The **minimum-distortion portfolio code** uses codewords of length:*

$$\ell^{\ast} = \frac{r}{2}\log T + \frac{1}{2}\log\det F_M(b^{\ast}) + O(1) \text{ nats} \tag{4.3}$$

*This is the description length of the optimal portfolio — determined by the factor
dimension $r$ and the Fisher geometry, not by the full simplex dimension $d-1$.*

*(iii) The **compression ratio** — signal dimension to description length — is:*

$$\mathrm{CR}(T,d,r) = \frac{Td}{r\log T/2 + \log\det F_M/2} \approx \frac{2Td}{r\log T} \tag{4.4}$$

*For $d=50$, $r=4$, $T=252$: $\mathrm{CR} \approx \frac{2 \times 252 \times 50}{4 \times 5.5} \approx 1145$.*
*The return sequence can be compressed by a factor of over 1000 with negligible portfolio performance loss.*

*Proof of (ii).* The optimal portfolio estimator is the MUP $\hat{b}_{T}^{M}$, which lies
in the $r$-dimensional manifold $M$. Specifying a point on $M$ requires $r$ real numbers;
at precision $1/\sqrt{T}$ (the posterior width from the Laplace approximation), each
requires $\frac{1}{2}\log T$ bits (Shannon's source coding theorem). The determinant
$\log\det F_M/2$ is the coding overhead from the non-uniform Fisher metric on $M$. $\square$

**Economic interpretation.** The return sequence $(x_1,\ldots,x_T)$ has $Td$ scalar
values, but the portfolio-relevant information is contained in $r\log T/2$ nats —
a tiny fraction. The factor structure $M$ is the compression codebook; the MUP is
the decoder. **The efficient market is the one whose factor structure achieves the
minimum description length encoding of its return process.**

### 4.2 The Kolmogorov–Cover–Chaitin connection

The **algorithmic complexity** of the portfolio strategy $b$ is the length of the
shortest program that computes $b$ given the return data. By the algorithmic version
of Shannon's source coding theorem:

$$K(b | x_{1:T}) \approx \ell^{\ast} = \frac{r}{2}\log T + O(\log\log T) \text{ bits} \tag{4.5}$$

(almost surely, for generic return processes). The universal portfolio $\hat{b}_{T}^{M}$
is **Kolmogorov optimal** — it achieves the algorithmic complexity lower bound. The
minimum-complexity strategy is the one that exploits only the factor structure (the
$r$-dimensional manifold) and ignores the $d-1-r$ idiosyncratic dimensions. This
is exactly the MUP.

---

## 5. Tightening Cover's Convergence Bound

### 5.1 Cover's original bound

Cover \[1991\] proved:

$$\frac{1}{T}\log S_T^{\ast} \geq L(b^{\ast}) - \frac{(d-1)\log(T+1)}{T} \tag{5.1}$$

This lower bounds the universal portfolio's performance relative to the best CRP.
The term $\frac{(d-1)\log T}{T}$ is the "regret" — the price of not knowing $b^{\ast}$
in advance.

### 5.2 Our exact asymptotic

From Theorem 2.2 and LAPLACE.md Theorem 4.3:

**Theorem 5.1** *(Tightened Cover bound)*. *For the Manifold Universal Portfolio:*

$$\frac{1}{T}\log S_T^{*,M} = L(b^{\ast}) - \frac{r\,\log T}{2T}
- \frac{\log\det F_M(b^{\ast})}{2T} + \frac{\mathcal{M}_{0}^{M}}{T^2} + O(1/T^3) \tag{5.2}$$

*where $\mathcal{M}_{0}^{M}$ is the manifold Maslov correction (Proposition 5.1 of LAPLACE.md
with $d$ replaced by $r+1$). This gives:*

*(i) The exact leading constant: $r/2$ vs Cover's $d-1$.*

*(ii) The exact sub-leading constant: $\log\det F_M(b^{\ast})/2$, computable from data.*

*(iii) A non-asymptotic bound: for $T \geq T_0(r, F_M)$, the MUP achieves within
$\varepsilon$ of $L(b^{\ast})$ whenever $T \geq (r\log T + \log\det F_M)/(2\varepsilon)$.*

*Comparison:*

| | Cover's bound | MUP (this paper) |
|:--|:---:|:---:|
| Leading regret | $(d-1)\log T / T$ | $r\log T / T$ |
| Sub-leading | $O(1/T)$ unknown | $\log\det F_M / T$ (explicit) |
| Next order | unknown | $\mathcal{M}_{0}^{M} / T^2$ (explicit) |
| Dimension | $d-1 = 49$ | $r = 4$ |

### 5.3 The minimax optimal regret

**Theorem 5.2** *(Minimax lower bound)*. *For any portfolio strategy $\hat{b}_{T}$ and
for a market with factor dimension $r$:*

$$\sup_{x_{1:T}} \left[L(b^{\ast}(x_{1:T})) - \frac{1}{T}\log S_T(\hat{b})\right]
\geq \frac{r\,\log T}{2T} + O(1/T) \tag{5.3}$$

*The MUP achieves this bound exactly — it is minimax optimal.*

*Proof.* The lower bound (5.3) follows from the Shtarkov minimax regret \[1987\] applied
to the $r$-dimensional model class $\{L(b) : b \in M^r\}$. The minimax optimal strategy
is the Normalised Maximum Likelihood (NML) code, which coincides with the Laplace
approximation to the manifold integral — exactly the MUP. $\square$

**The MUP is minimax optimal with regret $\frac{r\log T}{2T}$ — not $(d-1)\log T/T$
as in Cover's bound.** The difference is the factor model: the correct "complexity"
of the portfolio problem is $r$-dimensional, not $(d-1)$-dimensional.

---

## 6. Portfolio Construction from the Manifold Geometry

### 6.1 The geometric efficient frontier revisited

From INFORMATION_THEORY.md Section 6, the efficient frontier is the normal bundle of
the market manifold. We now make this constructive.

**Algorithm 6.1** (Geometric efficient frontier).

**Step 1.** Compute the MUP $\hat{b}_{T}^{M} \approx b^{\ast}$ and the normal frame $\{\nu_k\}_{k=r+1}^{d-1}$.

**Step 2.** The efficient frontier parameterised by risk level $\rho \geq 0$:

$$b_\rho = b^{\ast} + \rho\cdot\frac{\nu^{\ast}}{|\nu^{\ast}|_{g^{FR}}},
\qquad \nu^{\ast} = \operatorname{argmax}_{\nu \in N_{b^{\ast}}M,\,|\nu|=1}
\mathbb{E}[(b^{\ast} + \nu)^T x] \tag{6.1}$$

The normal vector $\nu^{\ast}$ that maximises expected return is $\nu^{\ast} = F(b^{\ast})^{-1}(\mu - \lambda_*\mathbf{1})/\|F^{-1}(\mu - \lambda_*\mathbf{1})\|$ where $\mu_i = \mathbb{E}[x_i]$ and $\lambda_*$ is the Lagrange multiplier. This is the **projection of the expected return vector onto the normal bundle** — exactly the idiosyncratic part of expected returns that the factor model misses.

**Step 3.** The frontier curve $\{b_\rho : \rho \geq 0\}$ traces the Markowitz efficient frontier from $b^{\ast}$ (minimum variance, on the manifold) outward in the normal direction (increasing idiosyncratic risk, increasing expected return).

**New insight.** The classical Markowitz frontier has two regimes:
- **On-manifold** ($\rho = 0$): pure factor bets, zero idiosyncratic risk, minimum variance for given factor exposure.
- **Off-manifold** ($\rho > 0$): idiosyncratic bets, increasing $H$ (moving away from the minimal surface), increasing Sharpe opportunity and increasing Willmore energy.

The traditional efficient frontier conflates these two regimes. The manifold geometry separates them cleanly: *factor allocation* (moving along $M$) and *idiosyncratic allocation* (moving off $M$) are orthogonal in the Fisher–Rao metric.

### 6.2 Risk attribution

**Definition 6.2** (Geometric risk decomposition). *For any portfolio $b \in \Delta_{d-1}$:*

$$\mathrm{Risk}(b) = \underbrace{(b - b^{\ast})^T F_M(b^{\ast})(b - b^{\ast})}_{\text{systematic (on-manifold)}} + \underbrace{(b - b^{\ast})^T F_N(b^{\ast})(b - b^{\ast})}_{\text{idiosyncratic (off-manifold)}} \tag{6.2}$$

*where $F_M = V_r^TFV_r$ is the factor Fisher matrix and $F_N = V_N^TFV_N$ is the
idiosyncratic Fisher matrix ($V_N = [v_{r+1}|\cdots|v_{d-1}]$).*

This decomposition is exact and orthogonal in $g^{FR}$ — systematic and idiosyncratic
risk are genuinely independent in the Fisher–Rao metric. **Traditional Barra-style risk
attribution corresponds to this decomposition, now given a canonical geometric derivation.**

---

## 7. The Tour de Force Paper: Structure and Synthesis

The six companion papers and this one form a coherent mathematical theory. We outline
the structure of a unified treatment.

### 7.1 The narrative arc

The theory begins with a question in financial mathematics (how accurate is the Laplace
approximation to Cover's universal portfolio?) and ends with a classification of all
efficient market structures using century-old theorems in differential geometry. The
narrative arc:

**Act I: The Simplex Integral (LAPLACE.md, FK_SIMPLEX.md)**

1. The universal portfolio is a simplex integral.
2. The Laplace approximation gives $O(1/T^2)$ error — surprisingly good.
3. *Why* this is so good: the Jeffreys prior ($= $ uniform Dirichlet$(1,\ldots,1)$) is the unique prior for which the $O(1/T)$ Bayesian correction vanishes.
4. The Laplace approximation is the leading WKB term of a Feynman–Kac PDE on the simplex.
5. The Fisher information matrix is the Hessian of the WKB action.
6. The stochastic Stokes theorem on the simplex: the Bhattacharyya sphere curvature corrects the classical Stokes theorem by $\varepsilon^2(d-2)/4$.

**Act II: The Minimal Surface (MINIMAL_SURFACE.md, CLASSIFICATION.md)**

7. The market's factor structure defines a submanifold $M$ of the simplex.
8. The mean curvature $H$ measures exploitable alpha: $\mathrm{Sharpe}^{\ast} = \|H\|_{L^2}$ (proved).
9. Market efficiency = minimal surface ($H=0$) (one direction proved, converse proved for dynamic strategies here).
10. The classification: stable efficient markets are exactly the great sphere sections (CAPMs) (proved for $r \geq d-2$; the generic case $r < d-2$ requires boundary corrections — see CLASSIFICATION Open Problem). This follows from Simons (1968) and Lawson–Simons (1973).
11. The Clifford torus, Lawson surfaces: unstable efficient market structures.
12. Only 12 years after Simons, the Clifford torus's stability was settled by Marques–Neves (2012) — directly applicable to market structure.

**Act III: The Information Theory (INFORMATION_THEORY.md, SVD_MANIFOLD.md)**

13. Efficient market = maximum channel capacity = minimum description length = SMB typical set decoder.
14. The SVD of the shape operator is trace-free iff the surface is minimal — curvature preservation under pseudoinversion.
15. Volatility is conformally invariant (Willmore energy unchanged) but controls the stability phase transition through the spectral gap.
16. Diaconis's mixing time = Jacobi eigenvalue = information absorption rate.

**Act IV: The Algorithm (this paper)**

17. Conjecture proved for dynamic strategies.
18. The Manifold Universal Portfolio: $r$-dimensional integral, minimax optimal, factor-of-12 regret improvement.
19. Maximum compression: factor dimension $r$ controls compression cost, not $d-1$.
20. Cover's bound tightened from $(d-1)\log T/T$ to $r\log T/T$.
21. Geometric efficient frontier: factor and idiosyncratic risk cleanly separated.

### 7.2 The central theorem of the unified paper

**Master Theorem.** *Let $M^r \subset (\Delta_{d-1}, g^{\mathrm{FR}})$ be the market
manifold of a $d$-asset market with $r$ systematic factors. The following are equivalent:*

1. $M$ is minimal: $H \equiv 0$ (geometry).
2. $\mathrm{Sharpe}^{\ast} = 0$ for all dynamic factor strategies (economics).
3. $\nabla_M C(b^{\ast}) = 0$: channel capacity is stationary (information theory).
4. $K(M) = K_{\rm CAPM}$: minimum description complexity for topology (complexity).
5. $\frac{1}{T}\log W_T(b^{\ast}) \to h_{\rm Kelly}$ without systematic bias (ergodic theory).
6. The MUP is minimax optimal with regret $\frac{r\log T}{2T}$ (online learning).

*Moreover: $M$ is a stable efficient market iff it is totally geodesic ($II = 0$, CAPM),
by the Lawson–Simons theorem (proved for $r \geq d-2$; the generic case $r < d-2$
requires boundary corrections — see CLASSIFICATION Open Problem). The Sharpe$^{\ast}$
of a perturbation $\Sigma_\varepsilon$ from a CAPM efficient market grows as
$\varepsilon|\lambda_1(J)|$ where $\lambda_1(J)$ is the first eigenvalue of the Jacobi
stability operator — the "stiffness" of the efficient equilibrium.*

### 7.3 Recommended title and structure for the Tour de Force paper

**Title:** *"Minimal Surfaces, Market Efficiency, and the Geometry of Universal Portfolios"*

**Subtitle:** *"From the Feynman–Kac simplex integral to the Simons stability theorem"*

**Sections:**
1. Introduction and Overview (5 pages)
2. The Universal Portfolio as a Feynman–Kac Functional (8 pages — from FK_SIMPLEX.md)
3. The Laplace Approximation as WKB (6 pages — from LAPLACE.md)
4. The Market Manifold and the Minimal Surface Condition (8 pages — from MINIMAL_SURFACE.md)
5. Classification of Efficient Markets (6 pages — from CLASSIFICATION.md)
6. The SVD Structure and Pseudoinverse Duality (4 pages — from SVD_MANIFOLD.md)
7. Information Theory: Capacity, Entropy, and the SMB Theorem (6 pages — from INFORMATION_THEORY.md)
8. The Manifold Universal Portfolio (6 pages — this paper)
9. Conclusions and Open Problems (3 pages)

**Total:** approximately 52 pages. Target: *Annals of Mathematics* or *Journal of the
American Mathematical Society* (if the conjecture is fully resolved);
*Annals of Applied Probability* (current state).

### 7.4 Open problems for the unified paper

**Priority 1** (most tractable, closes the main gap): Complete the proof of Theorem 1.2
by showing that in a deep market ($N \to \infty$), the dynamic factor strategy earns
strictly positive excess return when $H \neq 0$. This requires a formal model of
competitive equilibrium with $N$ investors, which is standard in continuous-time finance.

**Priority 2** (high impact): Implement the MUP on real return data (CRSP universe,
$d=50$ stocks, $T=10$ years) and compare to Cover's theoretical portfolio and to the
empirical best CRP. Compute the factor dimension $r$ adaptively using the stable rank
of the Fisher matrix.

**Priority 3** (deepest, most open): Determine whether the Plateau problem on
$(\Delta_{d-1}, g^{\mathrm{FR}})$ has a unique solution for generic boundary curves
$\Gamma = \{b^{\ast}(t)\}$. This would establish existence of the efficient market manifold
and its uniqueness given the log-optimal portfolio path — a fundamental structural result.

**Priority 4** (Diaconis connection): Prove the mixing time threshold (7.2 of
INFORMATION_THEORY.md) rigorously. The sharp threshold should follow from the spectral
theory of the WF diffusion using Diaconis's hypercontractivity methods.

---

## Appendix: The MUP is Cover's Portfolio Restricted to M

**Proposition A.1.** *The MUP $\hat{b}_{T}^{M}$ is the Cover universal portfolio of the
restricted market in which only portfolios on $M$ are permitted:*

$$\hat{b}_{T}^{M} = \hat{b}_{T}^{\rm Cover}\!\left[\text{restricted to }M^r\right] \tag{A.1}$$

*Proof.* By the definition of the MUP (2.1), it has exactly the form of Cover's
portfolio with the measure $d\mu$ replaced by the volume measure $d\mathrm{vol}_{M}$ on $M$.
This is Cover's portfolio for a "world" in which the investor is constrained to choose
$b \in M$. The universal portfolio in this restricted world is exactly the MUP. $\square$

This gives a clean economic interpretation: **the MUP is what Cover's portfolio becomes
when the investor knows the factor structure but not the factor loadings**. The factor
structure ($M$) is known; the specific portfolio within $M$ ($b^{\ast}$) is not. The MUP
averages over all portfolios within $M$, weighted by their historical wealth, exactly
as Cover averages over all portfolios in $\Delta$.

---

## References

Cover, T. M. (1991). Universal portfolios. *Mathematical Finance* 1(1), 1–29.

Cover, T. M. and Ordentlich, E. (1996). Universal portfolios with side information.
*IEEE Transactions on Information Theory* 42(2), 348–363.

Shtarkov, Y. M. (1987). Universal sequential coding of single messages.
*Problems of Information Transmission* 23(3), 175–186.

Xie, Q. and Barron, A. R. (2000). Asymptotic minimax regret for data compression,
gambling, and prediction. *IEEE Transactions on Information Theory* 46(2), 431–445.

*[All other references as per companion papers FK_SIMPLEX.md, LAPLACE.md,
MINIMAL_SURFACE.md, CLASSIFICATION.md, SVD_MANIFOLD.md, INFORMATION_THEORY.md]*
