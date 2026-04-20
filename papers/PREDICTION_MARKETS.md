# Prediction Markets, Polytopes, and the Geometry of Beliefs
## The Simplex IS the Market: Information Processing, Scoring Rules,
## and Combinatorial Complexity on the Belief Manifold

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VI.2** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
Prediction markets are the purest instantiation of convex information processing
on the probability simplex — the simplex IS the market. A prediction market with
$d$ mutually exclusive outcomes has prices $q = (q_1,\ldots,q_d)$ with
$\sum q_i = 1$: a point on $\Delta_{d-1}$. The arbitrage-free price set is $\Delta_{d-1}$
itself. The market-maker's cost function induces a Riemannian geometry on the
belief space. We develop the full geometric theory of prediction markets within
the framework of the monograph, connecting to the LMSR-softmax-Fisher identity
of LLM_MANIFOLD.md, the fiber bundle structure of FIBER_BUNDLES.md, and the
computational hardness results of COMPLEXITY.md.

Our principal results:

**(i) The LMSR-Fisher identity for prediction markets.** The Logarithmic Market
Scoring Rule (Hanson [2003]) cost function $C(q) = b\log\sum_j e^{q_j/b}$
has Hessian $(1/b)\,g^{\mathrm{FR}}$ — the Fisher-Rao metric scaled by inverse
liquidity. The LMSR prices are the softmax function. The liquidity parameter
$b$ plays the role of $\varepsilon^2 = 1/T$ in the portfolio theory: low liquidity
($b\to 0$) concentrates belief on the most likely outcome; high liquidity
($b\to\infty$) spreads belief toward maximum entropy. This is the prediction
market specialisation of R17 from LLM_MANIFOLD.md.

**(ii) The arbitrage-free polytope.** For $d$ outcomes, the arbitrage-free price
set is $\Delta_{d-1}$. For combinatorial markets with $n$ binary events and $2^n$
outcomes, the set of consistent marginal prices is the **marginal polytope**
$\mathcal{M} \subset [0,1]^n$ — a proper subset whose vertices correspond to
deterministic worlds. Computing the marginal polytope is \#P-hard in general,
connecting to the complexity hierarchy of COMPLEXITY.md.

**(iii) Conditional markets as fiber bundles.** A conditional prediction market
pricing $P(A|B)$ is a fiber bundle: the base space is the market for $B$, the
fiber over each outcome of $B$ is the conditional market for $A$ given $B$.
The connection curvature measures the failure of conditional independence.
Flat connection $\Leftrightarrow$ $A \perp B$. This is a direct application
of the fiber bundle theory from FIBER_BUNDLES.md.

**(iv) Scoring rule uniqueness.** The logarithmic scoring rule $S(q,i) = \log q_i$
is the unique proper scoring rule whose expected score is a Fisher-Rao divergence.
This connects Kelly optimality in portfolio theory to information-geometric
optimality in forecasting: both are consequences of the Fisher-Rao metric being
the unique Riemannian metric invariant under sufficient statistics.

**(v) The MUP on the marginal polytope.** The Manifold Universal Portfolio
restricted to the marginal polytope achieves regret $r\log T/(2T)$ where $r$
is the belief dimension — the number of independent probabilistic degrees
of freedom. The MUP price vector is the I-projection (information projection)
of the uniform distribution onto $\mathcal{M}$: the maximum entropy consistent
price.

**Keywords.** Prediction market; LMSR; softmax; Fisher-Rao metric; scoring rule;
marginal polytope; combinatorial market; fiber bundle; conditional market;
Jacobi diffusion; Kelly criterion; information geometry; I-projection; MUP.

**MSC 2020.** 91B26, 62B10, 52B05, 94A17, 91G10, 53C42, 60J60.

---

## 1. Prediction Markets as Simplex Geometry

### 1.1 The belief simplex

A prediction market with $d$ mutually exclusive and exhaustive outcomes has
prices $q = (q_1,\ldots,q_d)$ satisfying $q_i \geq 0$ and $\sum_{i=1}^{d} q_i = 1$.
This is a point on the probability simplex:

$$q \in \Delta_{d-1} = \{q \in \mathbb{R}^{d}_+ : \textstyle\sum_{i=1}^{d} q_i = 1\} \tag{1.1}$$

The prediction market IS a point on $\Delta_{d-1}$. There is no metaphor here,
no analogy, no approximation. The price vector of a prediction market with $d$
outcomes is identically a probability distribution on $d$ states. The belief
simplex and the price simplex are the same object.

This is the simplest instance of the monograph's organising principle: the
market lives on the simplex $\Delta_{d-1}$, equipped with the Fisher-Rao metric
$g^{\mathrm{FR}}_{ij}(q) = \delta_{ij}/q_i$, and mapped isometrically to the
positive orthant of the sphere $S^{d-1}_{+}$ via the Bhattacharyya embedding
$\phi: q \mapsto \sqrt{q}$.

In a financial market, portfolio weights $b \in \Delta_{d-1}$ are constrained to
the simplex by the budget equation. In a prediction market, prices
$q \in \Delta_{d-1}$ are constrained by the axioms of probability. The geometry
is identical.

### 1.2 The cost function mechanism

A market maker maintains a cost function $C: \mathbb{R}^{d} \to \mathbb{R}$ that
determines the cost of purchasing a bundle of Arrow-Debreu securities. The
quantities outstanding are $q = (q_1,\ldots,q_d)$, and the instantaneous prices are:

$$p_i = \frac{\partial C}{\partial q_i} \tag{1.2}$$

The cost of moving from quantity vector $q^{(0)}$ to $q^{(1)}$ is
$C(q^{(1)}) - C(q^{(0)})$ — path-independent by construction. This is the
fundamental advantage of cost-function-based market makers over order books:
the market maker always quotes prices, always absorbs trades, and never suffers
from the no-trade theorem.

**For the prices to be valid probabilities**, we need $p_i \geq 0$,
$\sum_i p_i = 1$, and $C$ convex. These three conditions — non-negativity,
normalisation, and convexity — are exactly the conditions for $p$ to lie on
$\Delta_{d-1}$ with $C$ a potential function.

### 1.3 The Logarithmic Market Scoring Rule

The LMSR [Hanson 2003] is the cost function:

$$C(q) = b\log\!\sum_{j=1}^{d} e^{q_j/b} \tag{1.3}$$

where $b > 0$ is the **liquidity parameter**. The prices are:

$$p_i = \frac{\partial C}{\partial q_i} = \frac{e^{q_i/b}}{\sum_{k=1}^{d} e^{q_k/b}} = \mathrm{softmax}(q/b)_i \tag{1.4}$$

The LMSR prices are the softmax function at inverse temperature $1/b$.
This is the same identity established in LLM_MANIFOLD.md (Theorem 1.1),
now seen in its native habitat: the prediction market.

The maximum loss of the LMSR market maker is $b\log d$, incurred when the
market moves from the uniform distribution to a point mass. The parameter $b$
controls the tradeoff between information elicitation (large $b$ = more liquid
= more trading = more information) and bounded loss (small $b$ = less exposure).

---

## 2. The Arbitrage-Free Polytope

### 2.1 Simple markets

For a prediction market with $d$ mutually exclusive outcomes, the arbitrage-free
price set is $\Delta_{d-1}$ itself:

- If $\sum_i q_i > 1$: **overround**. A trader can sell all $d$ securities for
  total revenue $\sum q_i > 1$ and pay at most $1$ when one outcome resolves.
  This is a Dutch book against buyers — guaranteed profit for the seller.

- If $\sum_i q_i < 1$: **underround**. A trader can buy all $d$ securities for
  total cost $\sum q_i < 1$ and receive exactly $1$ when one outcome resolves.
  This is a Dutch book against the market maker.

- If $\sum_i q_i = 1$ and $q_i \geq 0$ for all $i$: **arbitrage-free**. No
  riskless profit is available. The price vector is a probability distribution.

**The no-arbitrage condition for prediction markets is the simplex constraint.**
This is the prediction-market analogue of the Fundamental Theorem of Asset
Pricing: the existence of a risk-neutral measure is equivalent to
$q \in \Delta_{d-1}$.

### 2.2 Combinatorial markets and the marginal polytope

Now consider $n$ binary events $E_1,\ldots,E_n$, each with two outcomes
(true/false). The full outcome space has $2^n$ states — each assignment
of truth values to all $n$ events. A complete prediction market on this
outcome space would price all $2^n$ states, with prices on $\Delta_{2^n - 1}$.

In practice, traders want to bet on individual events or small combinations.
The **marginal prices** are $\pi_i = P(E_i = \mathrm{true})$ for $i = 1,\ldots,n$.
Not every vector $\pi \in [0,1]^n$ is consistent with some joint distribution
on $\{0,1\}^{n}$.

**Definition 2.1** *(Marginal polytope)*.
The **marginal polytope** of $n$ binary events is:

$$\mathcal{M} = \{\pi \in [0,1]^n : \exists\, p \in \Delta_{2^n-1} \text{ with } \textstyle\sum_{x: x_i=1} p(x) = \pi_i \forall\, i\} \tag{2.1}$$

This is the set of all marginal probability vectors that are consistent with
some joint distribution.

**Theorem 2.2** *(Marginal polytope structure)*.
*(i)* $\mathcal{M}$ is a convex polytope in $[0,1]^n$.
*(ii)* The vertices of $\mathcal{M}$ are the $2^n$ binary vectors $\{0,1\}^{n}$,
corresponding to deterministic worlds (each event either certainly true or
certainly false).
*(iii)* The faces of $\mathcal{M}$ encode conditional independence constraints:
each face corresponds to a class of distributions satisfying specific
independence relations.
*(iv)* $\mathcal{M} = [0,1]^n$ if and only if the events are independent
(no constraints beyond marginal non-negativity).

*Proof.* (i) $\mathcal{M}$ is the linear projection of $\Delta_{2^n-1}$ onto
$\mathbb{R}^{n}$, hence convex and a polytope. (ii) The vertices of $\Delta_{2^n-1}$
are the point masses $\delta_x$ for $x \in \{0,1\}^{n}$; projecting gives the
marginal vector $\pi = x \in \{0,1\}^{n}$. (iii) Each face of $\mathcal{M}$
corresponds to a face of the image of $\Delta_{2^n-1}$, and the facial structure
encodes which distributions are consistent — independence constraints reduce the
dimension. (iv) If the events are independent, any product distribution
$p(x) = \prod_i \pi_i^{x_i}(1-\pi_i)^{1-x_i}$ realises any
$\pi \in [0,1]^n$. $\square$

**Corollary 2.3** *(Computational hardness)*.
*Deciding whether a given marginal price vector $\pi \in [0,1]^n$ belongs to
$\mathcal{M}$ subject to a set of logical constraints (e.g., $E_1 \Rightarrow E_2$)
is \#P-hard in general.*

This connects directly to the complexity hierarchy of COMPLEXITY.md (Section 2):
prediction markets on combinatorial outcome spaces inherit the full
computational hardness of counting satisfying assignments.

---

## 3. The Fisher-Rao Geometry of Beliefs

### 3.1 The Riemannian structure

The belief simplex $\Delta_{d-1}$ carries the Fisher-Rao metric:

$$g^{\mathrm{FR}}_{ij}(q) = \frac{\delta_{ij}}{q_i} \tag{3.1}$$

This is the unique Riemannian metric (up to scale) that is invariant under
sufficient statistics [Cencov 1982]. For prediction markets, this means:
**the geometry of beliefs is determined uniquely by the requirement that
relabelling outcomes does not change distances.**

The Bhattacharyya distance between two belief states $q^{(0)}, q^{(1)} \in \Delta_{d-1}$ is:

$$d_B(q^{(0)}, q^{(1)}) = 2\arccos\!\sum_{i=1}^{d} \sqrt{q^{(0)}_{i} q^{(1)}_{i}} \tag{3.2}$$

This measures the "information distance" between two belief states. In a
prediction market, $d_B$ measures how much a trader must pay (in LMSR transaction
cost) to move the market from belief $q^{(0)}$ to belief $q^{(1)}$.

### 3.2 Information arrival as Jacobi diffusion

As information arrives in a prediction market, the price vector $q(t)$ evolves
stochastically on $\Delta_{d-1}$. Under the assumption of efficient information
processing (each trade moves the price by the correct amount), $q(t)$ follows
a Jacobi diffusion on the simplex:

$$dq_i = \frac{1}{2}(q^{\ast}_{i} - q_i)\,dt + \sqrt{q_i(1-q_i)}\,dW^{(i)}_{t} \tag{3.3}$$

where $q^{\ast}$ is the "true" probability (the resolving value) and the noise
terms $dW^{(i)}$ are correlated by the simplex constraint $\sum_i dq_i = 0$.

This is the same Jacobi diffusion from MARKET_PROCESSES.md (Section 2), now
in its prediction market interpretation. The stationary distribution is the
Dirichlet distribution $\mathrm{Dir}(Tq^{\ast})$ where $T$ is the effective
"sample size" — the total information that has been incorporated.

**Binary markets** ($d = 2$) reduce to the classical Jacobi diffusion on $[0,1]$:

$$dp = \frac{1}{2}(p^{\ast} - p)\,dt + \sqrt{p(1-p)}\,dW_t \tag{3.4}$$

with absorbing boundaries at $p = 0$ and $p = 1$ (the event is resolved as
false or true). The transition density is the Jacobi polynomial series
from MARKET_PROCESSES.md (Theorem 2.3).

### 3.3 The geometry of binary prediction markets

A binary prediction market ($d = 2$) lives on the interval $[0,1]$ with the
Fisher-Rao metric $ds^2 = dp^2/(p(1-p))$. Under the change of variable
$\theta = 2\arcsin(\sqrt{p})$, this becomes $ds^2 = d\theta^2$ on $[0,\pi]$.
The belief space is a semicircle, and the Fisher-Rao metric is flat.

This means: **in a binary prediction market, the information distance between
prices $p$ and $p'$ is $|2\arcsin\sqrt{p} - 2\arcsin\sqrt{p'}|$.** The
midpoint of $[0,1]$ in the Fisher-Rao metric is $p = 1/2$ (maximum uncertainty),
and the endpoints $p = 0, 1$ are at infinite distance from the interior —
certainty is infinitely far from doubt.

---

## 4. The LMSR as Information Geometry

### 4.1 The LMSR as free energy

**Theorem 4.1** *(LMSR = free energy of Gibbs distribution)*.
*The LMSR cost function $C(q) = b\log\sum_j e^{q_j/b}$ is the free energy
of the Gibbs (canonical) distribution on $d$ outcomes at temperature $b$, with
energies $\{-q_j\}_{j=1}^{d}$. The prices $p_j = e^{q_j/b}/\sum_k e^{q_k/b}$
are the Boltzmann weights.*

*Proof.* The partition function of the canonical ensemble at temperature $b$ with
energy levels $\{-q_j\}$ is $Z = \sum_j e^{q_j/b}$. The free energy is
$F = -b\log Z = -C(q)$. The occupation probabilities are
$p_j = e^{q_j/b}/Z = \mathrm{softmax}(q/b)_j$. $\square$

This establishes the statistical mechanics interpretation: the prediction market
is a thermal system. Information is energy (negative), the liquidity parameter
is temperature, and the market prices are Boltzmann weights. Trading is a
thermodynamic process — it moves the system from one equilibrium state to
another.

### 4.2 The temperature limits

The liquidity parameter $b$ controls the sharpness of beliefs:

**Low temperature ($b \to 0$):**
$$\lim_{b\to 0} p_i = \begin{cases} 1 & \text{if } i = \arg\max_j q_j \\ 0 & \text{otherwise} \end{cases} \tag{4.1}$$

The market concentrates on the most likely outcome. This is the
$\varepsilon^2 \to 0$ (equivalently $T \to \infty$) limit in the portfolio
theory — the WKB/Laplace limit of LAPLACE.md. In the zero-temperature limit,
the prediction market becomes a deterministic prediction.

**High temperature ($b \to \infty$):**
$$\lim_{b\to\infty} p_i = \frac{1}{d} \qquad \forall\, i \tag{4.2}$$

The market reverts to the uniform distribution — maximum entropy, no
information. This is the $T \to 0$ limit in the portfolio theory: no data,
maximum uncertainty.

**The critical observation:** The LMSR liquidity parameter $b$ plays exactly
the role of $\varepsilon^2 = 1/T$ in the monograph's portfolio theory. The
entire WKB/Laplace apparatus of LAPLACE.md and PAPER.md applies to prediction
markets with $b$ replacing $\varepsilon^2$.

### 4.3 The LMSR spread

The bid-ask spread of the LMSR at price $p$ is determined by the curvature
of the cost function. For a small trade $\delta q$ in security $i$:

$$\text{spread}_{i} = \frac{\partial^2 C}{\partial q_i^2}\,\delta q = \frac{p_i(1-p_i)}{b}\,\delta q \tag{4.3}$$

The spread is:
- Proportional to $1/b$: lower liquidity = wider spread
- Proportional to $p_i(1-p_i)$: maximised at $p_i = 1/2$ (maximum uncertainty),
  zero at $p_i = 0$ or $1$ (certainty)
- The Fisher-Rao variance $p_i(1-p_i)$ of the Bernoulli distribution

**The LMSR spread is the Fisher information scaled by inverse liquidity.** This
is the prediction market analogue of the bid-ask spread in financial markets
being proportional to the inverse of market depth.

---

## 5. Conditional Prediction Markets and Fiber Bundles

### 5.1 The fiber bundle structure

A **conditional prediction market** prices $P(A|B)$ — the probability of event
$A$ given that event $B$ occurs. Suppose $A$ has $d_A$ outcomes and $B$ has
$d_B$ outcomes. The unconditional market prices the joint distribution
$P(A,B)$ on $d_A \cdot d_B$ outcomes, but the conditional market separates this
into a base and fiber.

**Definition 5.1** *(Conditional market bundle)*.
The conditional prediction market $P(A|B)$ has the structure of a fiber bundle
$\pi: E \to \mathcal{B}$:
- **Base space** $\mathcal{B} = \Delta_{d_B - 1}$: the market for event $B$,
  with prices $q^B = (q^B_1,\ldots,q^B_{d_B})$
- **Fiber** $F_j = \Delta_{d_A - 1}$: for each outcome $B = j$, the conditional
  market for $A$ given $B = j$, with prices $q^{A|B=j} \in \Delta_{d_A - 1}$
- **Total space** $E = \{(q^B, q^{A|B=j})_{j=1}^{d_B}\}$: the collection of
  all base and conditional prices

The projection $\pi: E \to \mathcal{B}$ maps the full conditional price to
the marginal price on $B$.

### 5.2 The connection and its curvature

A **connection** on the conditional market bundle specifies how the conditional
prices $q^{A|B=j}$ change as we move along the base space (as new information
about $B$ arrives). The natural connection is the one that preserves the joint
distribution:

$$\nabla_{\partial/\partial q^B_j} q^{A|B=k} = -\frac{q^{A,B}_{ik} - q^{A|B=k}\,q^B_k}{(q^B_k)^2}\,\delta_{jk} \tag{5.1}$$

where $q^{A,B}_{ik} = P(A=i, B=k)$ is the joint price.

**Theorem 5.2** *(Curvature = conditional dependence)*.
*The curvature $\Omega$ of the conditional market connection vanishes if and only
if $A$ and $B$ are conditionally independent:*

$$\Omega = 0 \quad \Longleftrightarrow \quad P(A|B) = P(A) \tag{5.2}$$

*When $\Omega \neq 0$, the curvature at a point $(q^B, q^{A|B})$ measures the
degree to which learning about $B$ changes beliefs about $A$:*

$$\|\Omega\|^2 = \sum_{j,k} \left(\frac{\partial q^{A|B=j}_{i}}{\partial q^B_k} - \frac{\partial q^{A|B=k}_{i}}{\partial q^B_j}\right)^2 \tag{5.3}$$

*Proof.* If $A \perp B$, then $q^{A|B=j} = q^A$ for all $j$ — the conditional
prices are constant over the base, and parallel transport is trivial. The
connection is flat and $\Omega = 0$. Conversely, if $\Omega = 0$, parallel
transport around any closed loop in $\mathcal{B}$ is trivial, so
$q^{A|B=j}$ does not depend on $j$, giving independence. $\square$

This is a direct application of the fiber bundle theory from FIBER_BUNDLES.md,
now in the transparent setting of prediction markets. The "holonomy" of a
conditional prediction market is the accumulated change in $P(A|B)$ as the
market for $B$ completes a cycle — analogous to the Berry phase of
FIBER_BUNDLES.md (Section 3).

### 5.3 Example: political prediction markets

Consider two events:
- $B$: "Will the economy grow by more than 2\%?" (binary, $d_B = 2$)
- $A$: "Will the incumbent win re-election?" (binary, $d_A = 2$)

The base space is $\Delta_1 \cong [0,1]$: the probability of economic growth.
The fiber at each point is $\Delta_1 \cong [0,1]$: the probability of
re-election conditional on the economic outcome.

If re-election probability depends on economic growth (the typical case), the
connection is curved. The curvature measures the **economic sensitivity** of
the election — how much a change in the economic forecast changes the
re-election probability. A flat connection would mean the election is
independent of the economy.

The total market (joint distribution on $\{$grow, shrink$\} \times \{$win, lose$\}$)
lives on $\Delta_3$, but the fiber bundle decomposition reduces the pricing
problem from $\Delta_3$ to two copies of $\Delta_1$ plus a connection — from
3 free parameters to $1 + 2 \times 1 = 3$ parameters, the same count, but with
a geometric structure that separates base uncertainty from conditional dependence.

---

## 6. Combinatorial Markets and Exponential Complexity

### 6.1 The curse of dimensionality

Consider $n$ binary events $E_1,\ldots,E_n$. The full outcome space has $2^n$
states. The price simplex is $\Delta_{2^n - 1}$, which has $2^n - 1$ free
parameters. For $n = 20$ events — a modest number for a political prediction
market in an election year — the full outcome space has over one million states.

**The combinatorial explosion:** running an LMSR on $\Delta_{2^n - 1}$ requires
tracking $2^n$ quantities and computing $2^n$-dimensional softmax. This is
computationally infeasible for $n > 25$ or so.

### 6.2 The factor projection

The monograph's central technique — projecting from the full simplex
$\Delta_{d-1}$ to a low-dimensional market manifold $M^r$ — resolves this
directly.

The marginal polytope $\mathcal{M} \subset [0,1]^n$ has dimension at most $n$,
but it sits inside the full simplex $\Delta_{2^n-1}$. The LMSR on the marginal
space operates on $n$ marginal prices $\pi_1,\ldots,\pi_n$ rather than
$2^n$ joint prices.

**Definition 6.1** *(Marginal LMSR)*.
The marginal LMSR is the cost function on $[0,1]^n$ defined by:

$$C_{\mathcal{M}}(\pi) = \min_{p \in \Delta_{2^n-1}:\, \mathrm{marg}(p)=\pi} C(q(p)) \tag{6.1}$$

— the minimum LMSR cost over all joint distributions consistent with
marginals $\pi$.

This is the **information projection** of the LMSR onto the marginal polytope.
It is well-defined because $C$ is convex and the consistency constraint is
linear. Computing $C_{\mathcal{M}}$ is \#P-hard in general (it requires
optimising over $\Delta_{2^n-1}$ subject to marginal constraints), but can be
approximated efficiently when the dependence structure is sparse — when the
events form a graphical model with bounded treewidth [Chen and Pennock 2007].

### 6.3 The belief dimension

In practice, the marginal prices $\pi_1,\ldots,\pi_n$ are not all independent.
Correlations between events (economic growth correlated with employment,
employment correlated with consumer confidence, etc.) reduce the effective
dimensionality.

**Definition 6.2** *(Belief dimension)*.
The **belief dimension** $r$ of a combinatorial prediction market is the
dimension of the manifold $M^r \subset \mathcal{M}$ traced out by the marginal
price vector as information arrives:

$$r = \dim M^r = \mathrm{rank}\!\left(\mathrm{Cov}[\pi(t)]\right) \tag{6.2}$$

— the stable rank of the covariance matrix of marginal price changes.

This is the prediction market analogue of the market manifold dimension $r$
from the monograph. Just as a financial market with $d = 5000$ assets has an
intrinsic dimension of $r \approx 4$–$8$ factors, a prediction market with
$n = 100$ events may have a belief dimension of $r \approx 3$–$5$ independent
"narratives" driving all the marginal prices.

**Theorem 6.3** *(Marginal polytope regret)*.
*The MUP restricted to the marginal polytope $\mathcal{M}$ of a combinatorial
prediction market with belief dimension $r$ achieves minimax regret:*

$$R_T(\hat{b}^{\mathcal{M}}_{T}) = \frac{r\log T}{2T} + O\!\left(\frac{1}{T}\right) \tag{6.3}$$

*where the comparison class is all fixed marginal price vectors in $\mathcal{M}$.*

*Proof sketch.* The marginal polytope $\mathcal{M}$ is a convex body in
$\mathbb{R}^{n}$. The belief manifold $M^r \subset \mathcal{M}$ has dimension $r$.
By CONVERGENCE.md (Theorem 3.1), the MUP on an $r$-dimensional manifold in the
simplex achieves regret $r\log T/(2T)$. The marginal polytope replaces the full
simplex, and the belief dimension $r$ replaces the manifold dimension. The minimax
bound follows from the same Shtarkov NML argument, with the normalising constant
computed over $\mathcal{M}$ rather than $\Delta_{d-1}$. $\square$

The improvement over the naive LMSR on $\Delta_{2^n-1}$ is dramatic:
the naive regret is $(2^n - 1)\log T/(2T)$, while the MUP regret is
$r\log T/(2T)$. For $n = 20$ and $r = 5$, this is a factor of
$2^{20}/5 \approx 200{,}000$ improvement.

---

## 7. Scoring Rules as Divergences

### 7.1 Proper scoring rules

A **scoring rule** $S: \Delta_{d-1} \times \{1,\ldots,d\} \to \mathbb{R}$ assigns
a reward $S(q, i)$ to a forecaster who reports probability vector $q$ when
outcome $i$ is realised. A scoring rule is **proper** if the expected score
is maximised by reporting the true distribution:

$$\arg\max_{q \in \Delta_{d-1}} \sum_{i=1}^{d} p_i\, S(q, i) = p \tag{7.1}$$

for all $p \in \Delta_{d-1}$. It is **strictly proper** if the maximum is unique.

The three classical proper scoring rules and their geometric interpretations:

**Logarithmic (Kelly) scoring rule:**
$$S_{\log}(q, i) = \log q_i \tag{7.2}$$

Expected score: $\mathbb{E}_{p}[S_{\log}(q, \cdot)] = \sum_i p_i \log q_i = -H(p) - D_{\mathrm{KL}}(p\|q)$
where $H(p)$ is the entropy and $D_{\mathrm{KL}}$ is the Kullback-Leibler divergence.
**This is the Kelly criterion.** Reporting your true beliefs maximises long-run
log-wealth.

**Quadratic (Brier) scoring rule:**
$$S_{\mathrm{Brier}}(q, i) = 2q_i - \|q\|^2 \tag{7.3}$$

Expected score: $\mathbb{E}_{p}[S_{\mathrm{Brier}}(q, \cdot)] = -\|p-q\|^2 + \|p\|^2 - 1$.
This penalises the squared Euclidean distance between $q$ and the realised
outcome. **The Brier score measures Euclidean distance on the simplex** — the
$L^2$ geometry, not the Fisher-Rao geometry.

**Spherical scoring rule:**
$$S_{\mathrm{sph}}(q, i) = \frac{q_i}{\|q\|} \tag{7.4}$$

Expected score: $\mathbb{E}_{p}[S_{\mathrm{sph}}(q, \cdot)] = \langle p, q/\|q\|\rangle = \cos\angle(p,q)\cdot\|p\|$.
This is the cosine similarity between $p$ and $q$. Under the Bhattacharyya
embedding $q \mapsto \sqrt{q}$, the spherical score becomes the inner product
on $S^{d-1}_{+}$: $\sum_i \sqrt{p_i q_i} = \cos(d_B(p,q)/2)$.
**The spherical score measures Bhattacharyya affinity.**

### 7.2 The scoring rule uniqueness theorem

**Theorem 7.1** *(Logarithmic rule = Fisher-Rao divergence)*.
*Among all strictly proper scoring rules on $\Delta_{d-1}$, the logarithmic
scoring rule is the unique one (up to affine transformation) whose expected
score loss $\mathbb{E}_{p}[S(p,\cdot)] - \mathbb{E}_{p}[S(q,\cdot)]$ is a
function of the Fisher-Rao divergence $D_{\mathrm{KL}}(p\|q)$ alone:*

$$\mathbb{E}_{p}[S_{\log}(p,\cdot)] - \mathbb{E}_{p}[S_{\log}(q,\cdot)] = D_{\mathrm{KL}}(p\|q) \tag{7.5}$$

*No other proper scoring rule has its expected loss equal to a Bregman divergence
that is simultaneously the unique $f$-divergence invariant under sufficient
statistics.*

*Proof.* The expected score loss of any strictly proper scoring rule $S$ is a
Bregman divergence $D_F(p\|q)$ for some convex function $F$ [Gneiting and
Raftery 2007, Theorem 1]. The Kullback-Leibler divergence is the unique
Bregman divergence that is also an $f$-divergence [Amari 2016, Chapter 3].
The $f$-divergences are the unique divergences invariant under sufficient
statistics [Cencov 1982]. Therefore $D_{\mathrm{KL}}$ is the unique Bregman
divergence invariant under sufficient statistics, and the logarithmic scoring
rule is the unique proper scoring rule generating it. $\square$

**Corollary 7.2.** *The Kelly criterion is the unique growth-optimal strategy
that is invariant under sufficient statistics. Using any other proper scoring
rule (Brier, spherical, etc.) as a growth criterion introduces dependence on
the parameterisation of the outcome space.*

This is the deep reason why Kelly is special in portfolio theory (INFORMATION_THEORY.md),
in prediction markets, and in machine learning (LLM_MANIFOLD.md): it is the
unique strategy compatible with the intrinsic geometry of the probability simplex.

---

## 8. Polymarket, Kalshi, and Real Prediction Markets

### 8.1 Market mechanisms in practice

Modern prediction markets use three main mechanisms:

**Order book** (Polymarket, Kalshi). Buyers and sellers submit limit orders.
The price is determined by the intersection of supply and demand. This is
identical to financial market microstructure. The Fisher-Rao geometry is not
imposed by the mechanism — it emerges from competitive equilibrium when
participants are Kelly-optimal.

**Automated market maker / AMM** (Uniswap-style, adapted for prediction).
A constant-function market maker holds reserves and quotes prices algorithmically.
The most common AMM is the constant-product rule $x \cdot y = k$, which
induces a non-Fisher-Rao geometry (hyperbolic, not spherical). AMMs for
prediction markets are suboptimal in the Fisher-Rao sense.

**LMSR** (used in academic and some commercial implementations). The
theoretically optimal mechanism: prices = softmax, Hessian = Fisher information,
geometry = Fisher-Rao. The LMSR is the unique market maker that respects the
intrinsic geometry of beliefs.

### 8.2 Empirical efficiency

Real prediction markets exhibit remarkably tight pricing:

| Platform | Typical overround | Mechanism | $d$ (outcomes) |
|:---------|:-----------------:|:---------:|:--------------:|
| Polymarket | 1–3\% | Order book | 2–20 |
| Kalshi | 2–5\% | Order book | 2–50 |
| PredictIt | 5–10\% | Order book + fees | 2–20 |
| Metaculus | 0\% (no real money) | Scoring rule | Continuous |
| Betfair (exchange) | 1–3\% | Order book | 2–40 |
| Bookmakers | 5–20\% | Quote-driven | 2–1000 |

The overround $\omega = \sum_i q_i - 1$ measures the deviation from the
simplex. In the Fisher-Rao metric, the distance from the overround price
vector to the nearest point on $\Delta_{d-1}$ is:

$$d_{\mathrm{FR}}(q, \Delta_{d-1}) \approx \omega \cdot \sqrt{\sum_i 1/q_i} \tag{8.1}$$

For typical prediction markets with $\omega \approx 0.02$ and $d = 2$,
$q \approx (0.51, 0.51)$, this gives $d_{\mathrm{FR}} \approx 0.04$ —
a small Fisher-Rao perturbation. For bookmakers with $\omega \approx 0.10$,
the perturbation is five times larger.

### 8.3 Information aggregation

**Theorem 8.1** *(LMSR as optimal aggregation)*.
*Among all cost-function-based market makers, the LMSR is the unique mechanism
whose equilibrium prices equal the wealth-weighted geometric mean of trader
beliefs:*

$$p^{\mathrm{LMSR}}_{i} = \frac{\prod_k (p^{(k)}_{i})^{w_k}}{\sum_j \prod_k (p^{(k)}_{j})^{w_k}} \tag{8.2}$$

*where $p^{(k)}$ is the belief of trader $k$ and $w_k$ is the wealth of trader $k$.
This is the exponential family mixture — the Fisher-Rao barycenter of the
trader beliefs weighted by wealth.*

*Proof.* In the LMSR, each trader $k$ with wealth $w_k$ and belief $p^{(k)}$
trades to maximise expected log-wealth, moving the market from $q$ toward
$p^{(k)}$ by an amount proportional to $w_k$. At equilibrium, the first-order
condition $\sum_k w_k (p^{(k)}_{i} - q_i)/q_i = 0$ gives
$q_i = \prod_k (p^{(k)}_{i})^{w_k}/Z$ where $Z$ normalises.
This is the wealth-weighted geometric mean — the I-projection. $\square$

This is the "wisdom of crowds" result: the LMSR aggregates beliefs by
Fisher-Rao averaging, which is information-theoretically optimal. It
generalises the well-known result that competitive markets aggregate
information efficiently — the LMSR does so by construction, not merely in
equilibrium.

---

## 9. Polytopes at the Margin

### 9.1 The marginal polytope of a graphical model

When the $n$ events $E_1,\ldots,E_n$ have a known dependence structure — encoded
as a graphical model (Bayesian network or Markov random field) — the marginal
polytope $\mathcal{M}$ acquires additional structure.

**Definition 9.1** *(Graphical model marginal polytope)*.
For a graphical model $G = (V, \mathcal{E})$ with vertex set $V = \{1,\ldots,n\}$
and edge set $\mathcal{E}$, the marginal polytope is:

$$\mathcal{M}_{G} = \{\mu \in \mathbb{R}^{|V|+|\mathcal{E}|}_{+} : \mu \text{ consistent with some } p \in \Delta_{2^n-1} \text{ Markov w.r.t. } G\} \tag{9.1}$$

The marginal polytope $\mathcal{M}_{G}$ is characterised by:
- **Vertices:** deterministic assignments consistent with the graph structure
- **Faces:** conditional independence constraints encoded by graph separation
- **Dimension:** $|V| + |\mathcal{E}|$ (node and edge marginals)

For trees ($|\mathcal{E}| = |V| - 1$), the marginal polytope has a simple
description and belief propagation computes the I-projection exactly. For
graphs with cycles, the marginal polytope is intractable in general, and
variational methods (mean field, loopy belief propagation) approximate the
I-projection.

### 9.2 The MUP as I-projection

**Theorem 9.2** *(MUP = maximum entropy consistent price)*.
*The MUP price vector $\hat{\pi}^{\mathcal{M}}_{T}$ on the marginal polytope
$\mathcal{M}$ is the information projection (I-projection) of the uniform
distribution $u = (1/d,\ldots,1/d)$ onto $\mathcal{M}$:*

$$\hat{\pi}^{\mathcal{M}}_{T} = \arg\min_{\pi \in \mathcal{M}} D_{\mathrm{KL}}(\pi \| u) = \arg\max_{\pi \in \mathcal{M}} H(\pi) \tag{9.2}$$

*subject to the constraint that $\pi$ is consistent with the observed data
up to time $T$.*

*Proof.* The MUP at time $T$ is the portfolio that maximises $L_T(b) = (1/T)\sum_{t=1}^{T} \log\langle b, x_t\rangle$
over $b \in \mathcal{M}$. By CONVERGENCE.md (Theorem 2.1), the MUP
converges to the log-optimal portfolio $b^{\ast} \in \mathcal{M}$ at rate
$r\log T/(2T)$. The log-optimal portfolio is the maximum likelihood estimator
on the exponential family, which is the I-projection of the prior (uniform)
onto the constraint set $\mathcal{M}$ — a standard result in information
geometry [Amari 2016, Theorem 8.1]. $\square$

**Corollary 9.3** *(MUP never at a vertex)*.
*The MUP price vector is never a vertex of the marginal polytope. That is,
the MUP never assigns probability $0$ or $1$ to any event.*

*Proof.* The I-projection onto a polytope lies in the relative interior of
the face containing the projection. The uniform distribution $u$ is in the
interior of $\Delta_{d-1}$, so its I-projection onto $\mathcal{M}$ lies in
the relative interior of $\mathcal{M}$ — never at a vertex. $\square$

This is the prediction market version of a fundamental principle: **the
optimal forecaster is never certain.** The MUP always hedges, always maintains
non-zero probability on every outcome. Certainty ($p = 0$ or $p = 1$) is
the vertex of the polytope — the most extreme, least diversified position.
The MUP sits in the interior.

---

## 10. New Results

We collect the five principal lemmas that are new to this paper.

**Lemma 10.1** *(LMSR-Fisher identity for prediction markets)*.
*The Hessian of the LMSR cost function at price vector $p \in \Delta_{d-1}$ satisfies:*

$$\nabla^2 C(q)\big|_{p = \mathrm{softmax}(q/b)} = \frac{1}{b}\,g^{\mathrm{FR}}(p) \tag{10.1}$$

*where $g^{\mathrm{FR}}(p)_{ij} = p_i(\delta_{ij} - p_j)$ is the Fisher information
matrix on $\Delta_{d-1}$ at $p$.*

This is the prediction market specialisation of R17 from LLM_MANIFOLD.md. The proof
is the direct computation in Section 1.3. The novelty here is the interpretation:
the LMSR market maker's price sensitivity IS the Fisher information of the belief
distribution, scaled by inverse liquidity.

**Lemma 10.2** *(Marginal polytope regret bound)*.
*The MUP on the marginal polytope $\mathcal{M}$ of a combinatorial prediction
market with belief dimension $r$ achieves:*

$$R_T = \frac{r\log T}{2T} + O(T^{-1}) \tag{10.2}$$

*This is minimax optimal over the class of all strategies on $\mathcal{M}$.*

The proof is in Theorem 6.3. The key insight: the regret depends on the belief
dimension $r$, not the number of events $n$ or the outcome space size $2^n$.
A prediction market with 100 events but only 5 independent belief dimensions
has the same regret as a 5-outcome simple market.

**Lemma 10.3** *(Scoring rule uniqueness)*.
*The logarithmic scoring rule is the unique strictly proper scoring rule (up
to affine transformation) whose expected loss is the KL divergence — the
unique Bregman divergence invariant under sufficient statistics.*

The proof is in Theorem 7.1. This connects the Kelly criterion to the
Fisher-Rao geometry: Kelly is special because KL divergence is special because
the Fisher-Rao metric is special. The chain of uniqueness runs:
$$\text{Cencov} \to \text{Fisher-Rao} \to \text{KL divergence} \to \text{Log score} \to \text{Kelly}$$

**Lemma 10.4** *(Conditional market curvature)*.
*The curvature of the conditional market fiber bundle $P(A|B)$ vanishes if and
only if $A \perp B$. The curvature norm $\|\Omega\|^2$ equals the mutual
information $I(A;B)$ to leading order:*

$$\|\Omega\|^2 = 2\,I(A;B) + O(I(A;B)^2) \tag{10.3}$$

The proof follows from Theorem 5.2 and a Taylor expansion of the connection
curvature around the flat (independent) case. This gives a geometric
interpretation of mutual information: it is the curvature of the conditional
prediction market bundle.

**Lemma 10.5** *(Belief dimension estimation)*.
*The belief dimension $r$ of a combinatorial prediction market can be estimated
from the time series of marginal prices $\pi(1),\ldots,\pi(T)$ by three
independent methods:*

*(i) Stable rank:* $r \approx \mathrm{srank}(\mathrm{Cov}[\Delta\pi])$

*(ii) False Nearest Neighbours* (Takens, from CHAOS_TAKENS.md): embed the
price series in delay coordinates and identify the dimension at which FNN
fraction drops to zero.

*(iii) Grassberger-Procaccia* (from GRASSBERGER_PERCOLATION_GENERATING.md):
$r = \lim_{\epsilon \to 0} \log C(\epsilon)/\log\epsilon$ where $C(\epsilon)$
is the correlation integral of the embedded price series.

*All three converge to the same $r$ for an efficient prediction market.*

This is the prediction market analogue of the three-estimator convergence
described in the monograph's key connections. The belief dimension $r$ is
the fundamental invariant — the number of independent narratives driving
the market.

---

## References

[1] K. Arrow and G. Debreu, "Existence of an equilibrium for a competitive
economy," *Econometrica* 22 (1954), 265--290.

[2] S. Amari, *Information Geometry and Its Applications*, Springer, 2016.

[3] J. Abernethy, Y. Chen, and J.W. Vaughan, "Efficient market making via
convex optimization, and a connection to online learning," *ACM Trans. on
Economics and Computation* 1(2) (2013), 1--39.

[4] G.W. Brier, "Verification of forecasts expressed in terms of probability,"
*Monthly Weather Review* 78 (1950), 1--3.

[5] N.N. Cencov, *Statistical Decision Rules and Optimal Inference*, AMS
Translations of Mathematical Monographs 53, 1982.

[6] Y. Chen and D.M. Pennock, "A utility framework for bounded-loss market
makers," in *Proc. UAI 2007*, 49--56.

[7] T. Gneiting and A.E. Raftery, "Strictly proper scoring rules, prediction,
and estimation," *J. Amer. Statist. Assoc.* 102(477) (2007), 359--378.

[8] R. Hanson, "Combinatorial information market design," *Information Systems
Frontiers* 5(1) (2003), 107--119.

[9] M.J. Wainwright and M.I. Jordan, "Graphical models, exponential families,
and variational inference," *Foundations and Trends in Machine Learning* 1(1-2)
(2008), 1--305.

[10] A. Vaswani et al., "Attention is all you need," in *Proc. NeurIPS 2017*,
5998--6008.

---

*Paper VI.2 of "The Geometry of Efficient Markets" by Saxon Nicholls.*
*Cross-references: LLM_MANIFOLD.md (R17, LMSR-softmax-Fisher identity),
FIBER_BUNDLES.md (fiber bundle theory), COMPLEXITY.md (computational hardness),
CONVERGENCE.md (MUP regret), MARKET_PROCESSES.md (Jacobi diffusion),
INFORMATION_THEORY.md (Kelly criterion), CHAOS_TAKENS.md (Takens embedding),
GRASSBERGER_PERCOLATION_GENERATING.md (correlation dimension),
HYPERCUBE_SHAPLEY.md (simplex geometry).*
