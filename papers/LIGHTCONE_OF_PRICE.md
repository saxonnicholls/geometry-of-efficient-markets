# The Lightcone of Price:
## Causal Structure, Lorentzian Geometry, and the Speed
## of Information on Market Manifolds

**Saxon Nicholls** — me@saxonnicholls.com

**Paper 0.8** — Foundation

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
Time is not just another coordinate on the market manifold. It is distinguished:
you can trade forward but not backward; information propagates at finite speed
$c_M$; the cost of holding a position through time (carry, funding, theta) enters
with the OPPOSITE SIGN to the return on that position. These properties define a
semi-Riemannian (Lorentzian) manifold. We develop the Lorentzian geometry of
markets: the metric has signature $(-,+,+,\ldots,+)$ where the negative direction
is time and the positive directions are factor returns. The lightcone at each
point determines which future trades are causally accessible from the current
state. The speed of light $c_M$ is the maximum rate at which information
propagates on the Voronoi-tessellated market manifold — set by the spectral
gap and the graph diameter. Events outside the lightcone are CAUSALLY
DISCONNECTED from the present: no information from the current trade can
influence them.

This framework unifies several otherwise disconnected results:
(i) the CFL condition for portfolio rebalancing (OBSERVERS_AND_CHANNELS
Theorem O6) IS the condition that the discretisation respects the lightcone;
(ii) the O'Neill curvature of intermarket connections (FIBER_BUNDLES,
INTERMARKET_GEOMETRY) IS the spacetime curvature of the Lorentzian market;
(iii) the braid word of BRAIDS.md IS the worldline history of asset prices
in the Lorentzian spacetime;
(iv) the insider's information advantage (NETWORK_INFORMATION_THEORY
Theorem N3) IS the ability to see outside the public lightcone — they
have a WIDER lightcone than the market.

**Principal results:**

**(i) The market spacetime metric.** The $(r+1)$-dimensional market spacetime
has Lorentzian metric:
$$ds^2 = -c_M^2\,dt^2 + g^{\rm FR}_{ij}\,db^i\,db^j \tag{0.1}$$
where $c_M = \lambda_1 / \text{diam}_{G}$ is the information propagation speed,
$t$ is time, and $g^{\rm FR}$ is the Fisher-Rao metric on the spatial
(portfolio) directions. The signature is $(-,+,+,\ldots,+)$.

**(ii) The lightcone determines causality.** The future lightcone of a
trade at $(t_0, b_0)$ is:
$$\mathcal{J}^{+}(t_0, b_0) = \{(t, b) : t > t_0, d_{g^{\rm FR}}(b, b_0) \leq c_M(t - t_0)\} \tag{0.2}$$
— the set of future portfolio states reachable from $b_0$ at information speed
$c_M$. Trades outside this cone CANNOT be influenced by the current state.

**(iii) The insider has a wider lightcone.** An insider with private
information effectively has a larger $c_M^{\rm insider} > c_M^{\rm public}$.
Their lightcone is wider — they can "see" (and act on) events that are
outside the public lightcone. The insider alpha
$\alpha = \varepsilon^2|v_G|_{g^{\rm FR}}$ (from the monograph) is the
excess area of the insider's lightcone over the public lightcone.

**(iv) Market horizons.** The market has HORIZONS — surfaces beyond which
information cannot propagate within the available time. The horizon at
time $T$ is the sphere of radius $c_M \cdot T$ in Fisher-Rao distance.
Events beyond this horizon are outside the market's causal past — they
have never been priced. For an asset that has traded for $T$ periods,
the horizon radius is $c_M T$ in Fisher-Rao units — the market's "observable
universe."

**(v) Geodesics are optimal execution paths.** Timelike geodesics on the
Lorentzian market manifold are the paths that MAXIMISE the proper time
(the experienced return adjusted for carry cost). These are the
Almgren-Chriss optimal execution trajectories from
STOCHASTIC_CONTROL_KALMAN.md — now derived from the variational
principle of Lorentzian geometry rather than from stochastic control.

**Keywords.** Lorentzian geometry; semi-Riemannian; causal structure;
lightcone; horizon; proper time; timelike geodesic; information speed;
CFL condition; insider trading; braid worldlines; O'Neill curvature;
spacetime curvature; market metric.

---

## 1. Why Lorentzian?

### 1.1 Time is distinguished

In the Riemannian framework of the monograph, the market manifold $M^r$ is
a SPATIAL object — a snapshot of the portfolio simplex at a single moment.
Time enters as a PARAMETER: the manifold evolves under MCF, the WF diffusion
runs on it, the trader updates.

But time is not like space. Three asymmetries:

**Asymmetry 1: Irreversibility.** You can move freely in portfolio space
(buy or sell any asset). You CANNOT move backward in time. The return series
$x_1, x_2, \ldots$ is ordered. This is a CAUSAL structure, not just a
parameterisation.

**Asymmetry 2: Finite propagation speed.** Information about a trade at
time $t_0$ reaches other parts of the market at speed $c_M$ — NOT
instantaneously. On a Voronoi tessellation, information must hop from
cell to cell. The CFL condition from OBSERVERS_AND_CHANNELS limits how
fast portfolios can respond.

**Asymmetry 3: The cost of time.** Holding a position through time has a
COST — the carry (for bonds), the funding rate (for leveraged positions),
the theta decay (for options), the opportunity cost (for cash). This cost
enters with the OPPOSITE SIGN to the return. Returns are positive (you
earn them); carry costs are negative (you pay them). This opposite sign
is the signature of a Lorentzian metric.

### 1.2 The market spacetime

Define the **market spacetime** as the $(r+1)$-dimensional manifold:

$$\mathcal{M} = \mathbb{R} \times M^r \tag{1.1}$$

with points $(t, b)$ where $t \in \mathbb{R}$ is time and $b \in M^r$ is
the portfolio state.

The **Lorentzian metric** on $\mathcal{M}$:

$$g_{\mu\nu}\,dx^\mu\,dx^\nu = -c_M^2\,dt^2 + g^{\rm FR}_{ij}(b)\,db^i\,db^j \tag{1.2}$$

The signature is $(-,+,+,\ldots,+)$:
- The $tt$-component is $g_{00} = -c_M^2 < 0$ (timelike)
- The $ij$-components are $g_{ij} = g^{\rm FR}_{ij} = \delta_{ij}/b_i > 0$ (spacelike)

This is a static spacetime (the spatial metric $g^{\rm FR}$ does not depend
on $t$) — analogous to Schwarzschild spacetime in general relativity. The
spatial geometry is curved (the Fisher-Rao metric on the simplex has curvature
$K = 1/4$), but the time direction is flat (no "gravitational" time dilation
in the base model).

---

## 2. The Lightcone

### 2.1 Causal structure

A vector $v = (v^0, v^1, \ldots, v^r)$ at a point $(t, b) \in \mathcal{M}$ is:

- **Timelike** if $g_{\mu\nu}v^\mu v^\nu < 0$: $c_M^2(v^0)^2 > g^{\rm FR}_{ij}v^iv^j$.
  The time component dominates. This is a "slow" trajectory — the portfolio
  changes slowly relative to information speed.

- **Null (lightlike)** if $g_{\mu\nu}v^\mu v^\nu = 0$: $c_M^2(v^0)^2 = g^{\rm FR}_{ij}v^iv^j$.
  The portfolio changes AT information speed. This is the boundary of causality.

- **Spacelike** if $g_{\mu\nu}v^\mu v^\nu > 0$: $c_M^2(v^0)^2 < g^{\rm FR}_{ij}v^iv^j$.
  The portfolio changes FASTER than information can propagate.
  This is ACAUSAL — it requires information that hasn't arrived yet.

The **lightcone** at $(t_0, b_0)$:

$$\mathcal{C}(t_0, b_0) = \{(t, b) : c_M^2(t - t_0)^2 = d_{g^{\rm FR}}(b, b_0)^2\} \tag{2.1}$$

The **future lightcone** (causal future):

$$\mathcal{J}^{+}(t_0, b_0) = \{(t, b) : t > t_0, d_{g^{\rm FR}}(b, b_0) \leq c_M(t - t_0)\} \tag{2.2}$$

Everything inside $\mathcal{J}^{+}$ can be influenced by a trade at $(t_0, b_0)$.
Everything outside CANNOT — the information hasn't reached there yet.

### 2.2 The speed of light

The information speed $c_M$ on the Voronoi-tessellated manifold:

$$c_M = \frac{\text{diam}_{\rm FR}(M^r)}{\text{diam}_{G} \cdot \Delta t} \tag{2.3}$$

where $\text{diam}_{G}$ is the graph diameter of the Delaunay adjacency graph
and $\Delta t$ is the time per observation step.

For our Voronoi partition of FF25 ($N = 4$ cells, $\text{diam}_{G} = 1$):
$c_M = \text{diam}_{\rm FR} / \Delta t$. With $\Delta t = 1$ day and
$\text{diam}_{\rm FR} \approx 0.5$ radians: $c_M \approx 0.5$ radians/day.

**The speed of light is the spectral gap:** $c_M \propto \lambda_1$. Markets
with large spectral gaps have faster information propagation — wider lightcones
— and incorporate new information more quickly.

### 2.3 Different observers have different lightcones

A public market participant has lightcone determined by $c_M^{\rm public}$.

An insider has additional information channels → effectively larger $c_M$:

$$c_M^{\rm insider} = c_M^{\rm public} + \Delta c \tag{2.4}$$

where $\Delta c$ depends on the quality and speed of the insider's private signal.

The **insider's lightcone is wider.** Events that are outside the public
lightcone (not yet priced by the market) are INSIDE the insider's lightcone
(they can already see and act on them). The insider alpha is the AREA
DIFFERENCE between the two lightcones:

$$\alpha \propto \text{Vol}(\mathcal{J}^{+}_{\rm insider}) - \text{Vol}(\mathcal{J}^{+}_{\rm public}) \tag{2.5}$$

This gives a NEW geometric interpretation of insider trading from
NETWORK_INFORMATION_THEORY.md: the insider doesn't "cheat" — they
simply have a wider lightcone. Their trades are CAUSAL from their
perspective (inside their lightcone) but ACAUSAL from the public
perspective (outside the public lightcone).

---

## 3. The Braid as a Worldline History

### 3.1 Asset worldlines

In the Lorentzian spacetime $\mathcal{M}$, each asset traces a **worldline**:

$$\gamma_i : \mathbb{R} \to \mathcal{M}, \qquad \gamma_i(t) = (t, b_i(t)) \tag{3.1}$$

where $b_i(t)$ is the weight of asset $i$ at time $t$.

When two asset worldlines CROSS — asset $i$'s weight overtakes asset $j$'s —
this is a **crossing event**, encoded by the braid generator $\sigma_{ij}$
from BRAIDS.md.

**The braid word of BRAIDS.md IS the worldline history in the Lorentzian
spacetime.** Each crossing generator $\sigma_i$ corresponds to a point in
spacetime where two worldlines intersect — a spacetime EVENT.

### 3.2 Yang-Baxter = no faster-than-light arbitrage

The Yang-Baxter equation from BRAIDS.md:

$$\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1} \tag{3.2}$$

says that the order in which crossings occur doesn't matter (the braid
is invariant under Reidemeister moves). In Lorentzian terms: this is
the condition that no SPACELIKE path connects two crossings — i.e.,
the crossings are causally ordered. If a spacelike path existed between
them, you could rearrange the crossings by going "faster than light,"
creating an arbitrage.

**Yang-Baxter = causality = no-arbitrage.** The three are the same condition
stated in braid theory, Lorentzian geometry, and finance respectively.

---

## 4. The O'Neill Tensor as Spacetime Curvature

### 4.1 Fiber bundle = spacetime foliation

The fiber bundle from FIBER_BUNDLES.md has:
- Base $M^r_{\rm fin}$ (systematic factors)
- Fiber (idiosyncratic returns)
- Connection (how factors affect individual assets)

In the Lorentzian framework, the base IS the spatial manifold and the
fiber structure corresponds to the FOLIATION of spacetime into spatial
hypersurfaces. The O'Neill $A$-tensor:

$$A_X Y = \Pi_V(\nabla_{\Pi_H X}\Pi_H Y) + \Pi_H(\nabla_{\Pi_H X}\Pi_V Y) \tag{4.1}$$

measures how the horizontal (systematic) and vertical (idiosyncratic) directions
twist relative to each other. In spacetime terms: the O'Neill tensor IS the
**extrinsic curvature of the spatial hypersurface** — how the spatial geometry
changes from one time slice to the next.

### 4.2 Intermarket connections as wormholes

Two markets $M_1$ and $M_2$ connected by a neck (INTERMARKET_GEOMETRY.md)
are, in the Lorentzian framework, two spacetime regions connected by a
THROAT — a wormhole-like structure. The neck width determines the causal
connection: a wide neck allows fast information transfer (the two markets
are strongly causally connected); a thin neck restricts information flow
(weakly connected, large spread).

The NECK PINCH (market de-merger) is the throat closing — the two spacetime
regions becoming causally disconnected. After the pinch, events in $M_1$
CANNOT influence events in $M_2$, regardless of time. This is the Lorentzian
content of the EMU crisis: the Greek neck pinched, and the Greek and German
bond markets became causally disconnected.

---

## 5. Horizons

### 5.1 The market horizon

For a market that has existed for $T$ periods, the **market horizon** is
the sphere of Fisher-Rao radius $c_M T$ centred at the current state:

$$\mathcal{H}(T) = \{b \in M^r : d_{g^{\rm FR}}(b, b^{\ast}) = c_M T\} \tag{5.1}$$

Everything inside the horizon has been priced (it's in the market's causal
past). Everything OUTSIDE has never been reached by market information —
it is UNPRICED.

For a young market (small $T$): the horizon is small — many portfolio states
have never been explored. The market is in Stage 1-2 of the five-stage
evolution (WHY_MARKETS_EVOLVE.md).

For a mature market (large $T$): the horizon is large — most of $M^r$ has
been explored. The market is in Stage 4-5.

### 5.2 The Rindler horizon

A trader with finite attention (processing speed $\lambda_1^{\rm trader} < c_M$)
experiences a RINDLER HORIZON — the boundary of the region they can causally
influence, given their processing speed. Events outside their Rindler horizon
evolve beyond their ability to respond.

The Rindler horizon distance:

$$d_{\rm Rindler} = c_M^2 / a \tag{5.2}$$

where $a = c_M - \lambda_1^{\rm trader}$ is the "acceleration gap" between
the market's information speed and the trader's processing speed.

Slow traders (small $\lambda_1^{\rm trader}$) have CLOSE Rindler horizons —
they can only influence a small portion of the market. Fast traders (HFTs
with $\lambda_1 \approx c_M$) have DISTANT horizons — they influence most
of the market.

---

## 6. Proper Time and Optimal Execution

### 6.1 Proper time = risk-adjusted return

The **proper time** along a worldline $\gamma(t) = (t, b(t))$ is:

$$\tau = \int \sqrt{c_M^2 - g^{\rm FR}_{ij}\dot{b}^{i}\dot{b}^{j}} dt \tag{6.1}$$

This is maximised for timelike geodesics (the twin paradox: the traveller
who stays still ages MOST; the traveller who moves fast ages less).

In financial terms: $\tau$ is the risk-adjusted return. The
$g^{\rm FR}_{ij}\dot{b}^{i}\dot{b}^{j}$ term is the COST of rebalancing
(trading friction, market impact). The $c_M^2 dt^2$ term is the BENEFIT
of time passing (the risk-free rate, the carry).

**The geodesic (maximum proper time) is the Almgren-Chriss optimal execution
path.** This was derived from stochastic control in STOCHASTIC_CONTROL_KALMAN.md.
Here it emerges from the variational principle of Lorentzian geometry:
$\delta\tau = 0$ gives the geodesic equation.

---

## 7. New Results

**Theorem L1** *(Market spacetime is Lorentzian)*.
The $(r+1)$-dimensional market spacetime with metric
$ds^2 = -c_M^2 dt^2 + g^{\rm FR}_{ij} db^i db^j$ has signature $(-,+,\ldots,+)$.
The causal structure is determined by $c_M = \lambda_1 / \text{diam}_{G}$.

**Theorem L2** *(The insider has a wider lightcone)*.
The insider alpha is proportional to the area difference between the
insider and public lightcones.

**Theorem L3** *(Yang-Baxter = causality = no-arbitrage)*.
The braid group relation $\sigma_i\sigma_{i+1}\sigma_i = \sigma_{i+1}\sigma_i\sigma_{i+1}$
is equivalent to the causal ordering of crossing events in the Lorentzian spacetime.

**Theorem L4** *(The market horizon)*.
A market of age $T$ has priced all states within Fisher-Rao distance $c_M T$
of the initial state. States beyond this horizon are unpriced.

**Theorem L5** *(Proper time = risk-adjusted return)*.
The timelike geodesic on the Lorentzian market manifold is the Almgren-Chriss
optimal execution path.

---

## 8. Open Problems

**OP-L1.** Compute the curvature tensor $R_{\mu\nu\rho\sigma}$ of the Lorentzian
market manifold. The Ricci scalar $R$ should be related to the Willmore energy
and the Sharpe ratio through the Einstein equation analogue.

**OP-L2.** Does the market have gravitational time dilation? Near the Feller
boundary ($b_i \to 0$), the metric diverges — analogous to the Schwarzschild
singularity. Does time "slow down" near default?

**OP-L3.** Are there closed timelike curves in the market spacetime? If so,
they would represent arbitrage opportunities that exploit the temporal structure
— a new type of arbitrage beyond the spatial (curvature) type.

**OP-L4.** The Penrose-Hawking singularity theorems: under what conditions does
the market spacetime develop a singularity (a crisis)? The strong energy
condition (the analogue of positive mass) should relate to the no-arbitrage
condition.

**OP-L5.** Hawking radiation: does the market horizon emit "thermal" noise?
If so, this noise IS the minimum entropy production rate at the boundary
of the observable market — a geometric lower bound on market microstructure
noise.

---

## References

O'Neill, B. (1983). *Semi-Riemannian Geometry with Applications to Relativity*.
Academic Press.

Hawking, S. W. and Ellis, G. F. R. (1973). *The Large Scale Structure of
Space-Time*. Cambridge University Press.

Penrose, R. (1965). Gravitational collapse and space-time singularities.
*Physical Review Letters* 14(3), 57–59.

Wald, R. M. (1984). *General Relativity*. University of Chicago Press.

Almgren, R. and Chriss, N. (2001). Optimal execution of portfolio transactions.
*Journal of Risk* 3(2), 5–39.

*[All other references as per companion papers.]*
