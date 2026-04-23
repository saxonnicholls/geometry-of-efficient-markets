# The Convexification of Information:
## Free Convex Completions, Sobolev Regularity, and the Canonical
## Embedding of Non-Convex Spaces into Information Geometry

**Saxon Nicholls** — me@saxonnicholls.com

**Paper 0.2** — Foundation

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
Paper 0.1 established that classical commutative information processing
operates on a geodesically convex subset of the Fisher-Rao simplex. This
paper asks the next question: given a space that is NOT convex — a manifold
with holes, a negatively curved space, a discrete combinatorial object — is
there a canonical way to embed it into a convex information-processing space,
and what is the cost?

We develop three answers.

**First — the free convex completion:**

```math
\mathcal{P}(X) = \{\text{Borel probability measures on } X\}
```

with the Dirac embedding $x \mapsto \delta_x$. This is the universal
convexification — it embeds any measurable space into a convex space while
preserving all structure that can be preserved.

**Second — the symmetry convexification:**

```math
\mathcal{C}_{G}(X) = \text{orbit-averaged space of } X \text{ under group } G
```

which convexifies by exploiting symmetry.

**Third — the Sobolev convexification:** when $X$ lacks the smoothness
required by Čencov's theorem, we work in the Sobolev space

```math
W^{1,2}(\Delta_{d-1},\, g^{\rm FR})
```

where the Fisher-Rao metric is defined in the weak sense, extending the
information-geometric framework to non-smooth state spaces.

The central result: **convexification is probabilification**. The passage
from any space to its convex completion is, in every known case, the passage
from deterministic/pure/individual descriptions to
probabilistic/mixed/averaged descriptions. The convex hull operator, the
Legendre-Fenchel biconjugate, the density matrix construction, Reynolds
averaging, and ergodic time-averaging are all the same operation viewed from
different mathematical traditions.

**Principal results:**

**(i) The Free Convex Completion Theorem.** For any Polish space $X$, the
space of Borel probability measures $\mathcal{P}(X)$ with the weak-*
topology is a compact convex subset of a locally convex topological vector
space. The Dirac embedding $\iota: X \hookrightarrow \mathcal{P}(X)$,
$\iota(x) = \delta_x$, is a homeomorphism onto the extreme points of
$\mathcal{P}(X)$. This is the universal convexification: any affine map
from $\mathcal{P}(X)$ to a convex set $C$ factors uniquely through $\iota$.

**(ii) The Convexification Dimension.** The minimum ambient dimension $N$
required to embed a compact $r$-manifold $M^r$ into a convex subset of
$S^{N-1}_{+}$ is bounded by $N \geq 2r + 1$ (Whitney) and $N \leq r(r+3)/2 + 1$
(Nash). The gap between these bounds is the *convexification overhead* — the
price of making a non-convex space convex.

**(iii) The Sobolev Extension of Čencov.** When the state space has
regularity $W^{1,2}$ but not $C^\infty$, the Fisher-Rao metric is defined
as a weak Riemannian metric in the Sobolev sense. The monotonicity theorem
(Axiom 2) extends to $W^{1,2}$ channels via the theory of Sobolev mappings
between metric spaces (Ambrosio-Gigli-Savaré). The Čencov uniqueness
result holds in $W^{1,2}$ under a Muckenhoupt $A_2$ weight condition on the
state space boundary.

**(iv) Negative Curvature Embeds With Mandatory Alpha.** A compact manifold
$M^r$ with sectional curvature $K_M \leq -\kappa^2 < 0$ embedded
isometrically in $S^{N-1}_{+}$ must have extrinsic mean curvature
$\|H\| \geq c(r, \kappa)> 0$. By the Sharpe-curvature identity, this
means hyperbolic markets necessarily have positive alpha: chaos creates
exploitable inefficiency, with a lower bound determined by the intrinsic
curvature.

**(v) Ergodic Convexification = Birkhoff.** For an ergodic dynamical system
$(X, T, \mu)$, the time-average map $\mathcal{E}: X \to \mathcal{P}(X)$,
$\mathcal{E}(x) = \lim_{N\to\infty}\frac{1}{N}\sum_{n=0}^{N-1}\delta_{T^n x}$,
is a convexification. The Birkhoff ergodic theorem says $\mathcal{E}(x) = \mu$
for $\mu$-a.e. $x$. Ergodic averaging IS the free convex completion
restricted to a single orbit.

**Keywords.** Convexification; free convex completion; probability measures;
Dirac embedding; Legendre-Fenchel; Sobolev spaces; Fisher-Rao; Čencov;
Muckenhoupt weights; negative curvature; ergodic theorem; density matrices;
Reynolds averaging; orbit polytope; information geometry.

---

## 1. The Problem: Non-Convex Spaces in a Convex Theory

### 1.1 The tension

Paper 0.1 showed that information processing must happen in a convex space.
But the world is full of non-convex objects:

- The efficient market manifold $M^r$ can be a torus (non-convex: has a hole)
  or hyperbolic (negatively curved)
- Pure quantum states form $\mathbb{CP}^{n}$ (projective space: non-convex)
- Combinatorial objects (graphs, trees, codes) are discrete (not even continuous)
- Game-theoretic equilibria can lie on non-convex subsets of the strategy space
- Financial time series have jumps and discontinuities (not smooth)

How do these non-convex objects participate in information processing?

### 1.2 The resolution: ambient vs intrinsic

The key distinction, which Paper 0.1 noted but did not develop:

**Ambient convexity** is a property of the space $\mathcal{S}$ in which
information processing occurs (the portfolio simplex, the space of
distributions). This is what the axioms force.

**Intrinsic geometry** is a property of the submanifold $M^r \subset \mathcal{S}$
on which the system's states actually lie. This can be non-convex, negatively
curved, or topologically complex.

The market manifold $M^r$ lives INSIDE the convex simplex $\Delta_{d-1}$.
The simplex is convex (forced by the axioms). The manifold need not be.
Information processing happens in the ambient convex space; the dynamics are
constrained to the submanifold.

This paper develops the theory of how non-convex spaces embed into convex
ambient spaces, what structure is preserved, and what is gained.

### 1.3 Three convexification strategies

We develop three approaches, each suited to different situations:

| Strategy | Input | Output | Mechanism |
|:---------|:------|:-------|:----------|
| **Free completion** $\mathcal{P}(X)$ | Any measurable space $X$ | Convex space of measures | Take all mixtures |
| **Symmetry** $\mathcal{C}_{G}(X)$ | Space $X$ with group action $G$ | Convex orbit space | Average over orbits |
| **Sobolev extension** | Non-smooth space | $W^{1,2}$ Riemannian | Weak Fisher-Rao metric |

---

## 2. The Free Convex Completion

### 2.1 Construction

**Definition 2.1** (Free convex completion). *Let $X$ be a Polish space
(complete separable metric). The free convex completion of $X$ is the space
of Borel probability measures:*
```math
\mathcal{P}(X) = \{\mu : \mu \text{ is a Borel probability measure on } X\} \tag{2.1}
```
*equipped with the weak-* topology (convergence against bounded continuous
test functions).*

**The Dirac embedding** $\iota: X \hookrightarrow \mathcal{P}(X)$ sends each
point to its Dirac mass:
```math
\iota(x) = \delta_x \tag{2.2}
```

**Theorem 2.1** *(Free convex completion — Choquet theory).*

Let $X$ be a compact metrizable space. Then:

**(i)** $\mathcal{P}(X)$ is a compact convex subset of the locally convex
space $C(X)^{\ast}$ (dual of continuous functions).

**(ii)** The extreme points of $\mathcal{P}(X)$ are exactly the Dirac
masses:

```math
\mathrm{ext}(\mathcal{P}(X)) = \{\delta_x : x \in X\}.
```

**(iii)** (Choquet representation) Every $\mu \in \mathcal{P}(X)$ has a
unique representation as a mixture of extreme points:

```math
\mu = \int_X \delta_x \, d\mu(x).
```

**(iv)** (Universal property) For any continuous affine map $\phi: \mathcal{P}(X) \to C$ into a convex set $C$, there exists a unique
continuous map $f: X \to C$ such that

```math
\phi(\mu) = \int_X f(x) \, d\mu(x).
```

$\mathcal{P}(X)$ is the "free" convex set over $X$.

*Proof.* Parts (i)–(iii) are the content of Choquet's theorem (Phelps 1966).
Part (iv) is the universal property of the probability monad
(Giry 1982; Fritz 2020). $\square$

### 2.2 Why this IS convexification

The free convex completion answers the question "what is the smallest convex
space containing $X$?" Answer: the space of probability measures on $X$.

**The passage from $X$ to $\mathcal{P}(X)$ is the passage from deterministic
to probabilistic.** Every known convexification is a special case:

| Domain | $X$ (non-convex) | $\mathcal{P}(X)$ (convex) | Name of the passage |
|:-------|:-----------------|:--------------------------|:-------------------|
| Quantum mechanics | Pure states $\mathbb{CP}^{n}$ | Density matrices $\mathcal{D}_{n}$ | Purification → mixing |
| Game theory | Pure strategies $\{1,\ldots,d\}$ | Mixed strategies $\Delta_{d-1}$ | Deterministic → randomised |
| Finance | Individual assets $\{1,\ldots,d\}$ | Portfolios $\Delta_{d-1}$ | Single stock → diversification |
| Dynamical systems | Phase space $M$ | Invariant measures $\mathcal{P}_{T}(M)$ | Trajectory → ergodic measure |
| Statistics | Parameter space $\Theta$ | Priors/posteriors $\mathcal{P}(\Theta)$ | Point estimate → distribution |
| Optimisation | Feasible set $S$ | Relaxation $\mathrm{conv}(S)$ | Integer → continuous |

In every case, the "non-convex" object is a set of deterministic/pure states,
and the convexification is the set of all probability mixtures over those states.

### 2.3 The Fisher-Rao metric on $\mathcal{P}(X)$

When $X$ is finite ($|X| = d$), $\mathcal{P}(X) = \Delta_{d-1}$ and the
Fisher-Rao metric is the standard one:
```math
g^{\rm FR}_{ij}(\mu) = \frac{\delta_{ij}}{\mu_i} \tag{2.3}
```

When $X$ is a smooth manifold, $\mathcal{P}(X)$ is infinite-dimensional and
the Fisher-Rao metric generalises to:
```math
g^{\rm FR}_\mu(\dot\mu_1, \dot\mu_2) = \int_X \frac{\dot\mu_1(x)\,\dot\mu_2(x)}{\mu(x)}\,dx \tag{2.4}
```

where $\dot\mu_i$ are tangent vectors (signed measures with $\int\dot\mu_i = 0$)
and $\mu(x)$ is the density of $\mu$ with respect to a reference measure.

**Theorem 2.2** *(Infinite-dimensional Čencov)*.
*On $\mathcal{P}(X)$ for a smooth manifold $X$, the Fisher-Rao metric (2.4)
is the unique (up to scale) Riemannian metric that is:*
*(i) invariant under sufficient statistics (Markov morphisms)*
*(ii) defined on the tangent space of $\mathcal{P}(X)$ at each smooth density*

*This is the infinite-dimensional extension of Čencov's theorem
(Ay-Jost-Lê-Schwachhöfer 2017).*

### 2.4 The Bhattacharyya embedding generalises

The finite-dimensional Bhattacharyya embedding $\phi: p \mapsto \sqrt{p}$
generalises to infinite dimensions:
```math
\Phi: \mathcal{P}(X) \to L^2(X), \quad \Phi(\mu) = \sqrt{d\mu/dx} \tag{2.5}
```

The image lies on the unit sphere $S^\infty$ in $L^2(X)$ (since $\int|d\mu/dx|dx = 1$
implies $\|\Phi(\mu)\|^2 = 1$). The Bhattacharyya distance becomes:
```math
d_B(\mu, \nu) = \arccos\int_X\sqrt{\frac{d\mu}{dx}\cdot\frac{d\nu}{dx}}\,dx \tag{2.6}
```

The positive orthant $S^\infty_+$ (non-negative square roots) is geodesically
convex in $S^\infty$ by the same argument as Theorem 4.2 of Paper 0.1.

**Corollary.** The free convex completion $\mathcal{P}(X)$, equipped with the
Fisher-Rao metric and the Bhattacharyya embedding, is a geodesically convex
subset of the infinite-dimensional unit sphere. This is the
infinite-dimensional version of Paper 0.1's main theorem.

---

## 3. The Convexification Dimension

### 3.1 How many extra dimensions does convexification cost?

Given a compact $r$-dimensional manifold $M^r$ that is NOT convex, what is
the minimum ambient dimension $N$ such that $M^r$ embeds in a convex subset
of $S^{N-1}_{+}$?

**Definition 3.1** (Convexification dimension). *The convexification dimension
$N_{\rm conv}(M)$ of a compact manifold $M$ is the minimum $N$ such that there
exists an isometric embedding $M \hookrightarrow S^{N-1}_{+}$ where $S^{N-1}_{+}$
is geodesically convex.*

**Theorem 3.1** *(Bounds on convexification dimension)*.
*For a compact $r$-dimensional Riemannian manifold $M^r$:*

*(i) (Whitney lower bound) $N_{\rm conv}(M) \geq 2r + 1$.*

*(ii) (Nash upper bound) $N_{\rm conv}(M) \leq r(r+3)/2 + 1$ for $C^3$ embeddings.*

*(iii) (Topological contribution) If $M$ has first Betti number $\beta_1(M) > 0$
(non-trivial loops), then $N_{\rm conv}(M) \geq 2r + 1 + \beta_1(M)$.
Each independent hole requires at least one extra ambient dimension.*

*Proof sketch.* (i) follows from Whitney's embedding theorem: any smooth
$r$-manifold embeds in $\mathbb{R}^{2r+1}$, and the image can always be
placed in the positive orthant of a sphere of sufficiently large dimension.
(ii) follows from Nash's isometric embedding theorem. (iii) follows from the
topological constraint: to embed a manifold with a non-contractible loop in a
convex ambient space, the loop must be "filled" by the convex hull, requiring
at least one extra dimension per independent loop. $\square$

### 3.2 The three market types and their convexification cost

| Market type | $M^r$ | $\beta_1$ | Intrinsic curvature | $N_{\rm conv}$ | Extra dims |
|:-----------|:------|:---------:|:-------------------|:--------------:|:----------:|
| CAPM | $S^r_+$ (hemisphere) | 0 | $K = +1/4$ | $r + 1$ | 0 |
| Clifford | $T^2$ (torus) | 2 | $K = 0$ | $\geq 7$ | $\geq 2$ |
| Pseudo-Anosov | $\Sigma_g$ (genus $g$) | $2g$ | $K < 0$ | $\geq 2r+1+2g$ | $\geq 2g$ |

**Interpretation:** The CAPM market is already convex (it is a piece of a
sphere). No extra dimensions are needed. The Clifford torus has two holes
($\beta_1 = 2$), requiring at least 2 extra ambient dimensions. A hyperbolic
market of genus $g$ requires $2g$ extra dimensions — one per handle.

**The financial interpretation of extra dimensions:** Each extra ambient
dimension corresponds to an additional degree of freedom that the convex
ambient space has but the market manifold does not use. In portfolio terms:
these are the $d - r$ idiosyncratic directions that the factor model
projects away. The idiosyncratic dimensions are the *price of convexifying
the factor structure*.

---

## 4. Negative Curvature and Mandatory Alpha

### 4.1 The embedding curvature bound

**Theorem 4.1** *(Negative intrinsic curvature forces extrinsic curvature)*.
*Let $M^r$ be a compact Riemannian manifold with sectional curvature
$K_M \leq -\kappa^2 < 0$, isometrically embedded in $S^{N-1}(1/2)$
(the Bhattacharyya sphere of curvature $K = 1/4$). Then the mean
curvature satisfies:*

```math
\|H\|^2_{L^2(M)} \geq \frac{r(r-1)}{4}\left(\kappa^2 + \frac{1}{4}\right)\mathrm{vol}(M) \tag{4.1}
```

*Proof.* By the Gauss equation for a submanifold of $S^{N-1}(1/2)$:
```math
K_M(\sigma) = \frac{1}{4} + \langle B(e_1, e_1), B(e_2, e_2)\rangle - |B(e_1, e_2)|^2 \tag{4.2}
```

where $\sigma = \mathrm{span}(e_1, e_2)$ is a 2-plane and $B$ is the second
fundamental form. Since $K_M \leq -\kappa^2$:
```math
\langle B(e_1,e_1), B(e_2,e_2)\rangle - |B(e_1,e_2)|^2 \leq -\kappa^2 - \frac{1}{4} \tag{4.3}
```

Summing over an orthonormal basis and using $|H|^2 \geq \frac{1}{r}|B|^2$
(from the trace inequality):
```math
|H|^2 \geq \frac{r-1}{r}\left(\kappa^2 + \frac{1}{4}\right) \tag{4.4}
```

Integrating over $M$ gives (4.1). $\square$

### 4.2 The mandatory alpha theorem

**Corollary 4.2** *(Hyperbolic markets have mandatory positive alpha)*.
*If the efficient market manifold $M^r$ has everywhere negative sectional
curvature ($K_M \leq -\kappa^2 < 0$), then:*

```math
\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(M)} \geq \sqrt{\frac{r(r-1)}{4}\left(\kappa^2 + \frac{1}{4}\right)\mathrm{vol}(M)} > 0 \tag{4.5}
```

*A hyperbolic market cannot be efficient in the strong sense ($H = 0$).
There is a mandatory positive alpha, with a computable lower bound determined
by the intrinsic curvature and the manifold volume.*

**Interpretation.** This is remarkable. It says:

1. **Chaos creates alpha.** The pseudo-Anosov market type (Paper I.4) has
   negative curvature and chaotic dynamics. Theorem 4.1 says this chaos
   necessarily creates exploitable inefficiency. The more chaotic the market
   (larger $\kappa$), the more alpha is available.

2. **The alpha is geometric, not informational.** This alpha doesn't come
   from private information or superior analysis. It comes from the shape
   of the market manifold itself. Even an investor with no private information
   can capture it — they just need to know the topology.

3. **Only flat or positively curved markets can be truly efficient.** This
   explains why the classification theorem (Paper I.4) found that only CAPMs
   (positive curvature) and Clifford tori (zero curvature) can have $H = 0$.
   Negative curvature is incompatible with $H = 0$ in the Bhattacharyya sphere.

4. **The lower bound is computable.** Given estimates of $r$, $\kappa$, and
   $\mathrm{vol}(M)$, equation (4.5) gives a minimum Sharpe ratio for any
   strategy on a hyperbolic market. This is a testable prediction.

### 4.3 Connection to the Gauss-Bonnet theorem

For surfaces ($r = 2$):
```math
\int_M K_M \, d\mathrm{vol} = 2\pi\chi(M) = 2\pi(2 - 2g) \tag{4.6}
```

If $M$ has genus $g \geq 2$ (the pseudo-Anosov case):
```math
\int_M |K_M| \, d\mathrm{vol} \geq 4\pi(g - 1) \tag{4.7}
```

Combined with the embedding curvature bound (4.1):
```math
\mathrm{Sharpe}^{\ast} \geq c \cdot \sqrt{g - 1} \tag{4.8}
```

**The genus of the market manifold gives a lower bound on the achievable
Sharpe ratio.** Higher topological complexity (more handles) means more
mandatory alpha. This connects topology to finance in the most direct way
possible.

---

## 5. Symmetry Convexification

### 5.1 The Reynolds operator

**Definition 5.1** (Reynolds/symmetry convexification). *Let $G$ be a compact
group acting continuously on a space $X$ by isometries. The Reynolds operator is:*

```math
\mathcal{R}_{G}: X \to \mathrm{conv}(\mathrm{orbit}), \quad
\mathcal{R}_{G}(x) = \int_G g \cdot x \, d\mu_G(g) \tag{5.1}
```

*where $\mu_G$ is the normalised Haar measure on $G$.*

The Reynolds operator projects any point onto the convex hull of its orbit.
It is idempotent ($\mathcal{R}_{G}^{2} = \mathcal{R}_{G}$), linear, and $G$-invariant
($\mathcal{R}_{G}(g\cdot x) = \mathcal{R}_{G}(x)$).

### 5.2 Financial applications of symmetry convexification

**The equal-weight portfolio is a Reynolds operator.** The symmetric group
$S_d$ acts on $\Delta_{d-1}$ by permuting coordinates. The Reynolds operator
for $S_d$ sends any portfolio $b$ to the equal-weight portfolio:
```math
\mathcal{R}_{S_d}(b) = \frac{1}{d!}\sum_{\sigma \in S_d}\sigma(b)
= \left(\frac{1}{d}, \ldots, \frac{1}{d}\right) = b^{\rm ew} \tag{5.2}
```

**Interpretation:** Equal-weight investing is the symmetry convexification of
any portfolio under the permutation group. It is the maximally convexified
portfolio — the one that uses ALL the symmetry of the asset universe.

**Partial symmetry: sector-neutral portfolios.** If $G = S_{d_1} \times \cdots \times S_{d_k}$
(permutations within sectors, not between), the Reynolds operator gives the
sector-neutral portfolio — equal weight within sectors, not across.

**The MUP as a continuous Reynolds operator.** The MUP integrates over the
market manifold $M^r$ with wealth weighting. This is a generalised Reynolds
operator where the "group" is the continuous family of log-optimal portfolios
parametrised by $M^r$, and the "Haar measure" is the wealth-weighted volume:
```math
b^{\rm MUP} = \frac{\int_{M^r} b \, W_T(b) \, d\mathrm{vol}(b)}{\int_{M^r} W_T(b) \, d\mathrm{vol}(b)} \tag{5.3}
```

This is the Reynolds operator for the group of diffeomorphisms of $M^r$,
restricted to the wealth-weighted invariant measure.

### 5.3 Orbit polytopes and the geometry of diversification

For a finite group $G$ acting on $\mathbb{R}^{d}$, the orbit polytope of a
point $x$ is:
```math
P_G(x) = \mathrm{conv}\{g \cdot x : g \in G\} \tag{5.4}
```

The vertices are the orbit points; the centroid is $\mathcal{R}_{G}(x)$.

**For the symmetric group $S_d$ acting on $\Delta_{d-1}$:** The orbit polytope
of a generic portfolio $b$ is the **permutohedron** — a polytope with $d!$
vertices obtained by permuting the coordinates of $b$. The equal-weight portfolio
is its centroid.

**The Weyl chamber.** For the action of $S_d$ on ordered portfolios
($b_1 \geq b_2 \geq \cdots \geq b_d$), the fundamental domain is the Weyl
chamber $W = \{b \in \Delta_{d-1} : b_1 \geq \cdots \geq b_d\}$. The
log-optimal portfolio $b^{\ast}$ lies in the Weyl chamber (after relabelling).
The distance from $b^{\ast}$ to the chamber boundary measures how "concentrated"
the optimal portfolio is.

### 5.4 Steiner symmetrisation and portfolio simplification

**Steiner symmetrisation** replaces a convex body $K$ with a symmetric convex
body $S_H(K)$ having the same volume but symmetric about a hyperplane $H$.
Repeated Steiner symmetrisation converges to a ball (the most symmetric
convex body).

**Financial interpretation:** Steiner symmetrisation of the market manifold
$M^r$ about the equal-weight hyperplane replaces $M^r$ with a manifold having
the same volume (same number of effective strategies) but a more symmetric
factor structure. The limit (a ball) is the CAPM market — the most symmetric
possible factor structure.

This gives a new interpretation of the Minkowski inequality:
```math
\mathrm{vol}(\mathcal{R}_{G}(M)) \leq \mathrm{vol}(M)
```

**Symmetrisation reduces volume.** Diversification (the financial analogue of
symmetrisation) reduces the effective size of the strategy space.

---

## 6. The Sobolev Extension

### 6.1 The problem with smoothness

Čencov's theorem requires the state space to be a smooth manifold and the
divergence to be a smooth Riemannian distance. Financial data violates both:

- Returns have jumps (earnings announcements, circuit breakers)
- Portfolio weights hit the boundary $b_i = 0$ (short-sale constraints)
- The Fisher information matrix $F(b)$ diverges at the simplex boundary
  (the $1/b_i$ singularity)
- Empirical distributions are atomic, not smooth

We need a version of the theory that works without smoothness.

### 6.2 The Sobolev-Fisher-Rao metric

**Definition 6.1** (Sobolev-Fisher-Rao space). *The Sobolev-Fisher-Rao space
$W^{1,2}_{\rm FR}(\Delta_{d-1})$ is the completion of smooth positive
densities on $\Delta_{d-1}$ under the norm:*

```math
\|p\|^2_{W^{1,2}_{\rm FR}} = \int_{\Delta_{d-1}} p \, d\mathrm{vol}
+ \int_{\Delta_{d-1}} |\nabla_{\rm FR} p|^2_{g^{\rm FR}} \, d\mathrm{vol} \tag{6.1}
```

*where $\nabla_{\rm FR}$ is the gradient with respect to the Fisher-Rao metric.*

In the Bhattacharyya coordinates $u = \sqrt{p}$, this becomes the standard
Sobolev space $H^1(S^{d-1}_{+})$ on the positive sphere:
```math
\|u\|^2_{H^1} = \int_{S^{d-1}_{+}} |u|^2 + |\nabla u|^2 \, d\mathrm{vol}_{S^{d-1}} \tag{6.2}
```

**The $1/b_i$ singularity is removable in Bhattacharyya coordinates.** The
Fisher-Rao metric $g^{\rm FR}_{ij} = \delta_{ij}/b_i$ diverges as $b_i \to 0$.
But in $u_i = \sqrt{b_i}$ coordinates, the metric becomes the round metric on
$S^{d-1}$, which is perfectly smooth. The singularity is a coordinate artefact.

### 6.3 The Muckenhoupt condition and boundary regularity

The Fisher-Rao metric induces a weight function $w(b) = \prod_i b_i^{-1}$
on $\Delta_{d-1}$. This weight belongs to the Muckenhoupt class $A_2$ when
all components satisfy $0 < \alpha_i < 2$ (from Paper II.5, SOBOLEV_OPTIONS_GREEKS):

**Theorem 6.1** *(Sobolev regularity of the Fisher-Rao metric)*.
*The Fisher-Rao metric weight $w(b) = \prod b_i^{-1}$ is in $A_2(\Delta_{d-1})$.
Consequently:*

*(i) The Sobolev embedding $W^{1,2}_{w}(\Delta) \hookrightarrow L^q_w(\Delta)$
holds for $q \leq 2d/(d-2)$.*

*(ii) The Poincaré inequality holds:
```math
\int |f - \bar f|^2 w \, d\mathrm{vol} \leq C_P \int |\nabla f|^2 w \, d\mathrm{vol}
```
with $C_P = 1/\lambda_1$ (spectral gap of the weighted Laplacian).*

*(iii) Elliptic regularity: solutions of $\Delta_w f = g$ with
$g \in L^2_w$ satisfy $f \in W^{2,2}_{w}$.*

*Proof.* The $A_2$ membership is verified by the Muckenhoupt criterion
(SOBOLEV_OPTIONS_GREEKS Theorem 2.1). Parts (i)–(iii) follow from the
Fabes-Kenig-Serapioni theory of degenerate elliptic operators with $A_2$
weights. $\square$

### 6.4 Čencov in Sobolev regularity

**Theorem 6.2** *(Sobolev Čencov)*.
*Let $D$ be a divergence on $W^{1,2}_{\rm FR}(\Delta_{d-1})$ satisfying:*
*(i) $D$ induces a weak Riemannian metric in $W^{1,2}$*
*(ii) $D$ is monotone under all Markov maps that are bounded on $W^{1,2}$*
*(iii) $D$ is weakly continuous*

*Then $D$ is the Fisher-Rao distance (up to scale).*

*Proof sketch.* The key insight is that Čencov's proof uses the infinitesimal
monotonicity condition at each point, which requires only the metric tensor
$g_{ij}(p)$ to be defined a.e. (not everywhere). In $W^{1,2}$, the metric
tensor exists a.e. by Rademacher's theorem. The uniqueness argument
(pinning down $g_{ij}$ from the Markov invariance condition) proceeds as in
the smooth case, using the $A_2$ weight condition to control the boundary
singularity. The detailed proof uses the Ambrosio-Gigli-Savaré framework
for calculus on metric measure spaces. $\square$

### 6.5 What Sobolev regularity buys

The Sobolev extension handles the cases that the smooth theory cannot:

| Situation | Smooth theory | Sobolev extension |
|:----------|:-------------|:-----------------|
| Portfolio at boundary ($b_i = 0$) | Fisher metric diverges | Removable singularity in $u = \sqrt{b}$ |
| Jump in returns | Not differentiable | $W^{1,2}$ includes BV functions |
| Empirical distributions | Atomic, not smooth | Mollify; limit in $W^{1,2}$ |
| Discontinuous channels | Not a smooth map | Bounded on $W^{1,2}$ suffices |
| Fractal market structure | Not a manifold | Metric measure space with $A_2$ weight |

---

## 7. Ergodic Convexification

### 7.1 The Birkhoff convexification

**Theorem 7.1** *(Ergodic convexification = Birkhoff)*.
*Let $(X, T, \mu)$ be an ergodic measure-preserving system on a compact
metric space $X$. The ergodic convexification map
$\mathcal{E}: X \to \mathcal{P}(X)$ defined by:*

```math
\mathcal{E}(x) = \lim_{N\to\infty}\frac{1}{N}\sum_{n=0}^{N-1}\delta_{T^n x} \tag{7.1}
```

*satisfies:*

*(i) $\mathcal{E}(x) = \mu$ for $\mu$-a.e. $x$ (Birkhoff ergodic theorem).*

*(ii) $\mathcal{E}(x) \in \mathcal{P}(X)$ is in the free convex completion
of $X$.*

*(iii) The image $\mu$ is an extreme point of the set of $T$-invariant measures
iff the system is ergodic.*

*(iv) For any continuous $f: X \to \mathbb{R}$:
$\int f \, d\mathcal{E}(x) = \lim_{N\to\infty}\frac{1}{N}\sum_{n=0}^{N-1}f(T^n x) = \int f \, d\mu$.*

*Proof.* This is the Birkhoff ergodic theorem (Birkhoff 1931) restated in
the language of the free convex completion. $\square$

### 7.2 Financial interpretation

The ergodic convexification map sends a deterministic market trajectory
(a sequence of returns $x_1, x_2, \ldots$) to a probability measure on the
return space. This measure IS the market — it is the convexified description
of the dynamics.

**Key point:** The ergodic measure $\mu$ lives in the convex space
$\mathcal{P}(X)$, even if $X$ itself is non-convex. A chaotic deterministic
orbit on a hyperbolic manifold (non-convex) produces an ergodic measure that
lives in $\mathcal{P}(M)$ (convex). **Ergodic averaging is the canonical
convexification of dynamics.**

This resolves the question from Paper 0.1 about stochastic vs deterministic
markets. It does not matter whether the dynamics are stochastic (diffusion on
$M^r$) or deterministic (chaotic map on $M^r$). In either case, the
ergodic convexification produces a measure $\mu \in \mathcal{P}(M^r)$, and
all the information-geometric machinery of the monograph applies to $\mu$.

### 7.3 Clarification on ergodic coverage

Paper 0.1 incorrectly claimed "any ergodic orbit visits every point." The
correct statement is:

**The ergodic measure $\mu$ has support equal to $X$ iff the system is
uniquely ergodic or the orbit is dense.** For general ergodic systems, the
orbit visits $\mu$-a.e. point (full measure), but may miss a set of measure
zero. On a compact manifold with a smooth ergodic measure, the support is
the entire manifold, so the orbit is dense. This is the relevant case for
market manifolds with smooth stationary distributions (the Jeffreys prior /
WF stationary measure).

---

## 8. The Legendre-Fenchel Convexification

### 8.1 Convexifying functions

For functions (as opposed to sets), the canonical convexification is the
Legendre-Fenchel biconjugate:

**Definition 8.1** (Convex envelope). *The convex envelope of $f: \mathbb{R}^{d} \to \mathbb{R} \cup \{+\infty\}$ is:*
```math
f^{**}(x) = \sup\{g(x) : g \leq f, \, g \text{ convex}\} \tag{8.1}
```

*Equivalently, $f^{**}$ is the Legendre-Fenchel biconjugate:*
```math
f^{\ast}(y) = \sup_x(\langle x, y\rangle - f(x)), \qquad f^{**}(x) = \sup_y(\langle x, y\rangle - f^{\ast}(y)) \tag{8.2}
```

**Theorem 8.1** *(Fenchel-Moreau)*.
*$f^{**} = f$ iff $f$ is convex and lower semicontinuous. For non-convex $f$,
$f^{**}$ is the largest convex minorant of $f$.*

### 8.2 Financial interpretation: the Kelly function

The Kelly log-growth function $L_T(b) = \frac{1}{T}\sum_t \log\langle b, x_t\rangle$
is concave on $\Delta_{d-1}$ (as a function of $b$). Its Legendre-Fenchel
conjugate is:
```math
L_T^{\ast}(y) = \sup_{b \in \Delta_{d-1}}(\langle y, b\rangle - L_T(b)) \tag{8.3}
```

This is the **rate function** of the large deviations of the empirical portfolio
distribution. By Cramér's theorem, $L_T^{\ast}$ governs the probability that the
empirical portfolio mean deviates from $b^{\ast}$.

**The MUP is the Legendre-Fenchel dual of the Kelly function:**
```math
\log S_T^{\rm MUP} = \log\int_{\Delta} e^{T \cdot L_T(b)}\,d\mu(b)
\approx T \cdot L_T(b^{\ast}) + \frac{d-1}{2}\log\frac{2\pi}{T} - \frac{1}{2}\log\det F \tag{8.4}
```

The Laplace approximation IS the saddle-point approximation of the
Legendre-Fenchel transform.

---

## 9. The Five Convexification Operators: A Unified View

### 9.1 The equivalence

| Operator | Domain | Action | Name in context |
|:---------|:-------|:-------|:---------------|
| $\mathcal{P}(X)$ | Sets | Take all mixtures | Free convex completion |
| $f^{**}$ | Functions | Largest convex minorant | Legendre-Fenchel |
| $\rho = \sum p_i \|\psi_i\rangle\langle\psi_i\|$ | Quantum states | Mix pure states | Density matrix |
| $\mathcal{R}_{G}(x) = \int_G g\cdot x \, d\mu_G$ | Group actions | Average over orbits | Reynolds operator |
| $\mathcal{E}(x) = \lim \frac{1}{N}\sum \delta_{T^n x}$ | Dynamical systems | Time average | Ergodic measure |

**Theorem 9.1** *(Unification)*.
*All five convexification operators are instances of the free convex
completion $\mathcal{P}$:*

*(i) Legendre-Fenchel: $f^{**}(x) = \inf\{\int f \, d\mu : \mu \in \mathcal{P}(\mathrm{dom}(f)),\, \int \mathrm{id}\, d\mu = x\}$ (the convex envelope is the infimum over representations as a mixture).*

*(ii) Density matrix: $\mathcal{D}_{n} = \mathcal{P}(\mathbb{CP}^{n})$ (density
matrices are probability measures on pure states).*

*(iii) Reynolds: $\mathcal{R}_{G}(x) = \int_G g\cdot x \, d\mu_G = \int_{Gx} \mathrm{id}\, d(\iota_*\mu_G) \in \mathcal{P}(Gx)$ (the Reynolds average is the pushforward of Haar measure to the orbit).*

*(iv) Ergodic: $\mathcal{E}(x) = \mu \in \mathcal{P}(X)$ (the ergodic
measure is a probability measure, i.e., an element of the free convex completion).*

*In each case, convexification is the passage from $X$ to $\mathcal{P}(X)$.*

### 9.2 The categorical perspective

In the language of category theory, $\mathcal{P}$ is a **monad** on the
category of measurable spaces (the Giry monad). The unit $\eta: X \to \mathcal{P}(X)$
is the Dirac embedding $x \mapsto \delta_x$. The multiplication
$\mu: \mathcal{P}(\mathcal{P}(X)) \to \mathcal{P}(X)$ is the
"averaging of averages" operation.

The Kleisli category of the Giry monad is the category of **Markov kernels**
— exactly the channels of Paper 0.1's Axiom 2. The data processing
inequality is a property of Kleisli morphisms. The Fisher-Rao metric is
the unique invariant metric on $\mathcal{P}(X)$ compatible with the Kleisli
composition.

**The entire information-geometric framework is the geometry of the Giry monad.**

---

## 10. The Palindromic Completion of the Simplex

### 10.1 The sixth convexification operator

Section 9 unified five convexification operators as instances of the free
convex completion $\mathcal{P}$. There is a sixth — more economical than any
of them — that exploits a specific structural symmetry: **palindromic
reflection**.

The idea: if a space has a reflection symmetry, you only need to observe HALF
of it. The other half is determined. The palindromic completion builds the
full convex space from a fundamental domain — the half-space under reflection.

**Definition 10.1** (Palindromic reflection on $\Delta_{d-1}$). *For an
involution $\tau: \{1, \ldots, d\} \to \{1, \ldots, d\}$ (a permutation with
$\tau^2 = \mathrm{id}$), the **palindromic reflection** on $\Delta_{d-1}$
is:*

```math
R_\tau: \Delta_{d-1} \to \Delta_{d-1}, \qquad R_\tau(b_1, \ldots, b_d) = (b_{\tau(1)}, \ldots, b_{\tau(d)}) \tag{10.1}
```

*The simplest case: the reversal $\tau(i) = d+1-i$, giving
$R(b_1, \ldots, b_d) = (b_d, \ldots, b_1)$.*

**Definition 10.2** (Palindromic half-simplex). *The **palindromic
half-simplex** under $R_\tau$ is the fundamental domain:*

```math
\Delta^+_{d-1} = \{b \in \Delta_{d-1} : b_i \geq b_{\tau(i)} \text{ for all } i < \tau(i)\} \tag{10.2}
```

*This is a convex subset of $\Delta_{d-1}$ containing exactly one
representative from each pair $\{b, R_\tau(b)\}$.*

**Definition 10.3** (Palindromic completion). *The **palindromic completion**
of a set $S \subseteq \Delta^+_{d-1}$ is:*

```math
\mathrm{Pal}(S) = \mathrm{conv}(S \cup R_\tau(S)) \tag{10.3}
```

*The convex hull of $S$ and its palindromic reflection. This is the smallest
convex set that contains $S$ and is invariant under $R_\tau$.*

### 10.2 Information halving

**Theorem 10.4** (Palindromic information halving). *Let $f: \Delta_{d-1} \to
\mathbb{R}$ be a portfolio payoff function that is palindromic under $R_\tau$
($f = f \circ R_\tau$). Then:*

```math
H(f) = H(f|_{\Delta^+_{d-1}}) \tag{10.4}
```

*The entropy of $f$ on the full simplex equals its entropy on the
half-simplex. The information in the second half is zero — it is free.*

*Proof.* Since $f(b) = f(R_\tau(b))$ for all $b$, the values of $f$ on
$\Delta^- = \Delta \setminus \Delta^+$ are determined by the values on
$\Delta^+$. The conditional entropy $H(f|_{\Delta^-} \mid f|_{\Delta^+}) = 0$.
By the chain rule: $H(f) = H(f|_{\Delta^+}) + H(f|_{\Delta^-} \mid f|_{\Delta^+}) = H(f|_{\Delta^+})$. $\square$

This is the precise sense in which palindromic symmetry gives you free
information. Any palindromic structure in the market return function halves
the dimension of the estimation problem.

### 10.3 Multi-dimensional palindromic completion

For $k$ independent involutions $\tau_1, \ldots, \tau_k$ (commuting
reflections on $\Delta_{d-1}$), the **$k$-palindromic completion** uses the
fundamental domain under all $k$ reflections simultaneously:

```math
\Delta^+_{d-1}(k) = \{b : b_i \geq b_{\tau_j(i)} \text{ for all } i < \tau_j(i), \text{ all } j = 1, \ldots, k\} \tag{10.5}
```

The volume of this fundamental domain is $\mathrm{Vol}(\Delta_{d-1}) / 2^k$ —
the full simplex divided by the order of the palindromic group.

**Theorem 10.5** ($k$-palindromic information reduction). *A function $f$
that is palindromic under all $k$ reflections satisfies:*

```math
H(f) = H(f|_{\Delta^+(k)}) \tag{10.6}
```

*The effective entropy is reduced by a factor of $2^k$: you only need to
observe the fundamental domain; the remaining $2^k - 1$ copies are free.*

For a market with $r$ factors, the maximum palindromic dimension is $k = r$
(each factor has a reflection symmetry). In this case:

```math
H_{\rm eff} = \frac{H_{\rm full}}{2^r} \tag{10.7}
```

A fully palindromic market (symmetric in every factor direction) has
exponentially reduced information content. This is the CAPM at equilibrium:
every factor is mean-reverting (palindromic in time), and the effective
entropy is minimal.

### 10.4 Palindromic completion on the Bhattacharyya sphere

Under the Bhattacharyya embedding $\phi(b) = \sqrt{b} \in S^{d-1}_{+}$, the
palindromic reflection $R_\tau$ becomes a REFLECTION of the sphere:

```math
\hat{R}_\tau(\sqrt{b_1}, \ldots, \sqrt{b_d}) = (\sqrt{b_{\tau(1)}}, \ldots, \sqrt{b_{\tau(d)}}) \tag{10.8}
```

This is an isometry of $S^{d-1}_{+}$ (it preserves the round metric). The
palindromic half-sphere $S^+$ is a fundamental domain of the reflection group.

**The palindromic completion of $S^+$ gives the full positive orthant $S^{d-1}_{+}$.**

More generally, the group generated by $k$ independent reflections is a
**Coxeter group** $W$ of type $A$. The fundamental domain is a
**Weyl chamber** — a simplex-shaped region whose $2^k$ reflections tile
the sphere. The palindromic completion is the Coxeter group orbit of the
fundamental domain.

**Theorem 10.6** (Palindromic completion = Coxeter orbit). *The $k$-palindromic
completion of a function $f$ defined on the Weyl chamber
$C_W \subset S^{d-1}_{+}$ is:*

```math
\mathrm{Pal}_{W}(f)(x) = f(w \cdot x) \quad \text{where } w \in W \text{ is the unique element with } w \cdot x \in C_W \tag{10.9}
```

*This extends $f$ from the Weyl chamber to the full sphere by the action of
the Coxeter group. The extension is palindromic (invariant under $W$) by
construction, and carries no information beyond $f|_{C_W}$.*

### 10.5 The palindromic completion of the market manifold

The market manifold $M^r \subset S^{d-1}_{+}$ may or may not have palindromic
symmetry. Three cases:

**Case 1: CAPM (great sphere $S^r_+$).** The CAPM manifold IS palindromic
in all factor directions. The Jacobi process with symmetric parameters
satisfies detailed balance — the forward and reverse transition probabilities
are equal. The palindromic group is the full symmetric group $S_{r+1}$
(permutations of factors). The fundamental domain is a single Weyl chamber.
The market is maximally palindromic; information cost is minimal.

**Case 2: Clifford torus ($T^2$).** The torus has two palindromic directions
(the two circle factors) but the market manifold on it need NOT be symmetric
in both. The momentum factor breaks the palindromic symmetry in the angular
direction (momentum is directional; mean reversion is palindromic). The
palindromic dimension is $k = 1$ (the mean-reversion direction is palindromic;
the momentum direction is not). Information is halved, not quartered.

**Case 3: Pseudo-Anosov ($\mathbb{H}^{2}$).** Hyperbolic geometry has NO
global reflection symmetry that preserves the manifold. The pseudo-Anosov
monodromy is a hyperbolic isometry with no fixed points — it is maximally
non-palindromic. The palindromic dimension is $k = 0$. No free information.
Every bit must be earned. This is the geometric reason why pseudo-Anosov
markets (crises, chaos) are the hardest to predict.

### 10.6 The palindromic MUP

The MUP (Manifold Universal Portfolio) integrates over $M^r$:

```math
b^{\rm MUP}_{T} = \frac{\int_{M^r} b\, W_T(b)\, d\mathrm{vol}(b)}{\int_{M^r} W_T(b)\, d\mathrm{vol}(b)}
```

If $M^r$ has $k$-palindromic symmetry, the integral over $M^r$ reduces to
an integral over the fundamental domain $M^r_+$:

```math
b^{\rm MUP}_{T} = \frac{\int_{M^r_+} b\, W_T(b)\, d\mathrm{vol}(b) + \int_{M^r_+} R_\tau(b)\, W_T(R_\tau(b))\, d\mathrm{vol}(b)}{2\int_{M^r_+} W_T(b)\, d\mathrm{vol}(b)} \tag{10.10}
```

By palindromic symmetry, $W_T(b) = W_T(R_\tau(b))$ (palindromic functions
have the same wealth on both sides). So:

```math
b^{\rm MUP}_{T} = \frac{\int_{M^r_+} (b + R_\tau(b))\, W_T(b)\, d\mathrm{vol}(b)}{2\int_{M^r_+} W_T(b)\, d\mathrm{vol}(b)} \tag{10.11}
```

The integration domain is HALVED for each palindromic dimension. For a
$k$-palindromic market:

```math
\text{MUP computation cost} \propto \frac{\mathrm{Vol}(M^r)}{2^k} \tag{10.12}
```

The palindromic MUP is exponentially cheaper to compute than the general MUP.
This is the computational dividend of palindromic symmetry: you get the same
optimal portfolio from integrating over the fundamental domain.

### 10.7 Palindromic completion vs free completion: the efficiency ratio

The free convex completion $\mathcal{P}(X)$ embeds $X$ into the space of ALL
probability measures — it is maximally general but expensive. The palindromic
completion $\mathrm{Pal}(X)$ exploits a specific symmetry to embed $X$ into
a space of half the dimension — it is less general but exponentially cheaper.

| Completion | Domain needed | Information cost | When it applies |
|:---|:---|:---|:---|
| Free $\mathcal{P}(X)$ | Full $X$ | Full $H(X)$ | Always (universal) |
| Palindromic $\mathrm{Pal}(X)$ | Half-domain $X^+$ | $H(X)/2^k$ | When $X$ has palindromic symmetry |
| Symmetry $\mathcal{C}_{G}(X)$ | Fundamental domain $X/G$ | $H(X)/|G|$ | When $G$ acts on $X$ |

The palindromic completion is a special case of symmetry convexification
(Section 5) with $G = (\mathbb{Z}/2)^k$ — the group generated by $k$
independent reflections. But stating it as a palindromic operation connects
it to the filtration theory (palindromes in the return sequence), the
BWT/CFL decomposition (palindromic factors), and the Jacobi detailed
balance (palindromic processes).

**Theorem 10.7** (The six convexification operators). *The complete list of
canonical convexification operators on the portfolio simplex is:*

| # | Operator | Type | Information reduction |
|:---|:---|:---|:---|
| 1 | Free completion $\mathcal{P}$ | Universal | None (full embedding) |
| 2 | Legendre-Fenchel $f^{{\ast}{\ast}}$ | Functional | Removes non-convexity |
| 3 | Density matrix $\mathcal{D}_{n}$ | Quantum | Removes phase information |
| 4 | Reynolds $\mathcal{R}_{G}$ | Group-symmetric | Reduces by $|G|$ |
| 5 | Ergodic $\mathcal{E}$ | Time-average | Removes transient information |
| 6 | Palindromic $\mathrm{Pal}$ | Reflection-symmetric | Reduces by $2^k$ |

*All six are instances of $\mathcal{P}$. The palindromic completion is the
most efficient when reflection symmetry exists: it provides the maximum
information reduction per symmetry exploited.*

---

## 11. Open Problems

**OP-F. The non-commutative Giry monad.**
Is there a non-commutative version of the Giry monad where $\mathcal{P}(X)$
is replaced by the space of density matrices on a $C^{\ast}$-algebra? If so,
what is the analogue of the Fisher-Rao metric? (The Bures metric is a
candidate, but its uniqueness properties are different from Čencov's.)

**OP-G. Optimal convexification dimension.**
Theorem 3.1 gives bounds on $N_{\rm conv}(M)$ but the exact value is unknown
for most manifolds. For the Clifford torus $T^2 \subset S^3$, is
$N_{\rm conv} = 4$ (the ambient $S^3$) or does it require more?

**OP-H. Sobolev regularity of market manifolds.**
Financial time series have jumps and heavy tails. In what Sobolev space does
the empirical market manifold live? If the return distribution has finite
$p$-th moment, what is the optimal Sobolev regularity of the Fisher-Rao
metric on the implied portfolio simplex?

**OP-I. The convexification of quantum markets.**
If financial instruments include quantum assets (quantum computing stocks,
quantum communication channels), does the market manifold acquire
non-commutative structure? Would the density matrix formalism apply?

**OP-J. Information-theoretic characterisation of the convexification dimension.**
Is there a formula $N_{\rm conv}(M) = f(\text{information-theoretic invariants of } M)$?
Candidates: $N_{\rm conv} = r + \mathrm{Kolmogorov\,complexity}(M)$ or
$N_{\rm conv} = r + h_{\rm top}(M)/h_{\rm Kelly}$.

---

## References

Ambrosio, L., Gigli, N., and Savaré, G. (2008). *Gradient Flows in Metric
Spaces and in the Space of Probability Measures*. Birkhäuser.

Ay, N., Jost, J., Lê, H. V., and Schwachhöfer, L. (2017).
*Information Geometry*. Springer.

Birkhoff, G. D. (1931). Proof of the ergodic theorem.
*Proceedings of the National Academy of Sciences* 17(12), 656–660.

Čencov, N. N. (1982). *Statistical Decision Rules and Optimal Inference*.
American Mathematical Society.

Choquet, G. (1956). Existence des représentations intégrales.
*Comptes Rendus* 243, 699–702.

Fabes, E. B., Kenig, C. E., and Serapioni, R. P. (1982). The local
regularity of solutions of degenerate elliptic equations.
*Communications in Partial Differential Equations* 7(1), 77–116.

Fritz, T. (2020). A synthetic approach to Markov kernels, conditional
independence and theorems on sufficient statistics.
*Advances in Mathematics* 370, 107239.

Giry, M. (1982). A categorical approach to probability theory.
In *Categorical Aspects of Topology and Analysis*, Springer, 68–85.

Nash, J. F. (1956). The imbedding problem for Riemannian manifolds.
*Annals of Mathematics* 63(1), 20–63.

Phelps, R. R. (1966). *Lectures on Choquet's Theorem*. Van Nostrand.

Rockafellar, R. T. (1970). *Convex Analysis*. Princeton University Press.

Whitney, H. (1936). Differentiable manifolds.
*Annals of Mathematics* 37(3), 645–680.

*[All other references as per companion papers.]*
