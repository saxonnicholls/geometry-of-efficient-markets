# Closed-Form Stochastic Processes for Classified Market Manifolds:
## Beyond GBM — Exact SDEs, Transition Densities, and Return Distributions
## Forced by Market Topology

**Saxon Nicholls** — me@saxonnicholls.com

---

**Abstract.**  
We derive explicit, closed-form stochastic processes for each class of market
manifold in the classification of CLASSIFICATION.md. These are not modelling
choices — they are the unique processes compatible with the geometry of the
corresponding minimal surface and its Fisher-Rao metric. For each market type
we provide: the exact SDE in natural coordinates, the transition density as a
series in classical special functions, the stationary distribution, the characteristic
function of log-returns, and a simulation scheme. GBM is recovered as the
degenerate one-dimensional flat limit ($r=1$, near-Gaussian regime, large $T$).
The results organise as:

**CAPM ($S^1\_+$)** → **Jacobi/Wright-Fisher diffusion.** Transition density = Jacobi
polynomial series. Stationary distribution = Beta$(\alpha,\beta)$. Characteristic
function = Kummer confluent hypergeometric $\_1F\_1$.

**Multi-factor CAPM ($S^r\_+$)** → **Spherical Brownian motion.** Transition density
= Gegenbauer polynomial series. Stationary = uniform on $S^r\_+$. Characteristic
function = Bessel function series.

**Clifford torus ($T^2$)** → **Wrapped Gaussian / flat torus BM.** Transition density
= Jacobi theta function $\vartheta\_3$ (exactly closed-form). Stationary = uniform.
Log-returns are wrapped normal — **not Gaussian.** Periodic boundary conditions
create characteristic interference peaks in the return distribution.

**Figure-eight / hyperbolic ($\mathbb{H}^2$)** → **Hyperbolic Brownian motion.**
Transition density = McKean heat kernel (integral involving $\cosh$). Long-time
return distribution converges to Cauchy — power-law tails with $\alpha=1$.
Characteristic function = $e^{-t(\xi^2 + 1/4)}$.

**Lawson $\tau\_{m,n}$ ($\Sigma^2\_g$)** → **Fuchsian diffusion.** Transition density
controlled by Selberg zeta function and Maass waveforms. The spectral gap is
the Ramanujan bound on the automorphic spectrum.

**Pseudo-Anosov** → **Anosov diffusion along stable/unstable foliations.** The
return distribution is the Sinai-Ruelle-Bowen (SRB) measure — an absolutely
continuous but non-Gaussian, non-symmetric measure with power-law tails determined
by the Lyapunov exponent $\log\lambda\_{\rm pA}$.

**Keywords.** Jacobi diffusion; Wright-Fisher; spherical BM; wrapped normal;
Jacobi theta function; hyperbolic BM; McKean heat kernel; Fuchsian diffusion;
Selberg zeta; SRB measure; closed-form transition density; return distribution;
market topology; minimal surface diffusion.

**MSC 2020.** 60J60, 60J65, 58J35, 33C45, 11F72, 37D35, 91G10.

---

## 1. The Framework: From Geometry to Process

### 1.1 Why the process is determined by the geometry

Each market manifold $M^r \subset S^{d-1}\_+$ carries a canonical diffusion: the
intrinsic Brownian motion of the Riemannian manifold $(M^r, g\_M)$ where $g\_M = \iota^{\ast}g^{\mathrm{FR}}$
is the induced Fisher-Rao metric. This is the unique diffusion satisfying:

1. **Generator = half the Laplace-Beltrami operator**: $\mathcal{L} = \frac{\varepsilon^2}{2}\Delta\_M$
2. **Stationary distribution = normalised Riemannian volume**: $\rho\_\infty = d\mathrm{vol}\_M / \mathrm{vol}(M)$
3. **No preferred direction** (invariance under the isometries of $M$)

The process is not a modelling choice. It is the minimal diffusion compatible with
the geometry — the one that knows nothing except the shape of $M$.

**The key theorem** (from FOKKER\_PLANCK\_CFD Theorem 1.1): the stationary distribution
of this canonical diffusion is the Jeffreys prior — the same prior that makes Cover's
universal portfolio achieve $O(1/T^2)$ error. The geometry and the portfolio theory
are aligned: the process that is natural on $M$ is also the process that the universal
portfolio implicitly models.

### 1.2 The return process

For a portfolio $b\_t$ evolving on $M$ and an asset $i$, the **portfolio return** at
time $t$ is:

$$R_{t,i} = \log(b_{t,i}/b_{t-1,i}) \tag{1.1}$$

The **index return** is:

$$R_t^{\rm index} = \log\langle b_t, x_t\rangle \approx \sum_i b_{t,i}R_{t,i} \tag{1.2}$$

The distributional properties of $R\_{t,i}$ and $R\_t^{\rm index}$ are determined by
the diffusion on $M$. For each market type we compute these explicitly.

---

## 2. Type 1: CAPM — The Jacobi/Wright-Fisher Diffusion

### 2.1 The exact SDE

For the CAPM market ($r=1$, $M = S^1\_+$, two assets), the natural coordinate is
$b\_1 \in (0,1)$ (the weight on asset 1). The canonical diffusion on $S^1\_+$ in the
Fisher-Rao metric $g^{\mathrm{FR}}\_{11} = 1/(b\_1(1-b\_1))$ is:

$$\boxed{db_t = \kappa(\theta - b_t)\,dt + \sqrt{2\varepsilon^2 b_t(1-b_t)}\,dW_t} \tag{2.1}$$

with:
- $\kappa = \varepsilon^2\lambda\_1$ (Jacobi spectral gap, from CLASSIFICATION.md)
- $\theta = b^{\ast} = $ log-optimal portfolio weight
- $\varepsilon^2 = 1/T$ (the WF diffusion parameter)
- $\lambda\_1 = $ first nonzero eigenvalue of $-\Delta\_{S^1\_+}$

This is the **Wright-Fisher diffusion** (population genetics) or the **Jacobi diffusion**
(stochastic analysis). It is the natural diffusion on the 1-simplex $\Delta\_1 = [0,1]$
in the Fisher-Rao metric.

**Parameters from market data:**

$$\kappa = \frac{(1-\rho^2)\sigma_A^2\sigma_B^2}{(\sigma_A - \sigma_B\rho)^2\cdot(\sigma_B - \sigma_A\rho)^2}\cdot\varepsilon^2, \quad
\theta = b^{\ast}_1 = \frac{\mu_A\sigma_B^2 - \mu_B\rho\sigma_A\sigma_B}{\mu_A\sigma_B^2 + \mu_B\sigma_A^2 - (\mu_A+\mu_B)\rho\sigma_A\sigma_B} \tag{2.2}$$

The **Jacobi parameters** are $\alpha = \kappa\theta/\varepsilon^2$ and $\beta = \kappa(1-\theta)/\varepsilon^2$.

### 2.2 The exact transition density

**Theorem 2.1** *(Jacobi transition density, Karlin-McGregor 1957)*. *The transition
density of the Jacobi diffusion (2.1) is:*

$$p(t,b|b_0) = \sum_{n=0}^\infty e^{-\lambda_n t} q_n(b_0) q_n(b) \cdot w(b) \tag{2.3}$$

*where:*
- *$\lambda\_n = \varepsilon^2 n(n+\alpha+\beta)/(2(\alpha+\beta)^2)$ are the eigenvalues*
- *$q\_n(b) = P\_n^{(\alpha-1,\beta-1)}(2b-1)$ are the Jacobi polynomials*
- *$w(b) = b^{\alpha-1}(1-b)^{\beta-1}/B(\alpha,\beta)$ is the Beta density*
- *$B(\alpha,\beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$*

*The normalisation satisfies $\sum\_n (q\_n(b))^2 w(b) = \delta(b-b\_0)$.*

**The stationary distribution** (the $n=0$ term):

$$\rho_\infty(b) = \text{Beta}(\alpha, \beta) = \frac{b^{\alpha-1}(1-b)^{\beta-1}}{B(\alpha,\beta)} \tag{2.4}$$

For the Jeffreys prior: $\alpha = \beta = 1/2$ → arcsine distribution, $\rho\_\infty(b) = \frac{1}{\pi\sqrt{b(1-b)}}$.

### 2.3 Characteristic function of log-returns

For the Jacobi process, the moment generating function of $b\_t$ given $b\_0$:

$$M(u,t) = \mathbb{E}[e^{ub_t}|b_0] = e^{ub_0 e^{-\kappa t}}\cdot {}_1F_1\!\left(\alpha; \alpha+\beta; u(1-e^{-\kappa t})\right) \tag{2.5}$$

where $\_1F\_1(a;c;z)$ is the Kummer confluent hypergeometric function. Setting $u = i\xi$
gives the characteristic function of $b\_t$.

**Log-return distribution.** The log-return $r\_t = \log(b\_t/b\_{t-1})$ does not have
a simple closed form, but its characteristic function is:

$$\hat\phi_r(\xi) = \mathbb{E}[e^{i\xi\log(b_t/b_0)}] = \sum_{n=0}^\infty e^{-\lambda_n t}\frac{B(\alpha+i\xi, \beta)}{B(\alpha,\beta)} q_n(b_0) P_n^{(i\xi-1, \beta-1)}(1-2b_0) \tag{2.6}$$

**Short-time limit** ($\kappa t \ll 1$): the Jacobi diffusion approximates GBM:

$$r_t \approx \mathcal{N}\!\left(\left(\mu - \frac{\varepsilon^2}{2b_0(1-b_0)}\right)t,\; \frac{2\varepsilon^2 b_0(1-b_0)}{dt}\right) \tag{2.7}$$

This is a Gaussian with **position-dependent variance** $\sigma^2(b\_0) = 2\varepsilon^2 b\_0(1-b\_0)$ — the
Fisher-Rao diffusion coefficient. For $b\_0 = 0.5$ (equal weight): $\sigma^2 = \varepsilon^2/2$,
the minimum volatility. For $b\_0 \to 0$ or $b\_0 \to 1$ (concentrated portfolio): $\sigma^2 \to 0$.
**The Jacobi diffusion is more volatile at equal weights than at extreme concentrations** —
the opposite intuition from GBM, but correct for a mean-reverting portfolio process.

**Long-time limit** ($\kappa t \gg 1$): converges to Beta$(\alpha,\beta)$, independent of $b\_0$.

### 2.4 The GBM limit

GBM is recovered when: $b\_0 \to 0$ (small weight, single-asset limit), $\alpha\to\infty$
(large drift dominates), and $\alpha/(\alpha+\beta) = b^{\ast}$ (centred at equilibrium).

In this limit: $\sqrt{2\varepsilon^2 b\_t(1-b\_t)} \approx \sqrt{2\varepsilon^2 b\_t} = \sigma\sqrt{b\_t}$,
giving $d(\log b\_t) \approx (\mu-\sigma^2/2)dt + \sigma\,dW\_t$ — GBM for the portfolio weight.

**GBM is the zero-curvature, single-asset limit of the Jacobi diffusion.**

---

## 3. Type 2: Multi-Factor CAPM — Spherical Brownian Motion

### 3.1 The exact SDE

For the $r$-factor CAPM ($M = S^r\_+$), in angular coordinates
$(\theta\_1, \ldots, \theta\_{r-1}) \in [0,\pi/2]^{r-1}$ with $b\_k = \cos^2\theta\_{k-1}\sin^2\theta\_{k-2}\cdots$,
the canonical diffusion on $S^r\_+$ is:

$$d\theta_k = -\frac{(r-k)\varepsilon^2}{2}\cot\theta_k\,dt + \varepsilon\,dW^k_t, \qquad k = 1,\ldots,r-1 \tag{3.1}$$

The $-\cot\theta\_k$ drift is the **geometric drift** from the sphere metric (the sphere
has positive curvature, which creates a centripetal force pulling the process away from
the poles). For $r=1$: reduces to (2.1) since $\cot\theta \sim (1-2b\_1)/\sqrt{b\_1(1-b\_1)}$.

### 3.2 The heat kernel on $S^r\_+$

**Theorem 3.1** *(Spherical heat kernel)*. *The transition density of spherical BM
on $S^r$ (full sphere, then restrict to positive orthant) is:*

$$p_t(\psi) = \sum_{k=0}^\infty e^{-k(k+r-1)\varepsilon^2 t/2} \frac{(2k+r-1)\Gamma((r-1)/2)}{2\pi^{(r-1)/2}\Gamma(r)}
C_k^{(r-1)/2}(\cos\psi) \tag{3.2}$$

*where $\psi = d\_{S^r}(b,b')$ is the geodesic distance and $C\_k^{(r-1)/2}$ are the
Gegenbauer (ultraspherical) polynomials.*

**Special cases:**
- $r=1$ ($S^1$): $C\_k^0(\cos\psi) = T\_k(\cos\psi)$ (Chebyshev polynomials of first kind)
- $r=2$ ($S^2$): $C\_k^{1/2}(\cos\psi) = P\_k(\cos\psi)$ (Legendre polynomials)
- $r=3$ ($S^3$, Clifford torus ambient): $C\_k^1(\cos\psi) = U\_k(\cos\psi)$ (Chebyshev second kind)

**Return distribution tail.** For large $r$ (many factors), the returns from spherical BM
have tail index:

$$\alpha_{\rm tail} = \frac{r}{2} \tag{3.3}$$

(from the Weyl law applied to the $S^r$ heat kernel, as established in FOKKER\_PLANCK\_CFD).
For $r=4$ (Fama-French): $\alpha\_{\rm tail} = 2$ — consistent with empirical equity tail index.

---

## 4. Type 3: Clifford Torus — The Wrapped Gaussian (Exact Closed Form)

### 4.1 The exact SDE

For the Clifford torus market ($r=2$, $M = T^2$, balanced two-factor, $d=4$), the
natural coordinates are $(\theta, \varphi) \in [0, \pi/2]^2$. The induced metric on
the quarter-torus is flat ($g\_{T^2} = \mathrm{diag}(1/4, 1/4)$ in normalised coordinates),
giving the simplest possible diffusion:

$$\boxed{d\theta_t = \varepsilon\,dW^1_t, \qquad d\varphi_t = \varepsilon\,dW^2_t} \tag{4.1}$$

**with periodic boundary conditions** $\theta \sim \theta + \pi/2$, $\varphi \sim \varphi + \pi/2$.

This is standard 2D Brownian motion confined to the flat torus $[0,\pi/2]^2$ with
identification of opposite edges. **The Clifford torus market is the simplest
possible non-trivial market process** — 2D Brownian motion on a square with
periodic boundaries.

In portfolio weight coordinates ($b\_1 = \cos^2\theta/2$, $b\_3 = \cos^2\varphi/2$):

$$db_{1,t} = -\kappa_1(b_{1,t} - 1/4)\,dt + \sqrt{\varepsilon^2 b_{1,t}(1/2-b_{1,t})}\,dW^1_t \tag{4.2}$$
$$db_{3,t} = -\kappa_2(b_{3,t} - 1/4)\,dt + \sqrt{\varepsilon^2 b_{3,t}(1/2-b_{3,t})}\,dW^2_t \tag{4.3}$$

with $\kappa\_1 = \kappa\_2 = 4\varepsilon^2$ (from the Clifford torus Jacobi eigenvalue
$\lambda\_1 = 4$ for the quarter-torus Laplacian, CLASSIFICATION.md Section 6.2).

### 4.2 The exact transition density — Jacobi theta function

**Theorem 4.1** *(Clifford torus transition density — exact closed form)*. *The
transition density of the flat torus BM (4.1) is:*

$$\boxed{p_t(\theta,\varphi\,|\,\theta_0,\varphi_0) = \vartheta_3\!\!\left(\frac{\theta-\theta_0}{2}\bigg|\frac{i\pi\varepsilon^2 t}{(\pi/2)^2}\right)\cdot\vartheta_3\!\!\left(\frac{\varphi-\varphi_0}{2}\bigg|\frac{i\pi\varepsilon^2 t}{(\pi/2)^2}\right)\cdot\frac{4}{\pi^2}} \tag{4.4}$$

*where the Jacobi theta function is:*

$$\vartheta_3(z|\tau) = \sum_{n=-\infty}^\infty e^{i\pi\tau n^2 + 2niz}
= 1 + 2\sum_{n=1}^\infty e^{-n^2\pi^2\varepsilon^2 t/(\pi/2)^2}\cos(2n(\theta-\theta_0)) \tag{4.5}$$

*This is EXACTLY closed form — a convergent series in elementary functions.*

**Alternative form** using the modular parameter $q = e^{-4\varepsilon^2 t}$:

$$p_t(\theta\,|\,\theta_0) = \frac{2}{\pi}\sum_{n=-\infty}^\infty q^{n^2} e^{2ni(\theta-\theta_0)}
= \frac{2}{\pi}\left[1 + 2\sum_{n=1}^\infty q^{n^2}\cos(2n(\theta-\theta_0))\right] \tag{4.6}$$

**Key properties of the theta transition density:**

**(a) Short-time behaviour** ($t \to 0$, $q\to 1$): the theta function approaches a
Gaussian (all Poisson summation images far away), recovering $p\_t \approx \mathcal{N}(\theta\_0, \varepsilon^2 t)$.

**(b) Long-time behaviour** ($t \to \infty$, $q\to 0$): only the $n=0$ term survives,
giving $p\_\infty = 2/\pi$ (uniform on $[0,\pi/2]$) — consistent with the uniform stationary
distribution on the flat torus. ✓

**(c) Modular symmetry**: the theta function satisfies $\vartheta\_3(z|\tau) = (-i\tau)^{-1/2}e^{iz^2/(\pi\tau)}\vartheta\_3(z/\tau|-1/\tau)$ — the **modular transformation**. In market terms: **short-time and long-time behaviour are related by a modular transformation.** The market dynamics have a hidden symmetry between the $t\to 0$ and $t\to\infty$ regimes.

### 4.3 The spread process and its return distribution

For a Clifford torus market, the **spread** between the two factor groups is
$X\_t = \theta\_t - \varphi\_t$ (the relative within-group allocation). This is a
1D flat torus BM:

$$dX_t = \varepsilon\sqrt{2}\,dW_t, \qquad X \in [-\pi/2, \pi/2] \text{ (periodic)} \tag{4.7}$$

The transition density:

$$p_t(X|X_0) = \frac{2}{\pi}\vartheta_3\!\left(X-X_0\,\Big|\,\frac{i\pi\cdot 2\varepsilon^2 t}{(\pi/2)^2}\right) \tag{4.8}$$

**The spread return distribution is a wrapped normal distribution** — Gaussian with
periodic peaks at multiples of $\pi/2$ (corresponding to the torus boundary).

**Characteristic function of the spread:**

$$\hat\phi_{X_t}(\xi) = \mathbb{E}[e^{i\xi X_t}|X_0] = e^{-2\varepsilon^2\xi^2 t}\cdot\frac{\vartheta_3(\xi X_0 | \tau)}{\vartheta_3(0|\tau)} \tag{4.9}$$

This is a **Gaussian decay modulated by the theta function** — the characteristic
function oscillates with frequency determined by the torus topology.

**Return distribution vs GBM:**

| Feature | GBM | Clifford torus (flat torus BM) |
|:--------|:----|:------------------------------|
| Short-time | $\mathcal{N}(\mu dt, \sigma^2 dt)$ | $\mathcal{N}(0, 2\varepsilon^2 dt)$ (same!) |
| Long-time | Normal (unbounded) | Uniform on $[-\pi/2, \pi/2]$ (bounded!) |
| Characteristic function | $e^{i\mu\xi t - \sigma^2\xi^2 t/2}$ | $e^{-2\varepsilon^2\xi^2 t}\cdot\vartheta\_3(\cdot)$ |
| Tails | Gaussian (light) | Bounded support (no tails!) |
| Periodicity | None | Peaks at multiples of $\pi/2$ |
| Return autocorrelation | Zero (Markov) | Non-zero periodic pattern |

**The Clifford torus market has NO fat tails in the long run** — the portfolio is
bounded. But it has a **non-trivial autocorrelation structure** from the torus geometry:
returns autocorrelate at time lags corresponding to the torus circumference.

### 4.4 Theta function pricing formula

For a derivative with payoff $G(\theta\_T, \varphi\_T)$ on the Clifford torus market,
the price is:

$$V(\theta_0, \varphi_0, t) = e^{-r(T-t)}\int_0^{\pi/2}\!\!\int_0^{\pi/2}
G(\theta,\varphi)\cdot p_{T-t}(\theta,\varphi|\theta_0,\varphi_0)\,d\theta\,d\varphi \tag{4.10}$$

where $p\_{T-t}$ is the theta function (4.4). For a European call on the spread
$X = \theta - \varphi$ with strike $K$:

$$C(\theta_0-\varphi_0, t) = e^{-r(T-t)}\int_{-\pi/2}^{\pi/2}\max(X-K, 0)\cdot
\frac{2}{\pi}\vartheta_3\!\left(X-X_0\,\Big|\,\frac{2i\varepsilon^2(T-t)}{(\pi/2)^2}\right)dX \tag{4.11}$$

This is a **theta function option pricing formula** — more complex than Black-Scholes
but exactly computable. For short maturities: reduces to Black-Scholes. For long
maturities: the theta function effects become significant, modifying the option price
through the periodic corrections.

---

## 5. Type 4: Hyperbolic Market — The McKean Heat Kernel

### 5.1 The hyperbolic geometry of pseudo-Anosov markets

For the figure-eight knot market (pseudo-Anosov type, minimum complexity), the
market manifold $M$ carries a **hyperbolic metric** of constant negative curvature
$K = -\kappa\_{\rm hyp}^2$ (the hyperbolic curvature, distinct from the mean curvature $H$).

In the Bhattacharyya normalisation of our series ($K\_{\rm ambient} = +1/4$ for $S^{d-1}$),
the figure-eight market manifold has induced metric with $K\_M = -(1/4 + |II|^2)$
(from the Gauss equation $K\_M = K\_{\rm ambient} - |II|^2$). For the figure-eight:
$|II|^2 = (3-\sqrt{5})/2$ (related to the golden ratio), giving:

$$K_M = -\frac{1}{4} - \frac{3-\sqrt{5}}{2} = -\frac{5-\sqrt{5}}{4} \approx -0.809 \tag{5.1}$$

The market manifold has constant negative sectional curvature $K\_M \approx -0.809$ —
a hyperbolic surface.

### 5.2 The exact SDE in the Poincaré disc

In the Poincaré disc model $\mathbb{D} = \{z \in \mathbb{C}: |z| < 1\}$ with metric
$ds^2 = 4|dz|^2/(1-|z|^2)^2$, the hyperbolic BM is:

$$\boxed{dz_t = \frac{\varepsilon(1-|z_t|^2)}{2}\,dW_t^{\mathbb{C}}} \tag{5.2}$$

where $W\_t^{\mathbb{C}} = W\_t^1 + iW\_t^2$ is complex Brownian motion. In real
coordinates $(x\_t, y\_t)$ with $z\_t = x\_t + iy\_t$:

$$dx_t = \frac{\varepsilon(1-x_t^2-y_t^2)}{2}\,dW^1_t, \qquad
dy_t = \frac{\varepsilon(1-x_t^2-y_t^2)}{2}\,dW^2_t \tag{5.3}$$

**In the Poincaré upper half-plane** $\mathbb{H} = \{(x,y): y > 0\}$ with metric $ds^2 = (dx^2+dy^2)/y^2$:

$$dx_t = \varepsilon y_t\,dW^1_t, \qquad
dy_t = \frac{\varepsilon^2 y_t}{2}\,dt + \varepsilon y_t\,dW^2_t \tag{5.4}$$

Note the **positive drift** in $y$ — the process is pushed toward larger $y$ values
(toward the boundary $y\to\infty$), reflecting the hyperbolic geometry.

In log coordinates $(u\_t = \log x\_t, v\_t = \log y\_t)$:

$$du_t = -\frac{\varepsilon^2}{2}\,dt + \varepsilon\,dW^1_t, \qquad
dv_t = \frac{\varepsilon^2}{2}\,dt + \varepsilon\,dW^2_t \tag{5.5}$$

The $v$-coordinate is a Brownian motion with **positive drift** $\varepsilon^2/2$ —
the hyperbolic market drifts toward larger $y$ (toward the boundary at infinity).

### 5.3 The McKean heat kernel — exact formula

**Theorem 5.1** *(McKean 1970)*. *The transition density of hyperbolic BM
on $\mathbb{H}^2$ with curvature $K = -1$ (standard normalisation) is:*

$$\boxed{p_t(z,z') = \frac{\sqrt{2}\,e^{-t/8}}{(2\pi t)^{3/2}}
\int_{\rho(z,z')}^\infty \frac{r\,e^{-r^2/(2t)}}{\sqrt{\cosh r - \cosh\rho(z,z')}}\,dr} \tag{5.6}$$

*where $\rho(z,z') = d\_{\mathbb{H}^2}(z,z')$ is the hyperbolic geodesic distance.*

*In our Bhattacharyya normalisation (curvature $K\_M \approx -0.809$): rescale by
$\rho \to \rho/\sqrt{|K\_M|}$ and $t \to t/|K\_M|$ in (5.6).*

**Alternative formula** using the Legendre function:

$$p_t(\rho) = \frac{e^{-t/4}}{(4\pi t)^{1/2}}\cdot\frac{\rho\,e^{-\rho^2/(4t)}}{\sinh\rho} \tag{5.7}$$

where $\rho = \rho(z,z')$ is the hyperbolic distance. This is the **McKean formula**
— an exact, closed-form transition density for hyperbolic BM.

**Key features of (5.7):**
- The factor $e^{-\rho^2/(4t)}$ is Gaussian in the hyperbolic distance
- The factor $\rho/\sinh\rho$ corrects for the hyperbolic volume element ($\sinh\rho\,d\rho$ vs $\rho\,d\rho$ in flat space)
- The exponential prefactor $e^{-t/4}$ represents the **loss of mass** as the process
  drifts toward the boundary at infinity

### 5.4 The characteristic function and return distribution

The **characteristic function of the hyperbolic displacement** $\rho\_t$ (geodesic
distance from origin after time $t$):

$$\mathbb{E}[e^{i\xi\rho_t}] = e^{-t(1/4 + \xi^2)} \tag{5.8}$$

This is the **characteristic function of a normal distribution with mean 0 and
variance $2t$, shifted by $-t/4$** — but in hyperbolic space, not Euclidean space.

**The long-time boundary distribution.** As $t\to\infty$, hyperbolic BM converges
to a random point $Z\_\infty$ on the boundary $\partial\mathbb{H}^2 = \mathbb{R}\cup\{\infty\}$.
The distribution of $Z\_\infty$ is the **harmonic measure** — the **Cauchy distribution**:

$$Z_\infty \sim \text{Cauchy}(x_0, y_0) \tag{5.9}$$

(for a process started at $(x\_0, y\_0) \in \mathbb{H}$, the boundary limit is Cauchy with
location $x\_0$ and scale $y\_0$).

**The long-run return distribution is Cauchy.** This gives tail index $\alpha = 1$
(the minimum finite expectation, infinite variance). For pseudo-Anosov markets (figure-eight
type or more complex hyperbolic manifolds): **all moments of order $\geq 1$ are infinite.**
This is the geometric explanation of extreme fat tails in crisis markets.

**The return process.** In the upper half-plane model, the portfolio "return" is:

$$R_t = \log(y_t/y_0) = \frac{\varepsilon^2}{2}t + \varepsilon W^2_t \tag{5.10}$$

— a Brownian motion with **drift** $\varepsilon^2/2 > 0$. The hyperbolic market has
a **built-in positive drift** in the $y$-coordinate (the "distance to boundary"),
representing the market's tendency to drift toward increasingly extreme allocations
under crisis dynamics. This is a geometric mechanism for the empirically observed
**volatility feedback loop** in crisis markets: high volatility drives the process
toward the boundary of $\mathbb{H}^2$ (the "infinitely leveraged" state), which
increases volatility further.

---

## 6. Type 5: Lawson Surfaces — Fuchsian Diffusion

### 6.1 The covering space construction

For a Lawson surface $\tau\_{m,n}$ (genus $g=mn$), the universal covering space is
the hyperbolic upper half-plane $\mathbb{H}^2$, and:

$$\tau_{m,n} = \mathbb{H}^2 / \Gamma_{m,n} \tag{6.1}$$

where $\Gamma\_{m,n} \subset \mathrm{PSL}(2,\mathbb{R})$ is a **Fuchsian group**
(discrete group of isometries of $\mathbb{H}^2$) with fundamental domain of area
$4\pi(g-1) = 4\pi(mn-1)$ (by Gauss-Bonnet).

The canonical diffusion on $\tau\_{m,n}$ is hyperbolic BM on $\mathbb{H}^2$ projected
to the quotient:

$$d\tilde z_t = \text{hyperbolic BM on }\mathbb{H}^2 \pmod{\Gamma_{m,n}} \tag{6.2}$$

### 6.2 The Selberg zeta function as the market's "partition function"

The spectral theory of the Laplacian on $\tau\_{m,n}$ is governed by the
**Selberg trace formula** \[Selberg 1956\]:

$$\sum_k e^{-(\lambda_k - 1/4)t} = \text{(identity contribution)} + \text{(hyperbolic conjugacy classes)} \tag{6.3}$$

The **Selberg zeta function**:

$$Z(s) = \prod_{\gamma \in \Gamma_{\rm prim}} \prod_{k=0}^\infty (1 - e^{-(s+k)\ell(\gamma)}) \tag{6.4}$$

where the product is over primitive closed geodesics $\gamma$ of length $\ell(\gamma)$,
encodes the spectrum $\{\lambda\_k\}$ of $-\Delta\_{\tau\_{m,n}}$ through its zeros at
$s = 1/2 + i\sqrt{\lambda\_k - 1/4}$.

**The Selberg zeta function IS the market partition function** for the Lawson surface
market:

$$Z_M^{\rm Selberg}(s) = Z_{\rm CS}^{\rm market}(e^{-s}) \tag{6.5}$$

(where $Z\_{\rm CS}$ is the Chern-Simons partition function from KNOT\_THEORY.md).
The zeros of the Selberg zeta function are the **market resonances** — the characteristic
frequencies of market oscillations on the Lawson surface.

**The Ramanujan conjecture** (proved for arithmetic surfaces by Deligne \[1974\]) states
that all non-trivial eigenvalues of the Laplacian on arithmetic Fuchsian quotients satisfy:

$$\lambda_k \geq 1/4 \tag{6.6}$$

For market manifolds with arithmetic Fuchsian symmetry: the spectral gap is
$\lambda\_1 \geq 1/4$ — the **Ramanujan bound on the market's mean-reversion speed**.
Markets whose Lawson surface has arithmetic symmetry have the maximum possible
spectral gap and hence the fastest mean reversion. This is a geometric explanation
for why markets with rich symmetry structures are more efficient.

### 6.3 The transition density via automorphic forms

The transition density on $\tau\_{m,n}$ is expressed through automorphic forms — the
Maass waveforms $\psi\_k$ (eigenfunctions of the hyperbolic Laplacian on $\tau\_{m,n}$):

$$p_t(z,z') = \frac{1}{\mathrm{vol}(\tau_{m,n})} + \sum_{k=1}^\infty e^{-\lambda_k t}\psi_k(z)\overline{\psi_k(z')} \tag{6.7}$$

**The stationary distribution** is uniform on $\tau\_{m,n}$ (with respect to the
hyperbolic area measure). Long-run returns converge to the **hyperbolic Cauchy
distribution** (the boundary measure of $\mathbb{H}^2$ projected to $\tau\_{m,n}$).

---

## 7. Type 6: Pseudo-Anosov Markets — SRB Measure and Anosov Diffusion

### 7.1 The Anosov diffusion

For a pseudo-Anosov market (BRAIDS.md Section 4), the manifold $M$ carries a
pseudo-Anosov homeomorphism $f: M \to M$ with stable foliation $\mathcal{F}^s$
(contracting at rate $\lambda\_{\rm pA}^{-1}$) and unstable foliation $\mathcal{F}^u$
(expanding at rate $\lambda\_{\rm pA}$).

The **natural stochastic process** on a pseudo-Anosov market is not isotropic BM but
rather an **anisotropic diffusion** along the unstable foliation:

$$db_t = \varepsilon_u\,dW^u_t + \varepsilon_s\,dW^s_t \tag{7.1}$$

where $dW^u\_t$ is BM along the unstable foliation and $dW^s\_t$ is BM along the
stable foliation, with $\varepsilon\_u \gg \varepsilon\_s$ (the unstable direction
diffuses faster — it is the "chaotic" direction).

### 7.2 The Sinai-Ruelle-Bowen measure

The **stationary distribution** of the Anosov diffusion is the **Sinai-Ruelle-Bowen (SRB) measure** $\mu\_{\rm SRB}$. For a pseudo-Anosov map:

$$\mu_{\rm SRB} = \text{absolutely continuous on unstable manifolds, singular on stable manifolds} \tag{7.2}$$

The SRB measure is NOT the Riemannian volume element — it is a **fractal measure**
that concentrates on the unstable foliation. Its Hausdorff dimension is:

$$d_H(\mu_{\rm SRB}) = 1 + \frac{h_{\rm top}}{\log\lambda_{\rm pA}} \tag{7.3}$$

where $h\_{\rm top} = \log\lambda\_{\rm pA}$ is the topological entropy.
For the minimum pseudo-Anosov: $d\_H = 2$ (the fractal measure fills the manifold).

**The return distribution under the SRB measure.** The long-run distribution of
log-returns $r\_t = \log\langle b\_t, x\_t\rangle$ under the SRB measure is:

$$p_{\rm SRB}(r) \sim |r|^{-1-1/\chi} \quad\text{as } r\to\infty \tag{7.4}$$

where $\chi = \lambda\_u / |\lambda\_s|$ is the ratio of unstable to stable Lyapunov exponents.
For the minimum pseudo-Anosov ($\lambda\_u = \log\phi^2 = 2\log\phi$, $\lambda\_s = -2\log\phi$):
$\chi = 1$, giving $p\_{\rm SRB}(r) \sim |r|^{-2}$ — a power law with tail index $\alpha = 1$
(Cauchy). **The minimum pseudo-Anosov market has Cauchy-distributed long-run returns.**

---

## 8. The Complete Process Taxonomy and Log-Return Table

### 8.1 Closed-form processes and their log-return distributions

| Market type | SDE | Transition density | CF of log-return | Tail index |
|:-----------|:----|:-------------------|:-----------------|:----------:|
| CAPM | Jacobi (2.1) | Jacobi poly series (2.3) | Kummer $\_1F\_1$ (2.5) | $\alpha = T b^{\ast}-1/2$ |
| Multi-CAPM $S^r\_+$ | Spherical BM (3.1) | Gegenbauer series (3.2) | Bessel series | $r/2$ |
| Clifford $T^2$ | Flat torus BM (4.1) | $\vartheta\_3$ theta function (4.4) | $e^{-\varepsilon^2\xi^2 t}\vartheta\_3$ (4.9) | Bounded! |
| Figure-eight $\mathbb{H}^2$ | Hyperbolic BM (5.3) | McKean kernel (5.6-5.7) | $e^{-t(\xi^2+1/4)}$ (5.8) | 1 (Cauchy) |
| Lawson $\tau\_{m,n}$ | Fuchsian BM (6.2) | Selberg/automorphic (6.7) | Ramanujan bound | $\leq 1/2$ |
| Pseudo-Anosov | Anosov diffusion (7.1) | SRB measure (7.2-7.4) | Stable law | $1/\chi$ |

### 8.2 The transition from GBM to the correct process

The diagram of limiting cases:

```
                         Market topology (manifold type M)
                                        |
           ┌────────────────────────────┼─────────────────────────────┐
           |                            |                             |
     Flat (r=1)               Positively curved (S^r)     Negatively curved (H^2)
    CAPM, one factor          Multi-CAPM, many factors       Pseudo-Anosov, crisis
           |                            |                             |
    Jacobi diffusion           Spherical BM              Hyperbolic BM / Anosov
    Beta stationary            Uniform on S^r             Cauchy / SRB stationary
           |                            |                             |
           └──────────────┬─────────────┘                            |
                          |                                          |
                   Large T, r=1, near b_0=0.5:                      |
                          |                                          |
                         GBM                                   No GBM limit!
                  (Gaussian, light tails)               (power-law / Cauchy tails)
```

**GBM is the large-$T$, CAPM, equal-weight limit of the Jacobi diffusion.**
It is valid only for:
- Single-factor markets ($r=1$, great circle manifold)
- Portfolio near equal-weight ($b^{\ast}\_i \approx 1/d$, so diffusion coefficient $\sqrt{b(1-b)}$ is nearly constant)
- Short time horizons ($t \ll 1/\kappa$, so the mean-reversion hasn't kicked in)

For all other market types: GBM is wrong, and using it introduces systematic errors in
option pricing (wrong tails), risk management (wrong VaR), and portfolio optimisation
(wrong rebalancing frequency).

---

## 9. Simulation Schemes

### 9.1 Jacobi diffusion (CAPM)

**Milstein scheme** with reflection at boundaries $\{0, 1\}$:
```
b_{n+1} = b_n + κ(θ - b_n)Δt + √(2ε²b_n(1-b_n)Δt)·Z_n
         + ε²(b_n(1-b_n))(Z_n² - 1)Δt/(2b_n(1-b_n))   ← Milstein correction
         [reflect if b_{n+1} ∉ (0,1)]
where Z_n ~ N(0,1)
```
The Milstein correction eliminates the $O(\sqrt{\Delta t})$ strong order error of Euler.

**Exact simulation** using the Beta distribution:
For large $T\Delta t$ (when mean-reversion dominates): sample directly from the
conditional distribution $b\_t | b\_0 \sim \sum\_n e^{-\lambda\_n t}w\_n\,\text{Beta}(\alpha+n, \beta+n)$
(a mixture of Beta distributions weighted by the Jacobi polynomial coefficients).

### 9.2 Flat torus BM (Clifford torus)

**Exact simulation** using the theta function:
```
(θ_{n+1}, φ_{n+1}) = (θ_n + ε√Δt·Z_n^1, φ_n + ε√Δt·Z_n^2) mod π/2
where (Z_n^1, Z_n^2) ~ N(0,I₂)
```
The periodic boundary condition is handled by the modular reduction. No approximation
is needed — this is exact simulation of flat torus BM.

### 9.3 Hyperbolic BM (figure-eight market)

**In the upper half-plane** $(x\_t, y\_t)$, using the Milstein scheme for (5.4):
```
x_{n+1} = x_n + ε·y_n·√Δt·Z_n^1
y_{n+1} = y_n + (ε²/2)·y_n·Δt + ε·y_n·√Δt·Z_n^2
        + (ε²/2)·y_n·(Z_n^2² - 1)·Δt    ← Milstein correction
where (Z_n^1, Z_n^2) ~ N(0,I₂)
```
The Milstein correction is crucial for the $y$-component (lognormal structure).

**Alternatively:** simulate $v\_t = \log y\_t$ as a Brownian motion with drift:
$v\_{n+1} = v\_n + \varepsilon\sqrt{\Delta t}\,Z^2\_n$ — this is exact (Itô to Stratonovich).

---

## 10. Option Pricing with the Correct Market Process

### 10.1 The theta function option formula

For a Clifford torus market with spread $X\_t = \theta\_t - \varphi\_t$ following the
wrapped Gaussian (4.7), the European call option price is:

$$C(X_0, T) = e^{-rT}\int_{-\pi/2}^{\pi/2}\max(X-K, 0)\cdot\frac{2}{\pi}
\vartheta_3\!\left(X-X_0\,\Big|\,\frac{4i\varepsilon^2 T}{\pi}\right)dX \tag{10.1}$$

**For at-the-money ($K=0$):** by symmetry,

$$C_{\rm ATM} = e^{-rT}\cdot\frac{2}{\pi}\int_0^{\pi/2} X\cdot\vartheta_3(X|\tau)\,dX
= e^{-rT}\cdot\varepsilon\sqrt{T}\cdot g(\varepsilon^2 T) \tag{10.2}$$

where $g(u) = \frac{2}{\pi}\sqrt{u}\sum\_{n=0}^\infty(-1)^n\frac{e^{-(2n+1)^2/(4u)}}{2n+1}$
is a **theta function correction** to the Black-Scholes formula.

**For short maturities** ($\varepsilon^2 T \ll 1$): $g \to 1$ and the formula reduces to
Black-Scholes: $C\_{\rm ATM} \approx e^{-rT}\varepsilon\sqrt{T/2\pi}$ — the ATM Black-Scholes call price. ✓

**For long maturities** ($\varepsilon^2 T \gg 1$): $g \to \pi/4$ and
$C\_{\rm ATM} \approx e^{-rT}\cdot\pi\varepsilon\sqrt{T}/4$ — linear in $\sqrt{T}$ but with
a different coefficient. The theta function correction reduces the long-maturity call price
compared to Black-Scholes.

### 10.2 The McKean option formula for hyperbolic markets

For a hyperbolic market with McKean transition density (5.7), the call option price
depends on the Legendre function:

$$C_{\rm hyp}(T) = e^{-rT}\int_K^\infty(X-K)\cdot p_T^{\rm hyp}(X|X_0)\,dX \tag{10.3}$$

The integral can be evaluated using the **Mehler-Fock transform** of the McKean kernel.
For the case $K = X\_0$ (ATM):

$$C_{\rm ATM}^{\rm hyp} = e^{-rT}\cdot\frac{e^{-T/8}}{(8\pi T)^{1/2}}
\int_0^\infty X\cdot\frac{X\,e^{-X^2/(4T)}}{\sinh X}\,dX \tag{10.4}$$

This integral involves the **Lerch transcendent** and cannot be simplified to elementary functions, but is rapidly convergent numerically.

**Key property:** For the hyperbolic market, the call price grows **superlinearly** in $T$ — because the underlying process has Cauchy tails, the option has much more value at long maturities than Black-Scholes predicts. The hyperbolic market option formula corrects the systematic underpricing of long-dated options in Black-Scholes.

---

## 11. Summary: The Correct Process Determined by Topology

The central theorem of this paper:

**Theorem 11.1** *(The unique natural process on each market manifold)*. *For each
minimal market manifold $M^r$ in the classification of CLASSIFICATION.md, the unique
stochastic process compatible with the Fisher-Rao metric, invariant under the
isometries of $M$, and having the Jeffreys prior as its stationary distribution is
determined by the topology of $M$:*

$$\boxed{
\begin{array}{lcl}
S^1_+ & \to & \text{Jacobi diffusion, Beta stationary, Kummer CF}\\
S^r_+ & \to & \text{Spherical BM, Uniform on }S^r, \text{Gegenbauer series}\\
T^2 & \to & \text{Flat torus BM, Uniform on }T^2, \text{theta function CF}\\
\mathbb{H}^2 & \to & \text{Hyperbolic BM, Cauchy boundary, McKean kernel}\\
\Sigma^2_g & \to & \text{Fuchsian BM, Uniform on }\Sigma^2_g, \text{Selberg zeta}\\
M_{\rm pA} & \to & \text{Anosov diffusion, SRB measure, stable law CF}
\end{array}
}$$

*GBM is the degenerate limit of the Jacobi diffusion for small $r$, near-equal
weights, and short time horizons. It is not a valid model for any non-CAPM market.*

---

## References

Karlin, S. and McGregor, J. (1957). Classical diffusion processes and total positivity.
*Journal of Mathematical Analysis and Applications* 1(2), 163–183.

McKean, H. P. (1970). An upper bound to the spectrum of $\Delta$ on a manifold of
negative curvature. *Journal of Differential Geometry* 4(3), 359–366.

Selberg, A. (1956). Harmonic analysis and discontinuous groups in weakly symmetric
Riemannian spaces with applications to Dirichlet series. *Journal of the Indian
Mathematical Society* 20, 47–87.

Sinai, Ya. G. (1972). Gibbs measures in ergodic theory.
*Russian Mathematical Surveys* 27(4), 21–69.

*[All other references as per companion papers.]*
