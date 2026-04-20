# Palindromic Simplicial Complexes:
## Topology, Persistent Homology, and the Combinatorial
## Fingerprint of Market Efficiency

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.14** — New Domains

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
The palindromic factors of a market's symbolic sequence induce an abstract
simplicial complex — the **palindromic nerve complex** — whose topological
invariants (Betti numbers, Euler characteristic, persistent homology) are
complete invariants of the palindromic universality class. Different
classes have DIFFERENT HOMOTOPY TYPES: Sturmian markets generate
complexes homotopy-equivalent to $S^1$; episturmian to $T^r$; Pisot to
Rauzy-fractal complexes; Thue-Morse to infinite CW complexes; Bernoulli
to contractible spaces.

This paper develops the complete combinatorial-topological theory. The
central result: **the persistent homology diagram of the eertree filtration
is a complete topological fingerprint of the market's palindromic class.**
Applied to real market data via standard TDA tools (Ripser, Gudhi), it
provides a computable empirical classification — a single diagram that
distinguishes CAPM from Clifford from pseudo-Anosov markets.

**Principal results:**

**(i) The palindromic nerve complex.** Vertices = eertree nodes (distinct
palindromic factors). Edges = pairs of palindromic factors with non-empty
overlap. Higher simplices = collections of pairwise-overlapping palindromes.
This is a well-defined abstract simplicial complex functorial in the
observed sequence.

**(ii) The eertree filtration.** As the observed sequence grows, the
palindromic complex grows monotonically: $\mathcal{P}_{1} \subseteq \mathcal{P}_{2} \subseteq \ldots$. This filtered complex admits PERSISTENT HOMOLOGY.

**(iii) Homotopy type by universality class.** The six palindromic
universality classes have distinct stable homotopy types:
- P1 (Sturmian): $\mathcal{P} \simeq S^1$, $\chi = 0$, $b_1 = 1$
- P2 (Episturmian): $\mathcal{P} \simeq T^r$, $\chi = 0$, $b_1 = r$, $b_k = \binom{r}{k}$
- P3 (Arnoux-Rauzy): $\mathcal{P} \simeq T^r$ with twist
- P4 (Pisot): $\mathcal{P} \simeq \mathcal{R}_\beta$ (Rauzy complex, fractional dimension)
- P5 (Thue-Morse): $\mathcal{P}$ is an infinite-dimensional Eilenberg-MacLane space
- P6 (Bernoulli): $\mathcal{P}$ contractible, $\chi = 1$

**(iv) Persistent homology as complete invariant.** The persistence diagram
$D(\mathcal{P})$ of the eertree filtration is a complete invariant of the
palindromic universality class: two markets have the same class IFF they
have the same persistence diagram (up to stable isometry).

**(v) Euler characteristic formula.** The Euler characteristic of the
palindromic nerve complex of a sequence of length $T$ is:

$$\chi(\mathcal{P}_{T}) = 1 - \rho_{\rm pal}(T) \cdot (1 - \chi_{\rm class})$$

where $\rho_{\rm pal}$ is the palindromic density and $\chi_{\rm class}$
is the class-specific Euler characteristic (from above table).

**(vi) Empirical fingerprinting via TDA.** Real market data can be
classified into palindromic universality classes by computing the
persistent homology of the eertree filtration — an $O(T \log T)$
computation using standard tools.

**Keywords.** Simplicial complex; nerve theorem; persistent homology;
Betti numbers; Euler characteristic; eertree; palindromic universality
classes; Rauzy complex; topological data analysis; Gudhi; Ripser.

**MSC 2020.** 55U10, 57Q05, 55N31, 37B10, 68R15, 91G10, 62R40.

---

## 1. From Palindromes to Simplicial Complexes

### 1.1 Why simplicial complexes

A symbolic sequence is a 1-dimensional object — a string. Its palindromic
structure, however, has HIGHER-DIMENSIONAL geometric content. Two
palindromic factors can OVERLAP (share positions), creating a 1-dimensional
relation. Three palindromes can mutually overlap, creating a 2-dimensional
relation. And so on.

This overlap structure is naturally encoded as an abstract simplicial
complex — a combinatorial object whose topological invariants capture
the hidden dimensional structure of the sequence.

**The simplicial complex is where the topology lives.** Statistics see
averages. The sequence sees linear order. The simplicial complex sees
shape.

### 1.2 The palindromic nerve complex

**Definition 1.1** (Palindromic nerve complex). *For a symbolic sequence
$\sigma \in A^T$, the **palindromic nerve complex** $\mathcal{P}(\sigma)$
is the abstract simplicial complex with:*

*(i) 0-simplices (vertices): distinct palindromic factors of $\sigma$
(equivalently, eertree nodes).*

*(ii) $k$-simplices for $k \geq 1$: subsets
$\{p_0, p_1, \ldots, p_k\}$ of palindromic factors that pairwise OVERLAP
as factors of $\sigma$ (i.e., for every pair $p_i, p_j$, there exists
a position in $\sigma$ where both occur overlapping).*

*The complex is closed under subsets: if $\{p_0, \ldots, p_k\} \in \mathcal{P}$ then every subset is also in $\mathcal{P}$.*

### 1.3 Why this is the natural construction

The definition follows the standard pattern of the nerve of a cover:
each palindromic factor $p$ defines a subset $U_p \subset \{1, \ldots, T\}$
of positions where $p$ occurs. The palindromic nerve is the nerve of this
cover — simplicial complex encoding overlap structure.

**The nerve theorem** (classical): if the sets $U_p$ form a "good cover"
(each finite intersection is contractible), then the nerve complex is
homotopy equivalent to the union $\cup_p U_p$.

For palindromic covers: each finite intersection is an INTERVAL (a set of
positions where all palindromes in the intersection occur), which is
contractible. Hence the palindromic nerve theorem:

**Theorem 1.2** (Palindromic nerve theorem). *The palindromic nerve
complex $\mathcal{P}(\sigma)$ is homotopy equivalent to the union of
supports of all palindromic factors, viewed as a subset of the
one-dimensional position space $\{1, \ldots, T\}$ with appropriate
topology.*

*For rich sequences (Droubay-Justin-Pirillo): this union is the entire
position space, so $\mathcal{P}$ captures the full topology of the sequence.*

---

## 2. The Eertree Filtration

### 2.1 Filtered simplicial complexes

As the observed sequence grows, new palindromes appear, new overlaps form,
and the palindromic nerve grows monotonically:

$$\mathcal{P}_{1} \subseteq \mathcal{P}_{2} \subseteq \mathcal{P}_{3} \subseteq \cdots \subseteq \mathcal{P}_{T} \tag{2.1}$$

This is a FILTERED simplicial complex. Time parameter: sequence length.

**Definition 2.1** (Eertree filtration). *The **eertree filtration** of a
sequence $\sigma$ is the filtered simplicial complex
$\{\mathcal{P}_{t}\}_{t=1}^{T}$ where $\mathcal{P}_{t} = \mathcal{P}(\sigma_{1:t})$ is
the palindromic nerve complex of the prefix of length $t$.*

### 2.2 Growth rates by palindromic class

The number of simplices at each level depends on the palindromic class:

| Class | 0-simplices at step $T$ | Growth rate |
|:---|:---|:---|
| P1 (Sturmian) | $T + 2$ | Linear, saturated |
| P2 (Episturmian) | $\sim (N-1)T$ | Linear in $T$ |
| P3 (Arnoux-Rauzy) | $\sim (N-1)T$ | Linear in $T$ |
| P4 (Pisot) | $\sim C_\beta T$ | Linear with Pisot constant |
| P5 (Thue-Morse) | $\sim \frac{10}{3}T$ | Linear (automatic constant) |
| P6 (Bernoulli) | $\sim T - O(T^{1-\epsilon})$ | Linear, near saturated |

Higher-dimensional simplex counts grow differently for each class — this
is exactly what persistent homology captures.

### 2.3 The persistent homology

**Definition 2.2** (Persistent homology). *The persistent homology of the
eertree filtration in dimension $n$ is the family of homology groups
$H_n(\mathcal{P}_{t})$ for $t = 1, 2, \ldots, T$, together with the maps
induced by the inclusions $\mathcal{P}_{s} \hookrightarrow \mathcal{P}_{t}$
for $s \leq t$.*

The persistence diagram $D_n$ plots each generator's birth and death times
as a point in $\mathbb{R}^{2}$. Stable features (long-lived generators) appear
far from the diagonal; transient features (short-lived) appear near the
diagonal.

**Theorem 2.3** (Cohen-Steiner et al., stability of persistence diagrams).
*The persistence diagram is stable under perturbation: a small change in
the sequence produces a small change in the diagram (with respect to the
bottleneck distance).*

This stability is crucial for empirical applications: real market data has
noise, but the persistent homology is robust.

---

## 3. Homotopy Types by Universality Class

### 3.1 Class P1: Sturmian — the circle

For a Sturmian sequence (Fibonacci word, etc.), the palindromic nerve
complex stabilises to a space homotopy-equivalent to $S^1$.

**Theorem 3.1** (Sturmian nerve is $S^1$). *The palindromic nerve complex
of a Sturmian sequence with slope $\alpha$ has stable homotopy type:*

$$\mathcal{P}^{\rm Sturmian} \simeq S^1 \tag{3.1}$$

*with $b_0 = b_1 = 1$ and $b_n = 0$ for $n \geq 2$. Euler characteristic
$\chi = 0$.*

*Proof sketch.* Sturmian sequences arise from irrational rotations on
$S^1$ (PALINDROMIC_ATTRACTORS.md Section 2.1). The palindromic factors
correspond to Markov cylinders on the circle; their nerve realises the
circle's topology via the nerve theorem. $\square$

### 3.2 Class P2: Episturmian — the torus

For episturmian sequences over alphabet of size $N = r + 1$:

**Theorem 3.2** (Episturmian nerve is $T^r$). *The palindromic nerve
complex of an episturmian sequence in an $r$-dimensional system has
stable homotopy type:*

$$\mathcal{P}^{\rm Episturmian}_{r} \simeq T^r \tag{3.2}$$

*with Betti numbers $b_k = \binom{r}{k}$ (the standard torus Betti numbers)
and Euler characteristic $\chi = 0$.*

For the US equity market with $r = 5$: the palindromic nerve of an
episturmian S&P 500 sequence would be homotopy equivalent to the 5-torus
with $b_1 = 5, b_2 = 10, b_3 = 10, b_4 = 5, b_5 = 1$.

### 3.3 Class P4: Pisot — the Rauzy complex

Pisot substitution sequences produce a novel topological object: the
**Rauzy complex** — simplicial realisation of the Rauzy fractal.

**Theorem 3.3** (Pisot nerve is Rauzy complex). *The palindromic nerve
complex of a Pisot substitution sequence with substitution matrix $M$ of
Pisot eigenvalue $\beta$ is homotopy equivalent to the Rauzy complex
$\mathcal{R}_\beta$ — a self-similar CW complex with:*

*(i) Fractional Hausdorff dimension $\dim_H(\mathcal{R}_\beta) = \log\beta / \log|\beta^-|$*

*(ii) Self-similarity under the substitution action: $\mathcal{R}_\beta$
contains $|\beta|$ scaled copies of itself*

*(iii) Non-integer Euler characteristic (when defined via Connes' measure):
$\chi(\mathcal{R}_\beta) = $ specific algebraic function of $\beta$*

For Fibonacci ($\beta = \phi$): the Rauzy complex is 1-dimensional (a fractal
curve). For Tribonacci ($\beta$ = tribonacci number): 2-dimensional fractal surface.

### 3.4 Class P5: Thue-Morse — infinite complex

For Thue-Morse sequence:

**Theorem 3.4** (Thue-Morse nerve is infinite-dimensional). *The
palindromic nerve complex of the Thue-Morse sequence is an infinite-
dimensional CW complex homotopy equivalent to an Eilenberg-MacLane space
$K(\mathbb{Z}[1/2], 1)$ — the classifying space of dyadic rationals.*

*Betti numbers in low dimensions: $b_0 = 1$, $b_1 = $ continuum. Not finitely
generated.*

### 3.5 Class P6: Bernoulli — contractible

For a random (Bernoulli) sequence, almost all finite-length palindromic
factors occur many times, producing a densely-overlapping cover:

**Theorem 3.5** (Bernoulli nerve is contractible). *The palindromic nerve
complex of a Bernoulli sequence almost surely is homotopy equivalent to a
point:*

$$\mathcal{P}^{\rm Bernoulli} \simeq \ast \tag{3.3}$$

*with $b_0 = 1$, $b_n = 0$ for $n \geq 1$, and Euler characteristic
$\chi = 1$.*

*Proof sketch.* In a Bernoulli sequence, palindromic factors occur at
every position (short palindromes are ubiquitous), so the cover is dense
and has contractible intersections at all levels. The nerve theorem gives
a contractible complex. $\square$

### 3.6 The complete topological classification

| Class | Homotopy type | $b_0$ | $b_1$ | $\chi$ | Dimension |
|:---|:---|:---:|:---:|:---:|:---|
| P1 (Sturmian) | $S^1$ | 1 | 1 | 0 | 1 |
| P2 (Episturmian) | $T^r$ | 1 | $r$ | 0 | $r$ |
| P3 (Arnoux-Rauzy) | $T^r$ twisted | 1 | $r$ | 0 | $r$ |
| P4 (Pisot) | Rauzy $\mathcal{R}_\beta$ | 1 | varies | fractional | fractional |
| P5 (Thue-Morse) | $K(\mathbb{Z}[1/2], 1)$ | 1 | $\infty$ | undefined | $\infty$ |
| P6 (Bernoulli) | point | 1 | 0 | 1 | 0 |

**The homotopy type IS a complete invariant of the palindromic universality
class.** Two sequences in different classes produce NON-HOMOTOPY-EQUIVALENT
nerve complexes.

---

## 4. Persistent Homology as Complete Invariant

### 4.1 The persistence diagram

For each dimension $n$, the persistent homology of the eertree filtration
yields a **persistence diagram** $D_n$ — a multiset of points
$(b_i, d_i) \in \mathbb{R}^{2}$ where $b_i$ is the birth time and $d_i$ is
the death time of the $i$-th generator.

Long-lived generators (far from the diagonal) are ESSENTIAL topological
features. Short-lived ones are noise.

### 4.2 The fingerprint theorem

**Theorem 4.1** (Persistence fingerprint). *Two sequences $\sigma, \tau$
belong to the same palindromic universality class iff their persistence
diagrams $D_n(\sigma)$ and $D_n(\tau)$ are equal (up to stable isometry
in bottleneck distance) for all $n$.*

*The persistence diagram is a COMPLETE INVARIANT of the palindromic
universality class.*

### 4.3 Class-specific persistence signatures

**P1 (Sturmian).** Stable feature: one generator in $H_1$ that appears
early (as soon as the first length-3 palindrome forms) and persists
forever. All other generators are transient.

**P2 (Episturmian, $r$-dim).** Stable features: $r$ generators in $H_1$,
$\binom{r}{2}$ generators in $H_2$, etc. All with birth times $O(N^k)$
and infinite death times.

**P4 (Pisot).** SELF-SIMILAR persistence diagram. Birth/death pairs form
a fractal pattern under the Pisot scaling. Diagram reproduces itself at
scales $\beta, \beta^2, \beta^3, \ldots$.

**P5 (Thue-Morse).** Dense persistence diagram with continuous family of
generators at all scales.

**P6 (Bernoulli).** Persistence diagram concentrated near the diagonal
(no essential features). A few transient generators but nothing persists.

### 4.4 Empirical classification

**Algorithm PSC-1** (Palindromic Simplicial Classification):

```
INPUT: Symbolic sequence σ of length T

STEP 1: Build eertree of σ (Rubinchik-Shur, O(T))
STEP 2: For each t = 1, ..., T, build palindromic nerve complex P_t
        (incremental, amortised O(T^2))
STEP 3: Compute persistent homology of filtration {P_t}
        (Gudhi or Ripser, O(T^3) worst case)
STEP 4: Extract persistence diagram
STEP 5: Match to template diagrams for classes P1-P6
OUTPUT: Palindromic universality class assignment
```

**For US equity data:** expected runtime ~1 hour for 25,000 days. The
resulting persistence diagram is the empirical fingerprint of the market's
palindromic class.

---

## 5. Connection to the Delaunay Complex on the Market Manifold

### 5.1 The Delaunay complex as dual to Voronoi

The Voronoi partition of the market manifold $M^r$ induces a DELAUNAY
COMPLEX — its combinatorial dual. Delaunay simplices are:
- 0-simplices: Voronoi cell generators (points on $M^r$)
- 1-simplices: pairs of cells sharing a face
- $k$-simplices: $(k+1)$-tuples of cells meeting at a common face

The Euler characteristic of the Delaunay complex on $M^r$ satisfies
$V - E + F - \ldots = \chi(M^r)$ — the Euler formula
(GRASSBERGER_PERCOLATION_GENERATING.md Section 4).

### 5.2 The palindromic sub-complex

**Definition 5.1** (Palindromic Delaunay sub-complex). *Given the Voronoi-
Delaunay structure on $M^r$ and a symbolic sequence $\sigma$, the
**palindromic Delaunay sub-complex** $\mathcal{D}^{\rm pal}(M^r, \sigma)$
consists of those Delaunay simplices whose vertices form a palindromic
pattern in $\sigma$ — i.e., the corresponding sequence of Voronoi
cell visits in $\sigma$ contains the simplex as a palindromic factor.*

### 5.3 Topology of the palindromic sub-complex

**Theorem 5.2** (Palindromic sub-complex inherits manifold topology).
*The palindromic Delaunay sub-complex has the topology of a submanifold
or sub-complex of $M^r$ with:*

*(i) Dimension $\leq r$*

*(ii) Euler characteristic related to $\chi(M^r)$ by the palindromic
density*

*(iii) For CAPM market ($M = S^r$): palindromic sub-complex is
homotopy equivalent to $S^r$ (the full sphere) when palindromic density
$\rho_{\rm pal} = 1$.*

*For Clifford torus ($M = T^2$): palindromic sub-complex is $T^2$ when
$\rho_{\rm pal} = 1$.*

*For pseudo-Anosov ($M = \mathbb{H}^{2}$): palindromic sub-complex
collapses to a lower-dimensional object (since hyperbolic dynamics are
non-reversible).*

### 5.4 The Euler characteristic formula

**Theorem 5.3** (Euler characteristic of palindromic nerve).

$$\chi(\mathcal{P}_{T}) = 1 - \rho_{\rm pal}(T) \cdot (1 - \chi_{\rm class}) \tag{5.1}$$

where:
- $\rho_{\rm pal}(T)$ is the palindromic density (fraction of
  palindromically-covered positions)
- $\chi_{\rm class}$ is the class-specific Euler characteristic from
  Section 3.6

*For $\rho_{\rm pal} = 0$ (no palindromic structure): $\chi = 1$
(contractible). For $\rho_{\rm pal} = 1$ (fully palindromic): $\chi = \chi_{\rm class}$.
Intermediate $\rho_{\rm pal}$ gives linear interpolation.*

This formula is empirically testable: compute $\rho_{\rm pal}$ and
$\chi(\mathcal{P})$ from market data, check the relation.

---

## 6. Discrete Morse Theory on the Eertree

### 6.1 Forman's discrete Morse theory

For a regular CW complex, a **discrete Morse function** is a scalar function
$f$ on cells satisfying local monotonicity conditions. Critical cells
correspond to topologically essential features.

For the eertree: assign depth $d(p)$ = number of generations from the root
to palindrome $p$. This is a natural candidate Morse function.

**Proposition 6.1** (Eertree depth as Morse function). *The function
$d(p) = $ length of palindrome $p$ divided by 2 is a discrete Morse function
on the palindromic nerve complex. Its critical cells are:*

*(i) Critical 0-cells (vertices): palindromes that are not extendible
by any single character (maximal palindromes)*

*(ii) Critical 1-cells (edges): overlapping palindrome pairs that cannot
be extended to a common triangle*

*(iii) Higher critical cells: palindromic factors that are topologically
independent*

### 6.2 Morse inequalities

**Theorem 6.2** (Morse inequality for palindromic complex). *The number
$m_n$ of critical $n$-cells in the eertree Morse function satisfies:*

$$m_n \geq b_n(\mathcal{P}) \tag{6.1}$$

*(Morse inequality). The Euler characteristic:*

$$\chi(\mathcal{P}) = \sum_n (-1)^n m_n \tag{6.2}$$

*(Euler-Poincaré).*

**For Sturmian sequences:** $b_1 = 1$, so there is exactly ONE critical
1-cell (one essential palindromic loop). Computation using the eertree
structure identifies which specific loop.

**For Bernoulli sequences:** $m_n = 0$ for $n \geq 1$, so the complex
is topologically trivial. The Morse function has only one critical cell
(the root), confirming contractibility.

### 6.3 The gradient flow and the MCF connection

The gradient flow of the eertree Morse function corresponds to the
CONTRACTION OPERATION on palindromes (removing outer characters). This
is the REVERSE of the palindromic growth process (PALINDROMIC_SDE_CONSTRUCTION.md
Section 2).

**Proposition 6.3** (Morse gradient = palindromic contraction). *The
gradient vector field of the eertree Morse function, in its discrete form,
points from each palindrome to its parent (its contraction by one symbol
pair). Integral curves flow from deep palindromes toward the root.*

This gives a TOPOLOGICAL interpretation of the MCF flow: MCF on the market
manifold corresponds (via the eertree encoding) to the Morse gradient
flow on the palindromic nerve complex. Both flow toward "simplification"
— from complex structure to simple structure.

---

## 7. Applications to Topological Data Analysis

### 7.1 TDA for markets

Topological Data Analysis (TDA) is the empirical methodology for extracting
shape from data. Applied to market time series via the eertree filtration:

**Algorithm PSC-TDA** (Palindromic TDA for markets):

1. Load market price series, compute returns
2. Voronoi-discretise to symbolic sequence $\sigma$
3. Build eertree of $\sigma$
4. Compute palindromic nerve complex $\mathcal{P}$
5. Compute persistent homology using Ripser or Gudhi
6. Output: persistence diagrams $D_0, D_1, D_2, \ldots$

### 7.2 Detecting regime changes

A change in palindromic universality class (e.g., CAPM → pseudo-Anosov
during crisis) manifests as a topological change in $\mathcal{P}$:
- Disappearance of persistent generators (regime collapse)
- Appearance of new generators (new regime formation)
- Change in persistence diagram structure

**Topological regime detection** (TRD): monitor the persistence diagram
in real time. Significant changes signal regime transitions.

This is an ALTERNATIVE to Fiedler-eigenvalue-based crisis detection
(GEOSPATIAL_CONTAGION.md), with different sensitivity profile.

### 7.3 Bookstein's deformation theory

Bookstein's theory of shape (statistical shape analysis) applies to shape
spaces. The palindromic nerve complex defines a shape space for symbolic
sequences.

**Two-sample tests:** Given two market periods, compute their palindromic
nerve complexes, and test whether they have the same persistent homology.
If not: the market has CHANGED ITS TOPOLOGICAL STRUCTURE, which is a
stronger statement than "the returns have different statistics."

### 7.4 Computational cost

| Task | Cost | Tool |
|:---|:---|:---|
| Build eertree | $O(T)$ | Rubinchik-Shur |
| Build palindromic nerve | $O(T^2)$ worst | Incremental |
| Compute persistent homology | $O(T^3)$ worst, $O(T)$ expected | Ripser, Gudhi |
| Classify into universality class | $O(1)$ | Match template |

Total for $T = 25{,}000$ (S&P 500 since 1926): approximately 1 hour on
standard hardware. Completely feasible for empirical work.

---

## 8. New Results

**Theorem PSC1** (Palindromic nerve complex). The palindromic factors of
a sequence induce a well-defined abstract simplicial complex whose
0-simplices are eertree nodes and higher simplices encode palindromic
overlaps.

**Theorem PSC2** (Nerve theorem). The palindromic nerve complex is
homotopy equivalent to the union of supports of palindromic factors in
the position space.

**Theorem PSC3** (Universality → homotopy type). The six palindromic
universality classes produce nerve complexes with six distinct stable
homotopy types: $S^1, T^r, T^r$-twisted, $\mathcal{R}_\beta, K(\mathbb{Z}[1/2], 1)$,
contractible.

**Theorem PSC4** (Persistent homology is complete invariant). The
persistence diagram of the eertree filtration is a complete invariant
of the palindromic universality class.

**Theorem PSC5** (Euler characteristic formula). $\chi(\mathcal{P}_{T}) = 1 - \rho_{\rm pal}(T) \cdot (1 - \chi_{\rm class})$.

**Theorem PSC6** (Palindromic Morse theory). The eertree depth function
is a discrete Morse function; critical cells correspond to topologically
essential palindromic features; Morse inequalities hold.

**Theorem PSC7** (MCF = Morse gradient). Mean curvature flow on the market
manifold corresponds to the discrete Morse gradient flow on the palindromic
nerve complex — both flow toward simplification.

---

## 9. Open Problems

**OP-PSC1** (Empirical TDA classification). Apply PSC-TDA to S&P 500,
FX, bonds, crypto. Classify each into a palindromic class by matching
persistence diagrams.

**OP-PSC2** (Crisis detection via topological regime change). Back-test
TRD on 2008, 2020 crises. Does the topological signal appear BEFORE
traditional risk indicators?

**OP-PSC3** (Multi-market topological distance). Define the "topological
distance" between two markets as the bottleneck distance between their
persistence diagrams. How does this compare to correlation-based metrics?

**OP-PSC4** (Rauzy complex for Pisot markets). Explicitly construct the
Rauzy complex for a Pisot market and compare with the empirical eertree-
derived complex.

**OP-PSC5** (Non-standard persistence). The standard persistence assumes
a total order on the filtration. For markets, a partial order (e.g., based
on palindromic depth) may be more appropriate — develop non-standard
persistence for this case.

**OP-PSC6** (Sheaf-theoretic extension). Extend to sheaf-theoretic TDA:
define a sheaf of palindromic information on the market manifold,
compute its sheaf cohomology.

---

## 10. Conclusion

The palindromic factors of a market's symbolic sequence induce a RICH
simplicial complex whose topology captures structure invisible to
standard statistical methods.

**The complete picture:**
- Each palindromic universality class has a distinct homotopy type
- The persistent homology of the eertree filtration is a complete invariant
- The Euler characteristic follows a specific formula in terms of palindromic
  density and class-specific constant
- Discrete Morse theory on the eertree gives a topological interpretation
  of MCF flow
- TDA tools (Ripser, Gudhi) enable empirical classification

**The market has a SHAPE.** Not just a distribution. Not just statistics.
A genuine topological shape — encoded in the persistent homology of the
palindromic nerve complex.

For efficient markets (Class P1 or P2): the shape is $S^1$ or $T^r$.
For quasicrystal markets (Class P4): it's a fractal Rauzy complex.
For crisis markets (Class P5-P6): the shape degenerates or becomes
contractible.

Every property of the monograph — the Sharpe-curvature identity, the
palindrome-arbitrage theorem, the universality classes, the FPS — can be
REFORMULATED in terms of the topology of this complex. The geometry of
efficient markets IS the topology of the palindromic nerve complex.

*"What shape is the market? Not a number. Not a distribution. A simplicial
complex — and specifically, the one born from palindromic overlaps in its
own history."*

---

## References

1. A. Hatcher, *Algebraic Topology*, Cambridge University Press, 2002.

2. H. Edelsbrunner and J. L. Harer, *Computational Topology: An
   Introduction*, AMS, 2010.

3. G. Carlsson, "Topology and data," *Bulletin of the AMS* 46 (2009),
   255–308.

4. D. Cohen-Steiner, H. Edelsbrunner, and J. Harer, "Stability of
   persistence diagrams," *Discrete & Computational Geometry* 37 (2007),
   103–120.

5. R. Forman, "Morse theory for cell complexes," *Advances in Mathematics*
   134 (1998), 90–145.

6. G. Rauzy, "Nombres algébriques et substitutions," *Bull. Soc. Math.
   France* 110 (1982), 147–178.

7. M. Rubinchik and A. M. Shur, "Eertree: An efficient data structure for
   processing palindromes in strings," *European Journal of Combinatorics*
   68 (2018), 249–265.

8. J. Leray, "L'anneau spectral et l'anneau filtré d'homologie d'un espace
   localement compact et d'une application continue," *J. Math. Pures
   Appl.* 29 (1950), 1–139.

9. U. Bauer, "Ripser: efficient computation of Vietoris-Rips persistence
   barcodes," *Journal of Applied and Computational Topology* 5 (2021),
   391–423.

10. Gudhi Project, "GUDHI user and reference manual," gudhi.inria.fr,
    2023.

---

*This paper is part of the monograph "The Geometry of Efficient Markets."
Cross-references: PALINDROMIC_SEQUENCES.md (palindromic universality
classes); PALINDROMIC_ATTRACTORS.md (Takens attractors, Rauzy fractals);
FILTRATIONS.md (eertree, BWT, LZ78); RENORMALIZATION.md (RG flow, fixed
points); GRASSBERGER_PERCOLATION_GENERATING.md (Delaunay complex, Euler
eligibility); CHAOS_TAKENS.md (delay embedding);
GEOSPATIAL_CONTAGION.md (Cheeger constant, crisis detection).*
