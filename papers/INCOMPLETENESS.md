# Measurability, Computability, and Provability on the Market Manifold:
## Three Limits of Market Knowledge

**Saxon Nicholls** — me@saxonnicholls.com

**Paper 0.4 — Foundation** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
We separate three distinct limits on market knowledge that are frequently
conflated: (i) **observational incompleteness** — what the $\sigma$-algebra
$\mathcal{F}_{t}$ cannot resolve; (ii) **computational incompleteness** — what no
algorithm can decide in bounded time; (iii) **axiomatic incompleteness** — what no
recursive theory can prove. Each limit has a different mathematical source (measure
theory, computability theory, mathematical logic) and a different practical
consequence. Three main results make the separation precise. **Theorem A** (Filtration
Incompleteness): no computably generated public filtration is decision-complete for
all alpha-generating predicates in a Turing-universal market — this follows from
Rice's theorem applied to the Turing-complete market dynamics of BRAIDS.md.
**Theorem B** (Axiomatic Incompleteness Corollary): if market dynamics interpret
universal computation, then any consistent recursively axiomatized theory of the
market is incomplete — there exist true statements of the form "strategy $\beta_e$
eventually outperforms the benchmark" that are unprovable. **Theorem C** (Kolmogorov
Filtration Bound): a filtration with $N_t$ atoms resolves at most $\log N_t$ bits at
time $t$; if the realized path has Kolmogorov complexity growing faster than the
filtration capacity, then infinitely many true path predicates remain unresolved.
Supporting results include the $\Pi^0_2$-completeness of market efficiency
(falsifiable but not verifiable), the Sobolev-Kolmogorov bridge connecting discrete
and continuous information bounds, and a conjectural Kelly-Chaitin correspondence
linking the randomness of $h_{\rm Kelly}$'s digits to market efficiency.

**Keywords.** Incompleteness; Kolmogorov complexity; Rice's theorem;
arithmetical hierarchy; $\sigma$-algebra; Fisher-Rao metric; Kelly growth rate;
Martin-Lof randomness; filtration capacity; Sobolev space; undecidability.

**MSC 2020.** 03D32, 03F40, 68Q30, 94A17, 53A10, 91G10, 60G05, 46E35.

---

## 1. Introduction

### 1.1 The question

What can be known about a financial market?

Not empirically — that question admits only contingent answers, dependent on data
quality, computational resources, and the cleverness of the analyst. We mean the
question in the sense of mathematical logic and computability theory: what are the
*structural* limits of market knowledge? Which market properties are observable,
which are computable from observations, which are provable from axioms, and where
exactly do these three boundaries lie?

The geometric framework of this monograph — a financial market as a minimal
submanifold $M^r \subset S^{d-1}_{+}$ of the Bhattacharyya sphere, with portfolio
weights as barycentric coordinates on the simplex $\Delta_{d-1}$ — provides a
precise arena in which to ask this question. The Fisher-Rao metric
$g^{\rm FR}_{ij}(b) = \delta_{ij}/b_i$ endows the simplex with a natural notion
of distance. The Kelly growth rate $h_{\rm Kelly}$ measures the entropy of the
market process. The MUP (Manifold Universal Portfolio) achieves regret
$r \log T / (2T)$.

### 1.2 Three limits, three sources

Previous work in this monograph and in the broader literature has identified
various impossibility results for markets — undecidability of efficiency,
#P-hardness of exact prediction, incompressibility of return sequences. These
are frequently lumped together under the heading of "Godelian limits" or
"fundamental unknowability." This conflation obscures more than it illuminates.

The limits arise from three independent mathematical traditions, each with its
own source and its own practical consequence:

| Limit | Source | Mathematical tool | Practical consequence |
|:------|:-------|:------------------|:---------------------|
| **Observational** | What $\mathcal{F}_{t}$ cannot resolve | Measure theory, $\sigma$-algebras | Insider information exists; filtrations have finite capacity |
| **Computational** | What no algorithm can decide | Computability theory, Rice's theorem | No procedure decides all alpha predicates; efficiency is $\Pi^0_2$ |
| **Axiomatic** | What no recursive theory can prove | Mathematical logic, Godel's theorem | True market statements exist that no fixed theory derives |

These three walls are nested — observational $\subset$ computational $\subset$
axiomatic — but they are not the same wall, and confusing them leads to either
overclaiming (attributing to Godel what is really a $\sigma$-algebra limitation)
or underclaiming (treating computable limitations as merely practical).

### 1.3 Relation to companion papers

This paper synthesises and extends results from several companions.
COMPLEXITY.md establishes the prediction complexity hierarchy (P, #P, undecidable)
and Martin-Lof randomness of efficient returns. FILTRATIONS.md constructs the
geometric filtration and its Lempel-Ziv prefix tree representation.
INFORMATION_THEORY.md proves the SMB = Kelly theorem. BRAIDS.md establishes
Turing completeness of market dynamics. The present paper provides the
foundational framework that separates these results into their proper logical
categories.

### 1.4 Plan

Section 2 states the three main theorems. Section 3 develops the observational
limit (the $\sigma$-algebra hierarchy). Section 4 develops the computational
limit (Rice's theorem and $\Pi^0_2$-completeness). Section 5 develops the
axiomatic limit (Godel's theorem applied to market theories). Section 6
establishes the Kolmogorov filtration bound. Section 7 presents the
Sobolev-Kolmogorov bridge. Section 8 discusses the conjectural Kelly-Chaitin
correspondence. Section 9 draws implications and Section 10 poses open problems.

---

## 2. The Three Main Theorems

We state the three main results, each corresponding to one of the three limits.
Full proofs appear in the sections that follow.

**Theorem A** (Filtration Incompleteness). *No computably generated public
filtration is decision-complete for all alpha-generating predicates in a
Turing-universal market.*

That is: for any computable procedure that generates a filtration
$(\mathcal{F}^{\rm comp}_{t})_{t \geq 0}$ from the public price process, there
exist predicates of the form "strategy $\beta_e$ generates alpha over the next
$N$ periods" that are true but not $\mathcal{F}^{\rm comp}_{t}$-measurable
for any $t$. This is a consequence of Rice's theorem (Section 4), not Godel's
theorem.

**Theorem B** (Axiomatic Incompleteness Corollary). *If market dynamics
interpret universal computation (proved in BRAIDS.md), then any consistent
recursively axiomatized theory of the market is incomplete: there exist true
statements of the form "strategy $\beta_e$ eventually outperforms the benchmark"
that are unprovable in that theory.*

This is Godel's first incompleteness theorem applied to the market's
computational structure. It is the only result in this paper that genuinely
requires Godel; the others use weaker tools (Rice's theorem, Kolmogorov
complexity bounds).

**Theorem C** (Kolmogorov Filtration Bound). *A filtration with $N_t$ atoms
resolves at most $\log(N_t)$ bits at time $t$. If the realized path has
Kolmogorov complexity $K(x_{1:t})$ growing faster than the filtration capacity
$\sum_{s=1}^{t} \log(N_s)$, then infinitely many true path predicates remain
unresolved by that $\sigma$-algebra.*

This is a measure-theoretic / information-theoretic result. It does not require
computability theory or mathematical logic — it follows from the pigeonhole
principle applied to $\sigma$-algebra atoms.

---

## 3. The $\sigma$-Algebra Hierarchy (Observational Limit)

### 3.1 Three levels of market knowledge

Fix a market on manifold $M^r \subset S^{d-1}_{+}$ with return process
$(x_t)_{t=1}^{T}$. We define three nested $\sigma$-algebras on the underlying
probability space $(\Omega, \mathcal{F}, \mathbb{P})$:

**Definition 3.1** (Computational $\sigma$-algebra).
```math
\mathcal{F}^{\rm comp}_{T} = \sigma\bigl(f(x_{1:T}) : f \text{ computable in } \mathrm{poly}(T) \text{ time}\bigr).
```
This is the $\sigma$-algebra of events decidable by Turing machines in
polynomial time — the world of algorithmic traders, quantitative funds,
and any agent subject to computational resource constraints.

**Definition 3.2** (Market $\sigma$-algebra).
```math
\mathcal{F}^{M}_T = \sigma\bigl(b^{\ast}(s) \in A : s \leq T, A \in \mathcal{B}(M)\bigr).
```
This is the $\sigma$-algebra generated by the full price history projected onto
the market manifold — the world of anyone with complete data and unlimited
computation. It coincides with the manifold filtration of FILTRATIONS.md.

**Definition 3.3** (Oracle $\sigma$-algebra).
```math
\mathcal{F}^{\rm oracle}_{T} = \mathcal{F}^{M}_T \vee \sigma\bigl(v_G(s) : s \leq T, v_G \in \Gamma(NM)\bigr).
```
This is the $\sigma$-algebra generated by *both* the manifold path and the
normal bundle increments — the world of insiders who observe private
information orthogonal to the public price process. The normal bundle $NM$
carries the information that moves prices but is not yet reflected in them.

**Theorem 3.4** (Strict hierarchy). Under standard complexity-theoretic
assumptions ($\mathrm{P} \neq \#\mathrm{P}$) and the geometric EMH ($H = 0$
on $M^r$):
```math
\mathcal{F}^{\rm comp}_{T} \subsetneq \mathcal{F}^{M}_T \subsetneq \mathcal{F}^{\rm oracle}_{T}.
```
Both inclusions are strict.

*Proof.* **First inclusion (computational wall).** By the #P-hardness of exact
return prediction (COMPLEXITY.md, Theorem 2.2), there exist events in
$\mathcal{F}^{M}_T$ — specifically, events of the form
$\{L_T(b^{\ast}) \in [a,b]\}$ for sufficiently fine intervals $[a,b]$ — that
require super-polynomial time to decide. Under $\mathrm{P} \neq \#\mathrm{P}$,
these events are not in $\mathcal{F}^{\rm comp}_{T}$. The inclusion is therefore
strict. Note: this gap is a *computational* limitation (Wall 2), not an
observational one — the data is available, but the computation is infeasible.

**Second inclusion (observational wall).** The insider alpha result
(HAMILTONIAN_TAILS_COMPLETENESS.md): the excess growth rate available to an
insider observing $v_G \in \Gamma(NM)$ is
$\alpha = \varepsilon^2 |v_G|_{g^{\rm FR}}$, which is strictly positive
whenever $v_G \neq 0$. This means the event $\{$next price move is in direction
$v_G\}$ is measurable with respect to $\mathcal{F}^{\rm oracle}_{T}$ but not
$\mathcal{F}^{M}_T$. This gap is purely *observational* (Wall 1) — the
information is not in the public price process at all. $\square$

### 3.2 Information leakage

The mutual information between the oracle and market filtrations measures
insider leakage:

```math
I(\mathcal{F}^{\rm oracle}_{T};\, \mathcal{F}^{M}_T) = H(\mathcal{F}^{\rm oracle}_{T}) - H(\mathcal{F}^{\rm oracle}_{T} \mid \mathcal{F}^{M}_T).
```

When $I > 0$, insider information is partially reflected in prices — the
market is partially revealing. Perfect efficiency in the strong form requires
$\mathcal{F}^{M}_T = \mathcal{F}^{\rm oracle}_{T}$, which by Theorem 3.4 never
holds exactly. The gap $\mathcal{F}^{\rm oracle}_{T} \setminus \mathcal{F}^{M}_T$
is *irreducible private information* — a consequence of the observational
limit (measure theory), not of Godel's theorem.

---

## 4. Computational Incompleteness (Rice's Theorem)

### 4.1 Filtration incompleteness via Rice's theorem

The key tool for the computational limit is not Godel's incompleteness theorem
but Rice's theorem: every nontrivial extensional property of programs is
undecidable.

**Proof of Theorem A.** By BRAIDS.md (Theorem 6.1), the market dynamics on
$M^r$ are Turing-complete: the braid group action on portfolio trajectories
can simulate any Turing machine. In particular, for each Turing machine index
$e$, there exists a trading strategy $\beta_e$ whose long-run alpha is
determined by the halting behavior of machine $e$.

Consider the predicate $P_e$: "strategy $\beta_e$ generates positive alpha
over the next $N$ periods." This is an extensional property of the program $e$
(it depends on the function computed by $e$, not on $e$'s syntactic form).
By Rice's theorem, the set $\{e : P_e \text{ holds}\}$ is not recursively
decidable.

Now suppose a computably generated filtration
$(\mathcal{F}^{\rm comp}_{t})_{t \geq 0}$ were decision-complete for all
alpha predicates. Then for each $e$, there would exist a time $t_e$ such that
$P_e$ is $\mathcal{F}^{\rm comp}_{t_e}$-measurable. But measurability in a
computably generated $\sigma$-algebra implies decidability: the generating
functions are computable, so membership in any atom is decidable. This
contradicts Rice's theorem. $\square$

### 4.2 Efficiency is $\Pi^0_2$-complete

**Theorem 4.1** (Efficiency is $\Pi^0_2$-complete). The statement "the market
on $M^r$ is efficient" — formally, $H(b) = 0$ for all $b \in M^r$ — is
$\Pi^0_2$-complete.

The arithmetical hierarchy classifies statements by quantifier complexity:

| Level | Form | Example |
|:------|:-----|:--------|
| $\Sigma^0_1$ | $\exists n R(n)$ | "There exists an arbitrage" |
| $\Pi^0_1$ | $\forall n R(n)$ | "This strategy never profits" |
| $\Sigma^0_2$ | $\exists n \forall m R(n,m)$ | "There exists a profitable strategy" |
| $\Pi^0_2$ | $\forall n \exists m R(n,m)$ | "The market is efficient" |

*Proof.* **Membership in $\Pi^0_2$.** The statement "$H = 0$ everywhere on $M$"
is equivalent to:
```math
\forall \varepsilon > 0 \forall b \in M^r |H(b)| < \varepsilon.
```
Discretising: for each rational $\varepsilon = 1/n$ and each grid point
$b_k$ in a computable dense subset of $M^r$:
```math
\forall n \in \mathbb{N} \forall k \in \mathbb{N} |H(b_k)| < 1/n.
```
This has the form $\forall n \forall k R(n,k)$ where $R$ is decidable
(given oracle access to the curvature at $b_k$ to sufficient precision, which
requires finite but unbounded computation). This is $\Pi^0_2$.

**Hardness.** We reduce the $\Pi^0_2$-complete problem
"$\forall n \exists m T(e,n,m)$" (Kleene's T-predicate: "Turing machine $e$
halts on all inputs") to market efficiency.

Given Turing machine $e$, construct a market manifold $M_e^r$ as follows.
By the Turing completeness of braid dynamics (BRAIDS.md, Theorem 6.1), encode
the computation of machine $e$ on input $n$ as a braid $\beta_{e,n}$ in the
market. Define the mean curvature at the corresponding region of $M_e^r$ to be:
```math
H_{e,n}(b) = \begin{cases} 0 \& \text{if } e \text{ halts on input } n, \\ 1/n \& \text{if } e \text{ does not halt on input } n. \end{cases}
```
Then $H = 0$ everywhere on $M_e^r$ iff $e$ halts on all inputs. Since
"$e$ halts on all inputs" is $\Pi^0_2$-complete, so is market efficiency.
$\square$

### 4.3 Falsifiability

**Corollary 4.2** (Asymmetric epistemology). Market efficiency is:
- **Falsifiable:** a single observed $b^{\ast} \in M^r$ with $H(b^{\ast}) \neq 0$
  (an alpha) disproves efficiency. This is a $\Sigma^0_1$ certificate.
- **Not verifiable:** no finite amount of data can confirm $H = 0$ everywhere.
  Verification requires checking an infinite conjunction.

This is the precise sense in which the EMH is a scientific hypothesis in
Popper's framework: it is falsifiable but not provable from finite data. The
$\Pi^0_2$ classification explains *why* — it is at the same level as "this
program halts on all inputs," which is the canonical example of a falsifiable
but unverifiable statement in computability theory.

Note: this result uses computability theory (Rice's theorem, the arithmetical
hierarchy). It does not require Godel's incompleteness theorem. The statement
"no recursive procedure can decide efficiency in finite time" is precise;
but efficiency *is* falsifiable by observing alpha.

### 4.4 Dimension identification

**Corollary 4.3** (Undecidability of dimension). The statement $\dim(M) = r$
cannot be decided from finite data with certainty.

*Proof.* The dimension $r$ determines the manifold type and hence the stochastic
process (Jacobi, flat torus BM, or McKean kernel). Deciding between
$r$ and $r+1$ requires distinguishing the eigenvalue spectra of the Jacobi
operator on $M^r$ versus $M^{r+1}$. For any finite sample size $T$, there
exists a confidence level $\delta(T)$ such that the probability of correct
identification is $1 - \delta(T)$, where $\delta(T) \to 0$ as $T \to \infty$
but $\delta(T) > 0$ for all finite $T$.

More precisely, $\delta(T) \geq e^{-cT}$ for a constant $c$ depending on the
spectral gap $\lambda_1(L_M)$: the Jacobi eigenvalue controls the rate at
which the data reveals the dimension. $\square$

---

## 5. Axiomatic Incompleteness (Godel's Theorem)

### 5.1 When Godel genuinely applies

Godel's first incompleteness theorem states: any consistent, recursively
axiomatized theory that interprets arithmetic contains true statements that
are unprovable within that theory. The key prerequisite is that the theory
must be powerful enough to interpret arithmetic — i.e., it must encode
universal computation.

BRAIDS.md (Theorem 6.1) establishes that market dynamics on $M^r$ are
Turing-complete. This is the bridge that makes Godel's theorem applicable
to markets. Without Turing completeness, one would have only Rice's theorem
(Section 4) and measure-theoretic limitations (Section 3). With it, one
obtains genuinely unprovable truths.

### 5.2 Proof of Theorem B

**Proof of Theorem B.** Since market dynamics interpret universal computation
(BRAIDS.md), any sufficiently expressive theory $\mathcal{T}$ of the market —
one that can express statements about strategy performance, growth rates,
and convergence — interprets arithmetic via the encoding of Turing machines
into braid dynamics.

By Godel's first incompleteness theorem, $\mathcal{T}$ (if consistent and
recursively axiomatized) contains true but unprovable sentences. Specifically,
the Godel sentence $G_{\mathcal{T}}$ — which asserts its own unprovability —
can be translated back into market language. More concretely: for each Turing
machine index $e$, define the market statement
```math
\phi_e: \quad \text{"strategy } \beta_e \text{ eventually outperforms the benchmark."}
```
The set of $e$ for which $\phi_e$ is true is $\Sigma^0_1$ (it is
r.e. — recursively enumerable). By the incompleteness theorem, there exist
indices $e$ such that $\phi_e$ is true (strategy $\beta_e$ does eventually
outperform) but $\mathcal{T} \nvdash \phi_e$ (the theory cannot prove it).

This is the genuine Godel limit: not a limitation of data or computation, but
of proof. Even an agent with unlimited data, unlimited computation, and
complete knowledge of the market manifold $M^r$ cannot derive all true
market statements from any fixed recursive axiom system. $\square$

### 5.3 What Godel does NOT say

It is important to be precise about what Theorem B does and does not establish:

- Theorem B does **not** say "no AI can determine market efficiency." An AI
  can falsify efficiency by finding alpha; it cannot *prove* efficiency, but
  this is already established by the $\Pi^0_2$ result (Theorem 4.1), which
  uses only computability theory, not Godel.

- Theorem B does **not** say "the market is inherently unknowable." Most
  practical market questions (sign prediction, risk estimation, portfolio
  construction) are computable — they live at the P or #P level. The
  unprovable statements are logically deep but practically rare.

- Theorem B **does** say: for any fixed formal theory of markets, there exist
  true performance statements that the theory cannot derive. This is a
  limitation of *axiom systems*, not of *observation* or *computation*.

---

## 6. The Kolmogorov Filtration Bound (Theorem C)

### 6.1 Filtration capacity

**Proof of Theorem C.** A $\sigma$-algebra with $N$ atoms can distinguish at
most $N$ distinct outcomes, hence can resolve at most $\log_2(N)$ bits of
information. If the filtration $(\mathcal{F}_{t})$ has $N_t$ atoms at time $t$,
its cumulative capacity up to time $T$ is:
```math
\mathrm{Cap}_{T}(\mathcal{F}) = \sum_{t=1}^{T} \log_2(N_t).
```

Now let $(x_t)_{t=1}^{T}$ be the realized return path. Its Kolmogorov complexity
$K(x_{1:T})$ measures the minimum description length. If
$K(x_{1:T}) > \mathrm{Cap}_{T}(\mathcal{F})$, then by the pigeonhole principle,
there exist predicates about $x_{1:T}$ that are true but not
$\mathcal{F}_{T}$-measurable: the $\sigma$-algebra simply does not have enough
atoms to separate all the paths that differ in ways detectable by those predicates.

If $K(x_{1:t})/t$ exceeds $(\sum_{s=1}^{t} \log N_s)/t$ for infinitely many $t$
(which occurs when the path complexity grows faster than the filtration capacity),
then infinitely many true path predicates remain unresolved. $\square$

### 6.2 Application to market types

The three classified market types (CLASSIFICATION.md) have different complexity
profiles:

| Market type | Path complexity $K(x_{1:T})/T$ | LZ filtration capacity | Gap |
|:------------|:-------------------------------|:----------------------|:----|
| CAPM ($S^r_+$) | $r \cdot h_{\rm Kelly}$ | $\sim r \log T / T$ (vanishing) | Grows with $T$ |
| Clifford torus ($T^2$) | $2 h_{\rm Kelly}$ | $\sim 2 \log T / T$ | Grows with $T$ |
| Pseudo-Anosov ($\mathbb{H}^{2}$) | $r \cdot h_{\rm top}$ | $\sim r \cdot e^{h_{\rm top}} \cdot \log T / T$ | Grows fastest |

In all cases, the filtration capacity per unit time vanishes as $T \to \infty$
while the path complexity rate is constant, so the gap grows without bound.
This is the observational limit in action: no finite-capacity filtration keeps
pace with the path's information content.

### 6.3 The complexity decomposition

**Proposition 6.1** (Kolmogorov complexity of returns). Let $(x_t)_{t=1}^{T}$ be
the return sequence of an efficient market on $M^r$ with Kelly growth rate
$h_{\rm Kelly}$. Then:
```math
K(x_{1:T}) = r \cdot h_{\rm Kelly} \cdot T + O(\sqrt{T}).
```

*Proof.* The lower bound follows from the SMB theorem applied to the Kelly
measure $\mu^{\ast}$ (INFORMATION_THEORY.md, Theorem C):
```math
-\frac{1}{T}\log \mu^{\ast}(x_{1:T}) \to h_{\rm Kelly} \quad \text{a.s.}
```
By the Brudno-Zvonkin-Levin theorem, for ergodic processes:
$K(x_{1:T})/T \to h_{\mu^{\ast}}$ almost surely, where $h_{\mu^{\ast}}$ is
the measure-theoretic entropy rate. The entropy rate of the market process on
$M^r$ decomposes as $h_{\mu^{\ast}} = r \cdot h_{\rm Kelly}$: there are $r$
independent factor directions, each contributing $h_{\rm Kelly}$ bits per period
(this follows from the product structure of the Jacobi process on $S^r_+$ for
the CAPM case, and extends by ergodic decomposition to the general case).

For the upper bound, the LZ78 compression result from FILTRATIONS.md gives:
```math
c_{\rm LZ}(x_{1:T}) \sim \frac{r \log T}{\log(r+1)}
```
and the description of $x_{1:T}$ via the LZ dictionary has length
$c_{\rm LZ} \cdot \log T + O(c_{\rm LZ}) = r \cdot h_{\rm Kelly} \cdot T + O(\sqrt{T})$
by standard results on the optimality of LZ78 (Ziv-Lempel 1978, Theorem 2).

The $O(\sqrt{T})$ gap is tight: the central limit theorem for additive
functionals of the Markov chain on Voronoi cells gives fluctuations of order
$\sqrt{T}$ in the cumulative log-likelihood, which translates directly to
$O(\sqrt{T})$ fluctuations in description length. $\square$

**Remark.** The $O(\sqrt{T})$ residual is an information-theoretic phenomenon
(CLT fluctuations), not a "Godelian boundary." It arises from the observational
limit — finite-sample estimation noise — not from any logical incompleteness.

---

## 7. The Sobolev-Kolmogorov Bridge

### 7.1 Connecting discrete and continuous information bounds

Kolmogorov complexity is a discrete quantity (defined for finite strings),
while the Fisher-Rao metric and Sobolev norms are continuous objects. The
bridge between them is essential for applying information-theoretic bounds
to the continuous geometry of the simplex.

**Theorem 7.1** (Sobolev-Kolmogorov bridge). Let $f: \Delta_{d-1} \to \mathbb{R}$
be a portfolio payoff function in the weighted Sobolev space
$W^{1,2}(\Delta_{d-1}, \mu_J)$ (with Jacobi weight
$\mu_J = \prod b_i^{Tb^{\ast}_{i} - 1}$ as in SOBOLEV_OPTIONS_GREEKS.md). Let
$f|_{\rm grid}$ denote the restriction of $f$ to a regular grid of spacing
$\varepsilon$ on $\Delta_{d-1}$. Then:
```math
K(f|_{\rm grid}) \leq C_d \cdot \|f\|_{W^{1,2}(\Delta, \mu_J)} \cdot \log(1/\varepsilon) + O(d \log d).
```

*Proof sketch.* The Sobolev norm $\|f\|_{W^{1,2}}$ controls the total
variation of $f$ over the simplex. A function with bounded Sobolev norm can
be described to precision $\varepsilon$ by specifying its values at
$O(\varepsilon^{-d})$ grid points, each to precision $\varepsilon$, requiring
$O(\varepsilon^{-d} \cdot \log(1/\varepsilon))$ bits. But the Sobolev
embedding theorem guarantees that the function is Holder continuous with
exponent depending on $d$, so the grid values are correlated, and the
actual description length is $C_d \cdot \|f\|_{W^{1,2}} \cdot \log(1/\varepsilon)$
where $C_d$ absorbs the dimension-dependent constants.

The $O(d \log d)$ term is the overhead of specifying the grid structure on
$\Delta_{d-1}$. $\square$

### 7.2 The role of the Muckenhoupt condition

The Jacobi weight $\mu_J$ degenerates at the simplex boundary ($b_i \to 0$).
The Muckenhoupt $A_2$ condition (SOBOLEV_OPTIONS_GREEKS.md, Section 3) ensures
that the weighted Sobolev space is well-behaved despite this degeneracy:

```math
[w]_{A_2} = \sup_B \left(\frac{1}{|B|}\int_B w\right)\left(\frac{1}{|B|}\int_B w^{-1}\right) < \infty.
```

When $A_2$ holds, the Sobolev-Kolmogorov bridge (Theorem 7.1) is valid
uniformly on compact subsets of $\Delta_{d-1}$. When $A_2$ fails — which
happens at the Feller boundary — the bridge breaks: the Kolmogorov complexity
of $f|_{\rm grid}$ can exceed any computable bound.

**Corollary 7.2.** The Muckenhoupt $A_2$ condition is the analytic criterion
for the information-theoretic boundary: the Sobolev-Kolmogorov bridge is valid
precisely where $A_2$ holds, and the bridge fails at the Feller boundary
where the Fisher-Rao metric degenerates.

### 7.3 The complexity hierarchy on the simplex

Each level of the computational complexity hierarchy corresponds to a class
of market events, a $\sigma$-algebra, and a Fisher-Rao cost — the geodesic
distance on $\Delta_{d-1}$ that must be traversed to extract the information.

**Table 7.1.** The complexity-information correspondence.

| Complexity class | Market event | Limit type | Fisher-Rao cost |
|:-----------------|:-------------|:-----------|:----------------|
| **P** | Sign of next crossing | Computational | $O(1)$ |
| **NP** | Existence of profitable path | Computational | $O(\sqrt{T})$ |
| **#P** | Exact next return | Computational | $O(e^n)$ |
| **PSPACE** | Full market evolution | Computational | $O(T)$ |
| **$\Pi^0_2$** | Is the market efficient? | Computational | $\infty$ (limit statement) |
| **Godel** | True but unprovable market facts | Axiomatic | Beyond computation |

The Fisher-Rao cost increases monotonically with complexity class for the
computational hierarchy. The axiomatic limit (Godel) is qualitatively different:
it is not a matter of cost but of logical derivability.

---

## 8. The Kelly-Chaitin Correspondence (Conjecture)

### 8.1 Two numbers at the boundary of computability

Chaitin's halting probability $\Omega$ is defined as:
```math
\Omega = \sum_{\text{program } p \text{ halts}} 2^{-|p|}
```
where $|p|$ is the length of program $p$ on a fixed universal Turing machine.
$\Omega$ has three remarkable properties: it is well-defined (the sum converges),
its first $n$ binary digits are computable (given sufficient computation), and
its binary expansion is Martin-Lof random — maximally incompressible.

The Kelly growth rate $h_{\rm Kelly}$ has strikingly analogous properties.

**Proposition 8.1** (Properties of $h_{\rm Kelly}$).
1. $h_{\rm Kelly} = \lim_{T \to \infty} \frac{1}{T} \sum_{t=1}^{T} \log\langle b^{\ast}, x_t \rangle$ exists almost surely (by Birkhoff's ergodic theorem).
2. The first $n$ binary digits of $h_{\rm Kelly}$ are computable from $T \sim 10^{2n}$ observations (by the CLT convergence rate of the empirical mean).
3. The exact value of $h_{\rm Kelly}$ is not computable from any finite sample.

Property (3) follows from the undecidability of long-run strategy profitability
(COMPLEXITY.md, Theorem 2.4): if $h_{\rm Kelly}$ were exactly computable, one
could decide whether a strategy achieves positive growth by comparing its rate
to $h_{\rm Kelly}$, contradicting undecidability.

### 8.2 The conjectural randomness of Kelly digits

**Conjecture 8.2** (Kelly-Chaitin). Let $h_{\rm Kelly} = 0.b_1 b_2 b_3 \ldots$
be the binary expansion of the Kelly growth rate. Then:

(a) If the market is efficient ($H = 0$ on $M^r$), the sequence
$(b_n)_{n \geq 1}$ is Martin-Lof random.

(b) If the market is inefficient ($H \neq 0$), the sequence $(b_n)$ has
computable structure, and:
```math
K(b_1 \ldots b_n) \leq n - c \cdot \|H\|_{L^2(M)} \cdot n + O(\log n)
```
for a universal constant $c > 0$.

**Status.** This is stated as a conjecture rather than a theorem because the
identification of $h_{\rm Kelly}$ with an algorithmically random real requires
establishing that the market process, viewed as a dynamical system, produces
outputs whose entropy rate is genuinely Martin-Lof random (not merely
statistically random). The argument via the Calude-Hertling-Khoussainov-Wang
theorem (2001) — that the entropy rate of a Martin-Lof random ergodic process
is itself Martin-Lof random — requires verifying that the market process
satisfies the hypotheses of that theorem, which involves showing that the
Jacobi/torus/McKean process on $M^r$ is effectively ergodic in the sense
of algorithmic randomness. This verification remains open.

**Evidence for part (a).** When $H = 0$, the market return process is Martin-Lof
random with respect to $\mu^{\ast}$ (COMPLEXITY.md, Theorem 3.2). If the
CHKW theorem applies, part (a) follows.

**Evidence for part (b).** When $H \neq 0$, the Sharpe-curvature identity
$\mathrm{Sharpe}^{\ast} = \|H\|_{L^2(M)}$ provides a computable drift
direction (via the second fundamental form), yielding a computable subsequence
selection rule that biases the Kelly digits. By the Schnorr-Levin
characterisation, this gives the stated bound on $K(b_1 \ldots b_n)$.

### 8.3 Interpretation

If the Kelly-Chaitin conjecture holds, the randomness of the Kelly growth rate's
digits is a *thermometer* for market efficiency:

- **Fully random digits:** the market is a perfect minimal surface. No strategy
  exploits structure in the growth rate.
- **Partially structured digits:** the market has nonzero mean curvature. The
  amount of computable structure in $h_{\rm Kelly}$ is proportional to the
  Sharpe ratio of the best strategy.
- **Fully computable digits:** the market is deterministic. This never occurs
  for a genuine market (it would require zero volatility).

The analogy with Chaitin's $\Omega$ is suggestive but should not be overstated.
Both numbers encode halting-type information ($\Omega$ for Turing machines,
$h_{\rm Kelly}$ for trading strategies), and the universality of the MUP plays
a role analogous to the universal Turing machine. But the precise formal
connection requires the verification described above.

---

## 9. Implications

### 9.1 Three walls, not one

The central message of this paper is that the limits of market knowledge are
not one wall but three:

1. **The $\sigma$-algebra wall** (observational limit): what the public
   filtration $\mathcal{F}^{M}_t$ can resolve. This is the most immediate
   practical limitation — most "unknowability" in finance is simply the
   fact that insiders have information not in the public $\sigma$-algebra.
   The mathematical source is measure theory (finite filtration capacity,
   Theorem C). No logic or computability theory is needed.

2. **The Turing wall** (computational limit): what can be computed from
   observations. Even with unlimited data, some market questions (efficiency,
   long-run profitability) are undecidable — no algorithm resolves them in
   finite time (Theorem A, Theorem 4.1). The mathematical source is
   computability theory (Rice's theorem, the arithmetical hierarchy).

3. **The Godel wall** (axiomatic limit): what can be proved from axioms.
   Even with unlimited data and unlimited computation, any fixed recursive
   theory of the market is incomplete — some true performance statements
   are unprovable (Theorem B). The mathematical source is mathematical
   logic (Godel's first incompleteness theorem, applied via the Turing
   completeness of market dynamics).

Each wall is further from the market than the last. Most practical limitations
are at the first wall; the deepest theoretical limitations are at the third.

### 9.2 You can falsify but never prove market efficiency

Theorem 4.1 places market efficiency at the $\Pi^0_2$ level of the
arithmetical hierarchy. The practical consequence is stark:

- **To falsify:** Find one portfolio $b^{\ast}$ where $H(b^{\ast}) \neq 0$
  (i.e., find alpha). This is a finite computation — check the second
  fundamental form at observed portfolio positions.
- **To prove:** Verify $H(b) = 0$ for all $b \in M^r$. This requires
  checking an uncountable infinity of points, which no finite procedure can
  accomplish.

Every empirical study of market efficiency — every test for alpha, every
Fama-French regression, every out-of-sample backtest — is an attempt at
falsification. The studies that claim to "confirm" efficiency are
epistemologically confused: they have merely failed to falsify.

### 9.3 What computation cannot overcome, and what it can

The $\Pi^0_2$-completeness of market efficiency is a *computability-theoretic*
result. It does not depend on the computing substrate:

- **Classical computers:** Cannot decide efficiency (Theorem 4.1).
- **Quantum computers:** BQP $\subseteq$ PSPACE $\subsetneq$ $\Pi^0_2$.
  Quantum computation does not escape the arithmetical hierarchy.
- **Neural networks and LLMs:** These are computable functions (they run on
  digital hardware), hence operate within $\mathcal{F}^{\rm comp}_{T}$.
  By Theorem 3.4, they cannot access $\mathcal{F}^{M}_T$ fully.

However, most practical market questions are *not* at the $\Pi^0_2$ level.
Sign prediction, risk estimation, and portfolio construction are in P or #P.
The undecidability results constrain the *deepest* questions (efficiency,
completeness, long-run optimality), not the everyday ones.

### 9.4 The hierarchy of obstructions

```math
\underbrace{\text{P}}_{\text{sign}} \subsetneq \underbrace{\#\text{P}}_{\text{returns}} \subsetneq \underbrace{\text{PSPACE}}_{\text{evolution}} \subsetneq \underbrace{\Pi^0_2}_{\text{efficiency}} \subsetneq \underbrace{\text{Godel}}_{\text{provability}}.
```

Each level corresponds to a qualitatively different kind of market question and
a qualitatively different kind of limitation:
- P through PSPACE: computational limits (Wall 2) — the question is decidable
  but the cost varies.
- $\Pi^0_2$: computational limit at the boundary — the question is undecidable
  but falsifiable.
- Godel: axiomatic limit (Wall 3) — even decidability is insufficient; formal
  proof fails.

Finance textbooks typically operate at the P level (CAPM, Black-Scholes) and
occasionally reach #P (Monte Carlo for exotics). The fundamental questions of
finance — efficiency, arbitrage, completeness — live at $\Pi^0_2$. The
Godelian level is real but practically remote.

---

## 10. Open Problems

**OP-I.1** (Verify the Kelly-Chaitin conjecture). The main open problem is
to verify that the market processes (Jacobi, flat torus BM, McKean) satisfy
the hypotheses of the Calude-Hertling-Khoussainov-Wang theorem, establishing
Conjecture 8.2 as a theorem. This requires showing effective ergodicity in
the sense of algorithmic randomness.

**OP-I.2** (Complexity of the Sharpe ratio). The Sharpe ratio equals
$\|H\|_{L^2(M)}$ by the Sharpe-curvature theorem (MINIMAL_SURFACE.md).
What is the computational complexity of computing $\|H\|$ to precision
$\varepsilon$? It lies between P (an upper bound exists for the CAPM) and
#P (the general case inherits hardness from the Jones polynomial). Is there a
tight classification by market type?

**OP-I.3** (Algorithmic randomness of factor returns). The full return sequence
is Martin-Lof random for efficient markets. Are the *individual factor returns*
(the components of the return projected onto $TM$) also Martin-Lof random?
Or does the factor decomposition introduce computable structure that the full
sequence lacks? This connects to the question of whether PCA-based strategies
can exploit structure invisible to the aggregate return.

**OP-I.4** (The Sobolev regularity threshold). Theorem 7.1 bounds Kolmogorov
complexity by the $W^{1,2}$ Sobolev norm. Is there a critical Sobolev exponent
$s^{\ast}$ such that $W^{s,2}$ functions have $K(f|_{\rm grid}) = O(\log(1/\varepsilon))$
for $s > s^{\ast}$ (highly compressible) and
$K(f|_{\rm grid}) = \Omega(1/\varepsilon^{d-2s})$ for $s < s^{\ast}$
(incompressible)? If so, $s^{\ast}$ would be the analytic manifestation of the
information-theoretic boundary.

**OP-I.5** (Quantum estimation advantage). Does quantum computation provide any
advantage for estimating $h_{\rm Kelly}$? Specifically, is there a quantum
algorithm that achieves $n$ digits of $h_{\rm Kelly}$ from $o(10^{2n})$
observations? The Grover-type quadratic speedup would give $T \sim 10^n$,
which would halve the data requirement in the exponent.

---

## 11. Conclusion

The limits of market knowledge are not one wall but three: the $\sigma$-algebra
wall (what you can observe), the Turing wall (what you can compute from
observations), and the Godel wall (what you can prove from axioms). Each wall
is further from the market than the last. Most practical limitations are at the
first wall; the deepest theoretical limitations are at the third.

The $\sigma$-algebra wall is measure-theoretic. A filtration with $N_t$ atoms
resolves at most $\log N_t$ bits per period. The public price process generates
a filtration whose capacity grows slower than the path's Kolmogorov complexity,
so infinitely many true predicates escape observation. Insider information lives
in the gap between $\mathcal{F}^{M}_T$ and $\mathcal{F}^{\rm oracle}_{T}$ — the
normal bundle of the market manifold. This is where most practical
"unknowability" in finance resides.

The Turing wall is computability-theoretic. Rice's theorem, applied to the
Turing-complete market dynamics, shows that no computable filtration is
decision-complete for all alpha predicates. Market efficiency is
$\Pi^0_2$-complete: falsifiable by a single alpha observation, but not
verifiable by any finite procedure. This is a deeper limitation than the
$\sigma$-algebra wall — it persists even with unlimited data.

The Godel wall is logical. Any consistent recursive theory of the market is
incomplete: there exist true performance statements that no finite proof
derives. This is the deepest limitation, but also the most remote from
practice. It requires the full force of Godel's theorem, applied via the
Turing completeness of braid dynamics, and constrains only what can be
*proved*, not what can be *observed* or *computed*.

Three distinct boundaries — measurability, computability, provability —
constrain market knowledge in different ways. The geometry of the market
manifold tells us where each boundary lies: the filtration capacity bounds the
first, the arithmetical hierarchy classifies the second, and the logical
structure of any axiomatization determines the third.

---

## References

1. K. Godel, "Uber formal unentscheidbare Satze der Principia Mathematica und verwandter Systeme I," *Monatshefte fur Mathematik und Physik* 38 (1931), 173-198.

2. A.M. Turing, "On computable numbers, with an application to the Entscheidungsproblem," *Proceedings of the London Mathematical Society* 42 (1936), 230-265.

3. A.N. Kolmogorov, "Three approaches to the quantitative definition of information," *Problems of Information Transmission* 1(1) (1965), 1-7.

4. G.J. Chaitin, "A theory of program size formally identical to information theory," *Journal of the ACM* 22(3) (1975), 329-340.

5. P. Martin-Lof, "The definition of random sequences," *Information and Control* 9(6) (1966), 602-619.

6. C.P. Schnorr, "A unified approach to the definition of random sequences," *Mathematical Systems Theory* 5(3) (1971), 246-258.

7. L.A. Levin, "Laws of information conservation (nongrowth) and aspects of the foundation of probability theory," *Problems of Information Transmission* 10(3) (1974), 206-210.

8. H. Rice, "Classes of recursively enumerable sets and their decision problems," *Transactions of the American Mathematical Society* 74(2) (1953), 358-366.

9. M. Li and P. Vitanyi, *An Introduction to Kolmogorov Complexity and Its Applications*, Springer, 4th edition, 2019.

10. T.M. Cover and J.A. Thomas, *Elements of Information Theory*, Wiley, 2nd edition, 2006.

11. C. Calude, P. Hertling, B. Khoussainov, and Y. Wang, "Recursively enumerable reals and Chaitin $\Omega$ numbers," *Theoretical Computer Science* 255(1-2) (2001), 125-149.

12. A. Brudno, "Entropy and the complexity of the trajectories of a dynamical system," *Transactions of the Moscow Mathematical Society* 44 (1983), 127-151.

13. A.K. Zvonkin and L.A. Levin, "The complexity of finite objects and the basing of the concepts of information and randomness on the theory of algorithms," *Russian Mathematical Surveys* 25(6) (1970), 83-124.

14. J. Ziv and A. Lempel, "Compression of individual sequences via variable-rate coding," *IEEE Transactions on Information Theory* 24(5) (1978), 530-536.

15. F. Jaeger, D.L. Vertigan, and D.J.A. Welsh, "On the computational complexity of the Jones and Tutte polynomials," *Mathematical Proceedings of the Cambridge Philosophical Society* 108(1) (1990), 35-53.

16. T.M. Cover, "Universal portfolios," *Mathematical Finance* 1(1) (1991), 1-29.

17. R.I. Soare, *Turing Computability: Theory and Applications*, Springer, 2016.

18. S.-I. Amari, *Information Geometry and Its Applications*, Springer, 2016.

---

*This paper is part of the monograph "The Geometry of Efficient Markets."
Cross-references: COMPLEXITY.md (prediction hierarchy, Martin-Lof randomness);
FILTRATIONS.md (LZ78 prefix tree, Voronoi filtration);
INFORMATION_THEORY.md (SMB = Kelly, entropy rate);
BRAIDS.md (Turing completeness, braid dynamics);
SOBOLEV_OPTIONS_GREEKS.md (weighted Sobolev spaces, Muckenhoupt condition);
MINIMAL_SURFACE.md (Sharpe-curvature identity);
HAMILTONIAN_TAILS_COMPLETENESS.md (insider alpha, normal bundle).*
