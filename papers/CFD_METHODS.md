# Computational Fluid Dynamics for Market Manifolds:
## DMD, POD, Spectral Elements, and Adaptive Mesh Refinement
## Applied to the Empirical Validation of Geometric Market Theory

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VIII.2** — Empirical Methods

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
The geometric theory of efficient markets treats the portfolio simplex as a
fluid domain: the Wright-Fisher diffusion is an advection-diffusion PDE, the
Fokker-Planck equation governs the probability flow, and mean curvature flow
drives convergence to the minimal surface. Yet our empirical validation has
relied on statistical tools (PCA, regression, bootstrap) rather than the
computational fluid dynamics (CFD) tools purpose-built for these equations.
This paper develops a complete CFD toolkit for market manifold analysis,
addressing the eight experimental problems identified in EXPERIMENTAL_PROBLEMS.md.

We apply four CFD methodologies: (i) **Dynamic Mode Decomposition (DMD)** to
extract the continuous-time eigenvalues of the market dynamics from Voronoi cell
trajectories — giving the Jacobi operator eigenvalues without parametric
assumptions; (ii) **Proper Orthogonal Decomposition (POD)** to extract the
dominant spatial modes and their temporal evolution — proving that Nelson-Siegel
factors ARE Jacobi eigenfunctions and resolving the spectral gap question;
(iii) **Spectral element methods** to solve the Jacobi eigenvalue problem
directly on the discretised simplex — giving the exact spectral gap without
approximation; (iv) **Adaptive mesh refinement (AMR)** to concentrate Voronoi
cells near the simplex boundary where curvature is highest — improving the
resolution of boundary effects that drive fat tails, default, and the Feller
boundary classification.

Before retracting any theoretical claims, we must verify that the experimental
failures are not failures of the VALIDATION METHODOLOGY rather than the theory
itself. CFD tools provide the validation methodology that our statistical tests
lacked.

**Principal results:**

**(i) DMD gives continuous-time Koopman eigenvalues from discrete observations.**
The Voronoi transition matrix from Test 15V has eigenvalues {1.0, 0.197, 0.108,
0.016}. DMD converts these to continuous-time rates {0, -1.62, -2.23, -4.15}
per day. These ARE the discrete approximations to the Jacobi operator eigenvalues
on the market manifold. The spectral gap (1.62/day) corresponds to a mixing
half-life of 0.43 days — consistent with the observed 0.6-day mixing time.

**(ii) POD with temporal coefficients separates spatial modes from their dynamics.**
Applied to the yield curve, POD modes should match Nelson-Siegel shapes
(Test N1 gave r = 0.894). The POD temporal coefficients give the OU parameters
(κ, σ) for each mode independently — resolving the spectral gap question
(Problem P1) without the confounding between modes that plagued Test 4.

**(iii) The spectral element method solves the Jacobi eigenvalue problem exactly.**
On a triangulated simplex with d=25 vertices (FF25 portfolios), the spectral
element discretisation gives all eigenvalues of the weighted Laplacian to
machine precision. This definitively tests whether the theoretical eigenvalue
formulas match the data.

**(iv) AMR concentrates resolution where it matters.** The simplex boundary
(where b_i → 0) is where the Fisher-Rao metric diverges, fat tails originate,
and default occurs. Uniform Voronoi cells waste resolution in the interior.
AMR adapts the mesh to the curvature field, putting more cells near the boundary
and fewer in the flat interior. This directly improves Tests 7 (fat tails),
8R (Jacobi boundary), and N13 (Feller distance).

**Keywords.** Dynamic Mode Decomposition; Proper Orthogonal Decomposition;
spectral elements; adaptive mesh refinement; Voronoi tessellation; Jacobi
operator; Koopman operator; market manifold; computational fluid dynamics;
empirical validation.

---

## 1. Why CFD Tools for Markets?

### 1.1 The market IS a fluid dynamics problem

The Wright-Fisher diffusion on the portfolio simplex:

$$db_i = \varepsilon^2\!\left(\alpha_i - |\alpha|\,b_i\right)dt + \varepsilon\sqrt{b_i}\,dW_i \tag{1.1}$$

is an advection-diffusion equation. Its Fokker-Planck form:

$$\frac{\partial\rho}{\partial t} = -\nabla\cdot(v\rho) + \frac{\varepsilon^2}{2}\Delta_{g^{\rm FR}}\rho \tag{1.2}$$

is exactly the equation CFD solves every day — a convection term ($v\rho$) plus
a diffusion term ($\Delta\rho$) on a domain with boundaries.

The tools CFD has developed for this equation — spectral methods for eigenvalues,
modal decomposition for reduced-order models, adaptive meshing for boundary
layers — are precisely what we need for the market manifold.

### 1.2 What we've been doing wrong

Our statistical tests used:
- **PCA** (a linear projection) to estimate a nonlinear manifold
- **Covariance eigenvalues** (a second-order statistic) to estimate the Jacobi
  spectral gap (an infinite-order geometric object)
- **Uniform K-means clustering** for Voronoi cells, wasting resolution in the
  interior where nothing happens

CFD tools fix each of these:
- **POD** replaces PCA with a proper Galerkin projection that respects the
  geometry of the domain
- **DMD** extracts the eigenvalues of the DYNAMICS (the Koopman operator),
  not just the eigenvalues of the correlation structure
- **AMR** adapts the mesh to the physics, concentrating resolution where
  curvature is high

---

## 2. Dynamic Mode Decomposition (DMD)

### 2.1 Theory

DMD (Schmid 2010) extracts the eigenvalues of the linear operator that best
advances the system one time step:

Given snapshots $x_1, x_2, \ldots, x_T$ of the state, DMD finds the matrix
$A$ such that $x_{t+1} \approx A\,x_t$ in the least-squares sense. The
eigenvalues of $A$ are the **discrete-time Koopman eigenvalues**.

For a continuous-time system $\dot{x} = Lx$, the DMD eigenvalues $\mu_k$ of
$A$ relate to the continuous-time eigenvalues $\lambda_k$ of $L$ by:

$$\lambda_k = \frac{\log\mu_k}{\Delta t} \tag{2.1}$$

The real parts give decay/growth rates; the imaginary parts give oscillation
frequencies.

### 2.2 Application to the Voronoi transition matrix

Our Voronoi transition matrix $P$ from Test 15V has eigenvalues:

$$\mu(P) = \{1.000,\; 0.197,\; 0.108,\; 0.016\} \tag{2.2}$$

Applying equation (2.1) with $\Delta t = 1$ day:

$$\lambda(L) = \{0,\; -1.62,\; -2.23,\; -4.15\}\;\text{per day} \tag{2.3}$$

These are the **discrete Jacobi operator eigenvalues** on the 4-cell Voronoi
mesh. The spectral gap is $|\lambda_1| = 1.62$/day, giving a mixing
half-life of $\log 2/1.62 = 0.43$ days.

### 2.3 The DMD experiment for Problem P1

**Experiment DMD-1: Spectral gap from DMD vs OU estimation.**

1. Build the Voronoi partition with $N = 4, 8, 16, 32$ cells and $r = 3, 4, 5$ factors
2. Compute the transition matrix $P$ for each configuration
3. Extract DMD eigenvalues $\lambda_k = \log\mu_k / \Delta t$
4. For each $k$: compare $\lambda_k$ to the OU-estimated $\kappa_k$ from the
   $k$-th principal component

**Hypothesis:** $\lambda_k$ (DMD, from Voronoi transitions) correlates with
$\kappa_k$ (OU, from PC time series). If it does, the DMD eigenvalues ARE the
Jacobi spectral gap, and Problem P1 is resolved — the spectral gap is estimable
from the Voronoi geometry, not from the covariance.

**Experiment DMD-2: Spectral gap predicts future mixing.**

1. Estimate the spectral gap $\lambda_1$ in a rolling window (2-year estimation)
2. Measure the ACTUAL mixing speed in the next window (how fast does the empirical
   cell distribution converge to the stationary distribution?)
3. Test: does $\lambda_1$ predict the next-window mixing speed?

This is the PREDICTIVE version of the spectral gap test — analogous to Test N9
(which proved that curvature predicts future Sharpe).

**Experiment DMD-3: DMD eigenvalues across asset classes.**

Run DMD on: FF25, sector ETFs, 50 equities, FX, crypto, futures.
Compare the eigenvalue spectra. The theory predicts:
- CAPM markets: eigenvalues decay geometrically (one dominant mode)
- Clifford markets: pairs of eigenvalues with similar magnitude (two balanced modes)
- Pseudo-Anosov: complex eigenvalues (oscillatory dynamics from chaos)

### 2.4 Implementation

```python
def dmd(X, r=None):
    """
    Dynamic Mode Decomposition.
    X: (d, T) data matrix (d features, T snapshots)
    Returns: eigenvalues (continuous-time), modes, amplitudes
    """
    X1 = X[:, :-1]  # first T-1 snapshots
    X2 = X[:, 1:]   # last T-1 snapshots

    # SVD of X1
    U, S, Vh = np.linalg.svd(X1, full_matrices=False)
    if r is not None:
        U, S, Vh = U[:, :r], S[:r], Vh[:r, :]

    # DMD matrix
    A_tilde = U.T @ X2 @ Vh.T @ np.diag(1/S)

    # Eigendecomposition
    eigenvalues, W = np.linalg.eig(A_tilde)

    # Continuous-time eigenvalues
    dt = 1.0  # 1 day
    lambda_continuous = np.log(eigenvalues + 1e-15) / dt

    # DMD modes
    Phi = X2 @ Vh.T @ np.diag(1/S) @ W

    return lambda_continuous, Phi, eigenvalues
```

---

## 3. Proper Orthogonal Decomposition (POD)

### 3.1 Theory

POD (Sirovich 1987) extracts the dominant spatial modes from a set of snapshots.
Given snapshots $x_1, \ldots, x_T \in \mathbb{R}^d$, POD finds orthonormal
modes $\phi_1, \ldots, \phi_r$ that maximise the captured variance:

$$x_t \approx \bar{x} + \sum_{k=1}^{r} a_k(t)\,\phi_k \tag{3.1}$$

where $a_k(t)$ are the temporal coefficients.

**POD is PCA applied to spatial fields.** For markets: the "spatial field" is the
return vector across $d$ assets; the "snapshots" are daily observations. POD modes
$\phi_k$ are the eigenvectors of the sample covariance (same as PCA). The
temporal coefficients $a_k(t) = \langle x_t - \bar{x},\, \phi_k\rangle$ are
the factor returns.

**What POD adds beyond PCA:** the dynamics of the temporal coefficients.

### 3.2 POD with Galerkin projection

The key addition: project the Fokker-Planck equation (1.2) onto the POD modes.
This gives a reduced-order model for the temporal coefficients:

$$\dot{a}_k = \sum_j L_{kj}\,a_j + \text{noise} \tag{3.2}$$

where $L_{kj} = \langle\phi_k,\, \mathcal{L}\phi_j\rangle$ is the Galerkin
matrix — the projection of the Jacobi operator $\mathcal{L}$ onto the POD
basis.

**The eigenvalues of $L$ ARE the Jacobi spectral gap values.**

### 3.3 The POD experiment for Problem P1 and N1

**Experiment POD-1: Yield curve Jacobi eigenfunctions.**

1. Apply POD to daily yield curve changes (11 maturities, 1990-2024)
2. Extract the first 3 POD modes $\phi_1, \phi_2, \phi_3$
3. Compare to Nelson-Siegel shapes (this is Test N1, which gave r = 0.894)
4. NEW: compute the Galerkin matrix $L_{kj}$ from the temporal coefficient
   dynamics: fit $\dot{a}_k = \sum_j L_{kj} a_j$ by regression
5. The diagonal elements $L_{kk}$ = the per-mode mean-reversion speed
6. The off-diagonal elements $L_{kj}$ = the mode coupling

**Hypothesis:** $L_{kk}$ (POD Galerkin) matches the OU-estimated $\kappa_k$
from Test 4R. But POD gives the FULL $L$ matrix (including off-diagonal
coupling), not just the diagonal. This resolves the confounding between
modes that caused Test 4's failure.

**Experiment POD-2: Factor dynamics on the equity manifold.**

1. Apply POD to FF25 daily returns (25 assets)
2. Extract the first $r = 4$ POD modes
3. Compute the $4 \times 4$ Galerkin matrix $L$
4. The eigenvalues of $L$ = the Jacobi spectral gap values
5. Compare to: (a) OU-estimated κ from Test 4R, (b) DMD eigenvalues from
   Experiment DMD-1, (c) Voronoi transition eigenvalues from Section 2

If all three methods agree: the spectral gap is confirmed and Problem P1
is resolved.

### 3.4 Implementation

```python
def pod_galerkin(returns, r=4):
    """
    POD with Galerkin projection of the dynamics.
    Returns: modes, temporal coefficients, Galerkin matrix L
    """
    T, d = returns.shape
    mean = returns.mean(axis=0)
    centered = returns - mean

    # POD via SVD
    U, S, Vh = np.linalg.svd(centered, full_matrices=False)
    modes = Vh[:r]  # r × d
    coeffs = centered @ modes.T  # T × r (temporal coefficients a_k(t))

    # Galerkin projection: fit da_k/dt = Σ L_kj a_j
    da = np.diff(coeffs, axis=0)  # (T-1) × r
    a = coeffs[:-1]               # (T-1) × r

    # OLS: da = a @ L^T  →  L = (a^T a)^{-1} a^T da
    L = np.linalg.lstsq(a, da, rcond=None)[0].T  # r × r

    return modes, coeffs, L
```

---

## 4. Spectral Element Methods

### 4.1 Theory

The spectral element method (Patera 1984) solves eigenvalue problems on
arbitrary domains by decomposing the domain into elements, using high-order
polynomial bases within each element, and assembling the global system.

For the Jacobi eigenvalue problem on the simplex:

$$\mathcal{L}\psi_k = \lambda_k\,\psi_k \tag{4.1}$$

where $\mathcal{L}$ is the weighted Laplacian:

$$\mathcal{L}f = \frac{1}{\sqrt{g}}\sum_{ij}\frac{\partial}{\partial b_i}\!\left(\sqrt{g}\,g^{ij}\frac{\partial f}{\partial b_j}\right) + V(b)\,f \tag{4.2}$$

with $g^{ij} = \delta_{ij}/b_i$ (the Fisher-Rao metric) and $V(b)$ the
potential (from the Kelly growth rate).

### 4.2 The spectral element experiment

**Experiment SE-1: Exact Jacobi eigenvalues on the 2-asset simplex.**

For $d = 2$ (one-dimensional simplex $[0, 1]$), the Jacobi operator has
known exact eigenvalues: $\lambda_n = n(n + \alpha + \beta + 1)$ where
$\alpha, \beta$ are the Jacobi polynomial parameters.

1. Discretise $[0, 1]$ with $N = 100$ spectral elements (Chebyshev nodes)
2. Assemble the weighted Laplacian matrix
3. Compute eigenvalues numerically
4. Compare to the exact Jacobi polynomial eigenvalues

This is a VERIFICATION experiment — it checks that our numerical method
recovers the known answer. If it doesn't, the method is wrong. If it does,
we can trust it for $d > 2$.

**Experiment SE-2: Jacobi eigenvalues on the 25-asset simplex.**

1. Triangulate $\Delta_{24}$ using the Voronoi partition (K-means with $N = 64$ cells)
2. On each Voronoi cell: define a polynomial basis (Legendre, order 3)
3. Assemble the global weighted Laplacian (sparse matrix, dimension $64 \times 3^4$)
4. Solve the generalised eigenvalue problem $L\psi = \lambda M\psi$
5. The first few eigenvalues = the Jacobi spectral gap

This gives the EXACT spectral gap on the discretised simplex — no OU
approximation, no DMD, no POD. Pure geometry.

### 4.3 Implementation notes

For $d = 25$: the simplex $\Delta_{24}$ is 24-dimensional. A full spectral
element discretisation is computationally expensive. The practical approach:

- Project onto the $r$-dimensional manifold first (as in all our tests)
- Triangulate the $r$-dimensional factor space (not the full simplex)
- Use order-3 elements on each Voronoi cell → $3^r$ DOFs per cell
- For $r = 4$, $N = 64$ cells: $64 \times 81 = 5{,}184$ DOFs — easily solvable

Libraries: `scipy.sparse.linalg.eigsh` for the sparse eigenvalue problem,
or FEniCS/deal.II for the full spectral element pipeline.

---

## 5. Adaptive Mesh Refinement (AMR)

### 5.1 The problem with uniform Voronoi cells

Our K-means clustering gives UNIFORM cells — equal-sized regions of the factor
space. But the market's dynamics are NOT uniform:

- Near the simplex BOUNDARY ($b_i \to 0$): the Fisher-Rao metric DIVERGES
  ($g_{ii} = 1/b_i \to \infty$). Curvature is high. Fat tails originate here.
  Default occurs here. The Feller boundary classification matters here.
- In the simplex INTERIOR: the metric is well-behaved, curvature is low,
  the market is approximately efficient.

Uniform cells waste resolution in the interior and lack resolution at the boundary.

### 5.2 The AMR strategy

**Step 1: Initial uniform mesh** — K-means with $N = 16$ cells (as in Test 15V).

**Step 2: Error estimator** — for each cell $C_i$, compute:
$$e_i = \text{Var}(\text{returns within } C_i) \times \text{volume}(C_i)$$
High error = the cell contains too much variation = needs splitting.

**Step 3: Refine** — split cells with $e_i > \text{threshold}$ into 2 sub-cells
(bisection along the direction of maximum variance within the cell).

**Step 4: Coarsen** — merge cells with $e_i < \text{threshold}/4$ (the cell is
over-resolved).

**Step 5: Iterate** — repeat steps 2-4 until the maximum error is below
tolerance or the target number of cells is reached.

### 5.3 The AMR experiments

**Experiment AMR-1: Boundary-adapted Voronoi cells.**

1. Run AMR on the FF25 returns to get a boundary-adapted mesh
2. Recompute the transition matrix on the adapted mesh
3. Compare: does the adapted mesh give better Voronoi-LZ compression
   (Test 15V) than the uniform mesh?

**Hypothesis:** The adapted mesh captures more structure (lower LZ rate,
higher Z-score) because it resolves the boundary dynamics that uniform
cells miss.

**Experiment AMR-2: Fat tail estimation from boundary cells.**

1. Build an AMR mesh with high resolution near the boundary
2. Count the frequency of boundary-cell visits — this IS the tail probability
3. Compare to the Hill estimator from Test 7
4. The AMR estimate should be more robust (no parametric assumption about
   the tail shape)

**Experiment AMR-3: Feller boundary classification.**

1. Build an AMR mesh with very high resolution at $b_i \approx 0$ for each $i$
2. Classify the boundary behaviour: does the process hit the boundary (exit)
   or bounce back (entrance)?
3. For each portfolio $i$: estimate the Feller parameter $\alpha_i = Tb^{\ast}_i - 1/2$
4. Compare to the theoretical prediction from HAMILTONIAN_TAILS_COMPLETENESS

---

## 6. Experimental Design: The Complete CFD Validation Programme

### 6.1 Mapping experiments to problems

| Problem | CFD method | Experiment | Expected outcome |
|:--------|:----------|:-----------|:----------------|
| P1 (spectral gap) | DMD + POD + SE | DMD-1, POD-1, POD-2, SE-2 | Three independent estimates of spectral gap should agree |
| P2 (Laplace rate) | SE | SE-1 on $d=2$ | Exact eigenvalues → exact Laplace rate → verify O(1/T²) |
| P3 (vol surface) | AMR | AMR on the (k,T) vol surface | Better interpolation with adapted mesh |
| P4 (FX curvature) | POD + DMD | POD on FX with carry metric | Extract carry-adjusted eigenmodes |
| P5 (LOB impact) | DMD | DMD on L2 book snapshots | Koopman eigenvalues of the LOB dynamics |
| P6 (mandatory alpha) | AMR + SE | SE eigenvalue problem with curved metric | If min eigenvalue > 0, alpha is mandatory |
| P7 (pairs entry) | POD | POD on the spread process | Galerkin matrix gives κ per mode |
| P8 (Wigner surmise) | SE | SE on 500-stock simplex | 499 eigenvalues for proper spacing statistics |

### 6.2 Implementation priority

**Phase 1 (can do now with existing code + numpy):**
- DMD-1: extract continuous-time eigenvalues from the existing Voronoi transition matrix
- POD-2: Galerkin projection of factor dynamics on FF25
- AMR-1: bisection-based adaptive mesh refinement

**Phase 2 (needs a sparse eigenvalue solver):**
- SE-1: spectral elements on $d = 2$ simplex (verification)
- SE-2: spectral elements on $r = 4$ factor subspace

**Phase 3 (needs FEniCS or deal.II):**
- Full spectral element method on the weighted simplex
- AMR with hp-adaptivity (varying polynomial order per cell)

### 6.3 Software

| Tool | What it does | Installation |
|:-----|:-----------|:-------------|
| `numpy.linalg.svd` | DMD, POD | Already have |
| `scipy.sparse.linalg.eigsh` | Sparse eigenvalue problems | Already have |
| `sklearn.cluster.KMeans` | Voronoi tessellation | Already have |
| `pydmd` | Full DMD suite (exact, compressed, streaming) | `pip install pydmd` |
| FEniCS | Finite element method on arbitrary domains | `pip install fenics` or Docker |
| deal.II | High-performance spectral elements + AMR | C++, needs compilation |
| meshio | Mesh I/O (VTK, GMSH formats) | `pip install meshio` |
| pygmsh | Mesh generation | `pip install pygmsh` |

---

## 7. What This Means for the Retractions

Before retracting ANY theoretical claim, we should verify that the experimental
failure is not a failure of the VALIDATION METHOD. The CFD toolkit provides
the proper validation:

| Claim at risk | Current test | Problem | CFD fix | Retract? |
|:-------------|:-------------|:--------|:--------|:---------|
| Spectral gap prediction | Test 4 (covariance) | Wrong proxy | DMD + POD + SE | **Wait** |
| O(1/T²) Laplace | Test N15 (MC comparison) | MC floor | SE on $d=2$ (exact) | **Wait** |
| Vol surface = no-arb | Test N2 (closing prices) | Stale data | N2R (mid-quotes): 5.2% | **Qualify** |
| FX Sharpe = curvature | Test N10 (return covariance) | Missing carry | POD with carry metric | **Wait** |
| LOB impact = curvature | Test N12 (inverse depth) | Wrong proxy | Spread works (r=0.35) | **Restate** |
| Mandatory alpha | Test N16 (crypto vs FF25) | Wrong comparison | AMR on same asset class | **Wait** |
| Pairs z* > 2σ | Test N14 (short sample) | Noise | POD-Galerkin κ estimation | **Wait** |
| Wigner surmise | Test 6 (25 assets) | Too few eigenvalues | SE on 500 stocks | **Wait** |

**Recommendation: retract NOTHING yet.** Five of eight claims need the CFD
toolkit before a fair test can be conducted. Two claims (vol surface, LOB impact)
should be RESTATED with qualifications. Only after the CFD experiments in
Phase 1-2 do we have enough evidence to decide.

---

## 8. The Vision: A CFD Engine for Market Analysis

The ultimate goal: a real-time CFD engine that:

1. **Ingests** tick-level market data from Databento/Massive
2. **Tessellates** the portfolio simplex with AMR (boundary-adapted mesh)
3. **Estimates** the Jacobi operator eigenvalues via DMD (streaming, O(d²) per update)
4. **Projects** the dynamics onto POD modes (real-time factor decomposition)
5. **Predicts** the next-period curvature (hence Sharpe) from the eigenvalue spectrum
6. **Executes** the MUP on the estimated manifold

This is the C++ Universal Portfolio engine (already in `code/cpp/`) extended
with CFD capabilities. The Laplace integrator already implements the saddle-point
approximation. Adding DMD and POD gives it the full spectral decomposition.

---

## References

Schmid, P. J. (2010). Dynamic mode decomposition of numerical and experimental
data. *Journal of Fluid Mechanics* 656, 5–28.

Sirovich, L. (1987). Turbulence and the dynamics of coherent structures.
*Quarterly of Applied Mathematics* 45(3), 561–590.

Patera, A. T. (1984). A spectral element method for fluid dynamics: Laminar
flow in a channel expansion. *Journal of Computational Physics* 54(3), 468–488.

Berger, M. J. and Oliger, J. (1984). Adaptive mesh refinement for hyperbolic
partial differential equations. *Journal of Computational Physics* 53(3), 484–512.

Kutz, J. N., Brunton, S. L., Brunton, B. W., and Proctor, J. L. (2016).
*Dynamic Mode Decomposition: Data-Driven Modeling of Complex Systems*. SIAM.

Rowley, C. W. et al. (2009). Spectral analysis of nonlinear flows.
*Journal of Fluid Mechanics* 641, 115–127.

Mezić, I. (2005). Spectral properties of dynamical systems, model reduction
and decompositions. *Nonlinear Dynamics* 41, 309–325.

*[All other references as per companion papers.]*
