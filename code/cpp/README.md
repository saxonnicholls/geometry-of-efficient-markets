# Universal Portfolio — C++ Simplex Integration Engine

**Saxon Nicholls** — me@saxonnicholls.com

Copyright Saxon Nicholls 2026 MIT Licence

---

## Overview

High-performance C++20 implementation of the Universal Portfolio (Cover 1991)
with five integration methods, implementing the core theory from Papers I.1–I.5
of *The Geometry of Efficient Markets*.

## Integration Methods

| Method | Class | Convergence | Cost | Paper |
|:-------|:------|:-----------|:-----|:------|
| **Laplace** | `LaplaceIntegrator` | O(1/T²) | O(Td²) | I.1 |
| **Monte Carlo** | `MonteCarloIntegrator` | O(1/√N) | O(NTd) | — |
| **Quasi-Monte Carlo** | `MonteCarloIntegrator(true)` | O(1/N) | O(NTd) | — |
| **Factor-Projected** | `FactorProjectedIntegrator` | O(σ_idio) | O(Td²+r³) | I.5 |
| **Exponentiated Gradient** | `EGIntegrator` | O(√(log d/T)) | O(Td) | — |

## Key Components

- **`SimplexMath`** — Simplex projection (Duchi et al.), log-optimal solver with
  Armijo line search, Fisher information matrix, stable rank, Halton QMC sampling
- **`LaplaceIntegrator`** — The Laplace/WKB method from Paper I.1: solves b*,
  computes Fisher matrix, returns posterior mean with O(1/T²) accuracy
- **`EGIntegrator`** — Cover's original EG with true O(d) incremental updates
- **`UniversalPortfolio`** — Strategy-pattern top-level class, owns one
  integration method, supports online and batch modes
- **`Dashboard`** — ImGui/ImPlot real-time visualisation

## Building

```bash
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
./universal_portfolio
```

### Dependencies (auto-fetched via CMake)

- Eigen 3.4+
- nlohmann/json
- Dear ImGui + ImPlot + GLFW (for the dashboard)
- Catch2 (for tests)

## Architecture

```
include/
├── math/SimplexMath.hpp          # All simplex mathematics
├── interfaces/
│   ├── SimplexIntegralInterface.hpp  # Pure virtual integral interface
│   └── IntegrationMethodInterface.hpp # Strategy pattern for methods
├── portfolio/
│   ├── UniversalPortfolio.hpp    # Top-level portfolio class
│   ├── LaplaceIntegrator.hpp     # Laplace/WKB method
│   ├── MonteCarloIntegrator.hpp  # MC and QMC
│   ├── FactorProjectedIntegrator.hpp # PCA-reduced
│   └── EGIntegrator.hpp          # Exponentiated gradient
├── data/                         # Data sources (synthetic, CSV)
├── execution/                    # Paper trading, FIX (optional)
├── benchmark/                    # Method comparison framework
└── ui/                           # ImGui dashboard
```

## Connection to the Monograph

The Fisher information matrix `F(b*)` computed by `fisherInformation()` is the
negative Hessian of the Kelly growth rate at the log-optimal portfolio — the
central object of the monograph. Its stable rank gives the manifold dimension r.
Its eigenvalue spectrum determines the Dyson class (Paper IV.3). The Laplace
integrator implements the WKB expansion from Paper I.1 with the O(1/T²)
accuracy bound proved there.
