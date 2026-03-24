# Geospatial Indexing, Hilbert Curves, and Information Contagion
## on Market Manifolds: H3, S2, R-Trees, Local Hashing,
## and the Geometry of Financial Contagion

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.1** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
The portfolio simplex $\Delta\_{d-1}$ equipped with the Fisher-Rao metric IS a
Riemannian manifold — the same class of object that geospatial indexing systems
(Uber H3, Google S2, geohash, R-trees) are designed to index efficiently. We
develop the theory of **geospatial indexing on market manifolds**, applying these
computational geometry tools to derive new results on information flow, contagion
propagation, and local portfolio hashing.

The key connections:

**(i) H3 on the Bhattacharyya sphere.** The Bhattacharyya hemisphere $S^{d-1}\_+$ IS
a sphere — Uber's H3 hexagonal hierarchical index applies directly. At resolution
level $\ell$, the market manifold is partitioned into $7^\ell$ hexagonal cells (each
cell subdividing into 7 children). The H3 index of a portfolio $b$ is a 64-bit
integer encoding its position in the hierarchy; portfolios with similar H3 prefixes
are close in Fisher-Rao distance. The H3 hierarchy generates exactly the multi-scale
Voronoi filtration of FILTRATIONS.md.

**(ii) Hilbert curves minimise LZ complexity.** The Hilbert space-filling curve
$\mathcal{H}: [0,1] \to M^r$ is the unique continuous bijection that maximally
preserves locality — nearby points on the curve are nearby on $M$ in the Fisher-Rao
metric. When the Voronoi cell sequence is encoded along the Hilbert ordering
(rather than arbitrary ordering), the Lempel-Ziv complexity of the resulting sequence
is minimised: $c\_{\rm LZ}^{\rm Hilbert} \leq c\_{\rm LZ}^{\rm arbitrary}$ always.
The Hilbert-ordered market path is the most compressible representation of the
portfolio trajectory.

**(iii) Information propagation as diffusion on the Delaunay graph.** A news shock
affecting stock $i$ moves the portfolio from $b^{\ast}$ to $b^{\ast} + \delta e\_i$ in the
simplex. The perturbation propagates through the Delaunay graph of the Voronoi
partition at speed governed by the Jacobi spectral gap $\lambda\_1$. At time $t$
after the shock, the perturbation has spread to all Voronoi cells within
Fisher-Rao distance $\varepsilon\sqrt{t}$ of the origin cell — a heat equation
on the Delaunay graph.

**(iv) Contagion as curvature-driven flow.** In an inefficient market ($H\neq 0$),
perturbations do not propagate isotropically — they propagate faster in the
direction of $-\vec{H}$ (the mean curvature vector). The **contagion kernel** is
the heat kernel of the manifold Laplacian $e^{t\Delta\_M}$, which at short times is
approximately Gaussian in geodesic distance but is modulated by the curvature.
High-curvature regions are contagion hubs; low-curvature regions are contagion sinks.

**(v) The Federal Reserve contagion framework in geometric terms.** The Fed's
models of financial contagion (Acemoglu-Ozdaglar-Tahbaz-Salehi network contagion;
Glasserman-Young amplification; Adrian-Brunnermeier CoVaR) all assume a network
structure defined exogenously. In our framework, the contagion network IS the
Delaunay graph of the market manifold — it is endogenous, determined by the factor
structure. The systemic risk measure corresponds to the Cheeger constant $h\_M$ of
the manifold: a market with small $h\_M$ (a manifold with a thin bottleneck) has
high systemic risk — a small shock at the bottleneck can disconnect the manifold
and cause large-scale contagion.

**Keywords.** H3; S2; geohash; R-tree; Hilbert curve; Z-order; space-filling curve;
locality-sensitive hashing; information propagation; contagion; Delaunay graph;
heat kernel; Cheeger constant; systemic risk; financial network; Hawkes process;
curvature-driven flow; geodesic distance; portfolio hashing.

**MSC 2020.** 53A10, 91G10, 68P05, 05C50, 60J65, 91G20, 68Q25.

---

## 1. The Market Manifold as a Geospatial Object

### 1.1 Why geospatial methods apply

The portfolio simplex $\Delta\_{d-1}$ equipped with $g^{\mathrm{FR}}$ is a Riemannian
manifold of dimension $d-1$. The market manifold $M^r \subset \Delta\_{d-1}$ is an
$r$-dimensional Riemannian submanifold. These are precisely the objects that
geospatial indexing systems are designed to handle efficiently:

- **Uber H3:** Hierarchical hexagonal indexing on $S^2$ — applies to $S^{d-1}\_+$
- **Google S2:** Quad-tree on the cube mapped to $S^2$ — applies to $S^{d-1}\_+$
- **Geohash:** Z-order curve on $[0,1]^2$ — applies to the portfolio simplex directly
- **R-trees:** Axis-aligned bounding rectangles — applies in the Bhattacharyya coordinates
- **Hilbert curves:** Space-filling locality-preserving curves — applies on $M^r$

The market manifold is not merely *analogous* to a geospatial object — it IS one,
mapped to a sphere by the Bhattacharyya isometry $b \mapsto \sqrt{b} \in S^{d-1}\_+$.

### 1.2 The geospatial interpretation of portfolio weights

**Portfolio weights as spherical coordinates.** In the Bhattacharyya coordinates
$u = \sqrt{b} \in S^{d-1}\_+$, the portfolio weight $b\_i = u\_i^2$ is the squared
$i$-th coordinate. The Fisher-Rao metric is the standard round metric on $S^{d-1}$
(constant curvature $K=1/4$).

**For $d=3$ (three-asset market):** $u \in S^2\_+$ (positive octant of the 2-sphere).
The portfolio is literally a point on the surface of a sphere — geospatial indexing
on $S^2$ applies without modification.

**For $d=4$ (four-asset, Clifford torus market):** $u \in S^3\_+$ (positive orthant
of the 3-sphere). The Clifford torus $M \subset S^3$ is a submanifold that H3-type
indexing can address in 3D spherical coordinates.

---

## 2. Uber H3: Hierarchical Hexagonal Market Indexing

### 2.1 H3 on the Bhattacharyya sphere

H3 \[Brodsky 2018\] partitions the sphere $S^2$ into a hierarchy of hexagonal cells
(with 12 pentagonal exceptions from the icosahedron) at 16 resolution levels.
Resolution $\ell=0$: 122 base cells. Each cell subdivides into 7 at the next level,
giving $122\times 7^{\ell-1}$ cells at resolution $\ell$.

**The H3 market index.** For a three-asset portfolio $b = (b\_1,b\_2,b\_3)$ mapped
to $u = (\sqrt{b\_1},\sqrt{b\_2},\sqrt{b\_3}) \in S^2\_+$:

The H3 cell at resolution $\ell$ containing $u$ is a 64-bit integer
$\mathrm{H3}(u,\ell)$ such that:
$$\mathrm{H3}(u_1,\ell) = \mathrm{H3}(u_2,\ell) \iff d_{g^{\mathrm{FR}}}(b_1,b_2) \leq C_\ell \tag{2.1}$$
where $C\_\ell \approx \pi/(2\cdot 7^{\ell/2})$ is the cell radius at resolution $\ell$.

**The H3 hierarchy generates the multi-scale Voronoi filtration.** The atoms of
the H3 filtration at resolution $\ell$ are the H3 cells — they are exactly the
Voronoi cells of the $7^\ell$ H3 centres in the Fisher-Rao metric. The H3 hierarchy
therefore generates a filtration:
$$\mathcal{F}^{\mathrm{H3},0} \subseteq \mathcal{F}^{\mathrm{H3},1} \subseteq \ldots
\subseteq \mathcal{F}^{\mathrm{H3},15} \subseteq \mathcal{F}^M \tag{2.2}$$

At coarse resolution ($\ell=0$): 8 cells in the positive octant — the factor-level
filtration. At fine resolution ($\ell=10$): $8\times 7^9 \approx 3.2\times 10^8$ cells
— the portfolio path is resolved at $\mu$rad precision on the sphere.

### 2.2 H3 prefix equality = Fisher-Rao proximity

**Two portfolios are "H3-close" at level $\ell$** iff they share the same
H3 prefix of length $\ell$. This is equivalent to being within Fisher-Rao distance $C\_\ell$.

**Theorem 2.1** *(H3 locality)*. *For two portfolios $b\_1$, $b\_2$:*
$$\text{LCP}(\mathrm{H3}(b_1),\mathrm{H3}(b_2)) \geq \ell
\iff d_{g^{\mathrm{FR}}}(b_1,b_2) \leq C_\ell \tag{2.3}$$
*where LCP is the longest common prefix of the H3 cell IDs.*

*This gives an $O(1)$-time approximate Fisher-Rao distance computation:
$d\_{g^{\mathrm{FR}}}(b\_1,b\_2) \approx C\_{\mathrm{LCP}(b\_1,b\_2)}$ — the distance
is the resolution at which the two portfolios first disagree.*

**Practical application — portfolio similarity search:** Given a new market state
$b^{\ast}(T+1)$, find all historical states $\{b^{\ast}(t)\}\_{t \leq T}$ within Fisher-Rao
distance $\varepsilon$ in $O(\log(1/\varepsilon))$ time using the H3 prefix index.
This is the geometric nearest-neighbour problem for portfolio states, exactly the
H3 ring/disk query on the market sphere.

### 2.3 H3 resolution and information scale

Each H3 resolution level corresponds to a specific Fisher-Rao length scale:

| Resolution $\ell$ | Cell radius $C\_\ell$ | Market interpretation | Number of cells |
|:-----------------:|:--------------------:|:---------------------|:---------------:|
| 0 | $\pi/4$ | Full simplex (no structure) | 8 (on $S^2\_+$) |
| 1 | $\pi/4\sqrt{7}$ | Broad factor level | 56 |
| 2 | $\pi/4\cdot 7$ | Fine factor level | 392 |
| $r$ | $\pi/(4\cdot 7^{r/2})$ | Optimal for $r$-factor market | $8\cdot 7^r$ |
| 10 | $\approx 0.001$ rad | Near-individual-stock precision | $\sim 10^9$ |

**The optimal resolution for an $r$-factor market is $\ell = r$.** At this resolution,
each H3 cell corresponds approximately to one Voronoi cell of the $r$-factor market
manifold. Finer resolution resolves idiosyncratic structure (inside the Voronoi cells);
coarser resolution only sees systematic factor structure.

---

## 3. Google S2: Quad-Tree Decomposition

### 3.1 S2 on the portfolio sphere

Google S2 \[S2 Geometry Library\] maps $S^2$ to the six faces of a cube, applies a
quad-tree decomposition to each face, and maps back. Cells at level $\ell$ have
approximately $4^{-\ell}$ of the sphere area.

**The S2 market index** on $S^2\_+$ uses only the 3 cube faces that intersect the
positive octant. Each face is divided into $4^\ell$ cells at resolution $\ell$.

**Key advantage over H3:** S2 cells are **quadrilaterals** — aligned with the simplex
coordinate directions. For a portfolio with Voronoi cells aligned to the coordinate
axes (as for the multi-CAPM, where $M = S^r\_+$ and Voronoi cells are coordinate
simplices), S2 cells are the natural partition.

**S2 cell ID as a portfolio address.** An S2 cell ID at level 30 encodes a portfolio
$b$ with precision $\approx 1\mathrm{cm}^2$ on the Earth's surface — or equivalently,
$\approx 10^{-7}$ in portfolio weight units for $d=3$. This gives a 64-bit lossless
encoding of any portfolio to high precision.

### 3.2 The S2 hierarchy and factor decomposition

The S2 hierarchy at level $\ell$ on portfolio $S^2\_+$ partitions the market manifold
into $4^\ell$ cells, each corresponding to a specific range of factor exposures.

**At level 1** ($4$ cells for $S^2\_+$): the four "quadrant portfolios"
$(b\_1 \gtrless b^{\ast}\_1, b\_2 \gtrless b^{\ast}\_2)$ — the Clifford torus Voronoi cells.

**At level 2** ($16$ cells): each quadrant further divided into sub-quadrants by
within-group allocation — resolves the fine structure within each factor regime.

**The S2 level = the filtration depth of the Clifford torus filtration.** Each
S2 level $\ell$ corresponds to depth $\ell$ in the $\mathcal{F}^{\rm Vor}$ filtration
tree of FILTRATIONS.md Section 6.3.

---

## 4. Hilbert Curves: Locality-Preserving Portfolio Encoding

### 4.1 The Hilbert curve on the market manifold

A **Hilbert curve** $\mathcal{H}\_r: [0,1] \to M^r$ is a space-filling curve that
maps the unit interval bijectively and continuously to the $r$-dimensional market
manifold, with the locality property:

$$|s_1 - s_2| \leq \delta \implies d_{g_M}(\mathcal{H}_r(s_1), \mathcal{H}_r(s_2)) \leq C\delta^{1/r} \tag{4.1}$$

Points that are close on the Hilbert index $s \in [0,1]$ are close on the manifold.

**The Hilbert index** of a portfolio $b \in M^r$ is:

$$\mathrm{HI}(b) = \mathcal{H}_r^{-1}(b) \in [0,1] \tag{4.2}$$

— a single real number that encodes the portfolio's position on the manifold while
preserving proximity.

### 4.2 The Hilbert ordering minimises LZ complexity

**Theorem 4.1** *(Hilbert ordering minimises the prefix tree)*. *Among all
orderings of the Voronoi cells $\{0,\ldots,r\}^n$ at depth $n$, the Hilbert
ordering (cells ordered by their Hilbert index) gives the minimum LZ complexity:*

$$c_{\rm LZ}^{\mathrm{Hilbert}} = \min_{\sigma \in S_n} c_{\rm LZ}^\sigma \tag{4.3}$$

*where $\sigma$ ranges over all permutations of the cell labelling.*

*Proof sketch.* LZ complexity is minimised when consecutive phrases in the LZ parsing
are "close" to previously seen phrases — so the dictionary can reuse earlier entries.
The Hilbert ordering maximises the probability that consecutive cell transitions
(which correspond to consecutive Voronoi cells in the manifold path) produce
dictionary entries that are suffixes of previous entries. This is the locality
property of the Hilbert curve: nearby cells have similar Hilbert index prefixes,
so the prefix tree for the Hilbert-ordered path reuses branches maximally. $\square$

**Practical consequence.** When compressing the portfolio path for storage or
transmission, encoding the Voronoi cell sequence using Hilbert-ordered cell IDs
rather than arbitrary IDs reduces the compressed size by a factor of up to $r$.

### 4.3 The Hilbert curve and information revelation

The Hilbert curve index $\mathrm{HI}(b^{\ast}(t)) \in [0,1]$ is a scalar time series that
summarises the portfolio trajectory on $M^r$. Its properties:

**Binary expansion and the filtration.** The binary expansion of $\mathrm{HI}(b^{\ast}(t))$:
$$\mathrm{HI}(b^{\ast}(t)) = \sum_{k=1}^\infty b_k 2^{-k}, \qquad b_k \in \{0,1\} \tag{4.4}$$
has a remarkable property: the first $n$ bits $b\_1\cdots b\_n$ determine the depth-$n$
Hilbert cell containing $b^{\ast}(t)$ — equivalently, the depth-$n$ atom of the Hilbert filtration.

**The Hilbert filtration:**
$$\mathcal{F}^{\mathrm{HI}}_t^n = \sigma(b_1(s),\ldots,b_n(s) : s \leq t) \tag{4.5}$$
is generated by the first $n$ bits of the Hilbert index, and is equivalent to the
depth-$n$ Voronoi filtration $\mathcal{F}^{\rm Vor,n}\_t$ (by the locality correspondence
4.3). **The Hilbert curve converts the multi-dimensional filtration into a sequence of
binary decisions** — each bit of the Hilbert index is one binary split in the filtration tree.

---

## 5. R-Trees and Portfolio Range Queries

### 5.1 R-trees on the portfolio simplex

An **R-tree** \[Guttman 1984\] organises spatial objects into a tree of minimum
bounding rectangles (MBRs). For portfolio space:
- Each portfolio $b \in M^r$ is a point in $\mathbb{R}^d$ (with $\sum b\_i=1$ constraint)
- Each MBR is an axis-aligned box $[l\_1,u\_1]\times\cdots\times[l\_d,u\_d]$ in portfolio space
- The R-tree supports range queries: find all portfolios within a given MBR

**The natural MBR for portfolio space** is the Fisher-Rao ball:
$$B_{g^{\mathrm{FR}}}(b^{\ast}, \varepsilon) = \{b \in M : d_{g^{\mathrm{FR}}}(b, b^{\ast}) \leq \varepsilon\} \tag{5.1}$$

In simplex coordinates, this is an **ellipsoid** (not an axis-aligned box) — the
Fisher-Rao ball is elongated in directions of small portfolio weight $b\_i$ and
compressed in directions of large weight. The natural R-tree for portfolio space
should use Fisher-Rao balls as bounding regions rather than axis-aligned boxes.

**The Fisher-Rao R-tree.** Replace the axis-aligned MBR with the ellipsoidal
Fisher-Rao ball. The tree construction is identical to the standard R-tree but
with the Fisher-Rao distance function:

$$d_{g^{\mathrm{FR}}}(b_1,b_2) = 2\arccos\!\left(\sum_i\sqrt{b_{1,i}b_{2,i}}\right) \tag{5.2}$$

(the Bhattacharyya distance — the geodesic on $S^{d-1}$).

**Portfolio nearest-neighbour search.** For a new market state $b\_{\rm new}$, the
Fisher-Rao R-tree finds the $k$ nearest historical portfolio states in $O(\log T)$
expected time. This is the **market state nearest-neighbour problem** — finding
historical market environments most similar to the current one in Fisher-Rao geometry.

### 5.2 Range queries and regime detection

An R-tree range query on the market manifold:
$$Q_\varepsilon(b^{\ast}) = \{t : b^{\ast}(t) \in B_{g^{\mathrm{FR}}}(b^{\ast}, \varepsilon)\} \tag{5.3}$$

returns all times when the portfolio was within Fisher-Rao distance $\varepsilon$ of $b^{\ast}$.
The expected query time is $O(T^\gamma)$ for the R-tree (with $\gamma < 1$ depending
on the dimensionality and clustering structure).

**Regime detection via R-tree clustering.** The market manifold has a natural
cluster structure — efficient periods cluster near $b^{\ast}$ (small Fisher-Rao radius),
while crises push the portfolio toward the boundary $\partial\Delta$ (large Fisher-Rao
radius). An R-tree density query detects regimes:

- **Dense cluster near $b^{\ast}$**: normal efficient market
- **Sparse region near $\partial\Delta$**: crisis (portfolio concentrating in safe assets)
- **Multi-modal density** (two clusters of comparable size): regime transition

---

## 6. Local Hashing: Locality-Sensitive Hashing on $M$

### 6.1 LSH for the Fisher-Rao metric

**Locality-Sensitive Hashing (LSH)** \[Indyk-Motwani 1998\] maps points to hash
buckets such that nearby points hash to the same bucket with high probability.
For the Fisher-Rao metric:

$$\mathrm{LSH}_{g^{\mathrm{FR}}}(b) = \lfloor (\vec{v}\cdot\sqrt{b} + b) / w \rfloor \tag{6.1}$$

where $\vec{v} \in S^{d-1}$ is a random hyperplane normal and $w > 0$ is the bucket
width. This is standard spherical LSH applied to the Bhattacharyya coordinates $\sqrt{b}$.

**The collision probability** for two portfolios $b\_1, b\_2$ is:

$$\mathbb{P}(\mathrm{LSH}(b_1) = \mathrm{LSH}(b_2)) = 1 - \frac{d_{g^{\mathrm{FR}}}(b_1,b_2)}{\pi/2} + O(d^2_{g^{\mathrm{FR}}}) \tag{6.2}$$

Nearby portfolios (small Fisher-Rao distance) collide with high probability;
distant portfolios collide with low probability.

**Portfolio fingerprinting.** The LSH of the current portfolio $b^{\ast}(t)$ is a compact
"fingerprint" that can be compared across different markets, time periods, or asset
universes. Two markets are "in similar states" iff their portfolio fingerprints match.

### 6.2 The geohash encoding of portfolios

The **geohash** of a portfolio $b \in \Delta\_{d-1}$ is:

$$\mathrm{GH}(b) = \mathrm{H3}(\sqrt{b}, \ell) \tag{6.3}$$

— the H3 cell ID of the Bhattacharyya image at resolution $\ell$. This is a compact
string (8–16 characters) that identifies the portfolio to precision $C\_\ell$.

**Geohash proximity:** $\mathrm{GH}(b\_1)$ and $\mathrm{GH}(b\_2)$ share a prefix of
length $k$ iff $d\_{g^{\mathrm{FR}}}(b\_1,b\_2) \lesssim C\_k$. This is the portfolio
space analogue of "same city" (short prefix) vs "same street address" (long prefix).

---

## 7. Information Propagation on the Delaunay Graph

### 7.1 The contagion model

A shock to stock $i$ at time $t\_0$ moves the log-optimal portfolio:
$$b^{\ast}(t_0^+) = b^{\ast}(t_0^-) + \delta_i e_i, \qquad \delta_i = \frac{\partial b^{\ast}}{\partial x_i}\Delta x_i \tag{7.1}$$

This perturbation moves the portfolio from its current Voronoi cell to an adjacent
cell (if $\delta\_i$ is large enough to cross a Voronoi boundary). The perturbation
then propagates through the Delaunay graph via the **manifold heat equation**:

$$\frac{\partial}{\partial t}\delta b(b,t) = \varepsilon^2\Delta_M\,\delta b(b,t) \tag{7.2}$$

with initial condition $\delta b(b,0) = \delta\_i e\_i\cdot\mathbf{1}\_{b=b^{\ast}}$.

### 7.2 The contagion kernel

**Theorem 7.1** *(Contagion kernel on the market manifold)*. *The solution to (7.2)
is the manifold heat kernel:*

$$\delta b(b,t) = \int_M p_t(b,b')\,\delta b(b',0)\,d\mathrm{vol}_M(b') \tag{7.3}$$

*where $p\_t(b,b')$ is the heat kernel on $(M^r, g\_M)$ from MARKET\_PROCESSES.*

*For the CAPM ($M=S^1\_+$, Jacobi process): the contagion kernel is the Jacobi
polynomial series (MARKET\_PROCESSES equation 2.3).*

*For the Clifford torus ($M=T^2$): the contagion kernel is the theta function
$\vartheta\_3$ (MARKET\_PROCESSES equation 4.4).*

*For the hyperbolic market ($M=\mathbb{H}^2$): the contagion kernel is the McKean
kernel (MARKET\_PROCESSES equation 5.7).*

*The contagion speed is $\varepsilon = 1/\sqrt{T}$ — one observation worth of
information diffuses at rate $1/T$ per period.*

### 7.3 Multi-hop contagion and the graph Laplacian

On the Delaunay graph $\mathcal{D}(M)$ (the discrete skeleton of the market
manifold), the graph Laplacian is:

$$L_{kl}^{\mathcal{D}} = \begin{cases}
-w_{kl} & \text{if } k\text{ and }l\text{ are adjacent} \\
\sum_{j\sim k}w_{kj} & \text{if }k=l \\
0 & \text{otherwise}
\end{cases} \tag{7.4}$$

where $w\_{kl} = \pi\_k\pi\_l/d\_{g^{\mathrm{FR}}}(v\_k,v\_l)$ (transition weight
proportional to cell volumes and inversely proportional to Fisher-Rao distance).

**The discrete contagion equation:**

$$\frac{d}{dt}\boldsymbol{\delta}(t) = -L^{\mathcal{D}}\boldsymbol{\delta}(t) \tag{7.5}$$

where $\boldsymbol{\delta}(t) \in \mathbb{R}^{r+1}$ is the shock at each Voronoi cell.

**Solution:**

$$\boldsymbol{\delta}(t) = e^{-L^{\mathcal{D}}t}\boldsymbol{\delta}(0)
= \sum_{k=0}^r e^{-\lambda_k^{\mathcal{D}} t}\langle\boldsymbol{\delta}(0),\phi_k\rangle\phi_k \tag{7.6}$$

where $\{\lambda\_k^{\mathcal{D}}, \phi\_k\}$ are the eigenvalues and eigenvectors of
$L^{\mathcal{D}}$.

**The spectral gap $\lambda\_1^{\mathcal{D}}$** is the slowest contagion decay rate.
A market with small $\lambda\_1^{\mathcal{D}}$ (thin bottleneck in the Delaunay graph)
has slow contagion decay — shocks persist for a long time. By the Cheeger inequality
(FOKKER\_PLANCK\_CFD Theorem 6.1):

$$\frac{h_M^2}{4} \leq \lambda_1^{\mathcal{D}} \leq 2h_M \tag{7.7}$$

Small Cheeger constant $h\_M$ = narrow bottleneck in the market manifold = slow contagion
decay = high systemic risk.

### 7.4 Contagion hubs and sinks

**Contagion hubs** are Voronoi cells with high centrality in the Delaunay graph —
they have many neighbours and high transition probabilities. In the eigenvector
centrality decomposition:

$$\text{Centrality}(k) = \langle\phi_1, e_k\rangle^2 \tag{7.8}$$

(the squared loading of cell $k$ on the first non-trivial eigenvector of $L^{\mathcal{D}}$).

For the CAPM ($d=2$, 2-cell Delaunay graph): equal centrality for both cells.

For the Clifford torus ($d=4$, 4-cell graph with the torus adjacency matrix 3.7):
the first non-trivial eigenvector of $A^{T^2}$ has equal loadings on all 4 cells
(by symmetry) — the Clifford torus has no contagion hubs. All cells are equally central.

For an asymmetric Lawson surface: the cell containing $b^{\ast}$ has higher centrality
(it is closer to more cells) — the **log-optimal portfolio is the contagion hub of
an asymmetric market**.

---

## 8. The Federal Reserve Contagion Framework in Geometric Terms

### 8.1 The Fed's financial network models

The Federal Reserve's literature on financial contagion
\[see e.g. Acemoglu-Ozdaglar-Tahbaz-Salehi 2015; Glasserman-Young 2015;
Adrian-Brunnermeier 2016 (CoVaR)\] models the financial system as a network $G = (V,E)$
where nodes are financial institutions and edges are exposure relationships.
Contagion occurs when a shocked institution $i$ transmits losses to its counterparties.

**The key limitation:** The network is defined exogenously (from balance sheet data,
interbank exposures, etc.). The geometry of the contagion process is not derived from
first principles.

### 8.2 The endogenous contagion network from market geometry

**Theorem 8.1** *(The contagion network is the Delaunay graph)*. *For a market
on manifold $M^r$ with Voronoi partition $\{A\_k\}$:*

*(i) Institutions in the same Voronoi cell are maximally exposed — they hold
portfolios close in Fisher-Rao distance and are affected by the same factor shocks.*

*(ii) Institutions in adjacent Voronoi cells (connected in the Delaunay graph) are
directly exposed via the contagion kernel (7.3) — a shock in $A\_k$ propagates
to $A\_l$ at rate $w\_{kl}$ if $(A\_k,A\_l)$ are Delaunay adjacent.*

*(iii) Institutions in non-adjacent cells are indirectly exposed — shocks reach them
via multi-hop propagation through the Delaunay graph.*

*The contagion network is the Delaunay graph $\mathcal{D}(M)$ — endogenously determined
by the factor structure of the market.*

**Economic content:** Two firms are exposed to each other's shocks iff they hold
portfolios in adjacent Voronoi cells of the market manifold. The exposure strength
is the Delaunay edge weight $w\_{kl}$ — which is the Fisher-Rao distance (how
easily the optimal portfolio transitions between their factor regimes).

### 8.3 CoVaR in geometric language

**Adrian-Brunnermeier's CoVaR** \[2016\] defines the systemic contribution of
institution $i$ as:
$$\Delta\mathrm{CoVaR}^{j|i} = \mathrm{VaR}^j|\mathrm{distress}(i) - \mathrm{VaR}^j|\mathrm{median}(i) \tag{8.1}$$

In geometric terms: institution $i$ is in distress when $b^{\ast}\_i \to \partial\Delta$
(portfolio weight approaching zero — the Feller boundary). The VaR of institution $j$
given $i$'s distress equals the VaR under the conditional distribution given that
$b^{\ast}\_i(t)$ is in the crisis cell $A^{\rm crisis} = B\_{g^{\mathrm{FR}}}(\partial\Delta, \varepsilon)$:

$$\Delta\mathrm{CoVaR}^{j|i}_{\rm geom} = \mathrm{VaR}^j\!\left(\,\cdot\, | b^{\ast}_i \in A^{\rm crisis}\right) - \mathrm{VaR}^j\!\left(\,\cdot\, | b^{\ast}_i \in A^{\ast}_i\right) \tag{8.2}$$

The geometric CoVaR is large when $A^{\rm crisis}$ is close to $A^{\ast}\_j$ in the
Delaunay graph — when institutions $i$ and $j$ are in adjacent Voronoi cells.
**Two institutions have high mutual CoVaR iff they are Delaunay neighbours.**

### 8.4 Cheeger constant = systemic risk measure

**Theorem 8.2** *(Systemic risk = reciprocal Cheeger constant)*.

*Define the systemic risk of a market with manifold $M$ as:*

$$\mathcal{SR}(M) = \frac{1}{h_M} = \frac{\mathrm{vol}(M)}{\min_{S\subset M}\frac{|\partial S|}{\min(|S|,|M\setminus S|)}} \tag{8.3}$$

*The systemic risk $\mathcal{SR}(M)$ satisfies:*

*(i) $\mathcal{SR}(M) \leq 2/\lambda\_1(L\_M)$ (from the Cheeger inequality).*

*(ii) $\mathcal{SR}$ increases as the market manifold develops a bottleneck (thin neck
connecting two lobes of the manifold — the "dumbbell" geometry corresponding to a
bimodal factor structure).*

*(iii) A market crisis corresponds to MCF creating a bottleneck: as mean curvature
flow shrinks the market manifold, thin necks develop before the manifold pinches off,
maximally increasing systemic risk just before the critical point.*

*(iv) The spectral gap $\lambda\_1$ and the Cheeger constant $h\_M$ both collapse to
zero at the crisis point — the contagion becomes system-wide.*

*Proof.* (i) follows from the Cheeger inequality. (ii) follows from the definition
of $h\_M$ — a bottleneck minimises $|\partial S|/\min(|S|,|M\setminus S|)$. (iii) follows
from Huisken's monotonicity formula: MCF decreases the volume at rate proportional
to $\int H^2$, but necks (high curvature) shrink faster, creating the dumbbell shape.
(iv) At the neck pinch-off, $h\_M\to 0$ and $\lambda\_1\to 0$. $\square$

**This is the geometric reformulation of "too interconnected to fail":** a market
with small Cheeger constant has a thin bottleneck separating two large groups of
institutions — a shock in one group can cross the bottleneck and infect the other.
The Cheeger constant measures the width of this bottleneck in the portfolio space.

---

## 9. Hawkes Processes on the Delaunay Graph

### 9.1 Self-exciting contagion

Real financial shocks are self-exciting: a large move in stock $A$ tends to trigger
further large moves in correlated stocks. The **Hawkes process** \[Hawkes 1971\] on
the Delaunay graph $\mathcal{D}(M)$ models this:

$$\lambda_k(t) = \mu_k + \sum_{l: (k,l)\in\mathcal{D}}\int_{-\infty}^t \phi_{kl}(t-s)\,dN_l(s) \tag{9.1}$$

where $\lambda\_k(t)$ is the intensity of shocks to Voronoi cell $k$, $\mu\_k$ is the
baseline intensity, $\phi\_{kl}(t)$ is the excitation kernel from cell $l$ to cell $k$,
and $N\_l(s)$ is the counting process of shocks to cell $l$.

**The natural excitation kernel** from the market geometry is the manifold heat kernel:

$$\phi_{kl}(t) = \alpha_{kl}\,p_t(v_k, v_l) \tag{9.2}$$

where $p\_t(v\_k,v\_l)$ is the heat kernel evaluated at the Voronoi cell centres
($v\_k, v\_l$ are the centres) and $\alpha\_{kl}$ scales the excitation strength.

**Theorem 9.1** *(Hawkes criticality and market efficiency)*. *The Hawkes process
(9.1) on the Delaunay graph is:*

*(i) Subcritical (shocks die out) iff $\rho(A\_{\rm Hawkes}) < 1$ where
$A\_{\rm Hawkes,kl} = \int\_0^\infty \phi\_{kl}(t)\,dt = \alpha\_{kl}\,G(v\_k,v\_l)$
and $G$ is the Green's function of $-\Delta\_M$.*

*(ii) Critical iff $\rho(A\_{\rm Hawkes}) = 1$ — the Hawkes process is at criticality
iff the excitation strength exactly equals the spectral gap $\lambda\_1$ of the manifold
Laplacian.*

*(iii) For the efficient market: $G(v\_k,v\_l) = $ (constant at the spectral gap)
and the Hawkes process is naturally at criticality.*

The efficient market sits at the critical point of the Hawkes process — consistent
with the RG criticality of RENORMALIZATION.md. The efficient market is not just a
martingale; it is a **critical self-exciting process** where excitation and damping
exactly balance.

---

## 10. Information Flow and the Geospatial Hierarchy

### 10.1 The information flow rate

**Definition 10.1** (Information flow rate). *The information flow rate from
Voronoi cell $A\_k$ to $A\_l$ at time $t$ is:*

$$I_{kl}(t) = w_{kl}\!\left|p_{b^{\ast}}(A_l|A_k) - \pi_l\right| \tag{10.1}$$

*where $p\_{b^{\ast}}(A\_l|A\_k)$ is the transition probability from $A\_k$ to $A\_l$
and $\pi\_l$ is the stationary probability of cell $A\_l$.
This measures how much the market's current state in cell $A\_k$ changes our
estimate of the probability of next being in cell $A\_l$.*

The information flow rate is zero at stationarity (efficient market, uniform
distribution) and positive when the market is away from stationarity.

**The total information flow rate:**

$$I_{\rm total}(t) = \sum_{(k,l)\in\mathcal{D}} I_{kl}(t)
= D_{\rm KL}(p_{b^{\ast}}(\cdot|\mathcal{F}^{\rm Vor}_t) \| \pi) \tag{10.2}$$

— the KL divergence between the current conditional distribution and the stationary
distribution. This is zero at the efficient market equilibrium and positive during
information events.

### 10.2 The H3 hierarchy and multi-scale information

At H3 resolution $\ell$, the information flow rate $I\_{\rm total}^\ell(t)$ captures
shocks at scale $C\_\ell$. The **multi-scale information flow vector**:

$$\mathbf{I}(t) = (I_{\rm total}^0(t), I_{\rm total}^1(t), \ldots, I_{\rm total}^{15}(t)) \tag{10.3}$$

characterises the information event at each scale simultaneously.

**News affects different scales:**
- Macroeconomic news (Fed announcement): affects all scales simultaneously — large
  $I^\ell$ for all $\ell$. The H3 index changes at every resolution level.
- Company-specific news: affects only fine-scale cells — large $I^\ell$ only for
  large $\ell$. The H3 index changes only at the finest resolution levels.
- Factor rotation: affects medium-scale cells — large $I^\ell$ for $\ell \approx r$.

The **news scale classifier**: a news event at time $t$ is classified as
systematic (factor-level), semi-systematic, or idiosyncratic by the first
H3 resolution level $\ell^{\ast}$ at which $I^\ell(t)$ is significantly elevated.

---

## 11. Putting It Together: The Complete Geospatial Architecture

```
Portfolio space ∆_{d-1}
         │
         ▼  Bhattacharyya: b → √b
Sphere S^{d-1}_+
         │
    ┌────┴─────────────────────┐
    │                          │
    ▼ H3 hierarchical          ▼ S2 quad-tree
H3 cell ID (64-bit)         S2 cell ID (64-bit)
  Resolution ℓ = 0..15        Level ℓ = 0..30
  7^ℓ cells                  4^ℓ cells
         │                          │
         └────────┬─────────────────┘
                  │
                  ▼  Hilbert index 𝓗_r
        Scalar HI(b) ∈ [0,1]
        One-number portfolio address
        Locality-preserving
                  │
         ┌────────┴──────────────┐
         │                       │
         ▼                       ▼
    Voronoi cells           LZ prefix tree
    (r+1 cells)             (filtration atoms)
         │                       │
         ▼                       ▼
    Delaunay graph          Contagion kernel
    𝒟(M) = {A_kl}           p_t(v_k, v_l)
         │                       │
    ┌────┴─────────────┐         │
    │                  │         │
    ▼                  ▼         ▼
Cheeger h_M        Hawkes      Multi-scale
= systemic risk    process     info flow
= contagion rate   criticality  I^ℓ(t)
```

---

## References

Acemoglu, D., Ozdaglar, A., and Tahbaz-Salehi, A. (2015). Systemic risk and stability
in financial networks. *American Economic Review* 105(2), 564–608.

Adrian, T. and Brunnermeier, M. K. (2016). CoVaR.
*American Economic Review* 106(7), 1705–1741.

Brodsky, I. (2018). H3: Uber's hexagonal hierarchical spatial index.
*Uber Engineering Blog.* Available at: eng.uber.com/h3.

Guttman, A. (1984). R-trees: a dynamic index structure for spatial searching.
*ACM SIGMOD Record* 14(2), 47–57.

Glasserman, P. and Young, H. P. (2015). How likely is contagion in financial networks?
*Journal of Banking and Finance* 50, 383–399.

Hawkes, A. G. (1971). Spectra of some self-exciting and mutually exciting point processes.
*Biometrika* 58(1), 83–90.

Indyk, P. and Motwani, R. (1998). Approximate nearest neighbors: towards removing the
curse of dimensionality. *STOC 1998*, 604–613.

S2 Geometry Library. Google. Available at: s2geometry.io.

*[All other references as per companion papers.]*

---

### Connections to Other Papers

The percolation threshold $p_c$ on the Delaunay graph (GRASSBERGER\_PERCOLATION\_GENERATING.md) and the Hawkes process criticality condition $\rho(A_{\rm Hawkes}) = 1$ (Section 5 above) should be related: both measure the threshold at which local shocks become systemic. Specifically, $p_c \approx h_M$ (the Cheeger constant) and Hawkes criticality occurs when the spectral radius of the excitation kernel hits 1. These two thresholds should coincide on the Delaunay graph of the market manifold, giving a single geometric criterion for systemic risk (Conjecture C30).
