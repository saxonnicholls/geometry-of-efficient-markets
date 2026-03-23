# Code: The Geometry of Efficient Markets
## Open-Source Replication Suite

This directory contains the complete Python implementation accompanying the monograph
*"The Geometry of Efficient Markets: Minimal Surfaces, Universal Portfolios, and the
Mathematics of Financial Markets."*

Every major theorem in the monograph has a corresponding function. Every experiment
in `book/EXPERIMENTS.md` has a corresponding script. All data sources are free.

---

## Quick Start

```bash
pip install -r requirements.txt

# Verify installation
cd core && python kelly.py
cd core && python fisher_rao.py
cd core && python curvature.py

# Run the central experiment
cd experiments && python experiment_01_sharpe_curvature.py
```

---

## Directory Structure

```
code/
├── requirements.txt
├── core/                   ← Foundation: Kelly, Fisher-Rao geometry, curvature
├── shapley/                ← Kelly attribution to assets and factors
├── mup/                    ← Manifold Universal Portfolio algorithm
├── processes/              ← Exact stochastic processes (Jacobi, theta, McKean)
├── kalman/                 ← Manifold Kalman-Bucy filter
├── transformer/            ← Market transformer: dimension test, Kelly benchmark
├── takens/                 ← Delay embedding, FNN, diffusion maps
├── filtrations/            ← LZ78 filtration, CTW, Voronoi automaton
├── pairs/                  ← Geometric pairs trading (C++)
├── contagion/              ← Cheeger constant, Delaunay graph, crisis detection
├── rmt/                    ← Random matrix: Dyson class test, Tracy-Widom
└── experiments/            ← 17 replication experiments
```

---

## Module Reference

### `core/` — Foundation

The base layer. Every other module imports from here.

| File | Purpose | Key functions |
|:-----|:--------|:-------------|
| `kelly.py` | Log-optimal (Kelly) portfolio solver | `log_optimal_portfolio()`, `kelly_growth_rate()`, `fisher_information_matrix()`, `stable_rank()`, `factor_subspace()`, `rolling_kelly()` |
| `fisher_rao.py` | Fisher-Rao geometry on the portfolio simplex | `fisher_rao_distance()`, `geodesic()`, `geodesic_path()`, `damped_geodesic()`, `exp_map()`, `log_map()`, `tracking_error()`, `pairwise_fr_distances()` |
| `curvature.py` | Mean curvature of the market manifold | `mean_curvature_normal_bundle()`, `mean_curvature_from_returns()`, `sharpe_curvature_decomposition()`, `willmore_energy_proxy()`, `cheeger_constant_estimate()` |

**The central theorem implemented in `curvature.py`:**
```python
from core.curvature import sharpe_curvature_decomposition
result = sharpe_curvature_decomposition(returns, n_factors=4)
print(f"H = {result['H']:.4f}")           # mean curvature
print(f"Sharpe* ≈ {result['sharpe_predicted']:.4f}")  # theory prediction
print(f"Realised = {result['sharpe_realised']:.4f}")  # empirical check
```

---

### `shapley/` — Kelly Attribution

Shapley value attribution of Kelly growth to assets, factors, and sectors.
Implements the result: `phi_i = b*_i * (mu_i - mu_bar)` (proved unique and fair).

| File | Purpose | Key functions |
|:-----|:--------|:-------------|
| `kelly_shapley.py` | Asset, factor, and sector attribution | `kelly_shapley()`, `kelly_shapley_from_returns()`, `factor_shapley()`, `sector_shapley()`, `banzhaf_attribution()`, `print_attribution_report()` |

```python
from shapley.kelly_shapley import print_attribution_report
print_attribution_report(b_star, mu_annualised, asset_names, V_r, factor_names)
```

---

### `mup/` — Manifold Universal Portfolio

The MUP achieves regret `r·log(T)/(2T)` vs Cover's `(d-1)·log(T)/(2T)`.
For d=50, r=4: 12× improvement. Minimax optimal.

| File | Purpose |
|:-----|:--------|
| `manifold_universal_portfolio.py` | MUP algorithm and regret computation |
| `cover_portfolio.py` | Cover's original universal portfolio (baseline) |
| `regret_comparison.py` | Side-by-side regret comparison |

---

### `processes/` — Exact Stochastic Processes

Each market type has an exact transition density and option pricing formula.

| File | Market type | Process | Transition density |
|:-----|:-----------|:--------|:------------------|
| `jacobi_diffusion.py` | CAPM (great sphere) | Jacobi diffusion | Jacobi polynomial series |
| `theta_function_bm.py` | Clifford torus | Flat torus BM | Jacobi theta function ϑ₃ |
| `mckean_hyperbolic.py` | Pseudo-Anosov | Hyperbolic BM | McKean kernel |
| `option_pricing.py` | All types | — | Exact pricing per manifold type |

```python
from processes.theta_function_bm import theta_option_price
price = theta_option_price(S=100, K=105, T=0.25, epsilon=0.04)
```

---

### `kalman/` — Manifold Kalman-Bucy Filter

Optimal signal extraction and state estimation on the market manifold.
The Riccati steady-state solution is `P_∞ = F(b*)^{-1}` (inverse Fisher matrix).
The Kalman innovation IS the normal bundle projection of each return.

| File | Purpose |
|:-----|:--------|
| `manifold_kalman.py` | Kalman-Bucy filter on M^r |
| `extended_kalman_manifold.py` | Extended KF for nonlinear manifold dynamics |
| `signal_decomposition.py` | Factor vs idiosyncratic return decomposition |

---

### `transformer/` — Market Transformer

Tests the LLM convergence theorem: no model beats the MUP on an efficient market.
The Kelly rate is the theoretical minimum cross-entropy loss for any market model.

| File | Purpose |
|:-----|:--------|
| `dimension_estimator.py` | Estimate optimal transformer hidden dim = r |
| `kelly_loss_benchmark.py` | Compute Kelly rate as loss calibration benchmark |
| `lmsr_attention.py` | Demonstrate LMSR = softmax identity |

---

### `takens/` — Manifold Reconstruction

The market manifold M^r can be reconstructed from a single return series
using delay embedding (Takens' theorem). Minimum embedding dimension = 2r+1.
Optimal delay τ = 1/λ₁ (Jacobi spectral gap timescale).

| File | Purpose |
|:-----|:--------|
| `fnn_algorithm.py` | False nearest neighbours → identify r |
| `diffusion_maps.py` | Three-step manifold estimation: embed → kernel → M^r |
| `delay_selection.py` | Mutual information criterion for optimal τ |

```python
from takens.fnn_algorithm import find_embedding_dimension
r = find_embedding_dimension(return_series, tau=21)
print(f"Estimated manifold dimension: r = {r}")
```

---

### `filtrations/` — Geometric Filtrations

The LZ78 prefix tree IS the filtration atom hierarchy (proved).
Any grammar-based compressor generates a valid filtration on the return path space.

| File | Purpose |
|:-----|:--------|
| `lz78_filtration.py` | LZ78 compressor as filtration builder |
| `ctw_filtration.py` | Context Tree Weighting (CTW) — Bayesian optimal filtration |
| `voronoi_automaton.py` | Voronoi cell automaton and sofic shift |
| `filtration_complexity.py` | Filtration complexity = Willmore energy deficit |

---

### `pairs/` — Geometric Pairs Trading

Optimal entry/exit from the Hamiltonian free boundary:
- Entry: `z* = sqrt(1 + r/κ)` (not the classical 2σ rule)
- Exit: `x* = θ - σ·sqrt(r/(2κ³))`

| File | Purpose |
|:-----|:--------|
| `geometric_pairs_trading.cpp` | High-performance C++ implementation |
| `ou_params.py` | OU parameter estimation (κ, θ, σ) |
| `berry_phase_filter.py` | Berry phase entry timing adjustment |
| `backtest.py` | Pairs strategy backtester |

---

### `contagion/` — Systemic Risk

The contagion network IS the Delaunay graph of the market manifold (endogenous).
The Cheeger constant h_M = systemic risk measure. Collapses before crises.

| File | Purpose |
|:-----|:--------|
| `cheeger_constant.py` | Rolling Cheeger constant estimation (crisis indicator) |
| `delaunay_graph.py` | Delaunay graph of Voronoi partition |
| `crisis_detector.py` | Multi-signal crisis detection dashboard |
| `covar_geometric.py` | Geometric CoVaR: two institutions = Delaunay neighbours |

---

### `rmt/` — Random Matrix Theory

The Dyson symmetry class β ∈ {1, 2, 4} is forced by the manifold geometry.
CAPM → GOE (β=1), Clifford torus → GUE (β=2), pseudo-Anosov → GSE (β=4).

| File | Purpose |
|:-----|:--------|
| `dyson_class_test.py` | Ratio statistic test: GOE vs GUE vs GSE |
| `tracy_widom_fit.py` | Fit F₁/F₂/F₄ to largest eigenvalue distribution |
| `selberg_integral.py` | Exact MUP partition function via Selberg integral |
| `marchenko_pastur.py` | β-Marchenko-Pastur bulk distribution |

---

### `experiments/` — Replication Suite

17 experiments corresponding to `book/EXPERIMENTS.md`.
All use free data (yfinance, Ken French Data Library, CBOE).
All include falsification criteria — results that would require revising the theory.

| # | Script | Tests | Runtime |
|:-:|:-------|:------|:-------:|
| 01 | `experiment_01_sharpe_curvature.py` | Sharpe = ‖H‖ | ~15 min |
| 02 | `experiment_02_tail_index.py` | α = r/2 | ~10 min |
| 03 | `experiment_03_mup_vs_cover.py` | MUP regret ratio | ~45 min |
| 04 | `experiment_04_stationary_distribution.py` | Portfolio weights ~ Beta | ~5 min |
| 05 | `experiment_05_jacobi_vs_gbm.py` | σ² ∝ b(1-b) vs b² | ~8 min |
| 06 | `experiment_06_vol_skew_curvature.py` | Skew = H²/2σ_I | ~5 min |
| 07 | `experiment_07_pairs_threshold.py` | z* = √(1+r/κ) | ~20 min |
| 08 | `experiment_08_entropy_kelly.py` | h_top = h_Kelly | ~10 min |
| 09 | `experiment_09_reynolds_number.py` | Re as crisis indicator | ~8 min |
| 10 | `experiment_10_berry_phase.py` | Berry phase entry filter | ~25 min |
| 11 | `experiment_11_dyson_class.py` | GOE vs GUE ratio test | ~10 min |
| 12 | `experiment_12_tracy_widom.py` | F₁/F₂ eigenvalue fit | ~10 min |
| 13 | `experiment_13_takens_fnn.py` | FNN → identify r | ~15 min |
| 14 | `experiment_14_diffusion_maps.py` | Manifold reconstruction | ~20 min |
| 15 | `experiment_15_shapley_attribution.py` | φᵢ = b*ᵢ(μᵢ-μ̄) | ~5 min |
| 16 | `experiment_16_grassberger_dim.py` | Correlation dim ν = r | ~15 min |
| 17 | `experiment_17_transformer_dim.py` | Optimal dim = r | ~30 min |

Run all experiments:
```bash
cd experiments
for i in $(seq -w 1 17); do
    python experiment_${i}_*.py 2>&1 | tail -20
    echo "---"
done
```

---

## Data Sources

All data is freely available. No paid subscriptions required.

| Source | Access | Used in |
|:-------|:-------|:--------|
| Ken French Data Library | `pandas_datareader` (free) | Exp 1, 2, 4, 6, 8, 11, 15 |
| Yahoo Finance | `yfinance` pip package | Exp 2, 3, 5, 7, 9, 10, 13, 14 |
| CBOE (VIX, SKEW) | `yfinance` or direct download | Exp 6, 9 |
| WRDS/CRSP | Free academic registration | Exp 3 (full version) |

---

## Design Principles

**One function, one theorem.** Every key result from the monograph maps to a
named function with a docstring citing the theorem number.

**Correctness before speed.** The implementations prioritise mathematical
correctness and readability. Performance optimisation is secondary.

**Offline fallback.** Every experiment that downloads data has a synthetic
data fallback so it runs without internet access.

**Explicit falsification.** Every experiment states what result would
require revising the theory. Science, not advocacy.

---

## Dependencies

```
numpy>=1.24       scipy>=1.10       pandas>=2.0
statsmodels>=0.14 pandas-datareader>=0.10  yfinance>=0.2
scikit-learn>=1.3 matplotlib>=3.7   seaborn>=0.12
tqdm>=4.65        arch>=5.3
```

C++ code in `pairs/` requires a C++17 compiler. Build with:
```bash
cd pairs && g++ -O3 -std=c++17 geometric_pairs_trading.cpp -o pairs_trader
```

---

## Citation

If you use this code, please cite:

```
@book{geometry_efficient_markets_2025,
  title     = {The Geometry of Efficient Markets},
  subtitle  = {Minimal Surfaces, Universal Portfolios, and the
               Mathematics of Financial Markets},
  year      = {2025},
  note      = {Code available at github.com/saxonnicholls/geometry-of-efficient-markets}
}
```

---

*"The market has a shape. This code finds it."*
