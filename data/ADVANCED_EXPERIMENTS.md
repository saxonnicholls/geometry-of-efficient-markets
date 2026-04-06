# Advanced Experiments: Lie Groups, Wavelets, and Sparsity

**Saxon Nicholls** — me@saxonnicholls.com

## Insight-Driven Experimental Design

Three insights from our analysis suggest new experiments that could
push the scorecard from 60% toward 80%:

---

### Insight 1: Wavelets decompose the invariance problem by scale

The spectral hierarchy β is NOT invariant across datasets (CV = 2.13).
But it may be invariant WITHIN a single wavelet scale. Daubechies-4
(Mallat's fast algorithm, O(N)) gives compact, localised time-frequency
atoms that separate the dynamics by timescale.

**Experiment W1: β per wavelet scale**
- Decompose FF25 returns into db4 wavelet scales (8 levels: 2d to 512d)
- At each scale: compute PCA eigenvalues and OU κ per mode
- Estimate β at each scale independently
- If β is constant across scales: the theory is correct at each timescale
  (the non-invariance comes from MIXING scales, not from the theory being wrong)

**Experiment W2: Wavelet spectral gap predicts mixing**
- At each wavelet scale: estimate the spectral gap from the transition matrix
- Test: does the wavelet-scale spectral gap predict the mixing time at THAT scale?
- This is the scale-resolved version of Test 4R

**Experiment W3: Wavelet scalogram as crisis detector**
- Compute the wavelet scalogram (energy vs time × scale)
- Before crises: energy should shift from low frequencies to high frequencies
  (the market becomes "turbulent" — energy cascades to small scales)
- This is the wavelet version of Test 5 (Cheeger → crisis)

---

### Insight 2: FX has Lie group structure equities don't

The FX market's group multiplication (triangular arbitrage) holds to 2.1 bps.
This is a structure that equities don't have. It gives us:

**Experiment LG1: Group multiplication residuals at tick level**
- Use Massive S3 tick-level FX quotes
- Measure triangular arb residuals at nanosecond resolution
- Theory: residuals should mean-revert at the Koopman eigenvalue rate
- This is the most precise test of the Lie group structure

**Experiment LG2: Cartan subalgebra = factor space**
- The carry direction should be a Cartan generator (eigenvector of the
  adjoint representation)
- Test: does the carry portfolio align with a single PC of FX returns?
- The Cartan rank = the FX manifold dimension r

**Experiment LG3: Killing form = Fisher-Rao**
- The Killing form B(X,Y) = tr(ad_X · ad_Y) should equal the FR metric
- For an abelian group: B = 0 (FX is nearly abelian)
- The DEVIATION from B = 0 measures the non-commutativity of the FX group
- This deviation should correlate with the carry premium (non-commutativity = alpha)

---

### Insight 3: Sparsity of the Galerkin matrix reveals coupling structure

If the Galerkin matrix L is SPARSE in wavelet coordinates, the scales are
independent. If it's DENSE, the scales interact (turbulent cascade).

**Experiment SP1: Galerkin matrix sparsity in wavelet basis**
- Compute L in the standard PC basis (our current Galerkin matrix)
- Transform to wavelet basis: L_w = W L W^{-1}
- Compare sparsity: % of entries below threshold in each basis
- Theory: L_w should be sparser (scales decouple)

**Experiment SP2: Sparsity predicts simplicity**
- For different asset classes: compute the Galerkin matrix sparsity
- Theory: more efficient markets should have SPARSER L
  (the dynamics separate cleanly by scale)
- Compare: equities vs FX vs crypto vs yield curve

**Experiment SP3: Compression ratio of the dynamics**
- How many non-zero entries of L_w are needed to explain 90% of the dynamics?
- This is the "effective complexity" of the market dynamics
- Theory: r × r is enough (the manifold dimension determines the complexity)

---

## Priority and Data Requirements

| Experiment | Data | Priority | Expected Impact |
|:-----------|:-----|:--------:|:---------------|
| **W1** | FF25 (have) | **HIGH** | Resolves the invariance question |
| **W2** | FF25 (have) | HIGH | Validates spectral gap per scale |
| **W3** | Sector ETFs (have) | HIGH | Better crisis predictor than Test 5 |
| LG1 | Massive S3 tick FX | Medium | Most precise group structure test |
| LG2 | Spot FX (have) | Medium | Carry = Cartan confirmation |
| LG3 | Spot FX (have) | Medium | Killing form deviation = alpha |
| SP1 | FF25 (have) | Medium | Scale decoupling test |
| SP2 | Multiple (have) | Low | Cross-asset complexity comparison |
| SP3 | FF25 (have) | Low | Effective dynamical complexity |

W1 is the most important — if β is invariant within wavelet scales,
it resolves Problem P1 and rescues the spectral gap prediction.
