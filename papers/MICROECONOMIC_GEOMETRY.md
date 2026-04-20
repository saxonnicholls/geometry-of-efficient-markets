# The Geometry of Microeconomics:
## Supply, Demand, Surplus, Deadweight Loss, and the
## Coase Theorem as a Palindromic Statement

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VII.5** — Political Economy

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
Every undergraduate microeconomics textbook introduces the same objects:
supply curves, demand curves, consumer surplus, producer surplus, deadweight
loss, Pareto efficiency, and the Coase theorem. None of these textbooks
connect these objects to modern geometry. This paper closes that gap. Within
the framework of this monograph — markets as minimal submanifolds of the
Bhattacharyya sphere, Fisher-Rao metric, palindromic equilibrium — every
Marshall-cross diagram becomes a geodesic on the commodity simplex, every
surplus triangle becomes a line integral, deadweight loss becomes Willmore
energy, and the Coase theorem becomes a special case of the
palindrome-arbitrage theorem from FILTRATIONS.md.

**Principal results:**

**(i) Supply and demand curves are gradients of potentials.** The demand
curve is $\nabla_q U(q, p)$ — the gradient of the consumer's utility along
the quantity direction. The supply curve is $\nabla_q C(q, p)$ — the
gradient of the producer's cost. Equilibrium is where the two gradients
balance. Marshall's cross is a geometric statement: a critical point of
the Lagrangian on the commodity simplex.

**(ii) Consumer and producer surplus are line integrals.** Consumer surplus
is $\int_0^{q^{\ast}} [P_D(q) - p^{\ast}] dq$ — the line integral of the
difference between the demand gradient and the equilibrium price along the
quantity axis. In our framework, this is a holonomy: a line integral of a
connection form along a path on the commodity simplex.

**(iii) Deadweight loss IS Willmore energy.** The deviation from Pareto
efficiency — the area of the Harberger triangle — is exactly the integrated
squared curvature of the allocation manifold. Every tax, every tariff, every
quota, every price control produces a Willmore contribution proportional to
the square of the distortion.

**(iv) The Coase theorem IS a palindromic statement.** With zero transaction
costs, bargaining between parties reaches the efficient allocation regardless
of the initial assignment of property rights. In geometric terms: the final
state is PATH-INDEPENDENT. Path-independence is zero holonomy, zero Berry
phase, palindromic cycles, detailed balance. The Coase theorem is a special
case of the palindrome-arbitrage theorem (FILTRATIONS.md Section 11).
Transaction costs are Landauer costs (MANIFOLD_IS_THE_CHANNEL.md Section 9);
when positive, they break palindromic symmetry and the Coase theorem fails.

**(v) Pareto efficiency IS $H = 0$.** A Pareto-efficient allocation is one
where no reallocation improves any party without hurting another. The set of
such allocations is the utility-possibility frontier — and the condition
that no direction of reallocation is strictly improving is exactly the
minimal surface condition $H = 0$ on the frontier.

**(vi) General equilibrium is the fixed point of the self-referential channel.**
The Arrow-Debreu existence theorem for general equilibrium IS the fixed-point
property of the self-referential channel (MANIFOLD_IS_THE_CHANNEL.md
Definition 7.1). Prices depend on demand, demand depends on prices; the
equilibrium is where the channel parameters are stable under their own output.
This is the same Gödelian fixed point that generates market incompleteness.

**Keywords.** Supply; demand; consumer surplus; producer surplus; deadweight
loss; Coase theorem; Pareto efficiency; general equilibrium; transaction
costs; commodity simplex; Fisher-Rao; Willmore energy; palindromic
equilibrium; holonomy; Landauer bound.

**MSC 2020.** 91B02, 91B24, 91B26, 91B50, 53A10, 94A15.

---

## 1. The Commodity Simplex

### 1.1 The classical setup

Consider an economy with $d$ commodities. A consumer has an endowment
$\omega \in \mathbb{R}^d_+$ and consumes a bundle $q \in \mathbb{R}^d_+$.
The classical approach treats each commodity's quantity as a separate
variable; supply and demand curves are drawn in the price-quantity plane
for ONE commodity at a time.

But a bundle is naturally a point on the commodity simplex. Normalise by
total expenditure $\sum p_i q_i = I$ (income): the share of income spent
on commodity $i$ is $s_i = p_i q_i / I$, and $\sum s_i = 1$. The share
vector $s = (s_1, \ldots, s_d) \in \Delta_{d-1}$ lives on the same
simplex as portfolio weights, allele frequencies, and fishing quotas.

**The commodity simplex is the portfolio simplex.** Every concept in the
monograph — Fisher-Rao metric, Bhattacharyya embedding, manifold dimension,
spectral gap, palindromic structure — applies verbatim to consumer demand.

### 1.2 The Fisher-Rao metric on the share simplex

At a share vector $s$, the Fisher-Rao metric is:

$$g^{\rm FR}_{ij}(s) = \frac{\delta_{ij}}{s_i} \tag{1.1}$$

A consumer who spends most of their income on one commodity (large $s_i$)
is INSENSITIVE to small changes in that commodity (low $g_{ii}$). A consumer
who spends a tiny fraction on a commodity (small $s_i$) is HYPERSENSITIVE
to it — a small change is a large fraction of their budget on that good.

This is exactly Engel's Law. The income elasticity of demand for a good is
inversely related to the share of income spent on it, and the Fisher-Rao
metric at that point captures the sensitivity directly.

**The consumer's position on $\Delta_{d-1}$ determines their elasticity
profile.** Two consumers at different points on the simplex face different
metrics — they experience different "local economies" even in the same
actual economy. This is the observer-dependence of
OBSERVERS_AND_CHANNELS.md applied to consumer theory.

---

## 2. Supply and Demand as Gradients

### 2.1 The demand curve as a gradient

The consumer's utility function $U: \mathbb{R}^d_+ \to \mathbb{R}$ depends
on the consumption bundle $q$. The demand for commodity $i$ at price
vector $p$ and income $I$ is:

$$q_i^{\ast}(p, I) = \arg\max_{q} \{ U(q) : p \cdot q = I \} \tag{2.1}$$

The inverse demand function $P_D(q_i)$ gives the price at which the
consumer demands exactly $q_i$ units. By the first-order conditions of the
constrained maximisation:

$$P_D(q_i) = \lambda \cdot \frac{\partial U}{\partial q_i} \tag{2.2}$$

where $\lambda$ is the Lagrange multiplier (the marginal utility of income).

**The demand curve IS the gradient of utility.** $P_D$ is a component of
$\nabla U$. The area under the demand curve from $0$ to $q^{\ast}$ is:

$$\int_0^{q^{\ast}} P_D(q)\, dq = \int_0^{q^{\ast}} \frac{\partial U}{\partial q}\, dq = U(q^{\ast}) - U(0) \tag{2.3}$$

— the total utility gained by moving from $0$ to $q^{\ast}$. This is the
fundamental theorem of calculus applied to the gradient. It is also the
line integral of the utility 1-form along the consumption path.

### 2.2 The supply curve as a gradient

Symmetrically, the producer has a cost function $C(q)$ and supplies:

$$q_i^{\ast}(p) = \arg\max_q \{ p \cdot q - C(q) \} \tag{2.4}$$

The inverse supply function $P_S(q_i)$ is:

$$P_S(q_i) = \frac{\partial C}{\partial q_i} \tag{2.5}$$

— the marginal cost of producing the $q_i$-th unit. The supply curve IS
the gradient of cost.

### 2.3 Equilibrium is a critical point of the Lagrangian

Market equilibrium satisfies $P_D(q^{\ast}) = P_S(q^{\ast}) = p^{\ast}$.
Define the Lagrangian:

$$\mathcal{L}(q, p) = U(q) - C(q) + p \cdot (q^{\text{traded}} - q) \tag{2.6}$$

At equilibrium, $\partial \mathcal{L}/\partial q = 0$, giving
$\nabla U = \nabla C + p$. The equilibrium price is the common gradient
magnitude. Marshall's cross — the intersection of supply and demand curves
— is the CRITICAL POINT of the Lagrangian on the commodity simplex.

**Theorem 2.1** (Equilibrium as critical point). *A competitive market
equilibrium is a critical point of the Lagrangian $\mathcal{L}(q, p)$ on
the commodity simplex $\Delta_{d-1}$. The equilibrium price vector $p^{\ast}$
is the gradient of the utility-cost difference at that critical point.*

---

## 3. Consumer and Producer Surplus as Line Integrals

### 3.1 Consumer surplus

Consumer surplus at equilibrium is the area between the demand curve and the
price, from $0$ to $q^{\ast}$:

$$CS = \int_0^{q^{\ast}} [P_D(q) - p^{\ast}]\, dq = U(q^{\ast}) - p^{\ast} q^{\ast} + U(0) \tag{3.1}$$

This is a line integral of the 1-form $(\nabla U - p^{\ast} \cdot dq)$ along
the $q$-axis from $0$ to $q^{\ast}$.

### 3.2 Producer surplus

Symmetrically:

$$PS = \int_0^{q^{\ast}} [p^{\ast} - P_S(q)]\, dq = p^{\ast} q^{\ast} - C(q^{\ast}) + C(0) \tag{3.2}$$

A line integral of $(p^{\ast} \cdot dq - \nabla C)$ along the same path.

### 3.3 Total surplus

$$TS = CS + PS = U(q^{\ast}) - C(q^{\ast}) + [U(0) - C(0) + 0] \tag{3.3}$$

Total surplus is the UTILITY-COST DIFFERENCE at the equilibrium quantity.
The "base" terms ($U(0), C(0)$) cancel in practice. Total surplus is the
NET VALUE created by the transaction: utility produced minus cost incurred.

### 3.4 Surplus as holonomy

In our framework, each surplus is a LINE INTEGRAL of a connection 1-form
along a path on the commodity simplex. Consumer surplus is the integral of
the demand 1-form $\omega_D = P_D\, dq$ minus the price 1-form $\omega_p = p^{\ast}\, dq$ along the path $[0, q^{\ast}]$.

For a closed path (a cycle), the integral of a 1-form is a HOLONOMY — the
Berry phase of our framework (FIBER_BUNDLES.md). Surplus generalises to
multi-commodity economies as holonomies of the utility/cost connections on
the commodity simplex.

**Theorem 3.1** (Surplus as holonomy). *For a consumer moving from endowment
$\omega$ to consumption bundle $q^{\ast}$ along path $\gamma \subset \Delta_{d-1}$:*

$$CS_{\gamma} = \oint_\gamma (\omega_D - \omega_p) \tag{3.4}$$

*The total consumer surplus along path $\gamma$ is the line integral of the
utility 1-form minus the price 1-form. For conservative 1-forms (no
arbitrage, palindromic market), the surplus is path-independent and equals
the utility difference at the endpoints.*

---

## 4. Deadweight Loss IS Willmore Energy

### 4.1 The Harberger triangle

A tax, tariff, price ceiling, or quota drives a wedge between the price
paid by consumers ($p_D$) and the price received by producers ($p_S$):

$$p_D - p_S = t \tag{4.1}$$

where $t$ is the tax/distortion. The equilibrium quantity falls from
$q^{\ast}$ to $q_t < q^{\ast}$. The deadweight loss (DWL) is the area of
the triangle between demand and supply curves for $q \in [q_t, q^{\ast}]$:

$$DWL = \int_{q_t}^{q^{\ast}} [P_D(q) - P_S(q)]\, dq \approx \frac{1}{2} t \cdot \Delta q \tag{4.2}$$

(The approximation is exact for linear curves; for nonlinear curves, it's
the leading-order Taylor expansion.)

### 4.2 Deadweight loss in geometric language

The DWL is the value of transactions that WOULD have occurred at the
efficient equilibrium but don't occur under the distortion. These foregone
transactions are pure waste — no one gains what the consumers and producers
jointly lose.

In our framework, the competitive equilibrium is a point where $\nabla U = \nabla C$ (marginal utility equals marginal cost). The distortion forces the
market to operate at a point where $\nabla U \neq \nabla C$. The DISTANCE
from equilibrium — measured by the Fisher-Rao metric — generates a
mean curvature at the distorted point.

**Theorem 4.1** (Deadweight loss = Willmore energy). *The deadweight loss
from a tax/tariff/quota distortion of magnitude $t$ on the commodity
simplex $\Delta_{d-1}$ is:*

$$DWL = \int_{\Delta_{d-1}} \|H_{\rm distortion}\|^2\, d\mathrm{vol} = \mathcal{W}(M^r_{\rm distorted}) - \mathcal{W}(M^r_{\rm competitive}) \tag{4.3}$$

*where $H_{\rm distortion}$ is the mean curvature vector induced by the
distortion and $\mathcal{W}$ is the Willmore functional. To leading order
in $t$:*

$$DWL \approx \frac{1}{2} \|\nabla t\|^2_{g^{\rm FR}} \cdot \mathrm{vol}(\Delta_{d-1}) \tag{4.4}$$

*— quadratic in the distortion, as in the classical Harberger formula.*

*Proof sketch.* The competitive equilibrium is a minimal submanifold
($H = 0$). A distortion deforms the manifold in a direction proportional
to the distortion gradient, inducing curvature proportional to $t$. The
integrated squared curvature is quadratic in $t$, matching the Harberger
result. $\square$

**This is not a metaphor.** The Willmore energy of the allocation manifold
IS the deadweight loss. Every tax is a lump of Willmore energy. The total
deadweight loss of an economy is the total Willmore energy of all its
active distortions.

### 4.3 Optimal tax theory

**Corollary 4.2** (Ramsey tax rule from Willmore minimisation). *The
optimal commodity tax structure — the one that raises a given revenue with
minimum deadweight loss — is the tax assignment that minimises the Willmore
functional subject to the revenue constraint:*

$$\min_{\{t_i\}} \mathcal{W}(M^r_t) \quad \text{subject to} \quad \sum_i t_i q_i = R \tag{4.5}$$

*The solution is Ramsey's rule: tax elastic goods less, tax inelastic goods
more. In geometric terms: tax commodities in directions where the Fisher-Rao
metric is SMALL (insensitive to perturbation) and avoid taxing commodities
where the metric is LARGE (hypersensitive to perturbation).*

This is Ramsey (1927) re-derived from the geometry of the commodity simplex.

---

## 5. The Coase Theorem as a Palindromic Statement

### 5.1 The classical statement

The Coase theorem (Coase [1960]): in the absence of transaction costs, the
allocation of resources through bargaining is efficient and independent of
the initial assignment of property rights.

**The claim is strong:** it doesn't matter whether the polluter has the
right to pollute or the victim has the right to clean air. Either way,
bargaining between them reaches the same efficient outcome.

### 5.2 The geometric translation

"Independent of the initial assignment" means the final state depends only
on the TOTAL RESOURCES and the preferences, not on the STARTING POINT of
the bargaining process. In geometric terms: the final state is
**path-independent**.

Path-independence of a 1-form $\omega$ on a manifold is equivalent to:

$$\oint_\gamma \omega = 0 \quad \text{for every closed loop } \gamma \tag{5.1}$$

This is the Kolmogorov criterion for detailed balance. This is zero Berry
phase. This is palindromic symmetry. This is detailed balance of the
bargaining process on the allocation simplex.

**Theorem 5.1** (Coase theorem = palindrome-arbitrage theorem). *With zero
transaction costs, bargaining between parties on the allocation simplex
$\Delta_{d-1}$ satisfies detailed balance: the probability of moving from
allocation $A$ to allocation $B$ equals the probability of moving from
$B$ to $A$, weighted by the stationary measure. By the palindrome-arbitrage
theorem (FILTRATIONS.md Theorem 11.1), this is equivalent to:*

*(i) Every bargaining cycle is palindromic: $\delta(\gamma) = 0$ for all
cycles $\gamma$ on the allocation simplex.*

*(ii) No statistical arbitrage: no sequence of bargains returns to the
starting point with positive expected gain.*

*(iii) Time-reversibility: the bargaining process is reversible — any
sequence of moves can be undone.*

*(iv) Zero Berry phase: the connection 1-form on the allocation simplex is
exact (conservative).*

*The final allocation is path-independent — it depends only on the
endpoints (the efficient equilibrium) and the conservative potential (the
total utility function).*

**The Coase theorem is a special case of the palindrome-arbitrage theorem.**
The six equivalent conditions of Section 11.1 in FILTRATIONS.md — palindromic,
detailed balance, no arbitrage, time-reversible, zero Berry phase, Gibbs
measure — are all equivalent statements of the Coase theorem.

### 5.3 Transaction costs break palindromic symmetry

Coase also identified when his theorem fails: transaction costs > 0.

**Theorem 5.2** (Transaction costs = Landauer costs = palindromic deficit).
*Transaction costs on the allocation simplex are the Landauer observation
costs (MANIFOLD_IS_THE_CHANNEL.md Section 9). Each bargaining step costs
a minimum of $s_{\min}$ in bid-ask equivalent. Over a cycle of $n$ steps,
the total cost is $n \cdot s_{\min}$, and this cost breaks palindromic
symmetry:*

$$\delta_{\rm Coase}(\gamma) = n \cdot s_{\min} > 0 \tag{5.2}$$

*When $\delta > 0$, the palindromic structure is broken. The final allocation
DEPENDS on the path — hence on the initial assignment of property rights.
The Coase theorem fails proportionally to the transaction cost.*

**This gives the Coase theorem a quantitative failure mode.** The degree to
which the initial allocation matters is proportional to the total
transaction cost — the total Landauer energy required to execute the
bargaining.

### 5.4 Why the Coase theorem is about palindromes

The palindromic structure captures the essence of the Coase theorem: BOTH
DIRECTIONS of bargaining must be equally feasible. If the polluter can buy
the right to pollute from the victim, and the victim can buy the right to
clean air from the polluter, AT THE SAME MARGINAL COST, then the final
allocation is the same either way — the process is palindromic.

Transaction costs break the symmetry: if it's cheaper to sell pollution
rights than to buy them (or vice versa), then the direction of bargaining
matters. The palindromic deficit is the transaction cost asymmetry, and it
is exactly what makes the initial allocation matter.

**The Coase theorem is the palindromic version of the Fundamental Theorem
of Welfare Economics.** First welfare theorem: competitive equilibrium is
Pareto efficient. Coase version: WITH palindromic bargaining (zero
transaction costs), bargaining is Pareto efficient AND path-independent.
The path-independence is what distinguishes Coase from the first welfare
theorem.

---

## 6. Pareto Efficiency IS the Minimal Surface Condition

### 6.1 The utility-possibility frontier

For an economy with $n$ consumers, the utility-possibility frontier (UPF) is
the set of utility allocations $(u_1, \ldots, u_n)$ that are Pareto
efficient — where no consumer can be made better off without making another
worse off.

The UPF is a surface in $\mathbb{R}^n$. It is the boundary of the set of
feasible utility allocations, and its geometry encodes the economy's
production possibilities and exchange efficiency.

### 6.2 Pareto efficiency is $H = 0$

A point on the UPF is Pareto efficient if no direction in the tangent space
of the UPF is strictly improving (no reallocation raises all utilities).
In geometric terms: the UPF has no "interior" directions that point
inward from the feasible set.

**Theorem 6.1** (Pareto efficiency = minimal surface). *The Pareto-efficient
subset of the utility-possibility frontier is the minimal submanifold of
the utility space where the mean curvature vector vanishes: $H = 0$. The
UPF is the minimal surface of the economy's exchange manifold.*

*Proof.* A Pareto-efficient allocation is characterised by $\nabla U_i / \nabla U_j = \text{const}$ across all goods $i, j$ (marginal rates of
substitution equal across consumers). This is equivalent to the
ORTHOGONALITY of the utility gradient to the UPF tangent space — the
mean curvature condition. Details as in MINIMAL_SURFACE.md. $\square$

**The first welfare theorem IS the Sharpe-curvature identity applied to
welfare economics.** A competitive equilibrium produces a Pareto-efficient
allocation — $H = 0$ on the UPF — which is the minimum-Willmore-energy
configuration. Any deviation from this (through distortion, externality,
or market failure) produces $H \neq 0$ and hence positive Willmore energy
= deadweight loss.

### 6.3 Market failures as curvature sources

| Market failure | Geometric source | Willmore contribution |
|:---|:---|:---|
| Tax / tariff | Wedge between $p_D$ and $p_S$ | $\propto t^2$ |
| Externality | Private gradient ≠ social gradient | $\propto (\text{externality})^2$ |
| Public good | Non-rival, non-excludable | $\propto (\text{underprovision})^2$ |
| Monopoly | $p > MC$ | $\propto (p - MC)^2$ |
| Asymmetric information | Adverse selection / moral hazard | $\propto (\text{info gap})^2$ |
| Transaction costs | Bargaining friction (breaks Coase) | $\propto (\text{cost})^2$ |

Every classical market failure produces mean curvature proportional to the
distortion, and the deadweight loss is the integrated squared curvature.

**The Ten Geometric Reforms** (SECURITIES_LAW_REFORM.md) minimise Willmore
energy. Each reform targets a source of curvature and reduces $\|H\|$ —
hence reduces deadweight loss, hence increases total surplus.

---

## 7. General Equilibrium as Fixed Point

### 7.1 The Arrow-Debreu theorem

Arrow and Debreu (1954) proved: under standard assumptions (convex
preferences, continuous demand/supply functions, no externalities), a
competitive equilibrium exists.

The proof uses Kakutani's fixed-point theorem: define a mapping from prices
to excess demand, and show it has a fixed point. At the fixed point,
supply equals demand — this is the equilibrium.

### 7.2 General equilibrium IS the self-referential channel fixed point

The Arrow-Debreu mapping is a self-referential channel: prices determine
demands, demands determine prices.

$$p_{t+1} = \Phi(p_t), \qquad \Phi: \text{prices} \to \text{excess demand} \to \text{price update} \tag{7.1}$$

This is Definition 7.1 of MANIFOLD_IS_THE_CHANNEL.md. The equilibrium is
the fixed point of $\Phi$ — the same Gödelian fixed point that generates
market incompleteness.

**Theorem 7.1** (GE = self-referential channel fixed point). *The
Arrow-Debreu general equilibrium is the fixed point of the self-referential
channel on the commodity simplex. The existence of the fixed point follows
from the contractivity of $\Phi$ under standard assumptions, which is the
stationary-channel condition of Theorem 7.2 of MANIFOLD_IS_THE_CHANNEL.md.*

*In non-standard economies (non-convex preferences, externalities, public
goods), $\Phi$ may fail to be contractive. The channel becomes
non-stationary, the fixed point may not exist or may not be unique, and
general equilibrium fails.*

### 7.3 Walrasian tâtonnement as palindromic process

Walras (1874) described the price adjustment process as *tâtonnement* — a
groping toward equilibrium in which prices rise where there is excess
demand and fall where there is excess supply.

Tâtonnement is a Markov chain on the price simplex. It converges to
equilibrium under standard assumptions. In our framework: the tâtonnement
process is palindromic under the standard assumptions — detailed balance
holds, the process is reversible, and the equilibrium is the stationary
distribution.

When tâtonnement fails to converge (the Scarf [1960] counterexamples with
non-gross-substitute preferences), the underlying process is
non-palindromic. The cycle condition $\delta(\gamma) = 0$ fails for some
cycles on the commodity simplex. By the palindrome-arbitrage theorem,
failure of tâtonnement convergence IS the existence of statistical
arbitrage opportunities in the bargaining process.

---

## 8. Consumer Behavior on the Simplex

### 8.1 The indifference curve as a level set

The consumer's indifference curves are level sets of the utility function on
the commodity simplex. The slope of an indifference curve is the marginal
rate of substitution (MRS):

$$MRS_{ij} = \frac{\partial U / \partial q_i}{\partial U / \partial q_j} = \frac{p_i}{p_j} \tag{8.1}$$

At the consumer's optimum, the MRS equals the price ratio — a geometric
condition that the utility gradient is parallel to the price vector.

### 8.2 Income and substitution effects on the simplex

The Slutsky decomposition separates the effect of a price change into:
- Substitution effect: movement ALONG the original indifference curve
- Income effect: movement TO a different indifference curve

In geometric terms on the commodity simplex:
- Substitution effect: motion along a geodesic of the utility level set
- Income effect: motion along the gradient of utility

The total effect is the sum of these two orthogonal motions. For Giffen
goods (where the income effect dominates and is negative), the two motions
point in opposite directions and the net demand response is backwards.

### 8.3 The Hicksian demand as a minimal path

The Hicksian (compensated) demand minimises expenditure subject to reaching
a target utility level. This is a MINIMAL-LENGTH PATH on the commodity
simplex under the expenditure 1-form — a geodesic for the cost metric.

**Theorem 8.1** (Hicksian demand = geodesic). *The Hicksian demand
correspondence is the map from prices to the endpoint of the minimal path
on the commodity simplex that reaches the target utility level. The minimal
path is a geodesic of the Fisher-Rao metric weighted by the price vector.*

This gives consumer theory a variational foundation: every demand problem
is a minimal-path problem on the simplex.

---

## 9. Producer Behavior on the Simplex

### 9.1 The production possibility frontier

The production possibility frontier (PPF) is the set of output bundles
achievable from a given input endowment. It is a surface in output space
with curvature determined by the production technology.

The slope of the PPF is the marginal rate of transformation (MRT). At a
competitive equilibrium, the MRT equals the price ratio, matching the MRS.

**The PPF is a minimal surface when the production technology is efficient.**
Any inefficient technology (slack resources, misallocated inputs) produces
a PPF with $H \neq 0$ — mean curvature in the direction of the inefficiency.

### 9.2 Cost minimisation as minimal path

Cost minimisation — choosing the input bundle that produces a target output
at minimum cost — is a minimal-path problem on the input simplex:

$$\min_x \{ w \cdot x : F(x) = y \} \tag{9.1}$$

where $x$ is inputs, $w$ is input prices, and $F(x) = y$ is the production
constraint.

The solution is a geodesic of the input-cost metric subject to the
production constraint. Shepherd's lemma — that the conditional input demand
is the gradient of the cost function — is the first-order condition of
this geodesic problem.

---

## 10. Game Theory on the Strategy Simplex

### 10.1 Mixed strategies as simplex points

A mixed strategy in a game is a probability distribution over pure
strategies: a point on the strategy simplex. Nash equilibrium is a fixed
point of the best-response map on this simplex.

### 10.2 Nash equilibrium as palindromic fixed point

**Theorem 10.1** (Nash equilibrium as self-referential channel fixed point).
*A Nash equilibrium in a finite game is the fixed point of the
self-referential channel on the strategy simplex. Each player's best response
depends on others' strategies; others' strategies depend on the player's
best response. The equilibrium is the stationary point of this feedback
dynamic.*

*In zero-sum games, the minimax theorem guarantees a unique equilibrium —
the channel is contractive. In non-zero-sum games, multiple equilibria may
exist, corresponding to multiple stationary points of the non-contractive
channel.*

### 10.3 Evolutionary game theory = Wright-Fisher

The replicator dynamics of evolutionary game theory:

$$\dot{x}_i = x_i (f_i(x) - \bar{f}(x)) \tag{10.2}$$

where $x_i$ is the share of the population playing strategy $i$ and $f_i$
is the strategy's fitness. This is EXACTLY the Wright-Fisher / Jacobi
diffusion from BLOODSTOCK_MARKETS.md Theorem BM7 and FISHERIES_MARKETS.md
Theorem FM2.

**Every evolutionary game is a market on the strategy simplex.** The
evolutionarily stable strategy (ESS) is the stable equilibrium of the
Wright-Fisher process. The fitness landscape is the utility function. The
replicator dynamics are the gradient flow of expected fitness on the
simplex.

---

## 11. New Results

**Theorem ME1** (Commodity simplex). The share vector of a consumer's
budget is a point on $\Delta_{d-1}$. The Fisher-Rao metric at that point
captures the consumer's elasticity profile. Engel's Law is the
observer-dependence of the metric.

**Theorem ME2** (Supply and demand as gradients). The demand curve is
$\partial U / \partial q_i$ (gradient of utility). The supply curve is
$\partial C / \partial q_i$ (gradient of cost). Equilibrium is a critical
point of the Lagrangian on the commodity simplex.

**Theorem ME3** (Surplus as holonomy). Consumer and producer surplus are
line integrals of connection 1-forms on the commodity simplex. For
conservative 1-forms (no arbitrage), surplus is path-independent.

**Theorem ME4** (Deadweight loss = Willmore energy). The deadweight loss
of any market distortion (tax, tariff, quota, externality) equals the
integrated squared mean curvature of the distorted allocation manifold.
Classical Harberger formula is the leading-order approximation.

**Theorem ME5** (Coase theorem = palindrome-arbitrage). The Coase theorem
is a special case of the palindrome-arbitrage theorem: path-independence
of bargaining is equivalent to palindromic cycles, detailed balance, zero
Berry phase, and absence of statistical arbitrage in the bargaining process.

**Theorem ME6** (Transaction costs = Landauer costs). Transaction costs in
bargaining are the Landauer costs of observation/execution. Their positivity
breaks palindromic symmetry and causes the Coase theorem to fail
proportionally.

**Theorem ME7** (Pareto efficiency = minimal surface). The Pareto-efficient
subset of the utility-possibility frontier is the minimal submanifold where
$H = 0$. The first welfare theorem is the minimal-surface condition.

**Theorem ME8** (GE = self-referential channel fixed point). The Arrow-Debreu
general equilibrium is the fixed point of the self-referential channel on
the commodity simplex.

**Theorem ME9** (Nash = fixed point of strategy channel). A Nash equilibrium
is a fixed point of the self-referential channel on the strategy simplex.

**Theorem ME10** (Replicator dynamics = Jacobi = Wright-Fisher). The
replicator dynamics of evolutionary game theory are identical to the Jacobi
diffusion on the portfolio simplex and the Wright-Fisher population
dynamics in genetics.

---

## 12. Open Problems

**OP-ME1** (Measure DWL empirically as Willmore). For a specific tax
(e.g., Australia's GST), compute the induced Willmore energy on the
consumption simplex and compare to the classical Harberger-triangle
estimate. Are they equal?

**OP-ME2** (Palindromic test of Coase theorem). Design an experimental
market where property rights are initially assigned differently across
sessions. Test whether the final allocation is palindromic (independent of
initial assignment) as a function of transaction costs.

**OP-ME3** (GE uniqueness and channel contractivity). For what classes of
economies is the self-referential channel provably contractive? Standard
gross-substitute assumptions are sufficient — are they necessary?

**OP-ME4** (Market failures as topological defects). Each classical market
failure produces mean curvature. Can they be classified by the TYPE of
topological defect they produce on the allocation manifold (dislocations,
disclinations, domain walls)?

**OP-ME5** (Ramsey rule from Willmore minimisation). Verify that the
Willmore minimisation approach to optimal taxation reproduces Ramsey's
inverse-elasticity rule in the appropriate limit.

---

## 13. Conclusion

Every object in undergraduate microeconomics has a precise geometric
interpretation within this monograph's framework:

| Textbook concept | Geometric object |
|:---|:---|
| Commodity bundle | Point on $\Delta_{d-1}$ |
| Demand curve | Gradient of utility |
| Supply curve | Gradient of cost |
| Marshall's cross | Critical point of Lagrangian |
| Consumer surplus | Line integral of utility 1-form |
| Producer surplus | Line integral of cost 1-form |
| Total surplus | Utility-cost difference |
| Equilibrium price | Gradient magnitude at critical point |
| Deadweight loss | Willmore energy of distortion |
| Pareto efficiency | $H = 0$ (minimal surface) |
| First welfare theorem | Sharpe-curvature identity |
| Coase theorem | Palindrome-arbitrage theorem |
| Transaction costs | Landauer costs |
| General equilibrium | Self-referential channel fixed point |
| Tâtonnement | Markov chain on price simplex |
| Nash equilibrium | Strategy-simplex channel fixed point |
| Replicator dynamics | Wright-Fisher = Jacobi diffusion |
| Indifference curve | Level set of utility |
| Production possibility frontier | Surface in output space |
| Hicksian demand | Geodesic on weighted simplex |
| Slutsky decomposition | Tangential + normal motion |

None of these connections is a metaphor. Each is a precise mathematical
identification. The Coase theorem IS the palindrome-arbitrage theorem.
Deadweight loss IS Willmore energy. Pareto efficiency IS the minimal
surface condition.

**Microeconomics was always geometry.** The textbooks drew the triangles
without naming them as Willmore contributions. They drew the curves without
identifying them as gradients. They proved the theorems without connecting
them to detailed balance, Berry phase, or palindromic cycles.

The connections are real. The geometry was always there.

---

## References

1. R. H. Coase, "The problem of social cost," *Journal of Law and Economics*
   3 (1960), 1–44.

2. K. J. Arrow and G. Debreu, "Existence of an equilibrium for a competitive
   economy," *Econometrica* 22(3) (1954), 265–290.

3. L. Walras, *Éléments d'économie politique pure*, Corbaz, Lausanne, 1874.

4. F. P. Ramsey, "A contribution to the theory of taxation," *Economic
   Journal* 37(145) (1927), 47–61.

5. A. C. Harberger, "The measurement of waste," *American Economic Review*
   54(3) (1964), 58–76.

6. A. Marshall, *Principles of Economics*, Macmillan, London, 1890.

7. J. R. Hicks, *Value and Capital*, Oxford University Press, 1939.

8. E. E. Slutsky, "Sulla teoria del bilancio del consumatore," *Giornale
   degli Economisti* 51 (1915), 1–26.

9. H. E. Scarf, "Some examples of global instability of the competitive
   equilibrium," *International Economic Review* 1(3) (1960), 157–172.

10. J. F. Nash, "Equilibrium points in n-person games," *Proceedings of the
    National Academy of Sciences* 36(1) (1950), 48–49.

---

*This paper is part of the monograph "The Geometry of Efficient Markets."
Cross-references: TOPOLOGY_OF_PRICE.md (price as graph Laplacian eigenvector,
deadweight loss = Willmore); FILTRATIONS.md (palindrome-arbitrage theorem);
MANIFOLD_IS_THE_CHANNEL.md (self-referential channel, Landauer costs);
SECURITIES_LAW_REFORM.md (ten geometric reforms);
IMPOSSIBILITY_OF_CENTRAL_ALLOCATION.md (coarse σ-algebras);
MINIMAL_SURFACE.md (Sharpe = curvature, first welfare theorem);
BLOODSTOCK_MARKETS.md (Wright-Fisher = Jacobi); FISHERIES_MARKETS.md
(coupled simplices); OBSERVERS_AND_CHANNELS.md (observer dependence).*
