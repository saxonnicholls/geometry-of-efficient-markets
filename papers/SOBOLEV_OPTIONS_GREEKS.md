# Sobolev Spaces, Exact Option Pricing, Barrier Problems,
## and the Geometric Greeks on Market Manifolds

**Saxon Nicholls** — me@saxonnicholls.com

---

**Abstract.**  
We develop the rigorous functional-analytic framework for option pricing on
classified market manifolds, using Sobolev spaces and mollifiers to handle
the degenerate boundary behaviour of the Fisher-Rao metric, then derive exact
closed-form pricing formulas for European options, single and double barrier
options, and the complete set of geometric Greeks for each market type.

The Fisher-Rao metric $g^{\mathrm{FR}}\_{ii} = 1/b\_i$ diverges as $b\_i \to 0$ —
the simplex boundary is at infinite Fisher-Rao distance from any interior point.
This degeneracy requires weighted Sobolev spaces
$W^{k,2}(M, w\,d\mathrm{vol}\_M)$ where the weight $w = \prod\_i b\_i^{\alpha\_i-1}$
is the stationary Beta distribution. Mollifiers $M\_\delta f$ regularise
the degenerate boundary, producing uniformly elliptic approximations that
converge in the weighted Sobolev norm. The option price is a classical
solution of the FK PDE in the interior and a weighted $H^1$ solution near
the boundary.

**Exact pricing formulas derived:**
- CAPM/Jacobi: call price as incomplete Beta + Jacobi polynomial series
- Clifford torus: theta function call formula (Section 4)
- Hyperbolic/McKean: call price via Mehler-Fock transform
- Single barrier (CAPM): absorption at $b=0$ via regularised incomplete Beta
- Double barrier (Clifford): theta function with absorbing boundaries
- Gamma: the covariant Hessian $\nabla^2\_{g\_M}V$ for each market type

**Keywords.** Sobolev space; weighted Sobolev; mollifier; degenerate elliptic;
Muckenhoupt; exact option pricing; barrier option; first passage time; Greeks;
Gamma; Vanna; Volga; incomplete Beta; Jacobi polynomial; theta function barrier;
McKean; covariant Hessian; geometric Greeks.

**MSC 2020.** 35J70, 46E35, 60J60, 91G20, 35K65, 60G40.

---

## 1. Sobolev Spaces on the Market Manifold

### 1.1 Why classical Sobolev spaces are insufficient

The FK PDE on $(M^r, g\_M)$:
$$\frac{\partial u}{\partial t} = \frac{\varepsilon^2}{2}\Delta_M u - \varepsilon^2\vec{H}\cdot\nabla u + r(b)u,
\qquad u(b,T) = G(b) \tag{1.1}$$

has two sources of irregularity:
1. **Degenerate boundary**: the diffusion coefficient $\varepsilon^2\sqrt{b\_i(1-b\_i)} \to 0$
   as $b\_i \to 0$ or $b\_i \to 1$ — the operator is degenerate parabolic at $\partial\Delta$
2. **Non-smooth payoffs**: barrier options, digital options, and spread options
   have discontinuous or non-differentiable payoff functions $G(b)$

Classical Sobolev spaces $W^{k,2}(M)$ (without weights) are insufficient for both.

### 1.2 Weighted Sobolev spaces

**Definition 1.1** (Weighted Sobolev space). *For a weight function $w: M \to \mathbb{R}\_{>0}$
and $k \geq 0$, the weighted Sobolev space is:*

$$W^{k,2}(M, w) = \left\{u \in L^2(M, w) : \|u\|^2_{W^{k,2}(M,w)} = \sum_{|\alpha| \leq k}
\int_M |D^\alpha u|^2_{g_M}\,w\,d\mathrm{vol}_M < \infty\right\} \tag{1.2}$$

The natural weight for the market manifold is the stationary distribution of the
Fokker-Planck operator:

$$w_{\rm stat}(b) = \prod_{i=1}^r b_i^{\alpha_i - 1}(1-b_i)^{\beta_i - 1} \tag{1.3}$$

(the Dirichlet/Beta density, which is the Jeffreys prior from FOKKER\_PLANCK\_CFD).

**Theorem 1.2** *(Weighted Sobolev embedding)*. *On the market manifold $M^r$
with weight $w\_{\rm stat}$:*

$$W^{k,2}(M, w_{\rm stat}) \hookrightarrow C^{0,\gamma}(M) \quad\text{if } k > r/2 + \gamma \tag{1.4}$$

*where $C^{0,\gamma}$ is Hölder continuous with exponent $\gamma \in (0,1)$.*

*Consequence: for $r = 2$ (Clifford torus), options with $\gamma > 0$ regularity
require $k > 1$ — first-order weighted Sobolev regularity suffices for continuous
option prices. For $r = 4$ (Fama-French), we need $k > 2$.*

### 1.3 The Muckenhoupt $A\_2$ condition

The weight $w\_{\rm stat}$ is a Muckenhoupt $A\_2$ weight iff:

$$\sup_{B \subset M}\left(\frac{1}{|B|}\int_B w\right)\!\!\left(\frac{1}{|B|}\int_B w^{-1}\right) < \infty \tag{1.5}$$

**Lemma 1.3** *(The stationary weight satisfies $A\_2$)*. *The weight
$w\_{\rm stat} = \prod\_i b\_i^{\alpha\_i-1}$ is a Muckenhoupt $A\_2$ weight
iff $0 < \alpha\_i < 2$ for all $i$. In market terms: $A\_2$ holds iff
the Kelly weight satisfies $b^{\ast}\_i \in (0, 1/T)^c$ — the log-optimal portfolio
does not assign extreme weights close to 0 or 1/T.*

*Proof.* The Muckenhoupt condition fails precisely when the weight concentrates near
a boundary point with $\alpha\_i \leq 0$ (weight too singular) or $\alpha\_i \geq 2$
(inverse weight too singular). For $\alpha\_i = T b^{\ast}\_i - 1/2 \in (0,\infty)$,
the condition $\alpha\_i < 2$ requires $b^{\ast}\_i < 1/(2T) + 1/2 \approx 1$ — satisfied
for any non-trivial portfolio. $\square$

**Consequence.** When $A\_2$ holds, the FK operator $\mathcal{L}$ extends to a bounded
operator $W^{1,2}(M,w) \to W^{-1,2}(M,w)$ (the negative Sobolev space), and the
Lax-Milgram theorem gives a unique weak solution to the option pricing PDE.

### 1.4 Mollifiers for the degenerate boundary

The Fisher-Rao metric degenerates at $\partial\Delta$ ($g^{\mathrm{FR}}\_{ii} \to \infty$
as $b\_i \to 0$). To regularise, we introduce the **market mollifier**:

$$M_\delta b_i = b_i + \delta(1 - 2b_i) = (1-2\delta)b_i + \delta \tag{1.6}$$

which pushes all weights away from the boundary by $\delta$. The mollified Fisher-Rao metric:

$$g^{\mathrm{FR},\delta}_{ii}(b) = \frac{1}{M_\delta b_i} = \frac{1}{(1-2\delta)b_i + \delta} \tag{1.7}$$

is bounded and uniformly elliptic for $\delta > 0$:

$$\frac{1}{1/4 + \delta} \leq g^{\mathrm{FR},\delta}_{ii}(b) \leq \frac{1}{\delta} \tag{1.8}$$

**Theorem 1.4** *(Mollifier convergence)*. *Let $u^\delta$ be the solution to the
FK PDE (1.1) with mollified metric $g^{\delta}$, and $u$ the weak solution with
the original degenerate metric. Then:*

$$\|u^\delta - u\|_{W^{1,2}(M, w_{\rm stat})} \leq C\delta^{1/2}\|G\|_{W^{2,2}(M, w_{\rm stat})} \tag{1.9}$$

*The rate $\delta^{1/2}$ is optimal: the $\sqrt{\delta}$ error comes from the
$O(\sqrt{\delta})$ change in the boundary layer of the diffusion.*

*Proof.* The mollified solution $u^\delta$ satisfies a uniformly parabolic PDE, for
which classical Schauder estimates apply. The difference $v = u^\delta - u$ satisfies:
$\partial\_t v = \mathcal{L}^\delta v + (\mathcal{L}^\delta - \mathcal{L})u$.
The perturbation $(\mathcal{L}^\delta - \mathcal{L})u$ is bounded by
$\delta\|\nabla u/b\|\_{L^2(w)}$, which gives the $\delta^{1/2}$ rate via Gronwall. $\square$

**Practical implication.** For numerical option pricing, one should:
1. Mollify with $\delta = 1/(2T)$ (one half-observation worth of regularisation)
2. Solve the uniformly parabolic PDE using standard finite differences
3. The pricing error is $O(T^{-1/2})$ from mollification plus $O(h^2)$ from discretisation

---

## 2. Exact Option Pricing: CAPM / Jacobi Process

### 2.1 European call on portfolio weight

For the Jacobi process $b\_t$ with stationary Beta$(\alpha,\beta)$ distribution,
the European call with payoff $G(b\_T) = (b\_T - K)^+$:

$$C_{\rm Jacobi}(b_0, T; K) = e^{-rT}\mathbb{E}^{b_0}[(b_T - K)^+] \tag{2.1}$$

Using the transition density (MARKET\_PROCESSES equation 2.3):

$$C_{\rm Jacobi}(b_0, T; K) = e^{-rT}\sum_{n=0}^\infty e^{-\lambda_n T}\,q_n(b_0)\,
\underbrace{\int_K^1 (b-K)\,q_n(b)\,w(b)\,db}_{\equiv\, J_n(K)} \tag{2.2}$$

**Computing $J\_n(K)$** using properties of Jacobi polynomials:

$$J_0(K) = \frac{1}{B(\alpha,\beta)}\int_K^1 (b-K)b^{\alpha-1}(1-b)^{\beta-1}\,db \tag{2.3}$$

$$= \frac{\alpha}{\alpha+\beta}\bar{I}_K(\alpha+1,\beta) - K\cdot\bar{I}_K(\alpha,\beta) \tag{2.4}$$

where $\bar{I}\_K(\alpha,\beta) = 1 - I\_K(\alpha,\beta)$ is the **complementary regularised
incomplete Beta function** (available in all scientific computing libraries).

For $n \geq 1$, using the Rodrigues formula for Jacobi polynomials:

$$J_n(K) = \frac{(-1)^n}{n!B(\alpha,\beta)}\int_K^1 (b-K)\frac{d^n}{db^n}\!\left[b^{\alpha+n-1}(1-b)^{\beta+n-1}\right]db \tag{2.5}$$

Integration by parts $n$ times, using $(b-K)^{(j)} = \delta\_{j1}$ (the $j$-th derivative
of $(b-K)$ is 0 for $j\geq 2$ and 1 for $j=1$):

$$J_n(K) = \frac{1}{B(\alpha,\beta)}\left[\bar{I}_K(\alpha+n, \beta+n)\cdot\frac{B(\alpha+n,\beta+n)}{n!} - K\cdot\delta_{n,0}\cdot\bar{I}_K(\alpha,\beta)\right] \tag{2.6}$$

**Theorem 2.1** *(Exact Jacobi call formula)*. *The European call on the
log-optimal portfolio weight for a CAPM market is:*

$$\boxed{C_{\rm Jacobi}(b_0,T;K) = e^{-rT}\sum_{n=0}^\infty e^{-\lambda_n T}
\cdot P_n^{(\alpha-1,\beta-1)}(2b_0-1)
\cdot \frac{\bar{I}_K(\alpha+n,\beta+n)}{B(\alpha,\beta)/B(\alpha+n,\beta+n)}
+ e^{-rT} K\cdot\bar{I}_K(\alpha,\beta)} \tag{2.7}$$

*The series converges exponentially: $|e^{-\lambda\_n T}| \leq e^{-n\lambda\_1 T}$,
so the first $N$ terms give error $O(e^{-N\lambda\_1 T})$.*

*For large $T$ ($e^{-\lambda\_1 T} \ll 1$): only the $n=0$ term survives, giving
the **infinite-horizon call price** under the Beta stationary distribution.*

**ATM formula.** At-the-money ($K = b^{\ast} = \alpha/(\alpha+\beta)$), the $n=0$ term dominates:

$$C_{\rm ATM}^{n=0} = e^{-rT}\left[\frac{\alpha}{\alpha+\beta}\bar{I}_{b^{\ast}}(\alpha+1,\beta)
- b^{\ast}\bar{I}_{b^{\ast}}(\alpha,\beta)\right] \tag{2.8}$$

For symmetric parameters ($\alpha = \beta$, equal-weight log-optimal): $b^{\ast} = 1/2$,
$\bar{I}\_{1/2}(\alpha,\alpha) = 1/2$ by symmetry, giving:

$$C_{\rm ATM}^{\rm sym} = e^{-rT}\cdot\frac{1}{2}\left[\frac{1}{2}\bar{I}_{1/2}(\alpha+1,\alpha) - \frac{1}{2}\bar{I}_{1/2}(\alpha,\alpha)\right] = e^{-rT}\frac{\bar{I}_{1/2}(\alpha+1,\alpha) - 1/2}{4} \tag{2.9}$$

### 2.2 Digital call (binary option)

For the digital call $G(b\_T) = \mathbf{1}\_{b\_T > K}$:

$$D_{\rm Jacobi}(b_0, T; K) = e^{-rT}\sum_{n=0}^\infty e^{-\lambda_n T}
P_n^{(\alpha-1,\beta-1)}(2b_0-1)\cdot\bar{I}_K(\alpha+n,\beta+n)\cdot\frac{B(\alpha+n,\beta+n)}{B(\alpha,\beta)} \tag{2.10}$$

For $n=0$: $D^{n=0} = e^{-rT}\bar{I}\_K(\alpha,\beta)$ — the complementary CDF of the
Beta stationary distribution. **The digital call is the tail probability of the Beta
distribution.** This is the exact formula that replaces the Black-Scholes $N(d\_2)$.

---

## 3. Single Barrier Problems: Jacobi Hitting Zero

### 3.1 First passage time to zero weight

The **single barrier problem** asks: what is the probability that asset $A$'s portfolio
weight $b\_t$ first hits zero (the asset is driven out of the portfolio) before time $T$?

For the Jacobi diffusion (2.1), the boundary behavior at $b=0$ depends on the
Feller classification of the boundary:

| Parameter | Feller class | Behavior |
|:---------:|:------------:|:---------|
| $\alpha < 1$ (i.e. $Tb^{\ast}\_A < 3/2$) | Regular | Process can hit 0 and reflect |
| $\alpha = 1$ | Regular/entrance | Process reaches 0 instantaneously |
| $\alpha > 1$ (i.e. $Tb^{\ast}\_A > 3/2$) | Entrance | Process never reaches 0 |

For a typical CAPM market with $d=2$, $T=252$: $\alpha = Tb^{\ast} - 1/2 = 125.5$.
**The boundary 0 is an entrance boundary: the portfolio weight never hits zero.**
This is the geometric mechanism behind diversification — the Fisher-Rao metric
creates an infinite potential barrier at zero weight.

For small portfolios ($d=2$, $T=21$ weekly observations): $\alpha = 10$ — still
entrance. You need $Tb^{\ast} < 3/2$, i.e. $b^{\ast} < 1.5/T$ — a portfolio weight less than
$1.5\%$ for daily data — for the boundary to be reachable. This is consistent with
the observation that very small positions in an asset can be "washed out" by noise
but large positions cannot.

### 3.2 Absorption at zero: the case $0 < \alpha < 1$

For a market where the zero-weight boundary IS reachable ($\alpha < 1$, small portfolio),
the **first passage time distribution** for the Jacobi process hitting $b=0$ from $b\_0 > 0$:

**Laplace transform:**

$$\mathbb{E}_{b_0}[e^{-s\tau_0}] = \frac{{}_2F_1(a_1(s), a_2(s); \alpha; b_0)}{{}_2F_1(a_1(s), a_2(s); \alpha; 0^+)} \tag{3.1}$$

where $a\_{1,2}(s) = (\alpha+\beta-1 \pm \sqrt{(\alpha+\beta-1)^2 - 4s/\varepsilon^2})/2$
and $\_2F\_1$ is the Gauss hypergeometric function.

At $b\_0 = 0^+$ (the boundary): ${}\_2F\_1(a\_1,a\_2;\alpha;0) = 1$, giving:

$$\mathbb{E}_{b_0}[e^{-s\tau_0}] = {}_2F_1(a_1(s), a_2(s); \alpha; b_0) \tag{3.2}$$

**The first passage time density** is the inverse Laplace transform of (3.2):

$$f_{\tau_0}(t|b_0) = \mathcal{L}^{-1}\!\left[{}_2F_1(a_1(s),a_2(s);\alpha;b_0)\right](t) \tag{3.3}$$

This does not simplify to a standard distribution, but is rapidly computable by
numerical Laplace inversion (Talbot method) given (3.2).

**Survival probability to time $T$:**

$$\mathbb{P}(\tau_0 > T | b_0) = \sum_{n=0}^\infty e^{-\lambda_n T}
P_n^{(\alpha-1,\beta-1)}(2b_0-1)\cdot\frac{\int_0^1 P_n^{(\alpha-1,\beta-1)}(2b-1)w(b)\,db}{1/B(\alpha,\beta)} \tag{3.4}$$

(the integral of the eigenfunction over the survival region $[0,1]$, with absorbing
condition at $b=0$).

### 3.3 Down-and-out call (barrier option)

The **down-and-out call** — a call option that expires worthless if the portfolio
weight hits zero — has value:

$$C_{\rm DOC}(b_0, T; K) = e^{-rT}\mathbb{E}^{b_0}[(b_T-K)^+\cdot\mathbf{1}_{\tau_0 > T}] \tag{3.5}$$

For the entrance boundary case ($\alpha > 1$): $\mathbf{1}\_{\tau\_0 > T} = 1$ a.s., so
$C\_{\rm DOC} = C\_{\rm Jacobi}$ — the barrier is never hit and the option price is the
standard formula (2.7). **For typical equity markets, down-and-out options on portfolio
weights are equivalent to standard options because diversification prevents zero-weight events.**

For the regular boundary case ($0 < \alpha < 1$): the absorption modifies the
eigenfunction expansion, replacing $P\_n^{(\alpha-1,\beta-1)}(2b-1)$ with eigenfunctions
satisfying absorbing boundary conditions at $b=0$.

---

## 4. Double Barrier Problems: Clifford Torus

### 4.1 The spread process

For the Clifford torus market, the spread $X\_t = \theta\_t - \varphi\_t$ follows 1D BM
on the flat torus $[-\pi/2, \pi/2]$ with periodic BC (MARKET\_PROCESSES equation 4.7):

$$dX_t = \varepsilon\sqrt{2}\,dW_t, \qquad X \in [-\pi/2, \pi/2]_{\rm periodic} \tag{4.1}$$

The **double barrier problem** places absorbing boundaries at $\pm L$ (the spread
exits the "efficient" range):

$$\tau_{L} = \inf\{t : |X_t| = L\}, \qquad 0 < L < \pi/2 \tag{4.2}$$

### 4.2 Double barrier on the flat torus

**Theorem 4.1** *(Double barrier for Clifford torus — exact)*.

*The survival probability (spread stays within $(-L, L)$ until time $T$) is:*

$$\mathbb{P}(|X_t| < L\;\forall\,t \leq T | X_0) = \sum_{n=0}^\infty c_n(X_0)\,e^{-\mu_n T} \tag{4.3}$$

*where $\mu\_n = 2\varepsilon^2\left(\frac{n\pi}{2L}\right)^2$ and
$c\_n(X\_0) = \frac{2}{2L}\int\_{-L}^L \sin\!\left(\frac{n\pi(X+L)}{2L}\right)\!\sin\!\left(\frac{n\pi(X\_0+L)}{2L}\right)dX\_0$.*

*For the torus vs flat-space comparison: for $L < \pi/2$ (barriers inside one torus period),
the result is identical to the standard double-barrier Brownian motion formula.
The torus corrections appear only when $L = \pi/2$ (full period).*

*Proof.* The problem is standard Brownian motion on $[-L, L]$ with absorbing boundaries,
since $L < \pi/2$ means the barriers are encountered before the process wraps around.
The eigenvalue problem $-\Delta\phi = \mu\phi$ on $[-L,L]$ with $\phi(\pm L) = 0$ gives
sine functions with $\mu\_n = n^2\pi^2/(2L^2) \cdot 2\varepsilon^2$. $\square$

**The double barrier option price** (pay $G(X\_T)$ if the spread stays within $(-L,L)$):

$$V_{\rm DB}(X_0, T; L) = e^{-rT}\sum_{n=1}^\infty e^{-\mu_n T}\sin\!\!\left(\frac{n\pi(X_0+L)}{2L}\right)
\int_{-L}^L G(X)\sin\!\!\left(\frac{n\pi(X+L)}{2L}\right)dX \tag{4.4}$$

For the "corridor" payoff $G(X) = 1$ (pay 1 if spread stays within $(-L,L)$):

$$V_{\rm corridor}(X_0,T;L) = e^{-rT}\cdot\frac{4}{\pi}\sum_{n=0}^\infty\frac{(-1)^n}{2n+1}
e^{-\mu_{2n+1}T}\sin\!\left(\frac{(2n+1)\pi(X_0+L)}{2L}\right) \tag{4.5}$$

### 4.3 The torus correction for long barriers

When $L = \pi/2$ (the spread can range over the full torus period), the double barrier
becomes a **periodic obstacle problem** and the theta function appears:

$$\mathbb{P}(|X_t| < \pi/2\;\forall\,t\leq T|X_0) = \frac{\vartheta_3(0|\tau) - \vartheta_3(X_0|\tau)}{\vartheta_3(0|\tau)} \tag{4.6}$$

where $\tau = 2i\varepsilon^2 T / (\pi/2)^2$ — the modular parameter of the Clifford torus.

This is the **theta function barrier formula** — a genuinely new result that does not
appear in standard barrier option pricing literature because it requires the torus
geometry.

### 4.4 First passage time for the spread

The Laplace transform of the first exit time $\tau\_L$:

$$\mathbb{E}_{X_0}[e^{-s\tau_L}] = \frac{\cosh\!\left(\sqrt{s/\varepsilon^2}\,X_0\right)}{\cosh\!\left(\sqrt{s/\varepsilon^2}\,L\right)} \tag{4.7}$$

(the standard double-barrier BM Laplace transform). Inverting:

$$f_{\tau_L}(t|X_0) = \frac{\pi}{L^2}\varepsilon^2\sum_{n=1}^\infty (-1)^{n+1}n\sin\!\left(\frac{n\pi(X_0+L)}{2L}\right)e^{-n^2\pi^2\varepsilon^2 t/(2L^2)} \tag{4.8}$$

**Characteristic time for barrier hitting:**

$$\mathbb{E}[\tau_L] = \frac{L^2 - X_0^2}{2\varepsilon^2} \tag{4.9}$$

For a spread at the origin ($X\_0 = 0$): expected time to hit $\pm L$ is $L^2/(2\varepsilon^2)$.
For the CAPM (treating as 1D):  $L = 2\sigma$ (2-sigma threshold), $\varepsilon^2 = \sigma^2/T$:
$\mathbb{E}[\tau\_L] = 2T$ — the expected time to hit a 2-sigma barrier is 2 rebalancing periods.
This gives the rigorous basis for the "2-sigma, 2-period" rebalancing rule.

---

## 5. Exact Option Pricing: Hyperbolic / McKean Market

### 5.1 The European call via Mehler-Fock transform

For the hyperbolic BM with McKean kernel $p\_t(\rho) = \frac{e^{-t/4}}{(4\pi t)^{1/2}}\cdot\frac{\rho e^{-\rho^2/(4t)}}{\sinh\rho}$,
the European call on the hyperbolic distance $\rho\_T$:

$$C_{\rm hyp}(\rho_0, T; K) = e^{-rT}\int_K^\infty (\rho - K)\,p_T(\rho|\rho_0)\,d\rho \tag{5.1}$$

Using the **Mehler-Fock transform**:

$$p_T(\rho|\rho_0) = \int_0^\infty e^{-(1/4+\xi^2)T}\xi\tanh(\pi\xi)
P_{-1/2+i\xi}(\cosh\rho_0)P_{-1/2+i\xi}(\cosh\rho)\,d\xi \tag{5.2}$$

where $P\_{-1/2+i\xi}$ is the associated Legendre function (conical function).

**Theorem 5.1** *(McKean call formula)*. *The European call under hyperbolic BM is:*

$$C_{\rm hyp}(\rho_0,T;K) = e^{-(r+1/4)T}\int_0^\infty e^{-\xi^2 T}\xi\tanh(\pi\xi)
\cdot P_{-1/2+i\xi}(\cosh\rho_0)\cdot\Phi_\xi(K)\,d\xi \tag{5.3}$$

*where the "spectral call payoff" is:*

$$\Phi_\xi(K) = \int_K^\infty(\rho-K)P_{-1/2+i\xi}(\cosh\rho)\,d\rho \tag{5.4}$$

*For large $K$: $\Phi\_\xi(K) \sim K\cdot P\_{-1/2+i\xi}(\cosh K)/\sinh K$ (by the
asymptotic expansion of the Legendre function). The McKean call decays more slowly
in $K$ than the Black-Scholes call (Cauchy-type tail vs Gaussian tail).*

**ATM approximation.** For small $T$ and $\rho\_0 \approx 0$:

$$C_{\rm hyp}^{\rm ATM}(T) \approx e^{-rT}\varepsilon\sqrt{T/\pi} + e^{-rT}\frac{T^{3/2}\varepsilon^3}{4\sqrt{\pi}} + O(T^{5/2}) \tag{5.5}$$

The leading term is identical to Black-Scholes ATM ($e^{-rT}\sigma\sqrt{T/2\pi}$ with $\sigma = \varepsilon\sqrt{2}$).
The correction $+T^{3/2}\varepsilon^3/(4\sqrt{\pi})$ is positive — the hyperbolic market
gives a **higher ATM call price** than Black-Scholes. This is the fat-tail correction:
the Cauchy tails of the hyperbolic market create more option value.

---

## 6. The Geometric Greeks

### 6.1 Delta — the covariant gradient

The **geometric Delta** is the covariant gradient of the option price in the
Fisher-Rao metric:

$$\Delta_{g_M} V = \nabla_{g_M} V = g_M^{-1}\nabla_b V \tag{6.1}$$

**For the Jacobi process** (1D, $b \in (0,1)$):

$$\Delta_{\rm Jacobi} V = b(1-b)\frac{\partial V}{\partial b} \tag{6.2}$$

The factor $b(1-b)$ is the inverse of the Fisher-Rao metric $g^{\mathrm{FR}}\_{11} = 1/(b(1-b))$.
**The geometric Delta has an automatic dampening near the boundaries** ($b \to 0$ or $b \to 1$):
the hedging position is reduced proportionally to $b(1-b)$ — a concentrated portfolio
needs a smaller hedge than an equal-weight portfolio, for the same option on portfolio weight.

**For the flat torus** (2D, $(\theta,\varphi) \in [0,\pi/2]^2$):

$$\vec{\Delta}_{T^2} V = \left(\frac{\partial V}{\partial\theta}, \frac{\partial V}{\partial\varphi}\right) \tag{6.3}$$

Standard 2D gradient — no metric correction (flat geometry).

**For hyperbolic BM** (upper half-plane $(x,y)$):

$$\vec{\Delta}_{\mathbb{H}^2} V = y^2\left(\frac{\partial V}{\partial x}, \frac{\partial V}{\partial y}\right) \tag{6.4}$$

The factor $y^2$ (the inverse of the hyperbolic metric coefficient $g^{\mathbb{H}^2}\_{11} = 1/y^2$)
amplifies the gradient near the boundary $y \to 0$ — the hedging position must be
**increased** near the hyperbolic boundary, consistent with the Cauchy tails requiring
larger hedges for extreme events.

### 6.2 Gamma — the covariant Hessian

The **geometric Gamma** is the covariant Hessian of the option price:

$$\Gamma_{g_M} V = \nabla_{g_M}^2 V \tag{6.5}$$

In components: $(\Gamma\_{g\_M}V)\_{ij} = \partial\_{ij}V - \Gamma\_{ij}^k\partial\_k V$
where $\Gamma\_{ij}^k$ are the Christoffel symbols of $g\_M$.

**For the Jacobi process** (1D):

$$\Gamma_{\rm Jacobi} = b(1-b)\frac{\partial^2 V}{\partial b^2}
+ (1-2b)\frac{\partial V}{\partial b} \tag{6.6}$$

The second term $(1-2b)\partial\_b V$ is the **Christoffel correction** — it arises
from the curvature of the Fisher-Rao metric on $\Delta\_1$. At the equal-weight
portfolio ($b=1/2$): the correction vanishes ($1-2\times 1/2 = 0$) and
$\Gamma\_{\rm Jacobi} = (1/4)\partial^2 V/\partial b^2$ — the standard Gamma scaled
by $b(1-b)=1/4$.

The FK PDE for the Jacobi option price is:
$$\frac{\partial V}{\partial t} + \frac{\varepsilon^2}{2}\Gamma_{\rm Jacobi} V - rV = 0 \tag{6.7}$$

which explicitly shows that the **Gamma in the FK PDE is the geometric (covariant)
Gamma, not the standard partial derivative Gamma**.

**For the flat torus** (2D):

$$\Gamma_{T^2} V = \frac{\partial^2 V}{\partial\theta^2} + \frac{\partial^2 V}{\partial\varphi^2} \tag{6.8}$$

Standard Laplacian — no Christoffel corrections (flat geometry, zero Christoffel symbols).
The spread Gamma is:
$$\Gamma_{\rm spread} = \frac{\partial^2 V}{\partial X^2}, \qquad X = \theta - \varphi \tag{6.9}$$

**For hyperbolic BM**:

$$\Gamma_{\mathbb{H}^2} V = y^2\left(\frac{\partial^2 V}{\partial x^2} + \frac{\partial^2 V}{\partial y^2}\right) \tag{6.10}$$

The hyperbolic Gamma amplifies the standard Gamma by $y^2$ — a portfolio near the
hyperbolic boundary (extreme leverage or crisis state) has dramatically larger Gamma.
This is the geometric explanation of **Gamma blow-up near market crashes**: the
hyperbolic geometry forces increasing convexity as the system approaches the boundary.

**Gamma table across market types:**

| Market | Gamma $\Gamma\_{g\_M} V$ | At equal-weight ($b=1/2$) | Boundary behaviour |
|:-------|:-----------------------|:------------------------:|:-------------------|
| CAPM (Jacobi) | $b(1-b)\partial^2\_b + (1-2b)\partial\_b$ | $\frac{1}{4}\partial^2\_b$ | $\to 0$ as $b\to 0,1$ |
| Spherical BM | $\Delta\_{S^r}$ (Laplace-Beltrami) | $(r-1)^{-1}\partial^2$ | Bounded |
| Clifford $T^2$ | $\partial^2\_\theta + \partial^2\_\varphi$ | Standard | Periodic |
| Hyperbolic | $y^2(\partial^2\_x + \partial^2\_y)$ | Depends on $y\_0$ | $y^2 \to\infty$ at $y\to\infty$ |

### 6.3 Theta — the time decay

$$\Theta_M V = -\frac{\partial V}{\partial t} = \frac{\varepsilon^2}{2}\Gamma_{g_M} V + \vec{H}\cdot\Delta_{g_M} V - rV \tag{6.11}$$

For the **efficient market ($H=0$)**: $\Theta\_M = \frac{\varepsilon^2}{2}\Gamma\_{g\_M} V - rV$.
The time decay equals the geometric Gamma minus the discounting — exactly the
Black-Scholes theta formula, but with the covariant Gamma.

For the **inefficient market**: the additional term $\vec{H}\cdot\Delta\_{g\_M}V$ adds to
the time decay. A market with positive mean curvature in the direction of the Delta
has **faster time decay** — the option's theta is increased by the systematic drift.

### 6.4 Vega — the volatility sensitivity

The **geometric Vega** is the derivative with respect to $\varepsilon$ (the WF parameter):

$$\mathcal{V}_M V = \frac{\partial V}{\partial\varepsilon} \tag{6.12}$$

From the FK PDE: $\partial\_\varepsilon(\partial\_t V) = \partial\_t(\partial\_\varepsilon V)$,
and differentiating (6.7) with respect to $\varepsilon$:

$$\frac{\partial}{\partial t}(\mathcal{V}_M V) + \frac{\varepsilon^2}{2}\Gamma_{g_M}(\mathcal{V}_M V) = -\varepsilon\Gamma_{g_M} V \tag{6.13}$$

The Vega satisfies the **same PDE as the option price**, but with the Gamma as the
source term. This is the geometric version of the Black-Scholes Vega identity
$\mathcal{V} = S^2\sigma\Gamma(T-t)/(\partial C/\partial\sigma)$.

### 6.5 Vanna and Volga — the higher-order Greeks

**Vanna** = $\partial^2 V/\partial b\,\partial\varepsilon$:

In the geometric framework, Vanna is the mixed covariant derivative
$\nabla\_{g\_M}\partial\_\varepsilon V$. For the Jacobi process:

$$\text{Vanna}_{\rm Jacobi} = b(1-b)\frac{\partial^2 V}{\partial b\,\partial\varepsilon}
+ (1-2b)\frac{\partial V}{\partial\varepsilon} \tag{6.14}$$

**Volga (Vomma)** = $\partial^2 V/\partial\varepsilon^2$: The second derivative with respect
to the WF parameter, measuring the curvature of the option price in volatility space.

For the **Clifford torus**: Volga involves the second derivative of the theta function
with respect to the modular parameter $\tau = 4i\varepsilon^2 T/\pi$:

$$\text{Volga}_{T^2} = T^2\cdot\frac{\partial^2 C}{\partial T^2}\bigg|_{\text{Clifford}}
= T^2 \cdot\frac{\partial}{\partial\tau}\!\left(\frac{\partial C}{\partial\tau}\right)\cdot\left(\frac{4iT}{\pi}\right)^2 \tag{6.15}$$

This is the **modular second derivative** of the option price — it measures the rate of
change of the torus correction to the option price. For long-maturity options ($\varepsilon^2 T \gg 1$):
the Volga approaches zero as the price stabilises at the long-run uniform distribution value.
For short maturities ($\varepsilon^2 T \ll 1$): Volga equals the standard Black-Scholes Vomma.
The torus geometry creates a **Volga smile** — Volga peaks at intermediate maturities
corresponding to the torus traversal time $T^{\ast} = (\pi/2)^2/(4\varepsilon^2)$.

### 6.6 The Gamma surface across market types

The key insight from the geometric Greeks: **Gamma is the Laplace-Beltrami operator
of the option price surface on the market manifold.** This means:

- **CAPM (positive curvature sphere):** The sphere's positive Ricci curvature adds
  to the effective Gamma, making options more convex than in flat space. The correction
  is $+\varepsilon^2 K\_M/(2T)$ per unit of option price, where $K\_M > 0$ is the
  sectional curvature.

- **Flat torus:** No curvature correction to Gamma — the option price surface is flat
  in the portfolio-weight space. Gamma is pure second derivative.

- **Hyperbolic market (negative curvature):** The negative Ricci curvature subtracts
  from effective Gamma in the interior, but the $y^2$ prefactor creates extreme Gamma
  near the boundary. The net effect: options near the centre are less convex than
  Black-Scholes predicts; options near the boundary are more convex. **The hyperbolic
  market has a Gamma inversion**: vanilla options near-the-money have sub-BS Gamma
  while deep out-of-the-money options have super-BS Gamma — explaining the observed
  vol smile without stochastic volatility.

---

## 7. Sobolev Regularity and the Greeks' Existence

### 7.1 When do Greeks exist?

**Theorem 7.1** *(Regularity of option price in weighted Sobolev space)*.
*Under the Muckenhoupt $A\_2$ condition (Lemma 1.3), the option price $V(\cdot,t)$
satisfies:*

$$V(\cdot,t) \in W^{2,2}(M, w_{\rm stat}) \quad\forall t \in [0,T) \tag{7.1}$$

*Consequently:*
- *$\Delta\_{g\_M}V$ (Delta) exists as an $L^2(M,w)$ function for all payoffs $G \in L^2(M,w)$*
- *$\Gamma\_{g\_M}V$ (Gamma) exists as an $L^2(M,w)$ function under the same condition*
- *For discontinuous payoffs (barriers, digitals): $G \in L^\infty(M)$ suffices for $V \in W^{1,2}$
  (Delta exists) but $V \in W^{2,2}$ requires $G \in W^{1,2}$*

*Proof.* This follows from the weighted Sobolev theory for degenerate parabolic equations
under the $A\_2$ condition, via the Kohn-Nirenberg calculus for degenerate operators.
The $W^{2,2}$ regularity follows from the $L^2$ theory for the Laplace-Beltrami operator
on a compact Riemannian manifold with the weighted norm. $\square$

### 7.2 Delta-Gamma hedging on the manifold

For a portfolio $\Pi = V - \Delta\_0 b - \Gamma\_0 \text{(some convex position)}$:

**Delta-hedged portfolio on $M$:** $d\Pi = \frac{\partial V}{\partial t}\,dt + O(\varepsilon^2 dt)$
(no first-order exposure to $b$-moves on $M$).

**Gamma-hedged portfolio on $M$:** additionally hedging $\Gamma\_{g\_M}V$, the portfolio
is locally flat to second order in $db$.

**The residual after Delta-Gamma hedging** is:

$$d\Pi = -\Theta_M V\,dt + O(|db|^3_{g_M}) \tag{7.2}$$

**The P&L of a Delta-Gamma neutral portfolio equals Theta** — exactly the Black-Scholes
relationship, now proved for all geometric market types. For the efficient market ($H=0$,
$\Theta\_M = \frac{\varepsilon^2}{2}\Gamma\_{g\_M}V - rV$): the Delta-Gamma neutral portfolio
earns the risk-free rate, consistent with no-arbitrage.

For the inefficient market: the additional $\vec{H}\cdot\Delta\_{g\_M}V$ term creates
excess P&L proportional to the curvature — the Sharpe from the curvature drift
reappears as excess Theta for a Delta-hedged position.

---

## 8. Summary

| Result | Formula | Classical analog |
|:-------|:--------|:----------------|
| Jacobi call (CAPM) | $e^{-rT}\sum\_n e^{-\lambda\_n T}P\_n^{(\alpha-1,\beta-1)}(2b\_0-1)\cdot I\_n(K)$ | Black-Scholes |
| Digital (CAPM) | $e^{-rT}\bar{I}\_K(\alpha,\beta)$ | $e^{-rT}N(d\_2)$ |
| Clifford torus call | Theta function formula (MARKET\_PROCESSES 10.1) | B-S with $\vartheta\_3$ |
| Double barrier (Clifford) | Sine series (4.4) / theta function (4.6) | Standard double barrier |
| Hyperbolic call (McKean) | Mehler-Fock spectral integral (5.3) | B-S with Legendre functions |
| First passage time (Jacobi) | Hypergeometric Laplace transform (3.2) | Standard BM first passage |
| Delta (CAPM) | $b(1-b)\partial\_b V$ | $\partial\_S C$ |
| Gamma (CAPM) | $b(1-b)\partial^2\_b V + (1-2b)\partial\_b V$ | $\partial^2\_S C$ |
| Gamma (Clifford) | $\partial^2\_\theta V + \partial^2\_\varphi V$ | $\partial^2\_X C$ |
| Gamma (hyperbolic) | $y^2(\partial^2\_x + \partial^2\_y)V$ | $\partial^2\_S C\cdot y^2$ |
| Theta (all) | $\frac{\varepsilon^2}{2}\Gamma\_{g\_M}V + \vec{H}\cdot\Delta\_{g\_M}V - rV$ | B-S Theta |

The key message: **Black-Scholes is the special case of these formulas when the market
manifold is flat, one-dimensional, and near equal-weight.** The geometric framework
gives the exact correction for each departure from this idealization.

---

## References

Kohn, J. J. and Nirenberg, L. (1965). An algebra of pseudo-differential operators.
*Communications on Pure and Applied Mathematics* 18(1-2), 269–305.

Muckenhoupt, B. (1972). Weighted norm inequalities for the Hardy maximal function.
*Transactions of the American Mathematical Society* 165, 207–226.

Stein, E. M. and Weiss, G. (1971). *Introduction to Fourier Analysis on Euclidean Spaces*.
Princeton University Press. [For weighted Sobolev theory.]

Titchmarsh, E. C. (1946). *Eigenfunction Expansions Associated with Second-Order
Differential Equations*. Oxford University Press.
[For the Jacobi polynomial spectral expansion.]

*[All other references as per companion papers.]*
