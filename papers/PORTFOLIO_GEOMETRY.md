# Portfolio Construction on Minimal Market Manifolds:
## What Different Efficient Structures Mean for the Investor

**Saxon Nicholls** — me@saxonnicholls.com

---

**Abstract.**  
The classification of efficient market structures as minimal submanifolds of
the Bhattacharyya sphere (CLASSIFICATION.md) has direct, concrete implications
for portfolio construction that go beyond the Markowitz–CAPM paradigm. Different
minimal surfaces correspond to qualitatively different optimal portfolio strategies,
rebalancing rules, and risk decompositions. We work through four distinct portfolio
construction frameworks arising from the four main minimal surface types: (i) the
**great sphere (CAPM)** gives two-fund separation with a single rebalancing trigger;
(ii) the **Clifford torus** gives four-fund separation with orthogonal within-group
and between-group rebalancing, and an explicit group-balance threshold; (iii) the
**Veronese surface** gives a three-fund rule with a cyclic symmetry constraint;
(iv) the **Lawson surfaces** $\tau\_{m,n}$ give $mn+1$-fund separation with
period-$m$ and period-$n$ rebalancing cycles. In each case, the **rebalancing rule
is the geodesic flow on the minimal surface**, the **risk budget is the Fisher–Rao
ball**, and the **alpha signal is the mean curvature drift** $-\vec{H}(b^*)$.
We also derive: the optimal rebalancing frequency from the Jacobi spectral gap;
the minimum turnover portfolio consistent with staying within $\varepsilon$ of the
efficient manifold; and a **manifold-aware Black–Litterman** framework where investor
views are incorporated as perturbations of the minimal surface and the posterior
portfolio is the geodesic from $b^*$ in the direction of the view.

**Keywords.** Portfolio construction; minimal surface; rebalancing; two-fund
separation; Clifford torus; Lawson surfaces; Black-Litterman; turnover; geodesic
flow; rebalancing frequency; risk budget.

---

## 1. The Core Principle: Rebalancing as Geodesic Flow

### 1.1 Why standard rebalancing is wrong

Standard portfolio rebalancing rules (calendar rebalancing, threshold rebalancing)
are defined in Euclidean portfolio space — they trigger when $|b\_t - b^*|\_{\rm Euclidean}$
exceeds a threshold. This is geometrically incorrect: the natural distance on the
portfolio simplex is the Fisher–Rao distance $d\_{g^{\rm FR}}(b\_t, b^*)$, not the
Euclidean distance.

**The consequences of using the wrong metric:**
- Over-trading in low-weight assets (Fisher-Rao magnifies movements near $b\_i \to 0$)
- Under-trading in dominant positions (Fisher-Rao compresses movements near $b\_i \to 1$)
- Ignoring the curvature of the market manifold when choosing the rebalancing direction

**The correct rule:** Rebalance when $d\_{g^{\rm FR}}(b\_t, b^*)$ exceeds a threshold
$\delta$, and rebalance by following the **geodesic on $M$** from $b\_t$ toward $b^*$.

### 1.2 The optimal rebalancing frequency

**Theorem 1.1** *(Optimal rebalancing frequency from the Jacobi gap)*. *For a
market near a minimal surface $M^*$ with first Jacobi eigenvalue $\lambda\_1$, the
optimal rebalancing frequency is:*

$$f^* = \frac{\lambda_1}{\log(1/\varepsilon_{\rm tol})} \tag{1.1}$$

*rebalances per unit time, where $\varepsilon\_{\rm tol}$ is the tolerance on the
deviation from $M^*$. This is the frequency at which the geometric drift from
the manifold curvature (which grows at rate $\lambda\_1$) is corrected before it
accumulates beyond tolerance.*

*For the CAPM ($\lambda\_1 = (d-2)/4 = 12$ for $d=50$) and $\varepsilon\_{\rm tol} = 0.01$:
$f^* = 12/\log(100) \approx 2.6$ rebalances per day — continuous rebalancing is
approximately optimal.*

*For the Clifford torus ($\lambda\_1 = 5/2$ for $d=4$, slowest mode):
$f^* = 2.5/\log(100) \approx 0.54$ rebalances per day — rebalance roughly every two days.*

---

## 2. Great Sphere (CAPM): Two-Fund Separation

### 2.1 The portfolio rule

For the great $r$-sphere minimal surface in $S^{d-1}\_+$ (the CAPM universality class):

- **Factor subspace:** $M = \{b = \Pi\_\Delta(V\_r\alpha) : \alpha \in \mathbb{R}^r\_+\}$
- **Geodesics on $M$:** straight lines in the factor space $\alpha \in \Delta\_{r-1}$
- **Optimal portfolio:** $b^* = \Pi\_\Delta(V\_r\alpha^*)$ for $\alpha^* = \arg\max\_{\alpha \in \Delta\_{r-1}} L\_T(\Pi\_\Delta(V\_r\alpha))$

**Two-fund separation (general $r$):** Any portfolio on the great sphere is a
convex combination of $r+1$ "pure factor portfolios" $\{f\_0, f\_1, \ldots, f\_r\}$
where $f\_k = \Pi\_\Delta(V\_r e\_k)$. The $r=1$ case is the classical two-fund
(risk-free + market portfolio); $r=4$ gives five-fund separation (Fama-French).

**Portfolio construction rule (CAPM class):**
1. Estimate $V\_r$ from PCA of the return covariance.
2. Solve $\alpha^* = \arg\max L\_T(V\_r\alpha)$ — an $r$-dimensional convex program.
3. Hold $b^* = \Pi\_\Delta(V\_r\alpha^*)$.
4. Rebalance when $\|b\_t - b^*\|\_{F(b^*)} > \delta$ (Fisher-Rao threshold).
5. Rebalance direction: geodesic on $M$ — proportionally adjust $\alpha\_t$ toward $\alpha^*$.

**Minimum turnover:** For a portfolio drifting from $b^*$ due to price changes:

$$\mathrm{Turnover} = \|\dot{b}_t\|_{g^{\rm FR}} = |F(b^*)^{-1/2}\Sigma b^*\,r_t| \tag{2.1}$$

where $r\_t$ is the period return vector. This is the **geodesic speed** on $M$ — the rate
at which the portfolio moves in Fisher-Rao distance due to market returns. The minimum
turnover to stay on $M$ is zero (on the great sphere, buy-and-hold is a geodesic if
returns are proportional across assets). **The CAPM portfolio requires zero rebalancing
if all assets have the same return** — an exact statement of the result that the
market-cap weighted portfolio is buy-and-hold optimal in the CAPM.

---

## 3. Clifford Torus: Four-Fund Separation and Group Rebalancing

### 3.1 The structure

The Clifford torus market ($d=4$, $r=2$, Section 8.2 of MINIMAL\_SURFACE):
- Group 1: assets $\{1,2\}$ with aggregate weight $p = b\_1+b\_2$
- Group 2: assets $\{3,4\}$ with aggregate weight $1-p$
- The Clifford manifold: $p = 1/2$, $\theta = \arctan(b\_2/b\_1)$, $\varphi = \arctan(b\_4/b\_3)$

**Four-fund separation:** Any portfolio on the Clifford torus is determined by:
1. Between-group balance: $p = 1/2$ (fixed on the efficient surface)
2. Within-group-1 allocation: $\theta \in [0,\pi/2]$ (angle in group 1)
3. Within-group-2 allocation: $\varphi \in [0,\pi/2]$ (angle in group 2)

The four "pure portfolios" are: $(1,0,0,0)$, $(0,1,0,0)$, $(0,0,1,0)$, $(0,0,0,1)$.
The Clifford torus portfolio is:

$$b^*(\theta,\varphi) = (\tfrac{1}{2}\cos^2\theta,\; \tfrac{1}{2}\sin^2\theta,\;
\tfrac{1}{2}\cos^2\varphi,\; \tfrac{1}{2}\sin^2\varphi) \tag{3.1}$$

### 3.2 The explicit rebalancing rules

**Rule 1 (Between-group rebalancing — the dominant signal):**

The mean curvature drift at $p \neq 1/2$ is:

$$\dot{p} = -\varepsilon^2 H(p) = -\varepsilon^2\frac{|1-2p|}{4\sqrt{p(1-p)}} \tag{3.2}$$

Rebalancing rule: **whenever $|p - 1/2| > \delta\_p$, trade toward $p = 1/2$ at rate $H(p)$**.
This is the "group-relative value" trade — buy the underweight group, sell the overweight.

**Threshold:** The optimal $\delta\_p$ from (1.1): $\delta\_p = \varepsilon\_{\rm tol}/H'(1/2)$
where $H'(1/2) = \lim\_{p\to 1/2}H(p)/|p-1/2| = 1/2$ (from Example 3 of MINIMAL\_SURFACE).
So $\delta\_p = 2\varepsilon\_{\rm tol}$ — a group imbalance of $2\varepsilon\_{\rm tol}$
triggers rebalancing.

**Rule 2 (Within-group rebalancing — the momentum signal):**

Within group 1, the angle $\theta\_t$ drifts due to relative returns:

$$\dot\theta = \frac{r_{t,1} - r_{t,2}}{2} + \varepsilon^2(\lambda_1\theta + \ldots) \tag{3.3}$$

The mean curvature for within-group drift (mode $(1,0)$ of the Clifford torus Jacobi
spectrum, $\lambda\_{10} = -1/2$ in Bhattacharyya normalisation) creates a predictable
within-group momentum signal:

$$\text{Within-group Sharpe} = |\lambda_{10}|^{1/2}\varepsilon = \frac{1}{\sqrt{2T}} \tag{3.4}$$

This is small ($1/\sqrt{2\times 252} \approx 0.044$) but non-zero — **there is a
systematic within-group momentum signal of Sharpe $\approx 0.04$ per year in a
Clifford torus market that is not at $p=1/2$.**

**Portfolio construction rule (Clifford torus class):**
1. Identify the two asset groups from the factor structure.
2. Monitor $p\_t = b\_t^{(1)}$ (aggregate group-1 weight).
3. When $|p\_t - 1/2| > \delta\_p$: execute group rebalancing trade toward $p=1/2$.
4. Within each group: rebalance by within-group Kelly (log-optimal ratio of pairs).
5. Rebalancing frequency: $f^* \approx 0.54$ per day (every 2 days).

**Key insight:** The Clifford torus gives a **fully explicit quantitative rebalancing
rule** directly from the manifold geometry. The threshold $\delta\_p$ and the frequency
$f^*$ are not free parameters — they are determined by the Jacobi eigenvalues.

---

## 4. The Veronese Surface: Three-Fund Separation with Cyclic Symmetry

### 4.1 Structure

The Veronese surface ($d=5$, $r=2$, Section 5.3 of CLASSIFICATION.md):
Five assets with a cyclic $\mathbb{Z}\_3$ symmetry among three "base exposures"
$(x\_1, x\_2, x\_3)$, with portfolio weights:

$$b_i = v_i^2, \qquad v = \frac{1}{\sqrt{3}}(x_1x_2, x_2x_3, x_3x_1,
\frac{x_1^2-x_2^2}{2}, \frac{x_1^2+x_2^2-2x_3^2}{2\sqrt{3}}) \tag{4.1}$$

**Three-fund separation:** The Veronese portfolio lies in the three-dimensional
space of products $\{x\_ix\_j\}$ — it is a **pure second-harmonic portfolio**, holding
only pairwise factor products. The three "funds" are:
- $f\_1$: long $b\_1 = x\_1x\_2$ (cross of factor 1 and factor 2)
- $f\_2$: long $b\_4 = (x\_1^2-x\_2^2)/2$ (difference of squared factors)
- $f\_3$: the normalisation fund

**Portfolio rule:** Allocate between $f\_1, f\_2, f\_3$ according to the current
realisation of $(x\_1, x\_2, x\_3)$, with the $\mathbb{Z}\_3$ cyclic symmetry ensuring
the allocation is rotation-invariant under cyclic permutation of the three exposures.

**Rebalancing:** Because the Veronese is stable (index 0, CLASSIFICATION Table 5.3),
perturbations decay back to the Veronese automatically. The rebalancing frequency
from (1.1): $f^* = \frac{5/12}{\log(100)} \approx 0.24$ per day — rebalance every
4-5 days.

**Practical relevance:** The Veronese structure appears in markets with three
underlying risk factors where the factors are "mixed" by the assets — e.g.,
equity, bond, and currency exposure in a balanced multi-asset fund, where five
instruments (equity, bond, currency, carry, momentum) represent the five quadratic
products of the three underlying macro factors.

---

## 5. Lawson Surfaces: Multi-Period Rebalancing Cycles

### 5.1 Structure

Lawson surfaces $\tau\_{m,n}$ have genus $g = mn$, corresponding to $mn$ independent
feedback loops between two factor groups. The portfolio parameterisation
(MINIMAL\_SURFACE equation 8.16):

$$b(\theta,\varphi) = (\sin^2\!\rho\cos^2(m\theta),\; \sin^2\!\rho\sin^2(m\theta),\;
\cos^2\!\rho\cos^2(n\varphi),\; \cos^2\!\rho\sin^2(n\varphi)) \tag{5.1}$$

where $\rho = \rho(\theta,\varphi)$ solves a nonlinear ODE coupling the two groups.

**Multi-period rebalancing structure:**

The parameter $\theta$ runs through $m$ cycles as $\varphi$ runs through one cycle.
This means: **Factor 1 rebalances $m$ times for every $n$ rebalances of Factor 2.**
This is a **period-$m/n$ coupling** between the two factor groups.

For $\tau\_{2,1}$ ($m=2$, $n=1$): Factor 1 has a 2-period cycle (mean-reverts over
2 periods) while Factor 2 is single-period. Portfolio construction:
- Each period: rebalance Factor 2 allocation to Kelly-optimal
- Every 2 periods: rebalance Factor 1 allocation to Kelly-optimal
- Trigger: $\tau\_{2,1}$ Jacobi eigenvalue $\lambda\_1 \approx -5/2$ → frequency $f^* \approx 0.54/\text{day}$

**Practical interpretation:** The $\tau\_{2,1}$ market structure corresponds to a
momentum market (Factor 1 trends over 2 periods) coupled to a mean-reversion market
(Factor 2 reverts each period). The rebalancing rule automatically captures:
- **Trend following** in Factor 1 (hold for 2 periods, then rebalance)
- **Mean reversion** in Factor 2 (rebalance every period)

This is the geometric derivation of the empirically observed **momentum-mean reversion
combination** in systematic strategies: it arises naturally from the $\tau\_{2,1}$
Lawson surface structure.

---

## 6. The Manifold-Aware Black–Litterman Framework

### 6.1 Classical Black–Litterman

Black and Litterman \[1992\] combine market equilibrium weights (prior) with investor
views (likelihood) via Bayesian updating:

$$\mu_{\rm BL} = [(\tau\Sigma)^{-1} + P^T\Omega^{-1}P]^{-1}
[(\tau\Sigma)^{-1}\Pi + P^T\Omega^{-1}Q] \tag{6.1}$$

where $\Pi$ is the equilibrium return vector, $P$ is the pick matrix, $Q$ is the
view return vector, and $\Omega$ is the view uncertainty.

The equilibrium prior is the market portfolio $b\_{\rm MKT}$ — the CAPM efficient point.
Views are linear combinations of assets. The result is a "tilted" portfolio.

**Problem:** The Black-Litterman framework is Euclidean — it treats $\Delta\_{d-1}$
as a flat space. The tilted portfolio may not lie on the market manifold $M$ (it may
move off $M$ into the normal bundle), and the uncertainty matrix $\Omega$ is not
informed by the Fisher–Rao geometry.

### 6.2 Manifold Black–Litterman

**Definition 6.1** (Manifold Black–Litterman). *Given the efficient market portfolio
$b^* \in M$ and a view $v \in T\_{b^*}\Delta\_{d-1}$ with confidence $\omega > 0$:*

1. *Decompose the view: $v = v\_M + v\_N$ where $v\_M \in T\_{b^*}M$ (tangential) and $v\_N \in N\_{b^*}M$ (normal).*

2. *The tangential view $v\_M$ moves the portfolio along $M$ to a new point $b^{**}$
   via the geodesic on $(M, g\_M)$:*
   $$b^{**} = \exp_{b^*}^M(\omega\cdot v_M) \tag{6.2}$$

3. *The normal view $v\_N$ moves the portfolio off $M$ by distance $\omega\|v\_N\|\_{g^{\rm FR}}$,
   creating an idiosyncratic tilt with hedging error $\|v\_N\|^2\_{g^{\rm FR}}$.*

4. *The manifold Black-Litterman portfolio:*
   $$b_{\rm MBL} = \Pi_\Delta\left(b^{**} + \frac{\omega}{\omega + 1/T}v_N\right) \tag{6.3}$$

*where $1/T$ is the prior strength (inverse of observation count).*

**Key differences from classical BL:**

| Classical BL | Manifold BL |
|:-------------|:------------|
| Views in Euclidean space | Views decomposed into tangential/normal |
| Prior = market cap weights | Prior = manifold log-optimal $b^*$ |
| Uncertainty = flat covariance | Uncertainty = Fisher–Rao metric |
| No rebalancing structure | Geodesic rebalancing on $M$ |
| No incompleteness accounting | Normal view has unhedgeable error |

**The normal view uncertainty:** A view $v\_N$ in the normal bundle direction creates
a portfolio off $M$ with mean curvature $H \neq 0$. The expected alpha of this
off-manifold position is:

$$\alpha_{\rm view} = \langle v_N, \vec{H}(b^*)\rangle_{g^{\rm FR}} \leq |v_N|_{g^{\rm FR}}\cdot|H| \tag{6.4}$$

(by Cauchy-Schwarz, with equality when the view is aligned with the mean curvature).
**Views aligned with $\vec{H}$ earn maximum alpha per unit of view uncertainty** — the
manifold BL automatically identifies the highest-Sharpe view direction.

### 6.3 Incorporating factor uncertainty

When the market manifold $M$ is estimated from data (PCA + log-optimal solve), there
is estimation uncertainty in $M$ itself. The **manifold estimation uncertainty** is:

$$\Delta M \sim \sqrt{\frac{r(d-r)}{T}} \tag{6.5}$$

(the Fisher information bound on estimating a $r$-dimensional subspace of $\mathbb{R}^d$
from $T$ observations). For $d=50$, $r=4$, $T=252$: $\Delta M \approx \sqrt{4\times 46/252} \approx 0.85$ — substantial uncertainty in the manifold itself.

The **full Manifold Black-Litterman** must account for both portfolio uncertainty (Fisher-Rao
metric) and manifold uncertainty (6.5). The combined posterior is:

$$b_{\rm full-MBL} = \hat{b}_T^M \otimes \hat{M}_T \tag{6.6}$$

the tensor product of the MUP weights and the estimated manifold — a distribution
over both $b$ and $M$ simultaneously.

---

## 7. The Portfolio Construction Cookbook

Collecting the results into actionable rules:

### Step 1: Identify the market structure

From return data $X \in \mathbb{R}^{T\times d}$:
1. Compute $F(b^*) = V\Lambda V^T$ (Fisher matrix at log-optimal).
2. Determine $r = r\_{\rm eff}(F)$ (stable rank).
3. Identify the minimal surface type from the topology of $M$.

**Diagnostic:** The manifold type is determined by:
- $r=1$: CAPM (great circle)
- $r=2$, symmetric: check for $p \approx 1/2$ (Clifford torus) or $\mathbb{Z}\_3$ (Veronese)
- $r=2$, asymmetric period: check for momentum-mean reversion coupling ($\tau\_{2,1}$, $\tau\_{3,1}$, etc.)
- $r \geq 3$: higher Lawson surfaces or CAPM with more factors

### Step 2: Compute the portfolio

| Market type | Portfolio | Dimension of problem |
|:-----------|:----------|:--------------------|
| CAPM ($r=1$) | $b^* = \Pi\_\Delta(\phi\alpha^*)$ | 1D (scalar $\alpha$) |
| Multi-CAPM ($r$ factors) | $b^* = \Pi\_\Delta(V\_r\alpha^*)$ | $r$D |
| Clifford torus | $b^*(\theta^*, \varphi^*)$ | 2D |
| Veronese | $b^* = v^2(\alpha^*)$ | 2D (constrained) |
| $\tau\_{m,n}$ Lawson | $b^*(\theta^*, \varphi^*)$ | 2D (nonlinear ODE) |
| MUP (all cases) | $\hat{b}\_T^M$ from manifold integral | $r$D integral |

### Step 3: Rebalancing rule

For each market type, the rebalancing rule follows the geodesic on $M$:

**Threshold:** $\delta = \varepsilon\_{\rm tol}/\sqrt{\lambda\_1}$ in Fisher-Rao distance
(where $\lambda\_1$ is the first Jacobi eigenvalue of $M$).

**Direction:** Follow the geodesic from current $b\_t$ toward $b^*$ on $M$.

**Frequency:** $f^* = \lambda\_1/\log(1/\varepsilon\_{\rm tol})$ rebalances per period.

### Step 4: Risk attribution

Decompose portfolio risk using the normal bundle:

$$\text{Total risk} = \underbrace{|b_t - b^*|^2_{F_M}}_{\text{factor risk}} + \underbrace{|b_t - b^*|^2_{F_N}}_{\text{idiosyncratic risk}} + \underbrace{H^2\tau}_{\text{alpha risk}} \tag{7.1}$$

where $F\_M = V\_r^TFV\_r$ and $F\_N = V\_N^TFV\_N$ are the factor and idiosyncratic
Fisher matrices.

### Step 5: Alpha generation

The alpha signal is the mean curvature drift $-\vec{H}(b\_t)$:

$$\alpha = -\varepsilon^2\vec{H}(b_t) = -\frac{1}{T}\Pi_{N_{b_t}M}\nabla L_T(b_t) \tag{7.2}$$

This is computable from the Fisher matrix and the log-optimal portfolio.
Maximum Sharpe direction: $\vec{H}/|H|$ (normal to $M$ in the mean curvature direction).

---

## 8. New Results: What We Have Not Seen Before

**Result 8.1** *(Minimum-turnover frontier)*. *For a market manifold $M$ and a target
tracking error $\varepsilon$ (maximum $d\_{g^{\rm FR}}$ deviation from $b^*$), the minimum
turnover portfolio on $M$ solving:*

$$\min_{\tau\geq 0} \|\dot{b}\|_{g^{\rm FR}} \quad \text{s.t.} \quad d_{g^{\rm FR}}(b,b^*) \leq \varepsilon \tag{8.1}$$

*is the portfolio that follows the **unit-speed geodesic** on $M$ — it moves toward $b^*$
at constant Fisher-Rao speed. The minimum turnover is $\varepsilon\cdot\lambda\_1^{1/2}/\sqrt{2}$
(proportional to the square root of the spectral gap).*

**Result 8.2** *(Diversification and manifold dimension)*. *The effective number of bets
(HHI-based diversification) of the log-optimal portfolio on manifold $M^r$ is:*

$$N_{\rm eff}(b^*) = \frac{1}{\sum_i b_i^{*2}} = \frac{1}{|b^*|^2} \geq r+1 \tag{8.2}$$

*with equality when $b^*$ is at the centroid of $M$. The minimum diversification is $r+1$
funds — one per factor plus one "market" fund. You cannot diversify below $r+1$
funds without leaving the market manifold.*

**Result 8.3** *(Geometric Sharpe budget allocation)*. *The total Sharpe budget of the
manifold is:*

$$\mathrm{Sharpe}_{\rm total}^2 = \sum_{k=r+1}^{d-1}\frac{(b^*\cdot\nu_k)^2}{\lambda_k} \tag{8.3}$$

*This decomposes additively across the $d-1-r$ normal directions — each normal direction
contributes an independent Sharpe opportunity. The optimal allocation of the Sharpe budget:
concentrate in the normal direction with smallest $\lambda\_k$ (largest idiosyncratic risk,
hence most underpriced).*

---

## References

Black, F. and Litterman, R. (1992). Global portfolio optimization.
*Financial Analysts Journal* 48(5), 28–43.

*[All other references as per companion papers]*
