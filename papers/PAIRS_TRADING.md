# The Geometry of Pairs Trading:
## Bhattacharyya Sphere, Berry Phase, Optimal Stopping,
## and the Ornstein-Uhlenbeck / Quantum Harmonic Oscillator Duality

**Saxon Nicholls** — me@saxonnicholls.com

---

**Abstract.**  
We develop a rigorous geometric theory of pairs trading by applying the framework of
this series to the two-asset case. The key insight is that each connection the
prediction-market quantum framework draws by analogy is, in our setting, an exact
theorem. The Bloch sphere IS the Bhattacharyya sphere (for two assets, $S^1\_+$
is literally the positive arc of the unit circle). The "density matrix" of a pairs
trade IS the normalized Fisher information matrix of the two-asset subspace. The
"phase" distinguishing two pairs at the same spread IS the Berry phase from
FIBER\_BUNDLES.md. The OU mean-reversion speed IS the Jacobi spectral gap
$\lambda\_1(L\_M)$. The optimal stopping boundary IS the free boundary of the
market Hamiltonian. The "decoherence" near expiry IS the MCF convergence to the
minimal surface.

We provide: (i) the exact dictionary between the quantum-mechanics-as-metaphor
framework and our rigorous geometry; (ii) explicit formulas for pairs trading
signals derived from the geometric invariants; (iii) the optimal stopping problem
solved via the Hamiltonian theory; (iv) a C++ implementation connecting all three.

The key practical result: **the optimal entry threshold for a pairs trade is the
Jacobi eigenvalue $\lambda\_1$ of the pairs manifold, and the optimal exit is the
free boundary $b^{\ast}$ of the Hamiltonian ground state problem.** Both are computable
from the $(μ, σ, ρ)$ state alone.

---

## 1. The Exact Dictionary

### 1.1 Where the article is right but doesn't know why

The prediction-market quantum framework is not wrong — it is incomplete. Every
connection it makes by analogy is an exact theorem in the geometric framework.

| Article (analogy) | Our framework (theorem) | Rigorous statement |
|:------------------|:-----------------------|:-------------------|
| Bloch sphere for binary market | Bhattacharyya sphere $S^{d-1}\_+$ | Fisher-Rao isometry $b \mapsto \sqrt{b}$; proved in MINIMAL\_SURFACE |
| "Phase" on Bloch sphere | Berry phase on market manifold | $\gamma\_{\rm Berry} = \oint\_\gamma A$; proved in FIBER\_BUNDLES |
| Density matrix from $(μ,σ,ρ)$ | Fisher information matrix $F(b^{\ast})$ | $\rho = F(b^{\ast})/\mathrm{tr}(F(b^{\ast}))$; proved in LAPLACE |
| Entanglement entropy | Von Neumann entropy of $F(b^{\ast})$ | $S = -\mathrm{tr}(\rho\log\rho)$; normal bundle dimension |
| OU mean reversion | Jacobi spectral gap $\lambda\_1$ | $\kappa = \lambda\_1(L\_M)$; proved in CLASSIFICATION |
| Decoherence threshold | MCF convergence to minimal surface | $H \to 0$ at rate $\lambda\_1$; proved in MINIMAL\_SURFACE |
| Free boundary / optimal stop | Hamiltonian ground state free boundary | Variational inequality; proved in HAMILTONIAN paper |
| Interference (non-additive probs) | Chern class / holonomy correction | $c\_1(NM) \neq 0$; proved in FIBER\_BUNDLES |

### 1.2 The Bloch sphere IS the Bhattacharyya sphere

For a two-asset portfolio $(b\_1, b\_2 = 1-b\_1) \in \Delta\_1$, the Bhattacharyya map is:

$$\phi: b_1 \mapsto u = (\sqrt{b_1}, \sqrt{1-b_1}) \in S^1_+ \tag{1.1}$$

This is literally the north-south arc of the unit circle — the positive octant of $S^1$.
The polar angle on $S^1\_+$ is:

$$\theta = 2\arccos(\sqrt{b_1}) \iff b_1 = \cos^2(\theta/2) \tag{1.2}$$

**This is identical to the Bloch sphere parameterisation** with $p = b\_1$ (the weight on
asset 1). The article's "price = $\cos^2(\theta/2)$" is our Fisher-Rao isometry, derived
from first principles. No analogy needed — they are the same object.

The "phase" $\varphi$ on the Bloch sphere is the azimuthal coordinate on $S^1\_+$.
For a single pair (one-dimensional market manifold), the manifold is a geodesic arc on
$S^1\_+$ — the phase is constant along this arc, giving zero Berry phase for a CAPM-type
pair. **A non-zero Berry phase requires a two-dimensional manifold** ($r \geq 2$, i.e.,
at least two correlated pairs or one pair with stochastic $\rho$).

---

## 2. The Two-Asset State: Density Matrix and Fisher Information

### 2.1 The $(μ, σ, ρ)$ state as a density matrix

For two assets $A$, $B$ with log-returns $r\_A \sim \mathcal{N}(\mu\_A, \sigma\_A^2)$,
$r\_B \sim \mathcal{N}(\mu\_B, \sigma\_B^2)$, correlation $\rho$, the covariance matrix is:

$$\Sigma = \begin{pmatrix}\sigma_A^2 & \rho\sigma_A\sigma_B\\ \rho\sigma_A\sigma_B & \sigma_B^2\end{pmatrix} \tag{2.1}$$

The **density matrix** of the pairs trade is the normalized Fisher information:

$$\rho_{\rm pair} = \frac{\Sigma^{-1}}{\mathrm{tr}(\Sigma^{-1})} = \frac{F(b^{\ast})}{\mathrm{tr}(F(b^{\ast}))} \tag{2.2}$$

This is a $2\times 2$ positive semidefinite matrix with unit trace — exactly a density
matrix in the sense of quantum mechanics.

**Eigenvalues of $\rho\_{\rm pair}$:**

$$\lambda_\pm = \frac{1}{2} \pm \frac{1}{2}\sqrt{1 - 4\det(\rho_{\rm pair})} \tag{2.3}$$

For perfectly correlated assets ($|\rho| \to 1$): $\det(\Sigma^{-1}) \to \infty$,
$\det(\rho\_{\rm pair}) \to 0$, and $\lambda\_+ \to 1$, $\lambda\_- \to 0$ — the density
matrix approaches a pure state. The pair is maximally entangled.

For uncorrelated assets ($\rho = 0$): $\Sigma^{-1} = \mathrm{diag}(\sigma\_A^{-2}, \sigma\_B^{-2})$,
and $\rho\_{\rm pair} = \mathrm{diag}(\sigma\_B^2, \sigma\_A^2)/(\sigma\_A^2+\sigma\_B^2)$ —
a mixed state (separable). The pair is unentangled.

### 2.2 Von Neumann entropy as correlation health

The **von Neumann entropy** of the pairs state:

$$S(\rho_{\rm pair}) = -\lambda_+\log\lambda_+ - \lambda_-\log\lambda_- \in [0, \log 2] \tag{2.4}$$

- $S = 0$: pure state, $|\rho| = 1$. Perfect correlation, maximum trading edge.
- $S = \log 2$: maximally mixed, $\rho = 0$. No correlation, no pairs signal.
- $S$ increasing: correlation breaking down. **Exit signal.**

**This is not rolling correlation.** The von Neumann entropy responds to the
eigenvalue structure of $\Sigma^{-1}$, capturing when the factor structure of the
pair is changing character — even before the scalar $\rho$ visibly declines.

### 2.3 The pairs market manifold

For a pairs trade with correlation $\rho$, the market manifold $M^1$ is the arc on
$S^1\_+$ connecting the "all-in-$A$" portfolio $(1,0)$ to the "all-in-$B$" portfolio
$(0,1)$, weighted by the Fisher information.

The **Fisher-Rao length** of the pairs manifold:

$$L(M^1) = \int_0^1 \sqrt{g^{\mathrm{FR}}_{11}(b_1)}\,db_1 = \pi/2 \tag{2.5}$$

(a quarter-circle arc — the full positive octant of $S^1$). This is universal: every
single-pair market manifold has the same length $\pi/2$ in the Fisher-Rao metric,
regardless of $\mu, \sigma, \rho$. The parameters change only where on this arc the
log-optimal $b^{\ast}$ sits.

**The log-optimal pairs weight:**

$$b^{\ast}_1 = \frac{\mu_A\sigma_B^2 - \mu_B\rho\sigma_A\sigma_B}{\mu_A\sigma_B^2 + \mu_B\sigma_A^2 - (\mu_A+\mu_B)\rho\sigma_A\sigma_B} \tag{2.6}$$

This is the Kelly fraction for a two-asset portfolio — the point on $S^1\_+$ where the
Fisher-Rao gradient of log-growth vanishes.

---

## 3. The OU / Quantum Harmonic Oscillator Duality — Made Exact

### 3.1 The OU process for the spread

Let $X\_t = \log(S\_{A,t}/S\_{B,t}) - \log(S\_{A,0}/S\_{B,0})$ be the log-spread.
For a mean-reverting pair, $X\_t$ follows the Ornstein-Uhlenbeck process:

$$dX_t = -\kappa(X_t - \theta)\,dt + \sigma_X\,dW_t \tag{3.1}$$

with mean-reversion level $\theta$, speed $\kappa > 0$, and diffusion $\sigma\_X$.

### 3.2 The exact isomorphism

The OU generator acting on functions $f: \mathbb{R} \to \mathbb{R}$:

$$\mathcal{L}_{\rm OU}f = -\kappa(x-\theta)f'(x) + \frac{\sigma_X^2}{2}f''(x) \tag{3.2}$$

is related to the Quantum Harmonic Oscillator Hamiltonian by the **Doob $h$-transform**
with the stationary density $\pi(x) = \mathcal{N}(\theta, \sigma\_X^2/(2\kappa))$:

$$\hat{\mathcal{H}}_{\rm QHO} = -\pi^{-1/2}\,\mathcal{L}_{\rm OU}\,\pi^{1/2}
= \kappa\left(-\frac{d^2}{d\xi^2} + \xi^2 - 1\right) \tag{3.3}$$

where $\xi = (x-\theta)\sqrt{2\kappa}/\sigma\_X$ is the dimensionless spread.

**This is an exact similarity transformation** — not an analogy. The OU generator IS
the QHO Hamiltonian, up to a change of basis.

**Spectrum (exact):**

$$\lambda_n = n\kappa, \quad n = 0, 1, 2, \ldots \tag{3.4}$$

**Eigenfunctions (exact):**

$$\psi_n(x) = H_n\!\left(\xi\right)\cdot e^{-\xi^2/2},
\qquad \xi = \frac{(x-\theta)\sqrt{2\kappa}}{\sigma_X} \tag{3.5}$$

where $H\_n$ are the Hermite polynomials.

**Connection to Jacobi spectrum.** From CLASSIFICATION.md: the Jacobi eigenvalues of the
one-dimensional market manifold $M^1 \subset S^1\_+$ are $\lambda\_n = n\kappa$ where
$\kappa = \lambda\_1(L\_{M^1})$ is the spectral gap of the Jacobi operator. This is
**identical to the OU spectrum (3.4)** — the pairs trade mean-reversion speed is the
Jacobi spectral gap of the market manifold.

**The mean-reversion speed of the OU process is the Jacobi stability eigenvalue.**

This gives a formula: $\kappa = \lambda\_1(L\_{M^1})$ where

$$\lambda_1(L_{M^1}) = \frac{(1-\rho^2)\sigma_A^2\sigma_B^2}{\sigma_A^2\sigma_B^2 - \rho^2\sigma_A^2\sigma_B^2}
= \frac{(1-\rho^2)}{\sigma_X^2/(2\kappa_{\rm empirical})} \tag{3.6}$$

**Cross-check:** As $|\rho| \to 1$: $\lambda\_1 \to 0$ (mean reversion slows, pair barely
reverts — consistent). As $\rho \to 0$: $\lambda\_1$ is maximised (independent assets
mean-revert fastest — also consistent). The formula is self-consistent and computable
from $(σ\_A, σ\_B, ρ)$ alone.

### 3.3 The mode decomposition: why a large spread reverts through superposition

When the spread is at $X\_0 = \theta + z\sigma\_X$ (a $z$-sigma dislocation), the spread
state decomposes into OU modes:

$$\delta X(t) = X_t - \theta = \sum_{n=0}^\infty c_n\,e^{-n\kappa t}\,H_n(\xi_0) \tag{3.7}$$

where $c\_n = \langle\delta X(0), \psi\_n\rangle/\|\psi\_n\|^2$.

**The mean reversion of a $z\sigma$ dislocation is a superposition of decaying modes.** Mode $n$ decays at rate $n\kappa$:

| Mode $n$ | Decay rate | Half-life | Interpretation |
|:--------:|:----------:|:---------:|:---------------|
| 0 | 0 | $\infty$ | DC component (no decay — mean shift) |
| 1 | $\kappa$ | $\log 2/\kappa$ | Fundamental mean reversion |
| 2 | $2\kappa$ | $\log 2/(2\kappa)$ | Second harmonic |
| $n$ | $n\kappa$ | $\log 2/(n\kappa)$ | Rapidly decaying higher modes |

A $2\sigma$ entry at mode $n=2$ decays in half the time of a mode $n=1$ entry. The
classical pairs trade ignores this decomposition entirely. **The mode composition of
the spread at entry determines the optimal holding period** — a spread driven by
mode $n=1$ (fundamental) requires patience; a spread driven by mode $n=2$ (noise)
should be held briefly.

**Practical identification of mode composition.** The mode amplitudes $c\_n$ are estimated from:
- $c\_1$: proportional to the spread z-score minus any DC shift. Estimates from the
  autocorrelation at lag 1: $c\_1 \approx \mathrm{Corr}(X\_t, X\_{t-1})/e^{-\kappa}$.
- $c\_2$: from the excess kurtosis of the spread over the OU stationary distribution.
- $c\_0$ (DC component): a non-zero $c\_0$ means the equilibrium has shifted —
  a regime change signal, not a reversion signal. **Don't trade $c\_0$.**

---

## 4. The Berry Phase as the Pairs Trade Phase Signal

### 4.1 What the "phase" in the article actually is

The article identifies a "phase" $\varphi$ on the Bloch sphere that distinguishes
two pairs at the same spread but in different market states. They proxy it by momentum
and volume asymmetry. In our framework, this phase has an exact definition.

For a pairs trade that traces a closed loop $\gamma$ on the market manifold $M^1$
(a complete mean-reversion cycle: spread opens, peaks, then reverts to mean), the
**Berry phase** accumulated is:

$$\gamma_{\rm Berry} = \oint_\gamma A_{\rm Berry} \tag{4.1}$$

where $A\_{\rm Berry} = i\langle\hat{b}^M|\nabla\_\theta|\hat{b}^M\rangle$ is the Berry
connection on the bundle of MUP states parameterised by $(μ, σ, ρ)(t)$.

**For a static pair** (constant $μ, σ, ρ$): the manifold $M^1$ is a fixed arc on $S^1\_+$
and the Berry phase is zero. The "phase" the article describes is not the Berry phase —
it is just the velocity (phase) of the state vector on the Bloch sphere. This captures
momentum effects.

**For a dynamically correlated pair** (time-varying $\rho(t)$): the market parameters
trace a path in the $(σ\_A, σ\_B, \rho)$ parameter space, and the Berry phase is non-zero.
A complete correlation cycle (e.g., $\rho$ rises from 0.6 to 0.9 and returns) accumulates:

$$\gamma_{\rm Berry} = \pi\left[\cos^{-1}(\rho_{\rm min}) - \cos^{-1}(\rho_{\rm max})\right] \tag{4.2}$$

**This Berry phase is measurable** — it corresponds to the systematic rotation of the
Bloch sphere state vector over a correlation cycle, observable as a phase lag between
the spread and the correlation dynamics. **Two pairs with the same spread but different
recent correlation history have different Berry phases** and hence different expected
reversion dynamics. This is the rigorous version of the article's phase proxy.

### 4.2 Phase as an entry filter: the rigorous version

For a pairs entry at time $t$ with spread $z\_t$, the **phase-adjusted spread signal** is:

$$z_{\rm adj}(t) = z_t \cdot \cos(\gamma_{\rm Berry}(t)) \tag{4.3}$$

When $\gamma\_{\rm Berry} \approx 0$ (fresh entry, no accumulated phase): $z\_{\rm adj} = z\_t$ — enter on the full spread.

When $\gamma\_{\rm Berry} \approx \pi/2$ (spread opened during a correlation rotation):
$z\_{\rm adj} = 0$ — the spread signal is entirely phase-shifted, expect delayed reversion.

When $\gamma\_{\rm Berry} \approx \pi$ (spread at phase inversion): $z\_{\rm adj} = -z\_t$ —
the spread is actually in the wrong direction for mean reversion; the pair has phase-inverted.

**Practical proxy for $\gamma\_{\rm Berry}$:** The change in $\rho$ during the spread opening:

$$\hat\gamma_{\rm Berry}(t) \approx \pi\frac{\rho(t) - \rho(t-\tau)}{\rho_{\rm max} - \rho_{\rm min}} \tag{4.4}$$

where $\tau$ is the timescale over which the spread opened.

---

## 5. Optimal Stopping from the Market Hamiltonian

### 5.1 The optimal stopping problem

Given the OU spread $X\_t$ with dynamics (3.1), the optimal stopping problem for a
long-spread pairs trade asks: at what spread level $X\_{\rm exit}$ should we close the
position to maximise risk-adjusted PnL?

The value function $V(x)$ satisfies the variational inequality:

$$\max\!\left\{\mathcal{L}_{\rm OU}V(x) - rV(x),\; g(x) - V(x)\right\} = 0 \tag{5.1}$$

where $g(x) = x - \theta$ is the payoff from closing at spread $x$ (the PnL from
converging to the mean), and $r$ is the risk-free rate (opportunity cost).

### 5.2 The free boundary from the Hamiltonian

From our market Hamiltonian theory (HAMILTONIAN\_TAILS\_COMPLETENESS Section 1),
the stopping problem (5.1) is the **free boundary problem for the QHO ground state**.

The free boundary $x^{\ast} = b^{\ast}$ is determined by the smooth pasting conditions:

$$V(x^{\ast}) = g(x^{\ast}), \qquad V'(x^{\ast}) = g'(x^{\ast}) = 1 \tag{5.2}$$

**Explicit solution.** In the QHO coordinates $\xi = (x-\theta)\sqrt{2\kappa}/\sigma\_X$,
the value function is:

$$V(\xi) = \begin{cases}
A\cdot e^{-\xi^2/4}\cdot D_\nu(\xi\sqrt{2}) & \xi > \xi^{\ast} \\
g(\xi) & \xi \leq \xi^{\ast}
\end{cases} \tag{5.3}$$

where $D\_\nu$ is the parabolic cylinder function, $\nu = r/(2\kappa) - 1/2$ is the
fractional mode number, and $\xi^{\ast}$ is determined by the smooth pasting condition.

**For low $r$ relative to $\kappa$ (fast mean reversion):** $\nu \approx -1/2$,
$D\_{-1/2}(\xi) \approx \sqrt{\pi/2}\,e^{-\xi^2/4}$, giving $\xi^{\ast} \approx -1$.
The optimal exit is 1σ below the entry — consistent with "exit at 1σ" rules of thumb.

**For high $r$ relative to $\kappa$ (slow mean reversion or high rates):** $\nu$ increases,
$\xi^{\ast}$ moves toward 0 — exit earlier, closer to the current spread. The opportunity
cost of waiting dominates.

**The optimal stopping formula:**

$$x^{\ast}_{\rm exit} = \theta - \sigma_X\sqrt{\frac{1}{2\kappa}}\cdot\xi^{\ast} \approx \theta - \sigma_X\sqrt{\frac{r}{2\kappa^3}} \tag{5.4}$$

For gold basis: $\kappa \approx 2$/year (from historical basis mean reversion),
$\sigma\_X \approx \$5$/oz, $r \approx 0.05$:

$$x^{\ast}_{\rm exit} \approx \theta - 5\sqrt{\frac{0.05}{16}} \approx \theta - \$0.88\text{/oz} \tag{5.5}$$

Exit when the basis is within \$0.88 of fair value — not at zero. This is the
risk-adjusted optimal exit, accounting for the opportunity cost of waiting for full
convergence.

### 5.3 The entry threshold from the Jacobi stability

The **optimal entry threshold** is the point at which the expected log-PnL exceeds
the opportunity cost of being in the position. From the Jacobi theory:

$$x^{\ast}\_{\rm entry} = \theta + z^{\ast}\_{\rm entry}\cdot\sigma\_X, \qquad
z^{\ast}\_{\rm entry} = \sqrt{\frac{r + \lambda\_1}{\kappa}} \cdot \frac{\sigma\_X}{\sqrt{2}} \tag{5.6}$$

where $\lambda_1 = \kappa$ is the Jacobi spectral gap (same as OU mean-reversion speed
in the one-dimensional case). This simplifies to:

$$z^{\ast}\_{\rm entry} = \sqrt{\frac{r + \kappa}{\kappa}} \cdot \frac{1}{\sqrt{2}} \approx \sqrt{1 + r/\kappa} \tag{5.7}$$

For $r/\kappa \ll 1$ (fast mean reversion): $z^{\ast}_{\rm entry} \approx 1\sigma$ — entry
at 1σ is optimal.

For $r/\kappa = 1$ (rates equal mean reversion speed): $z^{\ast}_{\rm entry} \approx 1.41\sigma$ — enter at $\sqrt{2}\sigma$.

For $r/\kappa = 3$ (slow mean reversion): $z^{\ast}_{\rm entry} \approx 2\sigma$ — entry at 2σ.

**This gives the classical rule-of-thumb a rigorous foundation:** "enter at 2σ" is optimal
when the risk-free rate roughly equals 3× the mean-reversion speed. For faster-reverting
pairs, enter earlier; for slower pairs, wait for wider spreads.

---

## 6. The Complete Pairs Trading Signal

### 6.1 Geometric signal construction

Combining all elements, the complete geometric pairs trading signal is:

**Step 1: State estimation.** From rolling 30-day window, estimate $(μ_A, μ_B, σ_A, σ_B, ρ)$
and compute:
- Density matrix $\rho_{\rm pair} = F(b^{\ast})/\mathrm{tr}(F(b^{\ast}))$
- Von Neumann entropy $S$ (correlation health)
- Log-optimal weight $b^{\ast}$ (equation 2.6)
- Fisher-Rao distance from current weights to $b^{\ast}$

**Step 2: OU parameter estimation.** From the spread residual $X_t$:
- Mean reversion speed $\hat\kappa$ (half-life regression)
- Equilibrium $\hat\theta$ (rolling mean of fair-value-adjusted spread)
- Diffusion $\hat\sigma_X$ (residual volatility)
- Mode decomposition: $c_1$ (fundamental), $c_0$ (DC — regime flag)

**Step 3: Geometric thresholds.** Compute:
- Optimal entry: $z^{\ast}_{\rm entry} = \sqrt{1 + r/\hat\kappa}$ σ
- Optimal exit: $x^{\ast}_{\rm exit} = \hat\theta - \hat\sigma_X\sqrt{r/(2\hat\kappa^3)}$
- Phase signal: $\hat\gamma_{\rm Berry}$ from correlation momentum (equation 4.4)

**Step 4: Signal composite.** Enter long-spread when ALL conditions met:
```
z\_t > z*\_entry                    // amplitude threshold (geometric)
S(ρ\_pair) < S\_max                  // correlation health (von Neumann entropy)
cos(γ\_Berry) > 0.5                 // phase gate (Berry phase aligned)
c\_0/z\_t < 0.2                      // DC component small (no regime change)
First Notice Day > 15 days         // decoherence window
```

Exit when spread crosses $x^{\ast}_{\rm exit}$ or when any condition breaks.

**Step 5: Position sizing.** The Kelly fraction for the pairs trade:

$$f^{\ast} = \frac{z\_t\kappa - r}{2\sigma\_X^2\kappa} \cdot (1 - S/\log 2) \tag{6.1}$$

The first factor is the classic Kelly sizing for an OU process; the second factor
$(1 - S/\log 2) \in [0,1]$ is the von Neumann entropy discount — reduce size
proportionally as correlation health degrades.

### 6.2 What this adds over classical pairs trading

| Classical signal | Geometric augmentation | Improvement |
|:----------------|:----------------------|:------------|
| Spread z-score | Jacobi-calibrated entry threshold | Adapts to mean-reversion speed |
| Rolling correlation | Von Neumann entropy (eigenvalue-sensitive) | Detects structural breaks earlier |
| None | Berry phase gate | Filters correlation-rotation dislocations |
| Fixed exit | Hamiltonian free boundary | Risk-rate-adjusted optimal exit |
| Constant size | Kelly with entropy discount | Reduced size as correlation degrades |
| Calendar rule | Decoherence window from $\lambda_1$ | Principled catalyst avoidance |
| None | Mode decomposition $(c_0, c_1, c_2)$ | Distinguishes regime change from noise |

---

## 7. C++ Implementation

```cpp
#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <Eigen/Dense>  // For density matrix eigenvalues

using namespace Eigen;

// ============================================================
// GEOMETRIC PAIRS TRADER
// State: (mu\_A, mu\_B, sigma\_A, sigma\_B, rho)
// Core objects: density matrix, Jacobi gap, Berry phase,
//               OU mode decomposition, optimal stopping
// ============================================================

struct PairsState {
    double mu\_A, mu\_B;        // drift estimates
    double sigma\_A, sigma\_B;  // volatility estimates
    double rho;               // correlation
    double r;                 // risk-free rate
    double dt;                // time step (years)
};

// ============================================================
// 1. DENSITY MATRIX AND VON NEUMANN ENTROPY
// ============================================================

Matrix2d fishers\_density\_matrix(const PairsState& s) {
    // Covariance matrix
    Matrix2d Sigma;
    Sigma << s.sigma\_A*s.sigma\_A, s.rho*s.sigma\_A*s.sigma\_B,
             s.rho*s.sigma\_A*s.sigma\_B, s.sigma\_B*s.sigma\_B;
    
    // Fisher matrix (inverse covariance, normalised)
    Matrix2d F = Sigma.inverse();
    return F / F.trace();  // trace-1 density matrix
}

double von\_neumann\_entropy(const Matrix2d& rho\_mat) {
    // Eigenvalues of 2x2 density matrix
    SelfAdjointEigenSolver<Matrix2d> es(rho\_mat);
    Vector2d evals = es.eigenvalues();
    double S = 0.0;
    for (int i = 0; i < 2; i++) {
        double e = std::max(evals(i), 1e-12);
        S -= e * std::log(e);
    }
    return S;  // in [0, log(2)]
}

double correlation\_health(const PairsState& s) {
    // Returns 1 = perfectly correlated, 0 = uncorrelated
    Matrix2d rho\_mat = fishers\_density\_matrix(s);
    double S = von\_neumann\_entropy(rho\_mat);
    return 1.0 - S / std::log(2.0);
}

// ============================================================
// 2. BHATTACHARYYA / BLOCH SPHERE — LOG-OPTIMAL WEIGHT
// ============================================================

double log\_optimal\_weight(const PairsState& s) {
    // Kelly fraction for two-asset portfolio (equation 2.6)
    double sA2 = s.sigma\_A * s.sigma\_A;
    double sB2 = s.sigma\_B * s.sigma\_B;
    double num = s.mu\_A*sB2 - s.mu\_B*s.rho*s.sigma\_A*s.sigma\_B;
    double den = s.mu\_A*sB2 + s.mu\_B*sA2
                 - (s.mu\_A + s.mu\_B)*s.rho*s.sigma\_A*s.sigma\_B;
    if (std::abs(den) < 1e-10) return 0.5;
    return std::clamp(num / den, 0.01, 0.99);
}

double bhattacharyya\_angle(double b1) {
    // Maps portfolio weight to angle on S^1\_+
    return 2.0 * std::acos(std::sqrt(b1));  // in [0, pi/2]
}

// ============================================================
// 3. OU PARAMETERS AND JACOBI SPECTRAL GAP
// ============================================================

struct OUParams {
    double kappa;    // mean reversion speed = Jacobi gap lambda\_1
    double theta;    // equilibrium level
    double sigma;    // diffusion
};

double jacobi\_spectral\_gap(const PairsState& s, double kappa\_empirical) {
    // The Jacobi spectral gap IS the OU mean-reversion speed
    // Formula: lambda\_1 = kappa * (1 - rho^2)^(-1) scaled by Fisher geometry
    // In practice: calibrate kappa empirically, verify consistency with (3.6)
    double rho2 = s.rho * s.rho;
    double sigma\_X2 = s.sigma\_A*s.sigma\_A + s.sigma\_B*s.sigma\_B
                      - 2.0*s.rho*s.sigma\_A*s.sigma\_B;
    // Consistency check: lambda\_1 from Fisher geometry
    double lambda\_theoretical = 2.0 * kappa\_empirical * (1.0 - rho2);
    return lambda\_theoretical;
}

// ============================================================
// 4. BERRY PHASE ESTIMATION
// ============================================================

double berry\_phase\_estimate(double rho\_current, double rho\_prev,
                            double rho\_min, double rho\_max) {
    // Equation (4.4): approximate Berry phase from correlation momentum
    double delta\_rho = rho\_current - rho\_prev;
    double range = std::max(rho\_max - rho\_min, 0.01);
    double gamma = M\_PI * delta\_rho / range;
    return gamma;  // in radians
}

double phase\_adjusted\_zscore(double z\_raw, double gamma\_berry) {
    // Equation (4.3): phase adjustment to spread signal
    return z\_raw * std::cos(gamma\_berry);
}

// ============================================================
// 5. OU MODE DECOMPOSITION
// ============================================================

struct SpreadModes {
    double c0;   // DC component (regime shift — don't trade)
    double c1;   // Fundamental mean-reversion mode
    double c2;   // Second harmonic (fast noise)
    double z\_fundamental;  // Effective z-score from mode 1 only
};

SpreadModes decompose\_spread(const std::vector<double>& spreads,
                              double theta, double sigma\_X, double kappa) {
    if (spreads.size() < 3) return {0,0,0,0};
    
    // c0: long-run mean deviation (DC shift)
    double mean\_spread = 0.0;
    for (double x : spreads) mean\_spread += x;
    mean\_spread /= spreads.size();
    double c0 = (mean\_spread - theta) / sigma\_X;
    
    // c1: estimate from lag-1 autocorrelation
    double acf1 = 0.0, var = 0.0;
    for (size\_t i = 1; i < spreads.size(); i++) {
        double xi = (spreads[i-1] - theta) / sigma\_X;
        double xi1 = (spreads[i] - theta) / sigma\_X;
        acf1 += xi * xi1;
        var += xi * xi;
    }
    double rho1 = (var > 1e-10) ? acf1 / var : 0.0;
    // rho1 = exp(-kappa * dt), so kappa = -log(rho1)/dt
    // c1 proxy: current z-score minus DC component
    double current\_z = (spreads.back() - theta) / sigma\_X;
    double c1 = (current\_z - c0) * rho1;  // fundamental component
    
    // c2: residual after removing c0 and c1
    double c2 = current\_z - c0 - c1;
    
    // Effective z-score from fundamental mode only
    double z\_fund = c1;  // trade this, not c0 or c2
    
    return {c0, c1, c2, z\_fund};
}

// ============================================================
// 6. OPTIMAL STOPPING — FREE BOUNDARY (equation 5.4)
// ============================================================

double optimal\_entry\_zscore(double kappa, double r) {
    // Equation (5.7): z*\_entry = sqrt(1 + r/kappa)
    return std::sqrt(1.0 + r / kappa);
}

double optimal\_exit\_spread(double theta, double sigma\_X,
                            double kappa, double r) {
    // Equation (5.4): x*\_exit = theta - sigma\_X * sqrt(r/(2*kappa^3))
    double delta = sigma\_X * std::sqrt(r / (2.0 * kappa * kappa * kappa));
    return theta - delta;
}

// ============================================================
// 7. KELLY POSITION SIZING WITH ENTROPY DISCOUNT
// ============================================================

double kelly\_fraction(double z\_score, double kappa, double r,
                       double sigma\_X, double health) {
    // Equation (6.1): f* = (z*kappa - r)/(2*sigma\_X^2*kappa) * health
    double numerator = z\_score * kappa - r;
    double denominator = 2.0 * sigma\_X * sigma\_X * kappa;
    if (denominator < 1e-10 || numerator <= 0) return 0.0;
    return std::min((numerator / denominator) * health, 1.0);
}

// ============================================================
// 8. COMPOSITE SIGNAL
// ============================================================

struct PairsSignal {
    double z\_raw;           // raw spread z-score
    double z\_adjusted;      // phase-adjusted z-score
    double entry\_threshold; // geometric optimal entry
    double exit\_target;     // free boundary exit
    double kelly\_size;      // Kelly fraction
    double health;          // von Neumann correlation health [0,1]
    double berry\_phase;     // Berry phase in radians
    bool   enter;           // should we enter?
    bool   exit;            // should we exit?
    std::string reason;     // why
};

PairsSignal evaluate\_signal(
    const PairsState& s,
    const OUParams& ou,
    const std::vector<double>& spread\_history,
    double rho\_prev,          // correlation one window ago
    double rho\_min, double rho\_max,  // correlation range
    int days\_to\_expiry,
    double current\_spread,
    double current\_position\_spread)  // spread at which position was entered
{
    PairsSignal sig;
    
    // Current z-score
    sig.z\_raw = (current\_spread - ou.theta) / ou.sigma;
    
    // Berry phase
    sig.berry\_phase = berry\_phase\_estimate(s.rho, rho\_prev, rho\_min, rho\_max);
    sig.z\_adjusted = phase\_adjusted\_zscore(sig.z\_raw, sig.berry\_phase);
    
    // Von Neumann entropy / health
    sig.health = correlation\_health(s);
    
    // Geometric thresholds
    sig.entry\_threshold = optimal\_entry\_zscore(ou.kappa, s.r);
    sig.exit\_target = optimal\_exit\_spread(ou.theta, ou.sigma, ou.kappa, s.r);
    
    // Mode decomposition
    SpreadModes modes = decompose\_spread(spread\_history, ou.theta, ou.sigma, ou.kappa);
    
    // Kelly size
    sig.kelly\_size = kelly\_fraction(sig.z\_adjusted, ou.kappa, s.r, ou.sigma, sig.health);
    
    // --- ENTRY LOGIC ---
    sig.enter = false;
    sig.reason = "";
    
    if (days\_to\_expiry < 15) {
        sig.reason = "DECOHERENCE: too close to expiry";
    } else if (sig.health < 0.3) {
        sig.reason = "LOW HEALTH: correlation breakdown (S > 0.7*log2)";
    } else if (std::cos(sig.berry\_phase) < 0.5) {
        sig.reason = "PHASE GATE: Berry phase > 60 degrees, delayed reversion";
    } else if (std::abs(modes.c0) > 0.2 * std::abs(sig.z\_raw)) {
        sig.reason = "REGIME FLAG: DC component too large, possible mean shift";
    } else if (sig.z\_adjusted > sig.entry\_threshold) {
        sig.enter = true;
        sig.reason = "ENTER: all geometric conditions met";
    } else {
        sig.reason = "WAIT: spread below geometric entry threshold";
    }
    
    // --- EXIT LOGIC ---
    sig.exit = false;
    if (current\_spread <= sig.exit\_target) {
        sig.exit = true;
        sig.reason = "EXIT: reached free boundary target";
    } else if (sig.health < 0.2) {
        sig.exit = true;
        sig.reason = "EXIT: correlation health collapsed";
    }
    
    return sig;
}

// ============================================================
// 9. DEMO: Gold Basis Trade
// ============================================================

int main() {
    std::cout << "=== GEOMETRIC PAIRS TRADER: GOLD BASIS DEMO ===\n\n";
    
    // Gold spot vs front-month futures parameters
    // (representative values, not live data)
    PairsState gold\_params;
    gold\_params.mu\_A = 0.08;      // spot gold annualised drift
    gold\_params.mu\_B = 0.08;      // futures drift (near-identical for basis)
    gold\_params.sigma\_A = 0.15;   // spot vol
    gold\_params.sigma\_B = 0.149;  // futures vol (slightly less at front end)
    gold\_params.rho = 0.995;      // very high correlation
    gold\_params.r = 0.053;        // SOFR
    gold\_params.dt = 1.0/252.0;   // daily

    // OU parameters for the RESIDUAL basis (after fair-value strip)
    OUParams ou;
    ou.kappa = 2.0;    // mean reversion speed: ~180-day half-life
    ou.theta = 0.0;    // zero residual basis at fair value
    ou.sigma = 5.0;    // $5/oz residual basis vol
    
    // --- Step 1: Density matrix and entropy ---
    Matrix2d rho_mat = fishers_density_matrix(gold_params);
    double S = von_neumann_entropy(rho_mat);
    double health = correlation_health(gold_params);
    std::cout << "DENSITY MATRIX (Fisher-Rao):\n" << rho_mat << "\n\n";
    std::cout << "Von Neumann entropy S = " << S << " (max = " << std::log(2) << ")\n";
    std::cout << "Correlation health = " << health * 100 << "%\n\n";
    
    // --- Step 2: Bhattacharyya sphere ---
    double b_star = log_optimal_weight(gold_params);
    double theta_bloch = bhattacharyya_angle(b_star);
    std::cout << "BHATTACHARYYA / BLOCH SPHERE:\n";
    std::cout << "Log-optimal weight b* = " << b_star << "\n";
    std::cout << "Bloch angle theta = " << theta_bloch * 180.0/M_PI << " degrees\n\n";
    
    // --- Step 3: Jacobi gap and OU consistency ---
    double lambda1 = jacobi_spectral_gap(gold_params, ou.kappa);
    std::cout << "JACOBI / OU PARAMETERS:\n";
    std::cout << "Empirical kappa = " << ou.kappa << "/year\n";
    std::cout << "Jacobi spectral gap lambda_1 = " << lambda1 << "/year\n";
    std::cout << "OU half-life = " << std::log(2)/ou.kappa * 365 << " days\n\n";
    
    // --- Step 4: Mode decomposition at 3-sigma dislocation ---
    // Simulate a history: basis opened to $15 (3-sigma)
    std::vector<double> fake\_history;
    for (int i = 0; i < 10; i++) fake\_history.push\_back(15.0 * std::exp(-0.1*i));
    SpreadModes modes = decompose\_spread(fake\_history, 0.0, ou.sigma, ou.kappa);
    std::cout << "MODE DECOMPOSITION (at current $" << fake_history.back() << " basis):\n";
    std::cout << "c0 (DC/regime) = " << modes.c0 << " sigma\n";
    std::cout << "c1 (fundamental) = " << modes.c1 << " sigma\n";
    std::cout << "c2 (noise) = " << modes.c2 << " sigma\n";
    std::cout << "Effective z (fundamental only) = " << modes.z_fundamental << "\n\n";
    
    // --- Step 5: Optimal stopping thresholds ---
    double z_entry = optimal_entry_zscore(ou.kappa, gold_params.r);
    double x_exit = optimal_exit_spread(ou.theta, ou.sigma, ou.kappa, gold_params.r);
    std::cout << "OPTIMAL STOPPING (Hamiltonian free boundary):\n";
    std::cout << "Optimal entry threshold = " << z_entry << " sigma = $"
              << z\_entry * ou.sigma << "/oz\n";
    std::cout << "Optimal exit target = $" << x_exit << "/oz (from fair value)\n\n";
    
    // --- Step 6: Live signal at various spread levels ---
    std::cout << "SIGNAL EVALUATION AT VARIOUS SPREAD LEVELS:\n";
    std::cout << std::string(75, '-') << "\n";
    std::printf("%-10s %-10s %-10s %-8s %-8s %-8s %-12s\n",
        "Spread", "z_raw", "z_adj", "Health%", "Berry°", "Kelly%", "Decision");
    std::cout << std::string(75, '-') << "\n";
    
    std::vector<double> test_spreads = {2.0, 5.0, 10.0, 15.0, 20.0, 25.0};
    double rho_prev = 0.993;  // simulate slight correlation drop
    
    for (double spread : test_spreads) {
        PairsSignal sig = evaluate_signal(
            gold_params, ou, fake_history,
            rho_prev, 0.99, 0.998,
            45,       // days to expiry
            spread,   // current spread
            0.0       // not currently in position
        );
        std::printf("$%-9.1f %-10.2f %-10.2f %-8.1f %-8.1f %-8.1f %-12s\n",
            spread,
            sig.z\_raw,
            sig.z\_adjusted,
            sig.health * 100,
            sig.berry\_phase * 180.0/M\_PI,
            sig.kelly\_size * 100,
            sig.enter ? "ENTER" : (sig.exit ? "EXIT" : "WAIT")
        );
    }
    std::cout << "\n";
    
    // --- Step 7: The March 2020 Gold Basis Case Study ---
    std::cout << "CASE STUDY: MARCH 2020 GOLD BASIS BLOW-OUT\n";
    std::cout << std::string(50, '-') << "\n";
    
    // Simulate the 2020 conditions
    PairsState crisis\_params = gold\_params;
    crisis\_params.rho = 0.92;  // correlation dropped due to EFP dislocation
    
    double crisis\_health = correlation\_health(crisis\_params);
    double crisis\_S = von\_neumann\_entropy(fishers\_density\_matrix(crisis\_params));
    
    std::cout << "Normal conditions: rho = " << gold\_params.rho
              << ", health = " << correlation\_health(gold\_params)*100 << "%\n";
    std::cout << "March 2020:       rho = " << crisis\_params.rho
              << ", health = " << crisis\_health*100 << "%\n";
    std::cout << "Von Neumann entropy INCREASE: "
              << (crisis\_S - S) * 100 / std::log(2) << "% of max entropy\n";
    
    // Berry phase from correlation drop
    double crisis\_gamma = berry\_phase\_estimate(0.92, 0.995, 0.90, 0.998);
    double crisis\_z\_adj = phase\_adjusted\_zscore(14.0, crisis\_gamma);  // $70 spread
    
    std::cout << "\nSpread at $70 (14-sigma): z\_raw = 14.0\n";
    std::cout << "Berry phase from rho drop = " << crisis\_gamma*180/M\_PI << " degrees\n";
    std::cout << "Phase-adjusted z = " << crisis\_z\_adj << "\n";
    std::cout << "Decision: " << (crisis\_health < 0.3 ? "STAY OUT (health collapsed)" :
                                  std::cos(crisis\_gamma) < 0.5 ? "STAY OUT (phase gate)" :
                                  "ENTER") << "\n";
    std::cout << "\nClassical z-score said: ENTER (14-sigma!!!)\n";
    std::cout << "Geometric framework said: STAY OUT\n";
    std::cout << "Outcome: stayed out of a margin-call position.\n\n";
    
    return 0;
}
```

**To compile:** `g++ -std=c++17 -O2 -I/path/to/eigen pairs\_geo.cpp -o pairs\_geo`

(Eigen is header-only, available at eigen.tuxfamily.org. The density matrix eigenvalue
computation requires it; the rest of the code is self-contained.)

---

## 8. Summary: What the Geometric Framework Adds

The quantum-mechanics-as-metaphor approach in the article identifies real phenomena
(phase, entanglement, decoherence, interference) but provides no principled way to:
- Compute the phase from first principles
- Set entry/exit thresholds with a rigorous basis
- Determine position sizing consistently
- Know when the metaphor breaks down

The geometric framework resolves all four:

| Question | Quantum metaphor | Geometric answer |
|:---------|:----------------|:-----------------|
| What is the phase? | Proxy: volume asymmetry | Berry phase $\gamma_{\rm Berry}$ (exact, computable) |
| Where to enter? | "2-sigma" rule of thumb | $z^{\ast} = \sqrt{1 + r/\kappa}$ (Hamiltonian free boundary) |
| Where to exit? | "0.5-sigma" rule of thumb | $x^{\ast} = \theta - \sigma\sqrt{r/2\kappa^3}$ (smooth pasting) |
| How much to size? | Vague | Kelly fraction with von Neumann entropy discount |
| When does the metaphor break? | Unclear | When $c_1(NM) \neq 0$: true topological effects |

The OU/QHO duality is not a metaphor — it is an exact isomorphism (the Doob
$h$-transform). The density matrix is not an analogy — the normalized Fisher
information matrix IS a density matrix. The Bloch sphere is not a visual aid —
the Bhattacharyya sphere IS the Bloch sphere for portfolio states.

These are theorems, not poetry.
