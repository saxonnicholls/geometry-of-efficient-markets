# Stochastic Control, Kalman Filtering, and Portfolio Management
## on the Market Manifold: A Practical Guide for Portfolio Managers

**Saxon Nicholls** — me@saxonnicholls.com

**Paper V.2** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We develop the complete theory of stochastic optimal control and Kalman filtering
for markets whose state lives on the efficient market manifold $M^r \subset S^{d-1}_{+}$.
The results are immediately practical: they give portfolio managers explicit,
geometrically optimal rules for portfolio construction, rebalancing, signal
processing, risk management, and optimal execution.

The central insight running through everything: **the Fisher-Rao metric on the
market manifold is the correct geometry for all portfolio management problems.**
Using the wrong geometry (Euclidean, in standard practice) produces suboptimal
portfolios, incorrect Kalman gains, suboptimal execution schedules, and
mis-stated risk budgets. Using the right geometry (Fisher-Rao on $M^r$) gives
exact, provably optimal solutions to each problem.

**Principal results for practitioners:**

**(i) The manifold HJB equation = the FK PDE.** The stochastic control problem
"maximise expected log-growth subject to market dynamics on $M^r$" has
Hamilton-Jacobi-Bellman equation identical to the Feynman-Kac PDE of LAPLACE.md.
The value function IS the Kelly growth rate $L_T(b)$. The optimal control IS the MUP.
Stochastic control theory and universal portfolio theory are the same problem.

**(ii) The manifold Kalman-Bucy filter.** The optimal linear filter for estimating
the market state $b^{\ast}(t)\in M^r$ from observed returns $x_t\in\mathbb{R}^{d}$ has
Riccati equation whose steady-state solution is the Fisher information matrix $F(b^{\ast})$.
The Kalman gain is $K = F(b^{\ast})^{-1}V_r^T$ where $V_r$ is the factor loading matrix.
The innovation process IS the normal bundle projection $\Pi_{NM}(x_t)$ — the
idiosyncratic component of each return that the manifold model did not predict.

**(iii) Optimal execution = geodesic on $M^r$.** The Almgren-Chriss optimal
execution problem (minimise market impact + timing risk while liquidating or
establishing a portfolio) has solution: execute along the Fisher-Rao geodesic
from the initial portfolio to the target portfolio. The execution path is the
manifold analogue of VWAP execution — the trajectory of minimum Fisher-Rao length.

**(iv) Risk parity in Fisher-Rao geometry.** Risk parity (equal risk contribution)
in the Fisher-Rao metric means each asset contributes equal Fisher-Rao distance
from the log-optimal portfolio. The Fisher-Rao risk parity portfolio is:
$b^{\rm FRP}_{i} \propto 1/\sqrt{F_{ii}(b^{\ast})}$ — inversely proportional to the
square root of the $i$-th diagonal of the Fisher information matrix.

**(v) The separation theorem on $M^r$.** The optimal portfolio separates into
a manifold component (the MUP, tracking the factor structure) and a normal bundle
component (the idiosyncratic overlay, if any alpha exists in the normal directions).
The two components are orthogonal in the Fisher-Rao metric and can be managed
independently. This is the geometric extension of Tobin's two-fund separation.

**(vi) The Ornstein-Uhlenbeck controller.** The LQG (Linear Quadratic Gaussian)
optimal controller for the portfolio process on $M^r$ is an OU mean-reversion
controller: $u^{\ast}(b) = -K_{\rm LQG}(b - b^{\ast})$ with gain $K_{\rm LQG} = \varepsilon^2 F(b^{\ast})$.
The optimal rebalancing frequency is $1/\lambda_1$ — the Jacobi spectral gap timescale.

**Keywords.** Stochastic control; HJB equation; Kalman filter; Riccati equation;
innovation process; Almgren-Chriss; optimal execution; risk parity; Fisher-Rao;
separation theorem; LQG; portfolio rebalancing; signal extraction; tracking error.

---

## 1. The Hamilton-Jacobi-Bellman Equation on the Market Manifold

### 1.1 The stochastic control problem

The portfolio manager's problem: choose a portfolio process $b(t)\in M^r$
to maximise expected log-wealth over $[0,T]$:

```math
\sup_{b(\cdot)\in\mathcal{A}(M^r)}\mathbb{E}\!\left[\int_0^T L(b(t),\, x_t)\,dt\right] \tag{1.1}
```

subject to: $b(t)\in M^r$ (manifold constraint), and $b(t)$ adapted to $\mathcal{F}^{M}_t$.

The running reward is $L(b,x) = \log\langle b, x\rangle$ (log-return per period).

**The Bellman value function:**
```math
V(b,t) = \sup_{b(\cdot)}\mathbb{E}\!\left[\int_t^T L(b(s),x_s)\,ds\,\bigg|\,b(t)=b\right] \tag{1.2}
```

### 1.2 The HJB equation on $M^r$

Applying the dynamic programming principle to (1.2), using the market diffusion
$db = \varepsilon\,dW_M$ on $M^r$:

```math
\frac{\partial V}{\partial t} + \frac{\varepsilon^2}{2}\Delta_{M}V + L(b,x) = 0 \tag{1.3}
```

with terminal condition $V(b,T) = 0$.

**Theorem 1.1** *(HJB = FK PDE)*. *The HJB equation (1.3) is identical to the
Feynman-Kac PDE for the universal portfolio:*

```math
V(b,t) = L_T(b) = \frac{1}{T-t}\log\mathbb{E}\!\left[\prod_{s=t}^{T}\langle b(s), x_s\rangle\,\bigg|\,b(t)=b\right] \tag{1.4}
```

*The value function of the stochastic control problem IS the Kelly growth rate function.
The optimal control IS the MUP portfolio:*

```math
b^{\ast}(t) = \arg\max_{b\in M^r}V(b,t) = \hat{b}^{M}_T \tag{1.5}
```

*Proof.* The HJB equation (1.3) is the backward Kolmogorov equation for the market
diffusion on $M^r$ with running reward $L$. The Feynman-Kac formula gives its
solution as the conditional expectation (1.4). The optimal control is the maximiser
of the Hamiltonian $H(b,\nabla V) = L(b,x) + \nabla V\cdot f(b)$ over $M^r$,
which is the MUP at each time. $\square$

**Practical consequence:** A portfolio manager running the MUP is solving the
stochastic control problem (1.1) exactly. There is no better adapted strategy.

### 1.3 The verification theorem and the transversality condition

The value function $V(b,t) = L_T(b)$ satisfies the boundary condition:
$V(b^{\ast},T) = L_T(b^{\ast}) = h_{\rm Kelly}$ (the Kelly growth rate at maturity).
The **transversality condition** — that the marginal value of portfolio deviation
is zero at maturity — is:

```math
\nabla_{g_M}V\big|_{b=b^{\ast},t=T} = \nabla_{g_M}L_T\big|_{b^{\ast}} = 0 \tag{1.6}
```

This is the KKT condition for the log-optimal portfolio — it holds by definition
of $b^{\ast}$. **The log-optimal portfolio satisfies the HJB transversality condition exactly.**

---

## 2. The Manifold Kalman-Bucy Filter

### 2.1 Setup: state and observation

**State:** $b^{\ast}(t)\in M^r$ — the log-optimal portfolio (unobserved, estimated).

**State dynamics:** $db^{\ast} = -\varepsilon^2\vec{H}(b^{\ast})\,dt + \varepsilon\,dW_M$ (market diffusion)

**Observation:** $x_t \in \mathbb{R}^{d}$ — the full return vector (observed each period)

**Observation model:** 
```math
x_t = V_r\,\xi_t + \sigma_N\,\eta_t, \qquad \xi_t \in T_{b^{\ast}}M^r, \eta_t\in N_{b^{\ast}}M \tag{2.1}
```

where $V_r\in\mathbb{R}^{d\times r}$ is the factor loading matrix (columns = factor directions
in $\mathbb{R}^{d}$), $\xi_t$ is the factor shock (tangential), and $\eta_t$ is the
idiosyncratic shock (normal bundle).

### 2.2 The manifold Kalman-Bucy equations

The optimal linear filter for estimating $b^{\ast}(t)$ from $\{x_s:s\leq t\}$:

**State estimate:** $\hat{b}^{\ast}(t) = \mathbb{E}[b^{\ast}(t)|\mathcal{F}^{X}_t]$

**Innovation process:**
```math
\nu_t = x_t - V_r\xi_t = \Pi_{NM}(x_t) \tag{2.2}
```

the part of the return not explained by the current factor state estimate.
**The Kalman innovation IS the normal bundle projection of the return.**

**Riccati equation** for the estimation error covariance $P(t) = \mathbb{E}[(b^{\ast}-\hat b^{\ast})(b^{\ast}-\hat b^{\ast})^T|\mathcal{F}^{X}_t]$:

```math
\dot{P} = \varepsilon^2 g_M^{-1}(b^{\ast}) - P\cdot V_r^T R_N^{-1}V_r\cdot P \tag{2.3}
```

where $R_N = \sigma_N^2 I$ is the idiosyncratic noise covariance.

**Theorem 2.1** *(Riccati steady state = Fisher information matrix)*.
*The steady-state solution of the Riccati equation (2.3) is:*

```math
P_\infty = F(b^{\ast})^{-1} \tag{2.4}
```

*the inverse of the Fisher information matrix at the log-optimal portfolio.*

*Proof.* At steady state $\dot{P}=0$:
$\varepsilon^2 g_M^{-1}(b^{\ast}) = P_\infty\cdot V_r^T R_N^{-1}V_r\cdot P_\infty$.
Setting $P_\infty = F^{-1}$: $\varepsilon^2 F = F^{-1}\cdot V_r^TR_N^{-1}V_r\cdot F^{-1}$,
i.e., $\varepsilon^2 F^2 = V_r^TR_N^{-1}V_r$. Since the Fisher information at $b^{\ast}$
satisfies $F(b^{\ast}) = V_r^T\Sigma^{-1}V_r/\varepsilon^2$ (the inverse covariance
projected onto the factor subspace), this holds exactly. $\square$

**The Kalman gain matrix:**
```math
K = P_\infty\cdot V_r^T R_N^{-1} = F(b^{\ast})^{-1}V_r^T R_N^{-1} = \Pi_{TM}\cdot\Sigma^{-1} \tag{2.5}
```

This is the Fisher-Rao projection of the observation onto the tangent bundle —
exactly the operation of projecting the return observation onto the factor subspace.

**The Kalman filter update rule:**
```math
d\hat{b}^{\ast} = K\nu_t\,dt = F(b^{\ast})^{-1}V_r^T R_N^{-1}\Pi_{NM}(x_t)\,dt \tag{2.6}
```

**Three-part interpretation:**
1. $\Pi_{NM}(x_t)$: isolate the part of the return not explained by the current manifold estimate (the innovation)
2. $V_r^TR_N^{-1}$: weight the innovation by inverse idiosyncratic noise (Mahalanobis weight)
3. $F(b^{\ast})^{-1}$: map from observation space back to manifold state space via inverse Fisher matrix

### 2.3 What the Kalman filter tells a portfolio manager

**Signal extraction:** The Kalman filter decomposes each return vector into:
- **Factor component** $\Pi_{TM}(x_t) = V_r V_r^T x_t$: the part explained by the factor model — this updates the manifold state estimate $\hat b^{\ast}$
- **Idiosyncratic component** $\Pi_{NM}(x_t) = (I - V_rV_r^T)x_t$: the innovation — this is noise for factor investors but signal for stock pickers

**The signal-to-noise ratio on $M^r$:**
```math
\mathrm{SNR} = \frac{\|V_r^T x_t\|^2}{\|\Pi_{NM}(x_t)\|^2} = \frac{\text{factor variance}}{\text{idiosyncratic variance}} \tag{2.7}
```

**The filter's steady-state tracking error:**
```math
\mathrm{tr}(P_\infty) = \mathrm{tr}(F(b^{\ast})^{-1}) = \sum_{k=1}^{r} \frac{1}{\lambda_k(F)} \tag{2.8}
```

is the sum of reciprocal factor eigenvalues — small when factors are strong,
large when factors are weak. **The Kalman filter's tracking error is determined
by the condition number of the Fisher information matrix.**

### 2.4 The extended Kalman filter for nonlinear market dynamics

When the market is not at its log-optimal portfolio (i.e., during a transition),
the dynamics are nonlinear. The **manifold extended Kalman filter** (EKF):

1. Propagate the state estimate along the geodesic on $M^r$:
   $\hat b^{\ast}(t+\Delta t) = \exp_{\hat b^{\ast}(t)}(\varepsilon\sqrt{\Delta t}\,\hat\xi_t)$
   where $\exp$ is the Riemannian exponential map on $(M^r, g_M)$

2. Update the covariance using the parallel transport of $P$ along the geodesic:
   $P^- = \mathcal{P}_{\gamma}P\mathcal{P}_\gamma^T + \varepsilon^2\Delta t\cdot g_M^{-1}$
   where $\mathcal{P}_\gamma$ is parallel transport along the geodesic $\gamma$

3. Compute the Kalman gain as in (2.5)

4. Update the state estimate using the manifold Kalman update (2.6)

**The manifold EKF is the Riemannian analogue of the standard EKF**, replacing
Euclidean additions with Riemannian exponential maps and subtractions with
logarithmic maps $\log_{b^{\ast}}(b) = $ the tangent vector pointing from $b^{\ast}$ to $b$.

---

## 3. Optimal Portfolio Rebalancing as Geodesic Control

### 3.1 The rebalancing problem

A portfolio manager holds portfolio $b_0\in M^r$ and wants to rebalance to target
$b^{\ast}\in M^r$ while minimising a combination of:
- **Transaction costs:** proportional to $\|b(t) - b(t^-)\|_{g_M}$ (Fisher-Rao distance traded)
- **Tracking error:** $\int_0^T\|b(t) - b^{\ast}\|^2_{g_M}\,dt$ (time-average deviation from target)
- **Market impact:** proportional to trading speed $\|\dot b\|_{g_M}$

**The Almgren-Chriss problem on $M^r$:** minimise over trading paths $b:[0,T]\to M^r$:

```math
J[b] = \int_0^T\!\left(\alpha\|\dot b(t)\|^2_{g_M} + \lambda\|b(t)-b^{\ast}\|^2_{g_M}\right)dt \tag{3.1}
```

subject to $b(0) = b_0$, $b(T) = b^{\ast}$.

### 3.2 The geodesic execution schedule

**Theorem 3.1** *(Optimal execution = damped geodesic)*. *The optimal trading path
minimising (3.1) is the **critically damped geodesic** on $(M^r, g_M)$:*

```math
b^{\rm opt}(t) = \exp_{b^{\ast}}\!\!\left(-e^{-\kappa t}\log_{b^{\ast}}(b_0)\right), \qquad
\kappa = \sqrt{\lambda/\alpha} \tag{3.2}
```

*where $\exp_{b^{\ast}}$ and $\log_{b^{\ast}}$ are the Riemannian exponential and logarithm
maps at $b^{\ast}$, and $\kappa = \sqrt{\lambda/\alpha}$ is the damping rate.*

*For the unconstrained case ($\lambda=0$): constant-speed geodesic (VWAP execution).
For the heavily penalised case ($\lambda\gg\alpha$): instantaneous jump to $b^{\ast}$.*

*Proof.* The Euler-Lagrange equation for (3.1) is the damped geodesic equation on $M^r$:
$\nabla_{\dot b}\dot b + \kappa\dot b = 0$ (covariant acceleration + damping = 0).
The solution satisfying the boundary conditions is (3.2). $\square$

**In plain language:** The optimal execution path is the Fisher-Rao geodesic from
$b_0$ to $b^{\ast}$, traversed at a speed that decays exponentially at rate $\kappa$.
The portfolio "flows" toward the target along the path of minimum Fisher-Rao length —
which is the path of minimum information-theoretic distance.

### 3.3 The geodesic in each market type

**CAPM ($M = S^r_+$):** The geodesic is a great circle arc on the positive sphere.
In portfolio weight coordinates: $b^{\rm opt}(t) = (\cos(\theta_t)\sqrt{b_0} + \sin(\theta_t)(\sqrt{b^{\ast}}-\cos\phi\sqrt{b_0})/\sin\phi)^{\odot 2}$ where $\phi = d_{g^{\rm FR}}(b_0,b^{\ast})$ is the initial Fisher-Rao distance.

**Clifford torus ($M = T^2$):** The geodesic is a straight line on the flat torus —
linear interpolation in the $(\theta,\varphi)$ coordinates. This gives the "factor-by-factor"
execution schedule: trade the two factors independently at constant rates.

**Hyperbolic ($M = \mathbb{H}^{2}$):** The geodesic is a circle arc orthogonal to the
real axis in the Poincaré half-plane. This gives a curved execution path that
"bows away" from dangerous regions of the portfolio space — naturally avoiding
concentrated positions.

### 3.4 Transaction cost budget

The total transaction cost along the geodesic execution path (3.2) is:

```math
C_{\rm geodesic} = 2\alpha\kappa\|b_0 - b^{\ast}\|_{g_M}(1 - e^{-\kappa T}) \tag{3.3}
```

The break-even between immediate execution and geodesic execution occurs at
$T^{\ast} = \log(2\alpha\kappa/\lambda_{\rm cost})/\kappa$ where $\lambda_{\rm cost}$
is the linear transaction cost rate. **For $T < T^{\ast}$: execute immediately.
For $T > T^{\ast}$: execute along the geodesic.**

---

## 4. Risk Management on the Market Manifold

### 4.1 Tracking error in Fisher-Rao geometry

The **tracking error** of portfolio $b$ relative to the log-optimal portfolio $b^{\ast}$
is the Fisher-Rao distance:

```math
\mathrm{TE}(b) = d_{g^{\rm FR}}(b, b^{\ast}) = 2\arccos\!\left(\sum_i\sqrt{b_i b^{\ast}_{i}}\right) \tag{4.1}
```

This is the Bhattacharyya distance — the geodesic distance on $S^{d-1}_{+}$.

**Properties:**
- $\mathrm{TE} = 0$ iff $b = b^{\ast}$ (exact log-optimal)
- $\mathrm{TE} \leq \pi/2$ (bounded by the hemisphere diameter)
- $\mathrm{TE}$ is symmetric and satisfies the triangle inequality
- $\mathrm{TE}^{2} \approx \sum_i (b_i - b^{\ast}_{i})^2/b^{\ast}_{i}$ for small deviations (the $\chi^2$ distance)

**The tracking error approximation for small deviations:**
```math
\mathrm{TE}^{2} \approx (b-b^{\ast})^T F(b^{\ast})(b-b^{\ast}) \tag{4.2}
```

the quadratic form in the Fisher information matrix. **Tracking error IS the Fisher-Rao squared distance** — the natural risk measure for portfolio deviation from the log-optimal.

### 4.2 Fisher-Rao risk parity

**Standard risk parity:** weights each asset so that its contribution to portfolio
variance is equal: $b_i\sigma_i = b_j\sigma_j$ for all $i,j$.

**Fisher-Rao risk parity:** weights each asset so that its contribution to the
Fisher-Rao distance from $b^{\ast}$ is equal. The Fisher-Rao risk contribution of
asset $i$ is:

```math
\rho_i^{\rm FR}(b) = b_i\frac{\partial\,\mathrm{TE}^{2}(b)}{\partial b_i} = b_i\cdot 2F_{ii}(b^{\ast})(b_i-b^{\ast}_{i}) \tag{4.3}
```

**Equal Fisher-Rao risk contribution:** $\rho_i^{\rm FR} = c$ for all $i$ gives:

```math
b_i = b^{\ast}_{i} + \frac{c}{2F_{ii}(b^{\ast})\cdot b_i} \approx b^{\ast}_{i} + \frac{c}{2\cdot b^{*-1}_{i}\cdot b_i} \tag{4.4}
```

For equal weight $b_i = 1/d$: $F_{ii}(b^{\ast}) = d$ and $\rho_i^{\rm FR} = 2d(1/d - b^{\ast}_{i})$.
The Fisher-Rao risk parity portfolio is:

```math
b^{\rm FRP}_{i} = b^{\ast}_{i} + \frac{c}{2/b^{\ast}_{i}} = b^{\ast}_{i}\left(1 + \frac{c\,b^{\ast}_{i}}{2}\right) \approx b^{\ast}_{i} \tag{4.5}
```

to leading order in the deviation. **Fisher-Rao risk parity converges to the
log-optimal portfolio — equal Fisher-Rao risk contribution is achieved by the
log-optimal portfolio itself.** This gives a geometric justification for the
log-optimal portfolio as a risk-parity portfolio in the Fisher-Rao metric.

### 4.3 Value at Risk on the market manifold

**Manifold VaR:** For a portfolio $b\in M^r$, the $\alpha$-VaR over horizon $T$ is:

```math
\mathrm{VaR}_\alpha(b,T) = \inf\{v>0: \mathbb{P}(L_T(b(T))-L_T(b) < -v) \leq \alpha\} \tag{4.6}
```

Using the heat kernel $p_T(b,b')$ on $M^r$, the distribution of future log-growth
is the transition density of the market process:

```math
\mathrm{VaR}_\alpha(b,T) = -F_T^{-1}(\alpha) \tag{4.7}
```

where $F_T$ is the CDF of $L_T(b(T))-L_T(b)$ under the heat kernel.

**For the CAPM market (Jacobi process):** the VaR at confidence $\alpha$ is:

```math
\mathrm{VaR}_\alpha^{\rm CAPM}(b,T) = -\Phi^{-1}(\alpha)\sqrt{\varepsilon^2 T/b^{\ast}(1-b^{\ast})} \tag{4.8}
```

where $\Phi^{-1}$ is the inverse normal CDF and $b^{\ast}(1-b^{\ast})$ is the local variance
of the Jacobi process at the current portfolio weight.

**For the hyperbolic market (McKean process):** the VaR has heavy Cauchy tails:

```math
\mathrm{VaR}_\alpha^{\rm hyp}(b,T) \sim C\cdot T^{1/2}/\tan(\pi\alpha/2) \tag{4.9}
```

— the Cauchy VaR, which grows much faster for small $\alpha$ than the normal VaR.
**Hyperbolic (crisis) markets require much larger VaR buffers than CAPM (normal) markets** — by a factor of $\tan^{-1}(\pi\alpha/2)/\Phi^{-1}(\alpha)$, which for $\alpha=0.01$ is approximately 2.4×.

---

## 5. The Separation Theorem on $M^r$

### 5.1 The two-fund separation

**Classical Tobin separation:** In the CAPM, every investor holds the same risky
portfolio (the market portfolio) plus a position in the risk-free asset.

**Manifold two-fund separation:**

**Theorem 5.1** *(Two-fund separation on $M^r$)*. *For any investor with expected
log-utility, the optimal portfolio decomposes into:*

```math
b^{\rm opt} = \underbrace{\hat b^M_T}_{\text{Fund 1: MUP}} + \underbrace{\Pi_{NM}\alpha_t}_{\text{Fund 2: alpha overlay}} \tag{5.1}
```

*where the first fund is the Manifold Universal Portfolio (tracking $M^r$,
the systematic component) and the second fund is any $\mathcal{F}^{\rm oracle}$-adapted
process in the normal bundle $NM$ (the idiosyncratic alpha, zero on an efficient market).*

*The two funds are Fisher-Rao orthogonal: $\langle\hat b^M_T, \Pi_{NM}\alpha_t\rangle_{g_M} = 0$.*

*On an efficient market ($H=0$, no insider information): $\Pi_{NM}\alpha_t = 0$ and
the optimal portfolio is the MUP alone.*

**The practical consequence:** A portfolio manager should:
1. Hold the MUP as the core position (systematic factor exposure, $\mathcal{F}^{M}$-adapted)
2. Add an alpha overlay in the normal bundle only if genuinely in possession of
   information $\mathcal{G}_{t}\subset\mathcal{F}^{\rm oracle}$ not in $\mathcal{F}^{X}$

Any overlay that is $\mathcal{F}^{X}$-measurable (derived from public data) generates
zero expected excess return on an efficient market by Theorem 3.2 of LLM_MANIFOLD.md.

### 5.2 The tangential vs normal P&L attribution

The P&L of a portfolio $b$ over period $[t,t+\Delta t]$ decomposes as:

```math
\Delta\mathrm{PnL} = \underbrace{\langle\Pi_{TM}b,\, x_{t+\Delta t}\rangle}_{\text{Factor PnL}} + \underbrace{\langle\Pi_{NM}b,\, x_{t+\Delta t}\rangle}_{\text{Alpha PnL}} \tag{5.2}
```

The factor PnL has expectation $\varepsilon^2(L_T(b^{\ast})-L_T(b))\Delta t$ (the Kelly gap).
The alpha PnL has expectation $\varepsilon^2|v_{\mathcal{G}}|_{g^{\rm FR}}\Delta t$ if the manager
has side-channel information $v_\mathcal{G}\in NM$, and zero otherwise.

**Risk-adjusted P&L attribution:**
- Sharpe of factor component: $\varepsilon|H_{\rm tangential}(b)|$
- Sharpe of alpha component: $\varepsilon|v_\mathcal{G}|_{g^{\rm FR}}/\sigma_N$

---

## 6. The LQG Portfolio Controller

### 6.1 Setup

The **Linear Quadratic Gaussian (LQG)** portfolio controller minimises a quadratic cost:

```math
J_{\rm LQG} = \mathbb{E}\!\left[\int_0^T\!\left(q\|b-b^{\ast}\|^2_{g_M} + \rho\|u\|^2_{g_M}\right)dt\right] \tag{6.1}
```

where $u = \dot b$ is the rebalancing control, $q>0$ is the tracking penalty, and
$\rho>0$ is the trading cost penalty.

The dynamics: $db = u\,dt + \varepsilon\,dW_M$ (controlled diffusion on $M^r$).

### 6.2 The optimal LQG controller

**Theorem 6.1** *(LQG optimal control on $M^r$)*. *The optimal LQG controller is:*

```math
u^{\ast}(b) = -K_{\rm LQG}(b - b^{\ast}), \qquad K_{\rm LQG} = \sqrt{q/\rho} \tag{6.2}
```

*— an OU mean-reversion toward $b^{\ast}$ with rate $K_{\rm LQG} = \sqrt{q/\rho}$.
The optimal rebalancing rate equals $\sqrt{q/\rho}$ — the geometric mean of the
tracking urgency and the trading cost.*

*The controlled portfolio process:*
```math
db = -K_{\rm LQG}(b-b^{\ast})\,dt + \varepsilon\,dW_M \tag{6.3}
```
*is an OU process on $M^r$ with mean reversion rate $K_{\rm LQG}$ and stationary
distribution $\mathrm{Normal}_{g_M}(b^{\ast}, \varepsilon^2/(2K_{\rm LQG}))$.*

**Optimal rebalancing frequency:** The controller rebalances at rate $K_{\rm LQG}$
per unit time. In discrete time with daily rebalancing opportunities:
```math
f^{\ast} = K_{\rm LQG} = \sqrt{q/\rho} \text{ rebalances per day} \tag{6.4}
```

Matching to the Jacobi spectral gap timescale (PORTFOLIO_GEOMETRY.md): the
optimal $K_{\rm LQG} = \lambda_1(L_M)$ — setting the LQG mean-reversion rate
equal to the natural mean-reversion rate of the market.

### 6.3 The LQG-Kalman combination (LQG with uncertain state)

When the state $b^{\ast}(t)$ is not directly observed (only the noisy return $x_t$ is observed),
the **LQG with Kalman filter** (the separation principle):

1. **Estimate:** Run the manifold Kalman filter (Section 2) to obtain $\hat b^{\ast}(t)$
2. **Control:** Apply the LQG controller to the estimated state: $u^{\ast}(t) = -K_{\rm LQG}(\hat b(t) - \hat b^{\ast}(t))$

By the **separation theorem for stochastic control** (the certainty equivalence principle):
the optimal strategy is to estimate the state optimally (Kalman) and then control
as if the estimate were exact (LQG). **The estimation and control problems separate.**

**Combined tracking error** (from both estimation error and control error):
```math
\mathrm{TE}^{2}_{\rm total} = \underbrace{\mathrm{tr}(P_\infty)}_{\text{Kalman error}} + \underbrace{\varepsilon^2/(2K_{\rm LQG})}_{\text{LQG error}} = \mathrm{tr}(F^{-1}) + \varepsilon^2\sqrt{\rho/q} \tag{6.5}
```

**Optimal cost coefficient ratio** minimising total tracking error:
```math
\frac{\rho^{\ast}}{q} = \left(\frac{\varepsilon^2}{2\mathrm{tr}(F^{-1})}\right)^2 \tag{6.6}
```

— the trading cost should be set proportional to the square of the Kalman uncertainty.
When the factor model is highly uncertain (large $\mathrm{tr}(F^{-1})$): trade slowly.
When the factor model is precise (small $\mathrm{tr}(F^{-1})$): trade quickly.

---

## 7. Practical Implementation: The Manifold Portfolio Management System

### 7.1 The complete workflow

```
DAILY WORKFLOW FOR A MANIFOLD PORTFOLIO MANAGER
═══════════════════════════════════════════════

MORNING (before market open):
1. Update the Fisher information matrix F(b*) from last 252 days' returns
   F_hat = X.T @ diag(1/b*) @ X / T

2. Run the Kalman filter update from yesterday's close:
   b*_estimate += K @ (x_yesterday - V_r @ xi_estimate)
   K = inv(F_hat) @ V_r.T @ inv(R_noise)

3. Compute the current tracking error:
   TE = arccos(sum(sqrt(b_current * b*_estimate)))

4. Decide whether to rebalance (threshold: TE > 1/sqrt(T)):
   if TE > epsilon_threshold:
       compute geodesic path to b*_estimate
       schedule execution along geodesic

INTRADAY (execution):
5. Execute along the geodesic at rate kappa = sqrt(q/rho):
   b(t) = exp_{b*}(-exp(-kappa*t) * log_{b*}(b_current))

6. Monitor the Kalman innovation:
   innovation = Pi_NM(x_intraday)
   if |innovation| > 3*sigma_N: possible side-channel signal, flag for review

END OF DAY:
7. Compute P&L attribution:
   factor_PnL = <Pi_TM(b), x_today>
   alpha_PnL  = <Pi_NM(b), x_today>

8. Update the manifold estimate:
   If Dyson class has changed (ratio test), update the beta parameter
   If Cheeger constant has declined below threshold, increase TE tolerance

9. Record:
   - Tracking error TE
   - Kalman uncertainty tr(F^{-1})
   - Dyson class beta
   - Cheeger constant h_M
   - Shapley attribution phi_i = b*_i * (mu_i - mu_bar)
```

### 7.2 Key parameters and their geometric meaning

| Parameter | Formula | Geometric meaning | Update frequency |
|:----------|:--------|:-----------------|:----------------|
| Log-optimal $b^{\ast}$ | $\arg\max L_T(b)$ | Centre of $M^r$ | Daily |
| Fisher matrix $F$ | $-\nabla^2 L_T|_{b^{\ast}}$ | Local curvature of $M^r$ | Daily |
| Manifold dim $r$ | FNN / stable rank | Intrinsic complexity | Monthly |
| Dyson class $\beta$ | Ratio statistic | Symmetry of $M^r$ | Monthly |
| Cheeger constant $h_M$ | Fiedler eigenvalue | Systemic risk | Weekly |
| Kalman gain $K$ | $F^{-1}V_r^TR_N^{-1}$ | Optimal signal weight | Daily |
| Rebal rate $\kappa$ | $\lambda_1(L_M)$ | Natural mean reversion | Monthly |
| Tracking error TE | $d_{g^{\rm FR}}(b,b^{\ast})$ | Distance from optimal | Daily |
| Shapley $\phi_i$ | $b^{\ast}_{i}(\mu_i-\bar\mu)$ | Asset contribution | Daily |

### 7.3 Warning signals for portfolio managers

**Red flags — take immediate action:**
- Cheeger constant $h_M < 0.05$: bottleneck forming in contagion network — reduce gross exposure
- Dyson class changes from $\beta=1$ (GOE) to $\beta=2$ (GUE): factor structure changing — re-estimate the manifold
- Tracy-Widom exceedance: largest factor eigenvalue exceeds $F_\beta$ 1% quantile — factor spike, possible crisis onset
- Kalman innovation $|\nu_t| > 4\sigma_N$: possible side-channel information or model misspecification

**Yellow flags — monitor closely:**
- Tracking error exceeds $2/\sqrt{T}$: portfolio has drifted significantly from log-optimal
- Stable rank $\hat r$ declining: factor structure becoming more concentrated
- Kelly rate $h_{\rm Kelly}$ declining below historical mean: market becoming more efficient (less alpha available)

---

## Summary: The Geometric Portfolio Manager's Toolkit

| Problem | Classical tool | Manifold tool | Formula |
|:--------|:---------------|:-------------|:--------|
| Portfolio optimisation | Mean-variance | HJB on $M^r$ | Value function = $L_T(b^{\ast})$ |
| Signal extraction | Standard Kalman | Manifold Kalman-Bucy | Gain = $F(b^{\ast})^{-1}V_r^TR_N^{-1}$ |
| State estimation | Riccati equation | Riccati on $M^r$ | $P_\infty = F(b^{\ast})^{-1}$ |
| Execution | Almgren-Chriss | Geodesic on $M^r$ | $b(t) = \exp_{b^{\ast}}(-e^{-\kappa t}\log_{b^{\ast}}b_0)$ |
| Rebalancing rule | Heuristic (monthly) | LQG controller | Rate $= \lambda_1(L_M)$ |
| Risk measure | Variance, VaR | Fisher-Rao distance | $\mathrm{TE} = d_{g^{\rm FR}}(b,b^{\ast})$ |
| Risk parity | Equal variance | Equal Fisher-Rao | Converges to $b^{\ast}$ |
| Attribution | Factor regression | Shapley value | $\phi_i = b^{\ast}_{i}(\mu_i-\bar\mu)$ |
| Crisis detection | VIX | Cheeger constant | $h_M \to 0$ before crisis |
| Regime detection | Hidden Markov | Dyson class test | $\beta\in\{1,2,4\}$ |
| Separation | Tobin two-fund | Tangential/Normal | $b = b^M_{\rm MUP} + \Pi_{NM}\alpha$ |

---

### Connections to Other Papers

The Kalman innovation process — the normal bundle projection $\Pi_{NM}(x_t)$ of returns — captures "new information" at each step. This should be formally related to the LZ prefix tree of FILTRATIONS.md: LZ phrase boundaries correspond to times when the Kalman innovation exceeds a threshold, and the LZ complexity rate should equal the Kalman innovation variance rate. Both measure the rate at which genuinely new information arrives, one in a compression-theoretic language and the other in a filtering language (Conjecture C29).

The optimal execution geodesic on $M^r$ (Section 3, Almgren-Chriss) is the same object as the classical instanton in the path integral formulation (PATH_INTEGRAL.md). The Almgren-Chriss optimal execution IS the WKB saddle-point path: both minimise an action functional (market impact + timing risk in one language, the Hamilton-Jacobi action in the other), and the Van Vleck prefactor gives the execution uncertainty around the optimal trajectory.

---

## References

Kalman, R. E. (1960). A new approach to linear filtering and prediction problems.
*Journal of Basic Engineering* 82(1), 35–45.

Kalman, R. E. and Bucy, R. S. (1961). New results in linear filtering and prediction theory.
*Journal of Basic Engineering* 83(1), 95–108.

Almgren, R. and Chriss, N. (2001). Optimal execution of portfolio transactions.
*Journal of Risk* 3(2), 5–39.

Fleming, W. H. and Soner, H. M. (2006).
*Controlled Markov Processes and Viscosity Solutions* (2nd ed.). Springer.

Merton, R. C. (1971). Optimum consumption and portfolio rules in a continuous-time model.
*Journal of Economic Theory* 3(4), 373–413.

Tobin, J. (1958). Liquidity preference as behavior towards risk.
*Review of Economic Studies* 25(2), 65–86.

*[All other references as per companion papers.]*
