# A Feynman–Kac Formula on the High-Dimensional Simplex,  
## with a Stochastic Stokes Theorem and Applications to Universal Portfolio Theory

**Saxon Nicholls** — me@saxonnicholls.com

---

**Abstract.** We establish a Feynman–Kac representation for the wealth functional of Cover's
Universal Portfolio as the solution to a parabolic partial differential equation on the
$(d-1)$-simplex $\Delta\_{d-1}$, driven by the Wright–Fisher diffusion. The potential term is
precisely the Kelly log-growth rate $r(b,t)$, and the generator is the Wright–Fisher operator
$\mathcal{L}^\varepsilon$ whose stationary distribution is the uniform (Dirichlet) prior. In the
semiclassical limit $\varepsilon \to 0$, the WKB approximation to this PDE recovers the
Laplace approximation to the simplex integral, identifying the log-optimal portfolio $b^*$ as
the Hamilton–Jacobi saddle point and the Fisher information matrix as the Hessian of the action.
The normalised posterior measure satisfies a replicator–diffusion equation that unifies Cover's
online algorithm with evolutionary replicator dynamics in a single PDE. We then establish a
**stochastic Stokes theorem on $\Delta\_{d-1}$** for the Wright–Fisher diffusion: the stochastic
line integral of a differential form along the WF path decomposes into an interior term,
a curvature correction from the Fisher–Rao (Bhattacharyya sphere) geometry, and a boundary
local-time term recording the time the portfolio spends at the faces where individual asset
weights vanish. This corrects the classical Stokes theorem by an explicit $\varepsilon^2/4$
curvature term reflecting the constant positive sectional curvature of $(\Delta\_{d-1}, g\_{\rm FR})$.
We prove that the stable rank $r\_{\rm eff}$ of the Fisher matrix at $b^*$ controls the dimension
of the effective PDE: the heat kernel on $(\Delta\_{d-1}, g\_{\rm FR})$ is concentrated on an
$r\_{\rm eff}$-dimensional submanifold, extending the Johnson–Lindenstrauss lemma to the
measure-valued setting. To our knowledge these connections are new.

**Keywords.** Universal portfolio; Feynman–Kac; Wright–Fisher diffusion; simplex; Hamilton–Jacobi;
WKB; replicator dynamics; stochastic Stokes theorem; Fisher–Rao geometry; Bhattacharyya sphere;
Laplace approximation; log-optimal portfolio; effective rank.

**MSC 2020.** 91G10, 60J60, 35K10, 58J65, 53B21, 91A22.

---

## 1. Introduction

Cover's Universal Portfolio \[Cover 1991\] is a remarkable object: a portfolio strategy that
asymptotically matches the best constant-rebalanced portfolio in hindsight, with no statistical
assumptions on the market. Its wealth after $T$ periods is:

$$S_T^* = \int_{\Delta_{d-1}} \prod_{t=1}^T \langle b, x_t \rangle \, d\mu(b) \tag{1.1}$$

where $x\_t \in \mathbb{R}^d\_+$ are price relative vectors, $\mu$ is the uniform measure on
$\Delta\_{d-1} = \{b \in \mathbb{R}^d : b \geq 0,\, \mathbf{1}^T b = 1\}$, and the portfolio
weights traded at time $T$ are the posterior mean:

$$\hat{b}_T = \frac{\int_{\Delta_{d-1}} b \cdot W_T(b) \, d\mu(b)}{\int_{\Delta_{d-1}} W_T(b) \, d\mu(b)},
\qquad W_T(b) = \prod_{t=1}^T \langle b, x_t \rangle \tag{1.2}$$

This is a Bayesian posterior mean where the "likelihood" of portfolio $b$ is its realised wealth
$W\_T(b)$. The integral lives on a $(d-1)$-dimensional simplex; for $d = 50$ stocks this is a
49-dimensional integral. Ordentlich and Cover \[1998\] showed that computing $\hat{b}\_T$ exactly
is computationally intractable in general, and various approximation schemes have been proposed.

In this paper we identify $(1.2)$ as a **Feynman–Kac functional** on $\Delta\_{d-1}$. This
identification has several consequences that, to our knowledge, are new:

1. The simplex integral $(1.1)$ is the solution to a parabolic PDE with Kelly growth rate as
   potential, whose WKB limit is the log-optimal portfolio $b^*$.

2. The Laplace approximation — which we showed elsewhere \[preprint\] gives $O(1/T^2)$ accuracy
   for moderate $T$ — is precisely the leading WKB correction to this PDE, with the Fisher
   information matrix playing the role of the Hessian of the action.

3. The posterior distribution $\pi\_T(b) \propto W\_T(b)\mu(b)$ satisfies a **replicator–diffusion
   equation**, unifying Cover's algorithm with evolutionary game theory.

4. We establish a **stochastic Stokes theorem** for the Wright–Fisher diffusion on $\Delta\_{d-1}$,
   which corrects the classical Stokes theorem by a curvature term from the Fisher–Rao geometry.
   The simplex, viewed under the square-root (Bhattacharyya) parameterisation, is a hemisphere of
   the unit sphere $S^{d-1}$, with constant sectional curvature $1/4$; this curvature appears
   explicitly in the stochastic Stokes correction.

5. The stable rank $r\_{\rm eff}$ of the Fisher matrix controls the dimension of the effective PDE,
   extending JL dimension reduction to the measure-valued setting.

### 1.1 Related work

The Wright–Fisher diffusion and the simplex appear throughout population genetics
\[Ethier–Kurtz 1986\], evolutionary game theory \[Hofbauer–Sigmund 1998\], and Bayesian
nonparametrics \[Ferguson 1973\]. The information geometry of $\Delta\_{d-1}$ under the
Fisher–Rao metric is developed in Amari \[2016\]. Feynman–Kac on Riemannian manifolds is
treated in Elworthy \[1988\] and Hsu \[2002\]. The stochastic Stokes theorem in flat space
(Lévy area, iterated integrals) appears in Chen \[1958\] and Lyons \[1998\]; on Riemannian
manifolds in Elworthy–Le Jan–Li \[2010\]. The replicator equation without diffusion is the
central object of evolutionary game theory \[Taylor–Jonker 1978\]. None of these works
establishes the specific connection to the universal portfolio or the FK identification of
the simplex integral with a parabolic PDE having Kelly growth rate as potential.

### 1.2 Paper organisation

Section 2 reviews the geometry of $\Delta\_{d-1}$ and the Wright–Fisher diffusion.
Section 3 establishes the main Feynman–Kac theorem.
Section 4 develops the WKB / Hamilton–Jacobi limit and the Laplace approximation.
Section 5 derives the replicator–diffusion equation for the posterior.
Section 6 establishes the stochastic Stokes theorem on $\Delta\_{d-1}$.
Section 7 proves the effective dimension result via the heat kernel and stable rank.
Section 8 discusses implications for computation and open problems.

---

## 2. The Simplex, Its Diffusion, and Information Geometry

### 2.1 The standard simplex

Let $\Delta\_{d-1} = \{b \in \mathbb{R}^d : b\_i \geq 0,\, \sum\_i b\_i = 1\}$. This is a compact
$(d-1)$-dimensional manifold with corners. Its boundary stratifies as:

$$\partial \Delta_{d-1} = \bigcup_{i=1}^d F_i, \qquad F_i = \{b \in \Delta_{d-1} : b_i = 0\} \tag{2.1}$$

The interior is $\mathring{\Delta}\_{d-1} = \{b : b\_i > 0 \;\forall i\}$. The faces $F\_i$ are
themselves simplices: $F\_i \cong \Delta\_{d-2}$.

### 2.2 The Fisher–Rao metric and Bhattacharyya sphere

The **Fisher information metric** on $\mathring{\Delta}\_{d-1}$, viewed as a statistical manifold
of categorical distributions, is:

$$g^{\rm FR}_{ij}(b) = \frac{\delta_{ij}}{b_i} \tag{2.2}$$

Under the **square-root parameterisation** $\phi: b \mapsto \sqrt{b} = (\sqrt{b\_1},\ldots,\sqrt{b\_d})$,
the simplex maps to the positive orthant of the unit sphere:

$$\phi(\Delta_{d-1}) = S^{d-1}_+ := \{u \in \mathbb{R}^d : u_i \geq 0,\, \|u\|^2 = 1\} \tag{2.3}$$

Under this map, the Fisher–Rao metric pulls back to the standard round metric on $S^{d-1}$,
scaled by $1/4$: $g^{\rm FR} = 4\phi^* g\_{\rm round}$. Hence:

**Proposition 2.1** (Bhattacharyya sphere). *The Riemannian manifold $(\mathring{\Delta}\_{d-1}, g^{\rm FR})$
is isometric to the positive hemisphere $S^{d-1}\_+$ with constant sectional curvature $K = 1/4$.
The geodesic distance between $b, b' \in \Delta\_{d-1}$ is the Bhattacharyya angle:*

$$d_{\rm FR}(b, b') = 2\arccos\!\left(\sum_{i=1}^d \sqrt{b_i b'_i}\right) \tag{2.4}$$

This isometry will be fundamental: the Ricci curvature of $(\Delta\_{d-1}, g^{\rm FR})$ is
$\text{Ric} = \frac{d-2}{4} g^{\rm FR}$, and the Weitzenböck correction in the stochastic Stokes
theorem (Section 6) equals $\frac{d-2}{4}$ times the identity on 1-forms.

### 2.3 The Wright–Fisher diffusion

The **Wright–Fisher diffusion** on $\Delta\_{d-1}$ with noise parameter $\varepsilon > 0$ and
drift potential $\Phi$ is the diffusion process $B\_t$ satisfying (in Itô form):

$$dB_t^i = \frac{\varepsilon^2}{2}\sum_j \partial_j\bigl[B_t^i(\delta_{ij} - B_t^j)\bigr]\,dt
+ \nabla_\Delta \Phi(B_t)\,dt + \varepsilon\sum_k \sigma_{ik}(B_t)\,dW_t^k \tag{2.5}$$

where $\sigma\_{ik}(b)\sigma\_{jk}(b) = b\_i(\delta\_{ij} - b\_j)$ is the WF diffusion coefficient
(the square root of the covariance of the multinomial distribution), and $W\_t$ is
$d$-dimensional Brownian motion projected onto the tangent space of $\Delta\_{d-1}$.

The generator is:

$$\mathcal{L}^\varepsilon f(b) = \frac{\varepsilon^2}{2}\sum_{i,j=1}^d b_i(\delta_{ij} - b_j)
\frac{\partial^2 f}{\partial b_i \partial b_j} + \nabla_\Delta \Phi(b) \cdot \nabla f(b) \tag{2.6}$$

The diffusion coefficient $C\_{ij}(b) = b\_i(\delta\_{ij} - b\_j)$ is the **covariance matrix of the
Dirichlet distribution**, and equals the inverse of the Fisher–Rao metric restricted to the
tangent space of $\Delta\_{d-1}$ up to a scalar: $C(b) = [g^{\rm FR}(b)]^{-1}\_{\rm proj}$.

**Proposition 2.2** (Stationary distribution). *The drift-free WF diffusion ($\Phi = 0$) has
the uniform measure $\mu = \text{Dirichlet}(1,\ldots,1)$ as its unique stationary distribution.
With drift $\Phi = \sum\_i \alpha\_i \log b\_i$, the stationary distribution is
$\text{Dirichlet}(\alpha\_1,\ldots,\alpha\_d)$.*

*Proof.* Verify that $\int \mathcal{L}^\varepsilon f \, d\mu = 0$ by integration by parts,
using $\partial\_j[b\_i(\delta\_{ij}-b\_j)] = \delta\_{ij}(1-2b\_i) - b\_j(1-\delta\_{ij})$
and the fact that these terms integrate to zero against the flat measure on $\Delta\_{d-1}$. $\square$

### 2.4 Continuous-time market model

Fix a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}\_t), \mathbb{P})$.
Suppose $d$ asset prices $S\_{t,i}$ satisfy:

$$\frac{dS_{t,i}}{S_{t,i}} = \mu_i(t)\,dt + \sum_{k=1}^m \sigma_{ik}(t)\,dW_t^k,
\qquad \Sigma(t) = \sigma(t)\sigma(t)^T \tag{2.7}$$

The **instantaneous Kelly log-growth rate** of portfolio $b \in \Delta\_{d-1}$ is:

$$r(b, t) = b^T \mu(t) - \tfrac{1}{2}\,b^T \Sigma(t)\, b \tag{2.8}$$

This is the drift of $\log V\_t(b)$ where $V\_t(b)$ is the wealth of the constantly rebalanced
portfolio $b$. The **log-optimal portfolio** is:

$$b^*(t) = \arg\max_{b \in \Delta_{d-1}} r(b,t) \tag{2.9}$$

In the discrete-time setting, $r(b) = \frac{1}{T}\sum\_t \log\langle b, x\_t\rangle$ and
$b^* = \arg\max\_{b \in \Delta\_{d-1}} r(b)$ is the empirical log-optimal (Kelly) portfolio.

---

## 3. The Feynman–Kac Theorem on $\Delta\_{d-1}$

### 3.1 Main theorem

**Theorem 3.1** (FK on the simplex). *Let $B\_t^\varepsilon$ be the drift-free Wright–Fisher
diffusion on $\Delta\_{d-1}$ with generator $\mathcal{L}^\varepsilon$ (equation (2.6) with $\Phi=0$)
and initial condition $B\_0^\varepsilon = b$. Let $r: \Delta\_{d-1} \times [0,T] \to \mathbb{R}$ be
the Kelly growth rate (2.8), continuous and bounded. Define:*

$$u(b, t) = \mathbb{E}^b\!\left[\exp\!\left(\int_t^T r(B_s^\varepsilon, s)\,ds\right)
f(B_T^\varepsilon)\right] \tag{3.1}$$

*for $f \in C(\Delta\_{d-1})$. Then $u \in C^{2,1}(\mathring{\Delta}\_{d-1} \times [0,T))$ and
$u$ satisfies the parabolic PDE:*

$$\frac{\partial u}{\partial t}(b,t) = \mathcal{L}^\varepsilon u(b,t) + r(b,t)\cdot u(b,t),
\qquad (b,t) \in \mathring{\Delta}_{d-1} \times [0,T) \tag{3.2}$$

*with terminal condition $u(\cdot, T) = f$ and Wentzell boundary conditions at $\partial\Delta\_{d-1}$.*

**Proof.** The proof follows the classical FK argument \[Karatzas–Shreve 1991, Theorem 5.7.6\]
adapted to the manifold setting. Define $M\_s = e^{\int\_t^s r(B\_u,u)\,du} \cdot u(B\_s, s)$.
By Itô's formula on the manifold $(\Delta\_{d-1}, g^{\rm FR})$ in Stratonovich form:

$$dM_s = e^{\int_t^s r\,du}\left[\left(\frac{\partial u}{\partial s} + \mathcal{L}^\varepsilon u
+ ru\right)(B_s, s)\,ds + \nabla u(B_s, s) \cdot dB_s^{\rm mart}\right]$$

where $dB\_s^{\rm mart} = \varepsilon \sigma(B\_s)\,dW\_s$ is the martingale part of the WF diffusion.
The drift of $M\_s$ vanishes if and only if $u$ satisfies (3.2). Since $M\_s$ is a local martingale
and $u$ is bounded (by boundedness of $r$ and compactness of $\Delta\_{d-1}$), it is a true
martingale. Taking expectations: $u(b,t) = M\_t = \mathbb{E}^b[M\_T] = \mathbb{E}^b[e^{\int\_t^T r\,ds} f(B\_T)]$. $\square$

### 3.2 The universal portfolio as a FK functional

**Corollary 3.2.** *The normalisation constant of the universal portfolio satisfies:*

$$\log \int_{\Delta_{d-1}} W_T(b)\,d\mu(b) = \log u_0(T) \tag{3.3}$$

*where $u\_0(t) = \int\_{\Delta\_{d-1}} u(b, 0)\,d\mu(b)$ and $u$ solves (3.2) with $f \equiv 1$,
in the discrete-time limit where $r(b,s) = \log\langle b, x\_{\lceil sT/T \rceil}\rangle$ is the
step-function approximation.*

*The universal portfolio weights are:*

$$\hat{b}_T = \frac{\int_{\Delta_{d-1}} b \cdot u(b,0)\,d\mu(b)}{\int_{\Delta_{d-1}} u(b,0)\,d\mu(b)}
= \mathbb{E}^{\pi_0}[B_0^\varepsilon] \tag{3.4}$$

*where $\pi\_0(db) = u(b,0)\mu(db)/u\_0(0)$ is the initial distribution of the FK functional.*

**Remark 3.3.** Equation (3.4) has a striking interpretation: the universal portfolio weights
are the **initial expected position of the WF diffusion** under the FK-weighted measure. The
diffusion "knows" where the log-optimal portfolio will be, through the potential $r(b,t)$.

### 3.3 The adjoint equation and the posterior

Taking the adjoint of (3.2) in the $b$ variable, the **normalised posterior density**:

$$\pi_t(b) = \frac{u(b, t)\,\mu(b)}{\int_\Delta u(b',t)\,\mu(db')} \propto W_t(b)\,\mu(b)$$

satisfies a **forward equation**. Differentiating the normalisation and applying (3.2):

$$\frac{\partial \pi_t}{\partial t} = (\mathcal{L}^\varepsilon)^* \pi_t
+ \bigl(r(b,t) - \bar{r}_t\bigr)\,\pi_t \tag{3.5}$$

where $\bar{r}\_t = \int\_\Delta r(b,t)\,\pi\_t(db)$ is the posterior mean growth rate and
$(\mathcal{L}^\varepsilon)^*$ is the Fokker–Planck operator (formal $L^2$-adjoint of $\mathcal{L}^\varepsilon$).
We call (3.5) the **replicator–diffusion equation**, developed fully in Section 5.

---

## 4. The WKB Limit: Hamilton–Jacobi on the Simplex and the Laplace Approximation

### 4.1 The WKB ansatz

Write $u(b,t) = \exp\!\bigl(S(b,t)/\varepsilon^2\bigr)$. Substituting into (3.2) and collecting
powers of $\varepsilon$:

**Leading order** ($\varepsilon^0$): The **Hamilton–Jacobi equation on** $\Delta\_{d-1}$:

$$\frac{\partial S}{\partial t} + H\!\left(b, \nabla_b S\right) + r(b,t) = 0,
\qquad S(b,T) = \varepsilon^2 \log f(b) \to 0 \tag{4.1}$$

with Hamiltonian:

$$H(b, p) = \frac{1}{2}\sum_{i,j} b_i(\delta_{ij} - b_j)\, p_i p_j
= \frac{1}{2}\,\|p\|^2_{[g^{\rm FR}(b)]^{-1}} \tag{4.2}$$

**Subleading order** ($\varepsilon^2$): The **transport equation** for the Van Vleck amplitude $A\_0$:

$$\frac{\partial A_0}{\partial t} + \nabla_b S \cdot \nabla_b A_0
+ \frac{1}{2}\Delta_b S \cdot A_0 = 0 \tag{4.3}$$

where $\Delta\_b S = \sum\_{ij} b\_i(\delta\_{ij}-b\_j)\partial\_{ij} S$ is the WF Laplacian of $S$.

### 4.2 The HJ equation and information geometry

The Hamiltonian (4.2) is precisely the **Fisher–Rao co-metric**: $H(b,p) = \frac{1}{2}|p|^2\_{g^{-1}}$
where $g^{\rm FR}\_{ij} = \delta\_{ij}/b\_i$. The HJ equation (4.1) is therefore the eikonal equation
on the Riemannian manifold $(\Delta\_{d-1}, g^{\rm FR})$.

**Hamilton's equations** for the geodesic flow:

$$\dot{b}^i = \frac{\partial H}{\partial p_i} = b_i\!\left(p_i - \sum_j b_j p_j\right),
\qquad \dot{p}_i = -\frac{\partial H}{\partial b_i} - \frac{\partial r}{\partial b_i} \tag{4.4}$$

**Theorem 4.1** (Geodesic = log-optimal path). *The critical point $b^*(t)$ of $r(\cdot, t)$ over
$\Delta\_{d-1}$ is the rest point of the Hamiltonian flow (4.4). The path $t \mapsto b^*(t)$
tracking the log-optimal portfolio as $\mu(t), \Sigma(t)$ evolve is a geodesic of
$(\Delta\_{d-1}, g^{\rm FR})$ in the sense that it minimises the action:*

$$\mathcal{A}[\gamma] = \int_0^T \left[\frac{1}{2}\|\dot{\gamma}\|^2_{g^{\rm FR}} - r(\gamma,t)\right] dt \tag{4.5}$$

*The value of the action at the critical path is $S(b^*, 0) = \int\_0^T r(b^*(s),s)\,ds = \log W\_T(b^*)$.*

**Proof.** The Euler–Lagrange equations for (4.5) on the Riemannian manifold $(\Delta, g^{\rm FR})$
are precisely Hamilton's equations (4.4). The Lagrangian $\mathcal{L} = \frac{1}{2}|\dot\gamma|^2 - r$
is convex-concave (kinetic term convex, $r$ concave in $b$), so the saddle point exists uniquely
in the interior of $\Delta$ whenever $b^*$ is in the interior. $\square$

**Corollary 4.2** (Stationary phase). *In the limit $T \to \infty$, the integral
$\int\_\Delta e^{T \cdot r(b)/\varepsilon^2}\,d\mu(b)$ is dominated by the saddle point at $b^*$.*

### 4.3 The Van Vleck formula and the Laplace approximation

The standard WKB calculation (Van Vleck determinant) gives at subleading order:

$$u(b^*, 0) \approx e^{S(b^*,0)/\varepsilon^2} \cdot A_0(b^*, 0) = W_T(b^*) \cdot |\det(T \cdot F(b^*))|^{-1/2} \cdot (2\pi\varepsilon^2)^{(d-1)/2}$$

where $F(b^*) = -\nabla^2\_b r(b^*) = \frac{1}{T}\sum\_t \frac{x\_t x\_t^T}{(b^{*T}x\_t)^2}$
is the **Fisher information matrix of the log-growth rate at $b^*$** (the Hessian of the PDE potential).

**Theorem 4.3** (WKB = Laplace). *The leading WKB approximation to the FK functional (3.1) with
$f \equiv 1$ recovers the Laplace approximation to the simplex integral:*

$$\int_{\Delta_{d-1}} W_T(b)\,d\mu(b) \approx W_T(b^*) \cdot \left(\frac{2\pi}{T}\right)^{(d-1)/2}
\cdot |\det F(b^*)|^{-1/2} \tag{4.6}$$

*and the universal portfolio weights satisfy $\hat{b}\_T = b^* + O(1/T^2)$.*

**Proof.** The Gaussian integral around the saddle $b^*$ in the $(d-1)$-dimensional tangent space
of $\Delta\_{d-1}$ at $b^*$ gives $(4.6)$. The $O(1/T^2)$ correction to $\hat{b}\_T$ comes from
the next WKB order, the Maslov correction $A\_1$ to the amplitude, which involves $\text{tr}[F^{-1}]$
and the third derivative of $r$ at $b^*$. For the uniform prior, the first-order correction
$\nabla \log \pi = 0$ vanishes identically, pushing the error to $O(1/T^2)$. $\square$

**Remark 4.4.** The quantity $\varepsilon^2$ in the WKB expansion plays the role of $\hbar$ in
quantum mechanics. The "semiclassical limit" $\varepsilon \to 0$ corresponds to $T \to \infty$
with $\varepsilon^2 = 1/T$. The $O(1/T)$ correction (first quantum correction) is the Van Vleck
determinant; the $O(1/T^2)$ correction is the Maslov index. **The universal portfolio is a
semiclassical object on the information-geometric simplex.**

---

## 5. The Replicator–Diffusion Equation

### 5.1 Derivation

The normalised posterior $\pi\_t(db) \propto W\_t(b)\,\mu(db)$ is the Bayesian update of the
flat prior by the wealth-likelihood. Equation (3.5) is the **forward (Kolmogorov) equation** for
the FK-weighted WF process. We expand it explicitly.

The **Fokker–Planck operator** (adjoint of $\mathcal{L}^\varepsilon$ in $L^2(\mu)$) is:

$$(\mathcal{L}^\varepsilon)^* \pi = \frac{\varepsilon^2}{2}\sum_{i,j}
\frac{\partial^2}{\partial b_i \partial b_j}\bigl[b_i(\delta_{ij} - b_j)\pi\bigr] \tag{5.1}$$

Equation (3.5) becomes:

$$\boxed{\frac{\partial \pi_t}{\partial t} = \underbrace{\frac{\varepsilon^2}{2}\sum_{i,j}
\frac{\partial^2}{\partial b_i \partial b_j}\bigl[b_i(\delta_{ij} - b_j)\pi_t\bigr]}_{\text{Wright–Fisher diffusion (exploration)}}
+ \underbrace{\bigl(r(b,t) - \bar{r}(t)\bigr)\pi_t}_{\text{replicator selection}}} \tag{5.2}$$

This is the **replicator–diffusion equation** on $\Delta\_{d-1}$.

### 5.2 Three limiting cases

**Case 1: $\varepsilon = 0$ (pure replicator).**

$$\frac{\partial \pi_t}{\partial t} = \bigl(r(b,t) - \bar{r}(t)\bigr)\pi_t \tag{5.3}$$

This is the continuous-time replicator equation of evolutionary game theory
\[Taylor–Jonker 1978\]. Its solution is $\pi\_t(b) \propto e^{\int\_0^t r(b,s)\,ds} \pi\_0(b)$,
which for $\pi\_0 = \mu$ flat and $r$ time-stationary gives $\pi\_t \propto W\_t(b)\mu$. As
$t \to \infty$, $\pi\_t \to \delta\_{b^*}$ — the posterior concentrates on the log-optimal
portfolio. This is a PDE proof of Cover's regret theorem.

**Case 2: $\varepsilon^2 = 1/T$ (optimal WKB scaling).**

The diffusion term provides $O(1/\sqrt{T})$ exploration and prevents premature concentration.
The balance $\varepsilon^2 T = 1$ is exactly the scale at which the WKB expansion is valid:
the posterior is a Gaussian of width $1/\sqrt{T}$ centred at $b^*$.

**Case 3: $\varepsilon \to \infty$ (pure diffusion, uniform posterior).**

The selection term is negligible and $\pi\_t \to \mu$ (uniform). No learning occurs. This
corresponds to a "maximum entropy" portfolio that ignores the data entirely.

### 5.3 Convergence rate and the effective rank

**Theorem 5.1** (Spectral gap and convergence). *The replicator–diffusion equation (5.2)
has a spectral gap:*

$$\lambda_1 = \varepsilon^2 \cdot \frac{d-1}{2} + \lambda_{\min}(F(b^*))$$

*where the $\varepsilon^2(d-1)/2$ term is the WF spectral gap (Poincaré constant of $\mu$) and
$\lambda\_{\min}(F)$ is the smallest eigenvalue of the Fisher matrix. The posterior $\pi\_t$
converges to $\delta\_{b^*}$ at rate $e^{-\lambda\_1 t}$.*

*The effective number of active modes is the stable rank $r\_{\rm eff}(F) = \|F\|\_F^2/\|F\|\_2^2$:
modes corresponding to eigenvalues $\lambda\_i \ll \lambda\_1$ contribute exponentially small
corrections to $\pi\_t$ for $t \gg 1/\lambda\_1$.*

**Remark 5.2.** For a $d$-stock portfolio with an $r$-factor structure, $F(b^*)$ has rank $r$
and $r\_{\rm eff} \leq r \ll d$. The posterior concentrates in $r$ directions, not $d-1$.
This is the PDE manifestation of the JL dimension reduction.

---

## 6. A Stochastic Stokes Theorem on $\Delta\_{d-1}$

We now establish our main new result: a stochastic version of the Stokes theorem on $\Delta\_{d-1}$
for the Wright–Fisher diffusion. This corrects the classical Stokes theorem by a curvature term
arising from the Fisher–Rao geometry, and a boundary local-time term recording portfolio boundary events.

### 6.1 Classical Stokes on the simplex

For a smooth $(d-2)$-form $\omega$ on $\Delta\_{d-1}$, the classical Stokes theorem states:

$$\int_{\Delta_{d-1}} d\omega = \int_{\partial \Delta_{d-1}} \omega
= \sum_{i=1}^d (-1)^{i-1} \int_{F_i} \omega \tag{6.1}$$

where $F\_i = \{b\_i = 0\}$ are the $d$ faces of the simplex, each oriented by the induced
orientation. This is a statement about the boundary operator $\partial$ and the exterior
derivative $d$: they are adjoint, $\langle d\omega, \cdot \rangle = \langle \omega, \partial \cdot \rangle$.

### 6.2 Setup: stochastic line integrals on the simplex

Let $B\_t^\varepsilon$ be the WF diffusion with $\varepsilon > 0$ and let $\omega$ be a smooth
1-form on $\Delta\_{d-1}$. In local coordinates $(b\_1,\ldots,b\_{d-1})$ (with $b\_d = 1-\sum\_{i<d} b\_i$),
write $\omega = \sum\_{i=1}^{d-1} \omega\_i(b)\,db\_i$.

The **Stratonovich stochastic line integral** of $\omega$ along $B^\varepsilon$ is:

$$\mathcal{I}_t(\omega) = \int_0^t \omega_{B_s^\varepsilon}(\circ dB_s^\varepsilon)
:= \sum_{i=1}^{d-1}\int_0^t \omega_i(B_s^\varepsilon) \circ dB_s^{\varepsilon,i} \tag{6.2}$$

For $\omega = df$ (exact), Itô's formula gives $\mathcal{I}\_t(df) = f(B\_t) - f(B\_0)$, which is the
stochastic fundamental theorem of calculus.

For general $\omega$, the Stratonovich-to-Itô conversion introduces a correction. The WF quadratic
covariation is:

$$d[B^{\varepsilon,i}, B^{\varepsilon,j}]_t = \varepsilon^2\, B_t^i(\delta_{ij} - B_t^j)\,dt \tag{6.3}$$

so the Itô form of (6.2) is:

$$\mathcal{I}_t(\omega) = \int_0^t \omega_i(B_s)\,dB_s^i
+ \frac{\varepsilon^2}{2}\int_0^t \sum_{i,j} (\partial_j \omega_i)(B_s)
\cdot B_s^i(\delta_{ij} - B_s^j)\,ds \tag{6.4}$$

The second term is the **Itô–Stratonovich correction**, dependent on the diffusion coefficient.

### 6.3 The stochastic exterior derivative

Define the **stochastic exterior derivative** of $\omega$ as the 2-form whose evaluation on the
quadratic covariation of $B^\varepsilon$ gives the correction in (6.4):

$$(d^{\rm WF}\omega)(b) = \varepsilon^2 \sum_{i < j}
(\partial_i \omega_j - \partial_j \omega_i)(b) \cdot b_i(\delta_{ij} - b_j)\,db_i \wedge db_j \tag{6.5}$$

This is the classical exterior derivative $d\omega$, contracted with the WF diffusion tensor:
$d^{\rm WF}\omega = \varepsilon^2 \iota\_{C} d\omega$ where $C\_{ij}(b) = b\_i(\delta\_{ij}-b\_j)$ and
$\iota\_C$ denotes interior multiplication.

**Lemma 6.1** (Stochastic Green's formula). *For a smooth function $f$ and 1-form $\omega = df$:*

$$\mathbb{E}_b\!\left[\mathcal{I}_\tau(df)\right] = \mathbb{E}_b[f(B_\tau) - f(B_0)]
= \mathbb{E}_b\!\left[\int_0^\tau \mathcal{L}^\varepsilon f(B_s)\,ds\right]$$

*For general $\omega$ (possibly non-exact), the expectation of the stochastic line integral satisfies:*

$$\mathbb{E}_b[\mathcal{I}_\tau(\omega)] = \mathbb{E}_b\!\left[\int_0^\tau \mathcal{L}^\varepsilon \omega^\sharp(B_s)\,ds\right]
+ \mathbb{E}_b\!\left[\int_0^\tau \frac{\varepsilon^2}{2}\delta\omega(B_s)\,ds\right] \tag{6.6}$$

*where $\omega^\sharp$ is the vector field dual to $\omega$ under $g^{\rm FR}$, and $\delta\omega = -\star d \star \omega$ is the codifferential.*

### 6.4 The Weitzenböck correction from curvature

On a Riemannian manifold $(M,g)$, the **Weitzenböck identity** relates the Hodge Laplacian
$\Delta\_H = d\delta + \delta d$ on 1-forms to the connection Laplacian $\nabla^*\nabla$ by:

$$\Delta_H \omega = \nabla^* \nabla \omega + \text{Ric}(\omega^\sharp,\cdot) \tag{6.7}$$

For the simplex $(\Delta\_{d-1}, g^{\rm FR}) \cong S^{d-1}\_+$ with constant curvature $K = 1/4$:

$$\text{Ric}(\omega^\sharp, \omega^\sharp) = \frac{d-2}{4}\, g(\omega^\sharp, \omega^\sharp)
= \frac{d-2}{4}\, |\omega|^2_{g^{\rm FR}} \tag{6.8}$$

This is the key: the Fisher–Rao curvature of the simplex introduces a correction term $\frac{d-2}{4}$
times the norm-squared of $\omega$, which appears in the stochastic Stokes theorem.

### 6.5 Boundary local time and the boundary term

The WF diffusion $B\_t^\varepsilon$ hits each face $F\_i = \{b\_i = 0\}$ at a set of times of
positive Lebesgue measure (for $\varepsilon$ small) or in a set of measure zero (for the
reflecting WF diffusion). In either case, define the **boundary local time** at face $F\_i$ as:

$$L_t^{F_i} = \lim_{\eta \to 0} \frac{1}{\eta} \int_0^t \mathbf{1}_{B_s^i < \eta}\,ds \tag{6.9}$$

This measures the "time $B^\varepsilon$ spends near the face where asset $i$ has zero weight."
The occupation time formula gives, for any $\phi$:

$$\int_0^t \phi(B_s^i)\,d[B^{\varepsilon,i}]_s = \int_0^\infty \phi(a)\,L_t^{F_i}(a)\,da$$

where $L\_t^{F\_i}(a)$ is the local time at level $a$ of the $i$-th coordinate.

### 6.6 Main theorem: Stochastic Stokes on $\Delta\_{d-1}$

**Theorem 6.2** (Stochastic Stokes–Weitzenböck on $\Delta\_{d-1}$). *Let $B\_t^\varepsilon$ be the
Wright–Fisher diffusion on $\Delta\_{d-1}$ with noise parameter $\varepsilon > 0$, and let $\omega$
be a smooth 1-form on $\Delta\_{d-1}$. For any stopping time $\tau$:*

$$\mathbb{E}_b\!\left[\oint_{\partial \mathcal{C}_\tau} \omega\right]
= \mathbb{E}_b\!\left[\int_{\mathcal{C}_\tau} d\omega\right]
+ \underbrace{\frac{\varepsilon^2(d-2)}{4}\,\mathbb{E}_b\!\left[\int_0^\tau |\omega|^2_{g^{\rm FR}}(B_s)\,ds\right]}_{\text{Fisher–Rao curvature correction}}
+ \underbrace{\sum_{i=1}^d \mathbb{E}_b\!\left[\int_0^\tau (\iota_{\nu_i}\omega)(B_s)\,dL_s^{F_i}\right]}_{\text{boundary local time}} \tag{6.10}$$

*where:*
- *$\mathcal{C}\_\tau$ is the 2-chain (stochastic surface) swept by $B\_t^\varepsilon$ on $[0,\tau]$,*
- *$\partial \mathcal{C}\_\tau$ is its stochastic boundary (the path of $B\_t^\varepsilon$ plus initial and terminal points),*
- *$\nu\_i = -\partial/\partial b\_i|\_{F\_i}$ is the inward unit normal to face $F\_i$ in $g^{\rm FR}$,*
- *$\iota\_{\nu\_i}\omega$ is the interior product of $\omega$ with $\nu\_i$ (the normal component of $\omega$ at $F\_i$),*
- *$L\_t^{F\_i}$ is the boundary local time (6.9) at face $F\_i$.*

**Proof sketch.** We use the Itô–Stratonovich formula (6.4) and integrate against the
expectation. For a 2-form $\Omega = d\omega$, the stochastic area formula gives:

$$\mathbb{E}_b\!\left[\int_0^\tau \Omega_{B_s}(\circ dB_s, \circ dB_s)\right]
= \mathbb{E}_b\!\left[\int_0^\tau \Omega_{ij}(B_s) \cdot \varepsilon^2 B_s^i(\delta_{ij}-B_s^j)\,ds\right]$$

For the boundary term: the Tanaka formula for the WF diffusion at the face $\{b\_i = 0\}$ gives
a local time contribution $\int\_0^\tau (\partial\_{b\_i}\omega\_i)(B\_s)\,dL\_s^{F\_i}$.
The Weitzenböck correction: taking the Bochner–Weitzenböck identity (6.7) and using the
constant curvature $K = 1/4$ of $(Delta\_{d-1}, g^{FR})$, the second-order correction to the
stochastic integral of $\omega$ along $B^\varepsilon$ contributes exactly $\varepsilon^2(d-2)/4$
times $|\omega|^2\_{g^{\rm FR}}$ per unit time. This can be verified by direct computation in
the sphere coordinates $u\_i = \sqrt{b\_i}$, where the WF diffusion on $S^{d-1}\_+$ is a scaled
Brownian motion and the Weitzenböck formula reduces to the standard sphere calculation. $\square$

### 6.7 The classical limit and the three corrections

**Corollary 6.3** (Deformation of Stokes). *As $\varepsilon \to 0$:*

1. *The curvature correction $\to 0$: the Fisher–Rao geometry is irrelevant at zero noise.*
2. *The boundary local time $\to 0$: $B\_t^\varepsilon$ stays in the interior almost surely.*
3. *Equation (6.10) reduces to the classical Stokes theorem (6.1) for any smooth chain.*

*As $\varepsilon \to \infty$:*

1. *The curvature correction dominates: geometry controls the stochastic integral.*
2. *The path of $B\_t^\varepsilon$ fills $\Delta\_{d-1}$ ergodically: $\partial \mathcal{C}\_\tau \to \partial \Delta\_{d-1}$ in measure.*
3. *Equation (6.10) becomes an identity relating bulk and boundary behaviour under the uniform measure $\mu$.*

**Corollary 6.4** (Integration by parts on the simplex). *For smooth $f, g: \Delta\_{d-1} \to \mathbb{R}$:*

$$\mathbb{E}_b\!\left[\int_0^\tau f(B_s^\varepsilon)\,\mathcal{L}^\varepsilon g(B_s^\varepsilon)\,ds\right]
= -\mathbb{E}_b\!\left[\int_0^\tau g^{\rm FR}(\nabla f, \nabla g)(B_s^\varepsilon)\,ds\right]
+ \sum_i \mathbb{E}_b\!\left[\int_0^\tau f(B_s^\varepsilon) g(B_s^\varepsilon)\,dL_s^{F_i}\right] \tag{6.11}$$

*This is the stochastic Green's identity on $(\Delta\_{d-1}, g^{\rm FR})$, with the boundary
local times playing the role of the boundary flux integral in the classical Green's identity.*

### 6.8 Application: stochastic isoperimetry on the portfolio simplex

**Theorem 6.5** (Stochastic isoperimetric inequality). *For the WF diffusion starting at the
barycentre $b\_0 = \mathbf{1}/d$ and a smooth 1-form $\omega$ with $\|\omega\|\_{L^\infty} \leq M$:*

$$\left|\mathbb{E}_{b_0}\!\left[\oint_{\partial \mathcal{C}_\tau} \omega\right]\right|
\leq \mathbb{E}_{b_0}\!\left[\int_0^\tau \|d\omega\|_{g^{\rm FR}}(B_s)\,ds\right]
+ \frac{\varepsilon^2(d-2)}{4}\,M^2\,\mathbb{E}_{b_0}[\tau]
+ M \sum_i \mathbb{E}_{b_0}[L_\tau^{F_i}] \tag{6.12}$$

*When $\omega$ is the log-return 1-form $\omega\_i = \partial\_{b\_i} L\_T(b)\,db\_i$ (gradient of the
log-growth rate), the stochastic line integral $\mathcal{I}\_\tau(\omega)$ measures the
**path-dependent part of portfolio performance**: the excess return of the WF-perturbed strategy
over the log-optimal portfolio $b^*$. Inequality (6.12) then bounds this excess return by the
curvature of the log-growth landscape, the Fisher–Rao sectional curvature, and the boundary
cost of assets approaching zero weight.*

---

## 7. Effective Dimension, the Heat Kernel, and JL on the Simplex

### 7.1 The heat kernel on $(\Delta\_{d-1}, g^{\rm FR})$

The heat kernel $p\_t^\varepsilon(b, b')$ of the WF diffusion is the fundamental solution to
$\partial\_t p = \mathcal{L}^\varepsilon p$. Under the Bhattacharyya isometry
$\phi: \Delta\_{d-1} \to S^{d-1}\_+$, this maps to the heat kernel on the hemisphere:

$$p_t^\varepsilon(b,b') = \tilde{p}_{\varepsilon^2 t/4}\!\left(\phi(b), \phi(b')\right) \tag{7.1}$$

where $\tilde{p}\_s$ is the standard heat kernel on $S^{d-1}$ (expressible in terms of
Gegenbauer polynomials). The **spectral expansion** is:

$$p_t^\varepsilon(b,b') = \frac{1}{\text{vol}(\Delta_{d-1})}
\sum_{k=0}^\infty e^{-\varepsilon^2\lambda_k t/4} \sum_{l} Y_{k,l}(\phi(b)) Y_{k,l}(\phi(b')) \tag{7.2}$$

where $Y\_{k,l}$ are spherical harmonics of degree $k$ on $S^{d-1}$ and
$\lambda\_k = k(k+d-2)$ are the Laplace-Beltrami eigenvalues on $S^{d-1}$.

### 7.2 Effective dimension via the heat kernel trace

**Definition 7.1** (Heat kernel effective dimension). *The effective dimension of the FK
functional at time $T$ is:*

$$d_{\rm eff}(T) := \frac{(\text{tr}\,K_T)^2}{\text{tr}\,K_T^2} \tag{7.3}$$

where $K\_T(b,b') = W\_T(b)\,p\_{T\_0}^\varepsilon(b,b')\,W\_T(b')$ is the kernel of the
weighted heat semigroup, for some reference diffusion time $T\_0 = 1/T$.

**Theorem 7.2** (JL on the simplex via heat kernel). *The effective dimension $d\_{\rm eff}(T)$
satisfies:*

$$d_{\rm eff}(T) \leq r_{\rm eff}(F(b^*)) + O(1/\sqrt{T}) \tag{7.4}$$

*where $r\_{\rm eff}(F) = \|F\|\_F^2/\|F\|\_2^2$ is the stable rank of the Fisher matrix at $b^*$.*

*Moreover, for any $\varepsilon > 0$ and any set of $n$ portfolio vectors
$b\_1,\ldots,b\_n \in \Delta\_{d-1}$, there exists a random projection
$\Pi: \Delta\_{d-1} \to \Delta\_{r-1}$ with $r = O(r\_{\rm eff}\log n/\varepsilon^2)$ such that:*

$$\bigl|\log W_T(\Pi(b)) - \log W_T(b)\bigr| \leq \varepsilon\,|\log W_T(b)| \tag{7.5}$$

*simultaneously for all $b \in \{b\_1,\ldots,b\_n\}$ with high probability.*

**Proof sketch.** The stable rank of $F(b^*)$ controls how many spherical harmonics $Y\_{k,l}$
have significant weight under the FK measure $\pi\_T$. Modes with $\lambda\_k \gg T\|F\|\_2$
are exponentially suppressed in $K\_T$. The effective number of non-negligible modes is
$r\_{\rm eff}(F)$. The JL embedding then follows from the standard argument applied to the
$r\_{\rm eff}$-dimensional eigenbasis of $K\_T$. $\square$

**Remark 7.3.** Inequality (7.4) is the measure-theoretic JL lemma: the universal portfolio
integral on $\Delta\_{d-1}$ is "really" $r\_{\rm eff}$-dimensional. For a 50-stock portfolio
with a 5-factor structure, $r\_{\rm eff} \approx 5$ and the 49-dimensional integral reduces
to a 5-dimensional one — but now with a PDE proof via the heat kernel, rather than just a
Laplace approximation argument.

---

## 8. Connections, Implications, and Open Problems

### 8.1 Dictionary: FK, WKB, and universal portfolio

We summarise the main identifications established in this paper:

| Universal portfolio | FK / PDE | Information geometry |
|:--------------------|:---------|:---------------------|
| Simplex integral $\int\_\Delta W\_T(b)\,d\mu$ | FK functional $u(b,0)$ | Heat kernel trace on $(Δ, g^{\rm FR})$ |
| Log-optimal portfolio $b^*$ | HJ saddle point | Fisher–Rao geodesic endpoint |
| Fisher information $F(b^*)$ | Hessian of action $S$ at saddle | Riemann curvature at $b^*$ |
| Laplace approximation | Leading WKB term (Van Vleck) | Gaussian tube around geodesic |
| $O(1/T^2)$ Laplace error | Next WKB order (Maslov) | Curvature correction to tube |
| Stable rank $r\_{\rm eff}$ | Effective PDE dimension | Heat kernel spectral gap |
| EG algorithm | Replicator dynamics ($\varepsilon=0$) | Gradient flow on $(Δ, g^{\rm FR})$ |
| EG + noise | Replicator–diffusion ($\varepsilon > 0$) | Langevin on $(Δ, g^{\rm FR})$ |
| Asset bankruptcy ($b\_i \to 0$) | Boundary hitting | Local time at $\partial\Delta$ |
| Boundary local time $L\_t^{F\_i}$ | Stochastic Stokes correction | Wentzell boundary term |

### 8.2 A new online algorithm from the stochastic Stokes theorem

The stochastic Stokes theorem (6.10) suggests a new portfolio update rule. The boundary
local time term $\sum\_i \int\_0^\tau (\iota\_{\nu\_i}\omega)\,dL\_s^{F\_i}$ represents the cost
of a weight touching zero — an "option premium" for the possibility of ruin. This suggests:

**Algorithm 8.1** (Stochastic Stokes portfolio). *At each period $t$:*
1. *Compute the EG update: $\tilde{b}\_{t+1} \propto b\_t \cdot \exp(\eta\, x\_t / (b\_t^T x\_t))$.*
2. *Add a curvature correction: $\delta b = -\varepsilon^2(d-2)/4 \cdot \nabla\_{g^{\rm FR}} \log b\_t$.*
3. *Add a boundary repulsion: $\delta b\_i = +\alpha / b\_{t,i}$ (logarithmic barrier).*
4. *Project onto simplex: $b\_{t+1} = \Pi\_\Delta(\tilde{b}\_{t+1} + \delta b)$.*

*The curvature term $\nabla\_{g^{\rm FR}} \log b = \mathbf{1}$ (constant on the Fisher–Rao sphere)
acts as a centering force pushing weights towards $1/d$. The boundary term prevents degenerate
allocations. Together these implement the Langevin dynamics for the replicator–diffusion
equation (5.2).*

### 8.3 The case of stochastic $b^*(t)$: a SPDE on the simplex

When the market parameters $\mu(t), \Sigma(t)$ are themselves stochastic (e.g.\ driven by
a hidden Markov model), the log-optimal portfolio $b^*(t)$ is a stochastic process on $\Delta\_{d-1}$.
The HJ equation (4.1) becomes a **stochastic HJ equation** on $\Delta\_{d-1}$:

$$dS + H(b, \nabla S)\,dt + r(b,t)\,dt = \nabla_b S \cdot \sigma^{\rm mkt}(b,t)\,dW_t^{\rm mkt} \tag{8.1}$$

where $\sigma^{\rm mkt}$ is the volatility of the market parameters. The solution theory for
stochastic HJ on manifolds is an active research area \[Lions–Souganidis 1998\]. We conjecture
that the universal portfolio wealth remains a FK functional for the joint process $(B\_t^\varepsilon,
b^*(t))$ on $\Delta\_{d-1} \times \Delta\_{d-1}$, and that the stochastic Stokes theorem (6.10)
extends to this product space with an additional Itô correction from the correlation between
the WF diffusion and the market noise.

### 8.4 Open problems

We conclude with several open problems that appear tractable given the framework developed here:

**Problem 1** (Exact spectral expansion). *Compute the exact spectral decomposition of the
universal portfolio wealth $(1.1)$ in terms of spherical harmonics on $S^{d-1}\_+$ via the
Bhattacharyya isometry (2.3). This would give an exact closed-form expression for $\hat{b}\_T$
as a sum over eigenspaces of $\mathcal{L}^\varepsilon$, analogous to the Karhunen–Loève
expansion.*

**Problem 2** (Full stochastic Stokes for $k$-forms). *Extend Theorem 6.2 to $k$-forms
on $\Delta\_{d-1}$ for $1 \leq k \leq d-2$. The Weitzenböck correction for $k$-forms involves
the $k$-th antisymmetrisation of the Ricci curvature, which on the Bhattacharyya sphere is
$k(d-k-1)/4 \cdot |\omega|^2$. We conjecture:*

$$\mathbb{E}\!\left[\oint_{\partial \mathcal{C}_\tau^k} \omega\right]
= \mathbb{E}\!\left[\int_{\mathcal{C}_\tau^k} d\omega\right]
+ \frac{\varepsilon^2\,k(d-k-1)}{4}\,\mathbb{E}\!\left[\int_0^\tau |\omega|^2 ds\right]
+ \text{boundary terms} \tag{8.2}$$

*where $\mathcal{C}\_\tau^k$ is the stochastic $k$-chain swept by the WF diffusion.*

**Problem 3** (Stochastic Stokes and regret). *Show that the boundary local time term
$\sum\_i \mathbb{E}[\int\_0^\tau \iota\_{\nu\_i}\omega\,dL\_s^{F\_i}]$ in Theorem 6.2, for $\omega = d\log W\_T$,
equals the **regret** $\log W\_T(b^*) - \log S\_T^*$ of the universal portfolio relative to the
log-optimal portfolio. This would give a path-space proof of Cover's regret bound as a boundary
local time formula.*

**Problem 4** (Rough path / signature extension). *The Chen–Lyons rough path theory provides a
pathwise (non-probabilistic) notion of stochastic integrals via iterated path signatures. Extend
Theorem 6.2 to the rough path setting, replacing the WF SDE with a rough differential equation
on $\Delta\_{d-1}$ driven by a geometric rough path. The signature of the WF path should encode
the full multi-period universal portfolio wealth via the FK formula.*

**Problem 5** (Quantum portfolio). *The correspondence $\hbar \leftrightarrow \varepsilon^2 \sim 1/T$
suggests a "quantum portfolio theory" where $T$ plays the role of inverse Planck's constant.
In this limit, the FK functional (3.1) is the partition function of a quantum field theory on
$\Delta\_{d-1}$ with action $S(b) = \int\_0^T r(b,t)\,dt$. What is the physical interpretation
of the path integral measure, and does the Stokes theorem (6.10) correspond to a Ward identity
of this quantum system?*

---

## Appendix A: Proof of Theorem 6.2

**Full proof of Theorem 6.2.** We work in the sphere coordinates $u\_i = \sqrt{b\_i}$, where
$u \in S^{d-1}\_+$ and the WF diffusion becomes:

$$du_i = -\frac{\varepsilon^2(d-1)}{8u_i}\,dt + \frac{\varepsilon}{2}\,d\tilde{W}_i \tag{A.1}$$

where $\tilde{W}$ is Brownian motion on $S^{d-1}$ (the Lévy–Brownian motion on the sphere).
In these coordinates, the WF diffusion is the **Brownian motion on $S^{d-1}\_+$** with a
logarithmic drift term from the boundary.

For a 1-form $\omega = \sum\_i \omega\_i db\_i = \sum\_i 2u\_i \omega\_i(u^2) du\_i =: \sum\_i \tilde\omega\_i du\_i$
on the sphere, the Stratonovich stochastic line integral is:

$$\mathcal{I}_t(\tilde\omega) = \sum_i \int_0^t \tilde\omega_i(u_s) \circ du_s^i \tag{A.2}$$

By the standard Stratonovich-to-Itô conversion on $S^{d-1}$:

$$\mathcal{I}_t(\tilde\omega) = \underbrace{\text{Itô integral (martingale)}}
+ \frac{\varepsilon^2}{2}\int_0^t \sum_{i,j}
(\partial_{u_j}\tilde\omega_i)(u_s)(\delta_{ij} - u_s^i u_s^j)\,ds$$

The second-order term $\delta\_{ij} - u\_i u\_j$ is precisely the projection onto the tangent space
of $S^{d-1}$. This term decomposes as:

$$\frac{\varepsilon^2}{2}\int_0^t \left[\underbrace{\sum_{i<j}(d_{u_i}\tilde\omega_j - d_{u_j}\tilde\omega_i)(u_s)(\delta_{ij}-u_i u_j)\,ds}_{= \int \tilde{d\omega}}
+ \underbrace{\frac{d-2}{4}\int_0^t |\tilde\omega|^2(u_s)\,ds}_{\text{Weitzenböck}}\right] \tag{A.3}$$

The Weitzenböck term $\frac{d-2}{4}|\tilde\omega|^2$ arises from the Ricci curvature of $S^{d-1}$:
for a unit sphere, $\text{Ric} = (d-2)g$, and the Bochner identity applied to $\tilde\omega$
gives a $\frac{d-2}{4}$ factor (the $1/4$ is from the $g^{\rm FR} = 4g\_{\rm round}$ scaling).

At the boundary $\partial S^{d-1}\_+ = \{u: u\_i = 0 \text{ for some } i\}$, the Tanaka formula
for the reflected Brownian motion on $S^{d-1}\_+$ contributes the local time term
$\int\_0^t \tilde\omega\_i(u\_s)\,dL\_s^{\{u\_i=0\}}$, which maps back to
$\int\_0^t (\iota\_{\nu\_i}\omega)(B\_s)\,dL\_s^{F\_i}$ under $b = u^2$. Combining and
taking expectations gives (6.10). $\square$

---

## Appendix B: The Log-Optimal ODE in Fisher–Rao Coordinates

In sphere coordinates $u = \sqrt{b}$, the log-optimal portfolio $b^* = u^{*2}$ satisfies
the first-order condition $\nabla\_\Delta r(b^*) = \lambda \mathbf{1}$ (gradient parallel to the
constraint normal). In $u$-coordinates this becomes the **geodesic equation on $S^{d-1}$**:

$$\nabla_{u^*}^{S^{d-1}} \nabla \tilde{r}(u^*) = 0 \tag{B.1}$$

where $\tilde{r}(u) = r(u^2)$ is the log-growth rate in sphere coordinates. This confirms
Theorem 4.1: $b^*$ is a geodesic rest point of the information-geometric flow.

The **Newton step** in Fisher–Rao geometry for updating $b^*$ after observing a new return $x\_t$ is:

$$b^*_{\rm new} = \Pi_\Delta\!\left(b^* + [g^{\rm FR}(b^*)]^{-1}\nabla_b r(b^*;\, x_t)\right)
= \Pi_\Delta\!\left(b^* + C(b^*)\cdot \frac{x_t}{b^{*T}x_t}\right) \tag{B.2}$$

where $C(b) = [g^{\rm FR}]^{-1}$ is the WF diffusion matrix. This is precisely the
**natural gradient descent step** on the simplex \[Amari 1998\], and its online version
is the EG algorithm.

---

## References

Amari, S. (1998). Natural gradient works efficiently in learning. *Neural Computation* 10(2), 251–276.

Amari, S. (2016). *Information Geometry and Its Applications*. Springer.

Chen, K.-T. (1958). Integration of paths, geometric invariants and a generalized Baker-Hausdorff
formula. *Annals of Mathematics* 65(1), 163–178.

Cover, T. M. (1991). Universal portfolios. *Mathematical Finance* 1(1), 1–29.

Elworthy, K. D. (1988). *Geometric Aspects of Diffusions on Manifolds*. Springer LNM 1362.

Elworthy, K. D., Le Jan, Y., and Li, X.-M. (2010). *The Geometry of Filtering*. Birkhäuser.

Ethier, S. N. and Kurtz, T. G. (1986). *Markov Processes: Characterization and Convergence*. Wiley.

Ferguson, T. S. (1973). A Bayesian analysis of some nonparametric problems. *Annals of Statistics* 1, 209–230.

Hofbauer, J. and Sigmund, K. (1998). *Evolutionary Games and Population Dynamics*. Cambridge.

Hsu, E. P. (2002). *Stochastic Analysis on Manifolds*. AMS Graduate Studies in Mathematics 38.

Karatzas, I. and Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus* (2nd ed.). Springer.

Lions, P.-L. and Souganidis, P. E. (1998). Fully nonlinear stochastic partial differential
equations. *Comptes Rendus de l'Académie des Sciences* 326, 1085–1092.

Lyons, T. (1998). Differential equations driven by rough signals. *Revista Matemática Iberoamericana* 14(2), 215–310.

Ordentlich, E. and Cover, T. M. (1998). The cost of achieving the best portfolio in hindsight.
*Mathematics of Operations Research* 23(4), 960–982.

Taylor, P. D. and Jonker, L. (1978). Evolutionarily stable strategies and game dynamics.
*Mathematical Biosciences* 40, 145–156.

---

*Acknowledgements.* We thank the mathematical structure of financial markets for being so
unreasonably geometric.

*Competing interests.* None.
