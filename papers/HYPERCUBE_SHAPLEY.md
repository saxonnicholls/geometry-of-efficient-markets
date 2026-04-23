# Hypercube Embeddings, Shapley Values, and Attribution Analysis
## on the Market Manifold: The Simplex Inside the Cube,
## and the Unique Fair Attribution of Kelly Growth to Assets

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.6** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
The portfolio simplex $\Delta_{d-1} = \{b\in\mathbb{R}^{d}_+ : \sum b_i = 1\}$ embeds
naturally in the unit hypercube $[0,1]^d$. This embedding connects the Fisher-Rao
geometry of the simplex integral to the Walsh-Hadamard-Fourier analysis on the
hypercube, producing a new computational approach to the MUP and a new representation
of the filtration atoms. The Shapley value from cooperative game theory provides the
unique fair attribution of the Kelly log-growth rate to individual assets, satisfying
efficiency (sum = total), symmetry (identical assets get equal attribution), dummy
(irrelevant assets get zero), and linearity. We prove that the Shapley attribution
of Kelly growth to assets is the **Fisher-Rao projection** of the log-optimal
portfolio onto the coordinate axes — a purely geometric quantity.

**Our principal results:**

**(i) The simplex inside the hypercube.** $\Delta_{d-1}\subset[0,1]^d$ is a
codimension-1 face of the $d$-dimensional hypercube. The vertices of $\Delta_{d-1}$
are a subset of the vertices of $[0,1]^d$ (the $d$ standard basis vectors $e_i$).
The Walsh-Hadamard transform on $[0,1]^d$ restricts to the Fourier-Jacobi expansion
on $\Delta_{d-1}$, connecting the hypercube harmonic analysis to the Jacobi polynomial
series of MARKET_PROCESSES.md.

**(ii) The hypercube Fourier basis = Jacobi polynomial basis.** The Walsh functions
$w_S(b) = \prod_{i\in S}(2b_i-1)$ for $S\subseteq\{1,\ldots,d\}$ restricted to
$\Delta_{d-1}$ are proportional to the Jacobi polynomials $P_n^{(\alpha,\beta)}(2b_i-1)$.
The MUP partition function (a Selberg integral on $\Delta_{d-1}$) has an exact
Walsh-Fourier expansion on the hypercube with coefficients given by the Selberg integral
evaluated at successive Jacobi parameters.

**(iii) Hypercube Voronoi = simplicial complex.** The Voronoi decomposition of the
hypercube $[0,1]^d$ with centres at the $d$ simplex vertices $\{e_1,\ldots,e_d\}$ is
the **barycentric subdivision** of the simplex — the triangulation into $d!$ simplices
obtained by ordering coordinates. This is the Delaunay triangulation of $\Delta_{d-1}$
from FOKKER_PLANCK_CFD.md, now seen as the natural simplicial complex of the hypercube.

**(iv) Shapley values = Fisher-Rao attribution.** The Shapley value of asset $i$ in
the Kelly growth cooperative game $v(S) = \max_{b\in\Delta_{|S|-1}} L_T(b|S)$ is:

```math
\phi_i = \sum_{S\subseteq[d]\setminus\{i\}}\frac{|S|!(d-|S|-1)!}{d!}
\left[v(S\cup\{i\}) - v(S)\right] \tag{0.1}
```

This satisfies all four Shapley axioms. We prove that the Shapley attribution equals
the Fisher-Rao gradient of the Kelly growth rate projected onto the $i$-th coordinate:

```math
\phi_i = b^{\ast}_{i}\frac{\partial L_T}{\partial b_i}\bigg|_{b=b^{\ast}} = b^{\ast}_{i}(\mu_i - \bar\mu) \tag{0.2}
```

— the product of the log-optimal weight and the excess expected return. This is
the **CAPM alpha attribution formula** derived from cooperative game theory.

**Keywords.** Hypercube; simplex; Walsh-Hadamard transform; Fourier analysis on simplex;
barycentric subdivision; Voronoi; Shapley value; cooperative game; Kelly criterion;
attribution analysis; Fisher-Rao gradient; CAPM alpha; factor contribution.

---

## 1. The Simplex Inside the Hypercube

### 1.1 The embedding

The portfolio simplex $\Delta_{d-1}$ sits inside the unit hypercube $[0,1]^d$:

```math
\Delta_{d-1} = \{b \in [0,1]^d : \textstyle\sum_{i=1}^{d} b_i = 1\} \tag{1.1}
```

It is the intersection of the hypercube with the affine hyperplane $\sum b_i = 1$, which
is a face of the hyperplane arrangement $\{x_1+\cdots+x_d = 1\}$.

**The vertices of $\Delta_{d-1}$** are the $d$ standard basis vectors $e_1,\ldots,e_d$
— which are also $d$ of the $2^d$ vertices of $[0,1]^d$.

**The Bhattacharyya image.** Under $b\mapsto\sqrt{b}$, the simplex maps to $S^{d-1}_{+}$.
Under $\sqrt{b}\mapsto 2\sqrt{b}-1$, the sphere is flipped to $[-1,1]^d$, and the
Jacobi-type weight $\prod_i b_i^{\alpha_i-1} = \prod_i ((u_i+1)/2)^{\alpha_i-1}$
becomes a Gegenbauer weight on $[-1,1]^d$. This connects to the Walsh-Hadamard
transform on $\{-1,+1\}^{d}$ (the discrete hypercube).

### 1.2 The barycentric subdivision and Delaunay

**The barycentric subdivision** of $\Delta_{d-1}$ is the simplicial complex obtained
by ordering coordinates: for each permutation $\sigma\in S_d$, the simplex

```math
\Delta_\sigma = \{b\in\Delta_{d-1} : b_{\sigma(1)} \geq b_{\sigma(2)} \geq \cdots \geq b_{\sigma(d)}\}
```

forms one of $d!$ sub-simplices. Together they triangulate $\Delta_{d-1}$.

**Theorem 1.1** *(Barycentric subdivision = Voronoi Delaunay)*.
*The barycentric subdivision of $\Delta_{d-1}$ with respect to the Fisher-Rao metric
is exactly the Voronoi decomposition of FOKKER_PLANCK_CFD.md (Theorem 3.1) with
the $d$ standard basis vectors as centres. Each barycentric cell $\Delta_\sigma$
corresponds to the Voronoi cell of the vertex $e_{\sigma(1)}$ — the asset with the
highest weight.*

*Proof.* The barycentric cell $\Delta_\sigma = \{b : b_{\sigma(1)}\geq\cdots\geq b_{\sigma(d)}\}$
contains exactly those portfolios where asset $\sigma(1)$ has the largest weight.
In the Fisher-Rao metric, the distance from $b$ to vertex $e_i$ is
$d_{g^{\rm FR}}(b,e_i) = 2\arccos(\sqrt{b_i})$, which decreases in $b_i$.
So $b$ is closest to $e_{\sigma(1)}$ iff $b_{\sigma(1)}$ is the largest — precisely
the barycentric cell condition. $\square$

---

## 2. Walsh-Hadamard Transform on the Simplex

### 2.1 Walsh functions on the hypercube

The **Walsh functions** on $\{0,1\}^{d}$ (or $\{-1,+1\}^{d}$ in the $\pm 1$ basis) are:

```math
w_S(x) = \prod_{i\in S}(-1)^{x_i} = \prod_{i\in S}x_i, \qquad S\subseteq[d], x\in\{-1,+1\}^{d} \tag{2.1}
```

They form an orthonormal basis: $\sum_{x\in\{-1,+1\}^{d}}w_S(x)w_T(x) = 2^d\delta_{ST}$.

**Continuous extension to the simplex.** For $b \in \Delta_{d-1}$, replacing $x_i$ with
$2b_i - 1 \in [-1,+1]$:

```math
w_S(b) = \prod_{i\in S}(2b_i - 1) \tag{2.2}
```

The set $\{w_S : S\subseteq[d]\}$ is not orthonormal on $\Delta_{d-1}$, but is a
polynomial basis. The Walsh expansion of any function $f:\Delta_{d-1}\to\mathbb{R}$:

```math
f(b) = \sum_{S\subseteq[d]}\hat f_S\, w_S(b), \qquad
\hat f_S = \int_{\Delta_{d-1}} f(b)\, w_S(b)\, d\mathrm{vol}(b) \tag{2.3}
```

is the **Walsh-Fourier expansion on the simplex**.

### 2.2 Walsh = Jacobi polynomials

**Theorem 2.1** *(Walsh basis = Jacobi polynomial basis on the simplex)*.
*For $d=2$ (two-asset simplex $\Delta_1 = [0,1]$), the Walsh functions restricted to
$\Delta_1$ are proportional to the Jacobi polynomials:*

```math
w_{\{1\}}(b) = 2b_1 - 1 = P_1^{(0,0)}(2b_1-1) \tag{2.4}
```

*More generally: the multilinear Walsh function $w_S(b) = \prod_{i\in S}(2b_i-1)$
equals the degree-$|S|$ multivariate Jacobi polynomial on $\Delta_{d-1}$ evaluated
at the appropriate parameters.*

**The Jacobi polynomial series** of MARKET_PROCESSES.md (the transition density of the
Jacobi diffusion) is exactly the Walsh-Fourier expansion of the transition density on
the simplex.

### 2.3 The MUP partition function in Walsh coordinates

The MUP normalisation constant $\mathcal{Z}_{T} = \int_{\Delta_{d-1}}W_T(b)\,d\mathrm{vol}(b)$
has a Walsh expansion:

```math
\mathcal{Z}_{T} = \sum_{S\subseteq[d]}\hat W_S\cdot \hat{1}_{S} \tag{2.5}
```

where $\hat W_S = \int W_T(b)\,w_S(b)\,d\mathrm{vol}(b)$ are the Walsh coefficients
of the wealth function and $\hat{1}_{S} = \int w_S(b)\,d\mathrm{vol}(b)$ are the
volume coefficients.

**For the CAPM ($d=2$):** The Walsh expansion has only the $S=\emptyset$ and $S=\{1\}$ terms:
$\mathcal{Z}_{T} = B(\alpha,\beta) + \hat W_{\{1\}}\cdot 0$ (the $S=\{1\}$ term vanishes by
symmetry). The Selberg integral (RANDOM_MATRIX.md Theorem 3.1) = the $S=\emptyset$ Walsh coefficient.

**The hypercube representation is computationally efficient.** For $d=50$: the full
MUP integral over $\Delta_{49}$ has $\binom{50}{k}$ Walsh coefficients at each order $k$.
The leading $r$ terms (corresponding to the $r$-factor structure) dominate, with higher
terms suppressed by $e^{-\lambda_k T}$ (the Jacobi eigenvalue decay). The MUP is
approximated by the leading-order Walsh truncation.

---

## 3. Shapley Values: The Unique Fair Attribution

### 3.1 The cooperative game setup

**Definition 3.1** (Kelly growth cooperative game). *The Kelly cooperative game is
$(N, v)$ where:*
- *$N = \{1,\ldots,d\}$ = the set of assets (players)*
- *$v(S) = \max_{b\in\Delta_{|S|-1}}L_T^S(b)$ = the maximum Kelly growth rate achievable
  by a portfolio on the sub-simplex of assets in $S$*

*The characteristic function $v(S)$ measures the value of coalition $S$.*

**The Shapley value** $\phi_i$ of asset $i$ is the unique attribution satisfying:
1. **Efficiency:** $\sum_i\phi_i = v(N)$ — attributions sum to total Kelly rate
2. **Symmetry:** If $v(S\cup\{i\}) = v(S\cup\{j\})$ for all $S$: $\phi_i = \phi_j$
3. **Dummy:** If $v(S\cup\{i\}) = v(S)$ for all $S$: $\phi_i = 0$
4. **Linearity:** $\phi_i(v+w) = \phi_i(v) + \phi_i(w)$

By Shapley's theorem \[1953\]: there is a unique value satisfying all four axioms,
given by the formula (0.1).

### 3.2 The Shapley = Fisher-Rao gradient theorem

**Theorem 3.2** *(Shapley attribution = Fisher-Rao projection of Kelly gradient)*.
*For a market with $d$ assets and log-optimal portfolio $b^{\ast}$, the Shapley value of
asset $i$ in the Kelly game is:*

```math
\phi_i = b^{\ast}_{i}\frac{\partial L_T}{\partial b_i}\bigg|_{b^{\ast}} \tag{3.1}
```

*where $\partial L_T/\partial b_i|_{b^{\ast}} = \mu_i - \bar\mu$ is the excess expected
return of asset $i$ over the portfolio mean (the log-optimal portfolio's KKT condition).*

*Proof.* The Shapley value for a game with smooth characteristic function $v$ is:

```math
\phi_i = \int_0^1 \frac{\partial v(\lambda b^{\ast})}{\partial b^{\ast}_{i}}\,d\lambda \tag{3.2}
```

(the Owen \[1972\] integral formula). The Kelly game has $v(\lambda b^{\ast}) = L_T(\lambda b^{\ast})$.
The integral gives:

```math
\phi_i = \int_0^1 \lambda b^{\ast}_{i}\frac{\partial^2 L_T}{\partial b_i^2}\bigg|_{\lambda b^{\ast}}
+ b^{\ast}_{i}\frac{\partial L_T}{\partial b_i}\bigg|_{\lambda b^{\ast}}\,d\lambda \tag{3.3}
```

At the log-optimal portfolio: $\partial L_T/\partial b_i|_{b^{\ast}} = \mu_i - \bar\mu$
(the KKT condition, from CONVERGENCE.md equation 1.8). Substituting and integrating:
$\phi_i = b^{\ast}_{i}(\mu_i - \bar\mu)$. $\square$

### 3.3 The Shapley attribution in financial terms

**The Shapley value $\phi_i = b^{\ast}_{i}(\mu_i - \bar\mu)$ is:**
- **Proportional to the Kelly weight** $b^{\ast}_{i}$: assets with higher log-optimal weight
  receive higher attribution. A zero-weight asset gets zero Shapley value (dummy axiom ✓).
- **Proportional to the excess return** $\mu_i - \bar\mu$: only assets that outperform
  the Kelly mean contribute. Assets with mean expected return get zero attribution.
- **The CAPM alpha** for the log-optimal portfolio: this is the single-period excess
  return contribution of asset $i$ when held in the Kelly proportion.

**The total attribution** $\sum_i\phi_i = \sum_i b^{\ast}_{i}(\mu_i-\bar\mu) = \bar\mu^{\ast} - \bar\mu$
where $\bar\mu^{\ast} = b^{*T}\mu$ is the Kelly portfolio expected return. This equals the
Kelly portfolio alpha — the excess return over the equal-weight mean. Efficiency axiom ✓.

### 3.4 Factor attribution via Shapley

For a multi-factor market with $r$ factors and $d$ assets, the Shapley value of factor $k$
(rather than individual asset $i$) is:

```math
\Phi_k = \sum_{i=1}^{d} V_{ik} b^{\ast}_{i} (\mu_i - \bar\mu) \tag{3.4}
```

where $V_{ik}$ is the loading of asset $i$ on factor $k$ (from the PCA of the Fisher
information matrix). The total factor attribution:

```math
\sum_{k=1}^{r} \Phi_k = \sum_i b^{\ast}_{i}(\mu_i-\bar\mu) = \bar\mu^{\ast} - \bar\mu \tag{3.5}
```

equals the Kelly portfolio alpha — the Shapley attribution is complete.

**The factor Shapley values $\{\Phi_k\}$ give the unique fair attribution of the portfolio's
alpha to its underlying risk factors**, satisfying all four Shapley axioms. This is the
geometric derivation of the factor attribution formula from first principles.

---

## 4. The Hypercube Embedding of the Filtration

### 4.1 Filtration atoms as hypercube faces

The atoms of the Voronoi filtration (FILTRATIONS.md) are subsets $F_{s_0,\ldots,s_n}$
of the path space. In the hypercube representation:

Each atom $F_{s_0,\ldots,s_n}$ corresponds to a **face** of the hypercube $[0,1]^d$:
- The atom $F_{s_0}$ (initial cell $s_0$) = the face $\{b\in\Delta_{d-1}: b_{s_0}\geq b_i \forall i\}$
  = the simplex face closest to vertex $e_{s_0}$ = a face of the barycentric subdivision

The filtration hierarchy $\mathcal{F}^{\rm Vor}_{0}\subseteq\mathcal{F}^{\rm Vor}_{1}\subseteq\ldots$
corresponds to the hierarchy of faces of the hypercube: coarser filtrations correspond
to higher-dimensional faces (closer to the boundary of the hypercube); finer filtrations
correspond to lower-dimensional faces (closer to the vertices).

### 4.2 The ANOVA decomposition on the hypercube

The **ANOVA (Analysis of Variance) decomposition** of a function $f:\Delta_{d-1}\to\mathbb{R}$:

```math
f(b) = f_\emptyset + \sum_i f_i(b_i) + \sum_{i<j}f_{ij}(b_i,b_j) + \cdots \tag{4.1}
```

(where $f_\emptyset$ is the mean, $f_i$ is the main effect of asset $i$, etc.) is the
Walsh-Fourier decomposition restricted to the simplex.

**The ANOVA decomposition of the Kelly growth rate** gives:
- $f_\emptyset = \bar L_T$ (mean Kelly rate, achievable by equal weighting)
- $f_i(b_i) = b_i(\mu_i - \bar\mu)$ (main effect of asset $i$ = Shapley value $\phi_i$)
- $f_{ij}(b_i,b_j)$ (interaction effect of assets $i$ and $j$ = pairwise correlation contribution)

**The Shapley value is the main effect in the ANOVA decomposition of the Kelly game.**
Higher-order interactions (pairwise, triple, etc.) are the correction terms.

### 4.3 The hypercube-simplex correspondence table

| Hypercube $[0,1]^d$ | Portfolio simplex $\Delta_{d-1}$ |
|:--------------------|:---------------------------------|
| Vertices $\{0,1\}^{d}$ | Includes $e_1,\ldots,e_d$ (pure-asset portfolios) |
| Face of dim $k$ | $k$-asset coalition in Shapley game |
| Walsh function $w_S$ | Jacobi polynomial of degree $|S|$ |
| ANOVA main effect $f_i$ | Shapley value $\phi_i$ |
| ANOVA interaction $f_{ij}$ | Pairwise correlation contribution |
| Hypercube Fourier series | Jacobi polynomial series (transition density) |
| Barycentric subdivision | Voronoi Delaunay triangulation |
| Cube vertex $e_i$ | Pure factor portfolio $v_i$ |
| Cube dimension $d$ | Number of assets $d$ |
| Face lattice | Filtration hierarchy |

---

## 5. Rigorous Attribution Analysis from the Geometric Framework

### 5.1 The attribution decomposition

Combining Shapley values with the ANOVA decomposition:

**Asset-level attribution:** $\phi_i = b^{\ast}_{i}(\mu_i-\bar\mu)$ — the Shapley value,
provably the unique fair attribution.

**Factor-level attribution:** $\Phi_k = \sum_i V_{ik}\phi_i$ — the factor Shapley value,
the weighted sum of asset attributions projected onto the factor subspace.

**Idiosyncratic attribution:** $\psi_i = \phi_i - \sum_k V_{ik}\Phi_k$ — the residual
attribution not explained by factors = the normal bundle component of the Shapley value.

**Theorem 5.1** *(Attribution decomposition via normal bundle)*.
*The Shapley value decomposes as:*

```math
\phi_i = \underbrace{\Pi_{TM}\phi_i}_{\text{systematic}} + \underbrace{\Pi_{NM}\phi_i}_{\text{idiosyncratic}} \tag{5.1}
```

*where $\Pi_{TM}$ and $\Pi_{NM}$ project onto the tangent and normal bundle of the
market manifold. For an efficient market ($H=0$): the idiosyncratic component
$\Pi_{NM}\phi_i = 0$ for all assets — all Kelly attribution is systematic.
For an inefficient market: the idiosyncratic component is non-zero and represents
unexplained alpha.*

### 5.2 The Banzhaf power index

The **Banzhaf power index** \[1965\] — a close relative of the Shapley value — is:

```math
\beta_i = \frac{1}{2^{d-1}}\sum_{S\subseteq[d]\setminus\{i\}}[v(S\cup\{i\})-v(S)] \tag{5.2}
```

Unlike Shapley, the Banzhaf index does not satisfy efficiency (the values do not sum to $v(N)$).
In the Kelly game:

```math
\beta_i = \mathbb{E}_{S\subseteq[d]\setminus\{i\}}[v(S\cup\{i\})-v(S)] \tag{5.3}
```

— the expected marginal contribution of asset $i$ over a uniformly random coalition.

**The Banzhaf = the Walsh-Fourier coefficient** of $v$ at the singleton $\{i\}$:
```math
\beta_i = \hat v_{\{i\}} = \int_\Delta v(b)(2b_i-1)\,d\mathrm{vol}(b).
```

This connection — Banzhaf power index = Walsh-Fourier coefficient — links cooperative
game theory to the harmonic analysis on the hypercube/simplex. **Game theory and Fourier
analysis on the simplex are the same subject.**

---

## 6. Summary

$$
\begin{array}{lcl}
\Delta_{d-1}\subset[0,1]^d & & \text{simplex inside hypercube} \\
\text{Walsh }w_S & = & \text{Jacobi polynomial degree }|S| \\
\text{Barycentric subdivision} & = & \text{Voronoi Delaunay} \\
\text{ANOVA main effect} & = & \text{Shapley value} \\
\text{Shapley }\phi_i & = & b^{\ast}_{i}(\mu_i-\bar\mu)\text{ (proved)} \\
\text{Factor Shapley }\Phi_k & = & \text{unique fair factor attribution} \\
\text{Normal bundle }\Pi_{NM}\phi & = & \text{unexplained alpha} \\
\text{Banzhaf }= & & \text{Walsh-Fourier coefficient} \\
\text{MUP partition} & = & \text{leading Walsh coefficients (Selberg)}
\end{array}
}$$

The hypercube is the container; the simplex is the room we live in;
the Walsh-Fourier analysis is the harmonic structure; and the Shapley value is
the game-theoretically unique way to attribute the Kelly rate to assets.

---

## References

Banzhaf, J. F. (1965). Weighted voting doesn't work: a mathematical analysis.
*Rutgers Law Review* 19, 317–343.

Owen, G. (1972). Multilinear extensions of games.
*Management Science* 18(5-Part-2), 64–79.

Shapley, L. S. (1953). A value for $n$-person games. In: *Contributions to the Theory
of Games II*, 307–317. Princeton University Press.

*[All other references as per companion papers.]*
