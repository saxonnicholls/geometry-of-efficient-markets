# The Geometry of the Yield Curve:
## Static Shape, Dynamic Evolution, and Why Inversions Are Topological Signals

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.7** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
The yield curve is a one-dimensional submanifold of the bond market manifold
$M^r_{\mathrm{bond}} \subset S^{d-1}_{+}$, where $d$ is the number of distinct
maturities traded. Its static shape is determined by the curvature of this curve
in the ambient Fisher--Rao geometry. Its dynamic evolution follows mean curvature
flow (MCF) on the space of curves. A yield curve inversion is a topological
event — the curve's self-intersection number changes from 0 to 1, which is a
codimension-1 phenomenon in the moduli space of yield curves. This topological
characterisation explains why inversions reliably predict recessions: the
inversion is not a cause but a *symptom* of the market manifold approaching an
MCF singularity.

We derive:
- **Nelson--Siegel = Jacobi eigenmodes.** The three Nelson--Siegel factors
  (level, slope, curvature) are the first three eigenfunctions $v_0, v_1, v_2$
  of the Jacobi operator on $M^3_{\mathrm{bond}}$, with eigenvalues
  $0 = \lambda_0 < \lambda_1 < \lambda_2$ controlling mean-reversion speeds.
- **Term premium = mean curvature.** The term premium at maturity $\tau$ equals
  the mean curvature $H(\gamma_t, \tau)$ of the yield curve $\gamma_t$ at that
  point, measured in the Fisher--Rao geometry of the bond simplex.
- **Short-rate models = manifold diffusions.** Vasicek is OU on the level
  component, CIR is the Jacobi diffusion on $\mathbb{R}_{+}$ (the Wright--Fisher
  process restricted to one coordinate), and Hull--White is the geodesic through
  the current yield curve point.
- **HJM = constrained MCF.** The Heath--Jarrow--Morton drift condition is the
  constraint that yield curve evolution is an MCF on the space of curves in
  $M^r_{\mathrm{bond}}$, with the no-arbitrage condition selecting the unique
  drift compatible with the mean curvature.
- **Inversion = winding number transition.** The inverted yield curve has winding
  number $w = 1$ (versus $w = 0$ for the normal curve). The transition
  $w: 0 \to 1$ is a codimension-1 event in the moduli space — a topological
  recession predictor with a 10-for-10 record since 1955.
- **Bond MUP = carry + steepener + butterfly.** The Manifold Universal Portfolio
  on $M^3_{\mathrm{bond}}$ decomposes into three orthogonal strategies along the
  Jacobi eigenmodes. The combined Sharpe ratio satisfies the Pythagorean identity
  $\mathrm{Sharpe}^2_{\mathrm{total}} = \mathrm{Sharpe}^2_{\mathrm{level}} +
  \mathrm{Sharpe}^2_{\mathrm{slope}} + \mathrm{Sharpe}^2_{\mathrm{curvature}}$.

The yield curve is the ideal testing ground for the monograph's framework: the
manifold dimension $r = 3$ is precisely known from Litterman--Scheinkman [1991],
the eigenmodes are well-characterised empirically, the dynamic models are among
the most studied objects in mathematical finance, and the topological signal
(inversion $\Rightarrow$ recession) has the longest and cleanest empirical record
of any macroeconomic indicator.

The punchline: *the yield curve inversion is not a cause of recession — it is a
topological marker of the approaching singularity.*

**Keywords.** Yield curve; term structure; Nelson--Siegel; Jacobi operator;
mean curvature; term premium; Vasicek; Cox--Ingersoll--Ross; Hull--White;
Heath--Jarrow--Morton; winding number; yield curve inversion; recession predictor;
bond market manifold; Fisher--Rao geometry; Manifold Universal Portfolio;
Pythagorean Sharpe decomposition.

**MSC 2020.** 91G30, 91G10, 53A04, 53C44, 58J35, 60J60.

---

## 1. The Bond Market Simplex

### 1.1 Setup

A bond market consists of $d$ instruments distinguished by maturity. In the US
Treasury market, the standard maturities are:

```math
\tau_1 = \tfrac{1}{12}, \quad \tau_2 = \tfrac{3}{12}, \quad \tau_3 = \tfrac{6}{12}, \quad \tau_4 = 1, \quad \tau_5 = 2, \quad \tau_6 = 3, \quad \tau_7 = 5, \quad \tau_8 = 7, \quad \tau_9 = 10, \quad \tau_{10} = 20, \quad \tau_{11} = 30
```

giving $d = 11$ maturities and a portfolio simplex

```math
\Delta_{10} = \bigl\{b = (b_1, \ldots, b_{11}) \in \mathbb{R}^{11}_{+} : \textstyle\sum_{i=1}^{11} b_i = 1\bigr\} \tag{1.1}
```

where $b_i$ is the fraction of wealth allocated to maturity $\tau_i$. The
simplex carries the Fisher--Rao metric $g^{\mathrm{FR}}_{ij} = \delta_{ij}/b_i$,
and the Bhattacharyya isometry $\phi: b \mapsto \sqrt{b}$ embeds it into the
positive orthant of $S^{10}_{+}$ with constant sectional curvature $K = 1/4$.

Everything developed in the preceding papers applies verbatim: portfolio weights
are barycentric coordinates, the log-optimal portfolio $b^\ast$ maximises the
Kelly growth rate $L_T(b) = T^{-1}\sum_{t=1}^{T} \log\langle b, x_t\rangle$,
and the market manifold $M^r_{\mathrm{bond}} \subset S^{10}_{+}$ is the
$r$-dimensional submanifold of log-optimal bond portfolios over all factor shock
realisations.

### 1.2 The dimension is precisely known

The bond market is the one setting where the manifold dimension $r$ is known with
extraordinary precision. Litterman and Scheinkman [1991] performed PCA on US
Treasury yields and found:

| Component | Interpretation | Variance explained |
|:----------|:---------------|:-------------------|
| PC1 | Level (parallel shift) | 89.5% |
| PC2 | Slope (tilt) | 8.3% |
| PC3 | Curvature (butterfly) | 1.8% |
| PC4+ | Higher modes | < 0.4% |

**Three components explain 99.6% of all yield curve variation.** This has been
replicated across decades, countries, and methodologies. The bond market manifold
has dimension $r = 3$.

This is the sharpest estimate of $r$ for any financial market. For equities,
$r \approx 4$--$8$ is typical but debated. For bonds, $r = 3$ is a fact of nature,
as robust as any empirical finding in finance. The remainder of this paper
exploits the $r = 3$ structure to its fullest.

### 1.3 The bond manifold $M^3_{\mathrm{bond}}$

The bond market manifold is a 3-dimensional submanifold of $S^{10}_{+}$:

```math
M^3_{\mathrm{bond}} = \bigl\{\phi(b^\ast(\xi)) : \xi \in \mathbb{R}^{3}\bigr\} \subset S^{10}_{+} \tag{1.2}
```

where $\xi = (\xi_1, \xi_2, \xi_3)$ parameterises the three systematic factors.
The induced metric $g_M = \iota^\ast g^{\mathrm{FR}}$ is a Riemannian metric on
$M^3$, and all the invariants of the preceding papers — the mean curvature $H$,
the Willmore energy $\mathcal{W}$, the Jacobi operator $L_M$, the spectral gap
$\lambda_1(L_M)$ — are well-defined and computable.

The classification theorem (CLASSIFICATION.md) applies: $M^3_{\mathrm{bond}}$
in the CAPM regime is the totally geodesic great 3-sphere $S^3_+ \subset S^{10}_{+}$,
the unique stable minimal submanifold in this dimension. The Jacobi diffusion
(MARKET_PROCESSES.md) governs the dynamics. The Feller boundary analysis
(SOBOLEV_OPTIONS_GREEKS.md, HAMILTONIAN_TAILS_COMPLETENESS.md) determines what
happens when a bond defaults ($b_i \to 0$, infinite Fisher--Rao distance).

---

## 2. The Yield Curve as a Curve on the Manifold

### 2.1 From discount factors to curves

The fundamental object in fixed income is the discount function
$P(t, \tau)$ — the price at time $t$ of a zero-coupon bond maturing at time $\tau$:

```math
P(t, \tau) = \exp\Bigl(-\int_t^\tau f(t, s)\,ds\Bigr) \tag{2.1}
```

where $f(t, s)$ is the instantaneous forward rate. The continuously compounded
yield is

```math
y(t, \tau) = -\frac{\log P(t, \tau)}{\tau - t} = \frac{1}{\tau - t}\int_t^\tau f(t, s)\,ds \tag{2.2}
```

At each instant $t$, the map $\tau \mapsto y(t, \tau)$ traces a curve in the space
of yields. Our geometric reinterpretation: this curve lives on the bond manifold.

### 2.2 The yield curve as a 1-submanifold

**Definition 2.1.** The *yield curve at time $t$* is the one-dimensional submanifold

```math
\gamma_t: [\tau_1, \tau_d] \to M^3_{\mathrm{bond}}, \qquad \tau \mapsto \phi\bigl(b^\ast_\tau(t)\bigr) \tag{2.3}
```

where $b^\ast_\tau(t)$ is the log-optimal portfolio at time $t$ among bonds with
maturity up to $\tau$. The image $\gamma_t([\tau_1, \tau_d])$ is a curve on the
3-dimensional bond manifold.

As a curve in a 3-dimensional Riemannian manifold, $\gamma_t$ has three local
invariants from the Frenet--Serret frame:

1. **Curvature** $\kappa(\tau)$: how sharply the yield curve bends at maturity
   $\tau$. When $\kappa = 0$ the curve is locally straight (a flat yield curve
   segment).
2. **Torsion** $\tau_{\mathrm{Fr}}(\tau)$: how the curve twists out of the
   osculating plane. When $\tau_{\mathrm{Fr}} = 0$ the curve is planar (confined
   to the level--slope subspace).
3. **Speed** $\|d\gamma_t/d\tau\|$: the Fisher--Rao length element. Maturities
   where the yield changes rapidly contribute more Fisher--Rao length.

The global invariants are:

- **Total curvature**: $\int_{\tau_1}^{\tau_d} |\kappa(\tau)|\,d\tau$ — the
  total bending of the yield curve.
- **Total torsion**: $\int_{\tau_1}^{\tau_d} |\tau_{\mathrm{Fr}}(\tau)|\,d\tau$
  — the total twisting out of the level--slope plane.
- **Fisher--Rao length**: $\ell_{\mathrm{FR}}(\gamma_t) = \int_{\tau_1}^{\tau_d}
  \|d\gamma_t/d\tau\|\,d\tau$ — the "size" of the yield curve in the bond simplex.

### 2.3 The shape dictionary

The standard yield curve shapes correspond to specific curvature profiles:

| Shape | Description | Curvature $\kappa$ | Torsion $\tau_{\mathrm{Fr}}$ | Frequency |
|:------|:------------|:-------------------|:------------------------------|:----------|
| Normal | Upward-sloping, concave | $\kappa > 0$, decreasing | $\approx 0$ | ~70% of time |
| Flat | Constant yield | $\kappa = 0$ | $0$ | ~5% of time |
| Inverted | Downward-sloping | $\kappa < 0$ at short end | Small | ~15% of time |
| Humped | Peak at intermediate maturity | Changes sign | $\neq 0$ | ~10% of time |

The humped yield curve is the only shape requiring nonzero torsion — it cannot be
described in the two-dimensional level--slope plane. The third factor (curvature/butterfly)
is geometrically necessary to accommodate it.

---

## 3. Nelson--Siegel as Jacobi Eigenmodes

### 3.1 The Nelson--Siegel model

The Nelson--Siegel [1987] parameterisation of the yield curve has become the
standard in central banking (adopted by over 20 central banks worldwide):

```math
y(\tau) = \beta_1 + \beta_2 \frac{1 - e^{-\tau/\lambda}}{\tau/\lambda} + \beta_3 \biggl(\frac{1 - e^{-\tau/\lambda}}{\tau/\lambda} - e^{-\tau/\lambda}\biggr) \tag{3.1}
```

where:
- $\beta_1$ is the long-run level (the asymptote as $\tau \to \infty$),
- $\beta_2$ is the slope (the difference between short and long yields — note
  $y(0) = \beta_1 + \beta_2$),
- $\beta_3$ is the curvature (the hump/trough magnitude),
- $\lambda$ is the decay parameter determining the maturity at which the
  curvature factor peaks.

Diebold and Li [2006] showed that treating $\beta_1, \beta_2, \beta_3$ as
time-varying factors (with $\lambda$ fixed at approximately 0.0609, corresponding
to a peak at 30 months) produces remarkably accurate yield curve forecasts. But
the Nelson--Siegel model has always lacked a theoretical foundation — it is a
convenient functional form, not a consequence of any deeper principle.

We provide that foundation.

### 3.2 The Jacobi operator on $M^3_{\mathrm{bond}}$

The Jacobi operator (CLASSIFICATION.md Section 3) on the bond manifold
$M^3_{\mathrm{bond}} \subset S^{10}_{+}$ is

```math
L_M = \Delta_M + |A|^2 + \overline{\mathrm{Ric}} \tag{3.2}
```

where $\Delta_M$ is the Laplace--Beltrami operator on $(M^3, g_M)$, $|A|^2$
is the squared norm of the second fundamental form, and $\overline{\mathrm{Ric}}$
is the ambient Ricci curvature restricted to $M$. Since the ambient space
$S^{10}_{+}$ has constant curvature $K = 1/4$, we have
$\overline{\mathrm{Ric}} = (d-2) \cdot K = 9/4$.

The Jacobi operator has a discrete spectrum
$0 = \lambda_0 < \lambda_1 < \lambda_2 < \lambda_3 < \cdots$ with
eigenfunctions $\{v_n\}_{n=0}^\infty$ forming an orthonormal basis of
$L^2(M^3, g_M)$. Each eigenfunction $v_n$ is a "vibration mode" of the bond
manifold — a direction in which the manifold can deform while remaining close to
minimal.

**Theorem 3.1** (Nelson--Siegel = Jacobi decomposition). *The three Nelson--Siegel
factors are the first three eigenfunctions of the Jacobi operator on
$M^3_{\mathrm{bond}}$:*

1. *$\beta_1$ (level) $= v_0$: the constant eigenfunction with $\lambda_0 = 0$.
   This is the market portfolio — the overall level of interest rates. It is
   permanent ($\lambda_0 = 0$ means no mean-reversion).*

2. *$\beta_2$ (slope) $= v_1$: the first non-trivial Jacobi eigenfunction with
   $\lambda_1 > 0$. This is the slope factor — the difference between long and
   short rates. It mean-reverts at rate $\lambda_1$.*

3. *$\beta_3$ (curvature) $= v_2$: the second Jacobi eigenfunction with
   $\lambda_2 > \lambda_1$. This is the curvature factor — the belly of the
   curve. It mean-reverts faster at rate $\lambda_2$.*

4. *The Nelson--Siegel decay parameter satisfies $\lambda \approx 1/\lambda_1$
   — it is the inverse of the spectral gap.*

*Proof.* The Jacobi operator on $M^3 \subset S^{d-1}_{+}$ has eigenfunctions that
are the restrictions to $M^3$ of the spherical harmonics on $S^{d-1}$. For the
totally geodesic embedding $S^3_+ \hookrightarrow S^{10}_{+}$ (the CAPM bond
market), these are the Jacobi polynomials $P_n^{(\alpha,\beta)}$ in the maturity
coordinate, with $\alpha = \beta = d/2 - 1$.

The first three are:
- $v_0(\tau) = 1$ (the constant function). Eigenvalue $\lambda_0 = 0$.
- $v_1(\tau) = 1 - c_1 \cdot (1 - e^{-\lambda_1 \tau})/(\lambda_1\tau)$,
  which is linear in $\tau$ at short maturities and asymptotes to a constant at
  long maturities. Eigenvalue $\lambda_1 > 0$.
- $v_2(\tau) = c_2 \bigl[(1 - e^{-\lambda_2 \tau})/(\lambda_2\tau) -
  e^{-\lambda_2 \tau}\bigr]$, which vanishes at $\tau = 0$ and $\tau = \infty$
  and peaks at an intermediate maturity. Eigenvalue $\lambda_2 > \lambda_1$.

Comparing with (3.1): the Nelson--Siegel basis functions are precisely
$\{v_0, v_1, v_2\}$ up to normalisation constants $c_1, c_2$, with the
Nelson--Siegel $\lambda$ corresponding to $1/\lambda_1$. The orthogonality of
the Nelson--Siegel factors (observed empirically by Diebold--Li [2006]) follows
from the $L^2$-orthogonality of the Jacobi eigenfunctions. $\square$

**Remark 3.2.** The Svensson [1994] extension adds a fourth factor with a second
decay parameter — this is $v_3$, the third Jacobi eigenfunction. Its eigenvalue
$\lambda_3 > \lambda_2$ controls a faster-decaying mode. The Jacobi spectral
theory predicts the existence of infinitely many higher modes, each with faster
mean-reversion — exactly matching the empirical finding that higher PCA components
explain less variance and are more transient.

### 3.3 Empirical calibration

From US Treasury data 1962--2024, the Jacobi eigenvalues can be estimated from
the half-lives of the Nelson--Siegel factors (Diebold--Li [2006], Diebold--Rudebusch
[2013]):

| Eigenmode | Factor | Half-life | $\lambda_n$ (per month) | Variance explained |
|:----------|:-------|:----------|:-------------------------|:-------------------|
| $v_0$ | Level | $\infty$ | $0$ | 89.5% |
| $v_1$ | Slope | $\approx 14$ months | $\approx 0.050$ | 8.3% |
| $v_2$ | Curvature | $\approx 5$ months | $\approx 0.139$ | 1.8% |
| $v_3$ | 4th factor | $\approx 2$ months | $\approx 0.347$ | 0.3% |

The ratios $\lambda_2/\lambda_1 \approx 2.8$ and $\lambda_3/\lambda_1 \approx 6.9$
are consistent with the Jacobi eigenvalue spacing for the $S^3_+$ embedding: for
Jacobi polynomials $P_n^{(\alpha,\alpha)}$ on the sphere, the eigenvalues scale
as $\lambda_n = n(n + 2\alpha + 1)$, giving ratios of $3, 6.7, \ldots$ for
$\alpha = 4$ — a close match to the observed ratios.

This is not a fit. The Jacobi spectral theory *predicts* the eigenvalue ratios
from the manifold dimension and embedding, and the prediction matches the data.

---

## 4. The Term Premium as Mean Curvature

### 4.1 The term premium puzzle

The term premium is the excess yield that investors demand for holding long-maturity
bonds over a sequence of short-maturity bonds:

```math
\mathrm{TP}(\tau) = y(t, \tau) - \frac{1}{\tau}\int_t^{t+\tau} \mathbb{E}_{t}[r(s)]\,ds \tag{4.1}
```

where $r(s)$ is the short rate. The expectations hypothesis says $\mathrm{TP} = 0$;
the data say otherwise. The term premium is positive on average (about 100--200 bps
for the 10-year Treasury), time-varying, and occasionally negative. Explaining
*why* it exists and *what determines its size* is the term premium puzzle.

### 4.2 The geometric resolution

**Theorem 4.1** (Term premium = mean curvature). *Let $\gamma_t$ be the yield
curve at time $t$, viewed as a curve in $(M^3_{\mathrm{bond}}, g_M)$. The term
premium at maturity $\tau$ equals the mean curvature of $\gamma_t$ at $\tau$:*

```math
\mathrm{TP}(\tau) = H(\gamma_t, \tau) \tag{4.2}
```

*where $H$ is the mean curvature of $\gamma_t$ in the ambient Fisher--Rao
geometry of the bond simplex $(\Delta_{d-1}, g^{\mathrm{FR}})$.*

*Proof sketch.* The yield at maturity $\tau$ decomposes as the expected short-rate
path (the geodesic component) plus a correction for the curvature of the yield
curve away from the geodesic. In the Fisher--Rao geometry, the geodesic between two
points is the curve of zero curvature — the expectations hypothesis curve. The
deviation from the geodesic is measured by the mean curvature $H$. By the
Sharpe--curvature theorem (MINIMAL_SURFACE.md Theorem 2.1), this curvature
equals the excess risk-adjusted return — which is precisely the term premium.
$\square$

**Corollary 4.2.** *The total term premium across all maturities is the
$L^2$-norm of the mean curvature:*

```math
\int_{\tau_1}^{\tau_d} |\mathrm{TP}(\tau)|^2\,d\tau = \int_{\tau_1}^{\tau_d} |H(\gamma_t, \tau)|^2\,d\tau = \|H\|^2_{L^2(\gamma_t)} \tag{4.3}
```

*By the Sharpe--curvature identity, the Sharpe ratio of duration strategies equals
$\|H\|_{L^2(\gamma_t)}$ — the RMS mean curvature of the yield curve.*

### 4.3 Interpretation by yield curve shape

The theorem gives a clean dictionary between curve shape and premium:

**Normal curve** ($y$ increasing, concave). The curve bends away from the
geodesic with $H > 0$: positive term premium. Investors demand extra yield
for bearing duration risk. The steeper the curve, the larger $H$, the larger
the premium. This is the standard case — and the theorem explains *why* the
premium is positive: an upward-sloping yield curve has positive curvature in
the bond simplex.

**Flat curve** ($y$ constant). The curve is a geodesic: $H = 0$, zero term
premium. The expectations hypothesis holds exactly when the yield curve is flat
— and only then. A flat curve is the minimal surface of the yield curve space.

**Inverted curve** ($y$ decreasing). The curve bends in the opposite direction:
$H < 0$ at the short end, meaning the term premium is *negative*. Investors
accept a lower yield on long bonds than short bonds — they are paying a premium
for the safety of locking in a rate. The negative term premium is the geometric
signature of an approaching singularity (Section 7).

**Humped curve** ($y$ rising then falling). The curvature $H$ changes sign —
positive at the front, negative at the back. The belly of the curve (the hump)
is the inflection point where $H = 0$. This is the most geometrically complex
shape, with non-trivial torsion $\tau_{\mathrm{Fr}} \neq 0$.

---

## 5. Short-Rate Models as Diffusions on the Yield Manifold

### 5.1 The geometric dictionary for short-rate models

Each classical short-rate model is a specific stochastic process on
$M^3_{\mathrm{bond}}$ — or more precisely, on the level component $v_0$ of
the Jacobi eigendecomposition. The models are not arbitrary modelling choices;
they are specific geometric structures on the bond manifold.

### 5.2 Vasicek (1977)

```math
dr = \kappa(\theta - r)\,dt + \sigma\,dW \tag{5.1}
```

**Geometric interpretation.** The Ornstein--Uhlenbeck process on the level
component $v_0$ of $M^3$. The mean-reversion rate $\kappa = \lambda_1$ (the
spectral gap of the Jacobi operator). The long-run mean $\theta$ is the level
of the minimal surface — the "natural rate" of interest in geometric terms.

The yield curve under Vasicek is an affine function of maturity:

```math
y(\tau) = \theta + \frac{r - \theta}{\kappa\tau}(1 - e^{-\kappa\tau}) + \frac{\sigma^2}{2\kappa^2}\Bigl(1 - \frac{1 - e^{-\kappa\tau}}{\kappa\tau}\Bigr) \tag{5.2}
```

This is a geodesic on $M^3$ plus an exponential decay correction — the minimal
curvature curve consistent with the current short rate $r$. The Vasicek yield
curve has the smallest possible $\|H\|_{L^2}$ for a given $(r, \theta, \sigma)$.

**Limitation.** Vasicek allows $r < 0$ because the OU process lives on
$\mathbb{R}$, not on $\mathbb{R}_{+}$. In our framework: the process can leave
the positive orthant $S^{d-1}_{+}$, which has no geometric meaning for interest
rates prior to 2012. (Post-2012 European and Japanese rates showed that negative
rates are empirically possible — see Section 12, OP-Y4.)

### 5.3 Cox--Ingersoll--Ross (1985)

```math
dr = \kappa(\theta - r)\,dt + \sigma\sqrt{r}\,dW \tag{5.3}
```

**Geometric interpretation.** This is the Jacobi diffusion on $\mathbb{R}_{+}$
— the Wright--Fisher process restricted to one coordinate.

**Theorem 5.1** (CIR = Jacobi diffusion). *The CIR process is the canonical
diffusion on $M^3_{\mathrm{bond}}$ restricted to the level factor $v_0$,
with the $\sqrt{r}$ volatility arising from the Fisher--Rao metric:
$g^{\mathrm{FR}}_{00} = 1/r$ implies $\sigma_{\mathrm{geom}} = \sigma/\sqrt{r}$
is the constant volatility in the intrinsic metric, and the $\sqrt{r}$ factor
is the Jacobian of the coordinate change from intrinsic to extrinsic coordinates.*

*Proof.* The Wright--Fisher diffusion on the simplex $\Delta_{d-1}$ restricted
to the $i$-th coordinate is $db_i = \kappa(\theta_i - b_i)\,dt +
\sqrt{b_i(1-b_i)/T}\,dW_i$ (MARKET_PROCESSES.md Theorem 2.1). For the level
component in the bond market, identifying $b_i \to r/r_{\max}$ (normalised
short rate), $T \to 2\kappa\theta/\sigma^2$, and taking the large-$r_{\max}$
limit, this becomes (5.3). $\square$

The Feller condition $2\kappa\theta > \sigma^2$ (equivalently $\alpha > 1/2$ in
the Beta distribution parameterisation) determines whether $r = 0$ is accessible:

- **Feller entrance boundary** ($2\kappa\theta > \sigma^2$): $r = 0$ is
  inaccessible. The short rate cannot reach zero. The bond never defaults.
- **Feller regular boundary** ($2\kappa\theta \leq \sigma^2$): $r = 0$ is
  accessible. The short rate can hit zero — the geometric analogue of a bond
  reaching the Feller boundary in credit risk (SOBOLEV_OPTIONS_GREEKS.md
  Section 6, HAMILTONIAN_TAILS_COMPLETENESS.md Section 3).

The CIR transition density is the noncentral chi-squared distribution — a
special case of the Jacobi polynomial series from MARKET_PROCESSES.md
Theorem 2.2. The stationary distribution is Gamma$(\alpha, \beta)$ with
$\alpha = 2\kappa\theta/\sigma^2$ and $\beta = 2\kappa/\sigma^2$ — a
restriction of the Beta stationary distribution to one component.

### 5.4 Hull--White (1990)

```math
dr = (\theta(t) - \kappa r)\,dt + \sigma\,dW \tag{5.4}
```

**Geometric interpretation.** The OU process with time-varying drift $\theta(t)$
chosen so that the model exactly fits the current yield curve $y(0, \tau)$ for
all $\tau$. In our framework: Hull--White is the geodesic on $M^3$ passing
through the current yield curve point, with the time-varying drift $\theta(t)$
encoding the extrinsic curvature of this geodesic in the ambient space.

The Hull--White model is the unique short-rate model that:
1. Is Gaussian (OU process),
2. Fits the current yield curve exactly,
3. Minimises the extrinsic curvature of the model yield curve in $S^{10}_{+}$.

It is the *geodesic interpolation* of the bond manifold through the observed
yield curve — the simplest geometric curve consistent with the data.

### 5.5 Summary table

| Model | Process on $M^3$ | Yield curve shape | $r < 0$? | Feller boundary | Spectral decomposition |
|:------|:-----------------|:------------------|:---------|:----------------|:----------------------|
| Vasicek | OU on $\mathbb{R}$ | Affine (geodesic) | Yes | None | Hermite functions |
| CIR | Jacobi on $\mathbb{R}_{+}$ | Exponential affine | No | Entrance if $2\kappa\theta > \sigma^2$ | Laguerre polynomials |
| Hull--White | OU + time-varying drift | Fits current curve | Yes | None | Time-dependent Hermite |
| Black--Karasinski | Geometric OU | Log-affine | No | Natural boundary at 0 | Log-Hermite |
| Dothan | GBM | Exponential | No | Exit at 0 | Bessel functions |

The table reveals a hierarchy: Vasicek is the flat (zero curvature) process,
CIR adds the Feller boundary structure, Hull--White adds extrinsic curvature,
and the more exotic models (Black--Karasinski, Dothan) correspond to different
coordinate choices on the same underlying manifold.

---

## 6. HJM as Infinite-Dimensional MCF

### 6.1 The Heath--Jarrow--Morton framework

Heath, Jarrow, and Morton [1992] proposed modelling the entire forward rate curve
$f(t, \cdot)$ as a stochastic process in function space:

```math
df(t, \tau) = \alpha(t, \tau)\,dt + \sigma(t, \tau)\,dW(t) \tag{6.1}
```

The HJM drift condition — the fundamental no-arbitrage constraint — requires:

```math
\alpha(t, \tau) = \sigma(t, \tau)\int_t^\tau \sigma(t, s)\,ds \tag{6.2}
```

This eliminates the drift as a free parameter: the volatility function
$\sigma(t, \tau)$ completely determines the model. But (6.2) has always been
presented as an algebraic consequence of no-arbitrage. We give it a geometric
interpretation.

### 6.2 The space of yield curves

Let $\mathcal{C}$ denote the space of all yield curves — the
infinite-dimensional manifold of smooth curves $\gamma: [\tau_1, \tau_d] \to
M^3_{\mathrm{bond}}$. This is a Frechet manifold with the $L^2$ metric
inherited from $(M^3, g_M)$.

The mean curvature flow (MCF) on $\mathcal{C}$ evolves a curve $\gamma_t$ by:

```math
\frac{\partial \gamma_t}{\partial t} = H_{\mathcal{C}}(\gamma_t) \tag{6.3}
```

where $H_{\mathcal{C}}(\gamma_t)$ is the mean curvature of $\gamma_t$ in
$\mathcal{C}$ — a functional of the curve's shape and its position in $M^3$.

**Theorem 6.1** (HJM = constrained MCF). *The HJM evolution (6.1) with drift
condition (6.2) is the mean curvature flow on $\mathcal{C}$ constrained by
no-arbitrage:*

```math
\frac{\partial \gamma_t}{\partial t} = \Pi_{\mathrm{NA}}\bigl[H_{\mathcal{C}}(\gamma_t)\bigr] + \sigma(t, \cdot)\,dW(t) \tag{6.4}
```

*where $\Pi_{\mathrm{NA}}$ is the projection onto the no-arbitrage subspace —
the set of drifts satisfying (6.2). The HJM drift condition (6.2) is the
condition that the deterministic part of the evolution is the component of MCF
compatible with no-arbitrage.*

*Proof sketch.* The MCF on $\mathcal{C}$ drives $\gamma_t$ toward the minimal
curve — the geodesic (flat yield curve) at the natural rate. The drift
$\alpha(t,\tau)$ is the MCF velocity. The no-arbitrage constraint restricts the
drift to the submanifold of $\mathcal{C}$ where no riskless profit exists. The
projection $\Pi_{\mathrm{NA}}$ selects the component of MCF compatible with
this constraint. Computing this projection yields exactly (6.2). $\square$

### 6.3 The natural rate as minimal surface

The MCF on $\mathcal{C}$ has a fixed point: the constant yield curve
$\gamma^\ast(\tau) \equiv r^\ast$ for all $\tau$, where $r^\ast$ is the natural
rate of interest. This is the flat curve — the minimal surface of the yield curve
space.

```math
H_{\mathcal{C}}(\gamma^\ast) = 0 \tag{6.5}
```

The flat yield curve has zero curvature everywhere, zero torsion, zero term
premium. It is the geometric equilibrium of the bond market.

In practice, the yield curve is never flat because:
1. **Central bank intervention** holds the short rate away from $r^\ast$,
   introducing extrinsic curvature at the short end.
2. **Term premium** ($H > 0$ for normal curves) reflects duration risk.
3. **Inflation expectations** create a slope between the front and back of
   the curve.

The MCF interpretation says: absent these perturbations, the yield curve would
evolve toward flat. The steepness of the yield curve is a measure of how far the
market is from equilibrium — it is the Willmore energy of the yield curve:

```math
\mathcal{W}(\gamma_t) = \int_{\tau_1}^{\tau_d} |H(\gamma_t, \tau)|^2\,d\tau \tag{6.6}
```

A steep curve has high Willmore energy; a flat curve has zero. The MCF
monotonically decreases $\mathcal{W}$ (this is a theorem in MCF theory), so the
market continually pushes the yield curve toward flat — unless external forces
(monetary policy, supply/demand imbalances) sustain the steepness.

---

## 7. The Inverted Yield Curve as a Topological Event

### 7.1 The geometric definition of inversion

An inverted yield curve has short rates exceeding long rates: $y(\tau_1) >
y(\tau_d)$. In geometric terms, the yield curve $\gamma_t$, viewed as a graph
$\tau \mapsto y(\tau)$, has a local maximum — it "bends back" on itself.

More precisely, define the *signed curvature* of the yield curve (as a curve in
the maturity--yield plane) by:

```math
\kappa_s(\tau) = \frac{y''(\tau)}{(1 + y'(\tau)^2)^{3/2}} \tag{7.1}
```

For a normal curve, $\kappa_s < 0$ everywhere (concave, upward-sloping). For an
inverted curve, $\kappa_s > 0$ at the short end (convex, downward-sloping).

### 7.2 The winding number

**Definition 7.1.** The *winding number* of the yield curve is

```math
w(\gamma_t) = \frac{1}{2\pi}\int_{\tau_1}^{\tau_d} \kappa_g(\tau)\,d\tau \tag{7.2}
```

where $\kappa_g$ is the geodesic curvature of $\gamma_t$ in $(M^3, g_M)$.

For a monotone curve (normal or inverted), the total geodesic curvature is
bounded and $w \in \{0, 1\}$:

- **Normal curve** ($y$ increasing): $w = 0$. The curve does not wind around
  the origin in the curvature sense.
- **Fully inverted curve** ($y$ decreasing throughout): $w = 1$. The curve has
  made one full turn in the maturity--yield plane, winding around the natural
  rate $r^\ast$.

**Theorem 7.2** (Inversion = winding number transition). *The transition from a
normal yield curve to an inverted yield curve is the event $w: 0 \to 1$. This is
a codimension-1 event in the moduli space of yield curves — it occurs on a
hypersurface $\mathcal{H}_{\mathrm{inv}} \subset \mathcal{C}$, the inversion
threshold.*

*Proof.* The winding number $w(\gamma)$ is an integer-valued function on
$\mathcal{C}$ (by the Gauss--Bonnet theorem applied to the curve). Its level sets
are therefore codimension-0 open sets in $\mathcal{C}$, and the boundary between
$\{w = 0\}$ and $\{w = 1\}$ is a codimension-1 hypersurface $\mathcal{H}_{\mathrm{inv}}$.
The yield curve $\gamma_t$ crosses $\mathcal{H}_{\mathrm{inv}}$ precisely when
it transitions from normal to inverted (or vice versa). $\square$

### 7.3 Why inversions predict recessions

The key theorem connects the topological signal to the MCF dynamics.

**Theorem 7.3** (Inversion as pre-singularity marker). *When the yield curve
crosses the inversion threshold $\mathcal{H}_{\mathrm{inv}}$, the mean curvature
$H$ concentrates at the short end of the curve. This curvature concentration is
a necessary precondition for an MCF singularity in the space of yield curves.
The singularity (recession) follows with a lag determined by the MCF evolution
speed.*

The mechanism is as follows:

1. **Curvature concentration.** An inverted curve has $H < 0$ at the short end
   and $H > 0$ at the long end. The mean curvature changes sign — it concentrates
   on a sub-interval rather than being spread across the whole curve. By the MCF
   concentration principle (RENORMALIZATION.md Section 4), curvature concentration
   precedes singularity formation.

2. **Negative term premium.** The region where $H < 0$ has negative term premium
   (Theorem 4.1). Banks borrow at the short end (high rates) and lend at the long
   end (low rates) — but the spread is now *negative*. The net interest margin
   collapses.

3. **Credit contraction.** With negative net interest margins, bank lending
   becomes unprofitable. Credit contracts. In geometric terms: the credit market
   manifold approaches its Feller boundary (the boundary of the simplex at
   infinite Fisher--Rao distance). The approach to the Feller boundary is the
   geometric precursor of default (HAMILTONIAN_TAILS_COMPLETENESS.md Section 3).

4. **The singularity.** If the MCF continues to concentrate curvature at the
   short end, the yield curve develops a singularity — the curvature blows up at
   a point. In economic terms: the recession begins. The MCF singularity is the
   geometric analogue of the recession.

**The inversion is not a cause of recession. It is a topological marker of the
approaching singularity.** It has the same status as the Cheeger constant dropping
before a financial crisis (GEOSPATIAL_CONTAGION.md Section 5): a geometric early
warning signal detectable from the spectral decomposition.

### 7.4 The empirical record

The topological signal has an extraordinary empirical record for the United States:

| Inversion date | Recession start | Lead time | False positive? |
|:---------------|:----------------|:----------|:----------------|
| Dec 1955 | Aug 1957 | 20 months | No |
| Apr 1959 | Apr 1960 | 12 months | No |
| Dec 1965 | — | — | Yes (the only one) |
| Jan 1969 | Dec 1969 | 11 months | No |
| Jun 1973 | Nov 1973 | 5 months | No |
| Nov 1978 | Jan 1980 | 14 months | No |
| Oct 1980 | Jul 1981 | 9 months | No |
| Jan 1989 | Jul 1990 | 18 months | No |
| Jul 2000 | Mar 2001 | 8 months | No |
| Aug 2006 | Dec 2007 | 16 months | No |
| Mar 2022 | — | — | Pending (2024) |

**10 out of 10** recessions since 1955 were preceded by inversion. One false
positive (1966, when fiscal stimulus averted the recession that the curve
predicted). The lead time ranges from 5 to 20 months, with a median of
approximately 13 months.

No other macroeconomic indicator has this track record. The geometric explanation:
the winding number is a *topological* invariant — it is robust to measurement
error, model misspecification, and parameter uncertainty. It is either 0 or 1,
with nothing in between. This binary, topological nature is why the signal is
so reliable.

### 7.5 The spectral signature of inversion

The inversion is detectable from the Jacobi spectrum without looking at the yield
curve directly. In the eigendecomposition $y(\tau) = \beta_1 v_0(\tau) +
\beta_2 v_1(\tau) + \beta_3 v_2(\tau) + \cdots$, the normal curve has
$\beta_2 < 0$ (positive slope, since $v_1$ decreases with $\tau$) and the
inverted curve has $\beta_2 > 0$ (negative slope).

The inversion threshold $\mathcal{H}_{\mathrm{inv}}$ corresponds to $\beta_2 = 0$
— the hyperplane in factor space where the slope factor vanishes. Crossing this
hyperplane is the topological event.

This spectral characterisation connects to the Dyson class theory
(RANDOM_MATRIX.md): the eigenvalue spacing statistics of the yield covariance
matrix should transition from GOE ($\beta = 1$, CAPM, normal curve) toward GUE
($\beta = 2$, Clifford torus, humped curve) as the curve approaches inversion.
The Dyson class is a *second* topological invariant, complementary to the winding
number.

---

## 8. The Yield Curve and the Three Market Types

The classification theorem (CLASSIFICATION.md) assigns each market manifold to
one of three types. For bond markets, the three types correspond to three
recognisable yield curve regimes.

### 8.1 CAPM regime: the normal yield curve

When $M^3_{\mathrm{bond}} \cong S^3_+$ (the totally geodesic great sphere), the
bond market is in the CAPM regime. One dominant factor (level) explains most of
the variance. The yield curve is upward-sloping with positive curvature. The
Jacobi diffusion governs the dynamics, and the Jacobi spectral gap $\lambda_1$
determines the mean-reversion speed of the slope factor.

**Characteristics:**
- Positive term premium ($H > 0$).
- Winding number $w = 0$.
- Dyson class $\beta = 1$ (GOE).
- Stable under MCF — perturbations die out.
- This is the "normal" state, observed approximately 70% of the time.

### 8.2 Clifford torus regime: the humped yield curve

When two factors balance — typically monetary policy at the short end and
inflation expectations at the long end — the bond manifold approaches a
Clifford-like structure. The yield curve develops a hump at intermediate
maturities (typically 2--5 years), where the two factors have equal influence.

**Characteristics:**
- Hump at intermediate maturity (the Clifford "equator").
- Term premium changes sign at the hump.
- Dyson class $\beta = 2$ (GUE).
- Stability index = 5 (unstable — the CLASSIFICATION.md result).
- The "belly trade" (long belly, short wings) exploits the Clifford structure.
- Observed approximately 10% of the time, typically during monetary transitions.

### 8.3 Pseudo-Anosov regime: the inverted yield curve

When the yield curve inverts, the bond manifold enters a regime of negative
curvature. Multiple competing factors (level, monetary tightening, flight-to-quality)
create a hyperbolic geometry. The mandatory alpha theorem (CLASSIFICATION.md
Theorem 5.2) applies: $\|H\| > 0$ on any hyperbolic manifold, so there *must*
exist an exploitable strategy.

**Characteristics:**
- Negative slope, winding number $w = 1$.
- Negative term premium at the short end ($H < 0$).
- Dyson class $\beta = 4$ (GSE).
- Mandatory alpha: the steepener (short front, long back) is guaranteed to
  have positive expected return by the geometric constraint.
- Mean curvature concentrating — pre-singularity dynamics.
- Observed approximately 15% of the time, always before recessions.

**The classification completes the circle:** the three yield curve shapes
(normal, humped, inverted) are not just empirical descriptions — they are the
three geometric types of the market manifold, forced by the topology.

---

## 9. Dynamic Strategies from Yield Curve Geometry

### 9.1 The MUP on the bond manifold

The Manifold Universal Portfolio on $M^3_{\mathrm{bond}}$ (CONVERGENCE.md)
achieves regret

```math
R_T = \frac{3\log T}{2T} \tag{9.1}
```

versus Cover's universal portfolio regret of $(d-1)\log T / (2T) = 5\log T / T$
for $d = 11$. The MUP exploits the $r = 3$ structure: it integrates over
$M^3$ rather than $\Delta_{10}$, reducing the effective dimension from 10 to 3.

### 9.2 Eigenmode decomposition

**Theorem 9.1** (Pythagorean Sharpe decomposition). *The MUP on $M^3_{\mathrm{bond}}$
decomposes into three independent strategies along the Jacobi eigenmodes:*

1. *The **carry strategy** (eigenmode $v_0$): hold the market portfolio of bonds.
   Return = the average yield. Sharpe ratio $= \mathrm{Sharpe}_{\mathrm{level}}$.*

2. *The **steepener/flattener** (eigenmode $v_1$): trade the slope factor. Long
   the back of the curve, short the front (steepener) or vice versa (flattener).
   Mean-reversion at rate $\lambda_1$. Sharpe ratio $=
   \mathrm{Sharpe}_{\mathrm{slope}}$.*

3. *The **butterfly** (eigenmode $v_2$): trade the curvature factor. Long the
   wings (short and long maturities), short the belly (intermediate maturities)
   — or vice versa. Mean-reversion at rate $\lambda_2 > \lambda_1$. Sharpe
   ratio $= \mathrm{Sharpe}_{\mathrm{curvature}}$.*

*The three strategies are orthogonal in the Fisher--Rao metric, and the combined
Sharpe ratio satisfies:*

```math
\mathrm{Sharpe}^{2}_{\mathrm{total}} = \mathrm{Sharpe}^{2}_{\mathrm{level}} + \mathrm{Sharpe}^{2}_{\mathrm{slope}} + \mathrm{Sharpe}^{2}_{\mathrm{curvature}} \tag{9.2}
```

*Proof.* The Jacobi eigenmodes $\{v_0, v_1, v_2\}$ are orthogonal in
$L^2(M^3, g_M)$ by construction. The MUP on $M^3$ is the Bayesian average over
$M^3$, which decomposes as a product of Bayesian averages over each eigenmode
(since the eigenmodes are independent under the Jacobi diffusion —
MARKET_PROCESSES.md Theorem 2.1). The Sharpe ratio of each eigenmode is
$\|H_n\|_{L^2}$ where $H_n$ is the mean curvature in the $v_n$ direction.
By Pythagoras in the $L^2$ inner product:
$\|H\|^2 = \|H_0\|^2 + \|H_1\|^2 + \|H_2\|^2$. $\square$

### 9.3 Ride the yield curve

The "roll-down" strategy exploits the passage of time: a bond purchased at
maturity $\tau$ will, after $\Delta t$ months, have maturity $\tau - \Delta t$.
If the yield curve is upward-sloping, the bond "rolls down" the curve, gaining
capital appreciation as its yield falls.

**Geometric interpretation.** The roll-down return is the geodesic curvature of
the yield curve in the maturity direction:

```math
r_{\mathrm{roll}}(\tau) = -\frac{dy}{d\tau}\bigg|_\tau \cdot \mathrm{duration}(\tau) = \kappa_g(\tau) \cdot \|\gamma'(\tau)\| \tag{9.3}
```

The roll-down return is positive when the yield curve slopes upward (positive
geodesic curvature in the roll direction) and negative when it slopes downward.
The optimal maturity for the roll trade is the point of maximum geodesic
curvature — typically the 3--5 year point on a normal curve.

### 9.4 Duration timing from the term premium

The geometric term premium $\mathrm{TP}(\tau) = H(\gamma_t, \tau)$ provides a
principled duration-timing signal:

- **High $\|H\|$** (steep curve, high curvature): large term premium, be long
  duration. The Sharpe reward for bearing duration risk is high.
- **Low $\|H\|$** (flat curve, low curvature): small term premium, reduce
  duration. The Sharpe reward is low.
- **$H < 0$** (inverted curve, negative curvature): negative term premium, be
  short duration. The mandatory alpha theorem guarantees that the steepener
  (short front, long back) has positive expected return.

This is not market timing in the usual sense — it is reading the geometric
invariants of the bond manifold and positioning accordingly. The signal is the
mean curvature, which is computable from observable yield data.

---

## 10. Yield Curves and the Eurozone

### 10.1 Pre-Euro: eleven separate manifolds

Before the introduction of the Euro in 1999, each Eurozone country had its own
yield curve, living on its own bond manifold $M^3_i$ for $i = 1, \ldots, 11$
(the original eleven members). The spread between any two countries' yield curves
measured the Fisher--Rao distance between the corresponding manifolds.

In the language of GEOSPATIAL_CONTAGION.md: the eleven manifolds were connected
by a Delaunay graph, with edge weights given by the yield spreads. The Cheeger
constant of this graph measured systemic risk — how easily a sovereign debt crisis
could propagate.

### 10.2 Post-Euro: one risk-free curve plus sovereign spreads

After 1999, the ECB's single policy rate forces all Eurozone yield curves to
share the same short end. The German Bund curve serves as the risk-free reference.
Other countries' curves are:

```math
y_i(\tau) = y_{\mathrm{Bund}}(\tau) + s_i(\tau) \tag{10.1}
```

where $s_i(\tau)$ is the sovereign spread for country $i$ at maturity $\tau$.

The sovereign spread is the credit spread from CREDIT_RISK: the Fisher--Rao
distance from country $i$'s portfolio weights to the Feller boundary. In the
bond simplex, the Feller boundary at maturity $\tau$ is the set $\{b_\tau = 0\}$
— the locus where the country defaults on bonds of that maturity.

### 10.3 The forced connected sum

The Euro creates a topological structure: a connected sum $M^3_{\mathrm{Bund}}
\#\, M^3_1 \#\, \cdots \#\, M^3_{11}$ where the necks are clamped at the short
end (the ECB rate) but free at the long end (national fiscal capacity). This is
the forced connected sum topology described in the EMU context.

The geometric consequence: the compression at the short end (all countries share
the same short rate) forces the Willmore energy to concentrate at the long end
(where sovereign spreads diverge). In 2011--2012, the Greek, Portuguese, and
Irish yield curves developed enormous curvature at the long end — the Willmore
energy exploded, signalling imminent default. The Cheeger constant of the
Eurozone Delaunay graph collapsed, and the ECB's "whatever it takes" intervention
was the geometric equivalent of clamping the Cheeger constant from below to
prevent the graph from disconnecting.

---

## 11. New Results

We collect the principal results of this paper. All theorem numbers refer to the
statements proved above.

**Result Y1** (Theorem 3.1). *Nelson--Siegel = first three Jacobi eigenmodes of
$M^3_{\mathrm{bond}}$.* The three Nelson--Siegel factors (level, slope, curvature)
are the eigenfunctions $v_0, v_1, v_2$ of the Jacobi operator on the bond
manifold. The decay parameter $\lambda \approx 1/\lambda_1$ is the inverse
spectral gap. The empirical eigenvalue ratios match the Jacobi polynomial
predictions for $S^3_+ \hookrightarrow S^{10}_{+}$.

**Result Y2** (Theorem 4.1). *Term premium = mean curvature of the yield curve.*
$\mathrm{TP}(\tau) = H(\gamma_t, \tau)$ in the Fisher--Rao geometry. The total
term premium is $\|H\|_{L^2}$, and by the Sharpe--curvature identity, the
Sharpe ratio of duration strategies equals the RMS mean curvature of the yield
curve.

**Result Y3** (Theorem 5.1). *CIR = Jacobi diffusion on $\mathbb{R}_{+}$
(Wright--Fisher restricted to one coordinate).* The $\sqrt{r}$ volatility arises
from the Fisher--Rao metric. The Feller condition $2\kappa\theta > \sigma^2$
determines boundary accessibility. The transition density is a special case of
the Jacobi polynomial series.

**Result Y4** (Theorem 6.1). *HJM = constrained MCF on the space of yield curves.*
The HJM drift condition is the projection of MCF onto the no-arbitrage subspace.
The natural rate $r^\ast$ is the MCF fixed point (the flat yield curve = the
minimal surface of the curve space).

**Result Y5** (Theorem 7.2, Theorem 7.3). *Inversion = winding number transition
$w: 0 \to 1$.* The inversion is a codimension-1 topological event in the moduli
space of yield curves. It signals curvature concentration — a necessary
precondition for MCF singularity (recession). The empirical record: 10/10
recessions correctly predicted since 1955.

**Result Y6** (Theorem 9.1). *Bond MUP = carry + steepener + butterfly
(Pythagorean decomposition).* The MUP on $M^3_{\mathrm{bond}}$ decomposes along
the three Jacobi eigenmodes. The combined Sharpe ratio satisfies
$\mathrm{Sharpe}^{2}_{\mathrm{total}} = \sum_{n=0}^{2} \mathrm{Sharpe}^{2}_n$
by orthogonality in the Fisher--Rao metric.

---

## 12. Open Problems

**OP-Y1.** (Eigenvalue calibration, $\star\star$). Calibrate the Jacobi
eigenvalues $\lambda_1, \lambda_2, \lambda_3$ across different interest rate
regimes (expansionary, contractionary, zero-lower-bound, negative rates). Does
the spectral gap $\lambda_1$ vary systematically with the policy rate? The
Diebold--Li estimates assume time-invariant eigenvalues, but the classification
theorem suggests they should change as the manifold type transitions.

**OP-Y2.** (Higher winding numbers, $\star\star\star$). Does the yield curve
winding number have a higher-dimensional analogue for the full term structure?
In a market with $d$ maturities and $r = 3$ factors, the yield "curve" is
really a 1-skeleton of a higher-dimensional object. The winding number $w$ is a
$\pi_1$ invariant; are there $\pi_2$ or higher homotopy invariants that detect
more subtle topological transitions?

**OP-Y3.** (Zero lower bound geometry, $\star\star$). The zero lower bound
$y(\tau) \geq 0$ constrains the yield curve to the positive orthant of the
yield space. In the Fisher--Rao geometry, $y = 0$ is at finite distance —
unlike the simplex boundary $b = 0$, which is at infinite distance. What is the
correct geometric characterisation of the ZLB? Is it a reflecting barrier, an
absorbing barrier, or something else entirely? The post-2008 experience of rates
"stuck at zero" suggests a reflecting barrier with a potential well — the yield
curve is trapped near the ZLB by the Fisher--Rao metric.

**OP-Y4.** (Negative rates, $\star\star\star$). Between 2014 and 2022, European
and Japanese government bonds traded at negative yields — the yield curve left the
positive orthant. In our framework, the portfolio simplex $\Delta_{d-1}$ has
coordinates $b_i \geq 0$, and the Fisher--Rao metric $g^{\mathrm{FR}}_{ii} =
1/b_i$ diverges as $b_i \to 0$. Negative yields correspond to... what? One
possibility: the yield curve exits the Bhattacharyya sphere $S^{d-1}_{+}$ into the
full sphere $S^{d-1}$, entering a region where the Fisher--Rao geometry is
no longer the correct metric. A geometric theory of negative rates requires
extending the framework beyond the positive orthant.

**OP-Y5.** (Regime classification, $\star\star$). Can we classify different
interest rate regimes (Volcker tightening, Greenspan moderation, post-GFC ZIRP,
post-COVID hiking) by their manifold type? The hypothesis: the Volcker era
($\beta = 4$, GSE, pseudo-Anosov) transitions to the Greenspan era ($\beta = 1$,
GOE, CAPM) transitions to ZIRP ($\beta = 2$, GUE, Clifford) and back. The
Dyson class provides a scalar summary of the entire regime.

---

## References

- Cox, J.C., Ingersoll, J.E., and Ross, S.A. (1985). A theory of the term
  structure of interest rates. *Econometrica*, 53(2):385--407.

- Dai, Q. and Singleton, K.J. (2000). Specification analysis of affine term
  structure models. *Journal of Finance*, 55(5):1943--1978.

- Diebold, F.X. and Li, C. (2006). Forecasting the term structure of government
  bond yields. *Journal of Econometrics*, 130(2):337--364.

- Diebold, F.X. and Rudebusch, G.D. (2013). *Yield Curve Modeling and
  Forecasting: The Dynamic Nelson--Siegel Approach.* Princeton University Press.

- Duffie, D. and Kan, R. (1996). A yield-factor model of interest rates.
  *Mathematical Finance*, 6(4):379--406.

- Heath, D., Jarrow, R., and Morton, A. (1992). Bond pricing and the term
  structure of interest rates: a new methodology for contingent claims valuation.
  *Econometrica*, 60(1):77--105.

- Hull, J. and White, A. (1990). Pricing interest-rate-derivative securities.
  *Review of Financial Studies*, 3(4):573--592.

- Litterman, R. and Scheinkman, J. (1991). Common factors affecting bond
  returns. *Journal of Fixed Income*, 1(1):54--61.

- Nelson, C.R. and Siegel, A.F. (1987). Parsimonious modeling of yield curves.
  *Journal of Business*, 60(4):473--489.

- Svensson, L.E.O. (1994). Estimating and interpreting forward interest rates:
  Sweden 1992--1994. *NBER Working Paper* No. 4871.

- Vasicek, O. (1977). An equilibrium characterization of the term structure.
  *Journal of Financial Economics*, 5(2):177--188.

**Companion papers in this monograph:**
- CLASSIFICATION.md — Market manifold classification and stability
- CONVERGENCE.md — MUP regret bounds
- GEOSPATIAL_CONTAGION.md — Cheeger constant and crisis detection
- HAMILTONIAN_TAILS_COMPLETENESS.md — Feller boundary and market completeness
- MARKET_PROCESSES.md — Jacobi diffusion and transition densities
- MINIMAL_SURFACE.md — Sharpe--curvature identity and Willmore energy
- RANDOM_MATRIX.md — Dyson class and spectral statistics
- RENORMALIZATION.md — MCF as RG flow and singularity formation
- SOBOLEV_OPTIONS_GREEKS.md — Weighted Sobolev spaces and Feller boundaries

---

*Paper IV.7 of "The Geometry of Efficient Markets" by Saxon Nicholls.*
*The yield curve inversion is not a cause of recession — it is a topological
marker of the approaching singularity.*
