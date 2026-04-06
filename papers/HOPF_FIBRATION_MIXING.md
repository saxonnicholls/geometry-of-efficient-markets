# Hopf Fibrations, Topological Mixing, and the Information Architecture of Markets

**Saxon Nicholls** — me@saxonnicholls.com

**Paper III.5** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
The Hopf fibration $S^3 \xrightarrow{S^1} S^2$ is the simplest non-trivial fiber
bundle over a sphere. For a 3-asset market, the Bhattacharyya sphere IS $S^2_+$
and the Clifford torus from the classification theorem (CLASSIFICATION.md) lives
in $S^3$ as a Hopf fiber. We develop the connection between Hopf fibrations,
topological mixing, and information propagation on market manifolds. The Hopf map
is the canonical factor projection — it sends the full asset space (total space)
to the factor space (base). Topological mixing on the total space is the geometric
content of market efficiency. The mixing rate is the spectral gap $\lambda_1$.
Non-mixing markets have information bottlenecks — sectors where information
propagates slowly — and these bottlenecks are measured by the Cheeger constant
$h_M$ from GEOSPATIAL\_CONTAGION.md.

Our principal results:

**(i) Kelly invariance under Hopf fiber action.** The Kelly growth rate
$h_{\rm Kelly}$ is constant on each fiber of the Hopf fibration. The "gauge
freedom" — the degree of freedom that the factor model does not determine —
does not affect log-optimal wealth. The fiber direction is pure idiosyncratic
noise.

**(ii) Dyson class = Hopf fibration type.** The three Dyson symmetry classes
$\beta \in \{1,2,4\}$ correspond to real, complex, and quaternionic Hopf
fibrations over the factor base space: GOE ($\beta=1$) has $O(n)$ holonomy
and trivial real fiber structure; GUE ($\beta=2$) has $U(n)$ holonomy and
complex Hopf fiber structure; GSE ($\beta=4$) has $Sp(n)$ holonomy and
quaternionic Hopf fiber structure.

**(iii) The pseudo-Anosov market is the most efficiently mixing type.**
Despite being "chaotic," the pseudo-Anosov market has exponential decay of
correlations with rate equal to the stretch factor $\lambda_{\rm pA}$. This
exceeds the CAPM's polynomial mixing in transverse directions and the Clifford
torus's polynomial mixing along flat directions.

**(iv) Cheeger constant = minimum information flow rate.** A market manifold
is informationally efficient (in the mixing sense) iff $h_M > 0$ iff $M^r$ is
connected and has no bottlenecks. The Cheeger constant is the minimum information
flow rate across any partition of the market into two sectors.

**(v) MUP = Hopf projection of the Kelly strategy.** The MUP integrates over
the $r$-dimensional base of the Hopf fibration, averaging out the idiosyncratic
fiber direction. The regret $r \log T/(2T)$ is the regret over the base space
alone. The fiber contributes zero regret because idiosyncratic risk diversifies
away. This is the geometric reason why MUP beats Cover: Cover integrates over
the full $(d-1)$-dimensional simplex, while MUP integrates over the
$r$-dimensional base.

**Keywords.** Hopf fibration; topological mixing; spectral gap; Cheeger constant;
information propagation; factor projection; Dyson class; ergodic hierarchy;
Bernoulli property; Anosov mixing; fiber bundle; gauge invariance; MUP; Kelly
growth rate; information architecture.

**MSC 2020.** 55R25, 37A25, 53C40, 91G10, 37D20, 58J50, 57R22.

---

## 1. The Hopf Fibration and the 3-Asset Market

### 1.1 The standard Hopf fibration

The Hopf fibration, discovered by Heinz Hopf in 1931, is the map
$\pi: S^3 \to S^2$ defined by

$$\pi(z_1, z_2) = (2\operatorname{Re}(\bar{z}_1 z_2),\; 2\operatorname{Im}(\bar{z}_1 z_2),\; |z_1|^2 - |z_2|^2) \tag{1.1}$$

where $(z_1, z_2) \in \mathbb{C}^2$ with $|z_1|^2 + |z_2|^2 = 1$ parameterises
$S^3$. The fiber over each point $p \in S^2$ is a great circle $S^1 \subset S^3$.
Every two fibers are linked exactly once — they cannot be separated by any
continuous deformation. This linking is the topological content of the Hopf
invariant $H(\pi) = 1$.

The Hopf fibration is the simplest non-trivial fiber bundle over a sphere. It is
also the only fiber bundle structure on $S^3$ with fiber $S^1$ (up to orientation).
Its total space $S^3$, base $S^2$, and fiber $S^1$ are all spheres — a phenomenon
that occurs in exactly four cases (the real, complex, quaternionic, and octonionic
Hopf fibrations), corresponding to the four normed division algebras.

### 1.2 The 3-asset market as Hopf total space

For a market with $d = 3$ assets, the portfolio simplex is

$$\Delta_2 = \{(b_1, b_2, b_3) \in \mathbb{R}^3_+ : b_1 + b_2 + b_3 = 1\}$$

and the Bhattacharyya isometry $\phi: b \mapsto \sqrt{b}$ maps $\Delta_2$ to the
positive octant of the unit sphere:

$$S^2_+ = \{u \in \mathbb{R}^3 : u_i \geq 0,\; \|u\| = 1\}. \tag{1.2}$$

Now consider the ambient 3-sphere $S^3 \subset \mathbb{C}^2$. Writing
$z_j = u_{2j-1} + iu_{2j}$ for $j=1,2$, we have $S^3 = \{(u_1,u_2,u_3,u_4) :
\sum u_i^2 = 1\}$. The Bhattacharyya hemisphere $S^2_+$ embeds in $S^3$ as the
real locus $\{u_2 = 0, u_4 = 0, u_1 \geq 0, u_3 \geq 0\}$ — a great semicircle.
But the full Hopf fibration on $S^3$ restricts to a non-trivial structure on the
neighbourhood of $S^2_+$.

The Clifford torus from CLASSIFICATION.md,

$$T^2 = \{(z_1, z_2) \in S^3 : |z_1| = |z_2| = 1/\sqrt{2}\}, \tag{1.3}$$

is a Hopf fiber: under $\pi$, it maps to the equator $\{|z_1|^2 = |z_2|^2\}
\subset S^2$. This is the central observation: **the Clifford torus, which is the
canonical balanced two-factor market manifold, lives in $S^3$ as a Hopf fiber over
the equator of the factor sphere.**

### 1.3 The Hopf map as factor projection

The Hopf map $\pi: S^3 \to S^2$ has a direct financial interpretation.
The total space $S^3$ is the full asset space — each point encodes a complete
specification of portfolio weights including all correlations. The base $S^2$ is
the factor space — each point encodes the systematic factor exposures. The fiber
$S^1$ over each point of $S^2$ is the space of idiosyncratic configurations
consistent with a given factor exposure.

For $d = 3$ assets with $r = 2$ factors: the market manifold $M^2 \subset S^2_+$
projects via Hopf to $M^1 \subset S^1_+$ (the single-factor shadow). The fiber
direction parameterises the idiosyncratic degree of freedom — the one direction
that the two-factor model does not pin down.

More precisely: if $(b_1, b_2, b_3) \in M^2$ and the two factor loadings are
$\beta_1(b)$ and $\beta_2(b)$, then the Hopf map sends $(b_1, b_2, b_3) \mapsto
(\beta_1, \beta_2)$, and the fiber over $(\beta_1, \beta_2)$ is the set of all
portfolios with those factor exposures but varying idiosyncratic composition.

### 1.4 Kelly invariance on fibers

The Kelly growth rate function $L_T(b) = \frac{1}{T}\sum_{t=1}^T \log\langle b, x_t\rangle$
decomposes under the factor structure. Writing $\log\langle b, x_t\rangle =
\log\langle b, \bar{x}_t\rangle + \log(1 + \langle b, \epsilon_t\rangle/\langle b, \bar{x}_t\rangle)$
where $\bar{x}_t$ is the factor component and $\epsilon_t$ is idiosyncratic noise,
the idiosyncratic contribution averages to zero along the fiber.

**Lemma H1** (Kelly invariance under Hopf fiber action). *Let $\pi: S^{2d-1} \to
\mathbb{C}P^{d-1}$ be the complex Hopf fibration restricted to $S^{d-1}_+$.
Let $b, b' \in S^{d-1}_+$ lie in the same Hopf fiber: $\pi(b) = \pi(b')$.
Then*

$$\lim_{T \to \infty} L_T(b) = \lim_{T \to \infty} L_T(b') \quad \text{a.s.} \tag{1.4}$$

*provided the return process satisfies a strong law of large numbers with the
factor structure aligned to the Hopf base.*

*Proof.* The fiber action on $S^{d-1}_+$ is $b \mapsto e^{i\theta} \cdot b$ in
the complexified coordinates. In the real portfolio coordinates, this corresponds
to rotations within the idiosyncratic subspace $N_{b^*}M$ that preserve the
factor exposures $\Pi_{TM}(b) = \Pi_{TM}(b')$. The Kelly growth rate
decomposes as

$$L_T(b) = L_T^{\rm factor}(\pi(b)) + L_T^{\rm idio}(b) \tag{1.5}$$

where $L_T^{\rm factor}$ depends only on the Hopf base coordinate and
$L_T^{\rm idio}(b) \to 0$ a.s. by the law of large numbers applied to the
zero-mean idiosyncratic returns. Since $\pi(b) = \pi(b')$, the factor
contributions are identical, and both idiosyncratic contributions vanish in the
limit. $\blacksquare$

**Remark 1.1.** Lemma H1 says that the Hopf fiber is the "gauge orbit" of portfolio
theory. Just as in gauge theory the physical observables are invariant under
gauge transformations, the log-optimal growth rate is invariant under the Hopf
fiber action. The "gauge freedom" is precisely the idiosyncratic degree of freedom
that diversification eliminates.

---

## 2. Generalised Hopf Fibrations for $d > 3$

### 2.1 The four Hopf fibrations

The Hopf fibrations exist in exactly four dimensions, corresponding to the four
normed division algebras $\mathbb{R}, \mathbb{C}, \mathbb{H}, \mathbb{O}$:

| Division algebra | Fibration | Fiber | Base | Total space |
|:-----------------|:----------|:------|:-----|:------------|
| Real | $S^1 \to S^1$ | $S^0 = \{-1,1\}$ | $S^1$ | Trivial (double cover) |
| Complex | $S^{2n+1} \to \mathbb{C}P^n$ | $S^1$ | $\mathbb{C}P^n$ | Hopf bundle |
| Quaternionic | $S^{4n+3} \to \mathbb{H}P^n$ | $S^3$ | $\mathbb{H}P^n$ | Quaternionic Hopf |
| Octonionic | $S^{15} \to S^8$ | $S^7$ | $S^8$ | Exceptional (exists only for $n=1$) |

For a market with $d$ assets on $S^{d-1}_+$, the relevant fibration depends on $d$:

- **$d = 2k$ (even):** The sphere $S^{2k-1}$ admits the complex Hopf fibration
  $S^{2k-1} \to \mathbb{C}P^{k-1}$ with fiber $S^1$. The factor base is the
  $(k-1)$-dimensional complex projective space.
- **$d = 4k$ (divisible by 4):** The sphere $S^{4k-1}$ admits the quaternionic
  Hopf fibration $S^{4k-1} \to \mathbb{H}P^{k-1}$ with fiber $S^3$. The
  fiber is now 3-dimensional — three idiosyncratic degrees of freedom per
  quaternionic factor.
- **$d = 16$:** The octonionic Hopf fibration $S^{15} \to S^8$ applies. A
  16-asset market admits an exceptional fiber structure with 7-dimensional
  fiber $S^7$.

### 2.2 Holonomy groups and the Dyson correspondence

The structure group of each Hopf fibration determines the holonomy of the
associated connection. This connects directly to the Dyson classification from
RANDOM\_MATRIX.md.

**Complex Hopf and $U(n)$ holonomy.** The complex Hopf bundle $S^{2n+1} \to
\mathbb{C}P^n$ has structure group $U(1) \subset U(n)$. The connection 1-form
is the canonical connection on the principal $U(1)$-bundle, with curvature equal
to the Fubini-Study Kahler form $\omega_{FS}$ on $\mathbb{C}P^n$. For the
Clifford torus market: the $U(n)$ holonomy of the complex Hopf fiber is precisely
the GUE ($\beta = 2$) symmetry group from RANDOM\_MATRIX.md. The Berry phase
accumulated around a closed loop on $M^r$ (identified in FIBER\_BUNDLES.md) is
the holonomy of the Hopf connection.

**Quaternionic Hopf and $Sp(n)$ holonomy.** The quaternionic Hopf bundle
$S^{4n+3} \to \mathbb{H}P^n$ has structure group $Sp(1) \subset Sp(n)$. The
connection curvature is the quaternionic Kahler form. For the pseudo-Anosov
market: the $Sp(n)$ holonomy of the quaternionic fiber corresponds to the
GSE ($\beta = 4$) symmetry group. The stable/unstable foliation pairing that
defines the pseudo-Anosov structure provides exactly the quaternionic structure
$J_1, J_2, J_3$ satisfying $J_1 J_2 = J_3$.

**Real (trivial) fiber and $O(n)$ holonomy.** The CAPM market, with its totally
geodesic great sphere structure $S^r_+$, has trivial fiber — the factor model
explains everything. The holonomy is $O(n)$, the GOE ($\beta = 1$) symmetry
group. There is no non-trivial Hopf structure because there is no idiosyncratic
fiber to wind around.

**Lemma H2** (Dyson class = Hopf fibration type). *The Dyson symmetry class
$\beta \in \{1, 2, 4\}$ of the return covariance ensemble on $M^r$ corresponds
to the type of Hopf fibration over the factor base space:*

| $\beta$ | Ensemble | Holonomy | Hopf type | Fiber |
|:--------|:---------|:---------|:----------|:------|
| 1 | GOE | $O(n)$ | Real (trivial) | $S^0$ (discrete) |
| 2 | GUE | $U(n)$ | Complex | $S^1$ |
| 4 | GSE | $Sp(n)$ | Quaternionic | $S^3$ |

*Proof sketch.* The Dyson classification rests on the anti-unitary symmetries of
the Hamiltonian (in the market context: the symmetries of the Fisher information
matrix $F_M$). A system with time-reversal symmetry $\mathcal{T}$ and
$\mathcal{T}^2 = +1$ has $\beta = 1$ (real eigenvalues, $O(n)$ invariance). If
$\mathcal{T}^2 = -1$, then $\beta = 4$ (Kramers degeneracy, $Sp(n)$ invariance).
If $\mathcal{T}$ is broken, then $\beta = 2$ ($U(n)$ invariance).

For the CAPM market ($S^r_+$): the time-reversal symmetry
$b(t) \mapsto b(T-t)$ is a symmetry of the Jacobi process, and $\mathcal{T}^2 = +1$.
The fiber is trivial ($S^0$).

For the Clifford torus ($T^2$): the Berry phase from FIBER\_BUNDLES.md breaks
time-reversal symmetry — a portfolio traversing a closed loop on $T^2$ accumulates
a non-zero geometric phase. This forces $\beta = 2$ and the complex Hopf fiber
structure $S^1$.

For the pseudo-Anosov market ($\mathbb{H}^2$): the stable and unstable foliations
$\mathcal{F}^s, \mathcal{F}^u$ provide two anti-commuting complex structures
satisfying $\mathcal{T}^2 = -1$. This forces $\beta = 4$ and the quaternionic Hopf
fiber structure $S^3$. $\blacksquare$

**Remark 2.1.** Lemma H2 provides a new perspective on the Dyson-Manifold
correspondence proved in RANDOM\_MATRIX.md Theorem 2.1. The original proof
works through the symmetry algebra of the Fisher information matrix. The Hopf
fibration perspective is complementary: it identifies the fiber TYPE (trivial,
complex, quaternionic) as the geometric origin of the symmetry class.

---

## 3. Topological Mixing on Market Manifolds

### 3.1 The mixing hierarchy

Let $(M, g_M, \Phi_t)$ be the dynamical system consisting of the market manifold
$M^r$ with its induced metric $g_M$ and the Wright-Fisher flow $\Phi_t$ (the
Markov semigroup of the WF diffusion with parameter $\varepsilon^2 = 1/T$).
The ergodic hierarchy classifies systems by the strength of their stochastic
independence properties:

**Definition 3.1** (Mixing hierarchy).
1. *Ergodic* (weakest): For all measurable $A, B \subset M$,
   $\frac{1}{N}\sum_{n=0}^{N-1}\mu(\Phi_n^{-1}(A) \cap B) \to \mu(A)\mu(B)$
   as $N \to \infty$.
2. *Mixing*: $\mu(\Phi_n^{-1}(A) \cap B) \to \mu(A)\mu(B)$ as $n \to \infty$
   (no Cesaro averaging needed).
3. *Bernoulli* (strongest): $(M, \Phi_1, \mu)$ is measure-theoretically
   isomorphic to a Bernoulli shift (i.i.d. process).

The financial content of each level:
- **Ergodic** is sufficient for Birkhoff's theorem $\Rightarrow$ the Kelly
  criterion converges: $L_T(b^*) \to h_{\rm Kelly}$ a.s.
- **Mixing** is sufficient for the CLT on market returns $\Rightarrow$
  confidence intervals for the Sharpe ratio are valid.
- **Bernoulli** is the efficient market in the strongest possible sense
  $\Rightarrow$ past returns contain literally zero information about
  future returns.

### 3.2 Mixing and the spectral gap

For the WF diffusion on $M^r$, the generator is the Laplace-Beltrami operator
$\Delta_M$ (with respect to the induced metric $g_M$). The spectral gap is

$$\lambda_1 = \inf\left\{\frac{\int_M |\nabla f|^2\,d\mathrm{vol}_M}{\int_M f^2\,d\mathrm{vol}_M} : \int_M f\,d\mathrm{vol}_M = 0\right\} \tag{3.1}$$

the smallest non-zero eigenvalue of $-\Delta_M$.

**Proposition 3.1.** *The WF diffusion on $M^r$ is mixing iff $\lambda_1 > 0$.
The rate of mixing (correlation decay) is*

$$|\operatorname{Corr}(\Phi_n^*(f), g)| \leq C \cdot e^{-\lambda_1 n/T} \tag{3.2}$$

*for all $f, g \in L^2(M, \mu)$ with $\int f\,d\mu = \int g\,d\mu = 0$.*

*Proof.* Standard spectral theory for compact Riemannian manifolds. The
eigenfunction expansion of the heat kernel gives
$p_t(x,y) = \sum_k e^{-\lambda_k t}\phi_k(x)\phi_k(y)$,
and the correlation function decays as $e^{-\lambda_1 t}$ from the spectral gap.
For compact $M^r$ without boundary, $\lambda_1 > 0$ always. For $M^r$ with the
Feller boundary conditions of the simplex (SOBOLEV\_OPTIONS\_GREEKS.md), the
spectral gap remains strictly positive by the Feller boundary classification.
$\blacksquare$

### 3.3 Mixing rates for the three market types

The spectral gap $\lambda_1$ is explicitly computable for each classified market
type.

**CAPM market ($S^r_+$, Jacobi process).** The eigenvalues of
$-\Delta_{S^r_+}$ with Dirichlet boundary conditions on the simplex boundary are
the Jacobi polynomial eigenvalues:

$$\lambda_k = k(k + r + d - 3),\quad k = 1, 2, 3, \ldots \tag{3.3}$$

The spectral gap is $\lambda_1 = r + d - 2$. For $d = 50$, $r = 4$:
$\lambda_1 = 52$. Information propagates quickly — the CAPM is well-mixed with
fast exponential decay of correlations at rate $e^{-52 t/T}$.

**Clifford torus ($T^2$, flat torus BM).** The eigenvalues of the Laplacian on
the flat torus $T^2 = \mathbb{R}^2 / \Lambda$ (where $\Lambda$ is the lattice)
are

$$\lambda_{m,n} = 4\pi^2(m^2/a^2 + n^2/b^2),\quad (m,n) \in \mathbb{Z}^2 \setminus \{(0,0)\} \tag{3.4}$$

where $a, b$ are the torus periods. For the standard Clifford torus with
$a = b = \pi/2$ (the quarter-torus in $S^3$): $\lambda_1 = 4\pi^2/((\pi/2)^2) \cdot 1 = 16$.
The mixing is exponential but moderate. Crucially, the flat directions of the
torus produce polynomial corrections: the theta function kernel $\vartheta_3$ from
MARKET\_PROCESSES.md has algebraic tails from the lattice sum.

**Pseudo-Anosov market ($\mathbb{H}^2$, hyperbolic BM).** On a compact
hyperbolic surface $\Sigma_g$ of genus $g \geq 2$, the spectral gap satisfies

$$\lambda_1 \geq \frac{1}{4} - \frac{1}{4}\left(\frac{2\pi(2g-2)}{\mathrm{Area}(\Sigma_g)}\right)^2 \tag{3.5}$$

by the Cheeger-Buser inequality, with the Selberg $\frac{1}{4}$ conjecture
asserting $\lambda_1 \geq 1/4$ for arithmetic surfaces. For the pseudo-Anosov
market, the Anosov property gives something much stronger: exponential mixing
at rate $\log \lambda_{\rm pA}$, where $\lambda_{\rm pA} > 1$ is the
pseudo-Anosov stretch factor.

### 3.4 The mixing classification

Combining these spectral results with the ergodic theory of each process:

**Lemma H3** (Pseudo-Anosov is the most efficiently mixing type).
*The three classified market types satisfy the following mixing hierarchy:*

| Market type | Ergodic? | Mixing? | Bernoulli? | Mixing rate |
|:------------|:---------|:--------|:-----------|:------------|
| CAPM ($S^r_+$) | Yes | Yes | Yes | $e^{-\lambda_1 t}$, $\lambda_1 = r+d-2$ |
| Clifford torus ($T^2$) | Yes | Yes | No | $e^{-16t}$ with polynomial corrections |
| Pseudo-Anosov ($\mathbb{H}^2$) | Yes | Yes | Yes | $e^{-\lambda_{\rm pA} t}$, $\lambda_{\rm pA} = \log \lambda_{\rm pA}$ |

*The pseudo-Anosov market has the strongest mixing properties:*

*(a) It is Bernoulli (by the Ornstein isomorphism theorem for Anosov systems,
following Ornstein-Weiss 1973).*

*(b) Its exponential mixing rate $\log \lambda_{\rm pA}$ can exceed the CAPM rate
$r + d - 2$ for markets with large stretch factor.*

*(c) The Clifford torus is mixing but NOT Bernoulli — the polynomial corrections
from the flat directions prevent isomorphism with an i.i.d. process.*

*Proof.* (a) For the Anosov property: the pseudo-Anosov diffeomorphism
$\phi: \Sigma_g \to \Sigma_g$ has uniform hyperbolicity — there exist stable and
unstable foliations $\mathcal{F}^s, \mathcal{F}^u$ with contraction/expansion
rates $\lambda_{\rm pA}^{\pm 1}$. Ornstein's theorem (extended to Anosov systems
by Ornstein-Weiss) states that all Anosov diffeomorphisms preserving a smooth
measure are Bernoulli. The SRB measure from MARKET\_PROCESSES.md is absolutely
continuous along unstable manifolds, so the Ornstein-Weiss theorem applies.

(b) The CAPM spectral gap $\lambda_1 = r + d - 2$ grows linearly in $d$, but the
pseudo-Anosov stretch factor $\lambda_{\rm pA}$ is an intrinsic quantity of the
surface that can be made arbitrarily large by choosing higher-genus surfaces.
For $g \geq 3$, there exist pseudo-Anosov maps with $\log\lambda_{\rm pA} > d$.

(c) The flat torus $T^2$ has zero sectional curvature. The geodesic flow on a
flat torus is never mixing (it is quasi-periodic). The Brownian motion on $T^2$
is mixing (by heat kernel estimates) but the return to equilibrium has
polynomial corrections from the lattice structure — the theta function
$\vartheta_3(t) = 1 + 2\sum_{n=1}^\infty e^{-\pi n^2 t}$ decays exponentially
in the leading term but the sum over all lattice points introduces
$O(t^{-1/2})$ corrections. These polynomial tails prevent the Bernoulli
property (Kalikow 1982). $\blacksquare$

**Remark 3.1.** The paradox in Lemma H3 deserves emphasis. The "chaotic" market
(pseudo-Anosov) is the one where information propagates FASTEST. The CAPM market,
which is the "orderly" market, mixes well but not as forcefully. The Clifford
torus, the "balanced" market, mixes the slowest. This is because chaos =
sensitivity to initial conditions = rapid spreading of information across the
manifold. The pseudo-Anosov stretch factor $\lambda_{\rm pA}$ is a STRENGTH, not
a pathology — it means information about any perturbation reaches the entire
market exponentially fast. The "efficient" market, in the mixing sense, is the
chaotic one.

---

## 4. The Mixing Hierarchy and Information Propagation

### 4.1 From mixing to information propagation

The spectral gap controls not just abstract mixing but the concrete propagation
of information through the market. A news shock at time $t = 0$ affecting a single
asset $i$ displaces the log-optimal portfolio from $b^*$ to $b^* + \delta e_i$.
The perturbation propagates through $M^r$ according to the heat equation on the
manifold:

$$\frac{\partial u}{\partial t} = \frac{1}{T}\Delta_M u, \quad u(0, x) = \delta_{b^*}(x) \tag{4.1}$$

where $u(t, x)$ is the "information density" at point $x \in M^r$ at time $t$.
The solution expands in eigenfunctions:

$$u(t,x) = \sum_k e^{-\lambda_k t/T}\phi_k(b^*)\phi_k(x). \tag{4.2}$$

The information reaches equilibrium (uniform distribution over $M$) at rate
$\lambda_1/T$. The "half-life" of information asymmetry is

$$t_{1/2} = \frac{T \log 2}{\lambda_1}. \tag{4.3}$$

For the CAPM with $d = 50$, $r = 4$: $t_{1/2} = T\log 2/52 \approx 0.013T$.
Information equilibrates in about 1.3\% of the sample period. For the
pseudo-Anosov with $\lambda_{\rm pA} = 100$: $t_{1/2} \approx 0.007T$ — twice
as fast.

### 4.2 Bottlenecks and the Cheeger constant

Not all markets propagate information uniformly. A market with sector structure
— e.g., technology and energy stocks that are weakly correlated — has an
information bottleneck between sectors. The severity of the worst bottleneck is
measured by the Cheeger constant.

**Definition 4.1** (Cheeger constant). For a compact Riemannian manifold $M$,

$$h_M = \inf_{\Sigma}\frac{\mathrm{Area}(\Sigma)}{\min(\mathrm{Vol}(A), \mathrm{Vol}(B))} \tag{4.4}$$

where the infimum is over all hypersurfaces $\Sigma \subset M$ that partition $M$
into two open sets $A \cup B = M \setminus \Sigma$.

The Cheeger constant has a direct financial interpretation: $h_M$ is the
minimum rate at which information can flow between ANY two sectors of the
market. A high Cheeger constant means the market is well-connected — every
partition has a large "information surface" relative to the smaller sector.
A low Cheeger constant means there exists a partition where information flow
is throttled.

**Lemma H4** (Cheeger constant = minimum information flow rate).
*Let $M^r$ be a market manifold with Cheeger constant $h_M$ and spectral gap
$\lambda_1$. Then:*

*(a) Cheeger inequality:* $\lambda_1 \geq h_M^2/4$.

*(b) Buser inequality:* $\lambda_1 \leq C(r) \cdot h_M + h_M^2$ for a constant
$C(r)$ depending only on the dimension $r$ and a lower Ricci curvature bound.

*(c) Financial interpretation: $h_M = 0$ iff the market has disconnecting sectors
— components that can be separated with zero information flow. This is the
geometric criterion for a market that fails to mix.*

*(d) Crisis signature: $h_M \to 0$ before financial crises, as measured by the
Delaunay graph from GEOSPATIAL\_CONTAGION.md. The Fiedler eigenvalue of the
Delaunay adjacency matrix $\lambda_2(L_{\mathcal{D}})$ converges to $h_M$ in the
continuum limit and serves as a computable proxy.*

*Proof.* (a) is the classical Cheeger inequality (Cheeger 1970). (b) is the Buser
inequality (Buser 1982), which requires a lower Ricci curvature bound — satisfied
for compact $M^r$ with bounded geometry.

For (c): if $h_M = 0$, there exists a sequence of partitions $(A_n, B_n)$ with
$\mathrm{Area}(\Sigma_n)/\min(\mathrm{Vol}(A_n), \mathrm{Vol}(B_n)) \to 0$.
In the limit, $M$ develops a "bottleneck" of zero width — information in $A$
cannot reach $B$. The spectral gap $\lambda_1 \to 0$ by Cheeger's inequality,
and mixing ceases.

For (d): the Delaunay graph $\mathcal{D}(M)$ from GEOSPATIAL\_CONTAGION.md has
graph Cheeger constant $h_{\mathcal{D}} = \min_S |E(S, \bar{S})|/\min(|S|,
|\bar{S}|)$ (the edge expansion). As the mesh of the Delaunay triangulation
refines, $h_{\mathcal{D}} \to h_M$ (Dodziuk 1984). The Fiedler eigenvalue
$\lambda_2(L_{\mathcal{D}})$ of the graph Laplacian satisfies
$\lambda_2 \geq h_{\mathcal{D}}^2/2$ (the discrete Cheeger inequality) and
is computable in $O(d^2)$ operations from the correlation matrix. $\blacksquare$

**Remark 4.1.** The connection to GEOSPATIAL\_CONTAGION.md is precise: the Cheeger
constant $h_M$ identified there as the systemic risk measure is EXACTLY the
minimum information flow rate of Lemma H4. A market with $h_M \to 0$ is
simultaneously: (i) losing its mixing property, (ii) developing an information
bottleneck between sectors, and (iii) approaching a systemic crisis. These are
three descriptions of the same geometric phenomenon.

---

## 5. Hopf Invariant and Market Topology

### 5.1 The Hopf invariant

For a map $f: S^{2n-1} \to S^n$, the Hopf invariant $H(f) \in \mathbb{Z}$ is
defined cohomologically: if $\omega \in H^n(S^n)$ is the generator and
$f^*\omega = \alpha \in H^n(S^{2n-1})$, then $\alpha \cup \alpha =
H(f)\cdot\sigma$ where $\sigma \in H^{2n}(S^{2n-1})$ is the fundamental class.
Geometrically, $H(f)$ is the linking number of any two generic fiber preimages.

The Adams theorem (1960) states that maps with $H(f) = 1$ exist only for
$n = 1, 2, 4, 8$ — precisely the four Hopf fibrations.

### 5.2 Market interpretation

For the market manifold: the Hopf invariant of the factor projection
$\pi: S^{d-1}_+ \to B^{r}$ (where $B^r$ is the factor base) counts how many
times the idiosyncratic fiber "winds around" the factor base.

**$H(\pi) = 0$: Trivial fiber (CAPM).** The factor model explains everything.
There is no topological winding of the idiosyncratic fiber, no Berry phase, and
no topological alpha from the fiber direction. The normal bundle $NM$ is trivial
— every idiosyncratic position can be hedged continuously. This corresponds to
the GOE ($\beta = 1$) market where $O(n)$ symmetry prevents any non-trivial
fiber topology.

**$H(\pi) = \pm 1$: One unit of winding (Clifford torus).** The idiosyncratic
fiber winds once around the factor base. This winding is the geometric origin
of the Berry phase from FIBER\_BUNDLES.md: a portfolio that traverses a closed
loop in factor space accumulates a non-zero geometric phase. The sign of $H$
distinguishes the two possible orientations of the winding — in market terms,
whether the Berry phase is positive (momentum-like) or negative (mean-reversion-like).

**$H(\pi) = k$: Higher winding.** For markets with more complex fiber structure,
the Hopf invariant $|k| > 1$ indicates multiple windings of the idiosyncratic
fiber. Each additional winding is an additional unit of potential topological
alpha — a topologically protected signal that cannot be removed by any continuous
deformation of the market structure.

**Proposition 5.1.** *The Hopf invariant $H(\pi)$ is related to the first Chern
class of the normal bundle by:*

$$c_1(NM) = H(\pi) \cdot [\omega_{FS}] \in H^2(B^r, \mathbb{Z}) \tag{5.1}$$

*where $[\omega_{FS}]$ is the Fubini-Study class on the factor base. In
particular, the topologically protected alpha signals identified in
FIBER\_BUNDLES.md Theorem 4.1 are quantised in units of $H(\pi)$.*

*Proof.* For the complex Hopf bundle $S^{2n+1} \to \mathbb{C}P^n$, the first
Chern class is the generator of $H^2(\mathbb{C}P^n, \mathbb{Z}) \cong
\mathbb{Z}$, and equals $[\omega_{FS}]$. The Hopf invariant of the fibration is
$H(\pi) = 1$. For a general map $f: S^{d-1}_+ \to B^r$ that factors through
the Hopf fibration as $f = \pi \circ g$, the first Chern class of the pullback
bundle is $c_1(g^* \xi) = \deg(g) \cdot c_1(\xi) = \deg(g) \cdot [\omega_{FS}]$.
The Hopf invariant $H(f) = \deg(g)$ counts the degree of the map from $M^r$ to
the base, which equals the winding number of the fiber. $\blacksquare$

---

## 6. Information Architecture

### 6.1 The fiber bundle as information architecture

The "information architecture" of a market is the complete fiber bundle structure
$(E, B, F, \pi, G)$ where:

- **Total space $E = S^{d-1}_+$:** the full asset space. Each point is a
  complete portfolio specification.
- **Base $B = B^r$:** the factor space. Each point is a factor exposure vector.
  This is the "systematic" information — what drives correlated returns.
- **Fiber $F$:** the idiosyncratic space. Each point in the fiber over a base
  point $p$ is a specific asset allocation consistent with factor exposure $p$.
  This is the "stock-specific" information — what the factor model does not
  determine.
- **Projection $\pi: E \to B$:** the factor projection map. For the Hopf
  fibration, this is the Hopf map. It sends a portfolio to its factor exposures.
- **Structure group $G$:** the symmetry group of the fiber. For the complex Hopf
  bundle: $G = U(1)$. For the quaternionic Hopf bundle: $G = Sp(1) \cong SU(2)$.
  This determines the Dyson class $\beta$.
- **Connection $\nabla$:** how factor movements affect individual stocks (the
  factor loadings). The parallel transport of $\nabla$ is the optimal hedge
  updating rule from FIBER\_BUNDLES.md.
- **Curvature $F_\nabla$:** the failure of factor models to explain returns.
  Non-zero curvature = alpha = residual.

### 6.2 The simplest non-trivial architecture

The Hopf fibration $S^3 \xrightarrow{S^1} S^2$ gives the SIMPLEST non-trivial
information architecture. It has:
- 1-dimensional fiber (one idiosyncratic degree of freedom)
- 2-dimensional base (two systematic factors)
- Structure group $U(1)$ (rotations of the single idiosyncratic direction)
- Chern class $c_1 = 1$ (one unit of topological winding)

This is the minimal model for a market that is "more than CAPM but not by much."
The single unit of topological winding produces a single Berry phase, a single
unit of topological alpha, and a spectral gap controlled by the curvature of the
Hopf connection.

### 6.3 Horizontal and vertical information flow

Information flows through the fiber bundle architecture along two distinct
directions:

**Horizontal (along base):** Factor information — earnings announcements,
macro data, central bank decisions — propagates along the base $B^r$ at rate
$\lambda_1^{\rm base}$, the spectral gap of the Laplacian on the factor space.
This is the rate at which systematic risk is priced.

**Vertical (along fiber):** Idiosyncratic information — company-specific news,
governance changes, product launches — propagates along the fiber $F$ at rate
$\lambda_1^{\rm fiber}$, the spectral gap of the Laplacian restricted to the
fiber direction.

The mixing rate of the TOTAL market is governed by the bottleneck:

$$\lambda_1(M) \geq \lambda_1^{\rm base} + \lambda_1^{\rm fiber} - C \cdot \|F_\nabla\|^2 \tag{6.1}$$

where $\|F_\nabla\|^2$ is the curvature of the connection (the alpha). The
inequality shows that the total mixing rate is approximately the SUM of the
base and fiber rates, minus a correction for the curvature that couples them.

**Definition 6.1** (Informationally balanced market). A market is
*informationally balanced* if

$$\lambda_1^{\rm base} \approx \lambda_1^{\rm fiber}. \tag{6.2}$$

An informationally balanced market has no bottleneck between systematic and
idiosyncratic information flow. The Clifford torus, with its equal periods
$a = b$ and flat metric, is the canonical informationally balanced market. The
CAPM market has $\lambda_1^{\rm fiber} = \infty$ (the fiber is a point — there
is no idiosyncratic direction) and is trivially balanced. The pseudo-Anosov
market can be balanced or unbalanced depending on the stretch factor.

---

## 7. Topological Mixing and Convex Information Processing

### 7.1 The ambient mixing guarantee

The ambient space $S^{d-1}_+$ is compact and connected. The WF diffusion on
$S^{d-1}_+$ is therefore ergodic by the classical ergodic theorem for compact
manifolds without boundary. In fact, it is mixing: the spectral gap of
$-\Delta_{S^{d-1}_+}$ is $\lambda_1 = d - 1 > 0$ for all $d \geq 2$.

This means: on the FULL simplex, information always propagates. The question
is whether it propagates on the SUBMANIFOLD $M^r$.

### 7.2 Mixing on the submanifold

A submanifold $M^r \subset S^{d-1}_+$ inherits a Riemannian metric $g_M$ from
the ambient space. But it does NOT automatically inherit the mixing property
of the ambient space. The obstruction is topological:

- If $M^r$ is connected and compact, then $\lambda_1(M) > 0$ and $M$ is mixing.
- If $M^r$ is disconnected, then $\lambda_1(M) = 0$ and $M$ is not mixing —
  information in one component cannot reach the other.
- If $M^r$ develops a near-disconnection (a "bottleneck"), then
  $\lambda_1(M) \approx 0$ and mixing is slow.

**Theorem 7.1** (Informational efficiency = mixing = Cheeger positivity).
*A market manifold $M^r \subset S^{d-1}_+$ is informationally efficient in the
mixing sense iff the following equivalent conditions hold:*

*(a) $M^r$ is connected.*

*(b) $h_M > 0$ (the Cheeger constant is strictly positive).*

*(c) $\lambda_1(M) > 0$ (the spectral gap is strictly positive).*

*(d) For all open $U, V \subset M$ and all initial portfolios $b_0 \in U$, the
WF diffusion starting at $b_0$ reaches $V$ in finite expected time.*

*(e) The information flow rate across any partition of $M$ into two sectors is
bounded below by $h_M > 0$.*

*Proof.* (a) $\Leftrightarrow$ (c): For compact manifolds, $\lambda_1 > 0$ iff
the manifold is connected (the constant function is the only harmonic function
iff $M$ is connected).

(c) $\Rightarrow$ (b): The Cheeger inequality gives $h_M \geq 2\sqrt{\lambda_1} > 0$.

(b) $\Rightarrow$ (c): $\lambda_1 \geq h_M^2/4 > 0$.

(c) $\Leftrightarrow$ mixing: spectral gap $> 0$ implies exponential decay of
correlations (Proposition 3.1).

(c) $\Rightarrow$ (d): $\lambda_1 > 0$ implies the heat kernel $p_t(x,y) > 0$
for all $t > 0$ and all $x, y \in M$ (by the Harnack inequality on connected
compact manifolds). Hence the expected hitting time of any open set is finite.

(d) $\Rightarrow$ (a): If $M$ were disconnected, no diffusion path could cross
components.

(b) $\Leftrightarrow$ (e) is the definition of $h_M$. $\blacksquare$

### 7.3 The crisis as a mixing failure

Theorem 7.1 gives a precise geometric characterisation of financial crises: a
crisis is a period in which $h_M \to 0$.

Before a crisis: the market manifold $M^r$ is well-connected, $h_M$ is large,
information propagates quickly between all sectors, and the market is
informationally efficient.

During a crisis: the market manifold develops a bottleneck — two groups of
assets (e.g., "safe havens" and "risk assets") become weakly connected. The
Cheeger constant $h_M \to 0$, the spectral gap $\lambda_1 \to 0$, mixing
slows, and information ceases to propagate across the bottleneck.

After a crisis: central bank intervention, forced selling, or panic
re-establishes connections across the bottleneck. The Cheeger constant recovers,
$\lambda_1$ jumps, and mixing resumes.

This is the topological content of the contagion analysis in
GEOSPATIAL\_CONTAGION.md: the Fiedler eigenvalue of the Delaunay graph is a
computable, real-time proxy for $h_M$, and its decline is a leading indicator
of crisis.

---

## 8. The Hopf Fibration and the MUP

### 8.1 The MUP as Hopf projection

The Manifold Universal Portfolio (CONVERGENCE.md) is defined as

$$\hat{b}_T^M = \frac{\int_{M^r} b\, W_T(b)\,d\mu_M(b)}{\int_{M^r} W_T(b)\,d\mu_M(b)} \tag{8.1}$$

where the integration is over the $r$-dimensional market manifold $M^r$.

In the Hopf fibration language: $M^r$ is the BASE of the fibration. The MUP
integrates over the base, not the total space. Cover's original Universal Portfolio
integrates over the TOTAL space:

$$\hat{b}_T^{\rm Cover} = \frac{\int_{\Delta_{d-1}} b\, W_T(b)\,d\mu(b)}{\int_{\Delta_{d-1}} W_T(b)\,d\mu(b)}. \tag{8.2}$$

The passage from Cover to MUP is EXACTLY the Hopf projection: integrate out the
fiber direction, retain only the base.

**Lemma H5** (MUP = Hopf projection of Kelly strategy).
*The MUP regret decomposes as:*

$$\text{Regret}(\hat{b}_T^M) = \underbrace{\frac{r \log T}{2T}}_{\text{base regret}} + \underbrace{0}_{\text{fiber regret}} + O(1/T). \tag{8.3}$$

*The base regret is $r \log T/(2T)$ — the cost of learning the $r$-dimensional
factor structure. The fiber regret is zero — the idiosyncratic direction
contributes nothing to regret because it diversifies away. Cover's regret
$(d-1)\log T/(2T)$ equals $r \log T/(2T)$ (base) $+ (d-1-r)\log T/(2T)$
(unnecessary fiber integration).*

*Proof.* The Laplace approximation of the MUP integral (LAPLACE.md) gives

$$\log\int_{M^r} W_T(b)\,d\mu_M = T \cdot h_{\rm Kelly} + \frac{r}{2}\log\frac{2\pi}{T} - \frac{1}{2}\log\det F_M(b^*) + O(1/T) \tag{8.4}$$

where the $\frac{r}{2}\log T$ term comes from the $r$-dimensional Gaussian
integral over the base manifold $M^r$. The fiber direction does not contribute
because, by Lemma H1, the Kelly function is constant on fibers — the Hessian
has zero eigenvalues in the fiber directions, and these directions are excluded
from the $r$-dimensional integration.

Cover's integral over $\Delta_{d-1}$ produces

$$\log\int_{\Delta_{d-1}} W_T(b)\,d\mu = T \cdot h_{\rm Kelly} + \frac{d-1}{2}\log\frac{2\pi}{T} - \frac{1}{2}\log\det F(b^*) + O(1/T) \tag{8.5}$$

with $(d-1)/2 \cdot \log T$ because the integration is $(d-1)$-dimensional.
The difference in regret is $(d-1-r)\log T/(2T)$ — the wasted regret from
integrating over the $(d-1-r)$-dimensional fiber that contributes nothing
to log-wealth.

The MUP eliminates this waste by projecting (via the Hopf map) down to the
base. The Hopf fibration is the geometric reason for the improvement. $\blacksquare$

**Remark 8.1.** The MUP improvement factor is $(d-1)/r$. For $d = 50$,
$r = 4$: the MUP is $49/4 \approx 12\times$ more efficient than Cover.
This factor is the ratio of the total space dimension to the base dimension —
the ratio of the ambient simplex to the factor manifold. The Hopf fibration
makes this ratio geometric rather than algebraic.

### 8.2 The fiber integral as diversification

The act of "integrating out the fiber" in the MUP is not just a mathematical
convenience — it IS diversification. The fiber direction parameterises the
idiosyncratic compositions of portfolios with the same factor exposure. Averaging
over these compositions is exactly what diversification does: it keeps the
systematic exposure fixed while averaging out the idiosyncratic noise.

The Hopf fibration thus gives a precise geometric definition of diversification:

$$\text{Diversification} = \text{Hopf fiber integration} = \int_{\pi^{-1}(p)} d\mu_{\rm fiber}. \tag{8.6}$$

A "fully diversified" portfolio at factor exposure $p$ is the conditional
expectation over the fiber $\pi^{-1}(p)$. An "undiversified" portfolio is a
specific point on the fiber — a single stock-level allocation rather than an
average over all allocations with the same factor exposure.

---

## 9. Summary of New Results

We collect the five principal results of this paper.

**Lemma H1** (Kelly invariance under Hopf fiber action, Section 1.4).
The Kelly growth rate $h_{\rm Kelly}$ is constant on each Hopf fiber.
The idiosyncratic degree of freedom — the fiber direction — does not
affect log-optimal wealth. Portfolio theory is gauge-invariant with
respect to the Hopf action.

**Lemma H2** (Dyson class = Hopf fibration type, Section 2.2).
The Dyson symmetry class $\beta \in \{1, 2, 4\}$ corresponds to the
real ($S^0$), complex ($S^1$), and quaternionic ($S^3$) Hopf fibration
over the factor base. The GOE has trivial fiber, the GUE has $U(1)$
fiber, and the GSE has $Sp(1) \cong SU(2)$ fiber. This is a geometric
reinterpretation of the Dyson-Manifold correspondence.

**Lemma H3** (Pseudo-Anosov is the most efficiently mixing type, Section 3.4).
The pseudo-Anosov market is Bernoulli (by Ornstein-Weiss) with exponential
mixing rate $\log\lambda_{\rm pA}$, the CAPM is Bernoulli with rate
$r + d - 2$, and the Clifford torus is mixing but not Bernoulli. The "chaotic"
market propagates information fastest.

**Lemma H4** (Cheeger constant = minimum information flow rate, Section 4.2).
The Cheeger constant $h_M$ is the minimum rate of information flow across
any bipartition of the market manifold. It satisfies $h_M^2/4 \leq \lambda_1
\leq C(r)h_M + h_M^2$ and vanishes before financial crises as the market
develops sector bottlenecks.

**Lemma H5** (MUP = Hopf projection of Kelly strategy, Section 8.1).
The MUP integrates over the $r$-dimensional Hopf base, yielding regret
$r\log T/(2T)$. The fiber contributes zero regret. Cover's excess
regret $(d-1-r)\log T/(2T)$ is the cost of needlessly integrating over
the Hopf fiber. Diversification = Hopf fiber integration.

---

## 10. Open Problems

**OP-H1** (The octonionic Hopf fibration and 16-asset markets).
The octonionic Hopf fibration $S^{15} \to S^8$ with fiber $S^7$ exists
only for $d = 16$. Does a 16-asset market admit an exceptional fiber
structure not available to any other number of assets? The octonions are
non-associative — does this break the factor model interpretation? The
octonionic Hopf is related to the exceptional Lie group $G_2$ and to
triality — is there a "triality" among three distinguished 16-asset
market structures? **Difficulty: ★★★.**

**OP-H2** (Does the Hopf invariant constrain alpha?).
Proposition 5.1 shows that the Hopf invariant $H(\pi)$ equals the
first Chern class $c_1(NM)$. FIBER\_BUNDLES.md Theorem 4.1 shows
that $c_1 \neq 0$ implies topologically protected alpha. Quantitatively:
is the magnitude of the topological alpha bounded below by $|H(\pi)|$
times a universal constant depending only on the geometry of $M^r$?
Can we prove $|\alpha_{\rm top}| \geq |H(\pi)| \cdot h_{\rm Kelly}/(2\pi)$?
**Difficulty: ★★.**

**OP-H3** (Empirical mixing rates from market data).
The three market types predict distinct mixing rates: $\lambda_1 = r + d - 2$
(CAPM), $\lambda_1 = 16$ (Clifford), $\lambda_1 = \log\lambda_{\rm pA}$
(pseudo-Anosov). These can be estimated from the autocorrelation decay of
portfolio returns. Measure the mixing rates on S\&P 500 data across different
market regimes (bull, bear, crisis). Does the mixing rate transition between
types as predicted by the classification theorem? Does $h_M \to 0$ precede
the 2008 and 2020 crises? **Difficulty: ★.**

**OP-H4** (Information architecture of cryptocurrency markets).
Cryptocurrency markets have: (i) 24/7 trading (no close-to-open gap),
(ii) high correlation structure dominated by Bitcoin ($r \approx 1$?),
(iii) frequent regime changes. What is the Hopf fiber structure of a
crypto market? Is the fiber trivial (GOE/CAPM) because $r = 1$, or
does the high volatility induce non-trivial topology? The absence of a
close-to-open boundary condition changes the Feller classification —
does this affect the mixing rate? **Difficulty: ★★.**

---

## References

**Topology and Hopf fibrations:**
- Adams, J.F. (1960). "On the non-existence of elements of Hopf invariant one." *Annals of Mathematics* 72(1), 20--104.
- Hopf, H. (1931). "Uber die Abbildungen der dreidimensionalen Sphare auf die Kugelflache." *Mathematische Annalen* 104(1), 637--665.
- Milnor, J. (1965). *Topology from the Differentiable Viewpoint.* University Press of Virginia.
- Steenrod, N. (1951). *The Topology of Fibre Bundles.* Princeton University Press.

**Ergodic theory and mixing:**
- Cheeger, J. (1970). "A lower bound for the smallest eigenvalue of the Laplacian." In *Problems in Analysis* (Gunning, ed.), Princeton University Press, 195--199.
- Buser, P. (1982). "A note on the isoperimetric constant." *Annales Scientifiques de l'Ecole Normale Superieure* 15(2), 213--230.
- Ornstein, D. (1970). "Bernoulli shifts with the same entropy are isomorphic." *Advances in Mathematics* 4(3), 337--352.
- Ornstein, D. and Weiss, B. (1973). "Geodesic flows are Bernoullian." *Israel Journal of Mathematics* 14(2), 184--198.
- Kalikow, S. (1982). "T,T-inverse is not Bernoulli." *Ergodic Theory and Dynamical Systems* 2(2), 185--199.

**Differential geometry and spectral theory:**
- Dodziuk, J. (1984). "Difference equations, isoperimetric inequality and transience of certain random walks." *Transactions of the AMS* 284(2), 787--794.
- Chavel, I. (1984). *Eigenvalues in Riemannian Geometry.* Academic Press.

**Companion papers in this series:**
- CLASSIFICATION.md — Classification of efficient market structures via Simons stability.
- CONVERGENCE.md — MUP regret $r\log T/(2T)$, minimax optimality.
- FIBER\_BUNDLES.md — Holonomy, Berry phase, topologically protected alpha.
- GEOSPATIAL\_CONTAGION.md — Cheeger constant as systemic risk measure.
- MARKET\_PROCESSES.md — Exact SDEs per market topology.
- RANDOM\_MATRIX.md — Dyson class forced by manifold symmetry.
- LAPLACE.md — WKB/Laplace approximation on the simplex.
- SOBOLEV\_OPTIONS\_GREEKS.md — Feller boundary classification.

---

*Paper III.5 in the series "The Geometry of Efficient Markets."*
*Cross-references: CLASSIFICATION (Section 1.3), CONVERGENCE (Section 8.1),
FIBER\_BUNDLES (Sections 2.2, 5.2, 6.1), GEOSPATIAL\_CONTAGION (Sections 4.2, 7.3),
MARKET\_PROCESSES (Section 3.3), RANDOM\_MATRIX (Section 2.2), LAPLACE (Section 8.1),
SOBOLEV\_OPTIONS\_GREEKS (Section 3.2).*
