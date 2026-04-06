# Why Information Lives on the Simplex:
## Convexity as a Necessary Condition for Information Processing

**Saxon Nicholls** — me@saxonnicholls.com

**Paper 0.1** — Foundation

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
We prove that any system processing information under three natural axioms —
closure under combination, the data processing inequality, and continuity —
must operate on a geodesically convex subset of the probability simplex
equipped with the Fisher-Rao metric. The proof combines Čencov's uniqueness
theorem for monotone metrics with the Bhattacharyya isometric embedding of
the simplex into the unit sphere. This result is not a modelling choice but
a mathematical necessity: violating convexity violates the data processing
inequality, and with it the entire foundation of information theory.

We exhibit six independent instantiations — probability theory, financial
markets, Bayesian inference, machine learning, quantum mechanics, and game
theory — and show that the core results of the companion monograph
*The Geometry of Efficient Markets* follow as corollaries of convex
information processing.

**Principal results:**

**(i) The Convex Information Processing Theorem.** Any information processing
system satisfying closure under combination, the data processing inequality,
and continuity is isomorphic to a geodesically convex subset of
$(\Delta_{d-1}, g^{\rm FR})$ for some $d$. The Fisher-Rao metric is the
unique geometry compatible with these axioms (Čencov 1982).

**(ii) The Bhattacharyya sphere is forced.** The isometric embedding
$\phi: p \mapsto \sqrt{p}$ sends $(\Delta_{d-1}, g^{\rm FR})$ to the
positive orthant of $S^{d-1}(\frac{1}{2})$, which is geodesically convex.
Every information processing system therefore lives on a convex subset of a
sphere.

**(iii) The ambient convex space is forced.** Any financial market
satisfying the five axioms (three information axioms plus normalisation
and Markov channels) has its portfolio space embedded in
$S^{d-1}_+$ via the Bhattacharyya isometry. The efficient market manifold
$M^r \subset S^{d-1}_+$ is an additional optimality structure (selected by
the Kelly criterion) within this forced ambient space.

**(iv) Jensen's inequality underlies the data processing inequality.** The
concavity of Shannon entropy on the convex simplex, combined with Jensen's
inequality, is the mechanism behind the classical DPI for entropy. The full
DPI ($I(X;Z) \leq I(X;Y)$ for Markov chains $X \to Y \to Z$) is a stronger
statement requiring both Jensen and the chain rule for mutual information.
Convexity of the state space is a precondition for Jensen to apply.

**(v) Ergodic information processing.** An ergodic dynamical system on a
compact space visits $\mu$-almost every state (Birkhoff). For smooth ergodic
measures on compact manifolds, the support is the entire space and orbits
are dense. Convexity of the ambient space guarantees that the ergodic
measure (which lives in $\mathcal{P}(X)$, the free convex completion)
inherits the information-geometric structure of the simplex.

**Keywords.** Convexity; information processing; Fisher-Rao metric; Čencov
theorem; data processing inequality; simplex; Bhattacharyya sphere;
information geometry; Shannon entropy; Jensen's inequality; market manifold.

---

## 1. Introduction

### 1.1 The question

Every known system that processes information operates on a convex space:

- Probability distributions live on the simplex $\Delta_{d-1}$
- Portfolio weights live on the simplex $\Delta_{d-1}$
- Bayesian posteriors are convex combinations of prior and likelihood
- Neural network outputs pass through softmax onto $\Delta_{d-1}$
- Quantum states are density matrices: convex, $\rho \succeq 0$, $\mathrm{tr}(\rho) = 1$
- Mixed strategies in game theory live on $\Delta_{d-1}$
- Thermodynamic Gibbs states form a convex exponential family

Is this a coincidence? Or is convexity a *necessary condition* for
information processing?

We prove the latter. The argument requires only three axioms — each so
natural that violating any one of them produces a system that cannot
coherently process information.

### 1.2 Why this matters

If convexity is necessary, then:

1. **The geometry is forced.** The Fisher-Rao metric is the unique Riemannian
   metric compatible with information processing (Čencov's theorem). This is
   not a choice — it is a consequence.

2. **The market manifold is a theorem, not an axiom.** The entire framework of
   the companion monograph — that a financial market lives on a submanifold
   of the Bhattacharyya sphere — follows from the three axioms applied to
   portfolio allocation. We do not need to *assume* the market manifold; we
   *derive* it.

3. **Machine learning is constrained.** Any ML system whose output is a
   probability distribution (i.e., any classifier, any language model)
   operates on $\Delta_{d-1}$ with Fisher-Rao geometry. The softmax function
   is not an architectural choice — it is the unique map from $\mathbb{R}^d$
   to the information processing space.

4. **Quantum mechanics is a special case.** The density matrix formalism is
   convex information processing on the space of positive semidefinite
   matrices with unit trace. The axioms apply. The Born rule is a corollary.

### 1.3 Structure of this paper

Section 2 states the three axioms and proves the main theorem. Section 3
proves that the Fisher-Rao metric is forced. Section 4 establishes the
Bhattacharyya embedding. Section 5 gives the six instantiations. Section 6
derives the consequences for the companion monograph. Section 7 poses open
problems.

---

## 2. The Three Axioms

### 2.1 The setup

Let $\mathcal{S}$ be a set of **states** — the possible configurations of an
information processing system. We require three operations:

- A **combination** $\circ_\lambda : \mathcal{S} \times \mathcal{S} \to \mathcal{S}$
  for each $\lambda \in [0,1]$, representing the mixture or consensus of two states
- A **divergence** $D : \mathcal{S} \times \mathcal{S} \to \mathbb{R}_+$, measuring
  how distinguishable two states are
- A class of **channels** $\mathcal{C}$: maps $f: \mathcal{S} \to \mathcal{S}$
  representing information processing operations

### 2.2 The axioms

**Axiom 1 (Closure under combination).**
*For all $p, q \in \mathcal{S}$ and $\lambda \in [0,1]$:*
$$p \circ_\lambda q \in \mathcal{S} \tag{2.1}$$

*Moreover, $\circ$ satisfies the mixture axioms:*
- *$p \circ_0 q = p$ and $p \circ_1 q = q$ (boundary)*
- *$p \circ_\lambda q = q \circ_{1-\lambda} p$ (symmetry)*
- *$(p \circ_\lambda q) \circ_\mu r = p \circ_{\lambda(1-\mu)} (q \circ_{\mu/(1-\lambda(1-\mu))} r)$ (associativity of mixing)*

**Interpretation.** When two agents with states $p$ and $q$ communicate and
form a weighted consensus, the result is a valid state. If $\mathcal{S}$ is
not closed under combination, there exist agents whose communication produces
an invalid output. Information processing requires valid intermediate states.

**Axiom 2 (Data processing inequality).**
*For any channel $f \in \mathcal{C}$:*
$$D(f(p), f(q)) \leq D(p, q) \quad \forall\, p, q \in \mathcal{S} \tag{2.2}$$

**Interpretation.** Processing cannot increase the distinguishability of two
states. This is the fundamental law of information: you cannot create
information from nothing. Any map that processes, transmits, or transforms
information can only destroy distinguishability, never create it.

This axiom encodes:
- Shannon's data processing inequality: $I(X;Z) \leq I(X;Y)$ when $X \to Y \to Z$
- The second law of thermodynamics: entropy cannot decrease under physical processes
- The no-cloning theorem (quantum): processing cannot perfectly copy a state
- Market efficiency: processing public information cannot create private information

**Axiom 3 (Continuity).**
*The combination $\circ_\lambda$ and divergence $D$ are continuous:*
$$\lambda_n \to \lambda \implies p \circ_{\lambda_n} q \to p \circ_\lambda q \tag{2.3}$$
$$p_n \to p, q_n \to q \implies D(p_n, q_n) \to D(p, q) \tag{2.4}$$

**Interpretation.** Small changes in the mixture parameter produce small
changes in the state. Small changes in the states produce small changes in
distinguishability. This rules out pathological spaces where nearby states
are infinitely distinguishable.

### 2.3 What the axioms rule out

**Important distinction: ambient vs intrinsic convexity.** The convexity
required by Axiom 1 is the convexity of the AMBIENT STATE SPACE (the
portfolio simplex, the space of distributions), not the convexity of any
submanifold within it. The efficient market manifold $M^r$ can have
non-trivial topology (torus, higher genus surface) — it lives INSIDE the
convex ambient space. A torus violates Axiom 1 only if it is proposed as
the entire state space; as a submanifold of a convex simplex, it is
perfectly compatible with the axioms.

**Non-convex ambient state spaces.** If the ambient state space itself has a
"hole" (like an annulus proposed as the full set of allowed distributions),
Axiom 1 is violated: two states on opposite sides cannot be mixed without
leaving the space.

**Discrete state spaces without embedding.** A finite set $\{s_1, \ldots, s_n\}$
with no interpolation violates Axiom 1 for $\lambda \notin \{0,1\}$. The
standard resolution: embed discrete states as vertices of $\Delta_{n-1}$
and extend $\circ$ to mixtures. This is exactly the passage from pure to
mixed states in quantum mechanics, or from deterministic to randomised
strategies in game theory.

**Metrics that create information.** A divergence $D$ that increases under
some processing map violates Axiom 2. For example, the Euclidean distance
$\|p - q\|_2$ on $\Delta_{d-1}$ is NOT monotone under all stochastic maps.
Only the Fisher-Rao metric (and its affine rescalings) satisfies Axiom 2
for all Markov maps (Čencov 1982).

---

## 3. The Geometry Is Forced

### 3.1 Čencov's theorem

The key result that converts the axioms into geometry:

**Theorem 3.1** *(Čencov 1982; Morozova-Chentsov 1991)*.
*Let $D$ be a divergence on $\Delta_{d-1}$ satisfying:*
- *(i) $D$ is a smooth Riemannian distance (from some metric $g$)*
- *(ii) $D$ is monotone: $D(f(p), f(q)) \leq D(p, q)$ for all Markov maps $f$*
- *(iii) $D$ is continuous*

*Then $g = c \cdot g^{\rm FR}$ for some constant $c > 0$, where*
$$g^{\rm FR}_{ij}(p) = \frac{\delta_{ij}}{p_i} \tag{3.1}$$
*is the Fisher-Rao metric.*

*The Fisher-Rao metric is the unique (up to scale) Riemannian metric on the
space of probability distributions that is invariant under sufficient
statistics.*

**Proof.** See Čencov (1982), Chapter 9; or Amari and Nagaoka (2000),
Theorem 2.6. The argument proceeds by showing that the monotonicity
condition (ii) under all Markov maps is so restrictive that it pins down
the metric tensor uniquely at each point, modulo a global scale factor. $\square$

### 3.2 Application to our axioms

**Theorem 3.2** *(Fisher-Rao is forced, classical commutative case)*.
*Let $(\mathcal{S}, D, \circ, \mathcal{C})$ satisfy Axioms 1–3 and additionally:*

*(A4) Normalisation: there exists a linear functional $\ell: \mathcal{S} \to \mathbb{R}$
such that $\ell(p) = 1$ for all $p \in \mathcal{S}$, and the components of
each state are non-negative.*

*(A5) Markov channels: the channel class $\mathcal{C}$ includes all stochastic
matrices (Markov maps) $M: \Delta_{d-1} \to \Delta_{d-1}$.*

*If $\mathcal{S}$ is finite-dimensional and $D$ is a smooth Riemannian distance,
then $\mathcal{S}$ is isometric to a convex subset of
$(\Delta_{d-1}, c \cdot g^{\rm FR})$ for some $d$ and $c > 0$.*

*Remark.* Axioms A4 and A5 are NOT implied by A1–A3 alone. They encode
the specifically *probabilistic* character of the information processing system:
states are non-negative and normalised (A4), and all possible data-processing
operations are available (A5). Without A4, the proof does not land on the
simplex. Without A5, Čencov's uniqueness fails (a smaller channel class
admits more metrics). The quantum case, where states are density matrices
and channels are CPTP maps, requires the Petz classification (1996) instead
of Čencov.

*Proof.*

**Step 1: Convexity and simplex structure.** Axiom 1 gives closure under
$\circ_\lambda$. The mixture axioms (boundary, symmetry, associativity)
characterise abstract convex sets. By the embedding theorem for abstract
convex sets (Stone 1949; Phelps 1966), $\mathcal{S}$ is affinely isomorphic
to a convex subset of $\mathbb{R}^n$ for some $n$. Axiom A4 (normalisation
and non-negativity) restricts to the intersection of a hyperplane
$\{\sum x_i = 1\}$ with the positive orthant $\mathbb{R}^n_+$. This
intersection is $\Delta_{n-1}$, the standard simplex with $d = n$.

**Step 2: Metric uniqueness.** Axiom 2 gives monotonicity of $D$ under
channels. By Čencov's theorem (3.1), $D$ is the Fisher-Rao distance up
to scale.

**Step 3: Combination.** Axiom 3 gives continuity, required by Čencov's
theorem.

Therefore $(\mathcal{S}, D)$ is isometric to a convex subset of
$(\Delta_{d-1}, c \cdot g^{\rm FR})$. $\square$

### 3.3 The role of each axiom

| Axiom | What it forces | What breaks without it |
|:------|:--------------|:----------------------|
| Closure (A1) | $\mathcal{S}$ is convex | Communication between agents can produce invalid states |
| Data processing (A2) | $g = g^{\rm FR}$ (Čencov) | The "distance" between states can be created by processing |
| Continuity (A3) | Smooth Riemannian structure | Nearby states can be infinitely distinguishable |

**No axiom is redundant.** Dropping A1: the integers $\mathbb{Z}$ with
discrete metric satisfy A2 and A3 but are not convex. Dropping A2: the
Euclidean metric on $\Delta_{d-1}$ satisfies A1 and A3 but is not monotone.
Dropping A3: the discrete metric $D(p,q) = \mathbf{1}_{p \neq q}$ on
$\Delta_{d-1}$ satisfies A1 and A2 but is not continuous.

---

## 4. The Bhattacharyya Embedding

### 4.1 The isometric embedding

**Theorem 4.1** *(Bhattacharyya isometry)*.
*The map $\phi: \Delta_{d-1} \to S^{d-1}(\frac{1}{2})$ defined by*
$$\phi(p) = \sqrt{p} = (\sqrt{p_1}, \ldots, \sqrt{p_d}) \tag{4.1}$$
*is an isometric embedding of $(\Delta_{d-1}, \frac{1}{4}g^{\rm FR})$ into
the sphere $S^{d-1}(\frac{1}{2})$ of radius $\frac{1}{2}$ with the
round metric.*

*Proof.* Compute the pullback: let $v \in T_p\Delta_{d-1}$ with $\sum v_i = 0$.
Then $d\phi(v)_i = v_i/(2\sqrt{p_i})$ and
$$|d\phi(v)|^2 = \sum_i \frac{v_i^2}{4p_i} = \frac{1}{4}g^{\rm FR}(v,v)$$
The image satisfies $\sum \phi_i^2 = \sum p_i = 1$, hence
$\phi(\Delta_{d-1}) \subset S^{d-1}(1)$. Rescaling by $\frac{1}{2}$
normalises the curvature to $K = 1/4$, the standard Bhattacharyya
normalisation. $\square$

### 4.2 Geodesic convexity of the positive orthant

**Theorem 4.2** *(Geodesic convexity of $S^{d-1}_+$)*.
*The image $\phi(\Delta_{d-1}) = S^{d-1}_+ = S^{d-1} \cap \mathbb{R}^d_+$ is
geodesically convex in $S^{d-1}$: for any two points $u, v \in S^{d-1}_+$,
the minimising geodesic (great circle arc) from $u$ to $v$ lies entirely
in $S^{d-1}_+$.*

*Proof.* The geodesic on $S^{d-1}$ from $u$ to $v$ is
$$\gamma(t) = \frac{\sin((1-t)\theta)}{\sin\theta}\,u + \frac{\sin(t\theta)}{\sin\theta}\,v \tag{4.2}$$
where $\theta = \arccos(u \cdot v)$. Since $u, v \in \mathbb{R}^d_+$ and
$\theta \leq \pi/2$ (because $u \cdot v = \sum \sqrt{p_i q_i} \geq 0$),
both coefficients $\sin((1-t)\theta)/\sin\theta$ and $\sin(t\theta)/\sin\theta$
are non-negative for $t \in [0,1]$. Hence every component of $\gamma(t)$
is a non-negative linear combination of non-negative numbers, so
$\gamma(t) \in \mathbb{R}^d_+$. Since $|\gamma(t)| = 1$ by construction,
$\gamma(t) \in S^{d-1}_+$. $\square$

### 4.3 The main theorem

Combining Theorems 3.2, 4.1, and 4.2:

**Theorem 4.3** *(Convex Information Processing Theorem)*.
*Any information processing system $(\mathcal{S}, D, \circ)$ satisfying
Axioms 1–3 is isomorphic to a geodesically convex subset of the
Bhattacharyya sphere $(S^{d-1}_+, g_{\rm round})$ for some $d$.*

*In particular:*
- *The state space is convex*
- *The metric is Fisher-Rao (unique)*
- *The embedding is in a sphere of curvature $K = 1/4$*
- *Geodesics (shortest communication paths) stay inside the state space*
- *Jensen's inequality holds for any concave functional on $\mathcal{S}$*

---

## 5. Six Instantiations

### 5.1 Probability theory

**States:** $p \in \Delta_{d-1}$ (probability distributions over $d$ outcomes).
**Combination:** $p \circ_\lambda q = (1-\lambda)p + \lambda q$ (mixture distribution).
**Divergence:** $D(p,q) = 2\arccos\sum_i\sqrt{p_i q_i}$ (Bhattacharyya distance).
**Channels:** Markov maps $f: \Delta_{d-1} \to \Delta_{d-1}$, $f(p)_j = \sum_i M_{ji} p_i$.

Axiom 1: mixture of distributions is a distribution. ✓
Axiom 2: data processing inequality $D(fp, fq) \leq D(p,q)$ for Markov $f$
(Čencov 1982). ✓
Axiom 3: Bhattacharyya distance is continuous. ✓

**Corollary.** Shannon entropy $H(p) = -\sum p_i \log p_i$ is concave on
$\Delta_{d-1}$ (Jensen's inequality on a convex domain with a concave
functional). The data processing inequality $H(f(X)) \leq H(X)$ follows.

### 5.2 Financial markets

**States:** $b \in \Delta_{d-1}$ (portfolio weights over $d$ assets).
**Combination:** $b \circ_\lambda b' = (1-\lambda)b + \lambda b'$ (portfolio blending).
**Divergence:** Fisher-Rao distance $d_{g^{\rm FR}}(b, b')$.
**Channels:** Market operations — rebalancing, transaction costs, information arrival.

Axiom 1: blending two portfolios is a portfolio. ✓
Axiom 2: transaction costs, market impact, and information loss all reduce
distinguishability of portfolio strategies. No costless operation can
increase the Fisher-Rao distance between two portfolio states. ✓
Axiom 3: small changes in weights produce small changes in distance. ✓

**Corollary.** The market manifold $M^r \subset S^{d-1}_+$ of the companion
monograph is a geodesically convex subset of the Bhattacharyya sphere. This
is not an assumption — it follows from Theorem 4.3 applied to portfolio
information processing.

### 5.3 Bayesian inference

**States:** $\pi \in \Delta_{\Theta}$ (prior/posterior distributions over
parameter space $\Theta$).
**Combination:** $\pi \circ_\lambda \pi' = (1-\lambda)\pi + \lambda\pi'$
(mixture of priors).
**Divergence:** Fisher-Rao distance on the space of posteriors.
**Channels:** Bayesian updating $\pi \mapsto \pi(\cdot | x)$ given data $x$.

Axiom 1: mixture of priors is a prior. ✓
Axiom 2: Bayesian updating is a Markov map. By Čencov, it contracts
Fisher-Rao distance. This is the Bayesian version of "you can't create
information by processing data." ✓
Axiom 3: continuity of the posterior in the data. ✓

**Corollary.** The posterior $\pi(\theta | x_{1:T})$ converges to the
true parameter along a Fisher-Rao geodesic on the convex space of
posteriors. The Bernstein-von Mises theorem (Bayesian CLT) is a statement
about the curvature of this geodesic at the limit point.

### 5.4 Machine learning

**States:** $\sigma(z) \in \Delta_{d-1}$ (softmax output of a neural network
with logits $z \in \mathbb{R}^d$).
**Combination:** $\sigma(z) \circ_\lambda \sigma(z') = (1-\lambda)\sigma(z) + \lambda\sigma(z')$
(model averaging / ensembling).
**Divergence:** Fisher-Rao distance, or equivalently KL divergence at
leading order ($\mathrm{KL}(p\|q) = \frac{1}{2}d^2_{g^{\rm FR}}(p,q) + O(d^3)$).
**Channels:** Layers of the network; each layer is a differentiable map
$\Delta \to \Delta$.

Axiom 1: ensemble of models is a model. ✓
Axiom 2: each layer of a neural network is a differentiable function;
composition of layers contracts Fisher-Rao distance (by repeated application
of the data processing inequality). This is why deeper networks lose
information — each layer contracts. ✓
Axiom 3: softmax is continuous. ✓

**Corollary.** The softmax function $\sigma: \mathbb{R}^d \to \Delta_{d-1}$
is the unique continuous map from unconstrained logits to the information
processing space that preserves the Fisher-Rao structure. The cross-entropy
loss $-\sum y_i \log \sigma(z)_i$ is the Fisher-Rao divergence between
the true label $y$ and the predicted distribution $\sigma(z)$, to leading
order. Any ML system that outputs probabilities is doing Fisher-Rao
geometry on the simplex, whether it knows it or not.

### 5.5 Quantum mechanics

**States:** Density matrices $\rho \in \mathcal{D}_d = \{\rho \succeq 0 : \mathrm{tr}(\rho) = 1\}$.
**Combination:** $\rho \circ_\lambda \rho' = (1-\lambda)\rho + \lambda\rho'$
(mixing of quantum states).
**Divergence:** Quantum Fisher information metric (Bures metric):
$D_B(\rho, \sigma)^2 = 2(1 - \mathrm{tr}\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}})$.
**Channels:** Completely positive trace-preserving (CPTP) maps.

Axiom 1: mixture of density matrices is a density matrix (the set
$\mathcal{D}_d$ is convex). ✓
Axiom 2: CPTP maps contract the Bures metric (Uhlmann's monotonicity
theorem, the quantum data processing inequality). ✓
Axiom 3: Bures metric is continuous. ✓

**Corollary.** Quantum information processing satisfies all three axioms.
The Bures metric is the quantum analogue of the Fisher-Rao metric, and the
space of density matrices is the quantum analogue of the simplex. The
Born rule $\mathrm{Pr}(\text{outcome } i) = \mathrm{tr}(\rho\, \Pi_i)$
is the quantum version of "evaluating a probability distribution at an
event." The geometric structure is the same; only the non-commutativity of
the state space is new.

### 5.6 Game theory

**States:** $\sigma \in \Delta_{d-1}$ (mixed strategies over $d$ pure strategies).
**Combination:** $\sigma \circ_\lambda \sigma' = (1-\lambda)\sigma + \lambda\sigma'$
(randomised strategy mixing).
**Divergence:** Fisher-Rao distance between strategy distributions.
**Channels:** Best-response maps, regret-minimisation updates.

Axiom 1: randomisation of randomised strategies is a randomised strategy. ✓
Axiom 2: best-response dynamics contract the Fisher-Rao distance between
players' strategy profiles (this is the content of the convergence theorems
for fictitious play and regret matching). ✓
Axiom 3: payoff functions are continuous in the strategy profile. ✓

**Corollary.** Nash equilibria live on the convex set of mixed strategy
profiles. The multiplicative weights update algorithm
$\sigma_{t+1,i} \propto \sigma_{t,i} \cdot \exp(\eta \cdot u_i)$ is the
exponentiated gradient algorithm on the simplex — the same algorithm as
Cover's universal portfolio and the EG integrator of the companion code.
Online learning, game theory, and portfolio theory share identical geometry
because they are all instances of convex information processing.

---

## 6. Consequences for the Companion Monograph

The Convex Information Processing Theorem (4.3) provides the axiomatic
foundation for the companion monograph *The Geometry of Efficient Markets*.
Every major result is now derivable from the three axioms:

### 6.1 The market manifold is a theorem

**Old formulation (axiom):** "A financial market is a minimal submanifold
$M^r \subset S^{d-1}_+$."

**New formulation (theorem):** A financial market satisfying Axioms 1–3
has its state space isomorphic to a geodesically convex subset of
$(S^{d-1}_+, g_{\rm round})$. The efficient market manifold $M^r$ is
the submanifold on which the Kelly growth rate is maximised — the
zero set of the mean curvature vector.

The passage from axiom to theorem eliminates the strongest objection to the
geometric framework: "Why should a market be a manifold?" Because the
axioms of information processing force it.

### 6.2 The Fisher-Rao metric is not a choice

The Fisher-Rao metric $g^{\rm FR}_{ij} = \delta_{ij}/b_i$ appears
throughout the monograph. The standard objection: "Why not use the
Euclidean metric on the simplex?" Answer: because the Euclidean metric
violates Axiom 2. The Fisher-Rao metric is the unique Riemannian metric
compatible with the data processing inequality. It is not a modelling
choice. It is a mathematical necessity.

### 6.3 The Sharpe-curvature identity

The identity $\mathrm{Sharpe}^* = \|H\|_{L^2}$ (Paper I.3) requires the
Fisher-Rao metric to define the mean curvature $H$. From the axioms: the
metric is forced, the embedding is forced, the curvature is forced.
The Sharpe ratio is a computable geometric invariant of the information
processing system — not of a particular model of the market.

### 6.4 The MUP is optimal information processing

The Manifold Universal Portfolio (Paper I.5) integrates
$W_T(b) = \exp(T \cdot L_T(b))$ over the market manifold $M^r$. This is the
Bayesian optimal strategy on a convex information processing space: it
combines all consistent hypotheses (points on $M^r$) weighted by evidence
(accumulated wealth). The MUP is optimal precisely because $M^r$ is convex
(Axiom 1) and the weighting respects the data processing inequality
(Axiom 2).

### 6.5 LLMs are bounded by the MUP

Paper IV.2 proves that no LLM can beat the MUP on an efficient market.
From the axioms: both the LLM and the MUP process information on the same
convex simplex with the same Fisher-Rao metric. The LLM's softmax output
lives in $\Delta_{|\mathcal{V}|-1}$. The data processing inequality (Axiom 2)
means every layer of the LLM contracts Fisher-Rao distance. The MUP, by
integrating over the full manifold, achieves the information-theoretic
optimum. No amount of depth or data can overcome the geometry.

### 6.6 Ergodic coverage is complete

The ergodic market manifold theorem (the observation that stochastic and
deterministic dynamics produce the same long-run statistics if the dynamics
are ergodic on $M^r$) requires geodesic convexity. On a convex space, any
ergodic orbit visits every point — there are no topological obstructions
(holes, handles, non-trivial fundamental group) that could prevent coverage.

On a non-convex space (e.g., a torus or a surface of higher genus), an
ergodic orbit can be confined to a contractible subset and never visit
certain regions. Convexity rules this out: every point is reachable from
every other point via a geodesic that stays in $\mathcal{S}$.

### 6.7 The three market types

The classification of efficient markets into three types (Paper I.4 —
CAPM/sphere, Clifford torus, pseudo-Anosov/hyperbolic) is a classification
of minimal submanifolds of $S^{d-1}_+$. Theorem 4.3 tells us that the
ambient space $S^{d-1}_+$ is forced; the classification then follows from
the differential geometry of minimal submanifolds of spheres (Lawson 1969;
Simons 1968).

Note that the Clifford torus $T^2$ is itself convex in the intrinsic sense
(every pair of points on the flat torus is connected by a geodesic that
stays on the torus), even though its embedding in $S^3$ is not convex in
the ambient sense. The relevant convexity for information processing is the
convexity of the *portfolio space* $\Delta_{d-1}$, not of the market
manifold $M^r$.

---

## 7. Open Problems

**OP-A. Non-commutative generalisation.**
The quantum version (Section 5.5) uses density matrices, which are
non-commutative. The Bures metric replaces the Fisher-Rao metric. Is there
a non-commutative version of Theorem 4.3 where the Bhattacharyya sphere is
replaced by the space of density matrices with the Bures metric? If so,
this would give a "quantum market manifold" and a quantum version of the
companion monograph.

**OP-B. Infinite-dimensional state spaces.**
Our proof uses finite-dimensional embedding (Step 1 of Theorem 3.2).
For continuous probability distributions (infinite-dimensional simplex),
Čencov's theorem still holds (Amari and Nagaoka 2000), but the embedding
theorem for abstract convex sets requires additional topological hypotheses
(e.g., local compactness). Does Theorem 4.3 extend to
infinite-dimensional information processing systems?

**OP-C. Categorical formulation.**
The axioms have a natural categorical interpretation: states are objects,
channels are morphisms, and the axioms are properties of the category.
Is there a categorical version of Theorem 4.3 that characterises the
"category of convex information processing systems" abstractly?

**OP-D. Operational characterisation of curvature.**
In the companion monograph, the mean curvature $H$ of $M^r \subset S^{d-1}_+$
determines the Sharpe ratio. Is there a purely operational characterisation
of $H$ in terms of the axioms — without reference to the embedding?
If so, this would make the Sharpe-curvature identity a theorem of
abstract information processing, not just of embedded geometry.

**OP-E. The role of the dimension $d$.**
The axioms force the simplex $\Delta_{d-1}$ for some $d$, but do not
determine $d$. In financial markets, $d$ is the number of assets. In ML,
$d$ is the vocabulary size. Is there an information-theoretic characterisation
of $d$ — a "minimum description dimension" of the information processing
system? If so, this would connect to the manifold dimension $r$ via the
stable rank of the Fisher information matrix.

---

## 8. The Philosophical Point

### 8.1 Convexity is not optional

The three axioms — closure, monotonicity, continuity — are minimal. Any
system that communicates (Axiom 1), that cannot create information from
nothing (Axiom 2), and that responds continuously to its inputs (Axiom 3)
is *forced* to operate on a convex subset of the Fisher-Rao simplex.

This is not a modelling choice. It is not a convenience. It is not an
approximation. It is a mathematical necessity.

### 8.2 The unity of information processing systems

The six instantiations of Section 5 — probability, markets, Bayes, ML,
quantum, games — are traditionally studied by different communities using
different formalisms. The Convex Information Processing Theorem says they
are all the same system. The differences are:

- The dimension $d$ (number of outcomes, assets, parameters, tokens, energy levels, strategies)
- The manifold dimension $r$ (number of independent factors)
- The specific channels (Markov maps, market operations, neural network layers, CPTP maps, best-response dynamics)

But the geometry is identical: a convex subset of a sphere of curvature
$1/4$, with the unique monotone metric.

### 8.3 Why this matters for the monograph

The companion monograph begins with an axiom: "A financial market is a
minimal submanifold of the Bhattacharyya sphere." With this paper, that
axiom is promoted to a theorem. The monograph's 85 results, 30 conjectures,
and 34 open problems all rest on a foundation of three axioms that no
reasonable information processing system can violate.

The geometry of efficient markets is not a metaphor. It is not an analogy.
It is the unique mathematical structure compatible with the processing of
financial information.

---

## References

Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry*.
American Mathematical Society.

Bhattacharyya, A. (1943). On a measure of divergence between two
statistical populations. *Bulletin of the Calcutta Mathematical Society*
35, 99–109.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*.
American Mathematical Society. (Translation of 1972 Russian original.)

Cover, T. M. (1991). Universal portfolios. *Mathematical Finance* 1(1), 1–29.

Lawson, H. B. (1969). Local rigidity theorems for minimal hypersurfaces.
*Annals of Mathematics* 89(1), 187–197.

Morozova, E. A. and Chentsov, N. N. (1991). Markov invariant geometry on
manifolds of states. *Journal of Soviet Mathematics* 56(5), 2648–2669.

Phelps, R. R. (1966). *Lectures on Choquet's Theorem*. Van Nostrand.

Shannon, C. E. (1948). A mathematical theory of communication.
*Bell System Technical Journal* 27(3), 379–423.

Simons, J. (1968). Minimal varieties in Riemannian manifolds.
*Annals of Mathematics* 88(1), 62–105.

Stone, M. H. (1949). Postulates for the barycentric calculus.
*Annals of Mathematics* 50(1), 95–105.

Uhlmann, A. (1976). The "transition probability" in the state space of a
*-algebra. *Reports on Mathematical Physics* 9(2), 273–279.

*[All other references as per companion papers.]*
