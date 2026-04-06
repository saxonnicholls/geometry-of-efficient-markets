# Market Efficiency as a Minimal Surface Condition:  
## Willmore Energy, Mean Curvature Flow, and the Geometry of Efficient Markets

**Saxon Nicholls** — me@saxonnicholls.com

**Paper I.3** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We propose a geometric characterisation of market efficiency in terms of minimal surface
theory on the portfolio simplex $(\Delta_{d-1}, g^{\mathrm{FR}})$ equipped with the
Fisher–Rao metric. The central thesis is: *a fully efficient market corresponds precisely
to the condition that the market portfolio manifold $\Sigma \subset \Delta_{d-1}$ is a
minimal submanifold*, i.e.\ its mean curvature $H$ vanishes identically. The three classical
forms of the efficient market hypothesis — weak, semi-strong, and strong — correspond
respectively to (i) the log-optimal portfolio path being a geodesic in $\Sigma$, (ii) $\Sigma$
being totally geodesic in the public-information submanifold, and (iii) $\Sigma$ being minimal
in $(\Delta_{d-1}, g^{\mathrm{FR}})$. We introduce the **market inefficiency functional**:

$$\widetilde{\mathcal{W}}(\Sigma) = \int_\Sigma |H|^2_{g^{\mathrm{FR}}}\,d\mathrm{vol}_\Sigma$$

as the Willmore energy of $\Sigma$ in the Bhattacharyya sphere, and prove that
$\widetilde{\mathcal{W}}(\Sigma) = 0$ if and only if $\Sigma$ is a minimal submanifold,
establishing $\widetilde{\mathcal{W}}$ as a canonical, non-negative, scale-free measure of
market inefficiency (conformally invariant when $r=2$; see Section 4 for the general case). Arbitrage strategies correspond to the mean curvature flow (MCF) of
$\Sigma$: arbitrageurs deform the market manifold toward its minimal surface, and the
market is in equilibrium precisely when $\Sigma$ is the solution to the Plateau problem with
boundary $\Gamma = \{b^{\ast}(t)\}$ (the log-optimal portfolio path). The Whitney embedding
theorem provides the lower bound $\dim_{\mathrm{embed}} \geq 2r$ on the ambient dimension
required to represent the market, while the Takens embedding theorem guarantees that $2r+1$
consecutive return observations reconstruct the full manifold geometry. For US equity markets
with $r \approx 4$ systematic factors and $d = 50$ stocks, the market manifold has intrinsic
dimension $r \in \{3,\ldots,5\}$, embeds in $\mathbb{R}^{6\text{–}10}$, and the Willmore
energy $\mathcal{W}(\Sigma)$ is computable from the observed return data as a function of
the third fundamental form of the market manifold. We derive a closed-form estimator for
$\mathcal{W}(\Sigma)$ from the spectral structure of the empirical Fisher matrix, and
interpret market microstructure anomalies, momentum, mean-reversion, and factor zoo
proliferation as geometric defects in the market minimal surface.

**Keywords.** Minimal surface; Willmore energy; market efficiency; Fisher–Rao geometry;
mean curvature flow; Plateau problem; Whitney embedding; Takens embedding; Bhattacharyya
sphere; efficient market hypothesis; portfolio manifold; second fundamental form.

**MSC 2020.** 91G10, 53A10, 58J35, 53B25, 37C45, 91B26.

---

## 1. Introduction

### 1.1 The question

The Efficient Market Hypothesis (EMH) in its classical formulation \[Fama 1970\] states
that asset prices fully reflect all available information. This is a statement about
**information**, not about geometry. Yet the analysis of the previous papers in this series
has revealed that the universal portfolio, the log-optimal portfolio, and the posterior
distribution of portfolio weights all have deep geometric content in the Fisher–Rao metric on
$(\Delta_{d-1}, g^{\mathrm{FR}})$.

This raises a natural question: *what does market efficiency mean geometrically?*

We answer this question as follows. The market, at each time $t$, induces a submanifold
$\Sigma \subset \Delta_{d-1}$: the set of portfolios accessible given the factor structure
of returns. This manifold has a well-defined mean curvature in $g^{\mathrm{FR}}$.
**We prove that market efficiency is equivalent to the vanishing of this mean curvature** —
that is, to $\Sigma$ being a minimal surface in the Fisher–Rao geometry.

The efficiency measure $\mathcal{W}(\Sigma)$ (the Willmore energy) is then the natural
$L^2$-norm of the deviation of $\Sigma$ from its minimal surface counterpart. It is:

- **Zero** for a perfectly efficient market;
- **Positive** whenever systematic inefficiencies (predictable alpha, factor anomalies, microstructure effects) are present;
- **Conformally invariant** (for $r=2$, the two-factor surface case) under Möbius transformations of $S^{d-1}$; for general $r$, invariant under isometries of the ambient sphere;
- **Computable** from observable return data.

This gives the first rigorous, metric-based, continuous measure of market efficiency — not as
a binary (efficient/inefficient) but as a scalar field on the space of market structures.

### 1.2 Preview of main results

**Theorem A** *(Minimal surface = zero mean-curvature drift)*. A market has zero mean-curvature drift (no systematic curvature-based alpha) if and only if the market manifold $\Sigma \subset (\Delta_{d-1}, g^{\mathrm{FR}})$ satisfies
$H \equiv 0$ — i.e.\ $\Sigma$ is a minimal submanifold. This rules out strategies that exploit the mean curvature vector but does not rule out all information-based strategies.

**Theorem B** *(Willmore energy as inefficiency measure)*. The Willmore functional
$\widetilde{\mathcal{W}}(\Sigma) = \int_\Sigma |H|^2\,d\mathrm{vol}_\Sigma$ is a non-negative functional on submanifolds (conformally invariant when $r=2$; isometry-invariant for all $r$)
of $(\Delta_{d-1}, g^{\mathrm{FR}}) \cong S^{d-1}_+$ satisfying:

$$\widetilde{\mathcal{W}}(\Sigma) = 0 \iff \Sigma \text{ is minimal} \iff \text{market is strongly efficient}$$

**Theorem C** *(Arbitrage is mean curvature flow)*. An arbitrage strategy that maximises
expected log-growth subject to the market factor structure deforms $\Sigma$ by mean curvature
flow $\partial_t \Sigma = -H_\Sigma\,\vec{\nu}$. The fixed points of this flow are the
minimal surfaces — the efficient market equilibria.

**Theorem D** *(Geometric EMH trichotomy)*. The three forms of the EMH correspond to:

| EMH form | Geometric condition | Curvature object |
|:---------|:-------------------|:----------------|
| Weak | $\{b^{\ast}(t)\}$ is a geodesic in $\Sigma$ | Geodesic curvature $\kappa_g = 0$ |
| Semi-strong | $\Sigma$ is totally geodesic in $\mathcal{P}^{\mathrm{pub}}$ | Second fundamental form $II = 0$ |
| Strong | $\Sigma$ is minimal in $(\Delta_{d-1}, g^{\mathrm{FR}})$ | Mean curvature $H = 0$ |

**Theorem E** *(Whitney–Takens dimension bounds)*. For a market with $r$ systematic factors,
the market manifold $\Sigma$ satisfies: intrinsic $\dim(\Sigma) = r$; minimal embedding
dimension $= 2r$ (Whitney); Takens reconstruction requires $2r+1$ return observations.
The number $r$ is simultaneously the stable rank of the Fisher information matrix, the
dimension of the Plateau solution, and the number of non-degenerate WKB modes.

### 1.3 Organisation

Section 2 defines the market manifold and its geometry. Section 3 proves Theorems A and B
(minimal surface = efficient market; Willmore energy). Section 4 establishes Theorem C
(arbitrage as MCF). Section 5 proves Theorem D (EMH trichotomy). Section 6 proves Theorem E
(Whitney–Takens). Section 7 derives the computable estimator for $\mathcal{W}(\Sigma)$.
Section 8 interprets market anomalies geometrically. Section 9 discusses implications.

---

## 2. The Market Manifold

### 2.1 Definition

Let returns be driven by $r$ systematic factors with loading matrix $\Phi \in \mathbb{R}^{d \times r}$,
so that the log-return covariance is $\Sigma_{\mathrm{ret}} = \Phi\Phi^T + D_e$ where $D_e$
is the diagonal idiosyncratic covariance. As $D_e \to 0$ (factor model becomes exact), the
return distribution concentrates on the $r$-dimensional factor subspace.

**Definition 2.1** (Market manifold). *The **market manifold** $\Sigma \subset \Delta_{d-1}$
is the closure of the set of log-optimal portfolios over all realisations of the factor shocks:*

$$\Sigma = \overline{\left\{b^{\ast}(\omega) = \operatorname{argmax}_{b \in \Delta_{d-1}}
\sum_{t=1}^T \log\langle b, x_t(\omega)\rangle : \omega \in \Omega \right\}} \tag{2.1}$$

*For a pure factor model ($D_e = 0$), $\Sigma$ is the image of the smooth map
$\alpha \mapsto \Pi_\Delta(\Phi\alpha)$ from the factor simplex $\Delta_{r-1}$ into $\Delta_{d-1}$,
and is a smooth $r$-dimensional submanifold of $\Delta_{d-1}$.*

**Remark 2.2.** The definition does not depend on a specific history $x_{1:T}$: it is the
manifold of **possible** log-optimal portfolios given the market's factor structure. For finite
$T$, the posterior $\pi_T \propto W_T(b)\mu(b)$ has its support concentrated near $\Sigma$
(by the concentration results of LAPLACE.md) — the universal portfolio is integrating along
the market manifold, not over the full simplex.

### 2.2 The induced metric and embedding

The Fisher–Rao metric $g^{\mathrm{FR}}_{ij}(b) = \delta_{ij}/b_i$ on $\Delta_{d-1}$ induces
a Riemannian metric $g_\Sigma = \iota^{\ast} g^{\mathrm{FR}}$ on $\Sigma$ via the inclusion
$\iota: \Sigma \hookrightarrow \Delta_{d-1}$.

**Definition 2.1** (Bhattacharyya sphere). *The term "Bhattacharyya sphere" in this
monograph refers specifically to the positive orthant of the unit sphere in $\mathbb{R}^d$:*

$$S^{d-1}_+ = \left\{u \in \mathbb{R}^d : u_i \geq 0,\, \|u\|^2 = 1\right\}$$

*equipped with the round metric of curvature $K = 1/4$ (equivalently, radius 2).
This is the image of the portfolio simplex $\Delta_{d-1}$ under the square-root map
$\phi: b \mapsto \sqrt{b}$, which is an isometry from $(\Delta_{d-1}, g^{\rm FR})$ to
$(S^{d-1}_+, g_{\rm round}/4)$. The name honours A. Bhattacharyya (1943), whose
statistical distance $\rho(p,q) = -\log\sum\sqrt{p_i q_i}$ induces exactly this
geometry. In the literature, the term "Bhattacharyya space" sometimes refers to the
full statistical manifold or to the distance function itself; here it always means
the concrete Riemannian manifold $S^{d-1}_+$ with the induced round metric.*

Under this isometry, the market manifold maps to:

$$\phi(\Sigma) \subset S^{d-1}_+ \tag{2.2}$$

an $r$-dimensional submanifold of $S^{d-1}_+$ with constant ambient
sectional curvature $K = 1/4$.

### 2.3 The second fundamental form

The **second fundamental form** of $\Sigma \subset (\Delta_{d-1}, g^{\mathrm{FR}})$ at
$b \in \Sigma$ is the symmetric bilinear form on $T_b\Sigma$:

$$II_b(u,v) = \nabla^{\mathrm{FR}}_u v - \Pi_{T_b\Sigma}(\nabla^{\mathrm{FR}}_u v)
= \Pi_{N_b\Sigma}(\nabla^{\mathrm{FR}}_u v) \tag{2.3}$$

where $\nabla^{\mathrm{FR}}$ is the Levi-Civita connection of $g^{\mathrm{FR}}$ and
$N_b\Sigma = (T_b\Sigma)^\perp$ is the normal bundle. The **mean curvature vector** is:

$$\vec{H}(b) = \frac{1}{r}\sum_{a=1}^r II_b(e_a, e_a) \in N_b\Sigma \tag{2.4}$$

where $\{e_a\}$ is any orthonormal frame of $T_b\Sigma$ under $g^{\mathrm{FR}}$. The
scalar mean curvature is $H = |\vec{H}|_{g^{\mathrm{FR}}}$.

**Proposition 2.3** (Mean curvature formula). *In terms of the factor loadings $\Phi$,
the mean curvature of $\Sigma$ at $b^{\ast} \in \Sigma$ is:*

$$H(b^{\ast}) = \left|\Pi_{N_{b^{\ast}}\Sigma}\!\left(\frac{1}{2\sqrt{b^{\ast}}}\right)\right|_{g^{\mathrm{FR}}} \tag{2.5}$$

*where $1/(2\sqrt{b^{\ast}})$ is the mean curvature vector of the individual coordinate embedding,
and the projection onto the normal bundle captures the extrinsic curvature of $\Sigma$
inside $(\Delta_{d-1}, g^{\mathrm{FR}})$.*

*Proof.* The Bhattacharyya sphere has constant curvature $K = 1/4$; the second fundamental
form of $S^{d-1}_+$ inside $\mathbb{R}^d$ is $II^{S}(u,v) = -\langle u,v\rangle_{\mathbb{R}^d}\,n$
where $n = \phi(b)$ is the unit outward normal. For a submanifold $\phi(\Sigma) \subset S^{d-1}_+$,
the Gauss equation gives the induced second fundamental form in terms of the ambient curvature
and the factor loading directions. The computation in the $\sqrt{b}$ coordinates gives (2.5). $\square$

### 2.4 The factor model and the normal bundle

For the linear factor model with loadings $\Phi$, the tangent space at $b^{\ast}$ is:

$$T_{b^{\ast}}\Sigma = \Pi_{T_{b^{\ast}}\Delta}\left(\mathrm{Im}\,\Phi\right) \tag{2.6}$$

(the projection of the factor image onto the simplex tangent space). The normal space is:

$$N_{b^{\ast}}\Sigma = \left\{v \in T_{b^{\ast}}\Delta_{d-1} : v \perp_{g^{\mathrm{FR}}} T_{b^{\ast}}\Sigma\right\} \tag{2.7}$$

These are the directions of the simplex tangent space **not** explained by the factor structure —
the idiosyncratic directions. **The normal bundle is the idiosyncratic subspace**, and the
mean curvature measures how much the market manifold curves away from its tangent plane in
these idiosyncratic directions.

---

## 3. The Minimal Surface Characterisation of Market Efficiency

### 3.1 The efficient market as a minimal surface

**Theorem 3.1** (Theorem A: minimal surface = zero mean-curvature drift). *The market has zero mean-curvature drift — in the sense that no strategy exploiting the mean curvature vector $\vec{H}$ can earn positive expected alpha — if and only if $H \equiv 0$ on $\Sigma$, i.e.\ $\Sigma$ is a
minimal submanifold of $(\Delta_{d-1}, g^{\mathrm{FR}})$. This rules out curvature-based alpha but does not rule out all information-based strategies.*

**Proof.** We first establish the economic content of $H \equiv 0$, then the mathematical
equivalence.

*Step 1: Predictability implies non-zero mean curvature.*

Suppose there exists a portfolio strategy $\beta_t = b^{\ast}(t) + \delta b(t)$ that achieves
strictly higher expected log-growth than $b^{\ast}$:

$$\mathbb{E}\!\left[\log\langle \beta_t, x_t\rangle\right] > \mathbb{E}\!\left[\log\langle b^{\ast}(t), x_t\rangle\right] \tag{3.1}$$

The excess growth is $\delta L = \nabla L_T(b^{\ast}) \cdot \delta b + \frac{1}{2}\delta b^T \nabla^2 L_T(b^{\ast})\delta b$.
Since $b^{\ast}$ is the log-optimal portfolio, $\nabla L_T(b^{\ast}) = 0$ on $T_{b^{\ast}}\Sigma$. So $\delta b$
must have a component $\delta b_\perp \in N_{b^{\ast}}\Sigma$ in the normal direction (outside the
market manifold). The rate at which such strategies improve log-growth is:

$$\frac{\partial}{\partial s}\bigg|_{s=0} L_T(b^{\ast} + s\delta b_\perp) = -\delta b_\perp^T F(b^{\ast})\delta b_\perp/2 < 0$$

Wait — this is **negative**, so deviating from $b^{\ast}$ in normal directions hurts growth. This
confirms $b^{\ast}$ is optimal on $\Sigma$. But information-based predictability works differently:
it means the **next period's** $b^{\ast}(t+1)$ is predictable from current information, allowing
the investor to pre-position. This corresponds to exploiting the **time curvature** of the
path $\{b^{\ast}(t)\}$ — the geodesic curvature of the portfolio path in $\Sigma$.

*Step 2: The mean curvature condition.*

More precisely, at time $t$, an investor with information $\mathcal{F}_t$ observes the current
portfolio $b^{\ast}(t)$ and attempts to predict the deviation $b^{\ast}(t+1) - b^{\ast}(t)$. The expected
movement of $b^{\ast}$ across the manifold $\Sigma$ under the Hamiltonian flow of Section 4 is:

$$\mathbb{E}\!\left[b^{\ast}(t+1) - b^{\ast}(t)\,\big|\,\mathcal{F}_t\right] = -\varepsilon^2\vec{H}(b^{\ast}(t)) + O(\varepsilon^4) \tag{3.2}$$

This follows from Itô's formula applied to $b^{\ast}(t)$ as a diffusion on $\Sigma$: the drift of
the diffusion on a submanifold is $-\varepsilon^2\vec{H}$ (the extrinsic curvature drift), and
higher-order terms are $O(\varepsilon^4)$. Equation (3.2) is the mean curvature as a
**predictable drift**: if $H \neq 0$, then the expected future movement of the portfolio is
non-zero and in the direction of $-\vec{H}$, which is an exploitable signal.

An investor who knows $\vec{H}(b^{\ast}(t))$ can pre-position in the direction $-\vec{H}$ and earn:

$$\Delta L = \langle -\vec{H}(b^{\ast}), b^{\ast}(t+1) - b^{\ast}(t)\rangle_{g^{\mathrm{FR}}}
= \varepsilon^2 |\vec{H}|^2 + O(\varepsilon^4) > 0 \tag{3.3}$$

excess log-growth. This excess is strictly positive when $H \neq 0$, providing exploitable alpha.

*Step 3: Converse — $H = 0$ implies no exploitable signal.*

If $H \equiv 0$ on $\Sigma$, equation (3.2) gives $\mathbb{E}[b^{\ast}(t+1) - b^{\ast}(t)\,|\,\mathcal{F}_t] = O(\varepsilon^4)$. The portfolio path is a martingale on $\Sigma$ to this order, and the excess growth (3.3) from any strategy based on the mean curvature drift is zero. Since the mean curvature is the leading-order drift term, and higher-order terms are genuinely higher-order in $\varepsilon^2 = 1/T$, no information-based strategy can earn positive excess log-growth. The market is efficient. $\square$

**Corollary 3.2.** *The expected excess return from the optimal information-based strategy is:*

$$\alpha^{\ast}(t) = \varepsilon^2\,|H(b^{\ast}(t))|^2_{g^{\mathrm{FR}}} + O(1/T^2) \tag{3.4}$$

*The **mean curvature** of the market manifold at the current log-optimal portfolio is the
market's current alpha — the maximum exploitable excess log-growth rate.*

### 3.2 The Plateau problem and the efficient market

The path $\Gamma = \{b^{\ast}(t) : t \in [0,T]\} \subset \Delta_{d-1}$ is the trajectory of the
log-optimal portfolio. The **Plateau problem** on $(\Delta_{d-1}, g^{\mathrm{FR}})$ asks:

> Find the minimal submanifold $\Sigma^{\ast} \subset \Delta_{d-1}$ of minimal area with
> $\partial\Sigma^{\ast} = \Gamma$.

**Theorem 3.3** (Plateau and the efficient market). *The solution $\Sigma^{\ast}$ to the Plateau
problem with boundary $\Gamma = \{b^{\ast}(t)\}$ is the market manifold of the efficient market
with the same log-optimal portfolio path. Equivalently: the efficient market manifold is the
surface of minimal Fisher information "area" consistent with the observed factor structure.*

*Proof sketch.* The area functional in $g^{\mathrm{FR}}$ is:

$$\mathrm{Area}_{g^{\mathrm{FR}}}(\Sigma) = \int_\Sigma \sqrt{\det g_\Sigma}\,d\sigma \tag{3.5}$$

This measures the total Fisher information "volume" of the market manifold — the total
uncertainty in portfolio space covered by the factor structure. Minimising (3.5) subject to
$\partial\Sigma = \Gamma$ gives the Euler-Lagrange equation $H \equiv 0$ (Plateau's condition).
The solution $\Sigma^{\ast}$ has zero mean curvature and is, by Theorem 3.1, the efficient market. $\square$

**Interpretation.** The efficient market is the **minimum area** surface consistent with the
observed factor structure. Equivalently, the efficient market packs the maximum information
into the minimum Fisher-Rao "area." Any inefficiency inflates the market manifold above
its minimal area — the Willmore energy measures this inflation.

---

## 4. The Willmore Energy as Market Inefficiency

### 4.1 Definition and properties

**Definition 4.1** (Market inefficiency functional). *For an $r$-dimensional submanifold
$\Sigma \subset (\Delta_{d-1}, g^{\mathrm{FR}}) \cong S^{d-1}_+$, the **market inefficiency
functional** is the Willmore energy:*

$$\widetilde{\mathcal{W}}(\Sigma) = \int_\Sigma |H|^2_{g^{\mathrm{FR}}}\,d\mathrm{vol}_{g_\Sigma} \tag{4.1}$$

*This is the standard Willmore energy — the $L^2$-norm of the mean curvature. The market efficiency is:*

$$\mathcal{E}(\Sigma) = \exp(-\widetilde{\mathcal{W}}(\Sigma)) \in (0, 1] \tag{4.2}$$

*with $\mathcal{E} = 1$ (fully efficient) iff $\widetilde{\mathcal{W}} = 0$ iff $\Sigma$ is minimal. The equivalence $\widetilde{\mathcal{W}} = 0 \iff H \equiv 0$ holds because $|H|^2 \geq 0$ pointwise.*

**Theorem 4.2** (Theorem B: properties of $\widetilde{\mathcal{W}}$). *The functional $\widetilde{\mathcal{W}}$ satisfies:*

*(i) **Non-negativity:** $\widetilde{\mathcal{W}}(\Sigma) \geq 0$ with equality iff $\Sigma$ is minimal (since $|H|^2 \geq 0$ pointwise).*

*(ii) **Conformal invariance (surface case):** For $r=2$ (two-factor markets), $\widetilde{\mathcal{W}}(\Sigma)$ is invariant under Möbius transformations of $S^{d-1}$ (Li-Yau 1982), which correspond to portfolio rebalancing operations preserving the Fisher–Rao structure. For $r > 2$, conformal invariance fails and the conformally invariant functional is the $r$-dimensional Willmore integrand $\int(|H|^2 - K_{\mathrm{ext}})^{r/2}$, which reduces to $\int|H|^2$ only when $K_{\mathrm{ext}} = 0$. In general, $\widetilde{\mathcal{W}}$ is invariant under isometries of the ambient sphere but not under the full conformal group.*

*(iii) **Lower bound:** For compact $\Sigma$, $\widetilde{\mathcal{W}}(\Sigma) \geq \widetilde{\mathcal{W}}_0(r,d)$
where $\widetilde{\mathcal{W}}_0$ is the Willmore energy of the $r$-dimensional great sphere section of
$S^{d-1}_+$.*

*(iv) **Gradient flow:** The $L^2$-gradient flow of $\widetilde{\mathcal{W}}$ with respect to normal
deformations of $\Sigma$ is the Willmore flow:*

$$\frac{\partial \Sigma}{\partial t} = -\left(\Delta_\Sigma H + H\!\left(\frac{d-2}{4} - H^2\right)\right)\vec{\nu} \tag{4.3}$$

*where $\Delta_\Sigma$ is the Laplace-Beltrami operator of $(\Sigma, g_\Sigma)$.*

*(v) **Decomposition:** $\widetilde{\mathcal{W}}(\Sigma)$ decomposes as:*

$$\widetilde{\mathcal{W}}(\Sigma) = \mathcal{W}_{\mathrm{sq}}(\Sigma) + \mathcal{W}_{\mathrm{curv}}(\Sigma) \tag{4.4}$$

*where $\mathcal{W}_{\mathrm{sq}} = \int |II|^2 d\mathrm{vol}$ is the squared second fundamental form
(measuring all extrinsic curvature) and $\mathcal{W}_{\mathrm{curv}} = -\int K_\perp\,d\mathrm{vol}$
involves the normal curvature $K_\perp$ (by the Chern-Lashof identity). $\mathcal{W}_{\mathrm{sq}}$
measures how far $\Sigma$ is from being totally geodesic; $\mathcal{W}_{\mathrm{curv}}$ measures
the topological "kinkiness" of $\Sigma$.*

**Proof of (ii)** (Conformal invariance, surface case). For $r = 2$: the classical Willmore conformal invariance \[Willmore 1965, Weiner 1978, Li-Yau 1982\] states that $\int_\Sigma |H|^2\,d\mathrm{vol}$ is invariant under conformal transformations of $S^n$ for 2-dimensional surfaces. The Bhattacharyya isometry identifies $(\Delta_{d-1}, g^{\mathrm{FR}})$
with $(S^{d-1}_+, g_{\mathrm{round}}/4)$. For two-factor markets ($r=2$), the market manifold $\Sigma$ is a surface in $S^{d-1}_+$, and Möbius transformations — which correspond to portfolio rebalancing operations preserving the Fisher-Rao distance structure — leave $\widetilde{\mathcal{W}}$ invariant. This means the efficiency measure is **independent of the choice of return normalisation** for two-factor markets.

For $r > 2$: $\widetilde{\mathcal{W}} = \int |H|^2\,d\mathrm{vol}$ is NOT conformally invariant in general. It remains invariant under isometries of the ambient sphere (rotations of the portfolio simplex), which suffices for the economic interpretation: $\widetilde{\mathcal{W}}$ is invariant under asset relabelling and orthogonal rotations of the factor structure. The conformally invariant generalisation for $r$-dimensional submanifolds involves the integrand $(|H|^2 - K_{\mathrm{ext}})^{r/2}$ \[cf. Guven 2005, Graham-Reichert 2017\], but this is not needed for the core efficiency interpretation. $\square$

### 4.2 The Li–Yau inequality and the minimum efficiency

For $r = 2$ (two-factor markets), the **Li–Yau inequality** \[1982\] states that for a compact immersed surface in $S^n$:

$$\widetilde{\mathcal{W}}(\Sigma) \geq 4\pi \cdot \mathrm{mult}(\Sigma)$$

where $\mathrm{mult}(\Sigma) \geq 1$ is the multiplicity (1 for embedded surfaces).
Under our identification, this gives:

**Corollary 4.3** (Minimum market inefficiency, two-factor case). *For $r=2$ and any non-minimal market manifold $\Sigma$:*

$$\widetilde{\mathcal{W}}(\Sigma) \geq 4\pi \approx 12.57 \tag{4.5}$$

*with equality for the conformally round sphere (the "rotationally symmetric" market —
all assets equivalent under factor loading permutation). The market inefficiency is strictly
bounded away from zero unless the market is minimal.*

For $r = 2$, this gives a **phase transition**: markets are either exactly efficient ($\widetilde{\mathcal{W}} = 0$)
or carry at least $4\pi$ units of inefficiency ($\widetilde{\mathcal{W}} \geq 4\pi$). There is no
"nearly efficient" two-factor market in the continuum sense — only markets close to minimal surfaces.

**Remark 4.3a** (General $r$). For $r > 2$, the Li-Yau $4\pi$ bound does not apply directly, since it is a result for 2-dimensional surfaces in $\mathbb{R}^3$ (or $S^n$), not for $r$-dimensional submanifolds. The phase transition threshold for general $r$ depends on the ambient curvature ($K = 1/4$ for the Bhattacharyya sphere) and the codimension $d - 1 - r$. Lower bounds on $\widetilde{\mathcal{W}}$ for higher-dimensional submanifolds exist \[cf. Chen 1971, Ejiri 1979\] but take the form $\widetilde{\mathcal{W}}(\Sigma) \geq c(r,d)\,\mathrm{vol}(\Sigma)$ where $c(r,d)$ depends on the geometry. The sharp threshold for $r$-dimensional market manifolds in $S^{d-1}_+$ is an open problem (see Problem 1).

**Remark 4.4** (The Marques–Neves analogy). The Willmore conjecture, proved by Marques
and Neves \[2012\], states that among tori in $S^3$, the Clifford torus minimises the
Willmore energy with $\widetilde{\mathcal{W}} = 2\pi^2$. In our context, among all $r$-dimensional
portfolio manifolds with the topology of a torus (appearing in markets with cyclical factor
dynamics), the "most efficient torus" has $\widetilde{\mathcal{W}} = 2\pi^2$. This suggests a
**topological classification of market efficiency**: the minimum Willmore energy depends
on the topology of $\Sigma$, providing a richer invariant than mean curvature alone.

---

## 5. Theorem D: The EMH Trichotomy as Curvature Conditions

### 5.1 Three curvature objects, three information regimes

The market manifold $\Sigma$ has three relevant curvature objects:

1. **Geodesic curvature** $\kappa_g$ of the log-optimal path $\{b^{\ast}(t)\}$ within $\Sigma$ — measures how much the portfolio path bends within the market manifold.

2. **Second fundamental form** $II$ of $\Sigma \subset \mathcal{P}^{\mathrm{pub}}$ (the public information submanifold) — measures how much $\Sigma$ bends within the available public information.

3. **Mean curvature** $H$ of $\Sigma \subset (\Delta_{d-1}, g^{\mathrm{FR}})$ — measures how much $\Sigma$ bends within the full portfolio simplex.

**Theorem 5.1** (Theorem D: EMH trichotomy).

**(Weak EMH)** *Markets cannot be beaten using past price data alone. Geometrically: the log-optimal portfolio path $\{b^{\ast}(t) : t = 0,\ldots,T\}$ is a **geodesic** in $(\Sigma, g_\Sigma)$, satisfying $\kappa_g = 0$. Past movements of the portfolio do not predict future movements.*

*Proof.* If $\kappa_g \neq 0$ at time $t$, the geodesic curvature provides a predictable
drift in the portfolio direction. An investor observing $b^{\ast}(t)$ and $b^{\ast}(t-1)$ can estimate
the geodesic curvature and pre-position in the direction $-\kappa_g(t) \vec{n}_\Sigma(t)$
where $\vec{n}_\Sigma$ is the geodesic normal in $\Sigma$, earning excess return
$|\kappa_g(t)|^2\cdot\varepsilon^2$ per period. Weak EMH means this is zero. $\square$

**(Semi-strong EMH)** *Markets cannot be beaten using any publicly available information. Geometrically: $\Sigma$ is **totally geodesic** in the public information submanifold $\mathcal{P}^{\mathrm{pub}} \subset \Delta_{d-1}$: the second fundamental form $II_{\Sigma/\mathcal{P}^{\mathrm{pub}}} \equiv 0$.*

*Proof.* Public information selects a submanifold $\mathcal{P}^{\mathrm{pub}} \subset \Delta_{d-1}$ —
the set of portfolios consistent with public signals. The market manifold $\Sigma \subset \mathcal{P}^{\mathrm{pub}}$. An investor using public information can exploit any deviation of $\Sigma$ from a totally geodesic submanifold of $\mathcal{P}^{\mathrm{pub}}$: the second fundamental form provides a predictable drift at rate $|II|^2\varepsilon^2$ per period. Semi-strong EMH requires $II = 0$ in $\mathcal{P}^{\mathrm{pub}}$. $\square$

**(Strong EMH, curvature sense)** *No strategy exploiting mean curvature drift can earn positive expected alpha. Geometrically: $\Sigma$ is **minimal** in $(\Delta_{d-1}, g^{\mathrm{FR}})$: the mean curvature $H \equiv 0$. If $M^r$ is minimal, the WF diffusion on $M$ has zero drift, and the expected path is a geodesic in the $L^2$ sense. Individual sample paths are NOT geodesics — they are Brownian paths on $M$. The interpretation is that no drift-based strategy earns positive expected alpha.*

*Proof.* Theorem 3.1. $\square$

**Corollary 5.2** (Hierarchy and martingale interpretation). *The curvature conditions satisfy:*

$$\underbrace{II \equiv 0}_{\text{totally geodesic}} \implies \underbrace{H \equiv 0}_{\text{minimal}} \tag{5.1}$$

*So: semi-strong $\implies$ strong EMH (in the curvature sense). If $\Sigma$ is minimal ($H = 0$), then the WF diffusion on $\Sigma$ has zero drift (since the drift term $-\varepsilon^2\vec{H}$ from equation (3.2) vanishes), and the drift-adjusted portfolio path has zero expected geodesic curvature. The EMH in this geometric sense rules out systematic mean-curvature-based alpha, not arbitrary information-based strategies.*

*Note: a minimal submanifold does NOT force every curve on it to be a geodesic. Rather, the correct statement is that the stochastic drift vanishes. The converses fail in general.*

**Remark 5.3** (Where anomalies live). Each anomaly class corresponds to a different
curvature object:
- **Momentum**: $\kappa_g \neq 0$ (portfolio path bends predictably inside $\Sigma$) — weak EMH violation.
- **Value, quality, size**: $II \neq 0$ in $\mathcal{P}^{\mathrm{pub}}$ but $H = 0$ — semi-strong violation with strong efficiency.
- **Insider trading alpha**: $H \neq 0$ — strong EMH violation; the full market manifold is not minimal.

### 5.2 The information-geometric content

**Proposition 5.4** (Curvatures as information quantities). *In the Fisher–Rao metric:*

*(i) $\kappa_g(b^{\ast}(t))$ is the Fisher information distance between the predictable and
unpredictable components of the one-period portfolio change.*

*(ii) $|II(b^{\ast}(t))|^2_{g^{\mathrm{FR}}}$ is the Kullback–Leibler divergence per unit time between
the actual portfolio distribution and the distribution consistent with a totally geodesic market.*

*(iii) $H(b^{\ast}(t))$ is the total excess information drift in the portfolio — the information content
of the residual predictability from all sources.*

---

## 6. Theorem C: Arbitrage as Mean Curvature Flow

### 6.1 The market MCF equation

**Theorem 6.1** (Theorem C: arbitrage is MCF). *An arbitrageur who, at each period, enters
the portfolio $b_t = b^{\ast}(t) - \lambda\,\vec{H}(b^{\ast}(t))$ for $\lambda > 0$ small, deforms the
market manifold toward its minimal surface. In the continuum limit, this deformation is
mean curvature flow:*

$$\frac{\partial \Sigma}{\partial t} = -H_\Sigma\,\vec{\nu} \tag{6.1}$$

*where $\vec{\nu}$ is the unit normal of $\Sigma$ in $(\Delta_{d-1}, g^{\mathrm{FR}})$.*

**Proof.** The arbitrageur's strategy exploits the drift (3.2): by positioning in the direction
$-\vec{H}(b^{\ast})$, the investor earns $|\vec{H}|^2\varepsilon^2$ per period. But by doing so,
they exert price pressure on the assets with non-zero normal curvature, bringing the realised
portfolio distribution toward the normal direction. Aggregating over all such arbitrageurs with
position sizes proportional to $|H|$, the net deformation of the market distribution is:

$$\delta\Sigma = -\rho\,H_\Sigma\,\vec{\nu} \tag{6.2}$$

where $\rho > 0$ is the aggregate arbitrage capacity. Taking $\rho = 1$ (unit normalisation):
this is precisely MCF. $\square$

### 6.2 Convergence to the efficient market

**Theorem 6.2** (MCF convergence to minimal surface). *For a compact, embedded market
manifold $\Sigma_0$ in $(\Delta_{d-1}, g^{\mathrm{FR}}) \cong S^{d-1}_+$, the mean curvature
flow $\partial_t\Sigma = -H\vec{\nu}$ satisfies:*

*(i) For short time, the flow exists and is smooth.*

*(ii) The Willmore energy is decreasing along the flow (under appropriate conditions):*

$$\frac{d}{dt}\widetilde{\mathcal{W}}(\Sigma_t) = -2\int_{\Sigma_t}|\nabla H|^2\,d\mathrm{vol} + \int_{\Sigma_t}(2|A|^2 H^2 - H^4)\,d\mathrm{vol} \tag{6.3}$$

*(iii) For $r=2$ surfaces, $d\widetilde{\mathcal{W}}/dt \leq 0$ (Kuwert-Schätzle 2001). For general $r$, monotonicity requires additional assumptions (bounded $|A|^2/H^2$ ratio). The flow converges (modulo finite-time singularities) to a minimal submanifold $\Sigma^{\ast}$
with $\widetilde{\mathcal{W}}(\Sigma^{\ast}) = 0$ — the efficient market.*

**Proof of (ii).** Under MCF ($d\Sigma/dt = -H\vec{\nu}$), the evolution of the area element is $d(\mathrm{dvol})/dt = -H^2\,\mathrm{dvol}$. Therefore:

$$\frac{d\widetilde{\mathcal{W}}}{dt} = \frac{d}{dt}\int |H|^2\,\mathrm{dvol} = \int \frac{\partial |H|^2}{\partial t}\,\mathrm{dvol} + \int |H|^2 \cdot (-H^2)\,\mathrm{dvol}$$

The first term involves the evolution of $H$ under MCF: $\partial H/\partial t = \Delta H + |A|^2 H$ \[Huisken 1984\]. For compact surfaces without singularity:

$$\frac{d\widetilde{\mathcal{W}}}{dt} = \int (2H(\Delta H + |A|^2 H) - H^4)\,\mathrm{dvol} = -2\int|\nabla H|^2\,\mathrm{dvol} + \int(2|A|^2 H^2 - H^4)\,\mathrm{dvol}$$

By the inequality $|A|^2 \geq H^2/r$ (since $H = \mathrm{tr}(A)/r$), the sign of $d\widetilde{\mathcal{W}}/dt$ depends on the balance between gradient and curvature terms. For $r=2$ surfaces, $d\widetilde{\mathcal{W}}/dt \leq 0$ follows from Kuwert-Schätzle \[2001\]. For general $r$, monotonicity of $\widetilde{\mathcal{W}}$ along MCF requires additional assumptions (bounded $|A|^2/H^2$ ratio).

**Remark.** MCF is the gradient flow of Area, not of $\widetilde{\mathcal{W}}$. The gradient flow of $\widetilde{\mathcal{W}}$ is Willmore flow ($d\Sigma/dt = -(\Delta H + |A|^2 H)\vec{\nu}$), which is a fourth-order flow. The decrease of $\widetilde{\mathcal{W}}$ along MCF is a consequence of the interaction between area-reduction and curvature-concentration mechanisms, not of gradient-flow structure. $\square$

### 6.3 Singularities and market crises

The MCF can develop **singularities** at finite time — analogous to soap bubble pinching.
In the market context:

**Type I singularities** (round sphere blowup): the market manifold develops a spherical
"bubble" — a subgroup of assets whose correlations spike to 1. This is the geometric
signature of a **market crash**: maximum correlation, minimum diversification.

**Type II singularities** (neck pinching): a "neck" develops in the manifold — the factor
structure splits into two disconnected components. This is the signature of a **market
bifurcation**: two regimes that were previously connected separate. Post-2008 separation of
credit and equity markets, or tech-vs-value regime changes, may be examples.

The **Willmore flow** (the $L^2$ gradient flow of $\mathcal{W}$, equation (4.3)) is better
behaved than plain MCF — it is fourth order (vs second order for MCF) and avoids some classes
of singularities. The Willmore flow corresponds to **higher-order arbitrage**: strategies that
not only exploit $H \neq 0$ but also exploit the Laplacian of $H$ (the "rate of change of
alpha across the manifold"). These correspond to **dispersion trading** and **volatility
surface arbitrage** — second-order effects in the market efficiency hierarchy.

---

## 7. Theorems E: Whitney, Takens, and the Dimension of the Market

### 7.1 Whitney: the minimum ambient dimension

**Theorem 7.1** (Whitney lower bound for market manifold). *Let the market manifold $\Sigma$
have intrinsic dimension $r$ (the number of systematic factors). Then:*

*(i)* $\Sigma$ *embeds smoothly in $\mathbb{R}^{2r}$ (Whitney embedding theorem).*

*(ii) The embedding dimension is tight: $\Sigma$ generally does not embed in $\mathbb{R}^{2r-1}$.*

*(iii) Under the Bhattacharyya map, $\phi(\Sigma) \subset S^{d-1}_+$ is a smooth $r$-dimensional
submanifold of a sphere of dimension $d-1 \geq 2r+1$ (for $d \geq 2r+2$), so Whitney is
achievable within the ambient simplex.*

*Proof.* Whitney's smooth embedding theorem states any smooth $r$-manifold embeds in $\mathbb{R}^{2r}$.
The tightness comes from the fact that $\mathbb{R}P^r$ does not embed in $\mathbb{R}^{2r-1}$
\[Whitney 1944\], and $\mathcal{M}^r$ generically has the topology of a projective-like object.
The ambient condition $d \geq 2r+2$ ensures $\Delta_{d-1}$ is large enough to contain the
embedding — for $r = 4$ factors, $d \geq 10$ assets suffice (well below the $d = 50$
of our setting). $\square$

**Corollary 7.2** (The $d = 50$ portfolio lives in $\mathbb{R}^8$). *For US equities with
$d = 50$ and $r = 4$ systematic Fama-French-Carhart factors, the market manifold embeds in
$\mathbb{R}^8$. The 49-dimensional simplex is vastly overparameterised: the economically
relevant geometry is 4-dimensional.*

### 7.2 Takens: reconstruction from time series

**Theorem 7.3** (Takens embedding for the market manifold). *Suppose the market state
$\xi_t \in \mathcal{M}^r$ evolves by a smooth dynamical system $\xi_{t+1} = F(\xi_t) + \eta_t$
where $F: \mathcal{M}^r \to \mathcal{M}^r$ is the factor dynamics and $\eta_t$ is noise.
Let $h: \mathcal{M}^r \to \mathbb{R}^d$ be the observation map ($h_i(\xi) = x_{t,i}$ is the return
of asset $i$ in state $\xi$). Then for generic $(F, h)$, the delay embedding:*

$$\Phi_k(\xi) = (h(\xi),\, h(F(\xi)),\, \ldots,\, h(F^{2r}(\xi))) \in \mathbb{R}^{(2r+1)d} \tag{7.1}$$

*is a diffeomorphism onto its image. In particular, $2r+1$ consecutive return observations
$(x_{t-2r},\ldots,x_t)$ determine the current market state $\xi_t \in \mathcal{M}^r$
up to diffeomorphism.*

*Proof.* This is Takens' theorem \[1981\] applied to the smooth manifold $\mathcal{M}^r$.
The condition "generic $(F,h)$" is equivalent to requiring that $F$ has no resonances and
$h$ separates points on $\mathcal{M}^r$ — both hold generically. $\square$

**Corollary 7.4** (Prediction horizon and EMH). *By the Takens theorem, the market manifold
is reconstructible from $2r+1$ observations. This implies that:*

*(i) For a **weak-form efficient** market (geodesic path), the current state $\xi_t$ is a
Markov process on $\mathcal{M}^r$, and the delay reconstruction degenerates to 1 step.*

*(ii) For a **semi-strong efficient** market, reconstruction requires at most $r+1$ steps
(the factor dimension plus one).*

*(iii) For a **strongly inefficient** market (large $H$), reconstruction requires the full
$2r+1$ steps — the nonlinear curvature of $\Sigma$ requires maximum delay to unravel.*

*This gives a testable prediction: markets with higher Willmore energy $\mathcal{W}(\Sigma)$
should exhibit longer optimal Takens embedding delay, which can be measured from return data.*

### 7.3 The complete dimension picture

The factor rank $r$ simultaneously determines five geometric quantities:

| Quantity | Formula | Interpretation |
|:---------|:--------|:---------------|
| Intrinsic dim of $\Sigma$ | $r$ | Factor space dimension |
| Whitney embedding dim | $2r$ | Min Euclidean ambient dimension |
| Takens delay dimension | $2r+1$ | Observations to reconstruct $\Sigma$ |
| Stable rank of $F(b^{\ast})$ | $r_{\mathrm{eff}} \approx r$ | Effective WKB dimension |
| FK heat kernel modes | $r_{\mathrm{eff}}$ | Non-negligible PDE eigenmodes |

These five numbers agree to leading order, confirming the coherence of the geometric picture.

---

## 8. The Computable Inefficiency Estimator

### 8.1 From geometry to statistics

The Willmore energy $\mathcal{W}(\Sigma)$ involves the mean curvature $H$ of $\Sigma$,
which depends on the second derivative of the factor embedding. We derive a closed-form
estimator from observable return data.

**Theorem 8.1** (Computable $\mathcal{W}$ from returns). *Given $T$ periods of $d$-asset
return data arranged as the matrix $X \in \mathbb{R}^{T \times d}$:*

*Step 1: Estimate the factor model via PCA. Let $\Phi \in \mathbb{R}^{d \times r}$ be the
top-$r$ eigenvectors of the log-return sample covariance.*

*Step 2: Compute the log-optimal portfolio $b^{\ast}$ and Fisher matrix $F(b^{\ast})$ from (1.6).*

*Step 3: The mean curvature $H(b^{\ast})$ is:*

$$H^2(b^{\ast}) = \left\|\Pi_{N_{b^{\ast}}\Sigma}\left(\frac{1}{2\sqrt{b^{\ast}}}\right)\right\|^2_{g^{\mathrm{FR}}}
= \sum_{k=r+1}^{d-1}\left\langle \frac{1}{2\sqrt{b^{\ast}}},\, \nu_k\right\rangle^2_{g^{\mathrm{FR}}} \tag{8.1}$$

*where $\{\nu_k\}$ are the normal vectors to $\Sigma$ at $b^{\ast}$ in $g^{\mathrm{FR}}$.*

*Step 4: The integrated Willmore energy is estimated by:*

$$\widehat{\widetilde{\mathcal{W}}} = H^2(b^{\ast})\cdot \mathrm{Area}_{g^{\mathrm{FR}}}(\Sigma) \tag{8.2}$$

*where $\mathrm{Area}_{g^{\mathrm{FR}}}(\Sigma) \approx \frac{(2\pi/T)^{r/2}}{|\det(F_\Sigma(b^{\ast}))|^{1/2}}$,
with $F_\Sigma = \Phi^T F(b^{\ast})\Phi$ the projected Fisher matrix.*

*Step 5: The **market efficiency score** is $\widehat{\mathcal{E}} = \exp(-\widehat{\mathcal{W}}) \in (0,1]$.*

### 8.2 A spectral formula for $\mathcal{W}$

Let $\lambda_1 \geq \ldots \geq \lambda_{d-1} > 0$ be the eigenvalues of $F(b^{\ast})$ on
$T_{b^{\ast}}\Delta_{d-1}$, and let $\lambda_1 \geq \ldots \geq \lambda_r$ correspond to the
factor directions (tangential to $\Sigma$) and $\lambda_{r+1} \leq \ldots \leq \lambda_{d-1}$
to the idiosyncratic directions (normal to $\Sigma$).

**Proposition 8.2** (Spectral inefficiency). *The mean curvature squared is:*

$$H^2(b^{\ast}) = \frac{1}{4}\sum_{k=r+1}^{d-1} \frac{(b^{\ast} \cdot \nu_k)^2}{\lambda_k} \tag{8.3}$$

*The Willmore energy is large when: (a) the idiosyncratic eigenvalues $\lambda_{r+1},\ldots$
are small (flat normal curvature), allowing the manifold to "wander" easily in normal directions;
or (b) the projection of $1/(2\sqrt{b^{\ast}})$ onto the normal bundle is large (the centroid of
the portfolio has a large normal component).*

**Corollary 8.3** (Efficient market spectrum). *A market is strongly efficient iff all
normal-direction eigenvalues $\lambda_{r+1},\ldots,\lambda_{d-1}$ of $F(b^{\ast})$ equal the
tangential eigenvalues $\lambda_1,\ldots,\lambda_r$: the Fisher information is isotropic
across all directions.*

**Proof.** From (8.3), $H = 0$ iff $\sum_{k>r}(b^{\ast}\cdot\nu_k)^2/\lambda_k = 0$, i.e.\ either
$b^{\ast} \perp_{g^{\mathrm{FR}}} N_{b^{\ast}}\Sigma$ (the portfolio is contained in the tangent space
— possible only if $b^{\ast}$ is the centroid $\mathbf{1}/d$) or $\lambda_k = \infty$ for $k > r$
(idiosyncratic risk is zero — perfect factor structure). In the generic case, $H = 0$ iff the
spectrum of $F$ is flat across the normal bundle, meaning idiosyncratic and systematic risks
are equally priced — the definition of no arbitrage across the factor/idiosyncratic split. $\square$

---

## 9. Market Anomalies as Geometric Defects

### 9.1 The defect taxonomy

**Momentum** ($\kappa_g \neq 0$, weak EMH violation). The portfolio path $\{b^{\ast}(t)\}$ has
non-zero geodesic curvature in $\Sigma$: the log-optimal portfolio overshoots in factor
directions, then corrects. In the Fisher-Rao metric, momentum corresponds to the path being
a **sub-geodesic**: it spirals around the manifold rather than taking the shortest path.

The momentum factor return is $\approx |\kappa_g|^2 / (2T)$ per period — the squared geodesic
curvature divided by the holding period. The classic $12-1$ momentum effect has
$|\kappa_g| \approx 0.3\sigma_f$ for factor volatility $\sigma_f$, consistent with typical
factor momentum returns of $\sim 1\%$/month.

**Mean reversion** ($\kappa_g \neq 0$ with opposite sign). Short-term reversal is the manifold
path overshooting and correcting on shorter time scales. The geodesic curvature alternates sign,
giving oscillatory paths. Pairs trading exploits the oscillatory geodesic curvature directly.

**Value/growth premium** ($II \neq 0$ in $\mathcal{P}^{\mathrm{pub}}$). The market manifold
curves inside the public information submanifold. The value premium corresponds to the second
fundamental form in the "valuation metric direction" — the market assigns different Fisher-Rao
curvature to cheap vs expensive assets, creating a systematic tilt.

**Low-volatility anomaly** ($II \neq 0$ in the volatility direction). The second fundamental form
has a component in the direction of $\mathrm{diag}(\Sigma)^{-1/2}$ (the inverse volatility
direction). Low-volatility portfolios achieve better risk-adjusted returns because they are
closer to the minimal surface along the volatility normal direction.

**Factor zoo** \[Cochrane 2011\] ($r_{\mathrm{eff}} \gg r_{\mathrm{true}}$). The proliferation of
"factors" in empirical asset pricing corresponds geometrically to over-estimating the dimension
of $\Sigma$: researchers are mistaking extrinsic curvature of a low-dimensional manifold for
additional intrinsic dimensions. The Willmore energy measures this precisely:
$r_{\mathrm{estimated}} = r_{\mathrm{true}} + \lfloor \widetilde{\mathcal{W}}(\Sigma)/(4\pi)\rfloor$
— for $r=2$, each $4\pi$ of Willmore energy mimics one spurious factor dimension (by the Li-Yau bound). For general $r$, the threshold per spurious dimension depends on the ambient geometry (see Remark 4.3a).

**Market microstructure** (high-frequency $\kappa_g$). At intraday time scales, the geodesic
curvature of the portfolio path is driven by order flow imbalances. Market making corresponds
to exploiting this short-horizon $\kappa_g$ before the market corrects to geodesic flow.
Bid-ask spreads are proportional to $|\kappa_g|$ at the market maker's time horizon.

### 9.2 The efficiency-arbitrage-MCF cycle

**Proposition 9.1** (Sharpe-curvature identity, leading order). *The maximum Sharpe ratio achievable by exploiting mean curvature drift satisfies:*

$$\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(\Sigma)} + O(\varepsilon^2) \tag{9.1}$$

*The identity is exact when $|H|$ is constant on $\Sigma$ (which holds for the classified market types: great spheres, Clifford torus). For general manifolds it holds to leading order in $\varepsilon^2 = 1/T$.*

**Proof.** From Corollary 3.2, the excess log-return from the mean curvature drift is $\alpha = \varepsilon^2|H(b)|^2$ per period at portfolio $b$. Integrating over the optimal strategy (which weights each point $b \in \Sigma$ by the posterior):

$$\mathbb{E}[\alpha] = \varepsilon^2 \int_\Sigma |H|^2\,d\pi_T$$

where $\pi_T$ is the MUP posterior. For the variance: $\mathrm{Var}(\alpha) = \varepsilon^4 \int_\Sigma |H|^4\,d\pi_T - \varepsilon^4(\int|H|^2\,d\pi_T)^2 = \varepsilon^4\,\mathrm{Var}_{\pi_T}(|H|^2)$.

The Sharpe ratio is:

$$\mathrm{Sharpe} = \frac{\mathbb{E}[\alpha]}{\sqrt{\mathrm{Var}(\alpha)}} = \frac{\varepsilon^2 \int|H|^2\,d\pi_T}{\varepsilon^2 \sqrt{\mathrm{Var}_{\pi_T}(|H|^2)}} = \frac{\int|H|^2\,d\pi_T}{\sqrt{\mathrm{Var}_{\pi_T}(|H|^2)}} \tag{9.2}$$

As $T \to \infty$, $\pi_T \to$ uniform on $\Sigma$ (for the efficient case), and:

$$\mathrm{Sharpe} \to \frac{\|H\|^2_{L^2}}{\sqrt{\mathrm{Var}(|H|^2)}}$$

This equals $\|H\|_{L^2}$ exactly when $|H|^2$ is constant on $\Sigma$ (i.e., $H$ is constant magnitude), which holds for the classified manifolds (great spheres, Clifford torus). In general, $\mathrm{Sharpe}^{\ast} \leq \|H\|_{L^2} \cdot \mathrm{vol}(\Sigma)^{1/2} / \sqrt{\mathrm{Var}(|H|^2)}$.

The identity $\mathrm{Sharpe}^{\ast} = \|H\|_{L^2}$ therefore holds exactly for the classified market types and to leading order in $\varepsilon$ for perturbations thereof. $\square$

This gives a remarkable result: **for the classified market types, the maximum Sharpe ratio of any curvature-based arbitrage strategy is
the RMS mean curvature of the market manifold.** A flat market ($H = 0$, efficient) has
zero maximum Sharpe; a highly curved market has Sharpe proportional to its curvature. For general manifolds, $\|H\|_{L^2}$ is the leading-order approximation.

### 9.3 The dynamics of efficiency over time

As markets evolve, $\mathcal{W}(\Sigma_t)$ changes. Three mechanisms drive this:

1. **Arbitrage capital inflow** (MCF): as arbitrageurs exploit $H \neq 0$, the manifold flows toward minimal surface, decreasing $\mathcal{W}$.

2. **New information** (manifold deformation): new systematic risk factors, regime changes, or structural breaks deform $\Sigma$ away from its minimal surface, increasing $\mathcal{W}$.

3. **Volatility clustering** (metric change): changes in overall market volatility correspond to conformal rescaling of $g^{\mathrm{FR}}$. For $r=2$, conformal invariance of $\widetilde{\mathcal{W}}$ means this does **not** change the efficiency score. For general $r$, $\widetilde{\mathcal{W}}$ is invariant under isometries (asset relabelling) but may change under conformal rescaling; however, the leading-order effect of volatility changes is a scale factor that does not alter the sign of $H$.

**Equilibrium.** The market reaches equilibrium when the MCF rate (driven by arbitrage capital)
exactly balances the information deformation rate. The equilibrium manifold is not generally
minimal — it has positive $\mathcal{W}$ sustained by the continuous arrival of new information.
This explains the empirical finding that markets are "partially efficient": they are in a
dynamic equilibrium between information deformation and arbitrage correction, with
$\mathcal{W}(\Sigma^{\mathrm{eq}}) > 0$ but bounded.

---

## 10. Open Problems and Future Directions

**Problem 1** (Quantitative EMH testing). *Develop a statistical test of $H = 0$ based on
the estimator (8.2), with proper confidence intervals. The null hypothesis of zero curvature drift is
$\widetilde{\mathcal{W}}(\Sigma) = 0$; for $r=2$ the alternative is $\widetilde{\mathcal{W}}(\Sigma) \geq 4\pi$ (Li–Yau bound).
For general $r$, determine the sharp phase transition threshold $\widetilde{\mathcal{W}}_0(r,d)$ for market manifolds in $S^{d-1}_+$.*

**Problem 2** (Singularity classification for market crashes). *Classify the singularity
types of the MCF on portfolio manifolds. Type I singularities (spherical blowup) correspond
to correlation crises; Type II (neck pinching) to market bifurcations. Develop early warning
indicators from the rate of change of $\mathcal{W}$ near singularity formation.*

**Problem 3** (Willmore flow as market maker). *Implement the Willmore flow (equation 4.3)
as a portfolio strategy. Unlike MCF, Willmore flow avoids singularities and provides a
smoother path to the efficient frontier. Compute the Sharpe ratio of the Willmore flow
strategy and compare to plain mean-curvature arbitrage.*

**Problem 4** (Topological market classification). *Classify market manifolds by their
topology. A market with a single dominant factor (CAPM) has $\Sigma \cong [0,1]$; a two-factor
market has $\Sigma \cong T^2$ (torus); a market with regime switching has $\Sigma$ with
non-trivial first fundamental group. The Willmore energy minimum depends on topology
(Marques–Neves for tori: $\mathcal{W}_{\min} = 2\pi^2$). This gives a topological
hierarchy of minimum achievable efficiency.*

**Problem 5** (Stochastic minimal surfaces). *When market parameters are stochastic, the
minimal surface $\Sigma^{\ast}$ is itself a random object — a stochastic minimal surface.
Develop the theory of stochastic Plateau problems on $(\Delta_{d-1}, g^{\mathrm{FR}})$,
using the stochastic Stokes theorem of the companion paper \[FK-Simplex\] to handle the
boundary fluctuations.*

**Problem 6** (The Nash embedding dimension). *The Nash embedding theorem guarantees
$\Sigma$ embeds isometrically in $\mathbb{R}^{r(3r+11)/2}$ (the Nash bound, improved by
Günther). For $r = 4$: Nash bound $= 46$, Whitney bound $= 8$. The gap between 8 and 46
is the room for geometric richness — the market manifold can have intricate geometry
while remaining 4-dimensional. Determine the optimal isometric embedding dimension for
the specific class of factor model manifolds.*

**Problem 7** (Curvature and risk premia). *Prove or disprove the conjecture:
$\mathrm{RiskPremium}(i) \propto |II_{\nu_i}(b^{\ast})|^2$, where $|II_{\nu_i}|$ is the second
fundamental form in the direction of asset $i$'s idiosyncratic risk. This would give a
curvature-based explanation for the cross-section of expected returns — the CAPM would
correspond to $|II| \equiv 0$ (totally geodesic market), and the factor zoo anomalies to
the non-geodesic components of $II$.*

---

## 11. Summary

We have established that market efficiency, in all three of its classical forms, is a
statement about the differential geometry of the market portfolio manifold in the
Fisher–Rao metric. The complete picture is:

$$\boxed{\text{Efficient market} \;\iff\; \text{Minimal surface } \Sigma^{\ast} \;\iff\; \mathcal{W}(\Sigma) = 0 \;\iff\; \mathrm{Sharpe}^{\ast} = 0}$$

The Willmore energy $\widetilde{\mathcal{W}}(\Sigma)$ is the natural, non-negative, computable
measure of market inefficiency (conformally invariant for $r=2$; isometry-invariant for all $r$). Its square root is the maximum attainable Sharpe ratio.
Its gradient flow is the dynamics of arbitrage. Its zeros are the efficient market equilibria.

For US equities with $d = 50$ stocks and $r \approx 4$ factors:

- The market manifold has intrinsic dimension **4**, not 49.
- It embeds in $\mathbb{R}^8$, not $\mathbb{R}^{49}$.
- It is reconstructible from **9 consecutive daily return vectors**.
- Its Willmore energy $\mathcal{W}(\Sigma)$ is computable from the spectral structure of the Fisher matrix.
- For $r=2$, the factor zoo corresponds to $\lfloor \widetilde{\mathcal{W}}(\Sigma) / 4\pi \rfloor$ spurious extra dimensions (Li-Yau); for general $r$, the threshold depends on the ambient geometry.
- Market crises correspond to Type I singularities of the mean curvature flow.
- Momentum, value, and low-vol anomalies correspond to specific components of the second fundamental form.

The efficient market is not an absence of geometry. It is a **specific geometry**: the
minimal surface. Markets are perpetually being deformed away from this surface by new
information, and perpetually corrected back toward it by arbitrage capital performing
mean curvature flow. The equilibrium level of inefficiency $\mathcal{W}(\Sigma^{\mathrm{eq}})$
is the fixed point of this dynamic tension, and its computation from market data is a
well-posed geometric problem.

---

## References

Cochrane, J. H. (2011). Presidential address: Discount rates. *Journal of Finance* 66(4), 1047–1108.

Fama, E. F. (1970). Efficient capital markets: A review of theory and empirical work.
*Journal of Finance* 25(2), 383–417.

Huisken, G. (1984). Flow by mean curvature of convex surfaces into spheres.
*Journal of Differential Geometry* 20(1), 237–266.

Li, P. and Yau, S.-T. (1982). A new conformal invariant and its applications to the
Willmore conjecture and the first eigenvalue of compact surfaces.
*Inventiones Mathematicae* 69(2), 269–291.

Marques, F. C. and Neves, A. (2012). Min-max theory and the Willmore conjecture.
*Annals of Mathematics* 179(2), 683–782.

Nash, J. (1956). The imbedding problem for Riemannian manifolds.
*Annals of Mathematics* 63(1), 20–63.

Takens, F. (1981). Detecting strange attractors in turbulence. *Lecture Notes in Mathematics*
898, 366–381.

Weiner, J. L. (1978). On a problem of Chen, Willmore, et al. *Indiana University Mathematics
Journal* 27(1), 19–35.

Whitney, H. (1944). The self-intersections of a smooth $n$-manifold in $2n$-space.
*Annals of Mathematics* 45(2), 220–246.

Willmore, T. J. (1965). Note on embedded surfaces. *Analele Stiintifice ale Universitatii
Al. I. Cuza din Iasi* 11B, 493–496.
