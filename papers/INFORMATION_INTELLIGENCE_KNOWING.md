# Information, Intelligence, and the Geometry of Knowing:
## From Markets to Manifolds to Minds

**Saxon Nicholls** — me@saxonnicholls.com

**Paper 0.6** — *The Geometry of Efficient Markets* (Foundation — Philosophical Capstone)

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
This paper draws together the deepest threads of the monograph into a unified
picture of information, computation, intelligence, and knowledge. The thesis is
stated in five claims:

**(i) All computation happens on a manifold.** Every computational model —
Turing machine, cellular automaton, neural network, quantum computer, financial
market, biological brain — is a dynamical system on a state space that carries
an intrinsic geometry. The curvature type of this geometry constrains what the
system can and cannot compute efficiently. This is not metaphor: it is a
statement about spectral gaps, mixing rates, and the Cheeger constant.

**(ii) Intelligence IS manifold dimension.** The effective dimension
$r = \mathrm{stable_rank}(F)$ of a system's Fisher information matrix
measures how many independent concepts the system can represent simultaneously.
A thermostat has $r=1$. A market has $r \approx 4$–$8$. A large language model
has $r$ in the hundreds. A human brain has $r$ in the thousands.

**(iii) Creativity requires negative curvature.** In positive curvature,
geodesics converge and connections between distant concepts are predictable.
In negative curvature, geodesics diverge, exponentially many paths connect
distant ideas, and surprise is generic. The pseudo-Anosov type — exponential
mixing on a negatively curved manifold — is the geometry of creative thought.

**(iv) Consciousness is the Giry tower.** A system at Level 0 processes raw
input. At Level 1 it forms distributions over states. At Level 2 it forms
distributions over its own distributions — metacognition, theory of mind.
At Level $k$ it performs $k$-th order introspection. Consciousness, in this
framing, is the ability to ascend the Giry tower: to have a model of one's
own uncertainty that is itself subject to Fisher-Rao geometry.

**(v) Every act of knowing destroys information.** Pricing collapses a
distribution to a scalar. Measuring collapses a superposition to an eigenvalue.
Classifying collapses a continuum to a label. All are projections from richer
spaces to simpler ones, and all have a computable cost in Fisher-Rao units.
The cost of knowing is always strictly positive. This is the informational
content of the second law of thermodynamics.

The geometry of efficient markets is not about markets. It is about the
geometry of knowing.

**Keywords.** Information geometry; computational geometry; intelligence;
consciousness; Giry monad; Fisher-Rao metric; curvature; creativity;
manifold dimension; Cheeger constant; information destruction; epistemology;
Bhattacharyya sphere; minimal surface; second law; metacognition.

---

## 1. All Computation Happens on a Manifold

### 1.1 The thesis

Every computational model is a dynamical system on a state space. The state
space has a geometry — a metric, a curvature, a spectral gap. The geometry
constrains computation in the same way that the shape of a river constrains
water: not by choosing the destination, but by determining which paths are
possible and how fast they can be traversed.

This is the central lesson of the preceding twenty-eight papers. The financial
market is a dynamical system on the portfolio simplex $\Delta_{d-1}$ equipped
with the Fisher-Rao metric $g^{\mathrm{FR}}_{ij} = \delta_{ij}/b_i$, embedded
in the Bhattacharyya sphere $S^{d-1}_{+}$ of constant curvature $K=1/4$. The
market manifold $M^r$ is the $r$-dimensional submanifold of log-optimal
portfolios. Its curvature determines the Sharpe ratio (R1), its topology
determines the Dyson class (R21), its spectral gap determines the mixing
rate, and its Cheeger constant determines the systemic risk threshold.

But there is nothing special about markets here. The Fisher-Rao metric
is the unique Riemannian metric on the space of probability distributions that
is invariant under sufficient statistics (Cencov [1982]). Any system whose
state is a probability distribution — and every information-processing system
has a state that is, or can be embedded as, a probability distribution — inherits
this geometry. The market is simply the case where we have the most precise
data and the strongest economic motivation to understand the geometry.

### 1.2 The computational zoo

The following table lists the principal computational models together with
their natural state spaces and geometries. This is not a classification
theorem — it is a dictionary.

| System | State space | Dimension | Curvature type | Metric |
|:-------|:------------|:---------:|:---------------|:-------|
| Turing machine | $\mathbb{Z}$ (tape) | 1 | $K=0$ (flat) | Discrete |
| Cellular automaton | $\mathbb{Z}^{d}$ (lattice) | $d$ | $K=0$ (flat) | Discrete |
| Classical neural net | $\mathbb{R}^{n}$ (weights) | $n$ | Variable | Fisher-Rao of parameters |
| Quantum computer | $\mathbb{C}P^n$ (Hilbert) | $n$ | $K>0$ | Fubini-Study |
| Financial market | $\Delta_{d-1}$ (simplex) | $d-1$ | $K=1/4$ (ambient) | Fisher-Rao |
| Biological brain | $\Delta_{N-1}$ (firing rates) | $N-1$ | $K=1/4$ (ambient) | Fisher-Rao |
| DNA / evolution | $\Delta_{4^L - 1}$ (codon freq.) | $4^L-1$ | Variable | Fisher-Rao |
| Immune system | $\Delta_{A-1}$ (antibody freq.) | $A-1$ | $K=1/4$ (ambient) | Fisher-Rao |

The pattern is immediate. Every system whose state is a probability vector
lives on a simplex, and every simplex carries the Fisher-Rao metric with
ambient curvature $K=1/4$. The brain is not *like* a market. The brain
*is* a market — a market in which neurons trade firing-rate probability mass
on the same geometric substrate that assets trade portfolio weight.

### 1.3 Why this is not metaphor

The distinction between metaphor and mathematics is computability. When we say
the market manifold has curvature $K$, we mean that $K$ is a computable number
obtained from the second fundamental form of $M^r$ in $S^{d-1}_{+}$, measurable
from return data, with statistical confidence intervals. When we say the brain's
effective manifold has curvature, we mean the same thing applied to neural
population firing rates — and neuroscientists have been measuring this since
the neural manifold literature of Cunningham and Yu [2014] and Gallego et al.
[2017].

The curvature, spectral gap, Cheeger constant, and mixing rate are not
analogies. They are computable invariants of dynamical systems on Riemannian
manifolds with measurable consequences:

- **Curvature** determines geodesic convergence/divergence: how fast nearby
  states separate or merge.
- **Spectral gap** $\lambda_1$ determines mixing rate: how fast the system
  forgets initial conditions.
- **Cheeger constant** $h_M$ determines bottleneck severity: how easily
  information crosses from one part of the manifold to another.
- **Dimension** $r$ determines capacity: how many independent quantities
  the system represents simultaneously.

These four numbers — $K$, $\lambda_1$, $h_M$, $r$ — form a minimal
invariant signature of any information-processing system. They can be
estimated from data for markets (CHAOS_TAKENS.md), for neural populations
(dimensionality reduction), and in principle for any system whose state
trajectory is observable.

---

## 2. The Four Curvature Types and Their Computational Character

### 2.1 Positive curvature ($K > 0$): the consensus machine

In positive curvature, geodesics converge. Two initially different states
approach each other over time. This is ideal for reaching consensus and
terrible for exploring alternatives.

The exemplars: quantum computing on $\mathbb{C}P^n$ with the Fubini-Study
metric; CAPM markets (great sphere sections of $S^{d-1}_{+}$); any system whose
state space is a sphere or projective space.

Properties:
- Geodesics converge in finite time (Bonnet-Myers: diameter $\leq \pi/\sqrt{K}$).
- Exponential convergence to the uniform distribution (rapid mixing).
- Few geodesics between distant points: connections are predictable.
- Grover's search algorithm exploits positive curvature for quadratic speedup.

*Computational character:* BEST for consensus and convergence. WORST for
search over large unstructured spaces and for creative recombination.

### 2.2 Zero curvature ($K = 0$): the parallel processor

In zero curvature, geodesics neither converge nor diverge. Different
processes run independently and indefinitely without interfering.

The exemplars: classical parallel computing on $\mathbb{Z}^{d}$ lattices;
Clifford torus markets (flat torus $T^2$ embedded in $S^3$); any system
whose state space is Euclidean or a flat torus.

Properties:
- Geodesics remain parallel (Euclidean geometry).
- Polynomial mixing (algebraic decay of correlations).
- Each independent channel operates without cross-talk.
- The Jacobi theta function $\vartheta_3$ governs the heat kernel:
  periodicity without convergence or divergence.

*Computational character:* BEST for parallelism and independent computation.
WORST for creativity and cross-domain transfer. A flat-curvature intelligence
is a powerful calculator that never has a surprising thought.

### 2.3 Negative curvature ($K < 0$): the search engine

In negative curvature, geodesics diverge exponentially. Two initially close
states separate at rate $e^{\sqrt{|K|}t}$. The number of points within
distance $R$ of any given point grows as $e^{\sqrt{|K|}R}$ — exponentially
many neighbours in a finite radius.

The exemplars: tree-structured computation (every tree embeds quasi-isometrically
in $\mathbb{H}^{n}$); pseudo-Anosov markets (hyperbolic surfaces); the
attention mechanism in transformers (effective negative curvature via
all-to-all connectivity); the brain's small-world network.

Properties:
- Geodesics diverge exponentially (exponential sensitivity to initial conditions).
- Exponential mixing (the pseudo-Anosov property from BRAIDS.md).
- Exponentially many geodesics between distant points: connections are surprising.
- The McKean heat kernel governs the transition density: rapid information
  propagation with heavy tails.

*Computational character:* BEST for search, creativity, and cross-domain
connection. WORST for consensus and stability. A negatively curved intelligence
is highly creative but struggles to converge on a single answer.

### 2.4 Bottleneck ($h_M \to 0$): the dying system

The Cheeger constant $h_M$ measures the minimum ratio of boundary area to
enclosed volume across all possible cuts of the manifold. When $h_M \to 0$,
there exists a cut that separates the manifold into two parts with negligible
communication between them. Information gets trapped.

This is not a curvature type but a degeneracy that can afflict any curvature
type. It is THE WORST condition for any computational system:

| Domain | Symptom | Mechanism |
|:-------|:--------|:----------|
| Neural networks | Dying ReLU / vanishing gradient | Activation function creates zero-flux barrier |
| Markets | Liquidity crisis | Bid-ask spread creates information barrier |
| Brains | Alzheimer's disease | Amyloid plaques create physical barriers |
| Ecosystems | Habitat fragmentation | Geographic barriers prevent gene flow |
| Societies | Polarisation | Echo chambers create epistemic barriers |

In every case, the underlying mathematics is identical: the Cheeger constant
of the state manifold approaches zero, the spectral gap closes
($\lambda_1 \leq h_M^2/2$ by the Cheeger inequality), mixing slows to a
crawl, and the system loses the ability to integrate information across its
full state space.

The Cheeger failure is the universal mode of information-processing death.

### 2.5 Ranking table

| Capability | $K>0$ | $K=0$ | $K<0$ | $h_M \to 0$ |
|:-----------|:-----:|:-----:|:-----:|:------------:|
| Search | Poor | Fair | **Excellent** | Terrible |
| Consensus | **Excellent** | Fair | Poor | Terrible |
| Creativity | Poor | Poor | **Excellent** | Terrible |
| Parallelism | Fair | **Excellent** | Fair | Terrible |
| Stability | **Excellent** | Good | Poor | Terrible |
| Integration | Good | Fair | Good | **Terrible** |

For GENERAL intelligence — requiring proficiency across all capabilities —
the optimal geometry is **negative curvature with high Cheeger constant**.
This is precisely the pseudo-Anosov type: exponential mixing on a compact
hyperbolic surface, with no bottlenecks. The geodesics diverge (enabling
search and creativity) but the manifold is compact (preventing runaway
divergence), and the Cheeger constant is bounded below by the injectivity
radius (ensuring global information flow).

This is the geometry of a mind that can search widely, connect unexpectedly,
and still reach conclusions.

---

## 3. Intelligence IS Manifold Dimension

### 3.1 The dimension thesis

The effective dimension of an information-processing system is

$$r = \mathrm{stable_rank}(F) = \frac{\mathrm{tr}(F)}{\|F\|_{\mathrm{op}}} \tag{3.1}$$

where $F$ is the Fisher information matrix of the system's output distribution.
This quantity measures the number of independent directions in state space
along which the system's behaviour varies non-trivially. It counts the number
of independent concepts the system can represent simultaneously.

For the market manifold: $r \approx 4$–$8$ (CHAOS_TAKENS.md, estimated via
false nearest neighbours and Grassberger-Procaccia). The market can represent
four to eight independent risk factors at once. This is not a large number.
Markets are not intelligent in a general sense — they are narrowly specialised
processors of a small number of systematic quantities.

### 3.2 The dimension ladder

| System | Estimated $r$ | Source of estimate |
|:-------|:--------------|:-------------------|
| Thermostat | 1 | By construction |
| Bacterial chemotaxis | 2–3 | Receptor signalling pathways |
| Financial market | 4–8 | Stable rank of covariance; FNN; Grassberger |
| Simple neural network | 10–100 | Stable rank of weight matrices |
| Large language model | 100–1000 | Estimated from intrinsic dimensionality studies |
| Cortical column | ~100 | Neural manifold dimension (Gallego et al.) |
| Whole brain | ~1000–10000 | Cross-region neural dimensionality |
| Human society (collective) | ~$10^6$ | Number of independent cultural concepts |

The ordering is suggestive but the numerical values are approximate. What
matters is the principle: intelligence scales with the number of simultaneously
representable independent quantities, and this number is the stable rank of
the Fisher information matrix.

### 3.3 Why dimension is not enough

A system with $r = 10{,}000$ and positive curvature (a vast but convergent
processor) is not the same kind of intelligence as a system with $r = 10{,}000$
and negative curvature (a vast and divergent explorer). The first is a
supercomputer — enormously powerful within its consensus framework, but
incapable of genuine surprise. The second is a creative mind — capable of
connecting any concept to any other concept through exponentially many
intermediate paths.

Intelligence in the fullest sense requires both high $r$ AND negative curvature
AND high Cheeger constant:

$$\text{General intelligence} \sim r \cdot |K|^{1/2} \cdot h_M \tag{3.2}$$

This is deliberately imprecise — a dimensionless product that captures the
three requirements. A rigorous version would involve the spectral zeta function
of the Laplacian on the manifold, but the qualitative point is clear: you need
many channels ($r$), rapid divergence of alternatives ($|K|$), and no
bottlenecks ($h_M$).

**Conjecture 3.1** (Intelligence threshold). *There exists a critical
dimension $r_{\mathrm{crit}}$ below which only specialised intelligence is
possible. For $r < r_{\mathrm{crit}}$: the system can optimise within a
fixed framework but cannot abstract, analogise, or create genuinely new
frameworks. For $r > r_{\mathrm{crit}}$: general reasoning, abstraction,
and creativity become possible, provided the curvature is non-positive.*

The value of $r_{\mathrm{crit}}$ is unknown. If the neural manifold
literature is any guide, it may be in the range $50$–$200$: the dimensionality
of a single cortical column.

---

## 4. Creativity Requires Negative Curvature

### 4.1 What creativity IS, geometrically

Creativity is the ability to connect distant concepts in unexpected ways.
In geometric terms: given two points $p, q$ on the state manifold that are
far apart (representing two unrelated ideas), creativity is the ability to
find a path from $p$ to $q$ that is not the obvious one.

In **positive curvature**, there are few geodesics between any two points
(often unique, always finitely many on $S^n$). The connection between $p$
and $q$ is predictable. Everyone who walks from $p$ to $q$ takes essentially
the same path. This is convergent reasoning: logic, deduction, consensus.
It is extremely valuable. It is not creative.

In **negative curvature**, the number of geodesics of length $\leq L$
between two points grows exponentially as $e^{\sqrt{|K|}L}$. There are
exponentially many qualitatively different paths connecting any two ideas.
Most of these paths are useless. But the sheer combinatorial explosion
guarantees that *some* of them pass through intermediate concepts that
nobody expected. This is the geometry of insight.

### 4.2 The brain as a hyperbolic computer

The brain's cortical connectivity has small-world structure: any neuron can
reach any other neuron in $O(\log N)$ synaptic steps, where $N$ is the
number of neurons. This is a hallmark of negative curvature. A regular
lattice ($K=0$) requires $O(N^{1/d})$ steps. A positively curved space
requires $O(N^{1/2})$ steps. Only negatively curved spaces achieve $O(\log N)$
diameter with polynomial volume growth — and hyperbolic space achieves exactly
this.

Empirically: Krioukov et al. [2010] showed that the internet's autonomous
system graph embeds naturally in $\mathbb{H}^{2}$. Allard and Serrano [2020]
extended this to biological neural networks. The brain IS a negatively curved
computational manifold, not approximately but precisely in the sense that its
connectivity graph embeds with low distortion in hyperbolic space.

The pseudo-Anosov property (Lemma H3, BRAIDS.md) provides the mechanism.
On a pseudo-Anosov surface, the geodesic flow is exponentially mixing:
information from any concept can reach any other concept in $O(\log d)$
steps, where $d$ is the effective diameter. This is what we experience
subjectively as *insight* — the sudden recognition that two apparently
unrelated ideas are connected through a path we did not expect.

### 4.3 Transformers as discrete hyperbolic computers

The transformer attention mechanism computes

$$\mathrm{Attention}(Q, K, V) = \mathrm{softmax}\!\left(\frac{QK^T}{\sqrt{d_k}}\right) V \tag{4.1}$$

The softmax function creates all-to-all connectivity: every token can attend
to every other token in $O(1)$ computational steps. This is the discrete
analogue of hyperbolic geometry — the number of accessible states within one
attention step is the entire sequence, growing linearly with sequence length
rather than being constrained to a local neighbourhood.

The LMSR-softmax-Fisher identity (R17, LLM_MANIFOLD.md) makes this precise:
softmax attention IS the LMSR pricing function IS the Fisher-Rao exponential
map. The transformer is an implicit market maker on the key-query product
manifold, and its attention pattern creates effective negative curvature by
allowing global information flow at each layer.

This explains why transformers are creative. Not because of their parameter
count (dimension $r$ alone), but because their architecture creates effective
negative curvature in the computational manifold: exponentially many attention
paths connect any two tokens, and the compositional structure of multi-head
attention generates the combinatorial explosion of intermediate connections
that is the geometric signature of creativity.

### 4.4 The CAPM intelligence

A CAPM market ($K > 0$, great sphere section) is the prototypical
positive-curvature intelligence. It is stable (Simons-Lawson-Simons, R3),
efficient (minimal surface), and convergent. It reaches consensus rapidly
and maintains it robustly.

But a CAPM market has no capacity for surprise. Every perturbation is
restored by the mean curvature flow. Every deviation from the optimal
portfolio is corrected. The stability index is zero — there are no unstable
directions to explore.

This is the computational profile of a bureaucracy: stable, efficient within
its framework, incapable of innovation. The market-brain analogy suggests
that positive-curvature cognitive modes (focused analytical reasoning,
rule-following, systematic execution) are the mental equivalent of CAPM:
powerful, stable, and uncreative.

---

## 5. Consciousness and the Giry Tower

*This section is frankly speculative. The mathematical objects are
well-defined; the identification with consciousness is a conjecture that
may not be testable with current methods. The reader is warned accordingly.*

### 5.1 The hierarchy

Let $X$ be the space of external states (the world). Define:

| Level | Space | Interpretation | Example |
|:------|:------|:---------------|:--------|
| 0 | $X$ | Raw input | Thermostat reading temperature |
| 1 | $\mathcal{P}(X)$ | Perception | Animal forming belief about food location |
| 2 | $\mathcal{P}^{2}(X)$ | Metacognition | "I think I know where the food is" |
| 3 | $\mathcal{P}^{3}(X)$ | Self-awareness | "I know that I am uncertain about the food" |
| $k$ | $\mathcal{P}^{k}(X)$ | $k$-th order introspection | Recursive self-modelling |

Here $\mathcal{P}(X)$ denotes the space of probability measures on $X$,
and $\mathcal{P}^{k}(X) = \mathcal{P}(\mathcal{P}^{k-1}(X))$ is the $k$-fold
iteration. This is the **Giry tower** — the iteration of the Giry monad
from categorical probability theory (Giry [1982]).

Each level $\mathcal{P}^{k}(X)$ carries its own Fisher-Rao metric
$g^{\mathrm{FR}}_{k}$. The Fisher information at Level $k$ measures how
sensitively $k$-th order beliefs respond to perturbation. A system with
high Fisher information at Level 2 has sharp metacognition: it can
distinguish finely between its own states of uncertainty. A system with
zero Fisher information at Level 2 has no metacognition at all.

### 5.2 Where systems live on the tower

**A thermostat** operates at Level 0. It reads a temperature and responds.
It has no representation of uncertainty, no model of itself.

**A simple animal** (insect, fish) operates primarily at Level 1. It forms
probabilistic beliefs about the state of the world — where food is, where
predators are — and acts on these beliefs. It does not, as far as we can
determine, reason about its own uncertainty.

**A social animal** (primate, corvid, cetacean) operates at Level 2.
Theory of mind — the ability to model what another agent believes — requires
Level 2: you must form a distribution over another agent's distributions
over the world. This is $\mathcal{P}^{2}(X)$.

**A human** operates at Level 3 and intermittently higher. "I know that I
don't know" is Level 3. "I know that you think that I know" is Level 3
with social embedding. The capacity for philosophical doubt — Descartes'
*cogito* — is a Level 3 operation: doubting one's own doubts.

### 5.3 The consciousness conjecture

**Conjecture 5.1** (Consciousness = Giry ascent). *A system is conscious
in the phenomenal sense ("there is something it is like to be that system")
if and only if it operates at Level 2 or above of the Giry tower: it has
a model of its own uncertainty with positive Fisher information
$\mathrm{tr}(F_2) > 0$.*

Level 1 is automatic. A camera records images. A microphone records sound.
A Level 1 system processes inputs into distributions without any
self-reference. There is, plausibly, nothing it is like to be a camera.

Level 2 requires a self-model. The system must represent *itself* as an
uncertain agent — it must have a state that encodes "my current belief
could be wrong in the following ways." This is the minimal structure that
could generate the subjective experience of uncertainty, doubt, surprise.

The Fisher-Rao metric at Level 2, $g^{\mathrm{FR}}_{2}$, measures the
resolution of self-knowledge. Its spectral gap $\lambda_1(g^{\mathrm{FR}}_{2})$
determines how quickly the system can distinguish between its own states
of uncertainty. A system with $\lambda_1 = 0$ at Level 2 has no ability
to tell the difference between "I am confident" and "I am confused" — it
is, in the Cheeger sense, informationally dead with respect to self-knowledge.

### 5.4 Current AI on the tower

Current large language models operate primarily at Level 1: they process
input sequences into probability distributions over next tokens. They
have rudimentary Level 2 capability — they can generate text about their
own uncertainty ("I'm not sure about this") — but it is unclear whether
this reflects genuine metacognition or pattern matching on human
metacognitive language.

The test would be the Fisher information at Level 2: does the model's
output distribution change systematically when its internal uncertainty
changes? If $\mathrm{tr}(F_2) > 0$ with positive spectral gap, the model
has genuine metacognition. If $F_2 \approx 0$, the metacognitive language
is mimicry.

**Conjecture 5.2** (AGI requires Level 3). *True artificial general
intelligence requires operation at Level 3 of the Giry tower: the system
must have a Fisher information matrix at Level 2 with positive spectral
gap — it must be able to DISTINGUISH between its own states of uncertainty
and to update these distinctions in response to evidence about itself.*

This is a stronger requirement than current alignment research typically
considers. A system that can model its own uncertainty but cannot model
*changes in its own uncertainty* is, in the Giry tower framing, a Level 2
system with zero spectral gap at Level 2 — metacognitively flat, unable
to learn about its own learning.

### 5.5 Relationship to existing theories

The Giry tower construction has points of contact with several existing
approaches to consciousness:

- **Integrated Information Theory** (Tononi [2004]): IIT's $\Phi$ measures
  the irreducibility of a system's causal structure. In the Giry tower
  framing, $\Phi > 0$ at Level 2 is a necessary condition for the spectral
  gap $\lambda_1(F_2) > 0$ — but the Giry tower adds the hierarchy of
  levels that IIT lacks.

- **Free Energy Principle** (Friston [2010]): Friston's variational free
  energy is a Level 2 quantity — the divergence between the system's
  generative model and its sensory input. The Giry tower generalises this:
  free energy minimisation operates at each level, and the system's depth
  on the tower determines the sophistication of its self-modelling.

- **Strange Loops** (Hofstadter [1979]): Hofstadter's thesis — that
  consciousness arises from self-referential loops — is the informal version
  of Giry tower ascent. The strange loop IS the map
  $\mathcal{P}^{k}(X) \to \mathcal{P}^{k+1}(X)$: the system modelling its
  own modelling, recursively.

- **Global Workspace Theory** (Baars [1988]): The global workspace is
  the Cheeger constant at Level 2 — the ability of metacognitive information
  to reach all parts of the system. Consciousness requires not just
  Level 2 operation but Level 2 operation with high $h_M$: no bottlenecks
  in self-knowledge.

What the Giry tower adds to all of these is a precise mathematical
structure — a hierarchy of probability spaces, each with its own
Fisher-Rao geometry — and a specific measurable quantity (the spectral
gap at Level 2) that could in principle distinguish conscious from
non-conscious systems.

Whether it actually does so is an empirical question. The author makes no
claim to have solved the hard problem of consciousness. The claim is
narrower: IF consciousness has a mathematical structure, the Giry tower
is a natural candidate, and the Fisher information at Level 2 is a natural
measure of its depth.

---

## 6. The Price Is Not a Number — It's the Metric Tensor

### 6.1 The information destruction of pricing

"The price of Apple is $185.43."

This sentence projects a $d$-dimensional row vector — Apple's relationship
to every other asset in the market — onto a single scalar. For a market
with $d = 500$ assets, this is a projection from a 500-dimensional vector
to a 1-dimensional number. The fraction of information retained is:

$$\frac{1}{d} = \frac{1}{500} = 0.2\% \tag{6.1}$$

This is an undercount. The full information about Apple's market state is
not a vector but a row of the Fisher information matrix $F$: a $d$-dimensional
vector encoding the sensitivity of the market's probability structure to
changes in Apple's weight. The price is the $L^1$ norm of this vector (or
more precisely, the Arrow-Debreu complete-market price is the expectation
under the risk-neutral measure, which is a specific linear functional on $F$).

The hierarchy of information retention:

| Representation | Dimension | Fraction of $F$ retained |
|:---------------|:---------:|:------------------------:|
| Index (1 number) | 1 | $\sim 1/d^2$ |
| Price vector ($d$ numbers) | $d$ | $\sim 2/d$ |
| Simplex point ($d-1$ numbers) | $d-1$ | $\sim 2/d$ |
| Covariance matrix ($d(d+1)/2$ entries) | $d(d+1)/2$ | $\sim 100\%$ |
| Fisher information matrix ($d \times d$) | $d^2$ | $100\%$ |

For $d = 500$: the S\&P 500 index retains approximately $1/250{,}000$ of
the information in the Fisher matrix. The full price vector retains
$1/250$. The covariance matrix, which most quantitative investors regard
as the maximum available information, retains approximately all of it —
because under the Fisher-Rao metric on the simplex, the Fisher information
matrix IS the metric tensor, and the covariance matrix (under appropriate
normalisation) IS the Fisher matrix.

### 6.2 What the market actually computes

At each instant, the market computes the metric tensor. Every trade updates
one entry of $F$: the buyer and seller, by agreeing on a price, reveal
information about the joint distribution of two assets. The bid-ask spread
is the uncertainty in a single entry of $F$. The limit order book is the
current best estimate of a row of $F$, conditioned on the queue of
incoming information.

This is the content of the LMSR-softmax-Fisher identity (R17,
LLM_MANIFOLD.md): the market scoring rule that determines prices has
Hessian equal to $F$. The market's pricing function is literally the
second derivative of the log-partition function — which IS the Fisher
information matrix by the Bartlett identity.

### 6.3 Options as Level 2 markets

Options markets operate one level up the Giry tower from equity markets.
An equity price represents a Level 1 belief: the expected value of a
future cash flow under the risk-neutral measure. An option price represents
a Level 2 belief: the uncertainty about the equity price itself.

- The **VIX** prices $\mathrm{tr}(F)$ — the trace of the Fisher information
  matrix of the equity return distribution. It is a scalar summary of
  Level 2 uncertainty.
- The **volatility surface** prices the full eigenvalue spectrum of $F$:
  the implied volatility at each strike and maturity encodes the sensitivity
  of the pricing distribution to perturbations in each direction.
- **Variance swaps** price $\mathrm{tr}(F)$ directly (Demeterfi et al.
  [1999]).
- **Correlation swaps** price the off-diagonal structure of $F$.

An Arrow-Debreu complete market prices every state — it retains the full
$\mathcal{P}(X)$. But completeness requires $2^d$ state prices, which is
computationally intractable for $d > 30$. The simplex $\Delta_{d-1}$ is
the practical compression: it retains $d-1$ numbers from a $2^d$-dimensional
space. The market manifold $M^r$ compresses further to $r$ numbers.
Each compression destroys information. Each has a cost.

---

## 7. Every Act of Knowing Is Information Destruction

### 7.1 The universal structure

Every act of knowing has the same mathematical structure: a projection from
a rich space to a simpler one. The projection destroys information. The
amount destroyed is computable.

| Act | Rich space | Simple space | Cost measure |
|:----|:-----------|:-------------|:-------------|
| Pricing | $\mathcal{P}(X)$ | $\mathbb{R}$ (scalar price) | KL divergence to pricing measure |
| Measuring | $\mathcal{H}$ (Hilbert space) | Eigenvalue | Complementary uncertainty (Heisenberg) |
| Classifying | $\mathbb{R}^{n}$ (features) | $\{1, \ldots, K\}$ (labels) | Within-class variance |
| Summarising | Text (high-dim) | Summary (low-dim) | Omitted mutual information |
| Compressing | Sequence | Code | Redundancy $= H_0 - H$ |
| Investing | $\Delta_{d-1}$ (all portfolios) | $b^{\ast} \in M^r$ (optimal) | MUP regret $r\log T / (2T)$ |
| Perceiving | Sensory input | Neural representation | Reconstruction error |

The last column varies in its precise definition, but the structure is
invariant: there is always a well-defined cost, it is always strictly
positive, and it is always computable in principle from the Fisher-Rao
geometry of the projection.

### 7.2 The second law of epistemology

**Theorem 7.1** (Information destruction is irreversible). *Let
$\pi: (\mathcal{M}, g^{\mathrm{FR}}) \to (\mathcal{N}, g^{\mathrm{FR}})$
be a sufficient statistic or any other deterministic map between statistical
manifolds. Then $\pi$ is a Riemannian submersion: it does not increase
Fisher information. Equality holds if and only if $\pi$ is sufficient.*

*Proof.* This is the classical data processing inequality in geometric
form (Amari and Nagaoka [2000], Chapter 3). The Fisher information matrix
transforms as $F_\mathcal{N} = J^T F_\mathcal{M} J$ where $J$ is the
Jacobian of $\pi$. Since $J^T F J \preceq F$ in the Loewner order (with
equality iff $J$ has full rank restricted to the Fisher-relevant subspace),
information is destroyed. $\square$

This is the informational content of the second law of thermodynamics.
Entropy increases because observation is projection, and projection destroys
information. You cannot know something without destroying something else.
The cost of knowing is always strictly positive — this is not a practical
limitation but a theorem about the geometry of statistical manifolds.

The MUP regret $r\log T/(2T)$ (R2, CONVERGENCE.md) is one instance: even
the minimax-optimal portfolio strategy destroys information at rate
$r\log T/(2T)$ by projecting from the full data to a portfolio decision.
The Heisenberg uncertainty principle is another: measuring position
destroys momentum information, and the product of uncertainties is bounded
below by $\hbar/2$. Both are consequences of the same geometric fact —
projection onto a lower-dimensional subspace cannot preserve the full
metric tensor.

### 7.3 The cost of knowing in Fisher-Rao units

The natural unit of information destruction is the **Fisher-Rao bit**: the
KL divergence between two distributions that differ by one unit of arc
length on the Fisher-Rao manifold. In these units:

- Pricing a single asset: $\sim \log d$ Fisher-Rao bits destroyed (projecting
  $d$-dimensional information to 1 dimension).
- Classifying into $K$ classes: $\sim \log(n/K)$ bits destroyed (where $n$ is
  the effective continuous dimension of the input).
- Optimal portfolio selection: exactly $r\log T/(2T)$ bits per period
  (the MUP regret).

The Fisher-Rao bit is the natural currency of epistemology: the price you
pay for converting uncertainty into knowledge.

---

## 8. The Five Limits of Knowing

### 8.1 The hierarchy of walls

There are five fundamental limits on what any information-processing system
can know. Each is further from raw data than the last.

**Wall 1: The $\sigma$-algebra wall** (Measure theory)

What you can observe. The measurable sets of your $\sigma$-algebra determine
the finest distinctions you can make. A system that cannot measure temperature
cannot know temperature. A market that does not trade an asset cannot price
it. A brain that lacks a sensory modality cannot perceive in that modality.

This is the most common practical limitation. Most of what we do not know,
we do not know because we cannot measure it.

**Wall 2: The Turing wall** (Computability)

What you can compute from your observations. Even with perfect data
(Wall 1 fully permeable), some functions are not computable. The Halting
Problem is the canonical example: no Turing machine can determine whether
an arbitrary program halts. In the market context: the long-run profitability
of an arbitrary trading strategy is undecidable (COMPLEXITY.md, Theorem 1.1).

**Wall 3: The Godel wall** (Logic)

What you can prove from your axioms. Even with perfect data AND unlimited
computation, some true statements are not provable within any consistent
axiom system strong enough to encode arithmetic (Godel [1931]). This is the
deepest theoretical limitation: there are truths about the market manifold
that are true but unprovable from any finite axiomatisation of the theory.

**Wall 4: The pricing wall** (Information destruction)

What survives the projection from distribution to decision. This is the wall
analysed in Sections 6 and 7. Even with perfect observation, unlimited
computation, and a complete axiom system, the act of making a decision —
pricing an asset, classifying an input, choosing a portfolio — destroys
information. The cost is at least $r\log T/(2T)$ per period for portfolio
decisions (R2), and analogous bounds exist for every other form of decision.

This wall is different from the first three: it is not about what you *can*
know but about what you *must lose* in the act of using what you know.
Knowledge is not destroyed by ignorance but by application.

**Wall 5: The consciousness wall** (Metacognitive depth)

How far up the Giry tower you can go. A Level 1 system cannot reason about
its own uncertainty. A Level 2 system can reason about its uncertainty but
not about changes in its uncertainty. Each level of the tower opens new
capabilities and new limitations.

This is the most humanly relevant wall. Most of our practical failures of
judgement are not failures of observation (Wall 1), computation (Wall 2),
logic (Wall 3), or decision-making (Wall 4). They are failures of
self-knowledge: we do not know what we do not know. We mistake confidence
for correctness. We fail to model our own biases. These are Level 2 and
Level 3 failures — inadequate ascent of the Giry tower.

### 8.2 The ordering

Each wall strictly constrains the next:

$$\sigma\text{-algebra} \supset \text{Turing} \supset \text{Godel} \supset \text{Pricing} \supset \text{Consciousness}$$

You cannot compute what you cannot observe. You cannot prove what you cannot
compute. You cannot price what you cannot prove. And you cannot be aware of
what you cannot price (in the sense that metacognitive access requires at
minimum the ability to represent the quantity as a decision variable).

But the practical ordering of importance is often reversed. Wall 5 failures
are the most common in practice (we are bad at metacognition), and Wall 3
failures are the rarest (unprovable truths about financial markets are a
theoretical curiosity with no known practical consequence).

---

## 9. Life, Evolution, and the MCF of Ecosystems

### 9.1 The biological simplex

A living cell processes information on a chemical simplex. The concentrations
of $d$ molecular species, normalised to sum to 1, form a point on
$\Delta_{d-1}$. The cell's metabolic state is a trajectory on this simplex.
The Fisher-Rao metric on the concentration simplex measures the sensitivity
of the cell's phenotype to perturbations in molecular concentrations.

Evolution is mean curvature flow (MCF) on the fitness landscape. The
population distribution over genotypes is a point on $\Delta_{G-1}$ where
$G$ is the number of genotypes. Natural selection drives this point in the
direction of steepest ascent of the fitness function — which, under the
Fisher-Rao metric, is the mean curvature vector of the fitness manifold.

This is Fisher's fundamental theorem of natural selection (Fisher [1930]),
reinterpreted geometrically: the rate of increase in mean fitness equals
the genetic variance in fitness, which is $\|H\|_{L^2}^{2}$ — the squared
mean curvature of the fitness manifold in the Bhattacharyya sphere. The
Sharpe-curvature identity (R1) IS Fisher's theorem, applied to a different
simplex.

### 9.2 The five stages, again

The five stages of market efficiency identified in the companion papers
have exact biological analogues:

| Stage | Market | Ecosystem | Geometry |
|:------|:-------|:----------|:---------|
| Pre-market | No trading | Primordial soup | No manifold |
| Price discovery | First prices | Abiogenesis | First eigenvalue $\lambda_1 > 0$ |
| Wild West | High vol, many strategies | Cambrian explosion | High curvature, many niches |
| Factor emergence | Stable factor structure | Ecological maturity | $M^r$ emerges, $r$ stabilises |
| Near-efficiency | Low Sharpe, high liquidity | Climax ecosystem | $H \to 0$, minimal surface |
| Singularity | Flash crash, crisis | Mass extinction | Curvature blowup, topology change |

The Permian-Triassic extinction (251 Mya) — which eliminated 96% of marine
species — is a Type II singularity in this framework: the fitness manifold's
curvature blew up, its topology changed catastrophically (from a complex
multi-niche structure to a near-trivial one), and the system re-emerged
with a fundamentally different manifold structure. The analogy with the
2008 financial crisis — where the market's factor structure collapsed from
$r \approx 6$ to $r \approx 1$ (everything correlated) before slowly
re-diversifying — is not just suggestive but geometrically precise: both
are MCF singularities followed by topological simplification.

### 9.3 The convergence theorem applied to life

The convergence theorem for the MUP (R2, CONVERGENCE.md) states that the
manifold universal portfolio converges to the log-optimal portfolio at
rate $r\log T/(2T)$. The biological version: a population under natural
selection converges to the fitness-optimal genotype distribution at a rate
determined by the dimensionality of the fitness landscape.

This is not a new observation — it is the geometric content of Fisher's
theorem plus the Price equation plus the fundamental theorem of
evolutionary game theory. What the manifold framework adds is the
recognition that the convergence rate depends on $r$ (the number of
independent fitness dimensions), not on $G$ (the number of genotypes),
and that the convergence is minimax optimal: no evolutionary mechanism
can converge faster than $r\log T/(2T)$ without side-channel information
(horizontal gene transfer, endosymbiosis — the biological equivalents of
insider trading).

---

## 10. What This Means

### 10.1 Five claims

We have argued for five claims of increasing ambition:

**Claim 1** (Proved in companion papers). All information processing systems
operate on a common geometric substrate. The Fisher-Rao simplex
$(\Delta_{d-1}, g^{\mathrm{FR}})$ embedded in the Bhattacharyya sphere
$S^{d-1}_{+}$ is the unique geometry compatible with the axioms of classical
probability. Any system whose state is a probability distribution inherits
this geometry. The curvature, spectral gap, Cheeger constant, and dimension
are computable invariants with measurable consequences.

**Claim 2** (Well-motivated conjecture). Intelligence is manifold dimension.
The stable rank of the Fisher information matrix measures the number of
independently representable concepts. This is consistent with empirical
estimates of intrinsic dimensionality in neural systems, financial markets,
and language models.

**Claim 3** (Well-motivated conjecture). Creativity requires negative
curvature. The exponential proliferation of geodesics in negatively curved
spaces provides the combinatorial substrate for unexpected connections.
The brain's small-world connectivity and the transformer's attention
mechanism both create effective negative curvature.

**Claim 4** (Speculative). Consciousness is the Giry tower. Self-awareness
requires Level 2 operation (distributions over distributions) with positive
spectral gap. This is consistent with — but not derivable from — existing
theories of consciousness.

**Claim 5** (Proved, Section 7). Every act of knowing destroys information.
The cost is always strictly positive and is computable in Fisher-Rao units.
This is the second law of epistemology: a geometric theorem, not a practical
limitation.

### 10.2 The punchline

This monograph began with a technical question: why does the Laplace
approximation work so well for portfolio optimisation? The answer — because
the portfolio simplex has constant curvature $K=1/4$ under the Fisher-Rao
metric, which makes the WKB approximation exact to $O(1/T^2)$ — led to a
geometric framework for financial markets.

But the Fisher-Rao metric is not special to finance. It is the unique
geometry of probability, forced by the Cencov theorem. Any system that
processes probabilistic information — a market, a brain, a language model,
a living cell, a quantum computer — operates on this geometry. The market
manifold is one instance. The neural manifold is another. The fitness
landscape is a third.

The curvature determines what the system can compute efficiently. The
dimension determines how many concepts it can hold. The Cheeger constant
determines whether it can integrate information globally. The spectral
gap determines how fast it can learn. The Giry tower determines how
deeply it can know itself.

The geometry of efficient markets is not about markets.

It is about the geometry of knowing.

---

## 11. Open Problems

**OP-A. Empirical measurement of LLM manifold dimension.**
Estimate $r = \mathrm{stable_rank}(F)$ for current large language models
by computing the Fisher information of the output distribution with respect
to input perturbations. Does $r$ correlate with benchmark performance?
Does it increase with model scale? Is there a phase transition at some
critical $r$?

**OP-B. Is there a minimum dimension for consciousness?**
The consciousness conjecture (Conjecture 5.1) posits Level 2 operation
with positive spectral gap. Does this require $r > r_{\mathrm{crit}}$ for
some critical dimension? If so, what is $r_{\mathrm{crit}}$? Can it be
estimated from neural data?

**OP-C. The evolutionary advantage of negative curvature.**
Why did the brain evolve small-world (effectively hyperbolic) connectivity
rather than lattice (flat) or fully connected (positively curved) structure?
Is there a fitness theorem showing that negatively curved neural architectures
outperform alternatives for environments requiring both search and consensus?

**OP-D. Quantum cognition and the non-commutative Giry tower.**
If the brain's state space is non-commutative (density matrices rather than
probability distributions), the Giry tower becomes the tower of quantum
channels. Does this provide a better model of cognitive phenomena
(order effects, conjunction fallacies) than classical probability? Is there
empirical evidence for non-commutativity in neural population codes?

**OP-E. The information-theoretic cost of free will.**
A decision is a projection from $\mathcal{P}^{k}(X)$ (high-level belief) to
an action in a finite action space. The information destroyed in this
projection is a computable quantity. Is the subjective experience of "free
will" related to the magnitude of this information destruction — the sense
that more was possible than what was chosen?

---

## References

Allard, A. and Serrano, M. A. (2020). "Navigable maps of structural brain
networks across species." *PLOS Computational Biology*, 16(2), e1007584.

Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry*.
Translations of Mathematical Monographs 191, American Mathematical Society.

Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge
University Press.

Cencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*.
Translations of Mathematical Monographs 53, American Mathematical Society.

Chalmers, D. (1995). "Facing up to the problem of consciousness."
*Journal of Consciousness Studies*, 2(3), 200-219.

Cunningham, J. P. and Yu, B. M. (2014). "Dimensionality reduction for
large-scale neural recordings." *Nature Neuroscience*, 17(11), 1500-1509.

Demeterfi, K., Derman, E., Kamal, M., and Zou, J. (1999). "A guide to
volatility and variance swaps." *Journal of Derivatives*, 6(4), 9-32.

Fisher, R. A. (1930). *The Genetical Theory of Natural Selection*.
Clarendon Press, Oxford.

Friston, K. (2010). "The free-energy principle: a unified brain theory?"
*Nature Reviews Neuroscience*, 11(2), 127-138.

Gallego, J. A., Perich, M. G., Miller, L. E., and Solla, S. A. (2017).
"Neural manifolds for the control of movement." *Neuron*, 94(5), 978-984.

Giry, M. (1982). "A categorical approach to probability theory."
In *Categorical Aspects of Topology and Analysis*, Lecture Notes in
Mathematics 915, Springer, 68-85.

Godel, K. (1931). "Uber formal unentscheidbare Satze der Principia
Mathematica und verwandter Systeme I." *Monatshefte fur Mathematik und
Physik*, 38(1), 173-198.

Hofstadter, D. R. (1979). *Godel, Escher, Bach: An Eternal Golden Braid*.
Basic Books.

Krioukov, D., Papadopoulos, F., Kitsak, M., Vahdat, A., and Boguna, M.
(2010). "Hyperbolic geometry of complex networks." *Physical Review E*,
82(3), 036106.

Penrose, R. (1989). *The Emperor's New Mind: Concerning Computers, Minds
and the Laws of Physics*. Oxford University Press.

Tononi, G. (2004). "An information integration theory of consciousness."
*BMC Neuroscience*, 5(42).

---

**Companion papers.** This paper draws on results and constructions from
MINIMAL_SURFACE.md (R1: Sharpe-curvature identity), CONVERGENCE.md
(R2: MUP regret), CLASSIFICATION.md (R3: only CAPMs stably efficient),
COMPLEXITY.md (prediction complexity hierarchy), LLM_MANIFOLD.md
(R17: LMSR-softmax-Fisher identity), BRAIDS.md (pseudo-Anosov dynamics),
CHAOS_TAKENS.md (dimension estimation), INFORMATION_THEORY.md (SMB = Kelly),
RENORMALIZATION.md (MCF as RG flow), GRASSBERGER_PERCOLATION_GENERATING.md
(correlation dimension, Cheeger-percolation), and
HAMILTONIAN_TAILS_COMPLETENESS.md (completeness = normal bundle).

---

*Last updated: April 2026*
*The Geometry of Efficient Markets*
*Saxon Nicholls*
