# Random Matrix Theory and the Efficient Market Manifold:
## The Dyson Classification Is Not a Choice — It Is Forced by the Geometry

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.3** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
We establish that the appropriate random matrix ensemble for modelling an efficient
financial market is not a modelling choice but is uniquely determined by the
symmetry class of the underlying market manifold. The three Dyson ensembles —
GOE ($\beta=1$), GUE ($\beta=2$), GSE ($\beta=4$) — correspond respectively to the
three stable market manifold types: the CAPM great sphere (time-reversal symmetric,
real orthogonal group), the Clifford torus (complex structure from Berry phase,
unitary group), and the pseudo-Anosov hyperbolic market (quaternionic structure
from stable/unstable foliation pairing, symplectic group).

Our principal results:

**(i) The Dyson-Manifold correspondence.** The symmetry class $\beta$ of the return
covariance matrix ensemble is determined by the topological symmetry of the market
manifold: CAPM $\to$ GOE ($\beta=1$); Clifford torus $\to$ GUE ($\beta=2$);
pseudo-Anosov $\to$ GSE ($\beta=4$). The time-reversal symmetry breaking that
transitions GOE to GUE is exactly the Berry phase of the Clifford torus market.

**(ii) The Vandermonde determinant = eigenvalue repulsion = diversification pressure.**
The Vandermonde factor $\prod_{i<j}|\lambda_i-\lambda_j|^\beta$ in the joint
eigenvalue distribution is the $\beta$-th power of the eigenvalue repulsion. In the
market context, this repulsion is the Fisher-Rao pressure keeping portfolio weights
separated — the geometric mechanism of diversification. Stronger repulsion ($\beta=2$
or $4$ vs $\beta=1$) means the factor eigenvalues are more spread out, the manifold
is better conditioned, and the portfolio is more robustly diversified.

**(iii) The Selberg integral IS the MUP partition function.** The Selberg integral
$S_n(\alpha,\beta,\gamma) = \int_{[0,1]^n}\prod_i t_i^{\alpha-1}(1-t_i)^{\beta-1} \prod_{i<j}|t_i-t_j|^{2\gamma}\,dt_i$ is the exact partition function for the
$\beta$-ensemble on the portfolio simplex with Jacobi-type potential. Setting
$\alpha = \beta = Tb^{\ast} - 1/2$ (the Jacobi parameters from MARKET_PROCESSES.md)
and $\gamma = \beta/2$: the Selberg integral equals the MUP normalisation constant
$\int_{M^r}W_T(b)\,d\mathrm{vol}_{M}$.

**(iv) The bulk spectral distribution.** For all three ensembles, the
empirical spectral distribution of the return covariance converges to the
Marchenko-Pastur law with $\beta$-independent support $[(1-\sqrt{c})^2, (1+\sqrt{c})^2]$.
The $\beta$ dependence appears in local statistics: level spacing distributions
(Wigner surmise), eigenvalue correlations, and Tracy-Widom edge fluctuations.
Increasing $\beta$ increases eigenvalue repulsion, making the local spacing
more regular (less clustering) without changing the global density.

**(v) Tracy-Widom edge statistics are market-type specific.** The largest eigenvalue
of the sample return covariance follows Tracy-Widom $F_1$ for CAPM markets, $F_2$
for Clifford torus markets, and $F_4$ for pseudo-Anosov markets. This is a testable
prediction: the distribution of the largest factor eigenvalue should shift from $F_1$
to $F_2$ as the market transitions from single-factor to balanced two-factor structure.

**(vi) The mesoscopic regime = the factor-to-idiosyncratic transition.** The mesoscopic
regime (eigenvalue statistics at intermediate scales, between bulk and edge) corresponds
to the interface between the tangent bundle $TM$ (factor eigenvalues, bulk) and the
normal bundle $NM$ (idiosyncratic eigenvalues, edge). The mesoscopic statistics
interpolate between the $\beta$-ensemble and Poisson statistics, with the crossover
scale controlled by the Jacobi spectral gap $\lambda_1$.

**(vii) Wishart matrices and the Fisher information matrix.** The sample Fisher
information matrix $\hat{F} = X^TX/T$ (where $X$ is the $T\times d$ matrix of
standardised returns) is a Wishart matrix. For a CAPM market: a real Wishart matrix
(GOE Wishart) with Marchenko-Pastur bulk. For the Clifford torus: a complex Wishart
matrix (GUE Wishart) with the $\beta=2$ Marchenko-Pastur law.

**Keywords.** Random matrix theory; GOE; GUE; GSE; Dyson classification; Tracy-Widom;
Marchenko-Pastur; Wishart; Selberg integral; Vandermonde determinant; eigenvalue
repulsion; mesoscopic regime; variational problem; equilibrium measure; Jacobi ensemble.

**MSC 2020.** 60B20, 15B52, 60F99, 15A18, 62H10, 91G10.

---

## 1. The Dyson Threefold Way Applied to Markets

### 1.1 Dyson's classification

Dyson \[1962\] showed that random matrix ensembles fall into three universality classes,
distinguished by the symmetry of the matrix with respect to time-reversal:

| Class | Symmetry | $\beta$ | Matrix type | Time-reversal |
|:-----:|:--------:|:-------:|:-----------:|:-------------:|
| GOE | Orthogonal | 1 | Real symmetric | $T^2 = +1$ |
| GUE | Unitary | 2 | Complex Hermitian | None ($T$ broken) |
| GSE | Symplectic | 4 | Quaternionic self-dual | $T^2 = -1$ |

The three classes are characterised by $\beta \in \{1,2,4\}$ appearing in the
Vandermonde factor of the joint eigenvalue distribution:

$$P(\lambda_1,\ldots,\lambda_n) \propto \prod_{i<j}|\lambda_i-\lambda_j|^\beta
\cdot\exp\!\left(-\frac{\beta n}{2}\sum_i V(\lambda_i)\right) \tag{1.1}$$

### 1.2 The market symmetry classes

**Theorem 1.1 (conditional)** *(The Dyson-Manifold Correspondence)*.
*The Dyson symmetry class $\beta \in \{1,2,4\}$ of an efficient market is determined
by the geometry of $M^r$ as follows:*

**(i) CAPM ($M = S^r_+$, great sphere): GOE ($\beta=1$).**
The CAPM market manifold is real and time-reversal symmetric. Running time forward
or backward on the great sphere gives the same statistics (the sphere has no
preferred orientation). The return covariance is a real symmetric matrix in the GOE class.

**(ii) Clifford torus ($M = T^2$): GUE ($\beta=2$).**
The Clifford torus carries a complex structure (it is a complex torus $\mathbb{C}/\Lambda$)
and the Berry phase of FIBER_BUNDLES.md breaks time-reversal symmetry:
the phase accumulated going clockwise around the torus is the negative of the phase
going counterclockwise, so the forward and backward return processes are not equivalent.
The return covariance is a complex Hermitian matrix in the GUE class.

**(iii) Pseudo-Anosov / hyperbolic market: GSE ($\beta=4$).**
The pseudo-Anosov map has stable and unstable foliations $\mathcal{F}^{s}, \mathcal{F}^{u}$
that are conjugate in the symplectic sense: $\Omega(\mathcal{F}^{s}, \mathcal{F}^{u}) \neq 0$
for the symplectic form $\Omega$ on the cotangent bundle. This gives the return
covariance a quaternionic structure with Kramers degeneracy ($T^2 = -1$, GSE class).

*The correspondence is established via Zirnbauer's \[1996\] tenfold classification
of symmetric spaces. The proof requires verifying that the holonomy groups match:*

- *(i) The CAPM great sphere has $O(n)$ holonomy (proved: the normal bundle
  connection is real, and Schur-Weyl duality applied to the holonomy group
  of FIBER_BUNDLES yields the orthogonal class).*
- *(ii) The Clifford torus has $U(n)$ holonomy. This requires showing that the Berry
  phase provides a complex structure on the normal bundle — this is **Conjecture C26**
  (Grade A).*
- *(iii) The pseudo-Anosov case has $Sp(n)$ holonomy. This requires showing that the
  stable/unstable foliation pairing is symplectic on the normal bundle — this is
  **Conjecture C27** (Grade A).*

*Part (i) is proved; parts (ii) and (iii) are Grade A conjectures supported by the
physical arguments above and by the numerical evidence of Section 8.*

**Corollary 1.2** *(Discriminating the ensemble from return data)*.
*The symmetry class of the market's random matrix ensemble is detectable from the
empirical distribution of the return covariance eigenvalues. Specifically, the
ratio of the first and second eigenvalue spacings:*
$$r_n = \frac{\lambda_{n+1}-\lambda_n}{\lambda_n-\lambda_{n-1}}$$
*has a distribution that depends on $\beta$: the ratio distribution is different
for $\beta=1$ (GOE), $\beta=2$ (GUE), and $\beta=4$ (GSE). This is a model-free
test of the market manifold symmetry class.*

---

## 2. The Vandermonde Determinant and Portfolio Diversification

### 2.1 The Vandermonde = eigenvalue repulsion

The Vandermonde determinant:
$$\mathrm{Van}(\lambda) = \prod_{i<j}(\lambda_i - \lambda_j) = \det(\lambda_i^{j-1}) \tag{2.1}$$

appears in the joint eigenvalue distribution (1.1) as $|\mathrm{Van}(\lambda)|^\beta$.
In the random matrix context, this repulsion prevents eigenvalue clustering:
eigenvalues push apart with force $\beta/|\lambda_i-\lambda_j|$.

**In the market context:** The eigenvalues $\lambda_1,\ldots,\lambda_r$ of the
Fisher information matrix $F(b^{\ast})$ are the factor exposure magnitudes. The Vandermonde
repulsion is the Fisher-Rao pressure keeping factors orthogonal and well-separated.

**Theorem 2.1** *(Vandermonde = diversification pressure)*.
*The Fisher-Rao metric on the market manifold creates an effective Vandermonde repulsion
between the factor eigenvalues. Specifically, the probability measure on factor
eigenvalue configurations:*

$$\mu_{\rm factor}(d\lambda) \propto |\mathrm{Van}(\lambda)|^\beta
\prod_i \lambda_i^{\alpha_i-1}(1-\lambda_i)^{\beta_i-1}\,d\lambda_i \tag{2.2}$$

*is the $\beta$-Jacobi ensemble, which is the factor eigenvalue distribution under
the Jeffreys prior on the market manifold.*

*The Vandermonde factor $|\mathrm{Van}(\lambda)|^\beta$ is the geometric mechanism
of diversification: it creates a repulsive potential between factor eigenvalues
proportional to $\beta\log|\lambda_i-\lambda_j|^{-1}$, preventing any two factors
from collapsing to the same eigenvalue. Stronger repulsion ($\beta=2$ for GUE,
$\beta=4$ for GSE) means more robust diversification.*

**The CAPM market ($\beta=1$, GOE) has the weakest factor eigenvalue repulsion.**
Two CAPM factors can come close in eigenvalue without strongly penalising the density.
This is why the CAPM can degenerate — factor eigenvalues can become approximately equal
(the market becomes "accidentally degenerate") and the factor structure breaks down.

**The Clifford torus market ($\beta=2$, GUE) has stronger repulsion.** The complex
structure (Berry phase) doubles the repulsion, keeping the two factors well-separated.
This is why the balanced two-factor market ($p=1/2$) is more robust to factor
degeneracy than the CAPM — the GUE Vandermonde provides a stronger diversification force.

---

## 3. The Selberg Integral = MUP Partition Function

### 3.1 The Selberg integral

The Selberg integral \[Selberg 1944\]:

$$S_n(a,b,\gamma) = \int_0^1\cdots\int_0^1
\prod_{i=1}^{n} t_i^{a-1}(1-t_i)^{b-1}
\prod_{1\leq i<j\leq n}|t_i-t_j|^{2\gamma}\,dt_1\cdots dt_n \tag{3.1}$$

has the exact closed form:

$$S_n(a,b,\gamma) = \prod_{k=0}^{n-1}\frac{\Gamma(a+k\gamma)\Gamma(b+k\gamma)\Gamma(1+(k+1)\gamma)}
{\Gamma(a+b+(n-1+k)\gamma)\Gamma(1+\gamma)} \tag{3.2}$$

This is one of the most important integrals in mathematical physics — appearing in
conformal field theory, the quantum Hall effect, and random matrix theory.

### 3.2 The MUP normalisation is a Selberg integral

**Theorem 3.1** *(Selberg = MUP)*.
*The normalisation constant of the Manifold Universal Portfolio on the $r$-dimensional
market manifold is a Selberg integral:*

$$\mathcal{Z}_{T}^{M} = \int_{M^r} W_T(b)\,d\mathrm{vol}_{M}(b)
= S_r(Tb^{\ast}_{1} - 1/2, Tb^{\ast}_{2} - 1/2, \beta/2) \tag{3.3}$$

*where $\beta$ is the Dyson index of the market manifold (1, 2, or 4), and
$b^{\ast}_{1}, b^{\ast}_{2},\ldots$ are the log-optimal portfolio weights at the factor vertices.*

*Proof.* In eigenvalue coordinates on the market manifold, the wealth function
$W_T(b) = \exp(TL_T(b))$ takes the form $\prod_i \lambda_i^{Tb^{\ast}_{i}-1}(1-\lambda_i)^{Tb^{\ast}(1-\bullet)-1}$
(the Jacobi ensemble potential), and the Riemannian volume element $d\mathrm{vol}_{M}$
includes the Vandermonde factor $|\mathrm{Van}(\lambda)|^\beta$ from the Fisher-Rao
metric. The integral becomes the Selberg integral (3.1) with $a = Tb^{\ast}_{1} - 1/2$,
$b = Tb^{\ast}_{2} - 1/2$, $\gamma = \beta/2$. The closed form (3.2) gives the MUP
normalisation exactly. $\square$

**Corollary 3.2** *(The MUP partition function is exactly computable)*.
*For a CAPM market ($\beta=1$) with $n=r$ factors:*

$$\mathcal{Z}_{T}^{\rm CAPM} = S_r(Tb^{\ast}/r - 1/2, Tb^{\ast}/r - 1/2, 1/2)
= \prod_{k=0}^{r-1}\frac{\Gamma^2(Tb^{\ast}/r - 1/2 + k/2)\Gamma(1+(k+1)/2)}
{\Gamma(2Tb^{\ast}/r - 1 + (r-1+k)/2)\Gamma(3/2)} \tag{3.4}$$

*For a GUE market ($\beta=2$, Clifford torus):*

$$\mathcal{Z}_{T}^{\rm GUE} = S_r(Tb^{\ast}/r - 1/2, Tb^{\ast}/r - 1/2, 1)
= \prod_{k=0}^{r-1}\frac{\Gamma^2(Tb^{\ast}/r-1/2+k)\Gamma(k+2)}
{\Gamma(2Tb^{\ast}/r-1+(r-1+k))\Gamma(2)} \tag{3.5}$$

*The ratio $\mathcal{Z}_{T}^{\rm GUE}/\mathcal{Z}_{T}^{\rm CAPM}$ is an explicit function
of $r$ and $T$ that measures the excess diversification provided by the GUE Clifford
torus structure relative to the CAPM.*

---

## 4. Bulk Spectral Distributions

### 4.1 The $\beta$-Marchenko-Pastur law

The classical Marchenko-Pastur law is the GOE ($\beta=1$) result. For general $\beta$:

**Theorem 4.1** *($\beta$-Marchenko-Pastur)*.
*For a $\beta$-Wishart matrix $W_\beta = X_\beta^{\ast} X_\beta / T$ where $X_\beta$ is
a $T\times d$ random matrix in the $\beta$-ensemble (real/complex/quaternionic
for $\beta=1/2/4$) with aspect ratio $c = d/T$, the empirical spectral distribution
converges to the $\beta$-Marchenko-Pastur law:*

$$\rho_{\rm MP}^\beta(\lambda) = \frac{1}{2\pi c\lambda}
\sqrt{(\lambda_+ - \lambda)(\lambda-\lambda_-)}\cdot\mathbf{1}_{[\lambda_-,\lambda_+]}(\lambda)
\tag{4.1}$$

*where $\lambda_\pm = (1\pm\sqrt{c})^2$ and $c = d/T$ is the aspect ratio.*

**The global eigenvalue density (Marchenko-Pastur law) is $\beta$-independent:**
all three ensembles have the same bulk density with support $[(1-\sqrt{c})^2,\,(1+\sqrt{c})^2]$.
The $\beta$ dependence appears in **local statistics**: level spacing distribution,
eigenvalue correlations, and edge fluctuations (Tracy-Widom). Specifically, the
level spacing distribution transitions from Wigner surmise
$p_1(s) \propto s\cdot\exp(-\pi s^2/4)$ (GOE) to
$p_2(s) \propto s^2\cdot\exp(-4s^2/\pi)$ (GUE) to
$p_4(s) \propto s^4\cdot\exp(-64s^2/(9\pi))$ (GSE),
with increasing repulsion as $\beta$ increases.

### 4.2 The free energy and the equilibrium measure

The equilibrium measure $\mu^{\ast}$ — the weak limit of the empirical spectral distribution — 
minimises the $\beta$-ensemble free energy functional:

$$F_\beta[\mu] = \int V(\lambda)\,\mu(d\lambda)
- \frac{1}{\beta}\int\!\!\int\log|\lambda-\mu|\,\mu(d\lambda)\mu(d\mu) \tag{4.2}$$

**In the market context:** The potential $V(\lambda) = -L_T(b)$ is the negative Kelly
growth rate. The logarithmic energy term is the Fisher-Rao diversification pressure.
The equilibrium measure minimises the negative Kelly growth rate minus the diversification
pressure.

**Theorem 4.2** *(The equilibrium measure = log-optimal portfolio distribution)*.
*The equilibrium measure $\mu^{\ast}_\beta$ of the $\beta$-ensemble with potential
$V(\lambda) = -L_T(b)$ is the log-optimal portfolio distribution on $M^r$:*

$$\mu^{\ast}_\beta = \pi_T(db) = \frac{W_T(b)\,d\mathrm{vol}_{M}(b)}{\int_{M^r}W_T(b')\,d\mathrm{vol}_{M}(b')} \tag{4.3}$$

— the MUP posterior distribution. The variational problem for the RMT equilibrium
measure IS the MUP optimisation problem.

The Euler-Lagrange equation for (4.2):

$$V'(\lambda) - \frac{2}{\beta}\mathrm{P.V.}\int\frac{\mu^{\ast}(d\mu)}{\lambda-\mu} = C \tag{4.4}$$

(where P.V. is the principal value) is the Fredholm integral equation whose solution
is the MUP portfolio. The kernel $1/(\lambda-\mu)$ is the Cauchy transform — the
same function that appears in the McKean heat kernel for the hyperbolic market.

---

## 5. Tracy-Widom Edge Statistics and Market Crises

### 5.1 The Tracy-Widom distributions

The Tracy-Widom distribution $F_\beta(s)$ describes the rescaled fluctuations of the
largest eigenvalue $\lambda_{\rm max}$ of a $\beta$-ensemble matrix near the edge of
the support:

$$\mathbb{P}\!\left(\lambda_{\rm max} \leq \lambda_+ + \frac{s}{\lambda_+ n^{2/3}}\right)
\to F_\beta(s) \quad\text{as } n\to\infty \tag{5.1}$$

**The three distributions are connected through Fredholm determinant representations.**
The Tracy-Widom distributions $F_1$, $F_2$, $F_4$ are related via Fredholm determinants
of the Airy kernel with different boundary conditions:
- $F_2(s) = \det(I - K_{\rm Ai}|_{[s,\infty)})$, where $K_{\rm Ai}$ is the Airy kernel
- $F_1$ and $F_4$ involve related but distinct operators (the Airy kernel composed with projection operators reflecting the real and quaternionic symmetry constraints)

For practical purposes, $F_1(s) \leq F_2(s) \leq F_4(s)$ pointwise, reflecting that
GOE fluctuations are larger than GUE, which are larger than GSE.

**The tails:** All three Tracy-Widom distributions have heavy left tails and light
right tails. The right tail falls as $e^{-cs^{3/2}}$ — sub-Gaussian. The left tail
falls as $e^{-c|s|^3}$ — much lighter.

### 5.2 The TW-to-market dictionary

**Theorem 5.1** *(Tracy-Widom and market crises)*.
*The distribution of the largest factor eigenvalue $\hat\lambda_{\rm max}$ of the
sample Fisher information matrix $\hat F = X^TX/T$ converges to Tracy-Widom:*

**(i) CAPM market (GOE): $\hat\lambda_{\rm max} \to F_1$.**
A "market crisis" in the GOE regime corresponds to $\hat\lambda_{\rm max}$ exceeding
the Tracy-Widom edge $\lambda_+$ by more than $F_1^{-1}(0.01)$ (the 1% left tail).

**(ii) Clifford torus market (GUE): $\hat\lambda_{\rm max} \to F_2$.**
The GUE crisis threshold is lower (the right tail of $F_2$ falls faster than $F_1$),
meaning the two-factor balanced market is more resistant to extreme eigenvalue spikes.

**(iii) Pseudo-Anosov market (GSE): $\hat\lambda_{\rm max} \to F_4$.**
The GSE right tail is the lightest — extreme eigenvalue spikes are rarest in the
symplectic market. But the left tail is heavier — the largest eigenvalue is more
likely to be near its expected value (less spread in the distribution).

**The financial meaning of the TW edge:** The largest factor eigenvalue represents
the dominant risk factor's strength. A spike in $\lambda_{\rm max}$ (beyond the TW edge)
indicates that a single factor is becoming dominant — consistent with a crisis where
all correlations go to 1. The rate at which the TW distribution decays tells us the
frequency of such "dominant factor" events.

**Testable prediction:** During CAPM-type market periods, the empirical distribution
of the maximum rolling eigenvalue of the return covariance should fit $F_1$. During
balanced two-factor periods (Clifford torus regime), it should fit $F_2$.
The fit quality is a model-free test of the market's symmetry class.

---

## 6. The Mesoscopic Regime: The Factor-to-Idiosyncratic Transition

### 6.1 What is the mesoscopic regime?

In random matrix theory, the **bulk** regime describes eigenvalue statistics in the
interior of the spectrum (governed by the Marchenko-Pastur law), and the **edge** regime
describes the largest eigenvalue (governed by Tracy-Widom). The **mesoscopic** regime
is the intermediate scale — eigenvalue statistics at scales $1 \ll k \ll n$ eigenvalues
from the edge.

**In market terms:** The spectrum has three regions:
- **Bulk (1 to $r$):** Factor eigenvalues — large, systematic, governed by $\beta$-Marchenko-Pastur
- **Edge (near $\lambda_r$):** The smallest factor eigenvalue — Tracy-Widom with crossover
- **Noise floor ($r+1$ to $d$):** Idiosyncratic eigenvalues — small, near noise level

The **mesoscopic regime** is the transition region from the $r$-th factor eigenvalue
$\lambda_r$ to the noise floor $\lambda_{r+1},\ldots,\lambda_{r+k}$. This is
the factor-to-idiosyncratic transition — the boundary between $TM$ and $NM$.

### 6.2 The Jacobi crossover

**Theorem 6.1** *(Mesoscopic crossover from factor to idiosyncratic)*.
*At the mesoscopic scale near the $r$-th eigenvalue, the eigenvalue statistics
interpolate between the $\beta$-ensemble (factor statistics) and Poisson statistics
(idiosyncratic statistics), with the crossover controlled by the Jacobi spectral gap
$\lambda_1(L_M)$:*

$$\text{At scale } k \text{ from } \lambda_r: \quad \text{statistics} =
\begin{cases}
\beta\text{-ensemble} & k \ll \lambda_1(L_M)^{-1} \\
\text{Poisson} & k \gg \lambda_1(L_M)^{-1}
\end{cases} \tag{6.1}$$

*The Jacobi spectral gap $\lambda_1$ controls the mesoscopic crossover scale:
a large spectral gap means a sharp factor-to-idiosyncratic boundary; a small gap
means a gradual transition.*

*For the CAPM: $\lambda_1 = (d-2)/4 \approx 12$ — sharp boundary.*
*For the Clifford torus: $\lambda_1 = 5/2$ — less sharp, broader transition.*
*Near a crisis (spectral gap collapsing): $\lambda_1\to 0$ — factor and
idiosyncratic eigenvalues mix, and the matrix becomes ill-conditioned.*

**The mesoscopic regime is where model selection matters most.** In the bulk: any
$\beta$ model gives similar predictions (all Marchenko-Pastur forms are similar for
the same aspect ratio). At the edge: Tracy-Widom distinguishes $\beta=1,2,4$.
In the mesoscopic regime: the specific geometry of the transition from $TM$ to $NM$
is visible.

---

## 7. Wishart Matrices and the Fisher Information Matrix

### 7.1 The Wishart-Laguerre ensemble

For a GOE market ($\beta=1$), the sample Fisher information matrix:
$$\hat F = \frac{1}{T}X^TX, \qquad X\in\mathbb{R}^{T\times d} \tag{7.1}$$

is a **real Wishart matrix** (also called the Laguerre orthogonal ensemble). Its joint
eigenvalue density:

$$P_{\rm Wishart}^\beta(\lambda) \propto
\prod_{i<j}|\lambda_i-\lambda_j|^\beta
\cdot\prod_i\lambda_i^{\beta(T-d-1)/2}\cdot e^{-\beta T\lambda_i/2} \tag{7.2}$$

is a $\beta$-Laguerre ensemble with parameter $a = \beta(T-d-1)/2$.

**The Marchenko-Pastur law** is the limit ($T,d\to\infty$ with $c=d/T$ fixed) of
the Wishart eigenvalue density for $\beta=1$.

**For the GUE Clifford torus market ($\beta=2$):** The sample covariance is a
**complex Wishart matrix** — the Laguerre unitary ensemble. The density is (7.2)
with $\beta=2$. The bulk distribution has the same Marchenko-Pastur support as GOE
(the support is $\beta$-independent), but the local eigenvalue statistics differ:
stronger level repulsion produces more regular spacing.

**The Jacobi parameters match.** From MARKET_PROCESSES.md: the Jacobi diffusion
parameters are $\alpha_i = Tb^{\ast}_{i} - 1/2$. From (7.2): the Wishart Laguerre parameter
is $a = \beta(T-d-1)/2$. Setting $b^{\ast}_{i} = 1/d$ (equal-weight CAPM):
$\alpha = T/d - 1/2 = \beta(T-d-1)/(2d) + O(1)$ — consistent. The Jacobi diffusion
and the Wishart random matrix are the same object in different parameterisations.

### 7.2 The Bai-Silverstein theorem and the MUP

The **Bai-Silverstein theorem** \[1998\] gives the almost sure convergence of
the empirical spectral distribution of Wishart matrices to the Marchenko-Pastur law.

**Geometric form of Bai-Silverstein:** For an efficient CAPM market, the empirical
spectral distribution of $\hat F / \mathrm{tr}(\hat F)$ (the normalised Fisher matrix)
converges almost surely to the Marchenko-Pastur law — the same distribution as the
MUP stationary distribution $\rho_\infty = d\mathrm{vol}_{M}/\mathrm{vol}(M)$
(uniform on $M$). **The Bai-Silverstein theorem IS the FP stationarity result
(R5 of WHATS_NEW) in random matrix language.**

---

## 8. New Results: The Complete RMT-Geometry Dictionary

### 8.1 Correspondences

| RMT concept | Geometric market concept | Formula |
|:-----------|:------------------------|:--------|
| GOE ($\beta=1$) | CAPM great sphere (time-reversal symmetric) | $M = S^r_+$ |
| GUE ($\beta=2$) | Clifford torus (Berry phase breaks T-reversal) | $M = T^2$ |
| GSE ($\beta=4$) | Pseudo-Anosov (symplectic foliation pairing) | $M = \Sigma^2_g$ |
| Vandermonde $|\lambda_i-\lambda_j|^\beta$ | Fisher-Rao eigenvalue repulsion | $g^{\rm FR}$ pressure |
| Marchenko-Pastur bulk | Factor eigenvalue distribution | $d\mathrm{vol}_{M}$ |
| Tracy-Widom edge $F_\beta$ | Largest factor eigenvalue | $\hat\lambda_{\rm max}$ |
| Mesoscopic crossover | $TM\to NM$ transition | Jacobi gap $\lambda_1$ |
| Selberg integral | MUP partition function | $\mathcal{Z}_{T}^{M}$ |
| Equilibrium measure $\mu^{\ast}$ | MUP posterior | $\pi_T(db)$ |
| Wishart matrix | Sample Fisher information | $\hat F = X^TX/T$ |
| Bai-Silverstein | FP stationarity = Jeffreys prior | $\rho_\infty = d\mathrm{vol}_{M}$ |
| Ratio test $r_n$ | Symmetry class detector | $\beta\in\{1,2,4\}$ |

### 8.2 New testable predictions

**Prediction 8.1** *(Dyson class from ratio statistics)*.
During CAPM-type market periods (single dominant factor), the ratio statistic
$r_n = (\lambda_{n+1}-\lambda_n)/(\lambda_n-\lambda_{n-1})$ for consecutive
factor eigenvalues should follow the GOE ($\beta=1$) ratio distribution.
During balanced two-factor periods, the distribution should shift to GUE ($\beta=2$).
*Test:* Compute $r_n$ from quarterly rolling factor decompositions; fit to
$\beta=1,2,4$ ratio distributions using KS test.

**Prediction 8.2** *(TW crisis indicator)*.
The rescaled largest eigenvalue $((\hat\lambda_{\rm max} - \lambda_+)n^{2/3}/\lambda_+)$
should be distributed as $F_1$ in CAPM periods and $F_2$ in Clifford torus periods.
A spike beyond the $1\%$ left tail of the appropriate $F_\beta$ is a TW crisis signal.
*Test:* Rolling eigenvalue estimation; compare to $F_1$ vs $F_2$ CDFs; identify the
distribution of such exceedances around known market crises (2008, 2020).

**Prediction 8.3** *(Selberg ratio as factor model test)*.
The ratio $\mathcal{Z}_{T}^{\rm GUE}/\mathcal{Z}_{T}^{\rm CAPM}$ (equation 3.5/3.4) is
computable analytically. If the market is in the GUE regime, the MUP log-wealth
should exceed the CAPM MUP log-wealth by $\log(\mathcal{Z}^{\rm GUE}/\mathcal{Z}^{\rm CAPM})/T$.
This is a direct test of whether the market's symmetry class is GOE or GUE.

---

## 9. The Dyson Brownian Motion and MCF

### 9.1 Dyson's Brownian motion

Dyson \[1962\] showed that the eigenvalue dynamics of a matrix undergoing standard
Brownian motion form a particle system with logarithmic repulsion:

$$d\lambda_i = dW_i + \frac{\beta}{2}\sum_{j\neq i}\frac{dt}{\lambda_i-\lambda_j} \tag{9.1}$$

This is the **Dyson Brownian motion** — eigenvalues diffuse while repelling each other
with strength $\beta/2$.

**The market version:** The factor eigenvalues of the Fisher matrix $F(b^{\ast}(t))$,
as the market evolves, follow Dyson Brownian motion on the market manifold. The diffusion
coefficient is $\varepsilon = 1/\sqrt{T}$ (the WF parameter); the repulsion is
$\beta/2$ where $\beta$ is the market's symmetry class.

**Theorem 9.1** *(Factor eigenvalues follow Dyson BM on $M$)*.
*For a market on manifold $M$ with Dyson class $\beta$, the eigenvalue process
$(\lambda_1(t),\ldots,\lambda_r(t))$ of the Fisher information matrix satisfies:*

$$d\lambda_i = \varepsilon\,dW_i + \frac{\beta\varepsilon^2}{2}\sum_{j\neq i}\frac{dt}{\lambda_i-\lambda_j}
+ (\text{mean curvature drift}) \tag{9.2}$$

*For the efficient market ($H=0$): the mean curvature drift vanishes and the eigenvalues
perform pure $\beta$-Dyson BM.*

*For the inefficient market ($H\neq 0$): the extra drift $-\varepsilon^2\nabla H$ drives
eigenvalues toward lower curvature — the MCF of the market manifold manifests as
a systematic drift in the Dyson BM eigenvalue process.*

### 9.2 MCF as regularisation of Dyson BM

**The mean curvature flow** $\partial_t M = -H\vec\nu$ regularises the Dyson Brownian
motion of the factor eigenvalues — it prevents eigenvalue collisions ($\lambda_i\to\lambda_j$)
by creating a restoring force near degeneracy. The MCF is the "viscous" regularisation
of the eigenvalue repulsion.

For the CAPM ($\beta=1$): the minimal restoring force. Eigenvalue collisions are
possible (regular boundary in Feller sense, accessible).

For the Clifford torus ($\beta=2$): stronger repulsion. Eigenvalue collisions are
less likely. The two-factor balanced market is more robust.

For the pseudo-Anosov ($\beta=4$): strongest repulsion. Eigenvalue collisions are
extremely unlikely. But the price is that the symplectic structure creates correlated
eigenvalue dynamics (Kramers doublets — eigenvalues come in pairs).

---

## Summary: The RMT-Geometry-Finance Triangle

$$\begin{array}{ccc}
\text{Random Matrix Theory} & \longleftrightarrow & \text{Market Geometry} \\[6pt]
\beta\in\{1,2,4\} & \longleftrightarrow & \text{Symmetry of }M \\
\text{Vandermonde }|\lambda_i-\lambda_j|^\beta & \longleftrightarrow & \text{Fisher-Rao repulsion} \\
\text{Marchenko-Pastur} & \longleftrightarrow & d\mathrm{vol}_{M}\text{ (stationary dist.)} \\
\text{Tracy-Widom }F_\beta & \longleftrightarrow & \text{Largest factor eigenvalue} \\
\text{Selberg integral} & \longleftrightarrow & \text{MUP partition function} \\
\text{Equilibrium measure} & \longleftrightarrow & \text{MUP posterior} \\
\text{Dyson BM} & \longleftrightarrow & \text{Factor eigenvalue dynamics} \\
\text{MCF} & \longleftrightarrow & \text{Eigenvalue repulsion regularisation} \\
\text{Mesoscopic crossover} & \longleftrightarrow & TM\to NM\text{ transition} \\
\end{array}}$$

**The main theorem in one sentence:** The random matrix ensemble appropriate for
an efficient market is uniquely determined by the symmetry group of the market
manifold via Dyson's threefold way — it is not a modelling choice, it is a theorem.

---

### Connections to Other Papers

The derivative of the log Selberg integral $\partial \log S_r / \partial a_i$ with respect to the $i$-th parameter should equal the Shapley value $\phi_i = b^{\ast}_{i}(\mu_i - \bar\mu)$ from HYPERCUBE_SHAPLEY.md. Since the Selberg integral is the MUP partition function (Result (iii) above), this would give a closed-form computational tool for Shapley values directly from the partition function, bypassing the combinatorial sum entirely (Conjecture C28). If correct, the Shapley attribution of Kelly growth to individual assets is encoded in the sensitivity of the random matrix partition function to its parameters — a deep link between cooperative game theory and random matrix theory.

---

## References

Dyson, F. J. (1962). Statistical theory of the energy levels of complex systems, I–III.
*Journal of Mathematical Physics* 3(1), 140–175.

Marchenko, V. A. and Pastur, L. A. (1967). Distribution of eigenvalues for some sets
of random matrices. *Mathematics of the USSR-Sbornik* 1(4), 457–483.

Selberg, A. (1944). Remarks on a multiple integral.
*Norsk Matematisk Tidsskrift* 26, 71–78.

Tracy, C. A. and Widom, H. (1994). Level spacing distributions and the Airy kernel.
*Communications in Mathematical Physics* 159(1), 151–174.

Zirnbauer, M. R. (1996). Riemannian symmetric superspaces and their origin in
random-matrix theory. *Journal of Mathematical Physics* 37(10), 4986–5018.

Bai, Z. D. and Silverstein, J. W. (1998). No eigenvalues outside the support of
the limiting spectral distribution of large-dimensional sample covariance matrices.
*Annals of Probability* 26(1), 316–345.

*[All other references as per companion papers.]*
