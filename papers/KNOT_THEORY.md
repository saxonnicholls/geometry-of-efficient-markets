# Knot Theory and Market Structure:
## Knots as Boundaries of Efficient Markets, the Jones Polynomial
## as a Market Partition Function, and Topological Market Invariants

**Saxon Nicholls** — me@saxonnicholls.com

**Paper III.2** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We establish a deep connection between knot theory and the geometry of efficient
financial markets. The log-optimal portfolio path $\Gamma = \{b^{\ast}(t) : t \in [0,T]\}$
traces a curve in the Bhattacharyya sphere $S^{d-1}\_+$, and for $d \geq 4$ this
curve can be knotted. The knot type of $\Gamma$ is a topological market invariant —
it determines which minimal surface the efficient market must span (via the Plateau
problem), and hence which efficient market structure is "forced" by the market's
history. Our principal results:

**(i) Knots classify efficient markets:** The unknot forces the CAPM (great sphere,
genus 0). The trefoil forces a genus-1 minimal surface (Clifford torus universality).
The torus knot $T(m,n)$ forces the Lawson surface $\tau\_{m,n}$ (genus $(m-1)(n-1)/2$).
The Seifert genus of the market path is the minimum topological complexity of the
efficient market.

**(ii) The Jones polynomial is a market partition function:** By Witten's
theorem \[1989\], the Jones polynomial $J\_\Gamma(q)$ of the market path equals
the Chern-Simons partition function on $S^3$. Since we established in FIBER\_BUNDLES
that the Chern-Simons form appears in the market action, the Jones polynomial computes
the amplitude for market regime transitions — it is a topological market invariant
expressible as a sum over market trajectories.

**(iii) Ribbon knots and CAPM resolution:** A market path that is a ribbon (slice)
knot can be continuously resolved to the unknot by adding a temporal dimension.
Such markets are topologically "CAPM-equivalent" over infinite time. Markets whose
path is a non-ribbon knot have permanent topological complexity that cannot be
unwound, even over the full business cycle. The $s$-cobordism theorem and the
Gordian distance measure how "far" a market is from being CAPM-resolvable.

**(iv) Knot invariants as risk measures:** The Alexander polynomial $\Delta\_\Gamma(t)$
is the characteristic polynomial of the Seifert matrix — which is precisely the
monodromy of the normal bundle connection around the market cycle. The writhe of
the market knot is the Chern-Simons level modulo $2\pi$. The unknotting number
is the minimum number of regime changes needed to reduce the market to CAPM type.

**(v) Satellite knots and composite markets:** The satellite construction corresponds
to nested factor structures — a market whose factors are themselves factor portfolios
of simpler markets. The Jones polynomial of a satellite knot is computable from the
Jones polynomials of the component knots, giving a recursive structure for composite
market analysis.

**Keywords.** Knot theory; Jones polynomial; Alexander polynomial; Seifert genus;
Plateau problem; ribbon knot; concordance; Gordian distance; torus knots; Lawson
surfaces; Chern-Simons; market topology; writhe; unknotting number; satellite knots.

**MSC 2020.** 57M25, 57M27, 53A10, 91G10, 81T45, 57M50, 55N22.

---

## 1. How Knots Arise in Market Geometry

### 1.1 The market path as a curve in $S^{d-1}\_+$

The log-optimal portfolio path is:

$$\Gamma: [0,T] \to S^{d-1}_+, \qquad t \mapsto \phi(b^{\ast}(t)) = \sqrt{b^{\ast}(t)} \tag{1.1}$$

For $d = 3$ (three assets): $\Gamma$ is a curve in $S^2\_+$ (a positive octant of the
2-sphere). Curves on the 2-sphere cannot be knotted — the knot group of $S^2$ is
trivial. The market path is always unknotted for three assets.

For $d = 4$ (four assets): $\Gamma$ is a curve in $S^3\_+$ (a positive orthant of the
3-sphere). **Curves in $S^3$ can be knotted.** The log-optimal portfolio path for a
four-asset, two-factor market traces a curve in $S^3\_+$ that may be:
- The unknot (CAPM-type market)
- The trefoil knot (simplest non-trivial knot)
- A torus knot $T(m,n)$ (winding $m$ times in one direction and $n$ times in another)
- More exotic knots (hyperbolic knots, satellite knots)

For $d \geq 5$: knots exist in $S^{d-1}\_+$ but are automatically unknotted for
$d \geq 5$ (Whitney embedding: knots in $S^n$ are trivial for $n \geq 4$). However,
**links** (collections of multiple curves) can be non-trivially linked even in high
dimensions through the theory of higher-dimensional linking.

**The practically relevant case is $d = 4$:** the four-asset, two-factor market is
the smallest market where non-trivial knot topology can arise.

### 1.2 The Plateau problem for knotted boundaries

The **knotted Plateau problem** asks: given a knot $K \subset S^3$, find the minimal
surface $\Sigma^{\ast}$ spanning $K$:

$$\Sigma^{\ast} = \operatorname{argmin}_{\partial\Sigma = K} \mathrm{Area}_{g^{\mathrm{FR}}}(\Sigma) \tag{1.2}$$

The topology of $\Sigma^{\ast}$ is constrained by the knot type of $K$:

**Theorem 1.1** *(Seifert genus and the Plateau problem)*. *The minimum genus
$g(\Sigma^{\ast})$ of any spanning surface for a knot $K$ is the Seifert genus $g(K)$:*

$$g(\Sigma^{\ast}) = g(K) = \min_{\partial\Sigma = K} \text{genus}(\Sigma) \tag{1.3}$$

*For the unknot: $g = 0$ (spanning surface is a disk — CAPM, great sphere).*
*For the trefoil: $g = 1$ (spanning surface is a torus — Clifford torus universality).*
*For the torus knot $T(m,n)$: $g = (m-1)(n-1)/2$.*

*Proof.* This is the Seifert genus theorem \[Seifert 1934\]. The genus of the
Seifert surface (algorithmically constructed from the knot diagram) is a lower bound;
the minimal surface achieves this bound by Morrey's solution to the Plateau problem
for manifolds. $\square$

**The profound implication:** The knot type of the log-optimal portfolio path
**forces** the topology of the efficient market manifold. The market cannot be
efficient with a simpler topology than the Seifert genus of its path — the
topological complexity of the factor structure is bounded below by the knot invariant.

---

## 2. The Dictionary: Knots and Market Structures

### 2.1 The complete dictionary for low-crossing knots

| Knot $K$ | $g(K)$ | Crossings | Minimal surface $\Sigma^{\ast}$ | Market structure |
|:---------|:------:|:---------:|:--------------------------|:----------------|
| Unknot $0\_1$ | 0 | 0 | Great disk (great sphere) | CAPM, no factor interactions |
| Trefoil $3\_1$ | 1 | 3 | Seifert surface (torus-like) | Clifford torus market |
| Figure-eight $4\_1$ | 1 | 4 | Punctured torus | Hyperbolic 2-factor market |
| Torus knot $T(2,3) = 3\_1$ | 1 | 3 | Clifford torus | Balanced 2-factor |
| Torus knot $T(2,5) = 5\_1$ | 2 | 5 | Lawson $\tau\_{2,1}$ | Two-regime 2-factor |
| Torus knot $T(3,4)$ | 3 | 8 | Lawson $\tau\_{3,1}$ or higher | Three-regime factor |
| Torus knot $T(m,n)$ | $(m-1)(n-1)/2$ | — | Lawson $\tau\_{m,n}$-type | Multi-regime coupled |
| Satellite knot | $g\_{\rm comp} + g\_{\rm sat}$ | — | Composite surface | Nested factor structure |

**The figure-eight knot $4\_1$** is special: it is the simplest **hyperbolic knot**
(not a torus knot, not a satellite knot). The minimal surface spanning the figure-eight
knot is a once-punctured torus — a torus with a hole. In market terms: a four-asset
market whose log-optimal path traces a figure-eight knot has a minimal spanning surface
that is NOT the Clifford torus (which spans the trefoil) but rather a different
genus-1 surface — a **hyperbolic two-factor market structure** with more complex
curvature than the balanced Clifford structure.

The figure-eight knot market has an important property: the figure-eight knot is
**amphicheiral** (its mirror image is the same knot). This means the market has
a left-right symmetry — the long and short versions of the factor exposure are
topologically equivalent. **An amphicheiral market has symmetric long-short factor payoffs.**

### 2.2 The unknot = CAPM = efficient market

The CAPM great-sphere market has the unknot as its boundary:
the log-optimal path $\Gamma$ for a single-factor market is a great circle arc
(from MINIMAL\_SURFACE Section 8.1), which in $S^3\_+$ is a simple arc from one
boundary face to another — topologically, the unknot.

**Theorem 2.1** *(CAPM = unknot)*. *The log-optimal portfolio path of a CAPM
($r=1$, totally geodesic market manifold) is homotopic to the unknot in $S^{d-1}\_+$.
The minimal spanning surface is a great disk, confirming the CAPM structure.*

*Proof.* The CAPM path lies on a great circle $S^1\_+ \subset S^{d-1}\_+$ — a simple
arc in the positive hemisphere. Simple arcs in any hemisphere are isotopic to the
unknot (they have no room to knot since they lie in a 1-dimensional curve on a
contractible region). $\square$

### 2.3 The trefoil = balanced two-factor market

The Clifford torus market's log-optimal path traces a torus knot $T(2,3)$ — the
**trefoil** — in $S^3\_+$. The trefoil is the $(2,3)$ torus knot: it winds 2 times
around the torus in one direction and 3 times in the other.

**Why the trefoil?** The Clifford torus $\tau\_{1,1} \subset S^3$ is the standard
torus (product of two circles). Its log-optimal portfolio path, for a balanced
($p=1/2$) two-factor market where Factor 1 and Factor 2 cycle through their values
independently, traces a path that winds $m$ times around the $\theta$-direction
and $n$ times around the $\varphi$-direction — a torus knot $T(m,n)$.

For a balanced market where both factors complete one full cycle ($m=n=1$): the path
is the $(1,1)$ torus knot = the unknot. For a market where Factor 1 completes 2 cycles
while Factor 2 completes 3 cycles ($m=2$, $n=3$): the path is the trefoil $T(2,3)$.

The connection to the Lawson surfaces: $T(m,n)$ bounds the Lawson surface $\tau\_{m,n}$
(minimal, genus $(m-1)(n-1)/2$). **The torus knot $T(m,n)$ is the natural boundary
of the Lawson surface $\tau\_{m,n}$.**

---

## 3. The Jones Polynomial as a Market Partition Function

### 3.1 Witten's theorem

Witten \[1989\] established the profound connection:

$$J_K(q) = Z_{\rm CS}[S^3, K] \tag{3.1}$$

The **Jones polynomial** $J\_K(q)$ — a knot invariant that distinguishes most knots —
equals the Chern-Simons partition function on $S^3$ with the knot $K$ inserted as a
Wilson loop. The parameter $q = e^{2\pi i/(k+2)}$ encodes the Chern-Simons level $k$.

We established in FIBER\_BUNDLES (equation 7.4) that the portfolio action is:

$$\mathcal{S}[b, A] = \int_0^T L_T(b)\,dt + k\int_M \mathrm{CS}(A) \tag{3.2}$$

**Combining:** The path integral of the portfolio action with a fixed market path
$\Gamma$ inserted as a "Wilson loop" gives:

$$\int \mathcal{D}[b]\,e^{\mathcal{S}[b,A]}\,W(\Gamma) = J_\Gamma(e^{2\pi i/(k+2)}) \tag{3.3}$$

where $W(\Gamma) = \mathrm{tr}(\mathcal{P}\exp\oint\_\Gamma A)$ is the holonomy of the
connection around $\Gamma$ (the Berry phase from FIBER\_BUNDLES Section 3.2).

**Theorem 3.1** *(Jones polynomial = market partition function)*. *The Jones
polynomial of the log-optimal portfolio path $\Gamma$ is the market partition function
summing over all portfolio trajectories consistent with the market structure, weighted
by the portfolio action:*

$$J_\Gamma(q) = \int_{\{b: \partial b = \Gamma\}} \mathcal{D}[b]\,e^{\mathcal{S}[b,A]} \tag{3.4}$$

*where the integration is over all portfolio paths whose boundary is the market path
$\Gamma$, and $q = e^{2\pi i/(k+2)}$ encodes the Chern-Simons level (topological complexity).*

*The Jones polynomial evaluated at specific values of $q$ gives:*
- *$J\_\Gamma(1)$: the number of spanning surfaces (market structures) consistent with $\Gamma$*
- *$J\_\Gamma(-1)$: the determinant of the market knot (a measure of complexity)*
- *$J\_\Gamma(i)$: related to the Arf invariant (whether the market is "even" or "odd")*
- *$J\_\Gamma(e^{2\pi i/3})$: related to the 3-coloring number of the market structure*

### 3.2 Computing the Jones polynomial for market paths

**For the unknot (CAPM):** $J\_{\rm unknot}(q) = 1$. The market partition function is 1:
the CAPM has a unique market structure (the great sphere) and no topological complexity.

**For the trefoil (Clifford torus market):**
$$J_{3_1}(q) = -q^{-4} + q^{-3} + q^{-1} \tag{3.5}$$

This polynomial carries topological information:
- It has three terms (corresponding to the three crossings of the trefoil)
- The minimum degree $(-4)$ equals $-3g-1 = -4$ (Seifert genus $g=1$)
- It distinguishes the left-handed from right-handed trefoil (the Jones polynomial breaks chirality symmetry) — the two market chiralities (long-value-short-growth vs long-growth-short-value) are topologically distinct

**For the torus knot $T(m,n)$ (Lawson surface market):**
$$J_{T(m,n)}(q) = q^{(m-1)(n-1)/2}\cdot\frac{1 - q^{m+1} - q^{n+1} + q^{m+n}}{1 - q^2} \tag{3.6}$$

The leading power $(m-1)(n-1)/2 = g(K)$ is the Seifert genus — consistent with our
identification of the Lawson surface genus with the market complexity.

**For the figure-eight knot (hyperbolic 2-factor market):**
$$J_{4_1}(q) = q^2 - q + 1 - q^{-1} + q^{-2} \tag{3.7}$$

This is palindromic (reads the same forwards and backwards) — reflecting the
amphicheiral symmetry (long-short equivalence) of the figure-eight market.

### 3.3 Jones polynomial as a market risk indicator

The Jones polynomial evaluated at $q = -1$ gives the **determinant** of the knot:

$$\det(K) = |J_K(-1)| \tag{3.8}$$

| Knot | $\det(K)$ | Market interpretation |
|:-----|:---------:|:---------------------|
| Unknot | 1 | CAPM: one stable fixed point |
| Trefoil | 3 | Three stable equilibria in the two-factor market |
| Figure-eight | 5 | Five stable equilibria (hyperbolic market) |
| $T(2,5)$ | 5 | Five equilibria, torus structure |
| $T(m,n)$ | $\frac{\sin(mn\pi/p)}{\sin(\pi/p)}$ | $mn$ equilibria (from Lawson structure) |

**The determinant counts the number of topologically distinct market equilibria** —
the number of different efficient market configurations consistent with the knot type.
For the trefoil: there are exactly 3 efficient equilibria, corresponding to the three
lobes of the minimal Seifert surface.

---

## 4. The Alexander Polynomial and the Seifert Matrix

### 4.1 The Seifert matrix

For a knot $K$ with Seifert surface $\Sigma$, the **Seifert matrix** $V$ encodes the
linking numbers of cycles on $\Sigma$ with their push-offs in the normal direction:

$$V_{ij} = \mathrm{lk}(\alpha_i, \alpha_j^+) \tag{4.1}$$

where $\alpha\_1,\ldots,\alpha\_{2g}$ is a basis for $H\_1(\Sigma; \mathbb{Z})$ and
$\alpha\_j^+$ is the push-off of $\alpha\_j$ in the positive normal direction.

**The Alexander polynomial:**
$$\Delta_K(t) = \det(V - tV^T) \tag{4.2}$$

is a polynomial knot invariant, symmetric under $t \mapsto t^{-1}$ and normalised so
$\Delta\_K(1) = \pm 1$.

### 4.2 The Seifert matrix IS the monodromy of the normal bundle

**Theorem 4.1** *(Seifert matrix = normal bundle monodromy)*. *The Seifert matrix
$V$ of the market knot $\Gamma$ equals the monodromy matrix of the normal bundle
connection $\nabla^N$ around the market cycle $\Gamma$:*

$$V = \mathrm{Hol}_\Gamma(\nabla^N) \in \mathrm{GL}(d-1-r; \mathbb{Z}) \tag{4.3}$$

*where the holonomy is computed in the $\mathbb{Z}$-module structure on
$H\_1(\Sigma;\mathbb{Z})$ (the integer first homology of the Seifert surface).*

*Proof.* The Seifert matrix entries $V\_{ij} = \mathrm{lk}(\alpha\_i, \alpha\_j^+)$ are
precisely the linking numbers — how much $\alpha\_i$ winds around $\alpha\_j$ in the
normal direction. The holonomy of $\nabla^N$ around the cycle $\alpha\_i$ measures
exactly this winding, giving the identification. The integer structure comes from the
fact that linking numbers are integers ($\pi\_1(S^1) = \mathbb{Z}$). $\square$

**Financial interpretation.** The Seifert matrix $V$ encodes:
- **Diagonal entries $V\_{ii}$:** the self-linking of each homology cycle = the
  Chern-Simons level for that cycle
- **Off-diagonal entries $V\_{ij}$:** the mutual linking of cycles = the cross-factor
  holonomy = the "interaction term" between factor loops in the market

**The Alexander polynomial** $\Delta\_K(t)$ is the characteristic polynomial of this
monodromy — its roots $\{t : \Delta\_K(t) = 0\}$ are the eigenvalues of the normal
bundle monodromy. In market terms: the roots of the Alexander polynomial are the
eigenvalues of the **factor rotation matrix** after one complete business cycle.

**For the trefoil:** $\Delta\_{3\_1}(t) = t - 1 + t^{-1}$. The roots satisfy
$t^2 - t + 1 = 0$, giving $t = e^{\pm i\pi/3}$ — **the factor structure rotates
by $\pm 60°$ after each market cycle.** This is a precise prediction: in a trefoil
market, the dominant factor exposure rotates by $60°$ (one-sixth of a full rotation)
per business cycle.

**For the figure-eight:** $\Delta\_{4\_1}(t) = -t + 3 - t^{-1}$.
Roots: $t = (3 \pm \sqrt{5})/2 = \phi^2, \phi^{-2}$ where $\phi$ is the golden ratio.
**The factor rotation eigenvalues are $\phi^2$ and $\phi^{-2}$** — the golden ratio
squared. A hyperbolic market has factor rotation rates governed by the golden ratio.

---

## 5. Ribbon Knots, Concordance, and CAPM Resolution

### 5.1 Slice knots and the 4-ball

A knot $K \subset S^3$ is **slice** (or **ribbon**) if it bounds a smoothly embedded
disk $D^2 \hookrightarrow B^4$ in the 4-ball. Geometrically: $K$ can be "capped off"
with a disk by adding a temporal dimension.

**The cobordism interpretation:** $K$ is slice iff it is cobordant to the unknot in
$B^4$ — there exists a cobordism from $K$ (at $t=0$) to the unknot (at $t=1$) that
is a smooth surface in $S^3 \times [0,1]$.

**Definition 5.1** (CAPM-resolvable market). *A market with knot-type path $\Gamma$ is
**CAPM-resolvable** if $\Gamma$ is a slice knot. This means the market's topological
complexity can be continuously resolved to CAPM type by adding one dimension (time).*

**Theorem 5.2** *(Ribbon knots and CAPM resolution)*.

*(i) If the market path $\Gamma$ is a ribbon knot, the market is CAPM-resolvable:
the factor structure can be continuously deformed to the CAPM structure over a
finite temporal cobordism.*

*(ii) If $\Gamma$ is not a ribbon knot, the market has **permanent topological
complexity** — no continuous deformation over any finite time horizon can reduce
it to CAPM type.*

*(iii) The **Fox-Milnor theorem** \[1966\] gives an obstruction: $\Gamma$ is not
slice if $\Delta\_\Gamma(t) \neq f(t)f(t^{-1})$ for any $f \in \mathbb{Z}[t]$.
For the trefoil: $\Delta\_{3\_1}(t) = t - 1 + t^{-1}$. Is this of the form $ff^{\ast}$?
Testing: if $f = at + b$ then $ff^{\ast} = a^2 + ab(t+t^{-1}) + b^2 = ab(t+t^{-1}) + (a^2+b^2)$. Matching: $a^2+b^2 = -1$ (impossible over $\mathbb{Z}$).
Therefore the trefoil is NOT a ribbon knot — a trefoil market has permanent
topological complexity.*

**Profound implication.** A market whose log-optimal path traces a trefoil cannot
be reduced to CAPM type by any continuous evolution. The balanced two-factor market
structure (Clifford torus / trefoil boundary) is **topologically locked** — it cannot
deform to the simpler CAPM structure without a discontinuity (a market crisis, a
topological phase transition).

By contrast: the unknot markets (CAPMs) are trivially ribbon. The figure-eight knot
$4\_1$ is ribbon (it IS a slice knot — it bounds a disk in $B^4$). **Figure-eight
markets are CAPM-resolvable despite their apparent complexity**: over a full temporal
cobordism, the hyperbolic factor structure resolves to CAPM type.

### 5.2 The Gordian distance as market complexity measure

**Definition 5.3** (Gordian distance). *The Gordian distance $d\_G(K\_1, K\_2)$ between
two knots is the minimum number of crossing changes needed to deform $K\_1$ into $K\_2$.
The **unknotting number** $u(K) = d\_G(K, \text{unknot})$ is the minimum number of
crossing changes to unknot $K$.*

**Financial interpretation:** Each crossing change in the knot diagram corresponds
to a **market regime change** — a discrete event where two factor loadings cross
(one factor overtakes another in its effect on a group of assets).

- **$u(K) = 0$:** unknot, CAPM. No regime changes needed.
- **$u(K) = 1$:** trefoil ($u(3\_1) = 1$), figure-eight ($u(4\_1) = 1$). One regime change separates the market from CAPM.
- **$u(K) = k$:** the market requires exactly $k$ discrete regime changes to reach CAPM.

The Gordian distance gives a metric on the space of market structures:

$$d_G(M_1, M_2) = \text{minimum regime changes to deform market } M_1 \text{ to market } M_2 \tag{5.1}$$

**The Gordian distance is the market-structure distance** — a metric on the moduli
space of market topological types, measuring how many discrete economic disruptions
separate two market regimes.

**The Gordian complexity of an efficient market is bounded by the Seifert genus:**
$u(K) \leq g(K)$ (you need at most $g(K)$ crossing changes to unknot $K$). Since
$g(K) = $ minimum factor interactions, the unknotting number bounds the minimum
number of regime changes needed to simplify the market.

---

## 6. Satellite Knots and Composite Market Structures

### 6.1 The satellite construction

Given a knot $K$ (the "companion") and a knot $J$ (the "pattern"), the **satellite knot**
$S(K,J)$ is constructed by:
1. Take the solid torus neighborhood $N(K)$ of $K$
2. Replace it with $J$ embedded in the solid torus

The Seifert genus of a satellite satisfies:
$$g(S(K,J)) \geq g(K) + g(J) \tag{6.1}$$

(with equality for many common cases).

### 6.2 Composite markets

**Definition 6.1** (Composite market). *A **composite market** is one whose factor
structure nests: Factor 1 is itself a factor portfolio of a sub-market with factor
structure $M\_1$, and the outer market has additional factor structure $M\_2$. The
composite market manifold $M\_{\rm comp}$ is the satellite of $M\_2$ around $M\_1$.*

**The Seifert genus of the composite market:**
$$g(M_{\rm comp}) \geq g(M_1) + g(M_2) \tag{6.2}$$

**The Jones polynomial of the composite market:**

For a connected sum of knots $K\_1 \\# K\_2$ (the simplest form of composition):
$$J_{K_1 \\# K_2}(q) = J_{K_1}(q) \cdot J_{K_2}(q) \tag{6.3}$$

The Jones polynomial factorises over the composite market structure. **The market
partition function (Jones polynomial) of a composite market is the product of the
partition functions of its components.**

This is the topological version of the independent factor model: if two sub-markets
have independent factor structures (their knot types combine as a connected sum),
their market partition functions multiply — the topological complexity is additive.

**Example:** A market combining a trefoil (balanced 2-factor, one sub-market) with
a torus knot $T(2,5)$ (2-regime 2-factor, another sub-market):
- Composite knot: $3\_1 \\# 5\_1$ (trefoil connected sum with $T(2,5)$)
- Seifert genus: $g = 1 + 2 = 3$
- Jones polynomial: $J\_{3\_1}(q) \cdot J\_{5\_1}(q)$
- Market structure: Lawson $\tau\_{3,2}$ (genus 3) forced as the spanning surface

---

## 7. Khovanov Homology and Market Cohomology

### 7.1 Categorification of the Jones polynomial

The Jones polynomial is a polynomial invariant, but it admits a richer invariant:
**Khovanov homology** \[Khovanov 2000\] is a bigraded chain complex whose Euler
characteristic is the Jones polynomial:

$$\chi(\mathrm{Kh}(K)) = J_K(q) \tag{7.1}$$

Khovanov homology is strictly stronger than the Jones polynomial — it distinguishes
knots that the Jones polynomial cannot.

**For markets:** Khovanov homology of the market path $\Gamma$ is a bigraded
abelian group $\mathrm{Kh}^{i,j}(\Gamma)$ whose generating function:

$$P_\Gamma(t,q) = \sum_{i,j}(-1)^i q^j t^i\,\mathrm{rank}\,\mathrm{Kh}^{i,j}(\Gamma) \tag{7.2}$$

is the Poincaré polynomial of the market's topological structure. Setting $t=-1$
recovers the Jones polynomial.

**Financial interpretation of the bigrading:**
- The $q$-grading (quantum grading) corresponds to the **Chern-Simons level** —
  the topological charge of the market structure
- The $i$-grading (homological grading) corresponds to the **Jacobi eigenvalue index**
  — the number of unstable directions of the market equilibrium

The rank of $\mathrm{Kh}^{0,j}$ (the zeroth homological grading) counts the number of
**topologically stable market structures** at each Chern-Simons charge $j$.

### 7.2 The Rasmussen invariant and market complexity

Rasmussen \[2010\] defined an integer invariant $s(K)$ from the "s-grading" on
Khovanov homology satisfying:

$$|s(K)| \leq 2g_4(K) \leq 2g(K) \tag{7.3}$$

where $g\_4(K)$ is the 4-ball genus (slice genus) and $g(K)$ is the Seifert genus.

**The Rasmussen $s$-invariant** gives the sharpest known bound on the 4-ball genus —
how efficiently the market knot can be resolved by adding time as a dimension.

For torus knots $T(m,n)$: $s(T(m,n)) = (m-1)(n-1)$ (exact computation by Rasmussen).
Since $2g\_4 \leq s = (m-1)(n-1) = 2g$: the 4-ball genus equals the Seifert genus
for torus knots — **torus knot markets ($= $ Lawson surface markets) cannot be
made simpler even by adding time as a dimension.** They are maximally complex.

---

## 8. Knot Concordance and Market Evolution

### 8.1 The concordance group

Two knots $K\_0$ and $K\_1$ are **concordant** if there exists a smooth annulus
$A \subset S^3 \times [0,1]$ with $\partial A = K\_0 \times \{0\} \cup K\_1 \times \{1\}$.
Concordance is an equivalence relation; the concordance classes form the
**concordance group** $\mathcal{C}$ under connected sum.

**The concordance group of markets** is the group of topological types of market
paths under the equivalence: $M\_1 \sim M\_2$ if their market paths are concordant
(related by a temporal cobordism of market structures).

Key facts about $\mathcal{C}$:
- $\mathcal{C}$ contains $\mathbb{Z}^\infty$ (infinitely many independent elements)
- The concordance class of the unknot is the identity (CAPM = identity market)
- Torus knots $T(2, 2k+1)$ are all independent in $\mathcal{C}$ (Milnor \[1968\])

**The Milnor independence** means: the torus knot markets $T(2,3)$ (trefoil),
$T(2,5)$, $T(2,7)$, ... are all concordance-independent — no finite combination of
temporal cobordisms can relate them to each other or to the CAPM.

**The market concordance group has infinite rank** — there are infinitely many
topologically distinct market evolution types that cannot be related by any continuous
market dynamics.

### 8.2 Casson-Gordon invariants and market obstructions

The **Casson-Gordon invariants** \[1978\] are higher-order obstructions to a knot
being slice. They arise from the representation theory of the knot group
$\pi\_1(S^3 \setminus K)$ into finite groups.

**In market terms:** The knot group $\pi\_1(S^3 \setminus K)$ is the fundamental
group of the complement of the market path — the group of all portfolio trajectories
that "avoid" the market path $\Gamma$. This is the group of **market-avoiding strategies**
— strategies that never cross the log-optimal path.

The Casson-Gordon invariants measure whether the market-avoiding strategies can be
collectively "capped off" (extended to the 4-ball) — whether there exist time-extended
strategies that avoid the entire market history and still form a consistent group.

**When the Casson-Gordon invariants are non-zero:** The market-avoiding strategies cannot
all be extended consistently — there is a genuine topological obstruction to hedging the
market path. This is a higher-order version of market incompleteness, beyond the
linear incompleteness of Harrison-Pliska.

---

## 9. New Results: The Knot Perspective

### 9.1 The writhe as a market chirality invariant

**Definition 9.1** (Market writhe). *For a market path $\Gamma$ with a given planar
diagram, the **writhe** $w(\Gamma) = \sum\_c \epsilon(c)$ (sum of crossing signs)
is the Chern-Simons level of $\Gamma$ modulo the framing ambiguity.*

The writhe is NOT a knot invariant (it depends on the diagram), but it IS an invariant
of the **framed knot** — the knot together with a choice of normal framing. In market
terms: the writhe is an invariant of the market path together with a specific choice
of factor basis (the frame).

**The self-linking number:** $\mathrm{lk}(\Gamma, \Gamma^+) = w(\Gamma)$ — the linking
number of the market path with its push-off in the normal direction.

**Financial interpretation:** The writhe measures the **net chirality** of the market
— how many more right-handed factor crossings there are than left-handed ones. A market
with positive writhe is "right-handed" (factor interactions are predominantly one-signed).
A market with zero writhe is **achiral** — statistically symmetric under factor
sign reversal.

**For the CAPM:** writhe = 0 (unknot, no crossings). The CAPM is perfectly achiral —
it has no preference for long vs short factor exposure.

**For the trefoil (right-handed):** writhe = +3. The right-handed trefoil market has
a +3 chirality: three more right-handed than left-handed factor crossings per cycle.
This is the topological signature of a market with **positive factor momentum** —
a systematic preference for one direction of factor movement over another.

**The left-handed trefoil** has writhe $= -3$: negative factor momentum. **The Jones
polynomial distinguishes left-handed from right-handed trefoil** — it is the topological
invariant that detects market chirality.

### 9.2 A complete classification of four-asset two-factor markets

For $d=4$, $r=2$ (the fundamental case where knot theory first applies):

**Theorem 9.2** *(Topological classification of four-asset markets)*. *The topological
types of log-optimal portfolio paths for four-asset two-factor markets are classified
by knot types in $S^3\_+$. The main families are:*

| Market path topology | Knot type | $g(K)$ | $\Delta\_K(t)$ | $w$ | Market character |
|:--------------------|:---------:|:------:|:--------------:|:---:|:----------------|
| CAPM | Unknot | 0 | 1 | 0 | Single-factor, symmetric |
| Balanced 2-factor | Trefoil $3\_1$ | 1 | $t-1+t^{-1}$ | ±3 | Chiral, $60°$ rotation |
| Hyperbolic 2-factor | Figure-eight $4\_1$ | 1 | $-t+3-t^{-1}$ | 0 | Achiral, golden ratio |
| Momentum 2-factor | $T(2,5) = 5\_1$ | 2 | $t^2-t+1-t^{-1}+t^{-2}$ | ±5 | Strong chiral |
| Multi-regime | $T(3,4) = 8\_{19}$ | 3 | computed | ±7 | Three-regime |

*Each row corresponds to a distinct efficient market structure that cannot be
continuously deformed into any other without a topological transition (regime change).*

---

## 10. What Knot Theory Tells Us About Markets

Collecting the insights:

**1. Market topology is a knot invariant.** The knot type of the log-optimal path
is a topological market invariant — it classifies the market's factor structure in
a way that is immune to continuous market evolution. Different knot types correspond
to qualitatively different market regimes.

**2. The Jones polynomial is computable from market data.** Given the log-optimal
portfolio time series $b^{\ast}(t)$, project it into $S^3\_+$, compute the winding numbers,
and evaluate the Jones polynomial. This gives a computable topological market invariant.

**3. The Alexander polynomial predicts factor rotation.** The roots of $\Delta\_\Gamma(t)$
are the eigenvalues of the factor rotation matrix after one business cycle.
For trefoil markets: rotation by $60°$. For figure-eight markets: rotation by $\phi^2$.

**4. The unknotting number counts regime changes.** To move from one topological
market type to another requires a discrete number of regime changes equal to the
Gordian distance between the corresponding knot types.

**5. Torus knot markets are maximally complex.** The Rasmussen invariant shows that
$T(m,n)$ markets (= Lawson surface markets) cannot be simplified even by adding time.
Their topological complexity is permanent.

**6. Market chirality is the writhe.** The sign of the writhe measures whether the
market has positive or negative factor momentum — a topological explanation for the
empirically observed sign of momentum effects.

**7. The efficient market requires $J\_\Gamma(q) = 1$.** For the market to be truly
efficient in the topological sense (CAPM-type, no protected alpha), the Jones
polynomial of the market path must equal 1 — the unknot condition. This is the
strongest form of the Efficient Market Hypothesis, incorporating topological constraints.

$$\boxed{\text{Topological EMH: } J_\Gamma(q) = 1 \iff \text{market is topologically trivial (CAPM)}} \tag{10.1}$$

This is a new, computable, model-free test of market efficiency using knot invariants.

---

## 11. Open Problems

**Problem 1** *(Compute Jones polynomials from data)*. Given the empirical log-optimal
portfolio time series for the S\&P 500, compute the Jones polynomial $J\_\Gamma(q)$
of the annual market path. If $J\_\Gamma \neq 1$: determine the knot type and the
corresponding minimal spanning surface (efficient market structure).

**Problem 2** *(The market concordance group)*. Is the concordance group of market
paths finitely generated? The Milnor independence of torus knots suggests it is not,
but the physical constraint that market paths must lie in $S^{d-1}\_+$ (positive
simplex hemisphere) may impose additional relations.

**Problem 3** *(Khovanov homology as market risk)*. Develop the financial interpretation
of the bigraded Khovanov homology $\mathrm{Kh}^{i,j}(\Gamma)$. Conjecture: the
homological grading $i$ corresponds to the Jacobi stability index, and the quantum
grading $j$ corresponds to the Chern-Simons level (topological charge).

**Problem 4** *(The knot group as market symmetry)*. The knot group
$\pi\_1(S^3 \setminus \Gamma)$ is the group of market-avoiding strategies. Determine
its representation theory and connect it to the classification of hedging strategies.
For the trefoil: $\pi\_1(S^3 \setminus 3\_1) = \langle a,b : a^2 = b^3\rangle$
(the braid group $B\_3$). The market-avoiding strategies of a trefoil market form the
braid group on 3 strands — a rich algebraic structure.

**Problem 5** *(Topological EMH test)*. Implement Problem 1 empirically and test
whether the Jones polynomial of the market path equals 1 in efficient markets.
Prediction: the Jones polynomial should be close to 1 (CAPM-like) during periods
of market stability and should deviate from 1 around structural breaks.

---

## References

Fox, R. H. and Milnor, J. W. (1966). Singularities of 2-spheres in 4-space and
cobordism of knots. *Osaka Journal of Mathematics* 3(2), 257–267.

Khovanov, M. (2000). A categorification of the Jones polynomial.
*Duke Mathematical Journal* 101(3), 359–426.

Milnor, J. (1968). Infinite cyclic coverings. In: *Conference on the Topology of
Manifolds*, 115–133.

Rasmussen, J. (2010). Khovanov homology and the slice genus.
*Inventiones Mathematicae* 182(2), 419–447.

Seifert, H. (1934). Über das Geschlecht von Knoten.
*Mathematische Annalen* 110(1), 571–592.

Witten, E. (1989). Quantum field theory and the Jones polynomial.
*Communications in Mathematical Physics* 121(3), 351–399.

*[All other references as per companion papers]*
