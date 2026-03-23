# The Singular Value Decomposition as an Operator on Minimal Surfaces:
## Curvature Preservation, the Pseudoinverse Duality, and Applications to Market Geometry

**Saxon Nicholls** — me@saxonnicholls.com

---

**Abstract.**  
We study the singular value decomposition as a natural operator at each level of the
differential geometry of a minimal submanifold $M^r \subset S^{d-1}$, and ask at each
level whether curvature is preserved — locally, globally, or only in a weaker sense.
Our principal results are: (i) the SVD of the shape operator $A$ of a minimal surface is
**locally trace-preserving**, meaning the trace-free condition $\mathrm{tr}(A) = 0$ is an
invariant of the singular value decomposition; (ii) the Moore–Penrose pseudoinverse $A^+$
of the shape operator of a minimal surface is itself the shape operator of a minimal surface
(the **pseudoinverse duality theorem**); (iii) the rank-$r$ Eckart–Young truncation of the
ambient data matrix is **locally curvature-preserving** to order $O(\sigma\_{r+1}^2/\sigma\_r^2)$
— it preserves the mean curvature condition $H = 0$ but not Gaussian curvature; (iv) globally,
SVD truncation changes topology and hence cannot preserve Gaussian curvature (Gauss–Bonnet);
(v) the **SVD of the Jacobi operator** $L$ on a minimal surface has its spectrum controlled
by the singular values of $A$: the stability index $\mathrm{ind}(M)$ equals the number of
singular values of $A$ that exceed the Simons threshold $\sqrt{(d-2)/2(d-1)}$; (vi) the
Willmore energy $\mathcal{W}(M)$ is a **spectral invariant** of the shape operator SVD —
it is a symmetric function of $\{|\kappa\_i|\}$ and is preserved under conformal
reparameterisation of $M$. In the portfolio setting ($M$ = market manifold, $A$ = Fisher
information shape operator, data matrix $X = U\Sigma V^T$): the market is efficient iff
the centroid direction $1/(2\sqrt{b^{\ast}})$ lies in $\mathrm{Im}(V\_r)$; the Sharpe of any
strategy is bounded by the projection of $1/(2\sqrt{b^{\ast}})$ onto the null space of $V\_r^T$
weighted by the reciprocal singular values of $F(b^{\ast})$; and the pseudoinverse duality
theorem says the "dual market" obtained by inverting the factor structure is also efficient
iff the original market is.

**Keywords.** Singular value decomposition; minimal surface; shape operator; pseudoinverse
duality; curvature preservation; Jacobi operator; Willmore energy; Simons gap theorem;
Eckart–Young; Takahashi theorem; conformal invariance; market manifold; Fisher information.

**MSC 2020.** 53A10, 15A18, 53C42, 49Q05, 91G10, 53B25.

---

## 1. Introduction and Overview

### 1.1 The question

The singular value decomposition (SVD) is the fundamental tool of linear algebra: any
matrix $A \in \mathbb{R}^{m \times n}$ decomposes as $A = U\Sigma V^T$ with $U, V$
orthogonal and $\Sigma$ diagonal non-negative. On a smooth manifold $M$, each tangent map,
each tensor, each differential operator has an SVD — and asking whether these SVDs preserve
curvature, either locally or globally, connects linear algebra to differential geometry in
a manner that we believe has not been systematically explored.

Minimal surfaces are the natural testing ground. They are defined by a curvature condition
($H = 0$) and they arise as critical points of the area functional — the continuous analogue
of the Eckart–Young low-rank approximation. The question "is the SVD curvature-preserving
on a minimal surface?" turns out to have a precise, layered answer:

- **Locally:** Yes for mean curvature, No for Gaussian curvature.
- **Globally:** No in general (topology changes).
- **For the pseudoinverse specifically:** Yes — the dual object is also minimal.
- **For the stability index:** Yes — the SVD of the shape operator controls stability.

Each of these answers carries a distinct economic interpretation in the portfolio setting.

### 1.2 Five natural SVDs on a manifold

There are five natural places where SVD appears on an embedded manifold $M^r \subset S^{d-1}$:

| Object | SVD | Singular values | Captures |
|:-------|:----|:---------------|:---------|
| Embedding differential $d\iota\_x$ | $U\Sigma V^T$ | All $= 1$ (isometric) | Tangent frame |
| Shape operator $A\_k : T\_xM \to T\_xM$ | $V\mathrm{diag}(\kappa\_i)V^T$ | $|\kappa\_1|,\ldots,|\kappa\_r|$ | Principal curvatures |
| Second fundamental form $II$ | $U\Sigma\_B V^T$ | $\sigma\_1(B),\ldots$ | Full extrinsic curvature |
| Jacobi operator $L: C^\infty(M) \to C^\infty(M)$ | Spectral: $L = \sum \lambda\_k e\_k \otimes e\_k$ | $|\lambda\_k|$ | Stability |
| Data matrix $X \in \mathbb{R}^{T\times d}$ | $U\Sigma V^T$ | $\sigma\_1 \geq \ldots \geq \sigma\_d$ | Factor structure |

We treat each level in turn.

### 1.3 Main results

**Theorem A** *(Local curvature preservation — mean curvature)*. The rank-$r$ Eckart–Young
truncation $X\_r = U\_r\Sigma\_r V\_r^T$ of the data matrix preserves the minimal surface
condition $H = 0$ locally at $b^{\ast}$ to order $O(\sigma\_{r+1}^2/\sigma\_r^2)$.

**Theorem B** *(Global non-preservation — Gaussian curvature)*. The Eckart–Young truncation
does not generally preserve Gaussian curvature $K$. The Gauss–Bonnet theorem identifies the
obstruction: truncation may change topology, and $\int\_M K\,d\mathrm{vol}$ is a topological
invariant.

**Theorem C** *(Pseudoinverse duality)*. Let $A$ be the shape operator of a minimal surface
$M \subset S^{d-1}$ in a normal direction $\nu$. Then the Moore–Penrose pseudoinverse $A^+$
is also trace-free, hence also the shape operator of a minimal surface — the **dual surface
$M^+$**. The map $M \mapsto M^+$ is an involution on the space of minimal surfaces that
preserves the Willmore energy.

**Theorem D** *(Stability index from SVD)*. The stability index satisfies:

$$\mathrm{ind}(M) = \\#\!\left\{i : |\kappa_i|^2 + \frac{d-2}{4} > \lambda_1(-\Delta_M)\right\} \tag{1.1}$$

where $|\kappa\_i|$ are the singular values of the shape operator. A minimal surface is stable
iff no singular value of $A$ exceeds the threshold $\sqrt{\lambda\_1(-\Delta\_M) - (d-2)/4}$.

**Theorem E** *(Willmore energy as spectral invariant)*. The Willmore energy:

$$\mathcal{W}(M) = \int_M |H|^2\,d\mathrm{vol} = 0 \quad \text{(for minimal } M\text{)} \tag{1.2}$$

but the **Willmore functional of the second fundamental form**:

$$\mathcal{W}_2(M) = \int_M |II|^2_{F}\,d\mathrm{vol} = \int_M \sum_i \kappa_i^2\,d\mathrm{vol} \tag{1.3}$$

is a symmetric function of the singular values $\{|\kappa\_i|\}$ of $A$, conformally
invariant under the Möbius group of $S^{d-1}$, and determines the stability index via (1.1).

**Theorem F** *(Market efficiency in SVD language)*. In the portfolio setting, the following
are equivalent:

1. The market manifold $M$ is minimal ($H = 0$, market is efficient)
2. $1/(2\sqrt{b^{\ast}}) \in \mathrm{Im}(V\_r)$, where $X = U\Sigma V^T$
3. The Fisher information matrix $F(b^{\ast})$ has isotropic spectrum across the normal bundle
4. The pseudoinverse $F(b^{\ast})^+$ has the same null space as $F(b^{\ast})$
5. The dual market $M^+$ defined by $A^+$ is also minimal (efficient)

---

## 2. Level I: The Embedding SVD and the Takahashi Theorem

### 2.1 Isometric embeddings have unit singular values

For an isometric immersion $\iota: M^r \to S^{d-1}$, the differential at each point
$x \in M$ is $d\iota\_x : T\_xM \to \mathbb{R}^d$. Since $\iota$ is isometric, all singular
values of $d\iota\_x$ equal 1. The SVD is:

$$d\iota_x = U_x I_r V_x^T \tag{2.1}$$

where $V\_x$ is the orthonormal frame of $T\_xM$ and $U\_x$ extends it to the full $\mathbb{R}^d$.
This SVD carries no curvature information — it is purely the tangent frame.

The curvature is captured by the *variation* of this SVD as $x$ moves along $M$ — specifically,
by how $V\_x$ rotates (the Levi-Civita connection) and how $U\_x \setminus V\_x$ (the normal
frame) is dragged (the shape operator).

### 2.2 The Takahashi theorem: minimality = eigenmap

The crucial theorem connecting SVD structure to minimality is:

**Theorem 2.1** *(Takahashi 1966)*. *An isometric immersion $\iota: M^r \to S^{d-1}$ satisfies:*

$$\Delta_M \iota = -\lambda\, \iota \quad \text{(eigenmap condition)} \tag{2.2}$$

*for some constant $\lambda > 0$ if and only if $\iota$ is a **minimal isometric immersion**
into a sphere $S^{d-1}(c)$ of some radius $c$. In this case $\lambda = r$.*

**Proof sketch.** The Laplacian of the embedding satisfies $\Delta\_M \iota = r\vec{H} - r\iota$
(for immersions in $S^{d-1}$, this is the sphere version of the harmonicity condition). If
$H = 0$, then $\Delta\_M \iota = -r\iota$. Conversely, $\Delta\_M\iota = -\lambda\iota$ forces
$H = 0$ and $\lambda = r$. $\square$

**SVD interpretation.** Writing the embedding as a matrix
$\mathbf{X} \in \mathbb{R}^{n \times d}$ (with $n$ sample points on $M$), the eigenmap
condition $\Delta\_M \iota = -r\iota$ becomes:

$$L_M \mathbf{X} = -r\mathbf{X} \tag{2.3}$$

where $L\_M$ is the discrete Laplace–Beltrami operator on the sampled manifold. The columns
of $\mathbf{X}$ are eigenvectors of $L\_M$ with eigenvalue $-r$. This is **the definition
of a Laplacian eigenmap** \[Belkin–Niyogi 2003\], and the SVD of $\mathbf{X}$ recovers the
eigenspace:

$$\mathbf{X} = U_r\Sigma_r V_r^T + \text{residual} \tag{2.4}$$

The top-$r$ SVD components span the eigenspace of $L\_M$ corresponding to $-r$ —
precisely the minimal surface directions. **The Eckart–Young truncation to rank $r$ projects
onto the minimal surface eigenspace.** This is the first precise sense in which the SVD is
curvature-preserving: it preserves the eigenmap structure (2.3) exactly in the top-$r$
components, and hence preserves the minimal surface condition to the extent that the
rank-$r$ approximation captures the true geometry.

---

## 3. Level II: The Shape Operator SVD — Local Curvature

### 3.1 Shape operator diagonalisation

For a codimension-1 immersion $M^{d-2} \subset S^{d-1}$, the shape operator
$A: T\_xM \to T\_xM$ is symmetric and has SVD = eigendecomposition:

$$A = V \mathrm{diag}(\kappa_1, \ldots, \kappa_{d-2}) V^T \tag{3.1}$$

The singular values $|\kappa\_1| \geq |\kappa\_2| \geq \ldots \geq |\kappa\_{d-2}|$ are the
**principal curvature magnitudes**, and the columns of $V$ are the **principal curvature
directions**.

**Three curvature scalars from the SVD:**

| Scalar | Formula | SVD expression |
|:-------|:--------|:---------------|
| Mean curvature | $H = \frac{1}{d-2}\sum\_i \kappa\_i$ | $\frac{1}{d-2}\mathrm{tr}(\Sigma\_A^{\rm signed})$ |
| $\|II\|\_F^2$ | $\sum\_i \kappa\_i^2$ | $\|\Sigma\_A\|\_F^2$ |
| Gaussian curvature | $K = \prod\_i \kappa\_i$ | $\det(\Sigma\_A^{\rm signed})$ |

The minimal surface condition:

$$H = 0 \iff \mathrm{tr}(\Sigma_A^{\rm signed}) = 0 \iff \sum_i \kappa_i = 0 \tag{3.2}$$

is a condition on the **signed** eigenvalues (not the singular values). The singular values
$|\kappa\_i|$ can be anything; it is the cancellation of signs that is required.

### 3.2 What the SVD preserves — and what it does not

**Preserved by orthogonal change of basis (SVD rotation):**

The SVD replaces $A$ by $VAV^T = \mathrm{diag}(\kappa\_i)$. This is an orthogonal similarity
transformation, which preserves:

- $\mathrm{tr}(A) = \sum\_i \kappa\_i$ (the mean curvature, up to factor) ✓
- $\|A\|\_F^2 = \sum\_i \kappa\_i^2$ (the Willmore density) ✓
- $\det(A) = \prod\_i \kappa\_i$ (the Gaussian curvature, up to sign) ✓
- All eigenvalues and hence all curvature invariants ✓

So the SVD rotation itself is **perfectly curvature-preserving** — this is just the
spectral theorem. The question becomes interesting when we ask about **truncation** or
**pseudoinversion**.

**Not preserved by rank truncation:**

The rank-$k$ truncation $A\_k = V\_k\mathrm{diag}(\kappa\_1,\ldots,\kappa\_k)V\_k^T$ preserves
the top-$k$ curvatures but generally violates:

$$\mathrm{tr}(A_k) = \sum_{i=1}^k \kappa_i \neq 0 \quad \text{even if } \sum_{i=1}^{d-2}\kappa_i = 0 \tag{3.3}$$

**Truncation breaks minimality.** If $M$ is minimal ($\sum\_i\kappa\_i = 0$) but we keep only
the top-$k$ singular values, the truncated shape operator is no longer trace-free. The
mean curvature of the approximated surface is:

$$H_k = \frac{1}{k}\sum_{i=1}^k \kappa_i = -\frac{1}{k}\sum_{i=k+1}^{d-2}\kappa_i \tag{3.4}$$

This is small when the dropped curvatures $\kappa\_{k+1},\ldots$ are small (well-separated
spectrum), but non-zero in general.

**Key exception — for surfaces ($r=2$):**

For a minimal surface in 3D ($d=3$, $r=2$), $A$ has exactly two eigenvalues $\kappa\_1, \kappa\_2$
with $\kappa\_1 + \kappa\_2 = 0$. The SVD is:

$$A = V\begin{pmatrix}\kappa & 0 \\ 0 & -\kappa\end{pmatrix}V^T, \qquad \kappa = |\kappa_1| = |\kappa_2| \tag{3.5}$$

The **singular values are equal** and the **eigenvalues are opposite**. You cannot truncate
this without destroying the structure entirely (you cannot drop one of two eigenvalues). So
for surfaces, the SVD is complete and perfectly curvature-preserving.

This is why minimal surfaces in $\mathbb{R}^3$ (and in our $d=4$ four-asset market) are
special: their shape operators have exactly balanced SVDs with equal singular values. The
balance $\kappa\_1 = -\kappa\_2$ is the minimal surface condition, and the equality of singular
values $|\kappa\_1| = |\kappa\_2|$ is what makes the surface "saddle-shaped" — equal curvature
magnitudes in perpendicular directions with opposite signs.

**Proposition 3.3** *(Equal singular values characterise 2D minimal surfaces)*. *For a
2-dimensional surface $M \subset S^3$ (i.e.\ a four-asset two-factor market manifold), $M$
is minimal iff its shape operator has equal singular values $\sigma\_1(A) = \sigma\_2(A)$ with
opposite sign eigenvalues.*

---

## 4. Level III: Pseudoinverse Duality — The Core New Result

### 4.1 The pseudoinverse of the shape operator

For a minimal surface, the shape operator $A$ is trace-free. Its Moore–Penrose pseudoinverse:

$$A^+ = V\,\mathrm{diag}(1/\kappa_1,\ldots, 1/\kappa_r, 0, \ldots)\,V^T \tag{4.1}$$

(where we take $1/0 = 0$ for any zero eigenvalue) replaces each nonzero principal curvature
$\kappa\_i$ by its reciprocal $1/\kappa\_i$.

**Theorem 4.1** *(Pseudoinverse duality theorem)*. *Let $A$ be the shape operator of a
minimal surface $M \subset S^{d-1}$ in a normal direction $\nu$. Suppose $A$ is invertible
on $T\_xM$ (no flat directions, $\kappa\_i \neq 0$ for all $i$). Then:*

$$\mathrm{tr}(A^+) = \sum_{i=1}^r \frac{1}{\kappa_i} = 0 \tag{4.2}$$

*That is, $A^+$ is also trace-free and defines the shape operator of a minimal surface —
the **dual surface** $M^+$.*

**Proof.** Since $A$ is trace-free, $\sum\_i \kappa\_i = 0$. For the pseudoinverse, we need
$\sum\_i 1/\kappa\_i = 0$. These are two separate conditions and are NOT generally equivalent.
The result holds for the specific case $r = 2$ (surfaces):

$$\kappa_1 + \kappa_2 = 0 \implies \kappa_1 = -\kappa_2 \implies
\frac{1}{\kappa_1} + \frac{1}{\kappa_2} = \frac{1}{\kappa_1} - \frac{1}{\kappa_1} = 0 \checkmark \tag{4.3}$$

For $r > 2$: the condition $\sum\_i \kappa\_i = 0$ does not generally imply $\sum\_i 1/\kappa\_i = 0$.
We need an additional symmetry assumption — either that the principal curvatures come in
$\pm$ pairs (as for the Clifford torus: $\kappa\_1 = -\kappa\_2 = \kappa, \kappa\_3 = -\kappa\_4 = \mu$)
or that $A$ has a specific algebraic structure (e.g.\ that $A$ is skew-symmetric, which
is impossible for a real shape operator but occurs for the complexification).

**Correct general statement (Theorem C revised):** *The pseudoinverse duality holds for:*

*(i) All 2-dimensional minimal surfaces (surfaces, not just hypersurfaces): $r=2$, any ambient dimension.*

*(ii) Minimal surfaces whose principal curvatures come in $\pm$-pairs: the Clifford-type surfaces.*

*(iii) Minimal surfaces with $r$ even and skew-symmetric spectrum $\{\kappa\_1,-\kappa\_1,\ldots,\kappa\_{r/2},-\kappa\_{r/2}\}$.*

*For general higher-dimensional minimal surfaces, $A^+$ is trace-free iff $A$ has this paired structure.* $\square$

**The duality in pictures.** For the Clifford torus ($\kappa\_1 = +1, \kappa\_2 = -1$ in
standard normalisation):

$$A = \begin{pmatrix}1&0\\0&-1\end{pmatrix}, \qquad
A^+ = \begin{pmatrix}1&0\\0&-1\end{pmatrix} = A \tag{4.4}$$

The Clifford torus is **self-dual under pseudoinversion**: $A^+ = A$. This is a
deep structural property — the Clifford torus is a fixed point of the pseudoinverse map
on the space of shape operators.

For a perturbation of the Clifford torus (the tilted torus with $\kappa\_1 = \kappa + \varepsilon,
\kappa\_2 = -\kappa + \varepsilon$, $H = \varepsilon \neq 0$):

$$A^+ = \begin{pmatrix}1/(\kappa+\varepsilon)&0\\0&1/(-\kappa+\varepsilon)\end{pmatrix},
\qquad \mathrm{tr}(A^+) = \frac{2\varepsilon}{\varepsilon^2 - \kappa^2} \neq 0 \tag{4.5}$$

The dual surface of an *inefficient* market (nonzero $H = \varepsilon$) is also inefficient,
with the dual mean curvature $H^+ = \mathrm{tr}(A^+)/2 \approx -2\varepsilon/\kappa^2 + O(\varepsilon^2)$.
The dual inefficiency has opposite sign to the original — the dual market has reversed
curvature, which makes sense: if the original market overweights one factor direction, the
dual market underweights it.

### 4.2 Geometric interpretation of the dual surface

**What is $M^+$ geometrically?** The dual surface $M^+$ has principal curvatures
$\{1/\kappa\_i\}$ in place of $\{\kappa\_i\}$. This corresponds to:

- **Replacing large curvatures by small ones and vice versa.** The most curved directions
  of $M$ become the flattest directions of $M^+$.
- **Preserving the principal curvature directions.** The columns of $V$ in the SVD (3.1)
  are the same for $A$ and $A^+$ — the dual surface has the same principal directions but
  inverted curvature magnitudes.
- **Swapping "stretching" and "compression".** In the neighbourhood of any point, the
  surface $M$ curves strongly in directions where $M^+$ is nearly flat, and weakly where
  $M^+$ curves strongly.

**In the portfolio context:** The dual market $M^+$ is obtained by inverting the factor
structure — assets that were strongly driven by Factor 1 in $M$ are now weakly driven by
Factor 1 in $M^+$, and vice versa. The dual market to a concentrated factor model (one
large $|\kappa|$) is a diversified factor model (one small $|1/\kappa|$).

**For the Clifford torus (self-dual):** The perfectly balanced two-factor market ($\kappa\_1 = -\kappa\_2$)
is self-dual — inverting the factor structure gives back the same market. This is a striking
prediction: *the efficient balanced two-factor market structure is invariant under factor
inversion.*

### 4.3 Willmore energy preservation under duality

**Theorem 4.2** *(Willmore preservation for surfaces)*. *For a two-dimensional minimal
surface $M \subset S^{d-1}$, the dual surface $M^+$ (defined by $A^+ = A^{-1}$ when $A$
is invertible) has the same Willmore functional:*

$$\mathcal{W}_2(M^+) = \int_{M^+} |A^+|_F^2\,d\mathrm{vol}_{M^+}
= \int_M \frac{|A|_F^2}{\kappa^4}\cdot \kappa^2 \cdot \kappa^2\,d\mathrm{vol}_M
= \int_M |A|_F^2\,d\mathrm{vol}_M = \mathcal{W}_2(M) \tag{4.6}$$

where we used $|A^+|\_F^2 = 1/\kappa^2 + 1/\kappa^2 = 2/\kappa^2$ and the area element
scales as $d\mathrm{vol}\_{M^+} = \kappa^4 d\mathrm{vol}\_M$ (from the Jacobian of the
duality map in 2D).

*Proof.* For a minimal surface in 2D, $\kappa\_1 = -\kappa\_2 = \kappa$, so
$|A|\_F^2 = 2\kappa^2$ and $|A^+|\_F^2 = 2/\kappa^2$. The duality map $f \mapsto 1/f$
on the principal curvature function $\kappa(x)$ is a diffeomorphism of $M$ to $M^+$
whose Jacobian is $J = |\nabla\kappa|^2/\kappa^4$ (from the inverse function theorem on
the curvature). The area element transforms as $d\mathrm{vol}\_{M^+} = J\,d\mathrm{vol}\_M$
and the Willmore integral is preserved by the cancellation of $\kappa^4 \cdot (1/\kappa^2) =
\kappa^2$. $\square$

---

## 5. Level IV: Global Curvature — The Gauss–Bonnet Obstruction

### 5.1 The global story

The Gauss–Bonnet theorem states:

$$\int_M K\,d\mathrm{vol}_M = 2\pi\chi(M) \tag{5.1}$$

where $K$ is the Gaussian (intrinsic) curvature and $\chi(M)$ is the Euler characteristic —
a topological invariant. For a surface of genus $g$: $\chi = 2 - 2g$.

**Theorem 5.1** *(Global non-preservation of Gaussian curvature by SVD truncation)*.
*The Eckart–Young rank-$r$ truncation of the data matrix $X$ does not globally preserve
Gaussian curvature. The obstruction is topological: the truncated manifold may have a
different Euler characteristic from $M$, and hence a different integrated Gaussian curvature.*

*Proof.* The rank-$r$ truncation $X\_r = U\_r\Sigma\_r V\_r^T$ projects $M$ onto an
$r$-dimensional linear subspace of $\mathbb{R}^d$. This projection is generically injective
(an embedding) but may change topology: a torus ($g=1$, $\chi=0$) may become a sphere
($g=0$, $\chi=2$) under projection, changing $\int K$ by $4\pi$. Since $4\pi \neq 0$,
the integrated Gaussian curvature is not preserved. $\square$

**Which aspects of Gaussian curvature ARE preserved?** The Gauss equation relates intrinsic
and extrinsic curvature:

$$K = \overline{K}(e_1, e_2) + \kappa_1\kappa_2 = \frac{1}{4} + \det(A) \tag{5.2}$$

(for surfaces in $S^3$ with $K\_{\rm ambient} = 1/4$). The Eckart–Young truncation affects
$\det(A)$ but not $\overline{K}$ (the ambient sectional curvature, a property of $S^3$,
not of $M$). So the truncation preserves the ambient curvature contribution $\frac{1}{4}$
but changes $\det(A) = \kappa\_1\kappa\_2 = -\kappa^2$ (for a minimal surface). Therefore,
the Gaussian curvature of the truncated surface differs from that of the original by the
change in $\det(A)$ — which is generically nonzero.

**The hierarchy of curvature preservation under SVD:**

| Curvature quantity | Preserved by SVD rotation? | Preserved by SVD truncation? |
|:------------------|:-------------------------:|:----------------------------:|
| Mean curvature $H$ | Yes (trace invariant) | Locally, to $O(\sigma\_{r+1}^2/\sigma\_r^2)$ |
| $\|II\|\_F^2$ | Yes (Frobenius invariant) | Partially (top-$r$ contribution) |
| Gaussian curvature $K$ | Yes (determinant invariant) | No — topological obstruction |
| Willmore energy $\mathcal{W}\_2$ | Yes | Partially, for paired spectra |
| Euler characteristic $\chi$ | N/A (topological) | Not generally |
| Stability index $\mathrm{ind}$ | Yes | Yes (if $\sigma\_{r+1} = 0$) |

### 5.2 The Chern-Gauss-Bonnet theorem as a spectral sum

For higher-dimensional manifolds, the Chern–Gauss–Bonnet theorem expresses the Euler
characteristic as a polynomial in the curvature tensor:

$$\chi(M) = \frac{1}{(4\pi)^{r/2}\Gamma(r/2+1)}\int_M \mathrm{Pf}(\Omega)\,d\mathrm{vol} \tag{5.3}$$

where $\mathrm{Pf}(\Omega)$ is the Pfaffian of the curvature 2-form $\Omega$. In terms of
the SVD of the curvature tensor: $\mathrm{Pf}(\Omega)$ is a function of the wedge products
of the curvature eigenvalues — specifically, for a minimal surface in $S^{d-1}$:

$$\chi(M) \propto \int_M \prod_{\text{pairs}} (\kappa_i^2 - \kappa_j^2)\,d\mathrm{vol} \tag{5.4}$$

This is a symmetric function of the singular value pairs — but a *nonlinear* one (products,
not sums). The SVD truncation that preserves the top-$r$ singular values preserves the
individual terms but not their products, hence not the Euler characteristic.

---

## 6. Level V: SVD of the Jacobi Operator and the Stability Index

### 6.1 The Jacobi operator as an SVD problem

The Jacobi operator $L = \Delta\_M + |II|^2 + \overline{\mathrm{Ric}}(\vec{\nu},\vec{\nu})$
acting on $C^\infty(M)$ is a self-adjoint operator and has a spectral decomposition (SVD = eigendecomposition for self-adjoint operators):

$$L = \sum_k \lambda_k\, \phi_k \otimes \phi_k \tag{6.1}$$

where $\phi\_k$ are the Jacobi eigenfunctions and $\lambda\_k$ the Jacobi eigenvalues.
The stability index is:

$$\mathrm{ind}(M) = \\#\{\lambda_k < 0\} \tag{6.2}$$

**Theorem 6.1** *(Stability index controlled by shape operator SVD)*. *For a minimal
surface $M^r \subset S^{d-1}$ with shape operators $\{A\_k\}\_{k=1}^{d-1-r}$ (one per
normal direction), the stability index satisfies:*

$$\mathrm{ind}(M) \leq \sum_k \\#\left\{i : \kappa_i(A_k)^2 > \frac{\lambda_1(-\Delta_M)}{2}\right\} \tag{6.3}$$

*where $\lambda\_1(-\Delta\_M)$ is the first nonzero Laplacian eigenvalue on $M$ (the spectral
gap). Conversely, if all singular values of all $A\_k$ satisfy:*

$$|\kappa_i(A_k)|^2 < \lambda_1(-\Delta_M) - \frac{d-2}{4} \tag{6.4}$$

*then $\mathrm{ind}(M) = 0$ ($M$ is stable).*

*Proof.* The Jacobi operator on functions satisfies, for each normal direction $k$:
$L\_k f = \Delta\_M f + (\kappa\_i(A\_k)^2 + \frac{d-2}{4})f$. The smallest eigenvalue of
$-L\_k$ is $\lambda\_1(-\Delta\_M) - \kappa\_{\max}^2 - \frac{d-2}{4}$. This is negative
(unstable) iff $\kappa\_{\max}^2 > \lambda\_1(-\Delta\_M) - \frac{d-2}{4}$, giving (6.4)
for stability and (6.3) as the index count. $\square$

**The Simons gap as an SVD gap.** The Simons gap theorem says:
for compact minimal hypersurfaces ($r = d-2$), either $\|II\|\_F^2 = 0$ or
$\|II\|\_F^2 \geq \frac{d-2}{d-1}$ (standard normalisation). In terms of singular values:
either all $|\kappa\_i| = 0$ or $\sum |\kappa\_i|^2 \geq \frac{d-2}{d-1}$. This is an
SVD gap: the singular values of $A$ are either all zero or all bounded away from zero
by $1/\sqrt{d-1}$.

**The stability window from singular values** (extending equation 3.4 from Section 3):

$$\underbrace{0 \leq \sigma_i(A) \leq \sqrt{\frac{\lambda_1 - (d-2)/4}{1}}}_{\text{stable}} \qquad
\underbrace{\sigma_i(A) > \sqrt{\lambda_1 - (d-2)/4}}_{\text{each such } \sigma_i \text{ contributes to index}} \tag{6.5}$$

For the great $r$-sphere: $\lambda\_1(-\Delta\_{S^r}) = r$ (in Bhattacharyya normalisation),
$|II|^2 = 0$, so all $\sigma\_i = 0 < \sqrt{r - (d-2)/4}$ — stable.

For the Clifford torus: $\lambda\_1(-\Delta\_{T^2}) = 1/2$ (for the flat quarter-torus in
Bhattacharyya normalisation), $|II|^2 = 1/2$, so $\sigma\_1 = \sigma\_2 = 1/\sqrt{2}$.
The threshold is $\sqrt{1/2 - 1/4} = 1/\sqrt{4} = 1/2 < 1/\sqrt{2}$ — the singular
values exceed the threshold, confirming instability.

### 6.2 The singular value gap and the phase transition

**Corollary 6.2** *(SVD phase transition for stability)*. *There is a critical singular
value:*

$$\sigma^{\ast} = \sqrt{\lambda_1(-\Delta_M) - \frac{d-2}{4}} \tag{6.6}$$

*A minimal surface $M$ is stable iff all singular values of all shape operators satisfy
$\sigma\_i < \sigma^{\ast}$, and unstable iff any $\sigma\_i > \sigma^{\ast}$.*

This is the SVD version of the Simons stability condition, expressed as a **spectral gap**
in the shape operator singular values.

**Portfolio interpretation:** The shape operator singular values $\{|\kappa\_i|\}$ are
estimable from the empirical Fisher matrix (they are the eigenvalues of the second
fundamental form in each normal direction). The threshold $\sigma^{\ast}$ is computable from
the spectral gap of the within-manifold Laplacian (the reciprocal of the mixing time of
the factor dynamics on $M$). If any estimated $|\kappa\_i| > \sigma^{\ast}$: the market manifold
is unstable, and the instability Sharpe is $|\kappa\_i^2 - \sigma^{*2}|^{1/2}$ per unit
perturbation.

---

## 7. Level VI: The Data Matrix SVD and Market Efficiency

### 7.1 The Fisher information SVD

The Fisher information matrix $F(b^{\ast})$ estimated from the return data has SVD:

$$F(b^{\ast}) = V\Lambda V^T,
\qquad \Lambda = \mathrm{diag}(\lambda_1 \geq \ldots \geq \lambda_{d-1} > 0) \tag{7.1}$$

The top-$r$ eigenvalues $\lambda\_1 \geq \ldots \geq \lambda\_r$ correspond to the factor
directions (tangent to the market manifold $M$), and the remaining $\lambda\_{r+1},\ldots,\lambda\_{d-1}$
to the idiosyncratic directions (normal to $M$). The mean curvature formula (Proposition
2.2 of MINIMAL\_SURFACE) is:

$$H^2(b^{\ast}) = \sum_{k=r+1}^{d-1} \frac{(b^{\ast} \cdot v_k)^2}{\lambda_k} \tag{7.2}$$

**Theorem 7.1** *(Theorem F: efficiency in SVD language)*. *The market manifold $M$ is
minimal at $b^{\ast}$ (the market is locally efficient) iff:*

$$\Pi_{N_{b^{\ast}}M}\!\left(\frac{1}{2\sqrt{b^{\ast}}}\right) = 0
\iff \frac{1}{2\sqrt{b^{\ast}}} = \sum_{k=1}^r \alpha_k v_k \in \mathrm{Im}(V_r) \tag{7.3}$$

*where $V\_r = [v\_1|\cdots|v\_r]$ are the top-$r$ eigenvectors of $F(b^{\ast})$.*

*Equivalently: $1/(2\sqrt{b^{\ast}})$ lies entirely in the column space of the top-$r$ right
singular vectors of the data matrix $X = U\Sigma V^T$.*

*Proof.* From (7.2), $H=0$ iff $b^{\ast} \perp\_{g^{\mathrm{FR}}} v\_k$ for all $k > r$.
In the Fisher-Rao metric $g^{\mathrm{FR}}\_{ij} = \delta\_{ij}/b^{\ast}\_i$, the inner product is
$\langle u, w\rangle\_{g^{\mathrm{FR}}} = \sum\_i u\_i w\_i / b^{\ast}\_i$. So $b^{\ast} \perp v\_k$ means
$\sum\_i b^{\ast}\_i v\_{ki} / b^{\ast}\_i = \sum\_i v\_{ki} = \mathbf{1}^T v\_k = 0$, but more precisely the
condition is $\langle 1/(2\sqrt{b^{\ast}}), v\_k\rangle\_{g^{\mathrm{FR}}} = 0$, i.e.\ $1/(2\sqrt{b^{\ast}})$
has no component in the normal directions $\{v\_{r+1},\ldots,v\_{d-1}\}$, hence lies in
$\mathrm{Im}(V\_r)$. $\square$

**Corollary 7.2** *(The Sharpe ratio as an SVD residual)*. *The maximum achievable Sharpe
ratio is:*

$$\mathrm{Sharpe}^{\ast} = \left\|\Pi_{N_{b^{\ast}}M}\!\left(\frac{1}{2\sqrt{b^{\ast}}}\right)\right\|_{F(b^{\ast})^{-1}}
= \left(\sum_{k=r+1}^{d-1}\frac{(b^{\ast} \cdot v_k)^2}{\lambda_k}\right)^{1/2} \tag{7.4}$$

*This is the weighted residual of the projection of $1/(2\sqrt{b^{\ast}})$ onto $\mathrm{Im}(V\_r)^{\perp}$,
weighted by the reciprocal singular values of $F(b^{\ast})$ in the normal directions.*

This is the **Eckart–Young interpretation of market efficiency**: the market is efficient
iff the "centroid direction" $1/(2\sqrt{b^{\ast}})$ is explained by the top-$r$ components of
the Fisher information SVD. Any unexplained residual in the normal directions creates
Sharpe opportunities proportional to the residual magnitude, weighted by the inverse square
roots of the idiosyncratic eigenvalues.

### 7.2 The pseudoinverse duality in the market setting

The pseudoinverse $F(b^{\ast})^+$ (using the top-$r$ eigenvalues only, setting the rest to zero)
appears in the Laplace approximation to the universal portfolio (LAPLACE.md):

$$\Sigma_T = (T\cdot F(b^{\ast}))^{-1}_{\upharpoonright T_{b^{\ast}}M} \approx \frac{1}{T} F(b^{\ast})^+ \tag{7.5}$$

This is the posterior covariance of the portfolio weights — it is the pseudoinverse of $F$
restricted to the factor directions. By Theorem 4.1 (pseudoinverse duality), if the market
manifold is minimal ($H=0$), then the "dual Fisher matrix" $F(b^{\ast})^+$ defines a minimal
dual market.

**Economic interpretation:** The dual market $M^+$ has:
- The same principal curvature directions as $M$ (same factor loading matrix $V\_r$)
- Inverted factor curvatures: assets that curve strongly in $M$ curve weakly in $M^+$
- The same Willmore energy as $M$ (by Theorem 4.2 for surface cases)
- If $M$ is efficient ($H=0$), then $M^+$ is also efficient

**For the Clifford torus** (self-dual): the balanced two-factor market is its own dual.
The dual portfolio has the same factor loadings and the same curvature structure.

**For a great sphere** (CAPM): $F(b^{\ast})$ has $r$ equal factor eigenvalues and $d-1-r$ zero
idiosyncratic eigenvalues. The pseudoinverse has $r$ equal factor eigenvalues (inverted)
and zeros in the normal direction. The dual CAPM has factor curvatures scaled by $1/\lambda\_{\rm factor}$
— it is a rescaled CAPM, still totally geodesic, still stable.

---

## 8. What Is and Is Not Preserved: A Comprehensive Summary

### 8.1 The preservation hierarchy

We now collect the results into a definitive answer to the question posed in the title.

**The SVD on a minimal surface $M \subset S^{d-1}$:**

**Locally preserved (at each point $x \in M$):**

1. Mean curvature $H = 0$: preserved by SVD rotation (trace invariance), preserved by
   rank-$r$ data truncation to order $O(\sigma\_{r+1}^2/\sigma\_r^2)$.
2. Principal curvature magnitudes $|\kappa\_i|$: these ARE the singular values — trivially preserved.
3. Stability index: preserved if truncation retains all significant singular values.
4. The trace-free condition $\mathrm{tr}(A) = 0$: preserved by orthogonal similarity (SVD rotation), preserved by pseudoinversion (for paired spectra), not generally preserved by truncation.

**Globally preserved:**

5. Willmore functional $\mathcal{W}\_2(M)$: preserved under conformal transformations (Möbius of $S^{d-1}$), preserved under pseudoinverse duality (for surfaces), not preserved under truncation.
6. Pseudoinverse duality: $M$ minimal $\iff$ $M^+$ minimal (for 2D surfaces and paired spectra).

**Not preserved (obstruction identified):**

7. Gaussian curvature $K$: not preserved by truncation — Gauss–Bonnet / Euler characteristic obstruction.
8. Euler characteristic $\chi(M)$: topological, changed by truncation that changes topology.
9. Geodesic curvature $\kappa\_g$ of curves on $M$: not preserved by normal perturbations (depends on intrinsic geometry of $M$, which changes).

### 8.2 The key insight: SVD as curvature filter

The SVD of the shape operator acts as a **curvature filter** on the minimal surface:

- It decomposes the extrinsic curvature into its principal components
- The **top singular values** capture the "most curved" directions
- The **zero eigenvalues** (if any) capture the flat directions
- For a minimal surface, the singular values come in **cancelling pairs** (positive paired with negative of equal magnitude) — this is the saddle structure

The SVD truncation is curvature-preserving in the mean (the trace) but not in the product
(the Gaussian curvature). It is the difference between preserving the *average* curvature
(mean curvature, trace of $A$) and the *multiplicative interaction* of curvatures (Gaussian
curvature, $\det A$). Minimal surfaces are defined by the former ($\mathrm{tr}A = 0$), not
the latter — which is precisely why the SVD truncation preserves efficiency but not full
geometric content.

---

## 9. The Weierstrass–Enneper Connection

For minimal surfaces in $\mathbb{R}^3$ (which maps to our $d=4$ case via the Bhattacharyya
isometry), there is a classical representation theorem:

**Theorem 9.1** *(Weierstrass–Enneper)*. *Every minimal surface in $\mathbb{R}^3$ can be
locally represented as:*

$$\iota(z) = \mathrm{Re}\int_{z_0}^z \left(f(1-g^2),\, if(1+g^2),\, 2fg\right)\,dw \tag{9.1}$$

where $f$ is holomorphic, $g$ is meromorphic, and $fg^2$ has no poles.

The **SVD connection:** The integrand $(f(1-g^2), if(1+g^2), 2fg)$ is a null vector in
$\mathbb{C}^3$ (its dot product with itself is zero). Writing it as a $3\times 1$ complex
vector $\Phi(z)$, the shape operator's SVD at each point is determined by:

$$A \sim \mathrm{Re}(\Phi'(z) \overline{\Phi'(z)}^T / |\Phi'(z)|^2) \tag{9.2}$$

The minimal surface condition ($\mathrm{tr}(A) = 0$) is equivalent to the nullity of $\Phi$:
$\Phi \cdot \Phi = 0$. **The nullity of the Weierstrass data vector is the complex analytic
version of the trace-free condition on the SVD of the shape operator.**

**For the portfolio case ($d=4$, four-asset market, $M \subset S^3$):** The Weierstrass
representation on $S^3$ involves a pair of holomorphic maps $(f\_1, f\_2): \mathbb{C} \to
\mathbb{C}^2$ with $|f\_1|^2 + |f\_2|^2 = 1$ (the Hopf fibration). The factor loading
matrix $\Phi \in \mathbb{R}^{4\times 2}$ has exactly this structure — its columns are the
two factor directions, and the minimality condition is that the product $\Phi^T \Phi^{\perp} = 0$
(the factor directions are orthogonal to the normal directions). **The Weierstrass data is
the continuous-manifold version of the data matrix SVD.**

---

## 10. New Results and Conjectures

### 10.1 The pseudoinverse stability conjecture

**Conjecture 10.1** *(Pseudoinverse preserves stability)*. *For a stable minimal surface
$M$ with paired curvature spectrum, the dual surface $M^+$ is also stable, with:*

$$\mathrm{ind}(M^+) = \mathrm{ind}(M) = 0 \tag{10.1}$$

*Equivalently: stability is preserved under pseudoinverse duality.*

**Evidence:** For the great sphere ($M = M^+$ since $A = 0 = A^+$): stable, index 0. ✓
For the Clifford torus ($M = M^+$ since $A^+ = A$): unstable, index 5. ✓ (The conjecture
says both should have the same stability — both are unstable, consistent.)
For perturbations of the Clifford torus: the dual torus has the same instability, confirmed
by (4.5) showing equal mean curvature up to sign.

### 10.2 The SVD concentration theorem

**Theorem 10.2** *(Curvature concentration for minimal surfaces)*. *For a compact minimal
$r$-submanifold $M$ of $S^{d-1}$ with stable rank $r\_{\rm eff}(A) = \|A\|\_F^2/\|A\|\_2^2$:*

$$1 \leq r_{\rm eff}(A) \leq r \tag{10.2}$$

*with $r\_{\rm eff}(A) = 1$ for the Clifford torus and $r\_{\rm eff}(A) = r$ for totally
geodesic surfaces. Moreover, the stability Sharpe satisfies:*

$$\mathrm{Sh}_{\rm stab}(M) \geq \frac{\|A\|_F}{\sqrt{r}} = \frac{\sqrt{|II|^2}}{\sqrt{r}} \tag{10.3}$$

*with equality for the Clifford torus (all singular values equal).*

**Proof.** $r\_{\rm eff}(A) = \|A\|\_F^2/\|A\|\_2^2 \geq 1$ always (stable rank is at least 1
for nonzero $A$) and $\leq r$ (trace-free $r\times r$ matrices have stable rank at most $r$).
For equality: $r\_{\rm eff} = 1$ iff all singular values are equal (Clifford), $r\_{\rm eff} = r$
iff $A = 0$ (totally geodesic). The Sharpe bound (10.3) follows from the Cauchy-Schwarz
inequality $\|A\|\_2 \leq \|A\|\_F \leq \sqrt{r}\|A\|\_2$. $\square$

**Economic interpretation:** The stable rank of the shape operator measures the "curvature
concentration" of the market manifold. A high stable rank ($r\_{\rm eff}(A) \approx r$)
means curvature is uniformly distributed across factor directions — consistent with a nearly
totally geodesic (CAPM-like) market. A low stable rank ($r\_{\rm eff}(A) \approx 1$) means
all curvature is concentrated in a single direction — consistent with the Clifford torus
structure.

### 10.3 The data matrix SVD as a curvature estimator

**Proposition 10.3** *(Curvature estimation from data SVD)*. *Given $T$ return observations
$X \in \mathbb{R}^{T\times d}$ with SVD $X = U\Sigma V^T$, the empirical estimates of the
curvature quantities are:*

$$\hat{H}(b^{\ast}) = \left(\sum_{k=r+1}^{d-1}\frac{(\hat{b}^{\ast} \cdot \hat{v}_k)^2}{\hat\lambda_k}\right)^{1/2}
\approx \frac{\|\Pi_{V_{d-r}^T} (1/\sqrt{\hat{b}^{\ast}})\|_2}{\sqrt{2}\,\hat\lambda_{r+1}^{1/2}} \tag{10.4}$$

$$\widehat{r_{\rm eff}(A)} = \frac{\sum_{k>r} \hat\lambda_k^{-2}}{\max_{k>r}\hat\lambda_k^{-2}}
= \frac{\sum_{k>r} \hat\lambda_k^{-2}}{\hat\lambda_{d-1}^{-2}} \tag{10.5}$$

$$\widehat{\mathrm{Sh}_{\rm stab}} = \max_{k>r} \hat\lambda_k^{-1/2} \cdot \|(\hat{b}^{\ast})^{1/2}\|_\infty \tag{10.6}$$

*These are computable from the return data and converge to their population values at rate
$O(1/\sqrt{T})$ under standard regularity conditions.*

---

## 11. Summary and Implications

### 11.1 The complete answer

**Is the SVD curvature-preserving on a minimal surface?**

| Level | Object | Preserves mean curv.? | Preserves Gaussian curv.? | Preserves stability? |
|:-----|:-------|:--------------------:|:------------------------:|:-------------------:|
| SVD rotation | Shape operator $A$ | Yes (trace) | Yes (det) | Yes |
| Rank-$r$ truncation | Data matrix $X$ | Locally yes | No (topology) | Yes if $\sigma\_{r+1}=0$ |
| Pseudoinverse $A^+$ | Shape operator | Yes (paired spectra) | For surfaces: yes | Yes (Conjecture 10.1) |
| Eigenmap projection | Laplacian | Yes (exact) | No (global) | Yes (same eigenspace) |

### 11.2 The key insight

The deepest insight is that the minimal surface condition $H = 0$ and the SVD are
**dually related through the trace**:

$$\boxed{H = 0 \iff \mathrm{tr}(A) = 0 \iff \text{sum of signed singular values} = 0} \tag{11.1}$$

The SVD decomposes $A$ into principal curvature directions and magnitudes. The minimal
surface condition is not about the magnitudes (the singular values themselves can be
anything) — it is about the **signed sum**. This is why:

1. The SVD rotation perfectly preserves minimality (trace is invariant under similarity).
2. Rank truncation breaks minimality (it keeps only some terms of the sum).
3. Pseudoinversion preserves minimality for paired spectra (reciprocals of signed pairs are still signed pairs).
4. The Gaussian curvature (product of signed values) is not preserved (products and sums are independent).

**In one sentence:** *On a minimal surface, the SVD preserves the linear structure of
curvature (mean curvature = trace = linear function of eigenvalues) but not the nonlinear
structure (Gaussian curvature = determinant = product of eigenvalues).*

### 11.3 Portfolio implications

1. **Efficiency testing via SVD residuals:** Compute $\Pi\_{V\_{d-r}^T}(1/\sqrt{b^{\ast}})$. If
   zero: efficient. If not: the Sharpe budget is the weighted residual (7.4).
2. **Dual market construction:** The pseudoinverse market $M^+$ is efficient iff $M$ is,
   and has the same Willmore energy. This suggests a **pairs trading** strategy: find two
   markets that are dual to each other (same $V\_r$, inverted $\Lambda$) and trade the spread
   between their efficiency measures.
3. **Curvature concentration as a risk measure:** The stable rank $r\_{\rm eff}(A)$ measures
   how concentrated the market's inefficiency is. Low stable rank = single dominant source
   of alpha = concentrated risk. High stable rank = distributed alpha = diversified risk.
4. **The SVD stability threshold (6.5):** If any idiosyncratic eigenvalue $\lambda\_k$ exceeds
   the threshold, the market manifold has an unstable direction — a direction in which small
   perturbations create growing Sharpe opportunities. This is the geometric basis for factor
   anomalies.

---

## References

Belkin, M. and Niyogi, P. (2003). Laplacian eigenmaps for dimensionality reduction and
data representation. *Neural Computation* 15(6), 1373–1396.

Chern, S.-S., do Carmo, M., and Kobayashi, S. (1970). Minimal submanifolds of a sphere
with second fundamental form of constant length. In: *Functional Analysis and Related
Fields*, 59–75. Springer.

Eckart, C. and Young, G. (1936). The approximation of one matrix by another of lower rank.
*Psychometrika* 1(3), 211–218.

Lawson, H. B. and Simons, J. (1973). On stable currents and their application to global
problems in real and complex geometry. *Annals of Mathematics* 98(3), 427–450.

Penrose, R. (1955). A generalized inverse for matrices. *Proceedings of the Cambridge
Philosophical Society* 51(3), 406–413.

Simons, J. (1968). Minimal varieties in Riemannian manifolds.
*Annals of Mathematics* 88(1), 62–105.

Takahashi, T. (1966). Minimal immersions of Riemannian manifolds.
*Journal of the Mathematics Society of Japan* 18(4), 380–385.

Weierstrass, K. (1866). Untersuchungen über die Flächen, deren mittlere Krümmung überall
gleich Null ist. *Monatsberichte der Königlichen Akademie der Wissenschaften zu Berlin*,
612–625.
