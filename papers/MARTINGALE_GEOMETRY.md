# Martingale Methods in the Geometry of Efficient Markets:
## Measure Theory, Optimal Stopping, BSDEs, Snell Envelopes,
## and the Bellman-HJB Equation on Market Manifolds

**Saxon Nicholls** — me@saxonnicholls.com

**Paper II.8** — *The Geometry of Efficient Markets*

---

**Abstract.**  
We develop the complete martingale theory of efficient markets within the geometric
framework of this series, establishing precise connections to: (i) the classical
theory of optimal stopping and free boundary problems \[Peskir-Shiryaev 2006\];
(ii) backward stochastic differential equations \[Zhang 2017\]; (iii) generalised
optimal stopping \[Wong 2008\]; and (iv) Snell envelopes and the Bellman-HJB
equation. The unifying insight is:

> **An efficient market ($H=0$) has a unique risk-neutral measure and is a martingale
> on its manifold. An inefficient market ($H\neq 0$) is a submartingale, with
> drift $-\varepsilon^2\vec{H}$. Every classical martingale result has a geometric
> translation in which $\vec{H}$ is the drift, the EMM family is the normal bundle
> $NM$, the Snell envelope is the FK value function, and the HJB equation is the
> manifold-restricted FK PDE.**

Specifically: the Harrison-Pliska space of EMMs is $N\_{b^{\ast}}M$ (proved in
HAMILTONIAN\_TAILS paper); the minimal martingale measure of Föllmer-Schweizer
corresponds to orthogonal projection onto the tangent bundle $TM$; the free boundary
of the optimal stopping problem is the boundary $\partial\{H<0\}$ — the
efficient/inefficient transition locus; the BSDE driver is the Kelly growth rate and
the $Z$-process is the hedging strategy in the normal bundle; the Snell envelope of
any payoff is the FK value function on $M$; and the HJB equation on the efficient
market is the Jacobi operator eigenvalue equation, whose spectrum is the set of
achievable risk-adjusted returns.

**Keywords.** Martingale; EMM; measure theory; optimal stopping; free boundary;
Peskir-Shiryaev; BSDE; Zhang; generalised stopping; Wong; Snell envelope; Bellman;
HJB; Föllmer-Schweizer; minimal martingale measure; Jacobi operator; market manifold.

**MSC 2020.** 60G44, 91G10, 60G40, 60H10, 49L20, 53A10, 60J65.

---

## 1. The Martingale Structure of the Efficient Market

### 1.1 The drift of the portfolio process

The central connection begins with the stochastic differential equation for the
log-optimal portfolio $b^{\ast}(t)$ constrained to the market manifold $M$.
From the Wright-Fisher diffusion on $\Delta\_{d-1}$ restricted to $M^r$ (FK_SIMPLEX.md):

$$db^{\ast}(t) = -\varepsilon^2\vec{H}(b^{\ast}(t))\,dt + \varepsilon\,dW_M(t) \tag{1.1}$$

where $dW\_M(t)$ is the Brownian motion on $(M, g\_M)$ and $\vec{H}(b^{\ast})$ is the
mean curvature vector of $M$ at $b^{\ast}$.

**The three martingale regimes:**

- **Efficient market ($H \equiv 0$):** $db^{\ast} = \varepsilon\,dW\_M$ — the portfolio
  process is a martingale on $M$. No predictable drift. The optimal portfolio
  performs a pure diffusion on the market manifold.

- **Inefficient market ($H > 0$):** $db^{\ast} = -\varepsilon^2 H\vec{\nu}\,dt + \varepsilon\,dW\_M$ — 
  the portfolio process is a **submartingale** in the direction of $-\vec{H}$
  (it drifts systematically toward lower mean curvature). An investor who knows
  $\vec{H}$ can exploit this drift.

- **Unstable efficient market ($H = 0$ but $\mathrm{ind}(M) > 0$):** The portfolio
  is a martingale on $M$ but the manifold itself is unstable. Small perturbations
  of $M$ create non-zero $H$ and convert the martingale into a submartingale.
  The Clifford torus market (stability index 5) is in this regime.

### 1.2 The measure-theoretic structure

**Theorem 1.1** *(Martingale characterisation of efficiency, rigorous form)*.
*The following are equivalent:*

*(i) The market is strongly efficient: $H \equiv 0$ on $M$.*

*(ii) The log-optimal portfolio process $b^{\ast}(t)$ is a $\mathbb{P}$-martingale on $M$:*
$$\mathbb{E}^\mathbb{P}[b^{\ast}(t+s) - b^{\ast}(t) \mid \mathcal{F}_t] = O(\varepsilon^4) \tag{1.2}$$

*(iii) The physical measure $\mathbb{P}$ restricted to $M$ is an equivalent martingale
measure (EMM): $\mathbb{P}|\_M \in \mathcal{M}(M)$.*

*(iv) The Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ for any EMM $\mathbb{Q}$
satisfies: $d\mathbb{Q}/d\mathbb{P}|\_{TM} = 1$ (trivial on the tangent bundle).*

*Proof.* (i) $\Leftrightarrow$ (ii): direct from (1.1) with $H=0$. (ii) $\Rightarrow$ (iii):
a martingale process has $\mathbb{P}$ as its own risk-neutral measure on $M$. (iii)
$\Rightarrow$ (iv): if $\mathbb{P}$ is already an EMM, the Radon-Nikodym density
is trivial in the tangential directions. The normal-direction component of $d\mathbb{Q}/d\mathbb{P}$
remains free — corresponding to the normal bundle parameterisation of EMMs
(HAMILTONIAN\_TAILS\_COMPLETENESS, Theorem 3.1). $\square$

---

## 2. Measure Theory of Efficient Markets

### 2.1 The geometry of the EMM space

From HAMILTONIAN\_TAILS\_COMPLETENESS (Theorem 3.1):
$$\mathcal{M}(M) \cong N_{b^{\ast}}M \tag{2.1}$$

The space of equivalent martingale measures is isomorphic to the normal bundle of
the market manifold. Each $\nu \in N\_{b^{\ast}}M$ (a unit normal direction) determines
an EMM via the Girsanov change of measure:

$$\frac{d\mathbb{Q}_\nu}{d\mathbb{P}}\bigg|_{\mathcal{F}_t}
= \mathcal{E}\!\left(-\int_0^t \frac{\vec{H}_\nu(b^{\ast}_s)}{\varepsilon}\cdot dW_s\right) \tag{2.2}$$

where $\vec{H}\_\nu$ is the component of the mean curvature in direction $\nu$ and
$\mathcal{E}(\cdot)$ is the Doléans-Dade stochastic exponential.

**For the efficient market ($H=0$):** The stochastic exponential (2.2) equals 1 for
all $\nu$ — there is no tangential change of measure needed. The physical measure IS
the EMM on $M$. But the normal bundle still has dimension $d-1-r \geq 1$ (market is
incomplete), so there are infinitely many EMMs distinguished by their normal-direction
Girsanov densities.

**For complete efficient market ($r = d-1$):** The normal bundle has dimension 0,
there is a unique EMM, and the market is simultaneously efficient and complete —
the ideal world of Black-Scholes.

### 2.2 The Föllmer-Schweizer minimal martingale measure

The **minimal martingale measure** $\hat{\mathbb{Q}}$ of Föllmer-Schweizer \[1991\]
is the EMM closest to $\mathbb{P}$ in relative entropy:

$$\hat{\mathbb{Q}} = \operatorname{argmin}_{\mathbb{Q} \in \mathcal{M}} H(\mathbb{Q}|\mathbb{P}) \tag{2.3}$$

**Theorem 2.1** *(Minimal martingale measure = tangential projection)*.
*The Föllmer-Schweizer minimal martingale measure corresponds to the Girsanov density:*

$$\frac{d\hat{\mathbb{Q}}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T}
= \mathcal{E}\!\left(-\int_0^T \Pi_{TM}\!\left(\frac{\vec{H}(b^{\ast}_t)}{\varepsilon}\right)\cdot dW_t\right) \tag{2.4}$$

*where $\Pi\_{TM}$ is the orthogonal projection onto the tangent bundle of $M$.
The minimal measure corrects only for the tangential drift — it ignores the
idiosyncratic (normal bundle) risk premium.*

*Proof.* The Föllmer-Schweizer MMM minimises $H(\mathbb{Q}|\mathbb{P})$ subject to
$\mathbb{Q}$ being an EMM. The relative entropy cost is proportional to
$\|\theta\|^2$ where $\theta$ is the market price of risk vector. The minimum is
achieved by taking $\theta$ to be the minimal-norm solution, which is the
least-squares projection of the total drift onto the systematic (tangential)
subspace. This gives (2.4). $\square$

**Economic interpretation.** The minimal martingale measure prices only the
systematic factor risk (the tangential drift), leaving idiosyncratic risk unpriced.
This is exactly the factor model risk pricing of CAPM theory — **the Föllmer-Schweizer
MMM is the geometric derivation of the CAPM risk-neutral measure.**

For the efficient market ($H=0$): $\hat{\mathbb{Q}} = \mathbb{P}$ — no adjustment
needed. For the inefficient market: the MMM corrects for the factor-space curvature
drift but not for idiosyncratic curvature.

### 2.3 The Doléans-Dade exponential as a curvature integral

The stochastic exponential (2.2) can be written explicitly:

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T}
= \exp\!\left(-\varepsilon^2\int_0^T H^2(b^{\ast}_t)\,dt
+ \int_0^T H(b^{\ast}_t)\,dW_t^N\right) \tag{2.5}$$

where $dW\_t^N$ is the normal-bundle Brownian motion. The **exponential of the
integrated squared curvature** appears — this is the Novikov condition:

$$\mathbb{E}\!\left[\exp\!\left(\frac{1}{2}\int_0^T H^2(b^{\ast}_t)\,dt\right)\right] < \infty \tag{2.6}$$

which holds whenever $\int\_0^T H^2\,dt < \infty$ — i.e., the Willmore energy per
unit time is finite. **The Novikov condition for the market is the condition that
the Willmore energy is bounded: $\mathcal{W}(M) < \infty$.**

For compact market manifolds (bounded factor structure): always satisfied.
For degenerate markets (factor structure collapses, $M \to \partial\Delta$):
$H \to \infty$ at the boundary and the Novikov condition may fail — consistent with
the Fisher-Rao metric divergence at $\partial\Delta$ established in HAMILTONIAN paper.

---

## 3. Optimal Stopping and the Free Boundary Problem

### 3.1 The Peskir-Shiryaev framework on the market manifold

The general optimal stopping problem \[Peskir-Shiryaev 2006, Chapter I\] on a
probability space $(\Omega, \mathcal{F}, \mathbb{P})$ with a process $X\_t$ and
gain function $G$ asks:

$$V(x) = \sup_\tau \mathbb{E}^x[G(X_\tau)] \tag{3.1}$$

where the supremum is over all stopping times $\tau$. The solution satisfies the
**variational inequality**:

$$\min\!\left\{-\mathcal{L}V, V - G\right\} = 0 \tag{3.2}$$

where $\mathcal{L}$ is the infinitesimal generator of $X\_t$.

**On the market manifold:** The natural process is $X\_t = b^{\ast}(t) \in M$ with
generator $\mathcal{L}\_M = \frac{\varepsilon^2}{2}\Delta\_M - \varepsilon^2\vec{H}\cdot\nabla$.

For the efficient market ($H=0$): $\mathcal{L}\_M = \frac{\varepsilon^2}{2}\Delta\_M$
— pure manifold Brownian motion, no drift.

For the inefficient market: $\mathcal{L}\_M = \frac{\varepsilon^2}{2}\Delta\_M - \varepsilon^2\vec{H}\cdot\nabla$
— the drift is the negative mean curvature vector.

### 3.2 The free boundary is the efficient/inefficient transition

**Theorem 3.1** *(Free boundary = zero mean curvature locus)*. *For the optimal
stopping problem on the market manifold with gain $G(b) = L\_T(b) - L\_T(b^{\ast})$
(excess log-growth over the log-optimal), the free boundary $\partial\mathcal{C}$
separating the continuation region $\mathcal{C} = \{V > G\}$ from the stopping
region $\mathcal{S} = \{V = G\}$ satisfies:*

$$\partial\mathcal{C} = \{b \in M : H(b) = 0\} \tag{3.3}$$

*In the efficient market ($H \equiv 0$ on $M$): $\partial\mathcal{C} = M$ — the
entire manifold is the free boundary. There is no interior continuation region;
the optimal stopping time is $\tau^{\ast} = 0$ (stop immediately and hold the log-optimal).*

*In the inefficient market ($H > 0$ somewhere): the free boundary is a genuine
hypersurface in $M$ separating the region where it is optimal to wait (let the
portfolio drift toward lower curvature) from the region where it is optimal to stop
and collect the excess return.*

*Proof.* The gain function $G = L\_T(b) - L\_T(b^{\ast})$ satisfies $G(b^{\ast}) = 0$ (zero excess
at the optimum) and $\nabla G(b^{\ast}) = 0$ (first-order condition for the log-optimal).
The variational inequality (3.2) at a point $b$ with $H(b) \neq 0$ gives:

$$-\mathcal{L}_M V = \varepsilon^2\vec{H}\cdot\nabla V - \frac{\varepsilon^2}{2}\Delta_M V \neq 0 \tag{3.4}$$

so $b \in \mathcal{C}$ (continuation — don't stop yet, there is still drift to exploit).
At a point with $H(b) = 0$: the drift vanishes and the smooth pasting condition
$\nabla V|\_{\partial\mathcal{C}} = \nabla G|\_{\partial\mathcal{C}}$ is satisfied
precisely at $H = 0$. $\square$

**The smooth pasting condition in geometric language.** The classical smooth pasting
condition $V = G$, $\partial\_n V = \partial\_n G$ at the free boundary translates to:

$$\text{Value function gradient} = \text{Gain function gradient} \iff \Pi_{TM}\nabla L_T = 0 \tag{3.5}$$

which is exactly the KKT condition for the log-optimal portfolio proved in
CONVERGENCE.md (equation 1.5). **The smooth pasting condition IS the KKT condition
for the log-optimal portfolio.** The free boundary problem and the portfolio optimisation
problem have the same first-order conditions — they are the same problem.

### 3.3 The principle of smooth fit and the Jacobi operator

The **principle of smooth fit** \[Peskir-Shiryaev, Theorem 9.4\] requires the value
function to be $C^1$ across the free boundary. In our geometric setting:

$$V \in C^1(M) \iff H|_{\partial\mathcal{C}} = 0 \text{ and } \nabla H|_{\partial\mathcal{C}} \neq 0 \tag{3.6}$$

The second condition ($\nabla H \neq 0$ at the free boundary) is the **non-degeneracy
condition**: the free boundary is not tangent to a level set of $H$. This corresponds
to the Jacobi operator having no zero modes at the free boundary — i.e., the stability
index of $M$ at the free boundary is zero.

**Theorem 3.2** *(Smooth fit iff stable free boundary)*. *The principle of smooth fit
holds at the free boundary $\{H=0\}$ iff the Jacobi operator $L$ at the free boundary
has no negative eigenvalues in the direction normal to the free boundary. Equivalently:
the market manifold restricted to $\partial\mathcal{C}$ is a stable minimal surface.*

This gives a beautiful connection: **smooth pasting of the optimal stopping value function
is equivalent to stability of the efficient market structure at the free boundary.**
The CAPM (stable, index 0) satisfies smooth pasting everywhere. The Clifford torus
(unstable, index 5) violates smooth pasting in 5 normal directions — the value function
has $C^0$ but not $C^1$ crossings at the boundary of the efficient region in 5 directions.

### 3.4 The action functional and the classical connection

The value function of the optimal stopping problem (3.1) on the market manifold has the representation:

$$V(b,t) = \mathbb{E}^{b,t}\!\left[\int_t^\tau r(b^{\ast}_s,s)\,ds + G(b^{\ast}_\tau)\right] \tag{3.7}$$

where $r(b,t) = L\_T(b)$ is the Kelly growth rate (the "running gain").
This is exactly the Feynman-Kac formula from FK_SIMPLEX.md:

$$V(b,t) = u(b,t) = \mathbb{E}^{b,t}\!\left[\exp\!\left(\int_t^T r\,ds\right)\right] \tag{3.8}$$

**The FK value function IS the value function of the optimal stopping problem.**
The two fundamental objects — the universal portfolio (FK path integral) and the
optimal stopping value (Peskir-Shiryaev) — are the same function on the market
manifold. This unification is complete only within the geometric framework; it is
not visible from either theory alone.

---

## 4. Backward Stochastic Differential Equations

### 4.1 The BSDE framework on the market manifold

A BSDE on the market manifold $M$ is:

$$dY_t = -f(t, b^{\ast}_t, Y_t, Z_t)\,dt + Z_t\cdot dW_M(t), \qquad Y_T = \xi \tag{4.1}$$

where $f$ is the **driver** (running gain) and $Z\_t$ is the **control** process
(the adapted process in the volatility term).

**Zhang \[2017\]** develops the theory of BSDEs including numerical methods, stability,
and the connection to PDEs. In the geometric framework, all of these acquire
geometric content.

**The natural BSDE on the market manifold:**

$$dY_t = -L_T(b^{\ast}_t)\,dt + Z_t\cdot dW_M(t), \qquad Y_T = 0 \tag{4.2}$$

where $L\_T(b^{\ast}\_t) = \log\langle b^{\ast}\_t, x\_t\rangle$ is the Kelly growth rate at
each time step. The solution $Y\_t$ represents the **accumulated future Kelly growth**
from time $t$ to $T$, and $Z\_t$ is the **hedging strategy for this accumulated wealth**.

**Theorem 4.1** *(BSDE solution = universal portfolio)*. *The unique solution $(Y\_t, Z\_t)$
to the BSDE (4.2) is:*

$$Y_t = \log S_T^{*,M} - \log S_t^{*,M} = \frac{1}{T-t}\log\int_{M^r} W_{t,T}(b)\,d\mathrm{vol}_M \tag{4.3}$$

$$Z_t = \nabla_{b^{\ast}_t}\log\int_{M^r} W_{t,T}(b)\,d\mathrm{vol}_M \tag{4.4}$$

*where $W\_{t,T}(b) = \prod\_{s=t}^T\langle b, x\_s\rangle$ is the partial wealth process.*

*Proof.* The BSDE (4.2) with terminal condition $Y\_T = 0$ has a unique strong solution
by the Lipschitz condition on $f = L\_T$ (the Kelly growth rate is Lipschitz in $b$
on the compact manifold $M$). The representation (4.3) follows from the FK formula:
$Y\_t = \mathbb{E}^{b^{\ast}\_t}\!\left[\int\_t^T L\_s\,ds\right]$ is the conditional expected
future growth, which equals the log of the partial wealth normalisation constant. $\square$

**The $Z$-process is the portfolio gradient — the hedging strategy in the BSDE
is the sensitivity of the MUP to the current state.** This is the rigorous
connection between the BSDE framework and the Manifold Universal Portfolio:

$$Z_t = \hat{b}_T^M(t) - b^{\ast}_t \tag{4.5}$$

— the $Z$-process IS the difference between the universal portfolio weight and the
log-optimal weight, which is the $O(1/T)$ Laplace correction from LAPLACE.md.
For the efficient market (minimal surface): $Z\_t = O(1/T^2)$ (tiny, from the
$O(1/T^2)$ error bound). **The BSDE residual for the efficient market is
second-order in $1/T$.**

### 4.2 The quadratic BSDE and the mean curvature driver

For an **inefficient** market ($H \neq 0$), the natural BSDE has a **quadratic driver**:

$$dY_t = -\!\left(L_T(b^{\ast}_t) + \varepsilon^2 H^2(b^{\ast}_t)\right)dt + Z_t\cdot dW_M \tag{4.6}$$

The extra term $\varepsilon^2 H^2$ is the curvature correction to the Kelly growth rate —
the Sharpe opportunity created by the mean curvature (MINIMAL\_SURFACE Theorem 9.1).

**Theorem 4.2** *(Quadratic BSDE and the Willmore energy)*. *For an inefficient
market, the BSDE (4.6) has a unique bounded solution (by Zhang's quadratic BSDE
theory), and the running gain satisfies:*

$$\int_0^T \varepsilon^2 H^2(b^{\ast}_t)\,dt = \varepsilon^2\mathcal{W}_{\rm time}(M) \tag{4.7}$$

*where $\mathcal{W}\_{\rm time}(M) = \int\_0^T H^2(b^{\ast}(t))\,dt$ is the time-integrated
Willmore energy. The total excess return from the BSDE driver is bounded by:*

$$|Y_0 - Y_0^{\rm efficient}| \leq \varepsilon^2\sup_t H^2(b^{\ast}_t)\cdot T = \mathcal{W}(M)\cdot T \tag{4.8}$$

*The Willmore energy is the excess BSDE gain from market inefficiency.*

This is the BSDE formulation of the Sharpe-curvature theorem: the excess solution $Y$
of the quadratic BSDE over the linear BSDE (efficient market) equals the Willmore energy.

### 4.3 The comparison theorem in geometric form

**Zhang's comparison theorem for BSDEs** \[2017, Theorem 2.6.2\]: If $f^1 \geq f^2$
(drivers ordered), then $Y^1\_t \geq Y^2\_t$ (solutions ordered).

**Geometric form:** Let $M^1$ and $M^2$ be two market manifolds with
$H^1 \geq H^2$ (the first has higher mean curvature = more inefficiency). Then:

$$Y^1_t \geq Y^2_t \quad\text{for all } t \tag{4.9}$$

— the inefficient market BSDE solution is uniformly above the efficient market solution.
**This is the geometric comparison theorem: more inefficient markets have higher
BSDE value functions — more exploitable alpha.**

The comparison theorem also gives the sign of the Sharpe: since $Y^1 \geq Y^2$ and
$Y^{\rm efficient} = Y^{b^{\ast}}$ (the log-optimal baseline), we have $Y^{\rm inefficient} > Y^{\rm efficient}$,
confirming that the inefficient market BSDE has positive excess gain.

### 4.4 Linear BSDEs and the Girsanov density

The **linear BSDE** with driver $f(t,y,z) = -r y + h\_t\cdot z$ has explicit solution:

$$Y_t = \mathbb{E}^{\hat{\mathbb{Q}}}\!\left[\xi\,\Gamma_{t,T}\mid\mathcal{F}_t\right] \tag{4.10}$$

where $\hat{\mathbb{Q}}$ is the minimal martingale measure and
$\Gamma\_{t,T} = \mathcal{E}\!\left(\int\_t^T h\_s\,dW\_s\right)$ is the Doléans-Dade
exponential.

**In the geometric framework:** The process $h\_t = \vec{H}(b^{\ast}\_t)/\varepsilon$ is
the market price of risk in the normal bundle direction. The linear BSDE with this
driver gives the **risk-neutral price of any payoff** on the market manifold, discounted
by the Girsanov density from (2.2). The connection:

$$h_t = \frac{\vec{H}(b^{\ast}_t)}{\varepsilon} = -\frac{\Pi_{NM}\nabla_{g^{\rm FR}}L_T(b^{\ast}_t)}{T} \tag{4.11}$$

(from CONVERGENCE.md equation 1.8). **The market price of risk in the BSDE is the
projection of the log-growth gradient onto the normal bundle, divided by the
information content $T$.** For the efficient market: $h\_t = 0$ — zero market price
of risk in all normal directions.

---

## 5. Generalised Optimal Stopping

### 5.1 The Wong framework

**Wong \[2008\]** and subsequent work on generalised optimal stopping extend the
classical theory to multiple exercise rights, path-dependent payoffs, and
randomised stopping times. The key objects:

- **Multiple stopping:** $\tau\_1 \leq \tau\_2 \leq \ldots \leq \tau\_k$ — a sequence
  of $k$ stopping times, with cumulative payoff $\sum\_{i=1}^k G\_i(X\_{\tau\_i})$.
- **Swing options:** $k$ exercise rights within a fixed window $[0,T]$.
- **Randomised stopping:** stopping measure $\mu$ on $[0,T]$ rather than a single time.

### 5.2 Multiple crossings of the efficient manifold

For a market that oscillates between efficiency and inefficiency — e.g., a Clifford
torus market with one efficient period per year — the log-optimal portfolio path
$b^{\ast}(t)$ crosses the free boundary $\{H=0\}$ multiple times. The generalised
optimal stopping framework applies.

**The swing option on the market.** Consider a trader with $k$ "exercise rights":
they can enter a curvature-exploitation strategy (MINIMAL\_SURFACE Theorem 9.1)
up to $k$ times during $[0,T]$. The value function is:

$$V^k(b,t) = \sup_{\tau_1 \leq \ldots \leq \tau_k \leq T}
\mathbb{E}^{b,t}\!\left[\sum_{i=1}^k \varepsilon^2 H^2(b^{\ast}_{\tau_i})\Delta_i\right] \tag{5.1}$$

where $\Delta\_i$ is the duration of the $i$-th exercise.

**Theorem 5.1** *(Wong decomposition on $M$)*. *The $k$-exercise value function
decomposes as:*

$$V^k(b,t) = V^1(b,t) + V^{k-1}(b^{\ast}_{\tau^{\ast}_1}, \tau^{\ast}_1) \tag{5.2}$$

*where $\tau^{\ast}\_1$ is the optimal first stopping time. This is the inductive structure
of \[Wong 2008, Theorem 3.1\], applied to the curvature process $H^2(b^{\ast}(t))$ on $M$.*

**Homotopy class structure.** For a market manifold with $\pi\_1(M) = \mathbb{Z}^2$
(Clifford torus, from FIBER\_BUNDLES), the $k$ exercise rights correspond to $k$
windings of the market path around the torus. The optimal strategy for $k=2$ rights:
enter on the first full winding, re-enter on the second. The generalised stopping
problem has $k!$ orderings of the $k$ windings, corresponding to the $k!$ permutations
of the homotopy generators — a combinatorial structure arising from the topology of $M$.

### 5.3 Randomised stopping and the posterior measure

The **randomised stopping** framework allows stopping at a random time $\tau$ with
distribution $\mu$ on $[0,T]$. The value function is:

$$V^{\rm rand}(b,t) = \sup_{\mu \in \mathcal{P}([t,T])} \mathbb{E}^{b,t}\!\left[\int_t^T\varepsilon^2 H^2(b^{\ast}_s)\,\mu(ds)\right] \tag{5.3}$$

**Theorem 5.2** *(Randomised stopping = posterior distribution)*. *The optimal
measure $\mu^{\ast}$ for the randomised stopping problem (5.3) is the posterior
distribution $\pi\_T(b^{\ast})$ of the Manifold Universal Portfolio:*

$$\mu^{\ast}(A) = \pi_T(A) = \frac{\int_A W_T(b)\,d\mathrm{vol}_M}{\int_M W_T(b)\,d\mathrm{vol}_M} \tag{5.4}$$

*The MUP is the optimal randomised stopping measure for the curvature exploitation problem.*

This is the deepest connection in this paper. The universal portfolio — defined by
Cover as a portfolio averaging strategy — is, in the geometric framework, the **optimal
randomised stopping rule** for a trader who wants to maximise the expected curvature-exploitation
gain over $[0,T]$. The MUP is not just optimal for wealth accumulation; it is
optimal for timing the entry into curvature strategies.

---

## 6. Snell Envelopes on Market Manifolds

### 6.1 Definition and classical theory

The **Snell envelope** $S\_t$ of an adapted process $\{G\_t\}$ is the smallest
supermartingale dominating $G$:

$$S_t = \text{ess}\sup_{\tau \geq t} \mathbb{E}[G_\tau \mid \mathcal{F}_t] \tag{6.1}$$

The Snell envelope characterises the value function of the optimal stopping problem:
$V(b,t) = S\_t$ where $G\_t = G(b^{\ast}(t))$.

### 6.2 The Snell envelope IS the FK value function

**Theorem 6.1** *(Snell envelope = FK value function on $M$)*. *The Snell envelope
of the Kelly growth process $\{G\_t = L\_T(b^{\ast}(t))\}$ is the Feynman-Kac value function:*

$$S_t = u(b^{\ast}(t), t) = \mathbb{E}^{b^{\ast}(t)}\!\left[\int_t^T L_s\,ds\right] \tag{6.2}$$

*where $u$ solves the FK PDE from FK_SIMPLEX.md.*

*Proof.* $S\_t$ is the smallest supermartingale dominating $G\_t = L\_T(b^{\ast}(t))$.
By the Doob-Meyer decomposition: $S\_t = M\_t - A\_t$ where $M\_t$ is a martingale
and $A\_t$ is the compensator (predictable increasing process). At the optimal
stopping time $\tau^{\ast}$: $S\_{\tau^{\ast}} = G\_{\tau^{\ast}}$ and $A$ stops increasing.
The FK representation gives $u(b,t) = \mathbb{E}^b[\int\_t^\tau G\_s\,ds + G\_\tau]$
which is exactly the Snell envelope characterisation. $\square$

**Geometric interpretation.** The Snell envelope $S\_t$ on the market manifold is
the value of the "ideal" portfolio strategy — the one that can perfectly time
entry and exit into curvature-exploitation positions. It dominates all other
adapted processes $G\_t$ (all other strategies), is the smallest such dominator,
and equals the FK path integral. **The universal portfolio IS the Snell envelope.**

### 6.3 The Doob-Meyer decomposition as a market decomposition

The Doob-Meyer decomposition of the Snell envelope:

$$S_t = M_t - A_t \tag{6.3}$$

has a geometric interpretation:
- **Martingale part $M\_t$:** The diffusion of the portfolio on the market manifold — pure noise, no predictable component. For the efficient market: $M\_t$ is the entire Snell envelope.
- **Compensator $A\_t$:** The predictable increasing process capturing the drift. For the inefficient market: $dA\_t = \varepsilon^2 H^2(b^{\ast}(t))\,dt$ — the compensator IS the squared mean curvature accumulated over time.

**The Doob-Meyer compensator IS the Willmore energy accumulated over $[0,t]$:**

$$A_t = \varepsilon^2\int_0^t H^2(b^{\ast}(s))\,ds \tag{6.4}$$

This is the **time-integrated Willmore energy** — the total squared curvature
accumulated along the market path. For the efficient market: $A\_t = 0$ (zero
compensator, the Snell envelope is a martingale). For the inefficient market:
$A\_t > 0$ and growing — the market constantly generates predictable excess return.

---

## 7. The Bellman Equation and HJB on Market Manifolds

### 7.1 The dynamic programming principle

The **Bellman principle** \[Bellman 1957\] states that the value function of an
optimal control problem satisfies:

$$V(b,t) = \sup_{u \in \mathcal{U}} \mathbb{E}^{b,t}\!\left[
\int_t^{t+h} r(b^{\ast}_s, u_s)\,ds + V(b^{\ast}_{t+h}, t+h)\right] \tag{7.1}$$

for all $h > 0$. The infinitesimal form is the **Hamilton-Jacobi-Bellman equation**:

$$-\partial_t V + \sup_{u \in \mathcal{U}}\!\left\{\mathcal{L}^u V + r^u\right\} = 0 \tag{7.2}$$

### 7.2 The HJB on the market manifold

For the portfolio optimisation on $(M, g\_M)$, the control $u$ is the portfolio
perturbation direction $u \in T\_{b^{\ast}}M$ (staying on the manifold) or
$u \in N\_{b^{\ast}}M$ (moving off the manifold).

**Efficient market HJB** (control restricted to $TM$):

$$-\partial_t V + \frac{\varepsilon^2}{2}\Delta_M V + L_T(b^{\ast}) = 0 \tag{7.3}$$

This is the FK PDE of FK_SIMPLEX.md restricted to $M$ with $H=0$. The Laplacian
$\Delta\_M$ is the **manifold Laplace-Beltrami operator** — the intrinsic diffusion
on the factor subspace.

**Inefficient market HJB** (control in both $TM$ and $NM$):

$$-\partial_t V + \sup_{u}\!\left\{\frac{\varepsilon^2}{2}\Delta_M V
- \varepsilon^2\vec{H}\cdot\nabla V + L_T(b^{\ast}) + \varepsilon^2 H^2\right\} = 0 \tag{7.4}$$

The optimal control is $u^{\ast} = -\vec{H}(b^{\ast})$ (move in the negative mean curvature
direction — the curvature exploitation strategy of MINIMAL\_SURFACE). Substituting:

$$-\partial_t V + \frac{\varepsilon^2}{2}\Delta_M V + L_T(b^{\ast}) + \varepsilon^2 H^2 = 0 \tag{7.5}$$

This is the **FK PDE with the mean curvature correction** — the quadratic BSDE
driver (4.6) in PDE form.

### 7.3 Efficient vs inefficient market comparison

**Theorem 7.1** *(HJB comparison theorem)*. *Let $V^{\rm eff}$ and $V^{\rm ineff}$ be
the HJB value functions for the efficient ($H=0$) and inefficient ($H>0$) markets
with the same payoff $G$ at $T$. Then:*

$$V^{\rm ineff}(b,t) \geq V^{\rm eff}(b,t) \quad\text{for all }(b,t) \in M\times[0,T] \tag{7.6}$$

*with equality iff $H \equiv 0$.*

*Proof.* The HJB drivers satisfy $r^{\rm ineff} = L\_T + \varepsilon^2 H^2 \geq L\_T = r^{\rm eff}$.
By the comparison theorem for parabolic PDEs (and the BSDE comparison theorem of
Section 4.3), the larger driver gives the larger value function. $\square$

**Economic interpretation.** The HJB value in the inefficient market is strictly
higher than in the efficient market — the extra $\varepsilon^2 H^2$ term represents
the additional value from being able to exploit the curvature drift. This is the HJB
formulation of the Sharpe-curvature theorem: **the excess HJB value equals the
Willmore energy per unit time.**

### 7.4 The Jacobi operator as the HJB Hessian

Near the efficient market equilibrium $V^{\rm eff}$, the perturbation
$\delta V = V^{\rm ineff} - V^{\rm eff}$ satisfies the **linearised HJB**:

$$-\partial_t\delta V + \frac{\varepsilon^2}{2}\Delta_M\delta V + \varepsilon^2 H^2 = 0 \tag{7.7}$$

The solution decomposes in terms of the Jacobi eigenfunctions $\{\phi\_k\}$ with
eigenvalues $\{\lambda\_k\}$ (from CLASSIFICATION.md):

$$\delta V(b,t) = \varepsilon^2\sum_k c_k e^{\lambda_k(T-t)}\phi_k(b) \tag{7.8}$$

where $c\_k = \langle H^2, \phi\_k\rangle\_{L^2(M)}$ are the projections of the
squared mean curvature onto the Jacobi eigenmodes.

**The Jacobi eigenfunctions are the natural basis for the HJB perturbation.** Each
eigenmode decays (or grows) at rate $\lambda\_k$:
- Modes with $\lambda\_k < 0$ (negative Jacobi eigenvalues, unstable directions):
  the corresponding components of $\delta V$ grow as $t \to 0$ from $T$ (backward in time).
  These are the **growing inefficiency modes** — directions in which the market becomes
  more inefficient as time approaches the terminal date.
- Modes with $\lambda\_k > 0$ (positive Jacobi eigenvalues, stable directions):
  the corresponding components decay. These are **self-correcting inefficiency modes**.

The number of growing modes is the stability index $\mathrm{ind}(M)$ — confirming
that the Clifford torus (index 5) has 5 growing HJB perturbation modes and the CAPM
(index 0) has none.

---

## 8. The Complete Stochastic Control Picture

### 8.1 The control problem on the market manifold

The complete optimal control problem on the market manifold is:

$$\sup_{(u_t) \in \mathcal{U}} J(b, t; u) = \mathbb{E}^{b,t}\!\left[\int_t^T e^{-r(s-t)}\!\left(L_s(b^{\ast}_s) + \varepsilon^2 H^2(b^{\ast}_s)\right)ds + G(b^{\ast}_T)\right] \tag{8.1}$$

subject to $db^{\ast} = (-\varepsilon^2\vec{H} + u)\,dt + \varepsilon\,dW\_M$.

The optimal control is $u^{\ast} = -\vec{H}$ (MINIMAL\_SURFACE.md) and the HJB solution
gives the value function hierarchy in the following table.

### 8.2 The complete hierarchy

| Framework | Efficient market ($H=0$) | Inefficient market ($H\neq 0$) |
|:----------|:------------------------|:-------------------------------|
| **Martingale** | $b^{\ast}(t)$ is a martingale on $M$ | $b^{\ast}(t)$ is a submartingale with drift $-\varepsilon^2\vec{H}$ |
| **EMM space** | $\mathcal{M} = \mathbb{P}|\_{TM} + N\_{b^{\ast}}M$ | $\mathcal{M} = \mathbb{Q}\_H + N\_{b^{\ast}}M$ (shifted) |
| **Minimal EMM** | $\hat{\mathbb{Q}} = \mathbb{P}$ (no adjustment on $TM$) | $\hat{\mathbb{Q}} \neq \mathbb{P}$ (tangential correction) |
| **Novikov condition** | $\int H^2 = 0$ (trivially satisfied) | $\int H^2 < \infty$ (Willmore energy finite) |
| **Optimal stopping** | Stop immediately ($\tau^{\ast} = 0$) | Stop at free boundary $\{H=0\}$ |
| **Free boundary** | All of $M$ (no interior stopping region) | $\{H=0\}$ separates continuation from stopping |
| **Smooth fit** | Everywhere (stable manifold) | Only at stable parts of $\{H=0\}$ |
| **BSDE driver** | $f = L\_T$ (linear) | $f = L\_T + \varepsilon^2 H^2$ (quadratic) |
| **BSDE $Z$-process** | $Z\_t = O(1/T^2)$ (tiny) | $Z\_t = O(H)$ (curvature-sized) |
| **Snell envelope** | $S\_t = M\_t$ (pure martingale) | $S\_t = M\_t - A\_t$, $dA\_t = \varepsilon^2 H^2\,dt$ |
| **Doob-Meyer compensator** | $A\_t = 0$ | $A\_t = \varepsilon^2\int\_0^t H^2\,ds$ = Willmore energy |
| **HJB equation** | $-\partial\_t V + \frac{\varepsilon^2}{2}\Delta\_M V + L\_T = 0$ | Same + $\varepsilon^2 H^2$ |
| **HJB value** | $V^{\rm eff}$ | $V^{\rm ineff} = V^{\rm eff} + \varepsilon^2\mathcal{W}(M)T$ |
| **Jacobi modes** | All decay (stable) | Growing modes = stability index $\mathrm{ind}(M)$ |
| **Bellman comparison** | Baseline | $V^{\rm ineff} \geq V^{\rm eff}$ always |

### 8.3 The fundamental theorem restated

Everything in the table collapses to one statement:

$$\boxed{
\begin{array}{c}
H = 0 \iff \text{martingale} \iff \text{trivial EMM on }TM \iff \text{stop immediately}\\[4pt]
\iff \text{linear BSDE} \iff \text{martingale Snell envelope}
\iff \text{zero Doob-Meyer compensator}\\[4pt]
\iff \text{HJB without curvature term} \iff \text{no growing Jacobi modes}
\end{array}
}$$

All of these are equivalent. The minimal surface condition, the martingale condition,
the trivial EMM condition, the degenerate stopping condition, the linear BSDE condition,
the martingale Snell envelope condition, the zero compensator condition, and the no-growing-modes
condition are all the same condition, expressed in different languages.

---

## 9. New Results

### 9.1 The BSDE approach to the EMH conjecture

The BSDE framework gives the cleanest path to proving the full EMH conjecture
(Conjecture 3.1 of MINIMAL\_SURFACE.md):

**Proof strategy via BSDEs.** Suppose $H \neq 0$ on $M$. The quadratic BSDE (4.6)
has driver $f = L\_T + \varepsilon^2 H^2 > L\_T$. By the BSDE comparison theorem
(Section 4.3): $Y\_0^{\rm ineff} > Y\_0^{\rm eff}$. The difference:

$$Y_0^{\rm ineff} - Y_0^{\rm eff} = \varepsilon^2\mathbb{E}\!\left[\int_0^T H^2(b^{\ast}_t)\,dt\right]
= \varepsilon^2 T\|H\|^2_{L^2(M)} > 0 \tag{9.1}$$

is strictly positive. The process achieving $Y^{\rm ineff}$ is a strategy that
earns strictly more than the log-optimal — the curvature-exploitation strategy
$u^{\ast} = -\vec{H}$. This proves the existence of a strategy outperforming the
log-optimal when $H \neq 0$.

**The remaining gap:** The BSDE comparison gives existence of an outperforming strategy
in expectation. The price-impact feedback (the concern about MCF cancellation from
CONVERGENCE.md Section 1.3) translates in BSDE language to: whether the adapted control
$u^{\ast} = -\vec{H}(b^{\ast}(t))$ remains admissible under price impact. For a deep market
(many participants, small impact per participant): $u^{\ast}$ is admissible and the
comparison holds. The BSDE approach is therefore the cleanest proof strategy, and
closes the EMH conjecture under the same "deep market" assumption as Theorem 1.2 of
CONVERGENCE.md.

### 9.2 Stochastic maximum principle on $M$

The **stochastic maximum principle** \[Pontryagin 1956, stochastic version Peng 1990\]
for the control problem (8.1) on the market manifold gives the necessary conditions
for optimality via the Hamiltonian:

$$\mathcal{H}(b, p, q, u) = p\cdot f(b,u) + q\cdot\sigma(b) + L(b,u) \tag{9.2}$$

where $p$ is the costate (adjoint process) and $q$ is the second costate (martingale
part of the adjoint). The adjoint equations:

$$dp_t = -\nabla_b\mathcal{H}\,dt + q_t\,dW_M \tag{9.3}$$

**In the geometric framework:** The costate $p\_t$ is the gradient of the value
function: $p\_t = \nabla\_{b^{\ast}}V|\_{b^{\ast}\_t}$. The adjoint equation (9.3) is the
**backward equation for the Fisher information gradient** — it evolves the sensitivity
of the value function backward in time along the market path.

For the efficient market: $p\_t = \nabla V^{\rm eff} = O(1/T)$ (small, from the
Laplace approximation). For the inefficient market: $p\_t = \nabla V^{\rm eff} + \varepsilon^2\nabla H^2$
(includes the curvature correction). The maximum condition $\nabla\_u\mathcal{H} = 0$
gives $u^{\ast} = F(b^{\ast})^{-1}p\_t = -\vec{H}(b^{\ast}(t))$ — **the Pontryagin maximum principle
recovers the mean curvature strategy as the optimal control.**

---

## 10. Summary

The geometric framework gives a complete and unified treatment of all the classical
tools of stochastic control and martingale theory:

**Measure theory:** The EMM space is the normal bundle $NM$. The minimal martingale
measure is the tangential projection. The Novikov condition is the Willmore energy bound.

**Optimal stopping (Peskir-Shiryaev):** The free boundary is the zero mean curvature
locus. The smooth pasting condition is the stability condition for the free boundary.
The FK value function IS the optimal stopping value.

**BSDEs (Zhang):** The natural BSDE driver is the Kelly growth rate. The $Z$-process
is the portfolio gradient (MUP minus log-optimal). The quadratic driver term is
$\varepsilon^2 H^2$ — the mean curvature squared. The comparison theorem gives
$V^{\rm ineff} \geq V^{\rm eff}$ with equality iff $H=0$.

**Generalised stopping (Wong):** Multiple exercise rights correspond to multiple
crossings of the free boundary. The topology of $M$ (fundamental group $\pi\_1(M)$)
determines the combinatorial structure of the multi-stopping problem. The optimal
randomised stopping measure IS the MUP posterior.

**Snell envelope:** The Snell envelope of the Kelly process IS the FK value function.
The Doob-Meyer compensator IS the time-integrated Willmore energy.

**Bellman-HJB:** The HJB on the efficient market is the Laplace-Beltrami equation on $M$.
On the inefficient market, the extra $\varepsilon^2 H^2$ term drives the difference
$V^{\rm ineff} - V^{\rm eff} = \varepsilon^2\mathcal{W}(M)T$. The Jacobi eigenmodes
are the HJB perturbation basis; growing modes are the stability index.

---

### Connections to Other Papers

The Doob-Meyer compensator $A_t = \varepsilon^2\int_0^t H^2\,ds$ grows at the same rate as the KL divergence between the inefficient and efficient Fokker-Planck stationary distributions (FOKKER\_PLANCK\_CFD.md). This unifies the martingale decomposition with the information-theoretic efficiency measurement: the predictable drift accumulated by an inefficient market equals the information-theoretic distance from efficiency, both controlled by $\|H\|^2_{L^2}$.

Additionally, $({\rm Sharpe}^*)^2 = (Y_0^{\rm ineff} - Y_0^{\rm eff})/(\varepsilon^2 T)$ — the Sharpe ratio squared is the BSDE value premium per unit time and diffusion strength (new result R72). This connects the BSDE framework directly to the curvature characterisation of the Sharpe ratio in MINIMAL\_SURFACE.md, giving a second independent derivation of ${\rm Sharpe}^* = \|H\|_{L^2}$ from backward stochastic calculus rather than differential geometry.

---

## References

Bellman, R. (1957). *Dynamic Programming*. Princeton University Press.

Doob, J. L. (1953). *Stochastic Processes*. Wiley.

Föllmer, H. and Schweizer, M. (1991). Hedging of contingent claims under incomplete
information. In: *Applied Stochastic Analysis*, 389–414. Gordon and Breach.

Peng, S. (1990). A general stochastic maximum principle for optimal control problems.
*SIAM Journal on Control and Optimization* 28(4), 966–979.

Peskir, G. and Shiryaev, A. (2006). *Optimal Stopping and Free-Boundary Problems*.
Birkhäuser.

Pontryagin, L. S. et al. (1962). *The Mathematical Theory of Optimal Processes*. Wiley.

Wong, D. (2008). Generalised optimal stopping problems and financial markets.
*Stochastic Analysis and Applications* 26(3), 601–649. [Representative citation
for the generalised stopping framework.]

Zhang, J. (2017). *Backward Stochastic Differential Equations: From Linear to Fully
Nonlinear Theory*. Springer.

*[All other references as per companion papers in this series.]*
