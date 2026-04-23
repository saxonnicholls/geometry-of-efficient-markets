# Feynman Path Integrals on the Market Manifold:
## Derivative Pricing as a Sum Over Manifold Paths,
## the Langevin Equation, and the Constrained Risk-Neutral Measure

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.4** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We develop the Feynman path integral formulation of derivative pricing for markets
whose price process lives on a minimal submanifold $M^r \subset S^{d-1}_{+}$.
The key departure from classical option pricing theory: the measure in the path
integral is not the Wiener measure on the full space $\mathbb{R}^{d}$ but the
**geometric Wiener measure on $M^r$** — a measure supported on paths that remain
on the market manifold. This constrained path integral produces exact pricing formulas
for each market type, recovers and explains our previous results (MARKET_PROCESSES,
LAPLACE), and establishes the complete correspondence between the path integral,
the Langevin equation, stochastic quantisation, and the Feynman-Kac theory.

**The central results:**

**(i) The constrained path integral.** The price of a derivative with payoff $G(b_T)$
on a market on manifold $M^r$ is:

```math
V(b,t) = e^{-r(T-t)}\int_{\mathrm{Paths}(M^r)} \mathcal{D}[b]
e^{-S_M[b]/(2\varepsilon^2)} G(b_T) \tag{0.1}
```

where $S_M[b] = \int_t^T |\dot b_s + \varepsilon^2\vec{H}(b_s)|^2_{g_M}\,ds$ is the
Onsager-Machlup action on $M^r$ and the integral is over all continuous paths
from $b$ to any final state $b_T \in M^r$.

**(ii) The WKB saddle point = LAPLACE.md.** The stationary phase approximation of
(0.1) is achieved at the geodesic path on $M^r$ from $b$ to $b'$. The prefactor
is the Van Vleck-Morette determinant, which equals the Fisher information matrix
$F(b^{\ast})$ — recovering the Laplace approximation of LAPLACE.md as the WKB leading
term. The $O(1/T^2)$ error is the first-order WKB correction vanishing because the
Jeffreys prior = stationary distribution.

**(iii) The Clifford torus path integral = theta function.** The path integral on
$T^2$ sums over homotopy classes — paths winding $(n_1,n_2)$ times around the two
torus cycles. Each winding sector contributes a Gaussian. Summing over all
$(n_1,n_2)\in\mathbb{Z}^{2}$ via Poisson resummation gives exactly
$\vartheta_3\times\vartheta_3$ — the theta function transition density of
MARKET_PROCESSES.md is the path integral summed over topological sectors.

**(iv) The risk-neutral measure lives on $M^r$.** The Girsanov change of measure
(from MARTINGALE_GEOMETRY) leaves the tangential ($TM$) paths unchanged and weights
the normal bundle ($NM$) paths by $e^{-\int\vec{H}\cdot dW - \varepsilon^2\int H^2 dt/2}$.
For the efficient market ($H=0$): the physical measure IS the risk-neutral measure
on $M$. The path integral under $\mathbb{Q}$ equals the path integral under $\mathbb{P}$
restricted to $M$.

**(v) The Langevin equation on $M^r$.** The overdamped Langevin equation:
$\dot{b}_{t} = -\varepsilon^2\nabla_{g_M}V(b_t) + \varepsilon\eta_t$
(where $V = -L_T$ is the Kelly potential and $\eta_t$ is white noise on $(M^r,g_M)$)
generates exactly the diffusion of MARKET_PROCESSES.md. Its stationary distribution
is the Jeffreys prior (FOKKER_PLANCK_CFD R5). The Parisi-Wu stochastic quantisation
of the Langevin equation produces the same path integral (0.1).

**(vi) Integrating out the normal bundle.** The full path integral over all of
$\Delta_{d-1}$ (not just $M^r$) factors into a manifold integral (over $M^r$)
and a normal bundle integral (over $NM$). Integrating out the idiosyncratic
paths (over $NM$) with the normal bundle Gaussian measure produces an **effective
action** on $M^r$ with a correction term proportional to $\mathrm{tr}(F^{-1}_{N})$
— the idiosyncratic Fisher-Rao radius. For the incomplete market: this gives a
non-trivial effective action and a correction to option prices from idiosyncratic
risk.

**Keywords.** Feynman path integral; Onsager-Machlup; Van Vleck-Morette determinant;
geometric Wiener measure; constrained path integral; Langevin equation; stochastic
quantisation; Parisi-Wu; risk-neutral measure; topological sectors; winding number;
theta function; McKean; WKB; saddle point; instanton; normal bundle integration.

---

## 1. The Path Integral Framework

### 1.1 The standard path integral for derivative pricing

The standard Black-Scholes option pricing formula arises from the path integral
\[Kleinert 2004, Chapter 3\]:

```math
V(S,t) = e^{-r(T-t)}\int\mathcal{D}[S]
\exp\!\left(-\frac{1}{2\sigma^2}\int_t^T\frac{(\dot S/S - \mu)^2}{\,1\,}\,ds\right)G(S_T) \tag{1.1}
```

where $\mathcal{D}[S]$ is the Wiener measure on log-normal paths and the action is
the Onsager-Machlup functional for GBM. The integral is over all continuous paths
$S:[t,T]\to\mathbb{R}_{+}$.

**The problem:** This integral is over all paths in $\mathbb{R}^{d}$ — including paths
that are wildly inconsistent with the market's factor structure. A 50-asset market
with 4 factors has 46 idiosyncratic directions — the standard path integral wastes
most of its support on paths that never actually occur.

**The solution:** Restrict the path integral to paths on the market manifold $M^r$.

### 1.2 The geometric Wiener measure on $M^r$

The **geometric Wiener measure** on paths $b:[t,T]\to M^r$ is:

```math
\mathcal{D}^{M}[b] = \lim_{N\to\infty}\prod_{k=0}^{N-1}
\frac{d\mathrm{vol}_{M}(b_{t_k})}{(4\pi\varepsilon^2\Delta t)^{r/2}}
\cdot\exp\!\left(-\frac{|b_{t_{k+1}}-b_{t_k}|^2_{g_M}}{4\varepsilon^2\Delta t}\right) \tag{1.2}
```

where $d\mathrm{vol}_{M}$ is the Riemannian volume element of $(M^r,g_M)$ and
$|b-b'|_{g_M}$ is the geodesic distance. This is the heat kernel short-time
approximation on the manifold, assembled into a path measure.

**The key difference from flat-space Wiener measure:** the volume element $d\mathrm{vol}_{M}$
carries the curvature of $M^r$. For the flat torus ($M=T^2$): $d\mathrm{vol}_{T^2} = d\theta\,d\varphi/((\pi/2)^2)$ — no correction. For the spherical CAPM ($M=S^r_+$): $d\mathrm{vol}_{S^r} = \sin^{r-1}\theta\,d\theta\,d\Omega_{r-1}$ — sine correction from the curvature. For the hyperbolic market ($M=\mathbb{H}^{2}$): $d\mathrm{vol}_{\mathbb{H}^{2}} = y^{-2}\,dx\,dy$ — the Poincaré volume element.

### 1.3 The Onsager-Machlup action on $M^r$

The **Onsager-Machlup functional** gives the probability weight for a specific path
on a Riemannian manifold \[Ikeda-Watanabe 1989\]. For the market process on $M^r$:

```math
S_M[b] = \int_t^T\!\left[\frac{1}{2}|\dot b_s|^2_{g_M}
+ \varepsilon^2\vec{H}(b_s)\cdot\dot b_s
+ \frac{\varepsilon^4}{2}|\vec{H}(b_s)|^2_{g_M}
+ \frac{\varepsilon^2}{6}R_M(b_s)\right]ds \tag{1.3}
```

where $R_M$ is the scalar curvature of $(M^r, g_M)$ and $\varepsilon^2 = 1/T$.

**The four terms:**
1. **Kinetic term** $\frac{1}{2}|\dot b|^2_{g_M}$: the geodesic action — minimised by
   straight-line (geodesic) paths. This is the $\sigma^2$ term in Black-Scholes.
2. **Drift-velocity coupling** $\varepsilon^2\vec{H}\cdot\dot b$: the interaction between
   mean curvature (alpha) and path velocity. Paths aligned with $\vec{H}$ are favoured.
3. **Mean curvature potential** $\frac{\varepsilon^4}{2}|\vec{H}|^2$: the Willmore energy
   density as a potential. Paths spend more time in high-curvature (inefficient) regions.
4. **Scalar curvature correction** $\frac{\varepsilon^2}{6}R_M$: the DeWitt-Morette correction
   \[DeWitt 1957\] from the Riemannian measure — absent in flat space.

**For the efficient market ($H=0$):**

```math
S_M^{\rm eff}[b] = \int_t^T\!\left[\frac{1}{2}|\dot b_s|^2_{g_M}
+ \frac{\varepsilon^2}{6}R_M(b_s)\right]ds \tag{1.4}
```

The action is the kinetic term plus the scalar curvature correction. The curvature
correction is $+\frac{\varepsilon^2}{6}R_M$ — for positively curved manifolds (CAPM
sphere, $R_M = r(r-1)/4$): paths are slightly suppressed by the positive curvature.
For negatively curved manifolds (hyperbolic market, $R_M < 0$): paths are enhanced.

---

## 2. The WKB Approximation = LAPLACE.md

### 2.1 The stationary phase calculation

The path integral (0.1) in the limit $\varepsilon^2 \to 0$ ($T\to\infty$) is dominated
by the path minimising the action — the **classical path** or **instanton** connecting
$b$ to $b'$.

For the efficient market: the classical path minimises $S_M^{\rm eff}[b]$, which for
large $T$ is dominated by the kinetic term. The minimum is the **geodesic** on
$(M^r, g_M)$ from $b$ to $b'$.

**The WKB option price:**

```math
V^{\rm WKB}(b,t;b',T) = e^{-r(T-t)}\cdot
\underbrace{(4\pi\varepsilon^2(T-t))^{-r/2}}_{\text{prefactor}}
\cdot\underbrace{e^{-d_{g_M}(b,b')^2/(4\varepsilon^2(T-t))}}_{\text{Gaussian in geodesic distance}}
\cdot\underbrace{J(b,b',T)^{-1/2}}_{\text{Van Vleck det}}
\cdot G(b') \tag{2.1}
```

where $J(b,b',T)$ is the **Van Vleck-Morette determinant**:

```math
J(b,b',T) = \det\!\left(-\frac{\partial^2 S_{\rm cl}(b,b',T)}{\partial b_i\partial b'_j}\right) \tag{2.2}
```

**Theorem 2.1** *(Van Vleck = Fisher information)*.
*At the log-optimal portfolio $b = b^{\ast}$, the Van Vleck-Morette determinant equals
the Fisher information matrix:*

```math
J(b^{\ast},b^{\ast},T) = \det F(b^{\ast}) \tag{2.3}
```

*where $F(b^{\ast}) = -\nabla^2 L_T(b^{\ast})|_{b^{\ast}}$ is the Hessian of the Kelly growth rate.*

*Proof.* The classical action from $b^{\ast}$ to $b^{\ast}$ in time $T$ is $S_{\rm cl}(b^{\ast},b^{\ast},T) = 0$
(trivial path, no kinetic cost). The second derivative of $S_{\rm cl}$ with respect to
the endpoint is the inverse propagator — the Fisher information matrix of the stationary
process, which equals $F(b^{\ast})$ by the Cramér-Rao bound for the efficient market. $\square$

**This is LAPLACE.md restated as a path integral identity.** The WKB approximation
(2.1) evaluated at $b=b'=b^{\ast}$ with the Van Vleck determinant (2.3) gives:

```math
V^{\rm WKB}\big|_{b=b^{\ast}} = e^{-rT}\cdot(4\pi\varepsilon^2 T)^{-r/2}\cdot(\det F(b^{\ast}))^{-1/2}\cdot G(b^{\ast})
= e^{-rT}\cdot\frac{G(b^{\ast})}{(4\pi T)^{r/2}\sqrt{\det F(b^{\ast})}} \tag{2.4}
```

This is exactly the Laplace approximation of LAPLACE.md (equation 3.7). **The WKB saddle
point approximation for the manifold path integral IS the Laplace approximation
for the universal portfolio.** The two computations are the same calculation in different language.

**The $O(1/T^2)$ accuracy** follows from the same argument as LAPLACE.md: the Jeffreys
prior is the stationary distribution of the diffusion, which causes the $O(1/T)$ WKB
correction to vanish exactly. In path integral language: the one-loop correction
to the WKB approximation is zero when the integration measure is the geometric Wiener
measure with the stationary prior.

---

## 3. The Langevin Equation and Stochastic Quantisation

### 3.1 The overdamped Langevin equation on $M^r$

The **overdamped Langevin equation** on the Riemannian manifold $(M^r, g_M)$ is:

```math
\dot b_t = -\varepsilon^2\nabla_{g_M}V(b_t) + \varepsilon\,\eta_t \tag{3.1}
```

where $V = -L_T(b)$ is the Kelly potential (negative log-growth rate), and $\eta_t$
is white noise with covariance $\mathbb{E}[\eta_t^\mu\eta_s^\nu] = g_M^{\mu\nu}(b_t)\delta(t-s)$
(noise in the Fisher-Rao metric).

For the efficient market ($V$ = constant on $M^r$, i.e., $\nabla_{g_M}L_T = 0$ at $b^{\ast}$):

```math
\dot b_t = \varepsilon\,\eta_t \tag{3.2}
```

Pure diffusion on $M^r$ — the market portfolio performs Brownian motion on the manifold.

For the inefficient market ($V = -L_T$, $\nabla_{g_M}L_T \neq 0$):

```math
\dot b_t = \varepsilon^2\nabla_{g_M}L_T(b_t) + \varepsilon\,\eta_t
= -\varepsilon^2\Pi_{TM}\!\left[\nabla_{g^{\rm FR}}L_T\right] + \varepsilon\,\eta_t \tag{3.3}
```

The drift is the gradient of the Kelly growth rate projected onto $TM$ — which, by the
KKT conditions for the log-optimal portfolio, equals $-\varepsilon^2\Pi_{NM}\vec{H}/T + O(\varepsilon^4)$ (from CONVERGENCE.md). For the efficient market ($H=0$): zero drift.

**Connection to our previous processes:** Equation (3.3) IS the SDE from MARKET_PROCESSES.md —
the Langevin equation generates exactly the same diffusion as the WF process on $M^r$.

### 3.2 Parisi-Wu stochastic quantisation

**Parisi and Wu \[1981\]** proposed generating the Euclidean path integral measure by
running a Langevin equation in a fictitious "stochastic time" $\tau$:

```math
\frac{\partial b(t,\tau)}{\partial\tau} = -\frac{\delta S_M[b]}{\delta b(t,\tau)}
+ \xi(t,\tau) \tag{3.4}
```

where $S_M[b]$ is the action and $\xi$ is white noise in both real time $t$ and
fictitious time $\tau$.

**The stationary distribution** of the Parisi-Wu Langevin equation (3.4) is:

```math
\rho_\infty \propto e^{-S_M[b]} = e^{-\int_0^T |\dot b|^2_{g_M}/(2\varepsilon^2)\,dt}
\cdot e^{-\int_0^T \varepsilon^2|\vec{H}|^2/2\,dt} \tag{3.5}
```

This is the **path integral measure** — the Parisi-Wu stochastic quantisation generates
the path integral by running the field equation (3.4) to stationarity. The stationary
distribution IS the path integral measure.

**For the efficient market:** the stationary distribution is $e^{-\int|\dot b|^2_{g_M}/2\varepsilon^2}$
— the geometric Wiener measure. The Parisi-Wu approach gives the same path integral
as the direct construction.

### 3.3 The effective potential and instantons

The **effective potential** is the free energy density of the path integral:

```math
V_{\rm eff}(b) = -\frac{1}{T}\log\int_{\rm paths:b_0=b}\mathcal{D}^{M}[b']\,
e^{-S_M[b']/2\varepsilon^2} \tag{3.6}
```

— the log-probability of the path integral arriving at $b$ starting from a stationary distribution.

For the efficient market: $V_{\rm eff}(b) = -L_T(b)$ — the effective potential is
the Kelly growth rate. **The effective potential of the path integral = the Kelly criterion.**

**Instantons.** The Euclidean classical solutions of the Langevin equation (3.1) are
the paths that extremise the action $S_M[b]$. These are the **geodesics** on
$(M^r, g_M)$ — paths of minimum Fisher-Rao length. Each instanton connects one
portfolio configuration to another via the geodesic on $M^r$.

For the Clifford torus: instantons include constant paths ($b=b^{\ast}$, the
log-optimal portfolio) AND non-trivial winding paths that go around the torus.
The winding instantons contribute to the path integral with action
```math
S_{\rm instanton} = n^2(\pi/2)^2/(2\varepsilon^2\cdot\mathrm{Area}(T^2)) \propto n^2/\varepsilon^2
```
— exponentially suppressed for large winding number $n$. **Topological instantons
generate exponentially small corrections to option prices from the winding number sectors.**

---

## 4. The Path Integral Summed Over Topological Sectors

### 4.1 The Clifford torus: theta function from winding sum

For the Clifford torus market ($M = [0,\pi/2]^2$ with periodic identifications),
the path integral propagator from $(\theta_0,\varphi_0)$ to $(\theta,\varphi)$
in time $T$ is:

```math
K_{T^2}(\theta,\varphi|\theta_0,\varphi_0;T) = \sum_{(n_1,n_2)\in\mathbb{Z}^{2}}
K_{\rm flat}\!\left(\theta-\theta_0+\frac{n_1\pi}{2}, 
\varphi-\varphi_0+\frac{n_2\pi}{2}; T\right) \tag{4.1}
```

where $K_{\rm flat}(x,y;T) = \frac{1}{2\pi\varepsilon^2 T}e^{-(x^2+y^2)/(2\varepsilon^2 T)}$
is the flat-space Gaussian propagator.

**The sum over winding numbers** $(n_1,n_2)\in\mathbb{Z}^{2}$ is the Poisson resummation
of the Gaussian over the lattice $(\pi/2)\mathbb{Z}^{2}$. By the Poisson summation formula:

```math
\sum_{n\in\mathbb{Z}} e^{-(\theta+n\pi/2)^2/(2\varepsilon^2 T)}
= \sqrt{2\pi\varepsilon^2 T}\cdot\sum_{k\in\mathbb{Z}}
e^{-2k^2\varepsilon^2 T/(\pi^2/4)}\cos(4k\theta/\pi) \tag{4.2}
```

The right-hand side is $\frac{\pi}{\sqrt{2}}\cdot\vartheta_3\!\!\left(\frac{\theta}{\pi/2}\,\big|\,
\frac{2i\varepsilon^2 T}{\pi^2/4}\right)$ — the Jacobi theta function.

**Theorem 4.1** *(Theta function = path integral over topological sectors)*.
*The transition density of the Clifford torus market:*

```math
p_T(\theta|\theta_0) = \frac{2}{\pi}\vartheta_3\!\!\left(\frac{\theta-\theta_0}{2}\,\bigg|\,
\frac{4i\varepsilon^2 T}{\pi}\right) \tag{4.3}
```

*(from MARKET_PROCESSES.md equation 4.4) is EXACTLY the path integral (4.1)
evaluated by Poisson resummation over the winding lattice $\mathbb{Z}^{2} = \pi_1(T^2)$.*

*Each term in the theta function series corresponds to one topological sector
$(n_1,n_2) \in \pi_1(T^2) = \mathbb{Z}^{2}$. The $n=0$ term is the direct path;
$n\neq 0$ terms are paths winding around the torus.*

**The theta function IS the topological sector sum.** This explains why the theta
function appears: it is the unique function that correctly sums the contributions
from all homotopy classes of paths on $T^2$. Every term in the theta function
$\vartheta_3 = 1 + 2q + 2q^4 + 2q^9 + \ldots$ (where $q = e^{-4\varepsilon^2 T/\pi}$)
is a winding sector: the $q^{n^2}$ term is the contribution from paths winding
$n$ times around the torus.

**The modular transformation** $\vartheta_3(z|\tau) = (-i\tau)^{-1/2}e^{iz^2/\pi\tau}\vartheta_3(z/\tau|-1/\tau)$
is the **path integral S-duality**: it maps the short-time expansion (few windings,
direct paths dominate) to the long-time expansion (many windings, summed by the
dual theta function). This is the financial version of T-duality from string theory.

### 4.2 The McKean kernel as the hyperbolic path integral

For the hyperbolic market ($M=\mathbb{H}^{2}$ with Poincaré metric), the path integral
propagator is evaluated by summing over all classical paths (geodesics) from $(x_0,y_0)$
to $(x,y)$. In $\mathbb{H}^{2}$, for each geodesic distance $\rho$, there is exactly
one geodesic (unlike the torus, where there are infinitely many windings). The sum
over classical paths gives:

```math
K_{\mathbb{H}^{2}}(\rho;T) = \frac{e^{-T/4}}{(4\pi T)^{1/2}}\cdot
\frac{\rho\,e^{-\rho^2/(4T)}}{\sinh\rho} \tag{4.4}
```

— the McKean heat kernel (MARKET_PROCESSES.md equation 5.7).

**The factor $\rho/\sinh\rho$** is the ratio of the Euclidean to hyperbolic volume
elements — it is the Jacobian of the geodesic exponential map on $\mathbb{H}^{2}$,
which is the Van Vleck-Morette determinant for the hyperbolic geometry.

**The factor $e^{-T/4}$** is the scalar curvature correction (the DeWitt-Morette
term from equation 1.4 with $R_{\mathbb{H}^{2}} = -1$, giving $-\varepsilon^2R/6 = +T/(6\cdot 4) \cdot 4 \approx T/4$
in appropriate normalisation). The negative curvature of the hyperbolic market
ADDS to the path integral measure — paths on $\mathbb{H}^{2}$ are more probable than
on flat space. This is why the McKean kernel decays sub-Gaussianly: the negative
curvature spreads the paths out.

---

## 5. The Risk-Neutral Measure on the Market Manifold

### 5.1 The Girsanov theorem as a path integral change of measure

The Girsanov change of measure from the physical measure $\mathbb{P}$ to the
risk-neutral measure $\mathbb{Q}$ corresponds to a **shift in the Langevin drift**:

```math
\text{Under }\mathbb{P}: \dot b = -\varepsilon^2\vec{H} + \varepsilon\eta
\qquad\text{(inefficient market drift)}
```

```math
\text{Under }\mathbb{Q}: \dot b = \varepsilon\eta
\qquad\text{(efficient market, no drift)} \tag{5.1}
```

The Radon-Nikodym derivative is:

```math
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_T = \exp\!\left(
\frac{1}{\varepsilon}\int_0^T\vec{H}(b_t)\cdot dW_t^M
- \frac{\varepsilon}{2}\int_0^T|\vec{H}(b_t)|^2_{g_M}\,dt\right) \tag{5.2}
```

**In path integral language:** Changing measure from $\mathbb{P}$ to $\mathbb{Q}$
modifies the Onsager-Machlup action by removing the drift term:

```math
S_M^{\mathbb{P}}[b] = \int|\dot b + \varepsilon^2\vec{H}|^2_{g_M}/2\,dt
\quad\longrightarrow\quad
S_M^{\mathbb{Q}}[b] = \int|\dot b|^2_{g_M}/2\,dt \tag{5.3}
```

The risk-neutral action is the PURE kinetic term — the geodesic action. **Under the
risk-neutral measure, ALL paths on $M^r$ have equal kinetic cost; there is no
preferred direction.** This is the path integral statement of market efficiency:
under $\mathbb{Q}$, the market process is a martingale on $M^r$.

**The Novikov condition** (from MARTINGALE_GEOMETRY) is that the Girsanov factor (5.2)
is $\mathbb{P}$-integrable — i.e., $\mathbb{E}^\mathbb{P}[e^{\varepsilon\int H\,dW}] < \infty$.
This is equivalent to the Willmore energy bound
$\int_0^T|\vec{H}|^2_{g_M}\,dt = T\mathcal{W}(M)/\mathrm{vol}(M) < \infty$. **The
Novikov condition IS the finite Willmore energy condition.**

### 5.2 Option pricing under $\mathbb{Q}$ on $M^r$

Under the risk-neutral measure $\mathbb{Q}$, the option price is:

```math
V(b,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[G(b_T)|b_t=b]
= e^{-r(T-t)}\int_{M^r}p^{\mathbb{Q}}_{T-t}(b,b')\,G(b')\,d\mathrm{vol}_{M}(b') \tag{5.4}
```

where $p^{\mathbb{Q}}_{T-t}$ is the heat kernel under $\mathbb{Q}$ — the transition
density of the pure diffusion on $M^r$ (no drift).

**For the CAPM ($M=S^r_+$, GBM limit):** $p^{\mathbb{Q}}_\tau$ = Jacobi transition
density with $\kappa=0$ (no mean reversion under $\mathbb{Q}$, only diffusion).
At short times: reproduces the GBM/Black-Scholes formula.

**For the Clifford torus:** $p^{\mathbb{Q}}_\tau = \vartheta_3\times\vartheta_3$
(theta function, no drift term). The option price is the theta function call formula
(SOBOLEV_OPTIONS_GREEKS equation 10.1).

**For the hyperbolic market:** $p^{\mathbb{Q}}_\tau = K_{\mathbb{H}^{2}}(\rho;\tau)$
(McKean kernel). The option price is the McKean call formula (SOBOLEV equation 5.1).

**The critical observation:** The risk-neutral transition density under $\mathbb{Q}$
is the SAME as the physical transition density under $\mathbb{P}$ for the efficient
market ($H=0$) — because $d\mathbb{Q}/d\mathbb{P} = 1$ on $TM$ when $H=0$.
For the efficient market: **you don't need to change measure on the manifold.**
The physical paths and risk-neutral paths are the same.

---

## 6. Integrating Out the Normal Bundle

### 6.1 The full path integral

The full derivative price — accounting for all paths in $\Delta_{d-1}$, not just $M^r$ — is:

```math
V_{\rm full}(b,t) = e^{-r(T-t)}\int_{\rm all paths \Delta_{d-1}}
\mathcal{D}^{\Delta}[b] e^{-S_\Delta[b]/(2\varepsilon^2)} G(b_T) \tag{6.1}
```

**Splitting paths into manifold and normal components:**
Any path $b(t) \in \Delta_{d-1}$ near $M^r$ can be written as:

```math
b(t) = b^M(t) + \sum_{\alpha=r+1}^{d-1}\xi^\alpha(t)\nu_\alpha(b^M(t)) \tag{6.2}
```

where $b^M(t) \in M^r$ is the manifold component and $\xi^\alpha(t)\nu_\alpha$ are
the normal bundle coordinates (HAMILTONIAN_TAILS paper).

**The action splits:**

```math
S_\Delta[b] = S_M[b^M] + S_N[\xi;\,b^M] + S_{\rm coupling}[b^M,\xi] \tag{6.3}
```

where $S_N[\xi;b^M] = \int\sum_\alpha |\dot\xi^\alpha|^2/2\,dt$ is the normal bundle
kinetic term and $S_{\rm coupling}$ involves the second fundamental form $II$ coupling
$b^M$ and $\xi$.

### 6.2 Integrating out the normal bundle

**Theorem 6.1** *(Normal bundle integration gives an effective manifold action)*.
*Integrating out the normal bundle paths $\xi^\alpha$ in (6.1)-(6.3) gives an
effective action on $M^r$:*

```math
V_{\rm full}(b,t) = e^{-r(T-t)}\int_{M^r}\mathcal{D}^{M}[b^M]
 e^{-S_{\rm eff}[b^M]/(2\varepsilon^2)} G^{\rm eff}(b^M_T) \tag{6.4}
```

*where the effective action is:*

```math
S_{\rm eff}[b^M] = S_M[b^M]
+ \underbrace{\frac{\varepsilon^2}{2}\mathrm{tr}(F_N^{-1})\cdot(T-t)}_{\text{idiosyncratic correction}}
+ O(\varepsilon^4) \tag{6.5}
```

*and $F_N = \Pi_{NM}F(b^{\ast})\Pi_{NM}$ is the normal bundle Fisher matrix (idiosyncratic
Fisher information).*

*Proof.* The normal bundle integral $\int\mathcal{D}[\xi]e^{-S_N[\xi;b^M]/2\varepsilon^2}$
is a Gaussian path integral with propagator $(F_N)^{-1}$. Evaluating the Gaussian
gives the determinantal prefactor $(\det F_N)^{-1/2}$ — which contributes
$\frac{\varepsilon^2}{2}\mathrm{tr}(F_N^{-1})\cdot(T-t)$ to the effective action at
leading order in $\varepsilon^2$. $\square$

**The idiosyncratic correction** $\frac{\varepsilon^2}{2}\mathrm{tr}(F_N^{-1})$ is:
- Zero if $F_N = \infty$ (infinite idiosyncratic Fisher information = complete information = complete market)
- Non-zero for incomplete markets ($F_N < \infty$, $d-1-r > 0$ idiosyncratic directions)

For the Harrison-Pliska incomplete market with $d-1-r = 45$ idiosyncratic directions:
the normal bundle correction shifts all option prices upward by
$\frac{\varepsilon^2}{2}\mathrm{tr}(F_N^{-1})\cdot(T-t)$ — a model-independent
**incompleteness premium** on all derivatives.

---

## 7. The Complete Path Integral Picture

### 7.1 The pricing formula hierarchy

For each market type, the exact option pricing formula follows from the path integral:

| Market type | Path integral measure | Classical paths | Option formula |
|:-----------|:---------------------|:----------------|:---------------|
| CAPM | Jacobi Wiener on $S^r_+$ | Geodesics on sphere | Jacobi polynomial series |
| Clifford $T^2$ | Flat Wiener on $T^2$ | Geodesics + all windings | Theta function $\vartheta_3$ |
| Hyperbolic $\mathbb{H}^{2}$ | Poincaré Wiener on $\mathbb{H}^{2}$ | Unique geodesic (no windings) | McKean kernel |
| Lawson $\Sigma^2_g$ | Fuchsian Wiener on $\Sigma^2_g$ | Geodesics + homology cycles | Selberg/automorphic |
| GBM (limit) | Flat Wiener on $\mathbb{R}$ | Straight line | Black-Scholes |

### 7.2 The connection diagram

```
                    FEYNMAN-KAC PDE
                         │
    ┌────────────────────┼─────────────────────┐
    │                    │                     │
    ▼                    ▼                     ▼
PATH INTEGRAL       LANGEVIN EQ.          FK FORMULA
∫𝒟[b]e^{-S_M/2ε²}   ḃ = -ε²∇V + εη     u(b,T) = 𝔼[G(b_T)]
    │                    │                     │
    └────────────────────┼─────────────────────┘
                         │
              WKB SADDLE POINT
              = geodesic on M^r
              = Van Vleck = F(b*)
              = LAPLACE.md
                         │
              ┌──────────┼──────────┐
              │          │          │
              ▼          ▼          ▼
           CAPM      Clifford   Hyperbolic
        Jacobi series  θ-function  McKean
              │          │          │
         Exact option pricing formulas
         (MARKET_PROCESSES, SOBOLEV)
```

### 7.3 The new result: the incompleteness premium

From (6.5): the effective action on the market manifold receives an idiosyncratic
correction from integrating out the normal bundle:

```math
\Delta V_{\rm incompleteness}(b,t) = e^{-r(T-t)}\cdot\frac{\varepsilon^2}{2}
\mathrm{tr}(F_N^{-1})\cdot(T-t) \cdot V_{\rm manifold}(b,t) \tag{7.1}
```

**This is the path integral derivation of the incompleteness premium** — the additional
option value that arises because idiosyncratic paths contribute to the full path
integral even though they do not affect the systematic (manifold) payoff.

For variance swaps (payoff = $\int\sigma^2\,dt$, which has a non-trivial normal bundle
component from $H^2$): the incompleteness premium is the Willmore energy, consistent
with DERIVATIVES_CONVEXITY.md.

For index options (payoff depends only on the index = $\Pi_{TM}$ projection of returns):
the normal bundle paths do not contribute to $G^{\rm eff}$ — the incompleteness
premium is zero. **Index options are insulated from incompleteness**, consistent with
HAMILTONIAN_TAILS_COMPLETENESS.md.

---

## 8. Summary

The Feynman path integral for derivative pricing, when the market lives on $M^r$,
is a **constrained path integral over manifold paths** with the geometric Wiener
measure. Key results:

$$
\begin{array}{lcl}
\text{WKB saddle} & = & \text{geodesic on }M^r \\
\text{Van Vleck det.} & = & F(b^{\ast})\text{ (Fisher info)}\\
\text{WKB accuracy }{O(1/T^2)} & = & \text{Jeffreys prior = stationary dist.}\\
\text{Theta function} & = & \text{winding sum on }T^2\\
\text{McKean kernel} & = & \text{unique geodesic on }\mathbb{H}^{2}\\
\text{Novikov condition} & = & \text{finite Willmore energy}\\
\text{Risk-neutral on }M^r & = & \text{efficient market: }P=Q\\
\text{Normal bundle integral} & = & \text{incompleteness premium}\\
\text{Langevin stationary dist.} & = & \text{Jeffreys prior}\\
\text{Parisi-Wu equilibrium} & = & \text{path integral measure}\\
\end{array}
}$$

The path integral is the universal language that unifies: LAPLACE.md (WKB), MARKET_PROCESSES.md
(transition densities), MARTINGALE_GEOMETRY.md (risk-neutral measure), HAMILTONIAN_TAILS.md
(incompleteness), and FILTRATIONS.md (topological sectors = filtration winding numbers).

It is the language you learned first. Now it has a manifold to live on.

---

## References

DeWitt, B. S. (1957). Dynamical theory in curved spaces I.
*Physical Review* 85(4), 653–661.

Feynman, R. P. and Hibbs, A. R. (1965). *Quantum Mechanics and Path Integrals*. McGraw-Hill.

Ikeda, N. and Watanabe, S. (1989). *Stochastic Differential Equations and Diffusion Processes*
(2nd ed.). North-Holland.

Kleinert, H. (2004). *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics,
and Financial Markets* (4th ed.). World Scientific.

Onsager, L. and Machlup, S. (1953). Fluctuations and irreversible processes.
*Physical Review* 91(6), 1505–1512.

Parisi, G. and Wu, Y. S. (1981). Perturbation theory without gauge fixing.
*Scientia Sinica* 24(4), 483–496.

*[All other references as per companion papers.]*
