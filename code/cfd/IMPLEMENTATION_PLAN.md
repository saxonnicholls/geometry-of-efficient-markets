# CFD Implementation Plan

**Saxon Nicholls** — me@saxonnicholls.com

## Architecture

```
code/cfd/
├── IMPLEMENTATION_PLAN.md   ← This file
├── core/
│   ├── voronoi_mesh.py      ← Adaptive Voronoi tessellation with AMR
│   ├── dmd.py               ← Dynamic Mode Decomposition (exact, streaming)
│   ├── pod.py               ← Proper Orthogonal Decomposition + Galerkin
│   ├── spectral_elements.py ← Spectral element eigenvalue solver
│   └── utils.py             ← Shared utilities (simplex projection, FR metric)
├── experiments/
│   ├── dmd_spectral_gap.py  ← DMD-1, DMD-2, DMD-3
│   ├── pod_galerkin.py      ← POD-1, POD-2
│   ├── se_jacobi.py         ← SE-1, SE-2
│   └── amr_boundary.py      ← AMR-1, AMR-2, AMR-3
└── visualisation/
    └── cfd_gallery.py       ← Visualisations of modes, eigenvalues, meshes
```

## Phase 1: Immediate (numpy only, no new dependencies)

### Step 1: DMD on existing Voronoi data
- Input: Voronoi cell labels from Test 15V (already computed)
- Compute: one-hot encode the cell sequence → data matrix X (N_cells × T)
- Apply: SVD-based exact DMD → continuous-time eigenvalues
- Output: Koopman eigenvalues, DMD modes, comparison to transition matrix eigenvalues
- Time: 10 minutes to implement, seconds to run

### Step 2: POD-Galerkin on FF25
- Input: FF25 daily returns (already loaded in every test)
- Compute: SVD → modes + temporal coefficients
- Fit: da_k/dt = Σ L_kj a_j (OLS regression on the temporal coefficients)
- Output: Galerkin matrix L (4×4), its eigenvalues = Jacobi spectral gap
- Time: 10 minutes to implement, seconds to run

### Step 3: POD-Galerkin on yield curve
- Input: Treasury yield curve daily changes (already have)
- Compute: SVD → 3 modes (level, slope, curvature)
- Compare modes to Nelson-Siegel shapes (refinement of Test N1)
- Fit Galerkin matrix → per-mode κ values
- Output: definitive NS-Jacobi comparison with dynamics
- Time: 10 minutes, seconds to run

### Step 4: Simple AMR
- Input: FF25 returns projected to r=4 factor space
- Initial mesh: K-means with N=16 cells
- Refine: split cells with high internal variance
- Coarsen: merge cells with low variance
- Iterate 3 times → ~32-64 adapted cells
- Recompute Voronoi-LZ on adapted mesh → compare to uniform (Test 15V)
- Time: 30 minutes to implement, minutes to run

## Phase 2: Spectral elements (needs scipy.sparse)

### Step 5: SE-1 verification on d=2
- Discretise [0,1] with N=100 elements, order-3 Legendre polynomials
- Assemble the weighted Laplacian (Fisher-Rao metric = 1/(b(1-b)))
- Solve the generalised eigenvalue problem
- Compare to known Jacobi polynomial eigenvalues λ_n = n(n+α+β+1)
- This VERIFIES our numerical method against known exact results
- Time: 1 hour to implement, seconds to run

### Step 6: SE-2 on r=4 factor subspace
- Triangulate the 4D factor space using the Voronoi partition (64 cells)
- Define order-2 polynomial basis per cell
- Assemble the sparse global Laplacian
- Solve for the first 10 eigenvalues
- Compare to DMD and POD estimates from Phase 1
- Time: 2 hours to implement (the assembly is the hard part), minutes to solve

## Phase 3: Full pipeline (needs PyDMD, FEniCS)

### Step 7: Streaming DMD for real-time spectral gap
- pip install pydmd
- Use streaming DMD (BOPDMD) for online eigenvalue estimation
- Feed with Databento real-time data
- Output: real-time spectral gap, mixing time, Cheeger constant
- Integrate with the C++ Universal Portfolio engine

### Step 8: FEniCS for production spectral elements
- Docker container with FEniCS
- Define the weighted Laplacian on the simplex in variational form
- Solve with hp-adaptive mesh refinement
- Compare to Phase 2 results (validation)

## Dependencies

Phase 1: numpy, scipy, sklearn (ALREADY INSTALLED)
Phase 2: scipy.sparse (ALREADY INSTALLED)
Phase 3: pydmd (`pip install pydmd`), fenics (Docker)

## Expected Outcomes

| Experiment | What it resolves | Expected result |
|:-----------|:----------------|:---------------|
| DMD-1 | P1 (spectral gap) | DMD eigenvalues ≈ OU κ values |
| POD-2 | P1 (spectral gap) | Galerkin L eigenvalues = DMD eigenvalues |
| SE-1 | P2 (Laplace rate) | Numerical eigenvalues = exact Jacobi eigenvalues |
| AMR-1 | Tests 7, 8R, 15V | Better LZ compression with adapted mesh |
| POD-1 | N1 (yield curve) | Galerkin dynamics confirm NS shapes |
| DMD-3 | Test 6 (three types) | Different eigenvalue patterns for different market types |
