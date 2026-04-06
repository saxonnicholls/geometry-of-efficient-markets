# Visualisation Suite

**Saxon Nicholls** — me@saxonnicholls.com

Visualisations for *The Geometry of Efficient Markets*. Static PNGs for
the monograph and an interactive 3D browser-based manifold explorer.

---

## Quick Start

```bash
# Install dependencies
pip install numpy pandas scipy matplotlib scikit-learn plotly pyarrow

# Generate the three classified market manifold figures (for README.md)
python market_manifolds.py

# Generate the interactive FX manifold (opens in browser)
python fx_manifold_plotly.py

# Generate static FX manifold gallery (no browser needed)
python fx_manifold_interactive.py

# Generate all experiment result figures
cd ../../code/experiments
python run_all_tests.py
```

---

## Scripts

| Script | What it produces | Dependencies |
|:-------|:----------------|:-------------|
| `market_manifolds.py` | The three classified market types (CAPM sphere, Clifford torus, pseudo-Anosov saddle) used in the README. Three PNGs. | matplotlib, numpy |
| `fx_manifold_plotly.py` | **Interactive 3D FX market manifold.** Opens in browser. Rotate, zoom, hover, switch colour schemes via dropdown. | plotly, scipy, sklearn |
| `fx_manifold_interactive.py` | Static PNG gallery of the FX manifold from multiple angles, with minimal surface overlay. | matplotlib, scipy, sklearn |

---

## Interactive FX Manifold

The flagship visualisation. Open `gallery/fx_manifold_interactive.html` in any
browser (Chrome, Firefox, Safari — no server needed, fully self-contained).

### How to generate

```bash
cd code/visualisation
python fx_manifold_plotly.py
# → Opens gallery/fx_manifold_interactive.html in your default browser
```

### What you're looking at

The FX market has 7 major currencies (EUR, GBP, JPY, CHF, AUD, CAD, NZD vs USD).
At each minute, the currency allocation vector is a point on the 6-dimensional
simplex Δ₆. We apply:

1. **Bhattacharyya embedding:** w → √w maps the simplex to the positive sphere S⁶₊
2. **PCA:** project onto the top 3 principal components (which explain ~96% of variance)
3. **Minimal surface:** interpolate a smooth surface through the centroid of the path

The result is a 3D point cloud (the manifold path) floating around a blue translucent
surface (the minimal surface = the efficient manifold).

### Controls

| Action | Effect |
|:-------|:-------|
| **Drag** | Rotate the 3D view |
| **Scroll** | Zoom in/out |
| **Hover** | See timestamp, curvature κ, deviation H |
| **Dropdown** (top-left) | Switch colour scheme |

### Colour schemes (via dropdown)

| Scheme | What it shows | Interpretation |
|:-------|:-------------|:--------------|
| **Curvature (\|κ\|)** | Bright = high path curvature | Alpha opportunities — moments when the market deviates sharply from geodesic motion |
| **Deviation from surface (H)** | Red = above surface, blue = below | Mean curvature — the gap between the actual path and the efficient manifold |
| **Time** | Blue = start, yellow = end | How the market traverses the manifold over the month |
| **EURUSD** | Red = EUR strengthening, blue = weakening | This pair's footprint on the manifold |
| **GBPUSD** | Same colour scheme for GBP | |
| **JPYUSD** | Same for JPY | |
| **CHFUSD** | Same for CHF | |
| **AUDUSD** | Same for AUD | |
| **CADUSD** | Same for CAD | |
| **NZDUSD** | Same for NZD | |

### The key insight

The **gap between the coloured dots and the blue surface IS the Sharpe ratio.**
Where the dots are far from the surface, H is large, and there is exploitable alpha.
Where they hug the surface, the market is efficient. The Sharpe-curvature identity
— Sharpe* = ‖H‖_{L²} — is visible to the naked eye.

### Data

- **Source:** Databento GLBX.MDP3 (CME FX futures)
- **Resolution:** 1-minute bars
- **Period:** December 2024
- **Symbols:** 6E (EUR), 6B (GBP), 6J (JPY), 6S (CHF), 6A (AUD), 6C (CAD), 6N (NZD)
- **Size:** ~10,000 bars after cleaning

### PCA eigenvalues

| Component | Variance explained | Interpretation |
|:---------:|:-----------------:|:--------------|
| PC1 | 74.5% | **Dollar factor** — USD strengthening/weakening vs all |
| PC2 | 15.1% | **Carry factor** — high-yield (AUD, NZD) vs low-yield (JPY, CHF) |
| PC3 | 6.6% | **Risk factor** — risk-on vs risk-off |
| **Total** | **96.2%** | Three factors explain almost everything |

This confirms the monograph's prediction: the FX market manifold has dimension
r ≈ 3, with the three factors being dollar, carry, and risk.

---

## Gallery Contents

### Monograph figures (for README.md)

| File | Description |
|:-----|:-----------|
| `market_manifolds.png` | The three classified market types on the Bhattacharyya sphere |
| `curvature_profiles.png` | Mean curvature |H|² profiles across the three types |
| `classification_table.png` | Classification table: type → process → density → β |

### FX manifold

| File | Description |
|:-----|:-----------|
| `gallery/fx_manifold_interactive.html` | **Interactive 3D** — open in browser |
| `gallery/fx_manifold_vs_minimal_surface.png` | Four-angle static: manifold path vs minimal surface |
| `gallery/fx_manifold_per_pair.png` | Each currency pair's footprint on the manifold |
| `gallery/fx_manifold_deviation_analysis.png` | Deviation histogram, curvature time series, κ vs H scatter |

### Experiment results

| File | Test | Description |
|:-----|:-----|:-----------|
| `gallery/scorecard.png` | All | Colour-coded scorecard table |
| `gallery/test_07_fat_tails.png` | 7 | Hill estimator distribution vs predicted α = r/2 |
| `gallery/test_08_jacobi_fit.png` | 8 | Jacobi vs GBM KS statistics |
| `gallery/test_11_mif_vs_cap.png` | 11 | MIF vs cap-weight cumulative wealth |
| `gallery/test_14_shapley.png` | 14 | Shapley attribution bar chart + scatter |
| `gallery/test_15_lz_kelly.png` | 15 | Original LZ-Kelly (failed) |
| `gallery/test_15R_lz_symbolic.png` | 15R | L/S symbolic LZ across asset classes |
| `gallery/test_15V_lz_voronoi.png` | 15V | Voronoi-LZ: Z-score heatmap, transition matrix, rolling |
| `gallery/test_18_emu_spreads.png` | 18 | Sovereign spreads vs geometric distance (1-k/r) |
| `gallery/test_19_crypto_stages.png` | 19 | Crypto efficiency ranking by Willmore proxy |

---

## Requirements

```
numpy>=1.24
pandas>=2.0
scipy>=1.10
matplotlib>=3.7
scikit-learn>=1.3
plotly>=5.18
pyarrow>=14.0
```

The interactive HTML file (`fx_manifold_interactive.html`) is self-contained —
it includes the Plotly.js library. No server or installation needed to view it.
Just open in any modern browser.

---

## Generating New Visualisations

To regenerate all visualisations from scratch:

```bash
# 1. Download and process data
cd data/
python download_all.py
python process_all.py

# 2. Download Databento FX futures (requires API key in .env)
python download_databento_batch1.py

# 3. Generate all figures
cd ../code/visualisation/
python market_manifolds.py           # Three market types
python fx_manifold_plotly.py         # Interactive FX manifold
python fx_manifold_interactive.py    # Static FX manifold gallery

# 4. Generate experiment result figures
cd ../experiments/
python run_all_tests.py              # All test result figures
python test_15R_lz_symbolic.py       # LZ symbolic test figures
python test_15V_lz_voronoi.py        # LZ Voronoi test figures
```

---

*"The gap between the dots and the surface IS the Sharpe ratio."*
