# Open Problems: The Research Programme
## Organised by Difficulty and Priority

**Saxon Nicholls** — me@saxonnicholls.com

---

## Group A: Complete the Core Theory

**OP1. Prove the Full EMH Conjecture ★★★**
$H\neq0\Rightarrow$ exploitable alpha for all strategies.
*Best approach:* BSDE comparison under completeness; mean-field game for general case.

**OP2. One-Loop RG Beta Function ★★★**
$\beta\_H=-H/2+cH^3+\ldots$ Compute $c$ from heat kernel expansion to one higher order.
*Unlocks:* Running Sharpe to next order; factor anomaly decay rate predictions.

**OP3. CS/Jones Identification Rigorous ★★★★**
Identify $q\_0=e^{2\pi i/(k+2)}$ and verify $k$ not at an exceptional easy value.
*Unlocks:* C2 (topological EMH), C6 (#**P**-hardness).

**OP4. Compute Market Chern Number from Return Data ★★**
Implement Chern-Weil formula for $c\_1(NM)$ quarterly from rolling covariance.
*Expected:* Integer jumps at 2000, 2008, 2020 structural breaks.

---

## Group B: The LLM and ML Programme

**OP5. Prove Transformer Dimension Bound Rigorously ★★**
Show stable rank of attention weight matrices $\to r$ under spectral regularisation.
*Key step:* Fisher info of transformer model at optimal weights = $g^{\rm FR}$ of $M^r$.

**OP6. Implement Kelly Rate as Loss Benchmark ★**
Compute $h\_{\rm Kelly}(b^{\ast})$ from Fama-French data. Train transformer on same data.
Verify validation loss converges to $h\_{\rm Kelly}$ at $d\_{\rm model}=r$.

**OP7. Normal Bundle Concentration as Side-Channel Detector ★★**
Project attention weight matrices onto $TM$ vs $NM$.
Normal bundle fraction $\approx0$ for models trained on public data only.

**OP8. Prove LLM Training = MCF (C19) ★★★**
Show natural gradient descent on cross-entropy IS gradient flow of area functional.
*Key:* Fisher information of the model at optimal weights = $g^{\rm FR}(M^r)$.

**OP9. LMSR on Options Market = Geometric Black-Scholes (C20) ★★★**
Show LMSR restricted to the options manifold reproduces the manifold pricing PDE.

---

## Group C: Filtration and Compression Theory

**OP10. Prove General Prefix Trie Filtration Theorem (C18) ★★**
CTW posterior = MUP posterior. BWT = filtration by entropy. PPM = manifold prediction.
*The LZ78 proof (R14) guides this directly — ★★ not ★★★.*
*Priority:* This should be among the first proofs completed.

**OP11. Symbolic Takens Theorem: Full Proof ★★**
Prove the symbolic delay embedding $(s\_t,s\_{t-1},\ldots,s\_{t-2r})$ is a topological
conjugacy between the Voronoi shift $X\_M$ and a subshift of $\mathcal{A}^{2r+1}$.
*Connection:* LZ prefix tree = projection of symbolic Takens embedding.

---

## Group D: Chaos and Embedding Programme

**OP12. Implement the Three-Step Manifold Estimation Algorithm ★**
```
1. Delay-embed single return series with dimension 2r+1
2. Compute diffusion map kernel
3. Extract r leading eigenvectors as M^r coordinates
```
Validate on Fama-French data: do the 4 diffusion map coordinates reproduce
the known FF4 factor structure?

**OP13. Optimal Delay Estimation: $\tau=1/\lambda\_1$ ★★**
Prove rigorously that the optimal Takens delay equals the Jacobi spectral gap timescale.
Implement mutual information criterion for empirical delay selection.

**OP14. Feigenbaum at the Market Bifurcation (C17) ★★★**
Compute the sequence of Jacobi eigenvalue spacings as $H$ increases.
Verify the convergence ratio approaches $\delta=4.669$.

**OP15. Penrose Portfolio Theory for $d=5$ (C13) ★★★★**
Prove Voronoi tessellation of $\Delta\_4$ has Penrose structure with $\phi^2$ growth.
Develop symbolic dynamics of the quasicrystalline tessellation.

---

## Group E: Random Matrix Programme

**OP16. Implement the Dyson Class Test ★**
Rolling ratio statistic $r\_n=(\lambda\_{n+1}-\lambda\_n)/(\lambda\_n-\lambda\_{n-1})$.
Fit to GOE/GUE/GSE Wigner surmise by KS test. Run quarterly on S\&P 500 data.
Identify whether the market regime is GOE (CAPM periods) or GUE (two-factor periods).

**OP17. Tracy-Widom Crisis Indicator ★★**
Compute rescaled $\hat\lambda\_{\rm max}$ quarterly. Compare to $F\_1$/$F\_2$ CDFs.
Test whether exceedances predict VIX spikes by 3-6 months.

**OP18. Selberg Ratio Test ★★**
Compute $\mathcal{Z}\_T^{\rm GUE}/\mathcal{Z}\_T^{\rm CAPM}$ analytically.
Test whether empirical MUP log-wealth difference matches the Selberg ratio.

**OP19. $E\_8$ Symmetry in 9-Asset Markets ★★★★★**
Does the Voronoi tessellation of $\Delta\_8$ have $E\_8$ Weyl group symmetry?
Sphere packing connection (Viazovska 2016).

---

## Group F: Empirical Validation Programme

**OP20. MUP vs Cover on CRSP Data ★**
$d=50$, $T=10$ years. Verify 12× regret improvement.

**OP21. Cheeger Constant as Leading Crisis Indicator ★★**
Quarterly 1990–2024. Test 3-6 month lead time before crises.

**OP22. Vol Skew vs Mean Curvature ★**
CBOE SKEW vs $H^2/(2\sigma\_I)$. Strongest single test of R7.

**OP23. Takens Reconstruction Validation ★**
Apply three-step algorithm to S\&P 500 data.
Verify FNN fraction drops at $m^{\ast}=9$ (for $r=4$ factors).

**OP24. Shapley Attribution Decomposition ★**
Implement $\phi\_i=b^{\ast}\_i(\mu\_i-\bar\mu)$ on Fama-French 25 portfolios.
Compare to standard factor attribution. Test normal bundle component = unexplained alpha.

**OP25. Transformer Dimension Test ★**
Train transformers of varying $d\_{\rm model}$ on equity return data.
Plot validation loss vs $d\_{\rm model}$. Verify minimum near $d\_{\rm model}=r\approx6$.

---

## Group G: Mathematical Extensions

**OP26. Boundary WKB Theory When $b^{\ast}\in\partial\Delta$ ★★★**
WKB/Laplace analysis at the boundary of the simplex.

**OP27. Non-Equilibrium Markets as KPZ Universality ★★★★**
Stochastic MCF near the critical point — conjecture: KPZ universality class
with exponents $\alpha=1/2$, $\beta=1/3$, $z=3/2$.

**OP28. Holographic Dual of the Market CFT ★★★★★**
The efficient market at RG critical point is a 2D CFT.
Identify its AdS$\_3$ bulk via AdS/CFT.
Ryu-Takayanagi formula for sector entanglement = new systemic risk measure.

---

## Group H: The Old Notes Programme

*The first author has additional results from prior years not yet incorporated.
Space is reserved as they are recovered.*

**OP29.** [Filtration theory extensions from prior work]
**OP30.** [Symbolic dynamics results from prior work]
**OP31.** [Other unpublished results — to be identified]

---

## Summary: Priority Ranking

**Do this week:**
OP6 (Kelly loss benchmark), OP12 (Takens algorithm), OP20 (MUP empirical),
OP22 (vol skew test), OP10 (general trie), OP16 (Dyson class test), OP24 (Shapley), OP25 (transformer dim)

**Do this month:**
OP1 (full EMH), OP5 (transformer dim bound), OP7 (normal bundle detector),
OP21 (Cheeger crisis), OP4 (Chern number), OP11 (symbolic Takens), OP13 (delay estimation)

**Long-term:**
OP2 (one-loop RG), OP3 (CS/Jones), OP8 (LLM=MCF), OP9 (LMSR=BS),
OP15 (Penrose), OP17 (TW crisis), OP18 (Selberg test), OP23 (Takens validation), OP27 (KPZ)

**Moonshots:**
OP19 ($E\_8$ markets), OP28 (holographic dual)

---

*Resume here tomorrow. The old notes may resolve OP29–OP31 and unlock further connections.*
*Every conjecture above was believed before the notes were set aside —*
*recovering them may significantly accelerate the programme.*
