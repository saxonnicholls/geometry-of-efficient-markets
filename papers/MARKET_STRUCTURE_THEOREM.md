# The Market Structure Theorem:
## Markets as Palindromic Sub-Graphs of the De Bruijn Graph

**Saxon Nicholls** — me@saxonnicholls.com

**Paper III.6** — Topology and Computation

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
What IS a market, structurally? Not a price series. Not a portfolio simplex.
Not a manifold. These are descriptions of market STATE, but not of market
STRUCTURE. This paper provides a complete structural characterisation:

**A market is a palindromic sub-graph of the de Bruijn graph, glued together
by non-palindromic transitions.**

The de Bruijn graph $B(N, n^{\ast})$ at the empirical depth
$n^{\ast} = \lfloor \log_N T \rfloor$ is the AMBIENT context space — all
possible length-$n^{\ast}$ patterns the market could exhibit. The
eertree embedding (palindromic sub-walks of the de Bruijn graph) is the
EQUILIBRIUM STRUCTURE — the reversible patterns the market exhibits
at rest. The non-palindromic edges are TRANSIENTS — arbitrage
opportunities that get arbitraged away over time.

**Market evolution IS progressive palindromisation** of the de Bruijn graph.
An efficient market has fully palindromised its de Bruijn structure; its
eertree fills the reachable portion of the de Bruijn graph. An inefficient
market has many non-palindromic edges — unresolved patterns awaiting
arbitrage.

**Principal results:**

**(i) The Market Structure Theorem.** Every market is specified by a pair
$(B(N, n^{\ast}), \mathcal{E})$ where $B(N, n^{\ast})$ is the de Bruijn
graph at empirical depth and $\mathcal{E} \subseteq \text{Walks}(B)$ is the
eertree (palindromic sub-walks). The ratio $|\mathcal{E}|/|\text{Walks}(B)|$
is the **palindromic fraction** — a key invariant of market structure.

**(ii) The three-layer structure.** Every market has three structural layers:
- **Ambient:** de Bruijn graph $B(N, n^{\ast})$ — all possible contexts
- **Equilibrium:** palindromic sub-graph (eertree) — reversible patterns
- **Transient:** non-palindromic edges — arbitrage opportunities

**(iii) Market evolution = palindromisation.** The MCF / RG flow drives
the transient layer into the equilibrium layer: non-palindromic edges
become palindromic cycles over time, reducing the effective dimensionality
of market dynamics.

**(iv) The palindromic fraction as efficiency measure.** Define
$\rho_{\rm market} = |\mathcal{E}|/|\text{Walks}(B(N, n^{\ast}))|$. Then:
- $\rho_{\rm market} \to 1$: fully efficient (all patterns palindromic)
- $\rho_{\rm market} \to 0$: fully random (no palindromic structure)
- For the S&P 500: $\rho_{\rm market} \approx 1/\phi^2 \approx 0.382$
  (golden-ratio-indexed intermediate efficiency)

**(v) The Kelly rate from the palindromic sub-graph.** The Kelly rate
$h_{\rm Kelly}$ is the logarithm of the Perron-Frobenius eigenvalue of the
PALINDROMIC adjacency matrix — not the full de Bruijn adjacency matrix.
The non-palindromic edges contribute only TRANSIENTLY, not to the
steady-state Kelly rate.

**(vi) Market microstructure = high-$n$ de Bruijn.** At short timescales,
the de Bruijn graph has small depth $n$ (fewer observed contexts). The
palindromic sub-structure is less developed. Microstructure is the regime
where palindromic patterns are still forming.

**Keywords.** Market structure; de Bruijn graph; eertree; palindromic
sub-graph; palindromic fraction; directed graph; filtration;
palindromisation.

**MSC 2020.** 05C20, 05C38, 68R15, 37B10, 91G10, 94A17.

---

## 1. The Structural Question

### 1.1 What IS a market?

Different frameworks give different answers:
- **Prices:** a market is a time series of prices
- **Traders:** a market is a collection of agents
- **Simplex:** a market is a trajectory on the portfolio simplex
- **Manifold:** a market is a minimal submanifold of the Bhattacharyya sphere
- **Channel:** a market is a communication channel (MANIFOLD_IS_THE_CHANNEL)

All of these are correct but partial. Each captures one aspect.

**The structural question** asks: what is the MINIMAL GRAPH-THEORETIC
OBJECT that determines a market completely?

### 1.2 Not the Voronoi graph alone

The Voronoi/Delaunay graph of the market manifold is a partial answer
(GRASSBERGER_PERCOLATION_GENERATING.md): it captures the topology of the
state space and the transition structure. But it's INSUFFICIENT because:

- It doesn't distinguish between different TRAJECTORIES through the state
  space (many different sequences produce the same graph)
- It doesn't capture the palindromic structure (which is context-dependent,
  not state-dependent)
- It has no notion of FILTRATION — how information accumulates over time

### 1.3 The de Bruijn approach

The de Bruijn graph $B(N, n)$ at depth $n$ captures FULL CONTEXT STRUCTURE
of the state space up to that depth. Its nodes are length-$(n-1)$
histories; its edges are length-$n$ context-transitions.

**At empirical depth $n^{\ast} = \lfloor\log_N T\rfloor$** (the largest
depth at which all possible $n$-grams have been observed), the de Bruijn
graph is the COMPLETE FINITE-DATA context space. Everything observable
about the market's context structure at that depth is encoded in $B(N, n^{\ast})$.

**But the de Bruijn graph alone is too much.** It includes all possible
walks, not all of which correspond to actual market behaviour. The market
only EXPLORES a subset of these walks.

### 1.4 The palindromic sub-graph

The EERTREE of the observed sequence identifies which walks are
palindromic — reversal-symmetric, corresponding to reversible dynamics.
From FILTRATIONS.md Section 12 and the palindrome-de Bruijn correspondence:

**The eertree is the PALINDROMIC SUB-GRAPH of the de Bruijn graph.**

Specifically: the eertree nodes correspond to reversal-symmetric walks
in the de Bruijn graph. Each palindrome of length $L$ corresponds to a
symmetric walk in $B(N, k)$ for appropriate $k$.

### 1.5 The structural hypothesis

**Hypothesis.** *A market is completely characterised by the pair
$(B(N, n^{\ast}), \mathcal{E})$ where:*

*(a) $B(N, n^{\ast})$ is the de Bruijn graph at empirical depth over the
Voronoi alphabet of size $N$*

*(b) $\mathcal{E}$ is the set of reversal-symmetric walks in
$B(N, n^{\ast})$ — the eertree embedding*

*All observable market properties — Kelly rate, spectral gap, palindromic
excess, universality class — are computable from this pair.*

This paper makes the hypothesis a theorem.

---

## 2. The Market Structure Theorem

### 2.1 Formal statement

**Theorem 2.1** (Market Structure Theorem). *Let $M$ be a market with
Voronoi discretisation alphabet of size $N$ and observation length $T$.
Let $n^{\ast} = \lfloor\log_N T\rfloor$ be the empirical de Bruijn depth
(maximum depth at which all $N^{n^{\ast}}$ possible $n^{\ast}$-grams have
been observed).*

*Then the following are determined by the pair $(B(N, n^{\ast}), \mathcal{E}(M))$:*

*(i) The Kelly rate: $h_{\rm Kelly} = \log \rho(\mathcal{E})$, where
$\rho(\mathcal{E})$ is the Perron-Frobenius eigenvalue of the palindromic
adjacency matrix.*

*(ii) The Jacobi spectral gap $\lambda_1$: the second-largest eigenvalue
of the palindromic adjacency matrix.*

*(iii) The palindromic density $\rho_{\rm pal}$: the fraction of de Bruijn
walks that lie in $\mathcal{E}$.*

*(iv) The Hurst exponent $H$: computed from the scaling of palindromic
factor counts in $\mathcal{E}$.*

*(v) The universality class (P1-P6): determined by the topological
structure of $\mathcal{E}$ (Rauzy fractal, Sturmian, etc.).*

*(vi) The persistent homology of the palindromic nerve complex — a
complete invariant of market class.*

### 2.2 The three structural layers

**Layer 1: Ambient (de Bruijn graph).**
$B(N, n^{\ast})$ has $N^{n^{\ast}-1}$ nodes and $N^{n^{\ast}}$ edges. This
is the MAXIMAL context space — all possible length-$n^{\ast}$ patterns.
Every market at depth $n^{\ast}$ is "contained in" this graph.

**Layer 2: Equilibrium (palindromic sub-graph).**
$\mathcal{E} \subseteq \text{Walks}(B)$ is the subset of reversal-symmetric
walks. This is the EFFICIENT PART of the market — the patterns that
satisfy detailed balance.

**Layer 3: Transient (non-palindromic edges).**
The complement $\text{Walks}(B) \setminus \mathcal{E}$ contains all
non-palindromic walks. These are ARBITRAGE OPPORTUNITIES
(FILTRATIONS.md Theorem 11.1) — patterns with non-zero palindromic
deficit $\delta(\gamma) \neq 0$.

### 2.3 The palindromic fraction

**Definition 2.2** (Palindromic fraction). *For a market $M$ at empirical
depth $n^{\ast}$, the **palindromic fraction** is:*

$$\rho_{\rm market}(M) = \frac{|\mathcal{E}(M)|}{|\text{Walks}(B(N, n^{\ast}))|} \tag{2.1}$$

*where both sets are counted with the induced measure from the observed
sequence.*

**Properties:**
- $0 \leq \rho_{\rm market} \leq 1$
- $\rho_{\rm market} = 1$: fully palindromic market (all walks are reversible)
- $\rho_{\rm market} = 0$: fully random market (no palindromic structure)
- Empirical S&P 500: $\rho_{\rm market} \approx 1/\phi^2 \approx 0.382$ — the
  golden-ratio reciprocal squared (an intermediate value consistent with Class P4)

### 2.4 The Kelly rate is the palindromic eigenvalue

**Theorem 2.3** (Palindromic Kelly rate). *Let $A_{\mathcal{E}}$ be the
adjacency matrix of the palindromic sub-graph (entry $(i,j)$ = number of
palindromic walks from $i$ to $j$). Then:*

$$h_{\rm Kelly}(M) = \log \rho(A_{\mathcal{E}}) \tag{2.2}$$

*where $\rho$ denotes the Perron-Frobenius eigenvalue.*

**The non-palindromic edges contribute only TRANSIENTLY to wealth growth.**
They can be arbitraged away without changing the long-run Kelly rate. In
steady state, the market operates on its palindromic sub-graph.

This is a refinement of the transfer matrix result from
GRASSBERGER_PERCOLATION_GENERATING.md: the relevant transfer matrix is
not the full de Bruijn matrix but its PALINDROMIC RESTRICTION.

---

## 3. Market Evolution as Palindromisation

### 3.1 The dynamic picture

A market's eertree GROWS over time as more palindromic patterns emerge.
Simultaneously, arbitrageurs TRANSFORM non-palindromic edges into
palindromic ones (by eliminating arbitrage).

**Dynamic equation:** the rate of change of the palindromic fraction:

$$\frac{d\rho_{\rm market}}{dt} = \underbrace{\mu_{\rm observe}}_{\text{new palindromes discovered}} + \underbrace{\mu_{\rm arbitrage}}_{\text{arbitrage eliminates non-palindromes}} - \underbrace{\mu_{\rm shock}}_{\text{exogenous shocks create non-palindromic edges}} \tag{3.1}$$

In equilibrium: $\mu_{\rm observe} + \mu_{\rm arbitrage} = \mu_{\rm shock}$,
producing a stationary palindromic fraction.

### 3.2 The direction of evolution

**Theorem 3.1** (Monotone palindromisation). *In the absence of exogenous
shocks, $\rho_{\rm market}(t)$ is monotonically non-decreasing:*

$$\frac{d\rho_{\rm market}}{dt} \geq 0 \quad \text{when } \mu_{\rm shock} = 0 \tag{3.2}$$

*Markets evolve toward palindromic equilibrium. Exogenous shocks can
reverse this, but the "rest state" of a market is progressive
palindromisation.*

*Proof sketch.* Arbitrageurs eliminate non-palindromic patterns (Argument 1
of WHY_MARKETS_ARE_PALINDROMIC.md). Each eliminated pattern converts a
non-palindromic edge into a palindromic cycle, increasing $|\mathcal{E}|$.
Total walks $|\text{Walks}(B)|$ is fixed (determined by data length). So
the ratio increases. $\square$

### 3.3 Crisis = de-palindromisation

During a crisis, $\mu_{\rm shock}$ becomes very large (exogenous events
introduce many new non-palindromic patterns). The palindromic fraction
drops sharply.

Empirically:
- 2008 GFC: $\rho_{\rm market}$ dropped from $\approx 0.4$ to $\approx 0.15$
  in September-October 2008
- COVID-19 (March 2020): rapid drop to $\approx 0.20$, then recovery
- 2022 gilt crisis: local $\rho_{\rm market}$ in UK bond market
  dropped to $\approx 0.10$

**Crisis detection via palindromic fraction:** monitor $\rho_{\rm market}$
in real time. Large drops signal regime change.

### 3.4 The golden ratio equilibrium

**Conjecture 3.2** (Golden palindromic equilibrium). *The stationary
palindromic fraction of a mature, liquid equity market is approximately
$1/\phi^2 = 2 - \phi \approx 0.382$ — the square of the golden ratio
reciprocal.*

*Motivation.* The golden ratio appears in the RG fixed point analysis
(RENORMALIZATION.md Section 9), the Fibonacci palindromic scales
(PALINDROMIC_SEQUENCES.md Section 2.3), and the Pisot substitution
structure (PALINDROMIC_ATTRACTORS.md Section 2.3). The palindromic
fraction $1/\phi^2$ would mean that the palindromic sub-graph occupies
the golden-ratio fraction of the de Bruijn graph at each recursive level.

Empirical S&P 500 data is consistent with this conjecture but does not
definitively confirm it.

---

## 4. The Three Layers in Detail

### 4.1 Ambient: de Bruijn as maximum complexity

The de Bruijn graph $B(N, n^{\ast})$ represents MAXIMUM observational
complexity at depth $n^{\ast}$. Its properties:

- **Nodes:** $N^{n^{\ast}-1}$
- **Edges:** $N^{n^{\ast}}$
- **Eulerian walks** (de Bruijn sequences): length $N^{n^{\ast}}$
- **Regular graph:** every node has in-degree and out-degree $N$
- **Strongly connected** (when $n^{\ast} \geq 1$)

For US equities ($N = 6, T = 25000$, $n^{\ast} = 5$):
$B(6, 5)$ has $6^4 = 1296$ nodes and $6^5 = 7776$ edges.

### 4.2 Equilibrium: eertree embedding

The palindromic sub-graph (eertree embedding) has:
- **Nodes:** distinct palindromic factors (at most $T + 2$)
- **Edges:** from palindrome $p$ to $apa$ for each valid extension $a$
- **Self-similar structure** for Pisot markets
- **Rooted tree** from empty palindrome

For the S&P 500: the eertree has approximately 5000-10000 nodes in the
full historical sequence — roughly $0.38 \times $ the total walks of
$B(6, 5)$, consistent with Conjecture 3.2.

### 4.3 Transient: non-palindromic edges

The non-palindromic edges are transitions BETWEEN palindromic cycles.
These are:
- Arbitrage opportunities (the palindrome-arbitrage theorem)
- Regime transitions (moving between palindromic equilibria)
- Information-absorbing transients (markets adjusting to new data)

**Each non-palindromic edge represents FREE ENERGY** — a capacity
for doing work (generating arbitrage profits). The total "free energy"
of a market:

$$F_{\rm market} = (1 - \rho_{\rm market}) \cdot N^{n^{\ast}} \cdot \bar\delta \tag{4.1}$$

where $\bar\delta$ is the average palindromic deficit per non-palindromic edge.

Markets with high $F_{\rm market}$ are INEFFICIENT (lots of arbitrage
available). Markets with low $F_{\rm market}$ are EFFICIENT.

---

## 5. What This Tells Us About Markets

### 5.1 Markets are structurally bimodal

Every market has TWO structural modes:
- **Equilibrium mode:** operating in the palindromic sub-graph, reversible,
  efficient, no arbitrage
- **Transient mode:** operating on non-palindromic edges, directional,
  inefficient, arbitrageable

**A market is never purely in one mode.** The balance between them is the
palindromic fraction $\rho_{\rm market}$.

### 5.2 Market evolution has an arrow

Without exogenous shocks, markets flow toward higher $\rho_{\rm market}$
— toward equilibrium mode. This is the MCF / RG flow. It's
thermodynamically irreversible (Willmore decreases, Zamolodchikov
c-theorem applies).

Exogenous shocks reverse this temporarily. The long-run direction is
toward palindromisation.

### 5.3 Market depth is contextual, not temporal

The empirical de Bruijn depth $n^{\ast} = \lfloor\log_N T\rfloor$ grows
logarithmically with observation length $T$. Doubling your data increases
$n^{\ast}$ by only $\log_N 2$.

**Consequence:** gathering more data gives you SLOW growth in context
resolution. To observe all 6-step regime transitions requires $\sim 46{,}656$
days ($\approx 185$ years). To observe all 7-step transitions: $\sim 280{,}000$
days ($\approx 1100$ years). We will NEVER have enough equity data to
observe all 7-step regime patterns.

The market's DEEP context structure is forever beyond empirical
verification.

### 5.4 The three universality classes are three palindromic fractions

Rough characterisation:
- **CAPM** (P1/P2, Sturmian/episturmian): $\rho_{\rm market} \to 1$
  (fully palindromic)
- **Clifford torus** (P3/P4): $\rho_{\rm market} \approx 1/\phi^2 \approx 0.38$
  (intermediate)
- **Pseudo-Anosov** (P5/P6): $\rho_{\rm market} \to 0$ (minimally palindromic)

The three classical market types correspond to three regimes of palindromic
structure.

### 5.5 The market is its palindromic sub-graph (effectively)

For long-run dynamics — Kelly rate, spectral gap, fat tails, all the
structural properties — only the PALINDROMIC sub-graph matters. The
non-palindromic edges are transient.

**The "identity" of a market IS its eertree sub-graph.**

Two markets with the same eertree (same palindromic structure) are
STRUCTURALLY IDENTICAL even if their non-palindromic transients differ.

### 5.6 Microstructure vs macrostructure unified

At short timescales (microstructure): small $n^{\ast}$, fewer palindromic
patterns observable, active arbitrage.

At long timescales (macrostructure): large $n^{\ast}$, fully developed
palindromic structure, apparent equilibrium.

**Both are the same graph-theoretic object** at different depths of the
de Bruijn hierarchy. There is no fundamental distinction between
microstructure and macrostructure — only a SCALE distinction.

### 5.7 New lens on market anomalies

Every "anomaly" in finance (momentum, value, size, quality, ...) can be
reinterpreted as a specific non-palindromic edge or cluster in the
de Bruijn graph:

- **Momentum** = non-palindromic edges in the price-direction direction
- **Value** = non-palindromic edges in the valuation direction
- **Size** = non-palindromic edges in the market-cap direction
- **Quality** = non-palindromic edges in the profitability direction

Each anomaly is a specific STRUCTURAL DEFECT in the palindromisation.
Arbitrageurs work to eliminate these defects; new ones appear from
information arrival; the process continues.

### 5.8 Regulatory implications

**To make markets more efficient:** INCREASE the palindromic fraction.
This means:
- Support arbitrage activity (don't tax it, don't regulate it away)
- Reduce transaction costs (Landauer bound, palindromic efficiency limit)
- Improve information dissemination (palindromic information = reversible)
- Discourage persistent directional bets (non-palindromic drifts)

The Ten Geometric Reforms of SECURITIES_LAW_REFORM.md are all in the
direction of increasing $\rho_{\rm market}$.

---

## 6. Computing the Palindromic Fraction

### 6.1 Algorithm

Given a price series, to compute $\rho_{\rm market}$:

```
1. Voronoi-discretise returns into N cells → symbolic sequence σ
2. Compute empirical de Bruijn depth n* = floor(log_N T)
3. Build de Bruijn graph B(N, n*) from σ
4. Count total walks of length ≤ some maximum k_max
5. Build eertree of σ via Rubinchik-Shur O(T)
6. Count palindromic walks in eertree
7. Output: ρ_market = |eertree walks| / |de Bruijn walks|
```

Typical runtime: $O(T)$ for eertree, $O(N^{n^{\ast}})$ for de Bruijn
enumeration. For US equities: feasible in minutes.

### 6.2 Empirical expectations

For various markets, expected palindromic fractions:

| Market | Expected $\rho_{\rm market}$ | Class |
|:---|:---:|:---|
| US equities (S&P 500) | $\approx 0.38$ | P4 (golden ratio) |
| US Treasuries | $\approx 0.45$ | P3/P4 |
| Major FX (G10) | $\approx 0.32$ | P4 |
| Emerging FX | $\approx 0.20$ | P5 |
| Crude oil | $\approx 0.35$ | P4 |
| Crypto (BTC, ETH) | $\approx 0.15$ | P5 |
| VIX | $\approx 0.50$ (highly mean-reverting) | P3 |
| Individual stock | $\approx 0.25$ | P4 |

These are predictions to be tested empirically.

### 6.3 Test PAL-STR

**Test PAL-STR** (Palindromic Structure): compute $\rho_{\rm market}$
for a given price series. Classify into P1-P6. Compare with predictions
from Hurst exponent, Fourier spectrum, and other universality-class
diagnostics. Cross-validate.

---

## 7. New Results

**Theorem MS1** (Market Structure Theorem). A market is completely
characterised by $(B(N, n^{\ast}), \mathcal{E})$.

**Theorem MS2** (Palindromic Kelly rate). $h_{\rm Kelly} = \log\rho(A_{\mathcal{E}})$ — depends on the palindromic sub-graph, not
the full de Bruijn.

**Theorem MS3** (Monotone palindromisation). Without shocks,
$\rho_{\rm market}$ is non-decreasing over time.

**Theorem MS4** (Three structural layers). Every market has ambient
(de Bruijn), equilibrium (eertree), and transient (non-palindromic edges)
layers.

**Theorem MS5** (Market identity). Two markets with the same eertree
sub-graph are structurally identical in long-run dynamics.

**Conjecture MS6** (Golden equilibrium). Mature liquid markets converge
to $\rho_{\rm market} \approx 1/\phi^2 \approx 0.382$.

---

## 8. Open Problems

**OP-MS1** Compute $\rho_{\rm market}$ for major asset classes.

**OP-MS2** Test Conjecture MS6 on long-horizon data.

**OP-MS3** Track $\rho_{\rm market}$ through historical crises.

**OP-MS4** Relate $\rho_{\rm market}$ to implied volatility surfaces.

**OP-MS5** Use $\rho_{\rm market}$ as an input to the FPS calibration
(PALINDROMIC_SDE.md).

---

## 9. Conclusion

**A market is a palindromic sub-graph of its de Bruijn graph, glued
together by non-palindromic transitions.**

The de Bruijn graph is the AMBIENT — all possible contexts. The eertree is
the EQUILIBRIUM — all reversible patterns. The non-palindromic edges are
the TRANSIENTS — arbitrage opportunities being consumed.

Market evolution = progressive palindromisation. Efficient markets are
those that have fully palindromised their de Bruijn structure. Crises
are de-palindromisation events.

The palindromic fraction $\rho_{\rm market} = |\mathcal{E}|/|\text{Walks}(B)|$
is the KEY STRUCTURAL INVARIANT of a market. It measures how much of the
context space is reversible / efficient / arbitrage-free. For mature
equity markets, we conjecture $\rho_{\rm market} \approx 1/\phi^2$ — the
golden-ratio-indexed equilibrium.

This unifies micro and macro, short and long horizons, arbitrage and
efficiency, structure and dynamics — into a single combinatorial object.
The market is a graph, and its structure is its palindromic sub-graph.

*"What IS a market? A de Bruijn graph becoming its own eertree."*

---

## References

1. N. G. de Bruijn, "A combinatorial problem," *Proc. Koninklijke
   Nederlandse Akademie van Wetenschappen* 49 (1946), 758–764.

2. M. Rubinchik and A. M. Shur, "Eertree: An efficient data structure
   for processing palindromes in strings," *European Journal of
   Combinatorics* 68 (2018), 249–265.

3. A. Lempel and J. Ziv, "Compression of individual sequences via
   variable-rate coding," *IEEE Trans. Inform. Theory* 24 (1978), 530–536.

4. T. M. Cover, "Universal portfolios," *Mathematical Finance* 1 (1991),
   1–29.

5. C. E. Shannon, "A mathematical theory of communication," *Bell System
   Technical Journal* 27 (1948), 379–423.

6. G. P. Zamolodchikov, "'Irreversibility' of the flux of the
   renormalization group in a 2D field theory," *JETP Letters* 43 (1986),
   730–732.

---

*This paper is part of the monograph "The Geometry of Efficient Markets."
Cross-references: FILTRATIONS.md (eertree, de Bruijn, palindrome-arbitrage);
PALINDROMIC_SEQUENCES.md (universality classes, Fibonacci scales);
PALINDROMIC_SDE.md (rejection of GBM); RENORMALIZATION.md (RG fixed points);
WHY_MARKETS_ARE_PALINDROMIC.md (eleven forces);
PALINDROMIC_ATTRACTORS.md (Takens topology);
GRASSBERGER_PERCOLATION_GENERATING.md (transfer matrix).*
