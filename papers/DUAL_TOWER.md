# The Dual Tower of Information Processing:
## Spectral Duals, Finite Group Constructions,
## and the Multiresolution Analysis of Markets

**Saxon Nicholls** — me@saxonnicholls.com

**Paper 0.3** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
Papers 0.1–0.2 established that information processing on the portfolio simplex
$\Delta_{d-1}$ must be convex and that convexification is probabilification. The
present paper asks: how many "dual" perspectives does such a system admit? We
construct a countable infinity of dual spaces on the information simplex by three
independent routes — the Giry tower (iterated convex completions), the spectral
decomposition (Jacobi eigenfunctions of the Laplacian on $\Delta_{d-1}$), and the
subgroup lattice (irreducible representations of finite groups acting on the
simplex). All three constructions yield isomorphic multiresolution decompositions
of the market. We prove that the Legendre-Fenchel dual of the Kelly function is
the large-deviations rate function, and that the Pontryagin dual of the natural
abelian group action recovers the Fourier modes of the Clifford torus market.

**Our principal results:**

**(i) The Giry tower.** The iterated probability functor $\mathcal{P}^{k}(X)$ builds
a countable tower of dual spaces: pure states, portfolios, fund-of-funds,
$k$-th order beliefs. The Giry monad structure (unit = Dirac embedding,
multiplication = averaging) makes each level collapse to the one below. The MUP
posterior $\pi_T$ lives at Level 2; the Laplace approximation collapses it to
Level 1 at cost $r\log(T)/(2T)$ — the MUP regret IS the information cost of
collapsing one level of the tower.

**(ii) The spectral dual tower.** The eigenspace decomposition $L^2(\Delta,
g^{\rm FR}) = \bigoplus_{n=0}^\infty E_n$ of the Laplacian on the Fisher-Rao
simplex is a multiresolution analysis (MRA) of the market. The $n$-th eigenspace
$E_n$ is spanned by Jacobi polynomials of degree $n$. Projection onto $E_0$
recovers the market portfolio; projection onto $E_1$ recovers the CAPM factor;
projection onto $E_n$ recovers the $n$-th systematic factor. The spectral gap
$\lambda_1$ from CLASSIFICATION.md determines the coarsest non-trivial resolution.

**(iii) The finite group construction.** The symmetric group $S_d$ acts on
$\Delta_{d-1}$ by permuting coordinates. The Peter-Weyl decomposition
$L^2(\Delta) = \bigoplus_{\lambda \vdash d} V_\lambda \otimes V_\lambda^{\ast}$ over
irreducible representations indexed by partitions $\lambda \vdash d$ gives a finite
but rich dual structure. For any subgroup $G \leq S_d$, the $G$-invariant
submanifold $M^r_G = \{b \in M^r : g \cdot b = b, \forall g \in G\}$ defines a
dual market at that symmetry level. The lattice of subgroups gives a lattice of
dual manifolds interpolating between the equal-weight portfolio ($G = S_d$) and
the full market ($G = \{e\}$).

**(iv) Tower isomorphism.** The three towers — Giry, spectral, group — are
isomorphic as multiresolution decompositions of the market. Level $k$ of the Giry
tower corresponds to the $k$-th eigenspace of the spectral tower, which corresponds
to the $k$-th level of the subgroup lattice. The isomorphism is mediated by the
Casimir operator of the representation.

**(v) The punchline.** The factor structure of a market is the representation
theory of its symmetry group.

**Keywords.** Giry monad; spectral decomposition; Jacobi polynomials; Peter-Weyl theorem;
symmetric group; representation theory; multiresolution analysis; Legendre-Fenchel dual;
Pontryagin dual; factor models; portfolio simplex; Fisher-Rao geometry; Kelly criterion.

**MSC 2020.** 91G10, 46L65, 20C30, 43A40, 42C40, 60E10.

---

## 1. Introduction

### 1.1 The question

The companion papers of this series build a geometric theory of financial markets
on the portfolio simplex $(\Delta_{d-1}, g^{\rm FR})$ equipped with the Fisher-Rao
metric. Papers 0.1–0.2 established the foundational principles: information
processing must be convex (Paper 0.1), and convexification is equivalent to
probabilification (Paper 0.2). Every convex information processor is a probability
distribution on the simplex, every composition of such processors respects the
convex structure, and the simplex with the Fisher-Rao metric is the unique
(up to scale) Riemannian manifold on which this structure is realised.

But the simplex is not the end of the story. A probability distribution over
portfolios is itself a point in a higher-dimensional simplex. A distribution over
distributions lives one level higher still. How far does this tower extend? How
many dual perspectives does an information processing system admit?

Three independent constructions give the same answer: **countably infinitely many**.

1. **The Giry tower** (categorical). Iterate the probability functor
   $\mathcal{P}$: assets $\to$ portfolios $\to$ distributions over portfolios
   $\to$ $\cdots$ Each level is a new convex space. The Giry monad gives the
   algebraic structure: each level can be collapsed to the one below by averaging,
   at a quantifiable information cost.

2. **The spectral tower** (analytic). Decompose $L^2(\Delta_{d-1}, g^{\rm FR})$
   into eigenspaces of the Laplace-Beltrami operator. Each eigenspace captures
   one "frequency" of variation across the simplex. The tower is indexed by the
   eigenvalues $0 = \lambda_0 < \lambda_1 < \lambda_2 < \cdots$

3. **The group tower** (algebraic). The symmetric group $S_d$ acts on the simplex.
   Decompose functions into irreducible representations. The lattice of subgroups
   $\{e\} \leq \cdots \leq G \leq \cdots \leq S_d$ gives a lattice of dual
   markets at every symmetry level.

The main theorem of this paper (Theorem 6.1) establishes that these three towers
are isomorphic as multiresolution decompositions. The practical consequence:
**the factor structure of a market is the representation theory of its symmetry
group.** A CAPM market has $S_d$-symmetric factor structure (one non-trivial
representation); a multi-factor market has partially broken symmetry (several
representations); an idiosyncratic market has no symmetry at all.

### 1.2 Notation and setup

Throughout, $d$ denotes the number of assets, $r$ the dimension of the market
manifold $M^r \subset S^{d-1}_{+}$ (the number of systematic factors), and $T$
the number of time periods. Portfolio weights $b = (b_1, \ldots, b_d) \in
\Delta_{d-1}$. The Fisher-Rao metric is $g^{\rm FR}_{ij}(b) = \delta_{ij}/b_i$.
The Bhattacharyya isometry is $\phi: b \mapsto \sqrt{b} \in S^{d-1}_{+}$. The
log-optimal portfolio is $b^{\ast} = \arg\max_{b \in M^r} L_T(b)$ where
$L_T(b) = \frac{1}{T}\sum_{t=1}^{T} \log\langle b, x_t \rangle$. The MUP is
$\hat{b}^{M}_T = \int_{M^r} b\, W_T(b)\,d\mu_M(b) / \int_{M^r} W_T(b)\,d\mu_M(b)$.

---

## 2. The Giry Tower

### 2.1 Construction

Fix a finite set $X = \{1, \ldots, d\}$ of pure states (individual assets). Define:

- **Level 0:** $\mathcal{P}^{0}(X) = X$ — the space of pure states.
- **Level 1:** $\mathcal{P}^{1}(X) = \mathcal{P}(X) = \Delta_{d-1}$ — probability
  distributions over $X$. These are portfolios.
- **Level 2:** $\mathcal{P}^{2}(X) = \mathcal{P}(\Delta_{d-1})$ — probability
  distributions over portfolios. These are fund-of-funds, or equivalently
  hyperpriors over the portfolio space.
- **Level $k$:** $\mathcal{P}^{k}(X) = \mathcal{P}(\mathcal{P}^{k-1}(X))$ — the
  $k$-th order belief space.

Each level is a convex space: convex combinations of distributions over
distributions are well-defined. Moreover, each $\mathcal{P}^{k}(X)$ carries its
own Fisher-Rao metric $g^{\rm FR}_{k}$ inherited from the convex structure, and
each admits a Bhattacharyya embedding into a (generally infinite-dimensional)
sphere.

**Financial interpretation:**

| Level | Space | Financial object | Example |
|:------|:------|:----------------|:--------|
| 0 | $X$ | Individual assets | Stock $i$ |
| 1 | $\mathcal{P}(X) = \Delta_{d-1}$ | Portfolios | Hedge fund strategy |
| 2 | $\mathcal{P}^{2}(X)$ | Distributions over portfolios | Fund-of-funds; Bayesian prior over strategies |
| 3 | $\mathcal{P}^{3}(X)$ | Distributions over fund-of-funds | Meta-allocator; model uncertainty |
| $k$ | $\mathcal{P}^{k}(X)$ | $k$-th order beliefs | $k$-th level of Bayesian hierarchy |

### 2.2 The Giry monad

The tower carries the structure of a **monad** $(\mathcal{P}, \eta, \mu)$ in the
category of measurable spaces (Giry [1982]):

**Unit.** The map $\eta: X \to \mathcal{P}(X)$ sends each pure state $x$ to the
Dirac measure $\delta_x \in \Delta_{d-1}$. Financially: embed a single asset as
the degenerate portfolio that holds only that asset. This is the Dirac embedding
$\eta(i) = e_i$.

**Multiplication.** The map $\mu: \mathcal{P}^{2}(X) \to \mathcal{P}(X)$ sends a
distribution over distributions to its average:

$$\mu(\Pi) = \int_{\Delta_{d-1}} b\, d\Pi(b) \in \Delta_{d-1} \tag{2.1}$$

Financially: the fund-of-funds collapses to a single portfolio by taking the
weighted average of its constituent portfolios. This is the **averaging map**.

**Monad axioms.** The unit and multiplication satisfy:

$$\mu \circ \eta_{\mathcal{P}} = \mu \circ \mathcal{P}(\eta) = \mathrm{id}_{\mathcal{P}} \tag{2.2}$$
$$\mu \circ \mu_{\mathcal{P}} = \mu \circ \mathcal{P}(\mu) \tag{2.3}$$

The first says: embedding a portfolio as a Dirac distribution over portfolios and
then averaging returns the original portfolio. The second says: collapsing a
triple tower in either order gives the same result (associativity of averaging).

### 2.3 The MUP as a Level 2 object

The MUP posterior $\pi_T \in \mathcal{P}^{2}(X)$ is defined by:

$$d\pi_T(b) = \frac{W_T(b)\,d\mu_M(b)}{\int_{M^r} W_T(b)\,d\mu_M(b)} \tag{2.4}$$

where $W_T(b) = \exp(T \cdot L_T(b))$ is the wealth function and $\mu_M$ is
the volume measure on $M^r$. This is a probability distribution over
$M^r \subset \Delta_{d-1}$ — a Level 2 object.

The monad multiplication collapses it:

$$\mu(\pi_T) = \int_{M^r} b\,d\pi_T(b) = \hat{b}^{M}_T \tag{2.5}$$

The MUP portfolio $\hat{b}^{M}_T$ is the Level 1 shadow of the Level 2 posterior.

### 2.4 The Laplace approximation as level collapse

The Laplace approximation (LAPLACE.md) says that as $T \to \infty$, the posterior
$\pi_T$ concentrates on $b^{\ast}$:

$$\pi_T \xrightarrow{T\to\infty} \delta_{b^{\ast}} \tag{2.6}$$

The Laplace approximation collapses Level 2 to Level 1. The MUP regret

$$\frac{r\,\log T}{2T} \tag{2.7}$$

is the **information cost of this collapse** — the KL divergence between the
full posterior $\pi_T$ and the point mass $\delta_{b^{\ast}}$, normalised by $T$.
Explicitly, by the Laplace approximation to the normalising constant:

$$D_{\rm KL}(\pi_T \| \delta_{b^{\ast}}) \approx \frac{r}{2}\log T + \frac{1}{2}\log\det F_M(b^{\ast}) + O(1) \tag{2.8}$$

where $F_M(b^{\ast})$ is the Fisher information matrix of $M^r$ at $b^{\ast}$. Dividing by
$T$ gives the per-period regret $(r\log T)/(2T)$. Each dimension of the manifold
contributes $(\log T)/(2T)$ to the cost of collapsing one level of the tower.

### 2.5 Higher levels and the epistemic hierarchy

Level 3 arises naturally when there is **model uncertainty**: a distribution over
possible MUP posteriors, reflecting uncertainty about which manifold $M^r$ the
market lives on. The collapse $\mathcal{P}^{3} \to \mathcal{P}^{2}$ averages over
model uncertainty; its cost is the model selection penalty. Bayesian model
averaging is exactly the Level 3 $\to$ Level 2 monad multiplication.

In practice, practitioners rarely go above Level 3. But the mathematical tower
extends to countable infinity, and each level carries its own Fisher-Rao geometry.

---

## 3. The Spectral Dual Tower

### 3.1 The Laplacian on the simplex

The Laplace-Beltrami operator $\Delta_{g^{\rm FR}}$ on $(\Delta_{d-1},
g^{\rm FR})$ has a complete orthonormal system of eigenfunctions. In the
Bhattacharyya coordinates $u_i = \sqrt{b_i}$ on $S^{d-1}_{+}$, $\Delta_{g^{\rm FR}}$
becomes the spherical Laplacian $\Delta_{S^{d-1}}$ restricted to the positive
orthant. The eigenvalues are:

$$\lambda_n = n(n + d - 2), \qquad n = 0, 1, 2, \ldots \tag{3.1}$$

with eigenspaces $E_n$ of dimension $\binom{n+d-2}{d-2}(2n+d-2)/(n+d-2)$ (the
dimension of the space of spherical harmonics of degree $n$ on $S^{d-1}$,
restricted by the Neumann boundary conditions on $\partial S^{d-1}_{+}$).

### 3.2 Jacobi polynomial eigenfunctions

The eigenfunctions on $\Delta_{d-1}$ are multivariate Jacobi polynomials. In the
$d=2$ case (two assets, $b \in [0,1]$), the eigenfunctions are the classical
Jacobi polynomials $P_n^{(\alpha,\alpha)}(2b-1)$ with $\alpha = -1/2$ (the
Chebyshev special case), matching the spectral theory of the Wright-Fisher
diffusion on the interval.

For general $d$, the eigenfunctions are the Dunkl-Xu orthogonal polynomials on
the simplex (Dunkl and Xu [2014]), which generalise Jacobi polynomials to the
multivariate setting. These are exactly the polynomials that appear in the MUP
partition function (CONVERGENCE.md) and in the Walsh-Jacobi correspondence
(HYPERCUBE_SHAPLEY.md).

### 3.3 The spectral decomposition as MRA

The eigenspace decomposition

$$L^2(\Delta_{d-1}, g^{\rm FR}) = \bigoplus_{n=0}^\infty E_n \tag{3.2}$$

is a multiresolution analysis (MRA) of functions on the market. Define the
projection $\Pi_n: L^2 \to E_n$ and the partial sum
$\Pi_{\leq N} = \sum_{n=0}^{N} \Pi_n$. Then:

| Eigenspace | Eigenvalue | Market interpretation | Time scale |
|:-----------|:-----------|:---------------------|:-----------|
| $E_0$ | $\lambda_0 = 0$ | Constants = market portfolio (equal expected return) | $\infty$ (infinite horizon) |
| $E_1$ | $\lambda_1 = d - 1$ | First factor = CAPM beta (slowest mean-reversion) | $1/\lambda_1$ |
| $E_2$ | $\lambda_2 = 2d$ | Second factor (value, size, momentum, ...) | $1/\lambda_2$ |
| $E_n$ | $\lambda_n = n(n+d-2)$ | $n$-th systematic factor | $1/\lambda_n$ |
| $E_\infty$ | $\infty$ | Idiosyncratic noise (instantaneous) | $0$ |

**The spectral gap** $\lambda_1 = d - 1$ from the classification theory
(CLASSIFICATION.md) determines the coarsest non-trivial resolution. For CAPM
markets (great sphere $S^r_+$), this is the rate of mean-reversion of the single
factor. For non-CAPM markets, the Jacobi operator may have a smaller spectral
gap, corresponding to slower mean-reversion and richer factor structure.

### 3.4 The frequency response of a market

Any function $f \in L^2(\Delta, g^{\rm FR})$ — for instance, the Kelly growth
rate $L_T(b)$ — has a spectral expansion:

$$L_T(b) = \sum_{n=0}^\infty \hat{L}_{n} \cdot \psi_n(b) \tag{3.3}$$

where $\psi_n$ are the orthonormal Jacobi eigenfunctions and $\hat{L}_n =
\langle L_T, \psi_n \rangle_{L^2}$ are the spectral coefficients. The energy
at level $n$ is $|\hat{L}_{n}|^2$.

The **spectral profile** of the market is the sequence $\{|\hat{L}_{n}|^2\}_{n \geq 0}$.
A market dominated by low-frequency modes (energy concentrated in small $n$) is
a factor market with clean systematic structure. A market with energy spread
across all frequencies has weak factor structure and is dominated by
idiosyncratic variation.

The spectral gap $\lambda_1$ determines the lowest non-trivial frequency. The
eigenvalue spacing $\lambda_{n+1} - \lambda_n$ determines the "frequency
response" — how sharply the market separates adjacent factors. For the simplex
Laplacian, $\lambda_{n+1} - \lambda_n = 2n + d - 1$, which grows linearly in $n$:
higher factors are increasingly well-separated.

---

## 4. The Finite Group Construction

### 4.1 The symmetric group action

The symmetric group $S_d$ acts on $\Delta_{d-1}$ by permuting coordinates:

$$\sigma \cdot (b_1, \ldots, b_d) = (b_{\sigma^{-1}(1)}, \ldots, b_{\sigma^{-1}(d)}) \tag{4.1}$$

This action preserves the Fisher-Rao metric ($g^{\rm FR}$ depends on coordinates
only through the values $b_i$, not their labelling) and maps $S^{d-1}_{+}$ to itself
isometrically. The equal-weight portfolio $b_{\rm eq} = (1/d, \ldots, 1/d)$ is
the unique fixed point of the full $S_d$ action.

### 4.2 Peter-Weyl decomposition

By the Peter-Weyl theorem, the space of square-integrable functions on the simplex
decomposes into isotypic components under the $S_d$ action:

$$L^2(\Delta_{d-1}) = \bigoplus_{\lambda \vdash d} V_\lambda \otimes V_\lambda^{\ast} \tag{4.2}$$

where the sum runs over partitions $\lambda$ of $d$ (equivalently, over irreducible
representations of $S_d$), $V_\lambda$ is the irreducible representation space of
dimension $\dim V_\lambda = f^\lambda$ (given by the hook-length formula), and
$V_\lambda^{\ast}$ is its dual.

The partitions $\lambda \vdash d$ correspond to Young diagrams, and the
irreducible representations have a direct financial interpretation:

| Partition | Young diagram | Representation | Financial interpretation |
|:----------|:-------------|:---------------|:------------------------|
| $(d)$ | single row | Trivial (1-dim) | Market-wide average: equal treatment of all assets |
| $(d-1,1)$ | row + one box | Standard $(d-1)$-dim | CAPM deviations: how each asset differs from average |
| $(d-2,2)$ | two rows | Second antisymmetric | Pairwise interactions: sector/value effects |
| $(d-2,1,1)$ | row + column | Mixed | Three-way asymmetries |
| $(1^d)$ | single column | Sign (1-dim) | Fully antisymmetric: detects ordering (momentum?) |

### 4.3 The $G$-dual market manifold

For any subgroup $G \leq S_d$, define the **$G$-dual market manifold**:

$$M^r_G = \{b \in M^r : g \cdot b = b \forall\, g \in G\} \tag{4.3}$$

This is the submanifold of $M^r$ that is invariant under $G$ — the set of
portfolios on $M$ that are unchanged by the permutations in $G$.

**Extreme cases:**

- $M^r_{S_d} = \{b_{\rm eq}\}$: the $S_d$-invariant submanifold is a single
  point — the equal-weight portfolio (or its projection onto $M^r$). This is the
  maximally symmetric market: all assets are interchangeable.

- $M^r_{\{e\}} = M^r$: the trivially invariant submanifold is all of $M^r$.
  No symmetry constraint, full market manifold.

The lattice of subgroups $\{e\} \leq G_1 \leq G_2 \leq \cdots \leq S_d$ gives
a nested family of dual manifolds:

$$M^r = M^r_{\{e\}} \supseteq M^r_{G_1} \supseteq M^r_{G_2} \supseteq \cdots \supseteq M^r_{S_d} = \{b_{\rm eq}\} \tag{4.4}$$

Each inclusion $M^r_{G_2} \subseteq M^r_{G_1}$ (for $G_1 \leq G_2$) is a
symmetry-constrained restriction: the market at the coarser level sees fewer
distinctions between assets.

### 4.4 Factor hierarchy as representation theory

**Theorem 4.1** *(Factor hierarchy = representation decomposition).*
*Let $M^r$ be a market manifold with symmetry group $\mathrm{Aut}(M) \leq S_d$.
The factor decomposition of the market — the decomposition of the return space
into systematic factors and idiosyncratic noise — is the isotypic decomposition
of $L^2(M^r)$ under the action of $\mathrm{Aut}(M)$:*

$$L^2(M^r) = \bigoplus_{\lambda \vdash d} m_\lambda \cdot V_\lambda \tag{4.5}$$

*where $m_\lambda \geq 0$ is the multiplicity of the irreducible representation
$V_\lambda$ in the restricted action on $M^r$. The number of factors is*
$r = \#\{\lambda : m_\lambda > 0\} - 1$ *(excluding the trivial representation).*

*Proof sketch.* The return vector $x_t \in \mathbb{R}^{d}_+$ transforms under $S_d$ by
the permutation representation. The component of $x_t$ in $V_{(d)}$ (the trivial
representation) is the market return $\bar{x}_{t} = \frac{1}{d}\sum_i x_{t,i}$, which
carries no portfolio information. The component in $V_{(d-1,1)}$ (the standard
representation) is the vector of deviations $x_{t,i} - \bar{x}_{t}$, which carries
all the CAPM factor information. Higher representations capture higher-order
interactions.

The actual symmetry group $\mathrm{Aut}(M)$ of the market manifold is typically
a proper subgroup of $S_d$ (not all assets are interchangeable). The isotypic
decomposition under $\mathrm{Aut}(M)$ refines the $S_d$ decomposition: irreducible
representations of $S_d$ may split into multiple irreducible representations of
$\mathrm{Aut}(M)$, producing additional factors. Each such splitting corresponds
to a systematic factor that distinguishes assets within a previously symmetric
group. $\square$

**Corollary 4.2** *(CAPM is maximally symmetric).*
*A market has CAPM factor structure (one factor, $r = 1$) if and only if only
two irreducible representations of $\mathrm{Aut}(M)$ appear in the decomposition:
the trivial and one non-trivial. In this case, $\mathrm{Aut}(M)$ acts
transitively on the assets (up to the market portfolio).*

---

## 5. Specific Group Constructions

### 5.1 Table of group duals

| Group $G$ | Order | Irreps | Dual structure | Market interpretation |
|:-----------|:------|:-------|:---------------|:---------------------|
| $S_d$ | $d!$ | Partitions $\lambda \vdash d$ | Jacobi polynomial factors | Full permutation symmetry: all assets exchangeable |
| $\mathbb{Z}_{d}$ | $d$ | Roots of unity $\omega^k$ | Fourier modes (DFT) | Cyclic/seasonal structure |
| $(\mathbb{Z}_{2})^d$ | $2^d$ | Characters $\chi_S$, $S \subseteq [d]$ | Walsh functions | Binary interactions (HYPERCUBE_SHAPLEY) |
| $S_{d_1} \times \cdots \times S_{d_k}$ | $\prod d_j!$ | Tensor products $\bigotimes \lambda_j$ | Per-sector partitions | Sector structure: within vs between |
| $D_d$ (dihedral) | $2d$ | 2D reps + signs | Pairs of Fourier modes | Pairs trading symmetries |
| $A_d$ (alternating) | $d!/2$ | Self-associate partitions | Even permutations only | Orientation-preserving relabellings |

### 5.2 The cyclic group $\mathbb{Z}_{d}$

The cyclic group $\mathbb{Z}_{d} = \langle \sigma_{\rm cyc} \rangle$ acts on
$\Delta_{d-1}$ by the cyclic permutation $\sigma_{\rm cyc}: (b_1, b_2, \ldots,
b_d) \mapsto (b_d, b_1, \ldots, b_{d-1})$. Its irreducible representations
are one-dimensional, indexed by the $d$-th roots of unity:

$$\chi_k(\sigma_{\rm cyc}^{j}) = \omega^{jk}, \qquad \omega = e^{2\pi i/d}, \quad k = 0, 1, \ldots, d-1 \tag{5.1}$$

The isotypic decomposition under $\mathbb{Z}_{d}$ is the **discrete Fourier transform**
on the simplex. The $k$-th Fourier mode captures variations at frequency $k/d$
around the cyclic ordering of assets. This is the natural dual for markets with
temporal or seasonal cyclical structure — for instance, commodity markets with
annual production cycles, where the asset ordering reflects calendar months.

### 5.3 The binary group $(\mathbb{Z}_{2})^d$

The group $(\mathbb{Z}_{2})^d$ acts on $\Delta_{d-1}$ by sign flips $b_i \mapsto
1 - b_i$ (projected back to the simplex). Its characters are the Walsh functions:

$$\chi_S(b) = \prod_{i \in S}(-1)^{\mathbf{1}_{b_i < 1/d}}, \qquad S \subseteq [d] \tag{5.2}$$

**This is the Walsh-Jacobi correspondence of HYPERCUBE_SHAPLEY.md.** The Walsh
functions on the discrete hypercube $\{-1,+1\}^{d}$, restricted to $\Delta_{d-1}
\subset [0,1]^d$, are proportional to Jacobi polynomials. The isotypic
decomposition under $(\mathbb{Z}_{2})^d$ recovers the multilinear structure of
the Kelly growth rate, and the Shapley values $\phi_i = b^{\ast}_{i}(\mu_i - \bar{\mu})$
are the Level 1 Walsh-Fourier coefficients.

### 5.4 The sector group $S_{d_1} \times \cdots \times S_{d_k}$

If the $d$ assets are divided into $k$ sectors of sizes $d_1, \ldots, d_k$
($\sum d_j = d$), the natural symmetry group is $G_{\rm sec} = S_{d_1} \times
\cdots \times S_{d_k}$: assets within a sector are exchangeable, assets across
sectors are not. The irreducible representations are tensor products
$V_{\lambda_1} \otimes \cdots \otimes V_{\lambda_k}$ where $\lambda_j \vdash d_j$.

The isotypic decomposition under $G_{\rm sec}$ separates:

- **Within-sector factors:** Represented by non-trivial $\lambda_j$ in a single
  sector with trivial representations elsewhere. These are sector-specific
  systematic risks.

- **Between-sector factors:** Represented by non-trivial representations in
  multiple sectors simultaneously. These are cross-sector (macro) factors.

This is the group-theoretic foundation of the practitioner's distinction between
"sector risk" and "market risk." The representation theory makes it precise.

### 5.5 The dihedral group $D_d$

The dihedral group $D_d = \langle \sigma_{\rm cyc}, \tau_{\rm rev} \rangle$, where
$\tau_{\rm rev}: (b_1, \ldots, b_d) \mapsto (b_d, \ldots, b_1)$ is the
reversal, adds a reflection symmetry to the cyclic structure. Its two-dimensional
irreducible representations pair Fourier modes $\chi_k$ and $\chi_{d-k}$ into
real representations. The $D_d$-invariant portfolios are symmetric under both
cyclic permutation and reversal — they are the "palindromic" portfolios.

For pairs trading (PAIRS_TRADING.md), the relevant group is $D_2 \cong
\mathbb{Z}_2 \times \mathbb{Z}_2$, acting on a pair of assets by
exchange and by joint reflection about the mean. The invariant submanifold
$M^r_{D_2}$ consists of the symmetric spread positions, and the two-dimensional
representation captures the anti-symmetric component — the spread itself.

---

## 6. The Three Towers Are Isomorphic

### 6.1 Statement

**Theorem 6.1** *(Tower isomorphism).*
*The Giry tower, the spectral tower, and the group tower all give the same
multiresolution decomposition of the market, in the following precise sense:*

*(i) The $n$-th eigenspace $E_n$ of the Laplacian on $(\Delta_{d-1}, g^{\rm FR})$
is the direct sum of the irreducible representations of $S_d$ corresponding to
partitions of degree $n$:*

$$E_n = \bigoplus_{\substack{\lambda \vdash d \\ \deg(\lambda) = n}} V_\lambda \otimes V_\lambda^{\ast} \tag{6.1}$$

*where $\deg(\lambda) = \lambda_1 - 1$ is the degree of the associated spherical
harmonic.*

*(ii) The $k$-th level of the Giry tower $\mathcal{P}^{k}(X)$ has, as its space of
linear functionals, the functions of polynomial degree at most $k$ on
$\Delta_{d-1}$, which is $\bigoplus_{n=0}^{k} E_n$.*

*(iii) Therefore the Giry tower, truncated at level $k$, is dual to the spectral
truncation $\Pi_{\leq k}$, which is the sum of the first $k+1$ isotypic
components of the $S_d$ action.*

*Proof sketch.* Part (i) is a classical result in the representation theory of
the orthogonal group: the restriction of the $n$-th spherical harmonic space on
$S^{d-1}$ to the $S_d$ action decomposes into irreducible representations
indexed by partitions of length at most $d$ and degree $n$. The Jacobi
polynomials that span $E_n$ (Section 3.2) are the zonal spherical functions of
these representations.

Part (ii) follows from the structure of the Giry monad on finite sets.
$\mathcal{P}^{k}(X)$ is the space of $k$-th order type functionals on $X$. The
moments of a distribution $\Pi \in \mathcal{P}^{k}(X)$ that distinguish it from
lower-order objects are precisely the degree-$k$ polynomial moments — which lie
in $E_k$. The Giry multiplication $\mu$ collapses the $k$-th level by integrating
out the degree-$k$ variation, which is equivalent to the spectral projection
$\Pi_{\leq k} \to \Pi_{\leq k-1}$.

Part (iii) combines (i) and (ii): the Casimir operator of the $S_d$ representation
$V_\lambda$ has eigenvalue determined by $\deg(\lambda)$, which equals the
Laplacian eigenvalue $\lambda_n$. The Casimir mediates the isomorphism between
the group-theoretic and spectral decompositions. $\square$

### 6.2 The isomorphism in practice

Consider a $d = 10$ asset market with $r = 3$ factors:

| Tower level | Giry | Spectral | Group | Finance |
|:------------|:-----|:---------|:------|:--------|
| 0 | Pure states ($X$) | $E_0$ = constants | Trivial rep $(d)$ | Market portfolio |
| 1 | Portfolios ($\Delta_9$) | $E_1$ = first Jacobi | Standard rep $(d-1,1)$ | CAPM factor |
| 2 | Fund-of-funds ($\mathcal{P}^{2}$) | $E_2$ = second Jacobi | $(d-2,2)$ + $(d-2,1,1)$ | Value + size factors |
| 3 | Meta-allocator ($\mathcal{P}^{3}$) | $E_3$ = third Jacobi | Degree-3 reps | Third factor (momentum?) |
| $\geq 4$ | Higher beliefs | $E_{\geq 4}$ = high-frequency | Higher reps | Idiosyncratic noise |

The three factors ($r = 3$) correspond to the three non-trivial levels at which
the spectral energy is concentrated. The representation theory tells us not just
*that* there are three factors, but *what symmetry* each factor breaks.

### 6.3 Consequences

**Corollary 6.2** *(Dimensionality from representation theory).*
*The manifold dimension $r$ equals the number of distinct non-trivial
irreducible representations of $\mathrm{Aut}(M)$ that appear with non-zero
multiplicity in the isotypic decomposition of $L^2(M^r)$.*

**Corollary 6.3** *(MUP regret from representation theory).*
*The MUP regret $r\log T/(2T)$ counts the number of non-trivial representations
that must be learned. Each representation contributes $\log T/(2T)$ to the regret
— the cost of estimating one symmetry-breaking direction.*

---

## 7. The Legendre Dual

### 7.1 The Legendre-Fenchel transform

For functions rather than sets, the canonical dual is the Legendre-Fenchel
conjugate. The Kelly function $L_T: \Delta_{d-1} \to \mathbb{R}$ is concave. Its
Legendre-Fenchel conjugate is:

$$L_T^{\ast}(y) = \sup_{b \in \Delta_{d-1}} \left[\langle b, y \rangle - L_T(b)\right] \tag{7.1}$$

This is a convex function on $\mathbb{R}^{d}$. The conjugate $L_T^{\ast}$ is the
**rate function** of portfolio large deviations: $L_T^{\ast}(y)$ measures the
exponential cost of the portfolio achieving growth rate profile $y$ when the true
optimal is at $b^{\ast}$.

**Proposition 7.1** *(Kelly-rate function duality).*
*The rate function $L_T^{\ast}$ satisfies:*

*(i) $L_T^{\ast}(y) \geq 0$ with equality iff $y = \nabla L_T(b^{\ast})$ (the optimal
gradient).*

*(ii) Near the optimum: $L_T^*(y^* + \delta y) \approx \frac{1}{2}\delta y^T
[F_M(b^*)]^{-1} \delta y$, where $F_M(b^*)$ is the Fisher information matrix.*

*(iii) The MUP is the saddle-point: $\hat{b}^M_T = \arg\min_{b}
\sup_{y}[\langle b, y \rangle - L_T^*(y)]$.*

*Proof.* Part (i) is the definition of the conjugate at the dual optimum.
Part (ii) follows from the second-order expansion of $L_T$ at $b^{\ast}$: the
Hessian is $-F_M(b^{\ast})$, so the conjugate's Hessian is the inverse.
Part (iii) is the minimax theorem applied to the bilinear coupling. $\square$

### 7.2 Duality interpretation

The Legendre-Fenchel duality

$$\text{concave Kelly landscape} \longleftrightarrow \text{convex rate function} \tag{7.2}$$

is the function-level analogue of the Giry tower's set-level duality. The Kelly
function tells you the growth rate as a function of portfolio choice. The rate
function tells you the cost of deviation from optimality. They contain exactly
the same information, viewed from dual perspectives.

---

## 8. The Pontryagin Dual and Market Fourier Analysis

### 8.1 Pontryagin duality for abelian groups

For an abelian group $A$ acting on the simplex, the Pontryagin dual
$\hat{A} = \mathrm{Hom}(A, U(1))$ is the group of characters. The Peter-Weyl
decomposition reduces to the Fourier expansion:

$$f(b) = \sum_{\chi \in \hat{A}} \hat{f}(\chi)\,\chi(b) \tag{8.1}$$

with Fourier coefficients $\hat{f}(\chi) = \int_\Delta f(b)\,\overline{\chi(b)}
\,d\mu(b)$.

### 8.2 The cyclic case: market DFT

For the cyclic group $\mathbb{Z}_{d}$ acting by cyclic permutation, the Pontryagin
dual is $\hat{\mathbb{Z}}_{d} \cong \mathbb{Z}_{d}$ — the group is **self-dual**.
The characters are the roots of unity $\chi_k(\sigma^j) = e^{2\pi ijk/d}$. The
Fourier decomposition of returns is:

$$x_{t,j} = \sum_{k=0}^{d-1} \hat{x}_{t,k}\, e^{2\pi ijk/d} \tag{8.2}$$

The low-frequency components ($k$ small) capture the factor structure (systematic
risk). The high-frequency components ($k$ near $d/2$) capture idiosyncratic
variation. The spectral gap $\lambda_1$ from the Laplacian corresponds to the
lowest non-zero Fourier frequency $k = 1$.

### 8.3 The torus case: Clifford market Fourier analysis

For the Clifford torus market $T^2$ (CLASSIFICATION.md, MARKET_PROCESSES.md),
the natural symmetry group is $U(1) \times U(1)$ — the continuous torus group.
The Pontryagin dual of $T^r = U(1)^r$ is the **integer lattice**:

$$\widehat{T^r} = \mathbb{Z}^{r} \tag{8.3}$$

The characters are $\chi_{(n_1,\ldots,n_r)}(\theta_1,\ldots,\theta_r) =
e^{i(n_1\theta_1 + \cdots + n_r\theta_r)}$ for $(n_1,\ldots,n_r) \in
\mathbb{Z}^r$. The Fourier decomposition of a function on the Clifford torus
market is:

$$f(\theta) = \sum_{n \in \mathbb{Z}^{r}} \hat{f}(n)\, e^{i\langle n, \theta\rangle} \tag{8.4}$$

This connects directly to the theta-function transition density of
MARKET_PROCESSES.md: the heat kernel on $T^r$ is

$$K_{T^r}(t, \theta, \theta') = \sum_{n \in \mathbb{Z}^{r}} e^{-|n|^2 t/(2\varepsilon^2)}\, e^{i\langle n, \theta - \theta'\rangle} \tag{8.5}$$

which is the Jacobi theta function $\vartheta_3$. The Fourier modes indexed by
$\mathbb{Z}^{r}$ are exactly the spectral dual tower (Section 3) applied to the
flat torus geometry. The integer lattice $\mathbb{Z}^{r}$ is simultaneously:

- The Pontryagin dual of the torus symmetry group,
- The eigenvalue indexing set of the Laplacian on $T^r$,
- The set of winding numbers of closed geodesics on $T^r$.

### 8.4 Non-abelian duality

For non-abelian groups (such as $S_d$ for $d \geq 3$), the Pontryagin dual does
not exist in the classical sense — the dual object is the set of irreducible
representations, not a group. This is the Tannaka-Krein duality: a compact
group $G$ is determined (up to isomorphism) by its category of representations
$\mathrm{Rep}(G)$. The dual of the market's symmetry group is its
representation category — which is exactly the factor decomposition.

---

## 9. Applications

### 9.1 Multiresolution portfolio construction

The tower decomposition suggests a **level-by-level portfolio construction**:

1. **Level 0:** Set the overall equity allocation (market portfolio weight).
2. **Level 1:** Determine the CAPM tilt (the standard representation component).
3. **Level 2:** Add sector and style tilts (second isotypic component).
4. **Level $k$:** Add the $k$-th factor tilt.
5. **Truncate at level $r$:** All higher levels are idiosyncratic noise — do not
   trade on them.

The MUP regret bound $r\log T/(2T)$ guarantees that truncation at level $r$ loses
at most $r$ dimensions of regret. Trading on levels $k > r$ adds
$(k-r)\log T/(2T)$ regret for zero expected gain — pure overfitting.

### 9.2 Risk decomposition by representation

Total portfolio variance decomposes as:

$$\mathrm{Var}(r_p) = \sum_{\lambda \vdash d} m_\lambda \cdot \mathrm{Var}_\lambda(r_p) \tag{9.1}$$

where $\mathrm{Var}_\lambda$ is the variance contributed by the irreducible
representation $V_\lambda$. This is the representation-theoretic analogue of
factor risk decomposition. The trivial representation $(d)$ contributes market
risk; the standard representation $(d-1,1)$ contributes CAPM-beta risk; higher
representations contribute sector, style, and interaction risks.

### 9.3 The VIX as a spectral measurement

The VIX measures implied volatility of the S\&P 500 index — a market-wide
average. In the tower framework, the VIX is a measurement of $E_0$ (the
zero-frequency component). A "sector VIX" would measure $E_1$ (the first factor).
The full term structure of VIX futures is a measurement of the spectral profile
$\{|\hat{L}_{n}|^2\}$ at different time horizons.

### 9.4 Sector rotation as representation change

When market leadership rotates from one sector to another, the active
representation changes. If the market transitions from a technology-led regime
to a value-led regime, the dominant non-trivial representation shifts from one
irreducible component of $V_{(d-1,1)}$ to another. The representation theory
provides a coordinate-free description of regime change: it is not that
"different stocks go up," but that the market's symmetry group changes, and with
it the active representation.

---

## 10. Open Problems

**OP-A.** *(The quantum dual tower).* Replace the Giry monad with the quantum
probability monad (density matrices instead of distributions). Does the resulting
tower have a market interpretation? The quantum case admits entangled states at
Level 2 that have no classical analogue — what is the financial meaning of
entanglement between portfolio strategies? Difficulty: ★★★.

**OP-B.** *(The infinite-dimensional Giry tower).* For $d = \infty$ (a continuum
of assets), the simplex $\Delta_\infty$ is the space of probability measures on
$[0,\infty)$. The Giry tower $\mathcal{P}^{k}(\Delta_\infty)$ is a tower of
infinite-dimensional convex spaces. Does the spectral decomposition remain
discrete, or does a continuous spectrum appear? If continuous, what is the
financial interpretation of "spectral measure" vs "spectral eigenvalue"?
Difficulty: ★★.

**OP-C.** *(The dual of the dual).* For the Legendre-Fenchel transform:
$(L_T^{\ast})^{\ast} = L_T$ (bidual = original, since $L_T$ is concave and upper
semicontinuous). For the Pontryagin dual: $\hat{\hat{A}} \cong A$ (by the
Pontryagin duality theorem). For the Giry tower: does a notion of "dual monad"
exist such that applying it twice returns to the original? Difficulty: ★★★.

**OP-D.** *(Optimal group selection).* Given a return matrix $X \in
\mathbb{R}^{T \times d}$, find the subgroup $G \leq S_d$ whose isotypic
decomposition best explains the factor structure (in a minimum-description-length
sense). This is the group-theoretic analogue of PCA: instead of finding the
best linear subspace, find the best symmetry group. Is this problem
NP-hard? Difficulty: ★★.

**OP-E.** *(Crises and representation collapse).* A financial crisis
corresponds to a sudden change in the market manifold $M^r$ — typically a
reduction in effective dimension as correlations increase. In the representation
framework, this is a **symmetry restoration**: the market's effective symmetry
group grows (more assets become interchangeable), and higher representations
collapse into lower ones. Is there a representation-theoretic early warning
indicator analogous to the Feigenbaum bifurcation of CHAOS_TAKENS.md?
Difficulty: ★★★.

---

## 11. Conclusion

Three independent constructions — categorical (the Giry monad), analytic (the
spectral decomposition), and algebraic (the representation theory of finite
groups) — produce the same infinite tower of dual spaces on the information
simplex. The isomorphism between them (Theorem 6.1) is not a coincidence; it
reflects the deep structure of the simplex as a homogeneous space for the
symmetric group.

The practical consequence is a single sentence:

> **The factor structure of a market is the representation theory of its symmetry group.**

A CAPM market has maximally symmetric factor structure (one non-trivial
representation). A multi-factor market has partially broken symmetry (several
representations). An idiosyncratic market has no symmetry at all. The number
of factors $r$ counts the number of symmetry-breaking directions. The MUP
regret $r\log T/(2T)$ is the cost of learning each broken symmetry from data.
Crises are symmetry restorations; sector rotations are representation changes;
diversification is eigenvalue repulsion; and the spectral gap is the coarsest
non-trivial frequency of the market.

The dual tower provides the architecture. The representation theory fills in
the content. Together, they give a complete multiresolution analysis of any
financial market, with each level of resolution corresponding to one level of
the tower, one eigenspace of the Laplacian, and one irreducible representation
of the symmetry group.

---

## References

1. Giry, M. (1982). A categorical approach to probability theory. In *Categorical
   Aspects of Topology and Analysis*, Lecture Notes in Mathematics 915, pp. 68–85.
   Springer.

2. Fritz, T. (2020). A synthetic approach to Markov kernels, conditional
   independence and theorems on sufficient statistics. *Advances in Mathematics*,
   370, 107239.

3. Peter, F. and Weyl, H. (1927). Die Vollständigkeit der primitiven
   Darstellungen einer geschlossenen kontinuierlichen Gruppe. *Mathematische
   Annalen*, 97, 737–755.

4. Pontryagin, L. (1934). The theory of topological commutative groups. *Annals
   of Mathematics*, 35(2), 361–388.

5. Serre, J.-P. (1977). *Linear Representations of Finite Groups*. Graduate
   Texts in Mathematics 42. Springer.

6. Dunkl, C. F. and Xu, Y. (2014). *Orthogonal Polynomials of Several
   Variables*. Encyclopedia of Mathematics and its Applications 155. Cambridge
   University Press, 2nd edition.

7. James, G. and Kerber, A. (1981). *The Representation Theory of the Symmetric
   Group*. Encyclopedia of Mathematics and its Applications 16. Cambridge
   University Press.

8. Cover, T. M. (1991). Universal portfolios. *Mathematical Finance*, 1(1), 1–29.

9. Amari, S. and Nagaoka, H. (2000). *Methods of Information Geometry*. Translations
   of Mathematical Monographs 191. American Mathematical Society.

10. Tannaka, T. (1939). Über den Dualitätssatz der nichtkommutativen
    topologischen Gruppen. *Tohoku Mathematical Journal*, 45, 1–12.

11. Krein, M. G. (1949). A principle of duality for bicompact groups and
    quadratic block algebras. *Doklady Akademii Nauk SSSR*, 69, 725–728.

12. Mallat, S. (1989). A theory for multiresolution signal decomposition:
    the wavelet representation. *IEEE Transactions on Pattern Analysis and
    Machine Intelligence*, 11(7), 674–693.
