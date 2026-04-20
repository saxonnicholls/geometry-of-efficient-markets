# Inflation, Capital Flows, and Multiple Market Manifolds:
## The Geometry of Money, Goods, and Labour

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VI.1** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
The single-market framework of this monograph — one efficient market manifold
$M^r \subset S^{d-1}_{+}$ — extends naturally to an economy with multiple interacting
markets. We identify three fundamental market manifolds: the financial asset manifold
$M^r_{\rm fin}$ (stocks, bonds, currencies), the goods market manifold $M^s_{\rm goods}$
(consumer prices, commodities, real assets), and the labour market manifold
$M^t_{\rm lab}$ (wages, employment). Capital flows between these manifolds are
connections on a fiber bundle; inflation is the curvature of the connection between
the financial and goods manifolds; and the Fisher equation, the quantity theory of
money, and the Taylor rule all emerge as geometric identities in this framework.

**Principal results:**

**(i) Inflation = dual Fisher-Rao norm of the sectoral inflation covector.**
The sectoral inflation rates $\pi^{(i)} = \dot{p}_{i}/p_i$ form a covector on the
goods price simplex $\Delta_{d_g-1}$. The geometric inflation rate is the dual
Fisher-Rao norm: $\pi_t^{\rm geo} = \sqrt{\sum_i w_i(\pi^{(i)})^2}$, where $w_i$
are expenditure shares and the dual metric is $(g^{\rm FR})^{-1}_{ij} = w_i\delta_{ij}$.
This is a non-scalar, directional quantity — "inflation" in sector $i$ is the
component of the covector in direction $e_i$.

**(ii) Capital flow = connection on the financial-goods fiber bundle.**
The combined market space is a fiber bundle $\mathcal{B}$ with base
$M^r_{\rm fin}$ (financial positions) and fiber $M^s_{\rm goods}$ (goods prices).
Capital flows between the two markets define a connection $\nabla^{\rm flow}$ on
$\mathcal{B}$. The curvature of this connection is the inflation tensor —
non-zero curvature means capital flowing into the goods market is changing
relative prices, not just the price level.

**(iii) The Fisher equation is a parallel transport identity.**
The real return $r_{\rm real}$ on the financial manifold is the nominal return
$r_{\rm nom}$ minus the holonomy of $\nabla^{\rm flow}$ around the investment cycle:
$$r_{\rm real} = r_{\rm nom} - \pi_{\rm holonomy}$$
where $\pi_{\rm holonomy}$ is the Berry phase accumulated by a unit of capital
making one round trip through the goods market. For a flat connection
(uniform inflation): $\pi_{\rm holonomy} = \pi\cdot T$ (the standard Fisher equation).
For a curved connection (sector-specific inflation): the holonomy is path-dependent.

**(iv) The quantity theory of money = Gauss's law on $M^r_{\rm fin}$.**
$MV = PQ$ in geometric form: the money supply $M$ is the volume of
$M^r_{\rm fin}$; velocity $V$ is the geodesic flow rate connecting the two manifolds;
$PQ$ is the volume of $M^s_{\rm goods}$ times the goods output. Inflation occurs
when $M^r_{\rm fin}$ expands faster than $M^s_{\rm goods}$.

**(v) The Taylor rule = geodesic steering of the connection curvature.**
The central bank's Taylor rule ($r = r^{\ast} + \alpha(\pi-\pi^{\ast}) + \beta(y-y^{\ast})$)
is a feedback law that steers the curvature of $\nabla^{\rm flow}$ toward zero
— targeting flat connection, minimal inflation holonomy. The Taylor coefficients
$\alpha, \beta$ are the proportional-integral gains of a geometric PID controller
on the fiber bundle.

**Keywords.** Inflation; Fisher equation; quantity theory; Taylor rule; fiber bundle;
O'Neill tensor; connection curvature; holonomy; Fisher-Rao; goods market; capital
flows; monetary policy; multiple manifolds; Berry phase.

---

## 1. The Three Market Manifolds

### 1.1 The financial asset manifold $M^r_{\rm fin}$

This is the market manifold of the existing monograph. Portfolio weights
$b = (b_1,\ldots,b_{d_f})$ on $d_f$ financial assets (equities, bonds, currencies,
commodities) with Fisher-Rao metric $g^{\rm FR}_{ij} = \delta_{ij}/b_i$.

The log-optimal portfolio $b^{\ast}_{\rm fin}$ maximises log-wealth growth.
The efficient financial market manifold $M^r_{\rm fin} \subset S^{d_f-1}_{+}$
has dimension $r$ — the number of independent financial risk factors.

For the US economy: $r \approx 4$–$6$ (equity, rates, credit, FX, commodity, volatility).

### 1.2 The goods market manifold $M^s_{\rm goods}$

**The goods price simplex.** The CPI basket has weights
$w = (w_1,\ldots,w_{d_g})$ with $\sum w_i = 1$, $w_i \geq 0$, where $w_i$ is
the expenditure share on good $i$. This is a point on $\Delta_{d_g-1}$.

The goods market is "efficient" in the sense of competitive markets: the
expenditure weights $w^{\ast}$ minimise the cost of a target utility level — the
**Hicksian demand** problem. In our language: $w^{\ast} = \arg\min_{w\in\Delta_{d_g-1}} C(w,p)$
where $C(w,p) = \sum_i w_i p_i$ is the cost function.

**The goods market manifold $M^s_{\rm goods}$** is the set of optimal expenditure
bundles as prices $p$ vary over the factor structure of the price system
(s independent price factors — energy, food, housing, services, tradables, etc.).

The Fisher-Rao metric on $M^s_{\rm goods}$ gives the **information-theoretic
distance between consumption bundles** — the Bhattacharyya distance between
two expenditure weight vectors $w_1$ and $w_2$:
$$d_{g^{\rm FR}}(w_1, w_2) = 2\arccos\!\sum_i\sqrt{w_{1,i}w_{2,i}} \tag{1.1}$$

### 1.3 The labour market manifold $M^t_{\rm lab}$

The labour market has "portfolio weights" $\ell = (\ell_1,\ldots,\ell_{d_l})$
where $\ell_i$ is the share of total labour employed in sector $i$.
The Fisher-Rao metric on $\Delta_{d_l-1}$ gives the distance between
employment structures.

The efficient labour market manifold $M^t_{\rm lab} \subset S^{d_l-1}_{+}$
has dimension $t$ — the number of independent labour market factors
(skill premium, sectoral demand, geographic mobility, etc.).

**The three manifolds and their dimensions (approximate for the US economy):**

| Market | Manifold | Dimension | Fisher-Rao simplex |
|:-------|:---------|:---------:|:-------------------|
| Financial | $M^r_{\rm fin}$ | $r\approx 5$ | $\Delta_{d_f-1}$, $d_f\approx 5000$ |
| Goods | $M^s_{\rm goods}$ | $s\approx 4$ | $\Delta_{d_g-1}$, $d_g\approx 200$ |
| Labour | $M^t_{\rm lab}$ | $t\approx 3$ | $\Delta_{d_l-1}$, $d_l\approx 800$ |

---

## 2. Inflation as Dual Fisher-Rao Norm

### 2.1 The geometric definition of inflation

**Definition 2.1** (Geometric inflation). *Let $\pi_t^{(i)} = \dot{p}_{i,t}/p_{i,t}$
be the inflation rate of good $i$, and let $w = (w_1,\ldots,w_{d_g})$ be the
expenditure shares. The geometric inflation rate is the dual Fisher-Rao norm of
the sectoral inflation covector $\pi = (\pi^{(1)},\ldots,\pi^{(d_g)})$:*

$$\pi_t^{\rm geo} = |\pi|_{(g^{\rm FR})^{-1}}
= \sqrt{\sum_i w_i \left(\frac{\dot{p}_{i,t}}{p_{i,t}}\right)^2} \tag{2.1}$$

*The Fisher-Rao metric on the goods simplex is $g^{\rm FR}_{ij} = \delta_{ij}/w_i$.
The dual (inverse) metric is $(g^{\rm FR})^{-1}_{ij} = w_i\delta_{ij}$, so the
dual norm of a covector $\alpha$ is $|\alpha|_{(g^{\rm FR})^{-1}} = \sqrt{\sum_i w_i\alpha_i^2}$.
Sectoral inflation rates $\pi^{(i)} = \dot{p}_{i}/p_i$ are naturally covectors
(they act on expenditure shares to give the CPI rate $\sum w_i\pi^{(i)}$),
so the dual metric is the correct one.*

**Remark.** When all prices rise uniformly at rate $\pi_0$ (i.e., $\dot{p}_{i}/p_i = \pi_0$
for all $i$), the geometric rate gives $\pi_t^{\rm geo} = \pi_0\sqrt{\sum w_i} = \pi_0$,
recovering the headline rate. When relative prices change, $\pi_t^{\rm geo}$ captures
both level and compositional effects.

The standard CPI rate $\pi^{\rm CPI}_{t} = \sum_i w_i \dot{p}_{i}/p_i$ is the $L^1$ (weighted
average) norm of sectoral inflation rates. Our measure is the Fisher-Rao ($L^2$) norm.
By Jensen's inequality, $\pi^{\rm geo} \geq |\pi^{\rm CPI}|$ always; equality holds iff
inflation is uniform across sectors.

**An earlier version of this definition** used the Fisher-Rao speed of expenditure
*shares* $w_t$ rather than prices. That formulation fails for uniform inflation:
if all prices rise uniformly, expenditure shares are constant and the speed is zero.
The correct state variable is the vector of sectoral inflation rates, not the
expenditure shares themselves.

**Sectoral inflation.** The geometric inflation decomposes into:
$$\pi_t^{\rm geo} = \sqrt{\sum_s w_s \left(\pi_t^{(s)}\right)^2} \tag{2.2}$$

where $s$ indexes the CPI sub-categories (energy, food, shelter, services, goods).
Each sector contributes independently. **Headline inflation is the dual Fisher-Rao norm
of the sectoral inflation covector.**

### 2.2 The inflation manifold

The inflation state at time $t$ is a pair $(p_t, \dot{p}_{t}/p_t)$ — the vector of
prices and their rates of change. This lives in the **tangent bundle** $TM^s_{\rm goods}$,
not in the goods manifold itself. The **inflation manifold** is a subset of the
unit tangent bundle:

$$\mathcal{I} = \{(p, v) \in TM^s_{\rm goods} : |v|_{g^{\rm FR}} = \pi_{\rm target}\} \tag{2.3}$$

— the set of (price level, inflation velocity) pairs consistent with the central
bank's inflation target. This is a codimension-1 submanifold of $TM^s_{\rm goods}$,
not of $M^s_{\rm goods}$ itself — a crucial distinction, since the inflation target
constrains the *velocity*, not the *position*.

**The central bank's problem** is to steer the economy's trajectory in $TM^s_{\rm goods}$
so that it remains on $\mathcal{I}$ — equivalently, to keep the geometric inflation
rate (2.1) at $\pi_{\rm target}$. This is a velocity-tracking problem on
$M^s_{\rm goods}$, not a position-tracking problem.

---

## 3. Capital Flows as a Connection on the Fiber Bundle

### 3.1 The combined market space

The economy's state is described by a triple
$(b_{\rm fin}, w_{\rm goods}, \ell_{\rm lab}) \in M^r_{\rm fin}\times M^s_{\rm goods}\times M^t_{\rm lab}$.

We focus on the financial-goods pair. Define the **combined market space**:

$$\mathcal{B} = M^r_{\rm fin}\times_{f} M^s_{\rm goods} \tag{3.1}$$

as a fiber bundle with:
- **Base:** $M^r_{\rm fin}$ (the financial market — where capital is allocated)
- **Fiber:** $M^s_{\rm goods}$ (the goods market — where capital is deployed)
- **Projection:** $\pi_{\rm bundle}: \mathcal{B}\to M^r_{\rm fin}$ (maps each goods
  market state to the corresponding financial market state)

### 3.2 The capital flow connection

A **connection** on $\mathcal{B}$ specifies, for each financial market state $b \in M^r_{\rm fin}$
and each tangent direction $v\in T_b M^r_{\rm fin}$, how the goods market state moves:

$$\nabla^{\rm flow}_{v} w = \Gamma^{\rm flow}(b,w)\cdot v \tag{3.2}$$

where $\Gamma^{\rm flow}$ is the **capital flow connection coefficient** — a matrix
encoding how much goods market displacement $dw$ results from a given financial
market displacement $db$.

**The connection one-form** $A^{\rm flow}\in\Omega^1(M^r_{\rm fin}, \mathrm{End}(TM^s_{\rm goods}))$
encodes the capital flow rate between markets:

$$A^{\rm flow}_{ij}(b) = \frac{\partial w_j}{\partial b_i}\bigg|_{\rm equilibrium} \tag{3.3}$$

— how much the goods price weight $w_j$ changes when the financial weight $b_i$ changes.

### 3.3 Inflation = curvature of the capital flow connection

**Theorem 3.1** *(Inflation = contracted connection curvature)*.
*The inflation rate is the contraction of the curvature 2-form with the capital
flow velocity:*

$$\pi_t = |\iota_v F^{\rm flow}_{t}|_{g^{\rm FR}} \tag{3.4}$$

*where $F^{\rm flow} = dA^{\rm flow} + A^{\rm flow}\wedge A^{\rm flow}$ is the curvature
2-form of $\nabla^{\rm flow}$, and $v$ is the capital flow velocity vector.*

*Remark.* The curvature $F^{\rm flow}$ is a 2-form — it takes two tangent vectors
and returns a scalar. The inflation rate is obtained by contracting with the
capital flow velocity $v$ via the interior product $\iota_v$, yielding a 1-form
whose Fisher-Rao norm is the scalar inflation rate. This contraction is essential:
the curvature 2-form itself has no definite sign, but the contracted quantity
$\iota_v F^{\rm flow}$ does — positive in the price-level direction means inflation,
negative means deflation.

*Proof sketch.* The inflation rate measures how much the goods market state changes
relative to what pure financial equilibrium would predict. This excess change — the
failure of the financial and goods markets to move in lockstep — is the curvature
contracted with the flow direction. When $F^{\rm flow}=0$ (flat connection): capital
flows between markets without creating inflation. When $\iota_v F^{\rm flow}\neq 0$:
money is entering the goods market faster than new production absorbs it. $\square$

**Economic interpretation** (in terms of the contracted quantity $\iota_v F^{\rm flow}$):
- **Zero contraction ($\iota_v F^{\rm flow}=0$):** Capital flows freely between financial
  and goods markets without distortion. New money creation is exactly absorbed by new
  goods production. $\pi = 0$ (price stability).
- **Positive contraction ($\iota_v F^{\rm flow}>0$ in the price-level direction):**
  Capital is flowing into the goods market faster than new goods are being produced.
  Excess demand drives prices up. $\pi > 0$ (inflation).
- **Negative contraction ($\iota_v F^{\rm flow}<0$ in the price-level direction):**
  Capital is fleeing the goods market — hoarding, deflation. $\pi < 0$ (deflation).

*Note:* The 2-form $F^{\rm flow}$ itself has no definite sign — it is an antisymmetric
tensor. Only after contraction with the flow velocity $v$ do we obtain a 1-form
whose component in the price-level direction has a meaningful sign.

### 3.4 The O'Neill tensors and their economic meaning

The **O'Neill tensors** $A$ and $T$ of the fiber bundle submersion $\pi_{\rm bundle}$
measure the interaction between the horizontal (financial) and vertical (goods)
directions:

**The O'Neill $A$ tensor:**
$$A_X Y = \Pi_V(\nabla_{\Pi_H X}\Pi_H Y) + \Pi_H(\nabla_{\Pi_H X}\Pi_V Y) \tag{3.5}$$

measures how much horizontal (financial) movements create vertical (goods) movements
and vice versa. **$A$ = the capital flow intensity between markets.**

**The O'Neill $T$ tensor:**
$$T_U V = \Pi_H(\nabla_{\Pi_V U}\Pi_V V) + \Pi_V(\nabla_{\Pi_V U}\Pi_H V) \tag{3.6}$$

measures how goods market curvature affects financial market geometry.
**$T$ = the feedback from goods prices to financial asset prices.**

**The Grey-O'Neill formula** gives the sectional curvature of $\mathcal{B}$:
$$K_{\mathcal{B}}(X,U) = K_{\rm fin}(\Pi_H X) + K_{\rm goods}(\Pi_V U)
+ |A_{X}U|^2 - |T_U X|^2 \tag{3.7}$$

The total curvature of the combined economy is the sum of the curvatures of the
individual markets plus the cross-terms from the O'Neill tensors. **A high-inflation
economy has large $|A_{X}U|^2$ — strong coupling between financial and goods markets.**

---

## 4. The Fisher Equation as Parallel Transport

### 4.1 Parallel transport between markets

The **parallel transport** of a portfolio along the capital flow connection sends
a financial portfolio $b\in M^r_{\rm fin}$ along a path $\gamma$ in the goods
market and returns to the financial market. The accumulated **holonomy** is the
Berry phase from FIBER_BUNDLES.md, now given an economic interpretation:

$$\gamma_{\rm Fisher} = \oint_{\rm cycle}\nabla^{\rm flow} \tag{4.1}$$

**Theorem 4.1** *(Fisher equation = holonomy identity)*.
*The real return on the financial manifold equals the nominal return minus the
holonomy of the capital flow connection around the investment cycle:*

$$r_{\rm real} = r_{\rm nom} - \gamma_{\rm Fisher} \tag{4.2}$$

*For a flat connection (uniform, steady inflation at rate $\pi$):
$\gamma_{\rm Fisher} = \pi\cdot T$ and (4.2) reduces to the standard Fisher equation
$r_{\rm real} = r_{\rm nom} - \pi$.*

*For a curved connection (non-uniform inflation, sector-specific price shocks):
$\gamma_{\rm Fisher}$ is path-dependent — the real return depends on WHICH goods
the investor buys, not just the aggregate inflation rate.*

**The path-dependence of the Fisher equation under inflation heterogeneity:**
An equity investor whose consumption basket is weighted toward energy (large weight
on energy goods sector $w_{\rm energy}$) experiences a different Fisher correction
than a bond investor with equal consumption weights. In geometric terms: two investors
with the same nominal return experience different real returns if their paths through
the goods market manifold have different holonomies.

### 4.2 The Wicksell natural rate as the geodesic curvature

Wicksell's "natural rate of interest" $r^{\ast}$ — the interest rate consistent with
price stability — is geometrically the interest rate at which the curvature of
the capital flow connection is zero:

$$r^{\ast} : F^{\rm flow}(r^{\ast}) = 0 \tag{4.3}$$

The central bank's problem is to find $r^{\ast}$ and set the policy rate equal to it.
When the policy rate $r_{\rm policy} < r^{\ast}$: the connection has positive curvature
(inflationary). When $r_{\rm policy} > r^{\ast}$: negative curvature (deflationary).

**The natural rate is not constant.** It changes as $M^r_{\rm fin}$ and $M^s_{\rm goods}$
evolve — as the factor structure of both markets changes. In RG terms (RENORMALIZATION.md):
the natural rate runs with the energy scale, exactly as the gauge coupling runs in
quantum field theory.

---

## 5. The Quantity Theory as Gauss's Law

### 5.1 The geometric quantity theory

The classical quantity theory $MV = PQ$ is a statement about volumes on the manifolds.

**Interpretation of each term:**

$M$ (money supply) = volume of the financial market manifold:
$$M \propto \mathrm{vol}(M^r_{\rm fin}) = \int_{M^r_{\rm fin}}d\mathrm{vol}_{g^{\rm FR}} \tag{5.1}$$

$V$ (velocity) = the geodesic flow rate of capital between $M^r_{\rm fin}$ and $M^s_{\rm goods}$:
$$V = |\nabla^{\rm flow}|_{g_{\rm combined}} \tag{5.2}$$

$P$ (price level) = the geometric (Törnqvist) price index relative to a base period:
$$P_t = \exp\!\left(\sum_i w_i \log\frac{p_{i,t}}{p_{i,0}}\right) \tag{5.3}$$
This equals 1 at the base period and grows with the weighted geometric average
of price relatives. Unlike a Fisher-Rao distance of expenditure shares, this
correctly registers uniform inflation ($P_t = e^{\pi_0 t}$ when all prices
grow at rate $\pi_0$).

$Q$ (real output) = volume of the goods market manifold:
$$Q \propto \mathrm{vol}(M^s_{\rm goods}) \tag{5.4}$$

**Theorem 5.1** *(Geometric quantity theory = Gauss's law on the fiber bundle)*.
*The quantity theory $MV = PQ$ is the integrated divergence theorem applied to
the capital flow connection:*

$$\int_{M^r_{\rm fin}}\mathrm{div}(\nabla^{\rm flow})\,d\mathrm{vol}_{\rm fin}
= \int_{M^s_{\rm goods}}\pi\,d\mathrm{vol}_{\rm goods} \tag{5.5}$$

*The left side is the total capital outflow from the financial manifold (money creation
times velocity). The right side is the total inflation load on the goods manifold
(price level times real output). Gauss's theorem says they must balance.*

**Monetarism vs Keynesianism in geometric terms:**
- Monetarist view: controlling $\mathrm{vol}(M^r_{\rm fin})$ (the money supply)
  controls inflation. This is true iff the connection is flat — velocity $V$ is constant.
- Keynesian view: velocity $V$ varies (the connection is curved) — controlling
  $M$ alone is insufficient because changes in $V$ offset changes in $M$.
  The curvature of the connection is Keynes' "liquidity trap."

---

## 6. The Taylor Rule as Geodesic Steering

### 6.1 The Taylor rule derived geometrically

The Federal Reserve's Taylor rule:
$$r_{\rm policy} = r^{\ast} + 1.5(\pi - \pi^{\ast}) + 0.5(y - y^{\ast}) \tag{6.1}$$

where $\pi^{\ast}$ is the inflation target, $y-y^{\ast}$ is the output gap.

**Geometric derivation:**

The central bank wants to steer the goods manifold velocity toward $\pi^{\ast}$ and
the financial manifold toward full employment $y^{\ast}$. This is a combined tracking problem
on both manifolds simultaneously — a multi-manifold LQG controller
(STOCHASTIC_CONTROL_KALMAN.md Section 6).

The optimal LQG controller for the combined system steers:
$$\dot{r}_{\rm policy} = -K_\pi(\pi-\pi^{\ast}) - K_y(y-y^{\ast}) \tag{6.2}$$

The Taylor coefficients are the LQG gains:
$$K_\pi = \sqrt{q_\pi/\rho_\pi}, \qquad K_y = \sqrt{q_y/\rho_y} \tag{6.3}$$

where $q_\pi, q_y$ are the inflation and output gap penalties and $\rho_\pi, \rho_y$
are the rate-change costs. **Taylor's empirical coefficients ($K_\pi = 1.5$, $K_y = 0.5$)
are the empirically calibrated LQG gains of the Federal Reserve's geodesic steering controller.**

### 6.2 The Taylor principle as a stability condition

The Taylor principle: $K_\pi > 1$ (the policy rate responds more than one-for-one to inflation).

**Geometric interpretation:** The Taylor principle is the condition that the feedback
gain exceeds the natural instability of the inflation process. In LQG terms:
$K_\pi > 1$ ensures the closed-loop system (economy + central bank) has a
negative real eigenvalue — the inflation state is stable and mean-reverting.

For $K_\pi < 1$: the goods manifold drift exceeds the steering force — inflation
is explosive. **The Taylor principle is the condition that the central bank's LQG
controller is stabilising, i.e., that the closed-loop Jacobi spectral gap is positive.**

---

## 7. Currency Markets and the Third Manifold

### 7.1 International capital flows

When we add multiple economies — the US financial manifold $M^{r_{\rm US}}_{\rm fin}$,
the European manifold $M^{r_{\rm EU}}_{\rm fin}$, etc. — capital flows between economies
are geodesics on the product manifold:

$$M^r_{\rm int} = M^{r_{\rm US}}_{\rm fin}\times M^{r_{\rm EU}}_{\rm fin}\times\cdots \tag{7.1}$$

**The exchange rate** is the Fisher-Rao distance between the US and EU financial manifolds:

$$S_{\rm FX} = d_{g^{\rm FR}}(b^{\ast}_{\rm US}, \Phi(b^{\ast}_{\rm EU})) \tag{7.2}$$

where $\Phi$ is the currency conversion map sending EU portfolio weights to the
same asset space as the US portfolio.

**Uncovered interest parity (UIP)** in geometric terms: the geodesic from $M^r_{\rm fin,US}$
to $M^r_{\rm fin,EU}$ via the FX connection should have zero expected excess return
in equilibrium — the Fisher-Rao distance change equals the interest rate differential.
UIP violations = curvature of the international capital flow connection = the
**carry trade premium** in FX markets.

### 7.2 The carry trade as Berry phase between economies

The carry trade (borrow in low-rate currency, invest in high-rate currency) is a
loop in the international capital flow fiber bundle. The expected return of the
carry trade is the Berry phase accumulated going around this loop:

$$\gamma_{\rm carry} = \oint_{\rm FX\,cycle}\nabla^{\rm int\,flow} \tag{7.3}$$

Under UIP: $\gamma_{\rm carry} = 0$ (flat international connection).
The empirical carry trade premium (Lustig-Verdelhan) is evidence that the
international capital flow connection is curved — non-zero Berry phase.
The curvature is the risk premium for bearing the risk of connection curvature.

---

## 8. The Complete Multi-Market Picture

### 8.1 The three-manifold system

The complete economy is a triple fiber bundle:

```
Labour manifold M^t_lab
        │ wages ↕ employment
        │
Goods manifold M^s_goods ←── inflation connection ──→ Financial manifold M^r_fin
        │                          (∇^flow)                       │
        │  prices ↕ quantities                        capital ↕ returns
        │                                                         │
        └──────────────── output gap ─────────────────────────────┘
```

Each arrow is a connection with curvature:
- Financial → Goods: inflation (curvature = $\pi$)
- Goods → Labour: the Phillips curve (curvature = output gap $\to$ wage pressure)
- Labour → Financial: the equity risk premium (curvature = labour share $\to$ profit margin)

### 8.2 The Phillips curve as inter-manifold coupling

The **Phillips curve** ($\pi = f(y-y^{\ast})$, inflation rises when output exceeds potential)
is the O'Neill $A$-tensor coupling between the goods and labour manifolds:

$$\pi = |A^{\rm goods-lab}(y-y^{\ast})|_{g^{\rm FR}} \tag{8.1}$$

The Phillips curve is not a stable relationship — it shifts when the coupling
structure between the goods and labour manifolds changes. In geometric terms:
the $A$-tensor is not constant — it depends on the curvature of both manifolds.
The "flattening" of the Phillips curve (observed post-2000) is the weakening
of the O'Neill tensor coupling between the labour and goods manifolds — globalisation
and technology have reduced the sensitivity of goods prices to domestic labour conditions.

### 8.3 The inflation puzzle resolved geometrically

**Why did inflation remain low despite massive QE (2008–2020)?**
In our framework: QE expanded $\mathrm{vol}(M^r_{\rm fin})$ (money supply) enormously,
but the capital flow connection became nearly flat at the lower bound — velocity $V$
collapsed (Keynes' liquidity trap = zero curvature of $\nabla^{\rm flow}$). The Gauss
law (5.5) shows: if $V \to 0$, then $MV \to 0$ regardless of $M$. Money was created
but it did not flow through to the goods manifold. The financial manifold expanded
while the goods manifold stayed still.

**Why did inflation surge in 2021–2022?**
The COVID supply shock compressed $\mathrm{vol}(M^s_{\rm goods})$ (real output fell —
the goods manifold shrank). Simultaneously, fiscal stimulus via helicopter money
directly injected capital into the goods manifold (bypassing the financial manifold —
the connection curvature jumped discontinuously). The goods manifold shrank while
money was injected directly onto it. Classic positive curvature: $F^{\rm flow} \gg 0$.

**Why is inflation inherently sectoral (not uniform)?**
Because $M^s_{\rm goods}$ is a curved manifold — geodesics on it are not straight lines.
A shock to energy prices (a displacement on the energy sector face of $\Delta_{d_g-1}$)
does not propagate uniformly to all goods — it propagates along geodesics on $M^s_{\rm goods}$,
which curve depending on the input-output structure of the economy. Shelter inflation
is sticky because the shelter sector face of $M^s_{\rm goods}$ has high curvature —
slow geodesics (long mean reversion). Energy inflation is volatile because the energy
sector face has low curvature — fast geodesics.

---

## 9. What This Means for a Portfolio Manager

### 9.1 The key practical insights

**Inflation is not a number. It is a vector.**
The CPI headline number is the Fisher-Rao norm of a sectoral inflation vector.
Manage your portfolio's exposure to each component, not just the aggregate.
Your real return depends on YOUR consumption basket's Fisher-Rao path, not the
aggregate CPI.

**Real returns depend on path, not just level.**
The Fisher equation $r_{\rm real} = r_{\rm nom} - \pi$ is exact only for flat
connections. When the inflation connection is curved (sector-specific shocks),
your real return depends on the path of prices relevant to your specific
consumption and production structure. A commodity producer's real return during
an energy price spike is not the same as a tech company's real return.

**The natural rate is on the goods manifold, not in a spreadsheet.**
Central banks estimate $r^{\ast}$ econometrically. The geometric framework says $r^{\ast}$
is the policy rate at which the curvature of the capital flow connection is zero.
You can estimate it directly from the divergence of capital flows between the
financial and goods markets — no need for unobservable potential output.

**Carry trades are Berry phases. They decay when the connection flattens.**
The expected return on a carry trade is the Berry phase around the international
capital flow loop. When global monetary policy converges (all central banks at
the same rate), the loop curvature goes to zero, the Berry phase vanishes, and
carry returns collapse. This happened in 2008 and 2020.

**A supply shock is a sudden change in goods manifold geometry.**
COVID, war, supply chain disruption — these compress or deform $M^s_{\rm goods}$.
They are changes in the shape of the goods manifold, not just price level shocks.
The inflation from a supply shock is structurally different from demand-pull
inflation: it is a manifold deformation rather than increased flow velocity.
It responds differently to monetary policy — and our framework says why.

---

## 10. New Results for the Monograph

**Lemma I1** *(Inflation is not scale-invariant)*. The Fisher-Rao inflation rate (2.1)
is not invariant under rescaling of the expenditure weights. Doubling all weights
doubles the Fisher-Rao speed. This is why the inflation rate depends on the
composition of the CPI basket — changing the basket changes the manifold metric.
**Implication:** The "true" inflation rate of an individual investor depends on
their specific consumption basket, not the aggregate CPI.

**Lemma I2** *(The Fisher equation is a first Bianchi identity)*. The Fisher equation
$r_{\rm real} = r_{\rm nom} - \pi$ is the first Bianchi identity $dF^{\rm flow} = 0$
of the capital flow connection, integrated over one investment cycle. Non-Bianchi
corrections (when $dF\neq 0$) correspond to unexpected inflation — inflation not
explained by money supply growth.

**Lemma I3** *(The velocity of money is the O'Neill $A$-tensor norm)*. The Fisherian
velocity of money $V = PQ/M$ equals the Fisher-Rao norm of the O'Neill $A$-tensor:
$V = |A|_{g_{\rm combined}}$. High velocity = strong coupling between financial and
goods manifolds. The liquidity trap ($V\to 0$) is the collapse of the $A$-tensor —
complete decoupling of the two manifolds.

**Lemma I4** *(Stagflation = positive manifold curvature with contracting goods volume)*.
Stagflation (inflation + recession) is geometrically impossible in a simple two-manifold
system where both manifolds expand proportionally. It requires the goods manifold
to contract (supply shock, negative productivity) while the capital flow connection
maintains positive curvature (loose monetary policy). Stagflation is the signature
of a supply shock that the central bank fails to accommodate — or chooses not to.

---

## References

Fisher, I. (1930). *The Theory of Interest*. Macmillan.

O'Neill, B. (1966). The fundamental equations of a submersion.
*Michigan Mathematical Journal* 13(4), 459–469.

Taylor, J. B. (1993). Discretion versus policy rules in practice.
*Carnegie-Rochester Conference Series on Public Policy* 39, 195–214.

Wicksell, K. (1898). *Interest and Prices*. Macmillan (1936 translation).

Lustig, H. and Verdelhan, A. (2007). The cross-section of foreign currency
risk premia and consumption growth risk.
*American Economic Review* 97(1), 89–117.

*[All other references as per companion papers.]*
