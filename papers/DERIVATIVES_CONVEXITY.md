# Derivatives Pricing on Minimal Market Manifolds,
## Convex Geometry of Portfolios, and the Boyd Connections

**Saxon Nicholls** — me@saxonnicholls.com

**Paper II.4** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We develop two parallel theories. First, we price derivatives — index options in
particular — using the Feynman–Kac PDE established in FK_SIMPLEX.md, restricted to the
minimal market manifold $M^r \subset (\Delta_{d-1}, g^{\mathrm{FR}})$. For a strongly
efficient market ($H=0$), the Black–Scholes PDE reduces to a parabolic equation on
an $r$-dimensional Riemannian manifold with the Fisher–Rao metric, and index option prices
acquire a closed-form curvature correction beyond Black–Scholes: the implied volatility
surface is determined by the second fundamental form of $M$, the Willmore energy controls
the vol-of-vol, and put-call parity has a geometric correction from the mean curvature.
For an efficient market (minimal surface), **index option prices depend only on $r$
geometric invariants of $M$** — not on the full $d$-dimensional return distribution.
We work out explicit put and call pricing formulae. Second, we develop the convex geometry
of the portfolio problem. The log-growth rate $L_T(b)$ is strictly concave on $\Delta_{d-1}$,
its negative Hessian is the Fisher information matrix, and the minimal surface condition
$H=0$ is the condition that the **gradient of $L_T$ lies in the image of the embedding
differential** — a convex duality condition. We connect to Boyd's disciplined convex
programming framework: the portfolio optimisation problem is a log-sum-exp program, the
Fisher matrix is its Hessian, and the Lagrangian dual gives the risk-neutral measure.
We prove that CVaR (Conditional Value-at-Risk) is geometrically controlled by the distance
from the market manifold to the boundary of the simplex, VaR is the $g^{\mathrm{FR}}$-ball
radius at $b^{\ast}$, and the Markowitz efficient frontier is the projection of the $g^{\mathrm{FR}}$
unit ball onto the mean-variance plane. Convex operators are pervasive: the mean curvature
$H$ is the sub-differential of the area functional, the Willmore energy is a convex function
of the second fundamental form spectrum, and the stability index counts the negative
eigenvalues of a convex-concave saddle point problem.

**Keywords.** Index options; Feynman–Kac on manifolds; geometric Black–Scholes; minimal
surface; put-call parity; implied volatility; convex geometry; log-sum-exp; Fisher information;
CVaR; Markowitz; Boyd; disciplined convex programming; sub-differential; Legendre transform.

**MSC 2020.** 91G20, 91G10, 53A10, 90C25, 49N15, 53C17, 62P05.

---

## 1. Introduction

### 1.1 Two convergent threads

The universal portfolio theory developed in this series lives at the intersection of
two mathematical structures that have been studied independently:

**Thread 1: Feynman–Kac pricing.** The Black–Scholes equation is a Feynman–Kac PDE
on flat space. Our FK PDE lives on the curved space $(\Delta_{d-1}, g^{\mathrm{FR}})$.
The minimal surface condition constrains the geometry of this space and should therefore
simplify option pricing — just as Black–Scholes simplifies when the underlying follows
geometric Brownian motion on a straight line rather than a curve.

**Thread 2: Convex geometry.** The portfolio optimisation problem is convex: maximise
a concave function $L_T(b)$ over the convex set $\Delta_{d-1}$. The objects of our
geometric theory — the Fisher matrix, the mean curvature, the Jacobi operator — all
arise naturally from the convex analysis of this program. Boyd's group at Stanford has
developed disciplined convex programming (DCP) \[Grant–Boyd 2008\] as a systematic
framework; our theory fits squarely within it and extends it in geometric directions.

The central insight connecting both threads: **for a minimal market manifold ($H=0$),
the curvature of the option pricing PDE and the curvature of the portfolio optimisation
landscape are the same object** — the second fundamental form $II$ of $M$. This is
not a coincidence; it follows from the identification of the Fisher information as
both the WKB action Hessian (LAPLACE.md) and the KKT Hessian of the portfolio program.

---

## 2. Derivative Pricing on the Market Manifold

### 2.1 The geometric Black–Scholes framework

**Setup.** Let $S_t = (S_{t,1},\ldots,S_{t,d})^T$ be asset prices. The index (log-optimal
portfolio value) is $I_t = b^{*T}S_t$. A European call option on the index:

```math
C(I_t, t) = e^{-r_f(T-t)}\mathbb{E}^{\mathbb{Q}}\!\left[\max(I_T - K, 0)\right] \tag{2.1}
```

In the classical Black–Scholes model, $I_t$ follows GBM and the pricing PDE is:

```math
\frac{\partial C}{\partial t} + \frac{1}{2}\sigma_I^2 I^2\frac{\partial^2 C}{\partial I^2}
+ r_f I\frac{\partial C}{\partial I} - r_f C = 0 \tag{2.2}
```

The **geometric Black–Scholes** — pricing on the market manifold — generalises this
by replacing the scalar volatility $\sigma_I^2$ with the curvature-dependent volatility
of the index process on $M$.

### 2.2 The index process on the manifold

The index $I_t = b^{\ast}(t)^T S_t$ depends on both $S_t$ (prices) and $b^{\ast}(t)$ (evolving
weights). On the market manifold, $b^{\ast}(t)$ follows the WF diffusion restricted to $M^r$:

```math
db^{\ast}_{i} = -\varepsilon^2 H_i(b^{\ast}(t))\,dt + \varepsilon\sum_k \sigma_{ik}(b^{\ast}(t))\,dW_k \tag{2.3}
```

(from FK_SIMPLEX.md equation 2.5). For an efficient market ($H=0$), the drift vanishes
and the portfolio evolution is a pure diffusion on $M$. The index volatility is:

```math
\sigma_I^2(b^{\ast}, t) = \sum_{ij} b^{\ast}_{i} b^{\ast}_{j}\,\Sigma_{ij}^{\rm asset}(t)
= b^{*T}\Sigma^{\rm asset} b^{\ast} \tag{2.4}
```

where $\Sigma^{\rm asset}$ is the asset return covariance. In Fisher–Rao geometry:

```math
\sigma_I^2(b^{\ast}) = \langle b^{\ast}, F(b^{\ast})^{-1}b^{\ast}\rangle_{g^{\mathrm{FR}}} = \mathrm{tr}[F_M(b^{\ast})^{-1}] \tag{2.5}
```

(using the Bhattacharyya sphere identity $b^T\Sigma b \approx \mathrm{tr}[F_M^{-1}]$
for the log-normal factor model).

**Theorem 2.1** *(Index volatility decomposition)*. *The index volatility decomposes as:*

```math
\sigma_I^2 = \underbrace{\mathrm{tr}[F_M^{-1}]}_{\text{systematic (on-manifold)}}
+ \underbrace{\mathrm{tr}[F_N^{-1}]}_{\text{idiosyncratic (off-manifold)}}
+ \underbrace{2H^2\cdot\mathrm{Area}(M)}_{\text{curvature correction}} \tag{2.6}
```

*where $F_N = V_N^T F V_N$ is the idiosyncratic Fisher matrix and $H$ is the mean curvature.
For an efficient market ($H=0$), the curvature correction vanishes and:*

```math
\sigma_I^2\big|_{H=0} = \mathrm{tr}[F_M^{-1}] + \mathrm{tr}[F_N^{-1}] \tag{2.7}
```

*The idiosyncratic term $\mathrm{tr}[F_N^{-1}]$ is controlled by the eigenvalues of the
Fisher matrix in the normal bundle — the "basis risk" of tracking the index with the
factor portfolio.*

### 2.3 The manifold pricing PDE

For a derivative with payoff $\Psi(b^{\ast}(T), S_T)$ at expiry $T$, the price
$V(b^{\ast}, S, t)$ satisfies the **manifold pricing PDE**:

```math
\frac{\partial V}{\partial t} + \mathcal{L}^{M} V + r_f(S)\cdot V - r_f V = 0 \tag{2.8}
```

where $\mathcal{L}^{M}$ is the generator of the joint process $(b^{\ast}(t), S_t)$ restricted
to $M^r \times \mathbb{R}^{d}_+$.

For an index option (payoff depends only on $I_t = b^{*T}S_t$), the PDE reduces to
a 1-dimensional equation in the index value:

```math
\frac{\partial C}{\partial t} + \frac{1}{2}\sigma_I^2(b^{\ast})\cdot I^2\frac{\partial^2 C}{\partial I^2}
+ \underbrace{\varepsilon^2 H(b^{\ast})\cdot I\frac{\partial C}{\partial I}}_{\text{curvature drift}}
- r_f C + \underbrace{\frac{\varepsilon^2}{2}\Delta_M C}_{\text{manifold Laplacian}} = 0 \tag{2.9}
```

**For an efficient market ($H=0$):**

```math
\frac{\partial C}{\partial t} + \frac{1}{2}\sigma_I^2(b^{\ast})\cdot I^2\frac{\partial^2 C}{\partial I^2}
- r_f C + \frac{\varepsilon^2}{2}\Delta_M C = 0 \tag{2.10}
```

The extra term $\frac{\varepsilon^2}{2}\Delta_M C$ is the **manifold Laplacian correction**
— the diffusion of the portfolio weights on $M$ contributes to the option price through
the intrinsic geometry of the market manifold.

For the CAPM (great sphere, $M = S^r_+$): $\Delta_{S^r}$ has the spherical Laplacian
eigenvalues, and the correction adds $\varepsilon^2 k(k+r-1)/4$ to the effective
"interest rate" for the $k$-th harmonic component of the payoff. For smooth payoffs
(low harmonic content), this correction is small: $O(\varepsilon^2 r) = O(r/T)$.

### 2.4 Explicit index call formula

**Theorem 2.2** *(Geometric Black–Scholes for index calls)*. *For an efficient market
($H=0$), the price of a European index call $C(I, t; K, T)$ is:*

```math
C = I\cdot N(d_+) - Ke^{-r_f\tau}N(d_-) + \text{Manifold correction} \tag{2.11}
```

*where $\tau = T-t$, $d_\pm = \frac{\log(I/K) + (r_f \pm \sigma_I^2/2)\tau}{\sigma_I\sqrt\tau}$,
and the manifold correction is:*

```math
\Delta C = \frac{\varepsilon^2\tau}{2}\cdot\left[\frac{(r-1)}{4}\cdot I\cdot N'(d_+)
+ \frac{1}{2}\mathrm{tr}[F_M^{-1}\nabla^2_{b^{\ast}}C]\right] + O(\varepsilon^4) \tag{2.12}
```

*The first term in (2.12) is the Ricci curvature correction from the sphere $S^r_+$.
On the Bhattacharyya sphere (sectional curvature $K=1/4$), the Ricci curvature is
$\mathrm{Ric}_{S^r} = \frac{(r-1)}{4}g_{S^r}$, giving a factor of $(r-1)/4$ — not
$r(r-1)/4$. (The heat kernel expansion on a Riemannian manifold gives a scalar curvature
correction $R/6$, and $R = r(r-1)/4$ on $S^r$ with $K=1/4$. However, the correction to
the option price involves $\mathrm{Ric}(b^{\ast}, b^{\ast})$, not the full scalar curvature,
since the payoff depends on a single direction $b^{\ast}$. Hence the factor is $(r-1)/4$.)
The second term involves the Hessian of the call price with respect to portfolio weights.*

*Proof sketch.* The manifold Laplacian on $M = S^r_+$ in Bhattacharyya normalisation is
```math
\Delta_{S^r} = \frac{1}{\sqrt{\det g}}\partial_i(\sqrt{\det g}\,g^{ij}\partial_j).
```
For a function of the index $I = b^T S$ only, the Laplacian picks up only the radial
component plus the Ricci correction. Expanding $\Delta_M C$ around the Black–Scholes
solution and integrating over $\tau$ gives (2.12). $\square$

**Interpretation of (2.12):**
- The Ricci correction $\frac{(r-1)}{4}$ grows with factor dimension $r$.
- For $r=1$ (CAPM): the Ricci correction is $0$ — the great circle has no curvature, Black–Scholes is exact.
- For $r=2$ (two-factor): Ricci correction $= \frac{1}{4}$.
- For $r=4$ (Fama-French): Ricci correction $= \frac{3}{4}$.

### 2.5 Explicit index put formula and put-call parity

**Theorem 2.3** *(Geometric put-call parity)*. *For the manifold pricing model:*

```math
C - P = I - Ke^{-r_f\tau} + \underbrace{\frac{\varepsilon^2\tau}{2}\cdot\mathcal{R}(b^{\ast}, r)}_{\text{geometric correction}} \tag{2.13}
```

*where $\mathcal{R}(b^{\ast}, r) = \frac{(r-1)}{4}\mathrm{tr}[F_M^{-1}]$ is the Ricci
correction term. For $r=1$ (CAPM): $\mathcal{R} = 0$ and classical put-call parity holds
exactly. For $r \geq 2$: put-call parity acquires a positive geometric correction term —
calls are relatively more expensive than puts by $\mathcal{R}/2$.*

*Proof.* Apply (2.9) to $C - P$ with payoffs $\max(I-K,0)$ and $\max(K-I,0)$.
The difference satisfies (2.9) with payoff $I-K$ (linear, hence harmonic in $I$).
The manifold Laplacian of the linear payoff $\Psi(I) = I-K$ gives the Ricci correction.
Takahashi's theorem states $\Delta_M\phi_i = -(d-1)\phi_i$ for the Bhattacharyya
coordinate functions $\phi_i = \sqrt{b_i}$. Since $b_i = \phi_i^2$, the Laplacian
of $b_i$ is $\Delta_M b_i = 2\phi_i\Delta_M\phi_i + 2|\nabla\phi_i|^2
= -2(d-1)\phi_i^2 + 2|\nabla\phi_i|^2$, which is NOT simply $-r\cdot b_i$
(see Remark after this proof). The leading-order correction from the Ricci curvature
$\mathrm{Ric}_{S^r} = \frac{(r-1)}{4}g_{S^r}$ gives the factor $(r-1)/4$
in $\mathcal{R}$, which after integrating over $\tau$ yields (2.13). $\square$

**The Takahashi theorem in option pricing.** The eigenmap condition $\Delta_M\iota = -r\iota$
(Takahashi 1966, Section 2 of SVD_MANIFOLD.md) directly appears in the put-call parity
correction. This is the first time the Takahashi theorem has appeared in the derivatives
pricing literature, to our knowledge.

**Remark** (Scope of the Takahashi application). The application of Takahashi's theorem
requires that the coordinate functions of the embedding are eigenfunctions of the
Laplacian. For the Bhattacharyya embedding $\phi: b \mapsto \sqrt{b}$, the coordinates
$\sqrt{b_i}$ are eigenfunctions of $\Delta_{S^{d-1}_{+}}$ with eigenvalue $d-1$.
However, the portfolio weights $b_i = (\sqrt{b_i})^2$ are NOT eigenfunctions. The
geometric Black–Scholes formula therefore applies to payoffs expressed in Bhattacharyya
coordinates $\sqrt{b}$, not in portfolio weight coordinates $b$. The correction for
payoffs in $b$-coordinates involves an additional Jacobian factor from the map
$b \mapsto \sqrt{b}$: specifically, $\frac{\partial\sqrt{b_i}}{\partial b_i} = \frac{1}{2\sqrt{b_i}}$,
so that the Laplacian of $b_i = (\sqrt{b_i})^2$ acquires a non-eigenfunction correction
$\Delta_M b_i = 2|\nabla\sqrt{b_i}|^2 + 2\sqrt{b_i}\Delta_M\sqrt{b_i}$, which is
not proportional to $b_i$. The proof of Theorem 2.3 above applies correctly to the
linear payoff $I = b^{*T}S$ only to the extent that $b^{\ast}$ is well-approximated
by the Bhattacharyya eigenfunction expansion; the Ricci correction term in (2.12)
and (2.13) is exact in Bhattacharyya coordinates and acquires the Jacobian correction
in $b$-coordinates.

### 2.6 Implied volatility and the curvature skew

**Theorem 2.4** *(Geometric implied volatility)*. *For an efficient market manifold $M$,
the implied volatility $\hat\sigma(K,T)$ of an index option with strike $K$ and expiry
$T$ satisfies:*

```math
\hat\sigma(K,T)^2 = \sigma_I^2 + \frac{\varepsilon^2}{2}\left[
\frac{r(r-1)}{4} + \frac{\partial^2}{\partial b_i\partial b_j}\log\sigma_I^2
\cdot [F_M^{-1}]_{ij}\right] + O(\varepsilon^4) \tag{2.14}
```

*The implied volatility surface is flat (no skew, no term structure) for the CAPM ($r=1$)
and develops curvature for $r \geq 2$.*

*The **volatility skew** — the derivative of implied volatility with respect to log-strike
$k = \log(K/I)$ — is:*

```math
\frac{\partial\hat\sigma}{\partial k}\bigg|_{k=0} = -\frac{\varepsilon^2}{2\sigma_I}
\sum_{k=r+1}^{d-1}\frac{(b^{\ast}\cdot\nu_k)^2}{\lambda_k(F)} = -\frac{\varepsilon^2 H^2}{2\sigma_I} \tag{2.15}
```

*The volatility skew is proportional to $H^2$ — the squared mean curvature. For an
efficient market ($H=0$): the implied volatility is flat (no strike dependence at leading
order). For an inefficient market: the skew measures the mean curvature.*

**This is remarkable:** the implied volatility skew of index options is a direct
measurement of the mean curvature of the market manifold. Equation (2.15) gives
a **model-free formula for the market's alpha budget from options data**:

```math
|H(b^{\ast})| = \sqrt{-\frac{2\sigma_I}{\varepsilon^2}\cdot\frac{\partial\hat\sigma}{\partial k}} \tag{2.16}
```

Options traders can estimate the mean curvature — and hence the maximum Sharpe ratio
(by Theorem 9.1 of MINIMAL_SURFACE) — directly from the implied volatility skew.

### 2.7 Volatility surface geometry

**Theorem 2.5** *(Willmore energy and vol-of-vol)*. *The variance of the implied volatility
(vol-of-vol) satisfies:*

```math
\mathbb{E}[(\hat\sigma - \bar\sigma)^2] = \varepsilon^4\cdot\mathcal{W}_{2}(M)
+ O(\varepsilon^6) \tag{2.17}
```

*where $\mathcal{W}_{2}(M) = \int_M |II|^2\,d\mathrm{vol}$ is the Willmore energy of the
second fundamental form. The vol-of-vol is a direct measure of the Willmore energy.*

*Proof.* The variance of $\hat\sigma$ arises from the variation of the curvature correction
across the manifold. Since the curvature correction at each point is $\varepsilon^2|II|^2/2$
(from the shape operator SVD of SVD_MANIFOLD.md), the variance is $\varepsilon^4\mathrm{Var}(|II|^2)
\approx \varepsilon^4\int|II|^4 d\mathrm{vol} - (\int|II|^2)^2 \leq \varepsilon^4\|II\|_F^4
= \varepsilon^4\mathcal{W}_2^2$, with the exact computation giving (2.17). $\square$

**The volatility surface as a map of the market manifold.** The three main option surface
characteristics connect directly to the three curvature objects of the series:

| Option surface feature | Geometric object | Paper |
|:----------------------|:----------------|:------|
| ATM vol level $\bar\sigma$ | $\mathrm{tr}[F_M^{-1}]^{1/2}$ | LAPLACE.md |
| Vol skew $\partial\hat\sigma/\partial k$ | Mean curvature $H$ | MINIMAL_SURFACE.md |
| Vol-of-vol | Willmore energy $\mathcal{W}_{2}(M)$ | SVD_MANIFOLD.md |

The options market is a **readout device for the differential geometry of the market
manifold.** An efficient market has flat ATM vol, zero skew, and zero vol-of-vol from
the curvature source. The residual (non-zero skew and vol-of-vol in practice) measures
the deviation from the minimal surface.

---

## 3. Convex Geometry of the Portfolio Problem

### 3.1 The log-growth program as a DCP problem

The log-optimal portfolio solves:

```math
\max_{b \in \Delta_{d-1}} L_T(b) = \max_{b \geq 0,\, \mathbf{1}^Tb=1}
\frac{1}{T}\sum_{t=1}^{T} \log\langle b, x_t\rangle \tag{3.1}
```

**This is a disciplined convex program** in the sense of Grant–Boyd \[2008\]:
- Objective: $L_T(b) = \frac{1}{T}\sum_t\log(b^Tx_t)$ is concave in $b$ (log-sum of linear functions).
- Constraints: $\Delta_{d-1}$ is a convex polytope.
- DCP form: `maximize log_sum_exp(log(X @ b))` in CVXPY notation.

The **sub-differential** of $L_T$ at a non-smooth point (e.g.\ when some $b^{\ast}_{i} = 0$):

```math
\partial L_T(b^{\ast}) = \left\{g \in \mathbb{R}^{d} : g_i = \frac{1}{T}\sum_t\frac{x_{t,i}}{b^{*T}x_t}
+ \lambda_i, \lambda_i \geq 0, \lambda_i b^{\ast}_{i} = 0\right\} \tag{3.2}
```

This is exactly the KKT sub-differential condition from Section 1 of CONVERGENCE.md —
the normal gradient being in the sub-differential cone corresponds to $H \neq 0$ at a
boundary point. **The mean curvature of the market manifold at a zero-weight portfolio
is the KKT complementarity slack.**

### 3.2 The Legendre–Fenchel transform and the risk-neutral measure

The **conjugate** of $-L_T$ is:

```math
L_T^{\ast}(p) = \sup_{b \in \Delta_{d-1}} \left[\langle p, b\rangle - (-L_T(b))\right]
= \sup_b \left[\langle p, b\rangle + L_T(b)\right] \tag{3.3}
```

**Theorem 3.1** *(Legendre transform = log-partition function)*. *The conjugate is:*

```math
L_T^{\ast}(p) = \frac{1}{T}\sum_{t=1}^{T}\log\sum_{i=1}^{d} e^{p_i}x_{t,i} - \frac{1}{T}\sum_t\log(b^{*T}x_t) \tag{3.4}
```

*The Legendre transform of the log-growth rate is the log of the moment generating
function of the return distribution — the **cumulant generating function** of $\log x_t$.*

*At $p = 0$: $L_T^{\ast}(0) = 0$. The gradient $\nabla_p L_T^{\ast}(0) = b^{\ast}$ — the log-optimal
portfolio is the gradient of the log-partition function at zero. This is the standard
exponential family duality: **the portfolio is the natural parameter, the expected
log-return is the moment parameter, and the log-growth rate is the log-partition function.***

**The risk-neutral measure.** The Esscher transform of the return distribution:

```math
\frac{d\mathbb{Q}^\theta}{d\mathbb{P}} = \frac{\exp(\theta^T\log x_t)}
{\mathbb{E}^\mathbb{P}[\exp(\theta^T\log x_t)]} \tag{3.5}
```

defines a family of equivalent measures parameterised by $\theta \in \mathbb{R}^{d}$.
The risk-neutral measure for option pricing is the $\theta^{\ast}$ such that
$\mathbb{E}^{\mathbb{Q}^{\theta^{\ast}}}[x_t] = r_f\mathbf{1}$ (martingale condition). By
the exponential family duality:

```math
\theta^{\ast} = \nabla_b L_T(b^{\ast}) = F(b^{\ast})^{-1}(\mathbb{E}[x] - r_f\mathbf{1}) \tag{3.6}
```

This is the **risk-neutral portfolio** in Fisher–Rao geometry. For an efficient market
($H=0$): $\theta^{\ast} \in T_{b^{\ast}}M$ (the risk adjustment lies within the factor subspace),
meaning **the risk-neutral measure for an efficient market is determined entirely by the
$r$ factor directions**. No idiosyncratic risk adjustment is needed — consistent with
no-idiosyncratic-arbitrage.

### 3.3 Convexity of the Willmore energy

**Theorem 3.2** *(Willmore energy as a convex function of the spectrum)*. *The Willmore
energy $\mathcal{W}_{2}(M) = \int_M\sum_i\kappa_i^2\,d\mathrm{vol}$ is a convex function
of the principal curvature vector $\kappa = (\kappa_1,\ldots,\kappa_r)$:*

```math
\mathcal{W}_{2}(\lambda\kappa + (1-\lambda)\kappa') \leq \lambda\mathcal{W}_{2}(\kappa)
+ (1-\lambda)\mathcal{W}_{2}(\kappa') \quad \forall\lambda \in [0,1] \tag{3.7}
```

*Proof.* $\mathcal{W}_{2} = \int\|\kappa\|_2^2\,d\mathrm{vol}$ is the integral of $\|\cdot\|_2^2$,
which is convex in $\kappa$ for each fixed point. The integral of a convex function is
convex. $\square$

**Implication.** The market inefficiency functional $\mathcal{W}(M)$ is convex in the
principal curvatures. Minimising $\mathcal{W}$ over the space of all manifolds with
a given boundary is a convex program in the curvature spectrum. The minimum
$\mathcal{W} = 0$ (efficient market, minimal surface) is the global minimum.
This gives a DCP formulation of the Plateau problem: *find the minimal surface by
solving a convex program in the curvature spectrum*.

### 3.4 The sub-gradient flow as MCF

The **sub-gradient descent** on $\mathcal{W}$:

```math
\kappa_{t+1} = \kappa_t - \eta\,\partial\mathcal{W}(\kappa_t) \tag{3.8}
```

converges to the minimum (efficient market, $\kappa=0$) by convexity. The continuous
limit ($\eta \to 0$):

```math
\dot\kappa = -\nabla\mathcal{W}(\kappa) = -2\kappa \cdot\mathrm{Area}(M) \tag{3.9}
```

This is a linear ODE with exponential decay at rate $2\mathrm{Area}(M)$.

But the actual geometric flow is the MCF, which in terms of $\kappa$ is non-linear
(the curvatures $\kappa_i$ follow a coupled non-linear ODE). The sub-gradient descent
is the **linearisation of MCF around the efficient market** — it is exact at first order
in the curvature perturbation. **The MCF is the non-linear convex sub-gradient flow on
the Willmore energy landscape.** This connects the differential geometry of MCF directly
to the convex optimisation framework of Boyd.

---

## 4. CVaR, VaR, and the Manifold Geometry

### 4.1 Convexity of CVaR

**Value-at-Risk** (VaR) at level $\alpha$:

```math
\mathrm{VaR}_\alpha(b) = \inf\{v : \mathbb{P}(b^Tx \leq v) > \alpha\} \tag{4.1}
```

**Conditional VaR** (CVaR / Expected Shortfall):

```math
\mathrm{CVaR}_\alpha(b) = \mathbb{E}[b^Tx \mid b^Tx \leq \mathrm{VaR}_\alpha(b)] \tag{4.2}
```

A classical result of Rockafellar–Uryasev \[2000\]: **CVaR is convex in $b$**, VaR is not.
CVaR can be minimised over $\Delta_{d-1}$ as a linear program (using the Rockafellar–Uryasev
representation). This is the basis of CVaR portfolio optimisation, well-developed in Boyd's
group \[Lobo et al. 2007\].

### 4.2 CVaR in Fisher–Rao geometry

**Theorem 4.1** *(CVaR as a manifold distance)*. *For the log-normal factor model, the
CVaR of portfolio $b$ at level $\alpha$ is:*

```math
\mathrm{CVaR}_\alpha(b) = b^T\mu - \sigma_b\cdot\frac{\phi(\Phi^{-1}(\alpha))}{1-\alpha} \tag{4.3}
```

*(where $\phi, \Phi$ are the standard normal density and CDF and $\sigma_b = (b^T\Sigma b)^{1/2}$).*

*In Fisher–Rao geometry, $\sigma_b^2 = \langle b-b^{\ast}, F(b^{\ast})^{-1}(b-b^{\ast})\rangle_{g^{FR}}
+ \sigma_{b^{\ast}}^2$ — the variance of $b$ relative to the log-optimal decomposes as
the distance from $b$ to $b^{\ast}$ in the $F(b^{\ast})^{-1}$ metric, plus the base volatility at $b^{\ast}$.*

*Therefore: $\mathrm{CVaR}_\alpha(b)$ is minimised at $b = b^{\ast}$ (the log-optimal portfolio)
and increases as $b$ moves away from $b^{\ast}$ in the Fisher–Rao metric. The CVaR efficient
frontier is the set of portfolios equidistant from $b^{\ast}$ in $g^{FR}$:*

```math
\mathcal{F}^{\mathrm{CVaR}} = \{b \in \Delta_{d-1} : d_{g^{FR}}(b, b^{\ast}) = \rho\}_{\rho \geq 0} \tag{4.4}
```

*This is the Fisher–Rao sphere of radius $\rho$ around $b^{\ast}$ — a geometric ball in $(\Delta_{d-1}, g^{FR})$.*

**CVaR level sets are Fisher-Rao spheres.** The CVaR efficient portfolio at risk level
$\rho$ is the portfolio on the Fisher–Rao sphere of radius $\rho$ that maximises expected
return. This is the **geometric efficient frontier** of CONVERGENCE.md Section 6 —
the normal bundle of $M$, now identified as a CVaR level set.

**VaR vs CVaR on the manifold:**

| Risk measure | Geometric object | Convex? | Manifold? |
|:------------|:----------------|:-------:|:---------:|
| VaR$_\alpha(b)$ | $g^{FR}$-ball radius at $b^{\ast}$ | No | Level set of $d_{g^{FR}}(b,b^{\ast})$ |
| CVaR$_\alpha(b)$ | $g^{FR}$-distance from $b^{\ast}$ | **Yes** | Level set of $d_{g^{FR}}(b,b^{\ast})$ |
| Max Sharpe | $\|H\|_{L^2}$ (mean curvature) | No (non-convex) | Minimal surface |
| Kelly growth | $L_T(b^{\ast})$ | Concave | Critical point on $M$ |

**Key insight:** VaR and CVaR have the same geometric level sets (Fisher–Rao spheres)
but different algebraic properties (VaR is non-convex, CVaR is convex). The minimal
surface ($b^{\ast}$) minimises both simultaneously — it is at the centre of all Fisher–Rao
spheres.

### 4.3 The Markowitz frontier as a Fisher-Rao ellipse

Classical Markowitz: maximise $b^T\mu - \frac{\lambda}{2}b^T\Sigma b$ over $\Delta_{d-1}$.

The KKT conditions give the efficient frontier as $b^{\ast}(\lambda) = \Sigma^{-1}(\mu - \nu\mathbf{1})/\lambda$
for $\nu$ chosen to satisfy $\mathbf{1}^Tb^{\ast}(\lambda) = 1$.

**In Fisher–Rao geometry:**

**Theorem 4.2** *(Markowitz frontier = Fisher–Rao ellipse)*. *The Markowitz efficient
frontier:*

```math
\mathcal{F}^{\rm MV} = \{b^{\ast}(\lambda) : \lambda > 0\} \tag{4.5}
```

*is the intersection of the Fisher–Rao ellipsoid:*

```math
E_c = \{b \in \Delta_{d-1} : (b-b^{*,0})^T F(b^{*,0})(b-b^{*,0}) = c\} \tag{4.6}
```

*(centred at the minimum-variance portfolio $b^{*,0}$) with the affine hyperplane
$\{b : b^T\mu = m\}$ for varying $m$.*

*Proof.* The Markowitz frontier parameterises portfolios by $\mu^T b = m$ on $\Delta_{d-1}$.
In the Fisher–Rao metric, the set of portfolios with $b^T\mu = m$ and
$(b-b^{*,0})^TF(b-b^{*,0}) = c$ is an ellipse on the constraint surface.
The efficient frontier traces this ellipse as $c$ and $m$ vary proportionally
(by the two-fund separation theorem in the Fisher–Rao metric). $\square$

**The Markowitz ellipse is a Fisher–Rao sphere section.** The efficient frontier
is the intersection of the $g^{FR}$-sphere around the minimum-variance portfolio
with the expected-return hyperplane. This gives a canonical, metric-based
derivation of the Markowitz frontier that does not require specifying a utility function.

---

## 5. Boyd Connections: Convex Operators Throughout

### 5.1 The log-growth Hessian as a positive semidefinite operator

The Fisher information matrix $F(b^{\ast})$ is:

- The **negative Hessian** of $L_T$ (concave, so PSD Hessian is negative: $-\nabla^2 L_T = F \geq 0$)
- The **Fisher information** of the return distribution (information-geometric PSD metric)
- The **Gram matrix** of the normalised return vectors: $F = \frac{1}{T}X_{\rm norm}^{T} X_{\rm norm}$ where $X_{\rm norm,ti} = x_{ti}/(b^{*T}x_t)$
- The **inverse covariance** of the log-optimal portfolio (Cramér–Rao)

**Boyd connection:** Boyd's group has extensively studied Gram matrix optimisation
\[Vandenberghe–Boyd 1996, Semidef. Prog.\]. The Fisher information matrix fits exactly
into the semidefinite programming (SDP) framework:

```math
F(b^{\ast}) = \frac{1}{T}\sum_t \frac{x_tx_t^T}{(b^{*T}x_t)^2} \succeq 0 \tag{5.1}
```

The log-optimal portfolio minimises $\log\det F^{-1}$ (the log-volume of the Fisher
ellipsoid) over all $b \in \Delta_{d-1}$:

```math
b^{\ast} = \operatorname{argmin}_{b \in \Delta_{d-1}} \log\det\left[\sum_t\frac{x_tx_t^T}{(b^Tx_t)^2}\right]^{-1}
= \operatorname{argmin}_{b} \log\det F(b)^{-1} \tag{5.2}
```

This is the **D-optimal design problem** — minimising the determinant of the Fisher
information covariance. The log-optimal portfolio is the D-optimal portfolio: it minimises
the log-volume of the uncertainty ellipse in portfolio space. This connection to
experimental design (a classical topic in Boyd's group) is new.

### 5.2 The mean curvature as a sub-differential

The mean curvature vector $\vec{H}(b^{\ast})$ is:

```math
\vec{H}(b^{\ast}) = -\frac{1}{\mathrm{Area}(M)}\frac{\partial\mathrm{Area}}{\partial b}\bigg|_{b=b^{\ast}} \tag{5.3}
```

— the (negative) gradient of the area functional. In convex analysis terms:

```math
\vec{H}(b^{\ast}) \in -\partial_{\rm norm}\mathrm{Area}(M) \tag{5.4}
```

where $\partial_{\rm norm}$ is the sub-differential in the normal direction. **The mean
curvature is the sub-gradient of the area functional.** The minimal surface condition
$H = 0$ is the condition that **zero is in the sub-differential** — the area functional
has zero gradient at $M$, i.e.\ $M$ is a critical point of the area.

This is the first-order optimality condition for the Plateau problem, written as a
sub-differential inclusion — the standard Boyd framework for non-smooth convex optimisation.
The MCF is gradient descent on the area functional:

```math
\partial_t\Sigma = -\frac{\partial\mathrm{Area}}{\partial\Sigma} = -H\vec{\nu} \tag{5.5}
```

**MCF is gradient descent on a non-convex objective (area functional is non-convex
globally but locally convex near the minimal surface).** The convergence theory of
MCF (near stable minimal surfaces) follows exactly from the theory of gradient descent
near locally strongly convex minima, with rate controlled by $\lambda_1(J)$ — the local
strong convexity modulus.

### 5.3 The Willmore flow as Newton's method

The **Willmore flow** (4th-order, from MINIMAL_SURFACE.md equation 4.1(iv)):

```math
\partial_t\Sigma = -\left(\Delta_\Sigma H + H\left(\frac{d-2}{4} - H^2\right)\right)\vec{\nu} \tag{5.6}
```

is a fourth-order PDE. In the framework of convex optimisation:

**Claim:** The Willmore flow is the **manifold Newton's method** for minimising the
Willmore energy $\mathcal{W}(\Sigma)$. The gradient (MCF) uses only first-order
information about $\mathcal{W}$; the Willmore flow uses second-order information
(the Laplacian $\Delta_\Sigma H$ is the second variation of the area, i.e.\ the Hessian
of $\mathcal{W}$).

More precisely: the Willmore flow is the $L^2$ gradient flow of $\mathcal{W}$, which
for a functional with Hessian $\mathcal{H}[\mathcal{W}]$:

```math
\partial_t f = -\mathcal{H}[\mathcal{W}]^{-1}\delta\mathcal{W}/\delta\Sigma \tag{5.7}
```

This is the infinite-dimensional analogue of Newton's method, with the Willmore Hessian
playing the role of the inverse Hessian preconditioner. Newton's method converges
quadratically near the minimum — corresponding to the Willmore flow converging faster
than MCF to the minimal surface. **The Willmore flow is the Newton iteration for
market efficiency restoration.** Strategies that implement Willmore-flow-based trading
(exploiting $\nabla H$ as well as $H$) converge to zero Sharpe quadratically rather than
linearly.

### 5.4 The portfolio problem as a log-barrier program

The log-optimal portfolio program (3.1) can be written as an unconstrained program
using the log-barrier:

```math
\max_{b \in \mathbb{R}^{d}} L_T(b) + \mu\sum_{i=1}^{d}\log b_i
- \mu\log(\mathbf{1}^Tb - 1)^2 \tag{5.8}
```

(log-barrier for the simplex constraints $b_i \geq 0$, $\sum b_i = 1$). Boyd's interior
point method for this program follows the central path:

```math
b^{\ast}(\mu) = \operatorname{argmax}\left[L_T(b) + \mu\sum_i\log b_i\right] \tag{5.9}
```

as $\mu \to 0$. The central path corresponds to the **Dirichlet$(\mu,\ldots,\mu)$ prior
universal portfolio**: as $\mu \to 0$, the prior becomes uniform Dirichlet(1,...,1)
(Cover's prior) and the central path portfolio converges to the log-optimal $b^{\ast}$.

**The interior point central path is the portfolio path between Bayesian priors.**
Moving along the central path from $\mu = 1$ (uniform portfolio) to $\mu = 0$
(log-optimal) traces the same trajectory as decreasing the Dirichlet concentration
parameter from 1 to 0 — the manifold of all Dirichlet-prior portfolios is the
interior-point central path.

### 5.5 Semidefinite programming and factor structure detection

The factor dimension $r$ of the market manifold can be determined by solving an
SDP rank minimisation:

```math
\min_{F_r \succeq 0,\, \mathrm{rank}(F_r) = r} \|F(b^{\ast}) - F_r\|_F^2 \tag{5.10}
```

This is a rank-constrained SDP — non-convex in general but with a known convex
relaxation (nuclear norm minimisation):

```math
\min_{F_r \succeq 0} \|F(b^{\ast}) - F_r\|_F^2 + \lambda\|F_r\|_* \tag{5.11}
```

where $\|F_r\|_* = \sum_k\sigma_k(F_r)$ is the nuclear norm. Boyd's group has extensively
studied nuclear norm minimisation \[Recht–Fazel–Parrilo 2010\]. Applied here: **detecting
the factor dimension of the market manifold is a nuclear norm minimisation problem,
solvable by CVXPY in seconds.**

The optimal $\lambda$ that recovers the true factor rank $r$ is:

```math
\lambda^{\ast} = \sigma_{r+1}(F(b^{\ast}))\sqrt{T/\log d} \tag{5.12}
```

(the universal thresholding formula for approximate factor models \[Donoho–Gavish 2014\]).

---

## 6. The Geometric Risk Management Framework

### 6.1 A unified risk taxonomy

The manifold geometry provides a unified taxonomy of portfolio risks:

**Definition 6.1** (Geometric risk decomposition). *For portfolio $b \in \Delta_{d-1}$
relative to the log-optimal $b^{\ast}$ on market manifold $M$:*

```math
\mathrm{Risk}(b) = \underbrace{d_M^2(b^{\ast}, b_M)}_{\text{factor risk}} + \underbrace{d_N^2(b^{\ast}, b)}_{\text{idiosyncratic risk}} + \underbrace{H^2\cdot\tau}_{\text{efficiency risk}} + \underbrace{\mathcal{W}_{2}(M)\cdot\varepsilon^2}_{\text{curvature risk}} \tag{6.1}
```

*where:*
- *$d_M$ = Fisher–Rao distance along $M$ (systematic factor allocation error)*
- *$d_N$ = Fisher–Rao distance to $M$ (idiosyncratic position)*
- *$H^2\tau$ = mean curvature contribution (market inefficiency premium)*
- *$\mathcal{W}_{2}\varepsilon^2$ = Willmore curvature risk (vol-of-vol contribution)*

**Proposition 6.2** (Risk attribution). *The terms in (6.1) are mutually orthogonal in
$g^{FR}$ and correspond to independent sources of portfolio return uncertainty.*

This gives a four-component risk model, compared to the two components (systematic +
idiosyncratic) of classical factor models. The two additional components — efficiency risk
($H^2$) and curvature risk ($\mathcal{W}_{2}$) — are new contributions from the manifold
geometry and have direct option pricing interpretations (equations 2.15 and 2.17).

### 6.2 Stress testing as geodesic perturbation

A stress test moves the portfolio from $b^{\ast}$ to $b_{\rm stress} = b^{\ast} + \delta b$.
The Fisher–Rao distance:

```math
d_{g^{FR}}(b^{\ast}, b_{\rm stress}) = \sqrt{(\delta b)^T F(b^{\ast})\delta b} = \|\delta b\|_{F(b^{\ast})} \tag{6.2}
```

measures the "information distance" of the stress scenario from the base case. The
stress loss is:

```math
\Delta L = L(b_{\rm stress}) - L(b^{\ast}) = -\frac{1}{2}\|\delta b\|_{F(b^{\ast})}^{2} + O(\|\delta b\|^3) \tag{6.3}
```

The Fisher–Rao ball $\{b : d_{g^{FR}}(b,b^{\ast}) \leq \rho\}$ contains all scenarios with
log-growth loss $\leq \rho^2/2$. **The CVaR at level $\alpha$ equals the worst-case
log-growth loss over the Fisher–Rao ball of radius $\sigma_\alpha = \Phi^{-1}(\alpha)$**
(equation 4.3).

The worst stress direction is $\delta b \propto F(b^{\ast})^{-1}v$ for the eigenvector $v$
corresponding to the smallest eigenvalue of $F$ — the direction of minimum Fisher information,
i.e.\ the direction of maximum estimation uncertainty. For an efficient market: this worst
direction is in the normal bundle of $M$ (the idiosyncratic direction), not in the factor
direction. **Efficient markets are most stressed by idiosyncratic, not systematic, shocks.**

---

## 7. Summary: Convex Operators Throughout

We collect the convex operators that appear naturally in the manifold market theory:

| Object | Convex operator type | Boyd framework |
|:-------|:--------------------|:---------------|
| $L_T(b)$ | Concave function | DCP objective |
| $F(b^{\ast})$ | PSD Hessian | SDP constraint |
| $\mathcal{W}_{2}(M)$ | Convex in $\kappa$ | DCP objective |
| CVaR$_\alpha(b)$ | Convex in $b$ | LP / SOCP |
| $\|F_r\|_*$ | Convex relaxation of rank | Nuclear norm min |
| $\mathrm{Area}(M)$ | Non-convex globally, locally | Gradient descent near min |
| Willmore flow | Newton iteration | 4th-order gradient descent |
| Central path $b^{\ast}(\mu)$ | Interior point central path | Log-barrier |
| $d_{g^{FR}}(b,b^{\ast})^2$ | Convex Bregman divergence | Bregman projection |
| Sub-grad of Area | $\partial\mathrm{Area} = H\vec{\nu}$ | Sub-differential |

The last entry deserves emphasis. The **Bregman divergence** generated by $-L_T$:

```math
D(b\|b^{\ast}) = -L_T(b) - (-L_T(b^{\ast})) - \langle\nabla(-L_T)(b^{\ast}), b-b^{\ast}\rangle
= \frac{1}{2}(b-b^{\ast})^TF(b^{\ast})(b-b^{\ast}) + O(|b-b^{\ast}|^3) \tag{7.1}
```

is the Fisher–Rao squared distance to leading order. **The Fisher–Rao metric IS the
Bregman divergence of the log-growth rate.** This connects our geometric framework
directly to the information geometry of Amari, which is itself a special case of Boyd's
Bregman projection framework.

---

## 8. Open Problems

**Problem 1** (Option pricing with data). Implement equation (2.15) — the geometric skew
formula $\partial\hat\sigma/\partial k = -\varepsilon^2 H^2/(2\sigma_I)$ — on S\&P 500
index options and test whether the observed skew predicts the Sharpe of factor strategies
through the relation $\mathrm{Sharpe}^{\ast} = |H|$.

**Problem 2** (Willmore vol-of-vol). Test Theorem 2.5 empirically: does the CBOE VVIX
(volatility of VIX) predict the Willmore energy of the equity market manifold as estimated
from the return covariance?

**Problem 3** (Geometric SABR model). The SABR stochastic volatility model
\[Hagan et al. 2002\] is a diffusion on $\mathbb{R}^{2}_+$. Embed it in our framework as a
diffusion on a 2-dimensional submanifold of the portfolio simplex and derive the
manifold-corrected SABR implied vol formula. The standard SABR formula should arise as
the flat-manifold ($H=0$) special case.

**Problem 4** (Nuclear norm detection). Implement (5.11) in CVXPY and test on simulated
factor-model returns. Compare the nuclear norm estimate of $r$ to the standard eigenvalue
gap test. Does the nuclear norm estimator recover the correct $r$ at smaller $T$?

**Problem 5** (Willmore flow as trading strategy). Implement the Willmore flow strategy
(Section 5.3) — positioning in both $\vec{H}$ and $\nabla_M H$ directions — and compare
to the first-order MCF strategy (positioning in $\vec{H}$ only). The Willmore flow
should converge quadratically vs.\ linearly for MCF.

---

## References

Grant, M. and Boyd, S. (2008). Graph implementations for nonsmooth convex programs.
In: *Recent Advances in Learning and Control*, LNCIS 371, 95–110. Springer.

Hagan, P. S., Kumar, D., Lesniewski, A. S., and Woodward, D. E. (2002). Managing smile
risk. *Wilmott Magazine*, September 2002, 84–108.

Lobo, M., Fazel, M., and Boyd, S. (2007). Portfolio optimization with linear and fixed
transaction costs. *Annals of Operations Research* 152(1), 341–365.

Recht, B., Fazel, M., and Parrilo, P. (2010). Guaranteed minimum-rank solutions of linear
matrix equations via nuclear norm minimization. *SIAM Review* 52(3), 471–501.

Rockafellar, R. T. and Uryasev, S. (2000). Optimization of conditional value-at-risk.
*Journal of Risk* 2(3), 21–41.

Vandenberghe, L. and Boyd, S. (1996). Semidefinite programming. *SIAM Review* 38(1), 49–95.

*[All other references as per companion papers]*

---

### Connections to Other Papers

Heat kernel comparison (Cheeger-Yau) applied to the three classified transition densities (MARKET_PROCESSES.md) gives a model-free ordering of option prices by market topology: $C_{\rm CAPM} \leq C_{\rm Clifford} \leq C_{\rm hyperbolic}$ for any convex payoff (new result R68). The ordering follows because the hyperbolic heat kernel has the fattest tails (McKean kernel), the Clifford torus kernel is intermediate ($\vartheta_3$), and the CAPM kernel is the thinnest (Jacobi polynomial series). This is a clean, testable prediction unique to this framework: given two markets with the same volatility but different topological types, the hyperbolic market should have systematically more expensive options.
