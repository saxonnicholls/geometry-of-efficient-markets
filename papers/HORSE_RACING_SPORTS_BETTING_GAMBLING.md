# Horse Racing, Sports Betting, and Gambling Generally:
## The Geometry of the Dedicated Punter

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VI.1** — Applications

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
Cover's foundational work on universal portfolios grew from two roots: the
stock market and the racetrack. The stock market got a monograph. The
racetrack got a chapter. We redress the balance. The geometric framework of
this monograph — market manifolds, Fisher-Rao metric, Bhattacharyya sphere,
Kelly criterion — applies to any wagering market where a bettor allocates
capital across outcomes. A horse race with $d$ runners IS a portfolio
problem on $\Delta_{d-1}$. The bookmaker's odds define a point on the
simplex. The true win probabilities define another. The Fisher-Rao distance
between them is the edge. Everything in this monograph applies, with horses
instead of stocks and races instead of trading days.

We develop the theory for parimutuel betting (horse racing, greyhound racing),
fixed-odds sports betting (football, tennis, cricket, basketball), casino
games (blackjack, poker), and prediction markets. In each case, the
geometric framework yields results that are new, practical, and — for the
dedicated punter — potentially profitable.

**Principal results:**

**(i) The bettor's edge is the Fisher-Rao distance between true and implied probabilities.**
The overround $\Omega = \sum_i (1/o_i) - 1 > 0$ (where $o_i$ are decimal odds)
is the bookmaker's margin — a transaction cost, not an information distance.
A bookmaker can have $\Omega > 0$ (positive margin) with $q = p$ (no mispricing):
consider uniform margin $o_i = (1+\Omega)/p_i$, which gives normalised implied
probabilities $q_i = p_i$ while $\Omega > 0$. The exploitable edge comes from
the DISPLACEMENT $q \neq p$, not from the margin $\Omega$. The Fisher-Rao
distance $d_{g^{\rm FR}}(p, q)$ measures how much the bookmaker's implied
probabilities deviate from truth — this is the bettor's informational edge.

**(ii) Kelly betting on horses is MUP on the race manifold.**
A sequence of races with $d$ runners defines a sequence of return vectors.
The bettor allocates fraction $b_0$ to cash (kept regardless of outcome) and
$b_i$ to horse $i$. If horse $j$ wins, wealth is multiplied by
$b_0 + b_j \cdot o_j$ (cash kept plus winning bet paid at odds). The Kelly
bettor maximises $\mathbb{E}[\log(b_0 + b_{\rm winner} \cdot o_{\rm winner})]$
over bet vectors $b \in \Delta_d$ (including the cash component
$b_0 = 1 - \sum_{i \geq 1} b_i$). This is exactly the universal portfolio
problem with a risk-free asset. The MUP on the race manifold is the optimal
long-run betting strategy.

**(iii) The favourite-longshot bias is mean curvature of the odds manifold.**
The well-documented bias (favourites are underbet, longshots are overbet)
is geometrically the mean curvature vector $\vec{H}$ of the bookmaker's odds
manifold in the Bhattacharyya sphere. The Sharpe-curvature identity gives:
the maximum Sharpe ratio of any betting strategy against the bookmaker is
$\|H\|_{L^2}$ — computable from publicly available odds.

**(iv) The Harville formula is conjectured to arise from a Jacobi diffusion on the race simplex.**
The Harville (1973) model for finishing-order probabilities —
$P(\text{horse } i \text{ finishes } k\text{-th}) = p_i / \sum_{j \notin \{1,\ldots,k-1\}} p_j$
— is consistent with a sequential absorption model on $\Delta_{d-1}$ with
Jacobi-type dynamics, though the precise identification requires verification
(see Conjecture 5.1).

**(v) Card counting is Kalman filtering on the deck manifold.**
In blackjack, the composition of the remaining deck defines a point on
$\Delta_{51}$ (52-card simplex). Card counting systems (Hi-Lo, Omega II,
Wong Halves) are low-dimensional projections of the deck state — i.e.,
factor models. The optimal card counting system is the manifold Kalman
filter of Paper III.6, restricted to the deck manifold.

**Keywords.** Horse racing; sports betting; gambling; Kelly criterion; overround;
favourite-longshot bias; Harville formula; card counting; parimutuel;
bookmaker; Fisher-Rao; Bhattacharyya; simplex; universal portfolio; racetrack.

---

## 1. The Racetrack as a Financial Market

### 1.1 Cover's insight

Thomas Cover's 1991 universal portfolio paper opens with a quote about horse
racing. His earlier work with Breiman (Cover 1966, "Gambling on horses")
established that the Kelly criterion — maximise expected log wealth —
applies to sequential wagering just as it applies to sequential investing.
The mathematics is identical; only the narrative changes.

**Cover's key observation:** A horse race with $d$ runners and odds
$o_1, \ldots, o_d$ is isomorphic to a one-period stock market with $d+1$
assets: cash (risk-free) and $d$ bets. A bet vector $b \in \Delta_d$
(including the cash allocation $b_0 = 1 - \sum_{i \geq 1} b_i$) is a
portfolio. If horse $j$ wins, the return is $b_0 + b_j \cdot o_j$.
A sequence of races is a sequence of return vectors. The universal
portfolio is the universal bettor.

### 1.2 The race simplex

**Definition 1.1** (Race simplex). *A horse race with $d$ runners has
bet space $\Delta_d = \{b \in \mathbb{R}^{d+1}_+ : \sum b_i = 1\}$,
where $b_0$ is the cash (no-bet) fraction and $b_i$ for $i \geq 1$ is the
fraction wagered on horse $i$. The risky bet space is the face
$\{b \in \Delta_d : b_0 = 0\}$, isomorphic to $\Delta_{d-1}$.*

The Fisher-Rao metric on the race simplex:
$$g^{\rm FR}_{ij}(b) = \frac{\delta_{ij}}{b_i} \tag{1.1}$$

The Bhattacharyya embedding: $\phi: b \mapsto \sqrt{b} \in S^{d-1}_+$.

**Everything in this monograph applies.** The race simplex $\Delta_{d-1}$
is the portfolio simplex. The Fisher-Rao metric is the information metric.
The Bhattacharyya sphere is the ambient space. The Kelly criterion selects
the log-optimal bet. The MUP integrates over all Kelly-optimal bets.
The Sharpe-curvature identity measures the edge.

### 1.3 The three types of racing market

By the classification theorem (Paper I.4), the race manifold falls into
one of three types:

| Type | Geometry | Racing interpretation |
|:-----|:---------|:--------------------|
| CAPM (sphere) | One dominant factor | One "class" variable (going, distance, weight) dominates |
| Clifford (torus) | Two balanced factors | Two independent factors (speed + stamina, or form + class) |
| Pseudo-Anosov (hyperbolic) | Chaotic | Many interacting factors; form is unreliable |

**Most horse racing is CAPM-like:** one factor (raw ability/class) explains
most of the variance in finishing positions. Exotic races (handicaps, large
fields, unusual conditions) tend toward the Clifford or pseudo-Anosov types.

---

## 2. The Bookmaker's Overround as Geometry

### 2.1 The overround

A bookmaker offers decimal odds $o_1, \ldots, o_d$ on $d$ runners. The
implied probabilities are:
$$q_i = \frac{1}{o_i} \bigg/ \sum_j\frac{1}{o_j} \tag{2.1}$$

The **overround** (vig, juice, margin) is:
$$\Omega = \sum_i\frac{1}{o_i} - 1 > 0 \tag{2.2}$$

For a fair book: $\Omega = 0$. For a typical bookmaker: $\Omega \approx 0.05$–$0.20$
(5%–20% margin).

### 2.2 The geometric interpretation

The true win probabilities $p = (p_1, \ldots, p_d) \in \Delta_{d-1}$ and the
bookmaker's implied probabilities $q = (q_1, \ldots, q_d) \in \Delta_{d-1}$
are two points on the race simplex. The Fisher-Rao distance between them
measures how much information the bettor has that the bookmaker doesn't:

$$d_{g^{\rm FR}}(p, q) = 2\arccos\sum_i\sqrt{p_i q_i} \tag{2.3}$$

**Theorem 2.1** *(Edge = Fisher-Rao displacement)*.
*The bettor's expected log-growth advantage over the bookmaker is determined
by the Fisher-Rao distance between the true probabilities $p$ and the
implied probabilities $q$:*

$$\mathbb{E}[\text{log-growth per race}] = D_{\rm KL}(p \| q) - \frac{\Omega}{1+\Omega} \approx \frac{1}{2}d^2_{g^{\rm FR}}(p,q) - \frac{\Omega}{1+\Omega} \tag{2.4}$$

*The first term is the information edge (positive when you know $p$ better
than the bookmaker). The second term is the vig (always negative). A
profitable bettor needs $d_{g^{\rm FR}}(p,q) > \sqrt{2\Omega/(1+\Omega)}$
— the edge must exceed the margin.*

*Proof.* The bettor's expected log-wealth per race, betting according to
true probabilities $p$ against implied probabilities $q$ with overround
$\Omega$, decomposes as:

$$\mathbb{E}_p[\log(b_0 + b_{\rm winner} \cdot o_{\rm winner})] = D_{\rm KL}(p \| q) - \log(1 + \Omega)$$

where $D_{\rm KL}(p \| q) = \sum_i p_i \log(p_i/q_i)$ is the
Kullback-Leibler divergence (the information edge) and $\log(1+\Omega) \approx \Omega/(1+\Omega)$
is the cost of the vig. The Pinsker-type inequality
$D_{\rm KL}(p\|q) \geq \frac{1}{2}d^2_{g^{\rm FR}}(p,q)$ (with approximate
equality for small displacements) gives the Fisher-Rao formulation. The
bettor profits when the information edge exceeds the transaction cost. $\square$

**Interpretation:** The overround $\Omega$ is NOT the Fisher-Rao distance
— it is a transaction cost, analogous to the bid-ask spread in financial
markets. A bookmaker can have $\Omega > 0$ with $q = p$ (uniform margin,
no mispricing). The bettor's edge comes entirely from the displacement
$q \neq p$, measured by $d_{g^{\rm FR}}(p,q)$. The overround determines how
large the displacement must be before the bettor can profit.

### 2.3 The efficient bookmaker

An informationally efficient bookmaker has $q = p$ (true implied
probabilities), regardless of the overround. The overround $\Omega$ is a
spread/transaction cost — analogous to the bid-ask spread in financial
markets. An efficient bookmaker with positive vig has raw odds
$1/o_i = p_i(1+\Omega)$, so $q_i = p_i$ after normalisation. No betting
strategy has positive expected log-growth against an efficient bookmaker
AFTER paying the vig.

The EMH for racing is therefore: no bettor can achieve positive expected
log-growth after paying the vig. This is a weaker condition than $H = 0$;
it is $H = 0$ modulo the transaction cost boundary layer.

**No bookmaker is perfectly efficient.** The overround is always positive ($\Omega > 0$),
and real bookmakers inevitably have $q \neq p$ for at least some runners.
The question is: how large is the displacement $d_{g^{\rm FR}}(p,q)$, and
does it exceed the vig threshold $\sqrt{2\Omega/(1+\Omega)}$?

The geometric decomposition of the displacement: $d_{g^{\rm FR}}(p,q)$ can
be separated into a systematic component (the favourite-longshot bias,
present in all races) and a race-specific component (the bookmaker's
informational error on this particular race). A sophisticated punter
exploits races where the race-specific component is large — races where
the bookmaker's model is poor relative to the bettor's.

---

## 3. The Favourite-Longshot Bias

### 3.1 The empirical fact

The favourite-longshot bias (FLB) is one of the most robust findings in
gambling research (Griffith 1949; Ali 1977; Snowberg and Wolfers 2010):

- Favourites (short-priced horses) are **underbet** relative to their true
  win probability. They win more often than their odds imply.
- Longshots (long-priced horses) are **overbet** relative to their true
  win probability. They win less often than their odds imply.

The bias is present in every major racing jurisdiction, persists over decades,
and survives attempts to exploit it.

### 3.2 The geometric explanation

**Theorem 3.1** *(FLB = mean curvature of the odds manifold)*.
*The favourite-longshot bias is the mean curvature vector $\vec{H}$ of the
bookmaker's odds manifold $\mathcal{O} \subset S^{d-1}_+$, pointing from
longshots toward favourites.*

*Proof sketch.* The bookmaker's odds $q$ are displaced from the true
probabilities $p$ by the overround. The displacement is not uniform across
runners — it is systematically biased toward longshots (the bookmaker inflates
longshot odds more than favourite odds, because bettors are attracted to
large potential payoffs). In Fisher-Rao geometry, this non-uniform
displacement is exactly the mean curvature: the odds surface curves toward
the favourite corner of the simplex and away from the longshot corner.

More precisely: the second fundamental form of $\mathcal{O}$ in the direction
of the $i$-th horse is $B_{ii} \propto (p_i - q_i)/\sqrt{p_i}$. For favourites
($p_i > q_i$): $B_{ii} > 0$. For longshots ($p_i < q_i$): $B_{ii} < 0$.
The trace (mean curvature) is $H = \sum B_{ii}/d \propto \sum(p_i - q_i)/\sqrt{p_i}$,
which is positive because favourites contribute more (large $p_i$, positive
displacement) than longshots (small $p_i$, negative displacement). $\square$

### 3.3 The exploitable edge

By the Sharpe-curvature identity:
$$\mathrm{Sharpe}_{\rm FLB}^* = \|H\|_{L^2(\mathcal{O})} \tag{3.1}$$

The maximum Sharpe ratio of any betting strategy exploiting the FLB is
computable from publicly available odds.

**Note:** The table below gives illustrative estimates based on typical FLB
magnitudes. The Sharpe-curvature identity applies to the DISPLACEMENT
$d_{g^{\rm FR}}(p,q)$, not the overround $\Omega$ directly. The $\|H\|_{L^2}$
values are estimated from empirical studies of the FLB magnitude in each
market, not derived from $\Omega$.

| Market | $\Omega$ | $\|H\|_{L^2}$ (est.) | Sharpe (annualised, est.) |
|:-------|:--------:|:--------------------:|:------------------------:|
| UK horse racing (SP) | ~15% | ~0.08 | ~0.25 |
| Australian racing (TAB) | ~18% | ~0.10 | ~0.30 |
| US horse racing (tote) | ~20% | ~0.12 | ~0.35 |
| Football (Pinnacle) | ~3% | ~0.02 | ~0.06 |
| Football (high-street bookie) | ~10% | ~0.06 | ~0.18 |

**Pinnacle (the sharpest sports bookmaker) has the lowest mean curvature.**
Their odds manifold is closest to minimal. Betting against Pinnacle has the
lowest edge. Betting against a high-street bookmaker has 3x the edge —
because their odds manifold curves more.

---

## 4. Kelly Betting on Horse Racing

### 4.1 The Kelly formula for racing

The correct model for horse race betting includes a cash (no-bet) asset.
The bettor allocates fraction $b_0$ to cash (kept regardless of outcome)
and $b_i$ to horse $i$. The bet vector lives on $\Delta_d$ (the $d+1$-dimensional
simplex including cash), with $b_0 = 1 - \sum_{i \geq 1} b_i$.

The return vector for race $t$ is $x_t \in \mathbb{R}^{d+1}_+$ where
$x_{t,0} = 1$ (cash) and $x_{t,i} = o_i$ if horse $i$ wins, $0$ otherwise.
The wealth evolution is:

$$W_{t+1} = W_t \cdot (b_0 + b_{\rm winner} \cdot o_{\rm winner}) \tag{4.0}$$

The Kelly growth rate is $\mathbb{E}[\log(b_0 + b_{\rm winner} \cdot o_{\rm winner})]$.
Given true win probabilities $p$ and decimal odds $o$, the Kelly bet is:

$$b^*_i = \max\left(0, \frac{p_i o_i - 1}{\sum_j p_j o_j - 1}\right) \tag{4.1}$$

with the cash component $b^*_0 = 1 - \sum_{i \geq 1} b^*_i$ absorbing the
residual. Note: without the cash asset, maximising $\mathbb{E}[\log\langle b, x\rangle]$
on $\Delta_{d-1}$ with $x_i = o_i \cdot \mathbf{1}_{i=\rm winner}$ gives
$b_i = p_i$ (independent of odds), which is clearly wrong. The cash asset
is essential — it provides the "don't bet" option that makes the Kelly
formula sensitive to the odds.

### 4.2 The MUP bettor

The Kelly bettor needs to know $p$ (the true probabilities). The MUP bettor
does not — it integrates over all possible $p$ weighted by evidence from
past races:

$$b^{\rm MUP}_T = \frac{\int_{M^r} b(p)\, W_T(b(p))\, d\mathrm{vol}(p)}{\int_{M^r} W_T(b(p))\, d\mathrm{vol}(p)} \tag{4.2}$$

where $M^r$ is the race manifold (the set of plausible true probability
vectors, with $r$ independent factors — class, going, distance, jockey, etc.).

**The MUP bettor is the optimal punter who does not know the true odds but
learns them from race results.** Its regret — the log-wealth gap to the
Kelly bettor who knows $p$ — is $r\log T/(2T)$ where $T$ is the number
of races observed and $r$ is the number of independent racing factors.

### 4.3 Fractional Kelly

In practice, most serious punters use fractional Kelly — betting a fraction
$f \in (0,1)$ of the Kelly-optimal amount. In our framework:

$$b^f = (1-f)\cdot b^{\rm cash} + f\cdot b^* \tag{4.3}$$

where $b^{\rm cash} = (1, 0, \ldots, 0)$ (keep everything in cash).

**Important clarification:** Fractional Kelly $b^f = (1-f) \cdot b^{\rm cash} + f \cdot b^*$
is a Euclidean convex combination, NOT a Fisher-Rao geodesic. The Fisher-Rao
geodesic from $b^{\rm cash}$ to $b^*$ has a different parameterisation (it
passes through the Bhattacharyya sphere). The Euclidean mixture is the
PRACTICAL fractional Kelly; the Fisher-Rao geodesic would be the
GEOMETRICALLY correct interpolation. For small $f$, the two agree to
leading order.

The log-growth rate of fractional Kelly is:
$$g(f) = \mathbb{E}[\log(1 - f + f \cdot (b^* \cdot x))] \tag{4.4}$$

which is concave in $f$ with maximum at $f = 1$ (full Kelly) and $g(0) = 0$
(no bet). The variance of log-wealth is approximately $f^2 \cdot \mathrm{Var}(\log(b^* \cdot x))$.
The risk-adjusted optimal fraction is $f^* = 1/(\text{risk aversion})$.

**Geometric interpretation of fractional Kelly:** it interpolates between
"don't bet" and "full Kelly" in Euclidean space on the simplex. The
log-growth rate along this interpolation is concave in $f$ (peaking at
$f = 1$), but the variance is quadratic in $f$. The practical punter
chooses $f$ to balance growth rate against drawdown risk.

---

## 5. The Harville Formula and Finishing Orders

### 5.1 Harville's model

Harville (1973) proposed that the probability of a finishing order
$(\sigma_1, \sigma_2, \ldots, \sigma_d)$ (horse $\sigma_k$ finishes $k$-th) is:

$$P(\sigma_1, \ldots, \sigma_d) = \prod_{k=1}^{d}\frac{p_{\sigma_k}}{1 - \sum_{j=1}^{k-1}p_{\sigma_j}} \tag{5.1}$$

This is used to price exotic bets (exactas, trifectas, superfectas).

### 5.2 The geometric interpretation: sequential absorption

**Conjecture 5.1** *(Harville-Jacobi correspondence)*.
*The Harville finishing-order formula is consistent with a sequential
absorption model on the simplex with Jacobi-type dynamics. The precise
identification requires:*

*(i) specifying the SDE in the standard Wright-Fisher form
$db_i = \varepsilon^2(\alpha_i - |\alpha|b_i)\,dt + \varepsilon\sqrt{b_i}\,dW_i$;*

*(ii) computing the multi-exit absorption density;*

*(iii) matching to the Harville product formula.*

*Steps (i)-(ii) are standard; step (iii) is the non-trivial identification
that we conjecture holds when the Jacobi parameters $\alpha_i$ are
proportional to the win probabilities $p_i$.*

**Remark.** The intuition is natural: consider a Jacobi diffusion on
$\Delta_{d-1}$ where each coordinate $b_i$ represents horse $i$'s
"survival probability." When $b_i$ hits zero (the $i$-th face of
$\Delta_{d-1}$), horse $i$ has been "eliminated." The remaining process
continues on $\Delta_{d-2}$ (one fewer horse). The successive hitting
times of the boundary faces give the finishing order. The Harville formula
would then be the probability of a specific sequence of hitting times,
computed from the Jacobi transition density with absorbing boundary
conditions. This is plausible but not yet proved.

### 5.3 When Harville fails

The Harville model assumes horses finish independently (conditional on
abilities $p$). This fails when:

- **Pace effects:** a fast early pace hurts all frontrunners (correlation
  within running styles)
- **Jockey tactics:** jockeys in the same stable may cooperate
- **Track position:** inside draw advantage in short races

In geometric terms: Harville fails when the race manifold has non-trivial
topology (the factors are correlated, so the manifold is not a product).
The Henery model (1981) and the Stern model (1990) correct for this by
allowing correlated Jacobi diffusions — equivalent to a non-diagonal
Fisher information matrix on the race simplex.

---

## 6. Sports Betting: Football, Tennis, Cricket

### 6.1 Football (soccer) as a three-asset market

A football match has three outcomes: home win, draw, away win. The bet
simplex is $\Delta_2$ — a triangle. The bookmaker's odds define a point
$q \in \Delta_2$. The true probabilities are $p \in \Delta_2$.

The Fisher-Rao geometry of $\Delta_2$ is completely explicit:
- The Bhattacharyya sphere is $S^2_+$ (positive octant of the unit sphere)
- Geodesics are great circle arcs
- The curvature is $K = 1/4$ everywhere

**The football betting problem is the simplest non-trivial market:**
$d = 3$ assets, $r = 2$ factors (home strength, away strength), and the
manifold $M^2 \subset S^2_+$ is a 2D surface in 3D space — visualisable.

### 6.2 The draw as the key to football betting

**Theorem 6.1** *(The draw anomaly is the Clifford torus of football betting)*.
*In football betting, the draw outcome exhibits anomalous pricing
analogous to the favourite-longshot bias. The draw is systematically
overpriced by bookmakers (implied probability too high) because:*

*(i) Draws are the least popular bet (bettors prefer decisive outcomes)*

*(ii) The bookmaker loads more margin onto the draw (behavioural finance)*

*(iii) The draw probability is the most stable across matches (lowest
variance), so the bookmaker has the least informational edge on draws*

*Geometrically: the draw direction in $\Delta_2$ has the lowest curvature
(most "flat" direction of the odds manifold). The mean curvature vector
$\vec{H}$ points away from the draw vertex and toward the win vertices.*

### 6.3 Tennis as a two-asset market

A tennis match has two outcomes: player A wins, player B wins. The bet
simplex is $\Delta_1 = [0,1]$ — an interval. This is the simplest possible
market: one-dimensional, and the Fisher-Rao metric is:

$$g^{\rm FR}(b) = \frac{1}{b(1-b)} \tag{6.1}$$

This is the metric of the Jacobi diffusion from Paper II.3. Tennis match
probabilities evolve during the match as a Jacobi diffusion on $[0,1]$
with the match state (sets, games, points) as the "time" variable.

**In-play tennis betting IS a Jacobi diffusion.** The live odds during a
match trace a path on $[0,1]$ with the Jacobi SDE. The spectral gap
$\lambda_1$ determines how quickly the odds mean-revert after a break of
serve. The mean-reversion speed IS the informational efficiency of the
in-play market.

### 6.4 Cricket as a high-dimensional sequential market

A cricket match evolves through balls, overs, wickets, and innings. The
outcome space grows exponentially. But the Fisher-Rao framework applies:

- **State:** probability of each team winning, given the current match state
- **Manifold:** the set of match states consistent with the current score and situation
- **Factor structure:** $r \approx 3$ (batting strength, bowling strength, conditions)
- **Process:** a compound Jacobi diffusion (continuous drift from runs scored,
  jumps from wickets falling)

The Feller boundary analysis (Paper II.5) gives: wickets are **exit boundaries**
(absorbing), while the score is a continuous state variable. A team's
innings ends when 10 wickets fall — 10 successive Feller boundary hits.

---

## 7. Casino Games: Blackjack and Poker

### 7.1 Card counting as manifold Kalman filtering

In blackjack, the remaining deck composition determines the house edge. A
full deck of 52 cards has state space $\Delta_{51}$ (the fraction of each
card remaining). As cards are dealt, the state moves through the simplex.

**Card counting systems are factor projections.** The Hi-Lo system assigns
$+1$ to cards 2–6, $0$ to 7–9, $-1$ to 10–A, and tracks the running count.
This is a projection from $\Delta_{51}$ to $\mathbb{R}^1$ — a one-factor
model ($r = 1$) of the deck state.

| Counting system | Factors $r$ | Projection type |
|:---------------|:-----------:|:---------------|
| Hi-Lo | 1 | Single linear combination |
| Omega II | 2 | Two linear combinations (high/low + neutral) |
| Wong Halves | 1 | Refined single projection (fractional values) |
| Zen Count | 2 | Two projections with different weighting |
| Full deck tracking | 9 | Track all 10 denominations (minus 1 for constraint) |

**Theorem 7.1** *(Optimal card counting = manifold Kalman filter)*.
*The information-theoretically optimal card counting system is the manifold
Kalman filter (Paper III.6) applied to the deck simplex $\Delta_{51}$. The
optimal number of "counts" to track is the effective dimension $r$ of the
deck manifold — the number of independent factors affecting the house edge.*

*For standard blackjack: $r \approx 2$–$3$ (high cards, low cards, aces).
The Omega II system ($r = 2$) is therefore near-optimal among practical
counting systems. Full deck tracking ($r = 9$) captures the remaining
information but at much higher cognitive cost.*

### 7.2 Poker as a game on the information simplex

In poker, each player has a probability distribution over opponent hands.
As the hand progresses (preflop -> flop -> turn -> river), the distribution
updates via Bayesian inference. Each player's belief is a point on the
simplex $\Delta_{N-1}$ where $N = \binom{52}{2} = 1326$ (possible two-card
holdings).

**The poker information manifold** has:
- Dimension $r \approx 3$–$5$ (hand strength, position, betting pattern,
  player type, stack depth)
- Fisher-Rao metric measuring the distinguishability of opponent hand ranges
- Mean curvature measuring the informativeness of each street

**Bluffing is movement along the mean curvature vector.** When a player
bets with a weak hand (bluff), they move their perceived position on the
information manifold in the direction of $\vec{H}$ — toward the "strong hand"
region. The efficiency of the bluff depends on $|\vec{H}|$ at the current
information state.

---

## 8. The Punter's Practical Guide

### 8.1 What the geometry tells you to do

**Rule 1: Know your edge in Fisher-Rao units.**
Before placing any bet, compute $d_{g^{\rm FR}}(p, q)$ — the Fisher-Rao
distance between your estimated true probabilities and the bookmaker's implied
probabilities. If $d < 0.05$: you have no meaningful edge, don't bet.
If $d > 0.10$: you have a significant edge. If $d > 0.20$: either you're
right and it's a great bet, or you're wrong and your probability estimates
are poor. Check your estimates.

**Rule 2: Kelly sizing, always.**
Size every bet using the Kelly formula (4.1). Never bet more than Kelly
(that's the region of negative expected log-growth — guaranteed long-run ruin).
Fractional Kelly ($f = 0.25$–$0.50$) if you're uncertain about your edge.

**Rule 3: The bookmaker's overround is your cost of admission.**
The overround $\Omega$ is the price you pay for the privilege of betting.
You need a Fisher-Rao edge of at least $d_{g^{\rm FR}}(p,q) > \sqrt{2\Omega/(1+\Omega)}$
to overcome the vig. For a 5% margin bookmaker: $\sqrt{2 \cdot 0.05/1.05} \approx 0.31$.
For a 20% margin: $\sqrt{2 \cdot 0.20/1.20} \approx 0.58$. Bet with the sharpest
bookmaker you can access.

**Rule 4: Bet where the manifold curves most.**
The FLB (favourite-longshot bias) is largest in markets with high curvature:
large fields, high overround, unsophisticated bookmaker. Handicap races
with 20+ runners at a high-street bookmaker have the highest
$\|H\|_{L^2}$. Two-runner match bets on Betfair have the lowest.

**Rule 5: Track your Sharpe ratio, not your P&L.**
A winning punter should have Sharpe ratio $\approx \|H\|_{L^2}$ computed
over a rolling window of at least $T = 1/\varepsilon^2$ bets. For racing
($\varepsilon^2 \approx 1/100$ per race): you need at least 100 bets to
distinguish skill from luck. For football ($\varepsilon^2 \approx 1/50$):
at least 50 bets.

### 8.2 What the geometry tells you NOT to do

**Don't bet accumulators.** An accumulator (parlay) bets on multiple
independent outcomes simultaneously. In geometric terms: it moves you from
$\Delta_{d-1}$ to $\Delta_{d^k-1}$ (product simplex for $k$ legs). The
overround compounds: $\Omega_{\rm acca} \approx k\Omega$. The Fisher-Rao
distance you need to overcome grows as $\sqrt{k}$. Four-fold accumulators
at a 10% margin bookmaker require Fisher-Rao edge $> 0.89$. Almost no one
has that edge.

**Don't bet in-play unless your model updates faster than the market.**
In-play markets are Jacobi diffusions. The spectral gap $\lambda_1$ gives
the speed at which information is priced. If you can't update your
probability estimates faster than $1/\lambda_1$ (typically 5–30 seconds
for tennis, 1–5 minutes for football): you are trading against someone who
can.

**Don't confuse a long losing streak with a bad system.**
The probability of a losing streak of length $L$ for a Kelly bettor with
Fisher-Rao edge $d_{g^{\rm FR}}(p,q)$ is approximately $\exp(-L \cdot d^2_{g^{\rm FR}}/2)$.
(Here $d_{g^{\rm FR}}$ is the displacement between true and implied
probabilities, not the overround.) For edge $d = 0.10$: a streak of 200
losers in a row has probability $\exp(-1) \approx 37\%$.
Losing 200 bets in a row does NOT mean your system is broken. It means
you're a gambler. The Fisher-Rao distance is small. Welcome to the simplex.

---

## 9. The Connection to Prediction Markets

### 9.1 A prediction market is a horse race with information arrival

A prediction market (Polymarket, Kalshi, PredictIt) prices the probability
of an event: "Will X happen?" The market price $q$ is the implied
probability. The true probability $p$ is unknown.

This is identical to a horse race with two runners (yes/no) and continuous
trading. The bet simplex is $\Delta_1 = [0,1]$. The market price traces a
path $q_t \in [0,1]$ that is a Jacobi diffusion (Paper II.3) with:
- Drift: toward the true probability $p$ (information arrival)
- Volatility: proportional to $\sqrt{q(1-q)}$ (maximal at $q = 1/2$)
- Boundary: absorbing at $q = 0$ and $q = 1$ (the event resolves)

**The prediction market IS the Jacobi diffusion.** Every result in
Paper II.3 (MARKET_PROCESSES) applies directly. The spectral gap gives the
information arrival rate. The Feller boundary classification gives the
resolution dynamics. The Kelly criterion gives the optimal trading strategy.

### 9.2 Multi-outcome prediction markets and polytopes

A prediction market with $d$ mutually exclusive outcomes (e.g., "Who will
win the election?") has prices $q_1, \ldots, q_d$ with $\sum q_i = 1$
(after normalisation). This is a point on $\Delta_{d-1}$ — the prediction
simplex.

**The market-making mechanism defines the geometry.** For a logarithmic
market scoring rule (LMSR, Hanson 2003):

$$C(q) = b\log\sum_i e^{q_i/b} \tag{9.1}$$

the cost function $C$ is convex on $\mathbb{R}^d$, and the prices
$p_i = \partial C/\partial q_i = e^{q_i/b}/\sum e^{q_j/b}$ are the softmax
of the $q_i$. **The LMSR is the softmax function.** This is the same
connection as Paper IV.2 (LLM_MANIFOLD): market-making = softmax = Fisher-Rao.

The prediction market polytope — the set of arbitrage-free price vectors —
is the simplex $\Delta_{d-1}$ itself. The boundary faces correspond to
certainty about individual outcomes. The interior corresponds to genuine
uncertainty. The centroid $q = (1/d, \ldots, 1/d)$ is maximum uncertainty.

**Arbitrage in prediction markets is movement outside the simplex.**
If $\sum q_i > 1$: the market is overpriced (total implied probability
exceeds 1). The excess $\Omega = \sum q_i - 1$ is the overround — the
prediction market's equivalent of the bookmaker's vig. If $\sum q_i < 1$:
the market is underpriced, and there is a Dutch book (guaranteed profit
from buying all outcomes).

### 9.3 Conditional prediction markets

A conditional prediction market prices "What is $P(A | B)$?" This is a
point on the fiber of the conditional probability bundle $\mathcal{B}$
with base $\mathcal{P}(B)$ (the market for event $B$) and fiber
$\mathcal{P}(A | B)$ (the conditional market).

This is exactly the fiber bundle structure of Paper II.2 (FIBER_BUNDLES):
- Base: the unconditional market
- Fiber: the conditional market
- Connection: how conditioning on $B$ changes the price of $A$
- Curvature: the failure of conditional independence

**The inflation paper's fiber bundle structure applies to conditional
prediction markets.** Capital flowing from the $B$-market to the $A|B$-market
is a connection. The curvature is the "correlation premium" — the extra
return from understanding the dependence between $A$ and $B$.

---

## 10. New Results for the Monograph

**Lemma G1** *(Edge-displacement correspondence)*. The bettor's expected
log-growth advantage is $D_{\rm KL}(p \| q) - \log(1+\Omega) \approx
\frac{1}{2}d^2_{g^{\rm FR}}(p,q) - \Omega/(1+\Omega)$. The first term is
the information edge from the displacement $q \neq p$; the second is the
transaction cost from the overround. The overround $\Omega$ is a vig, not a
curvature — a bookmaker with $q = p$ (no mispricing) has zero edge regardless
of $\Omega$. A fair book ($\Omega = 0$) removes the transaction cost but
does not guarantee $q = p$; a minimal odds manifold ($H = 0$) requires both
$q = p$ and $\Omega = 0$.

**Lemma G2** *(Kelly regret for the MUP bettor)*. The MUP bettor's regret
on a sequence of $T$ races with $d$ runners and $r$ independent factors is
$r\log T/(2T)$, identical to the portfolio case. For $d = 12$ (typical
field), $r = 3$, $T = 1000$ races: regret $\approx$ 1.0%.

**Lemma G3** *(Harville-Jacobi conjecture)*. The Harville finishing-order
formula is conjectured to be the multi-exit Jacobi transition density on
$\Delta_{d-1}$ with sequential Feller absorption, when Jacobi parameters
$\alpha_i \propto p_i$. The Henery and Stern corrections would correspond
to correlated Jacobi diffusions (non-diagonal Fisher matrix). See
Conjecture 5.1 for the precise statement and required verification steps.

**Lemma G4** *(Card counting optimality)*. The optimal card counting system
for shoe-dealt blackjack tracks $r = \mathrm{rank}_{\rm stable}(F_{\rm deck})$
independent counts, where $F_{\rm deck}$ is the Fisher information matrix
of the deck composition. For 6-deck shoe: $r \approx 2$–$3$.

**Lemma G5** *(Prediction market = Jacobi diffusion)*. A binary prediction
market with continuous trading is a Jacobi diffusion on $[0,1]$ with
absorbing boundaries. The LMSR cost function is the free energy of the
Jacobi stationary distribution. The LMSR = softmax = Fisher-Rao identity
from Paper IV.2 applies.

---

## References

Ali, M. M. (1977). Probability and utility estimates for racetrack bettors.
*Journal of Political Economy* 85(4), 803–815.

Cover, T. M. (1966). Gambling on horses. Unpublished manuscript (circulated
in the Cover-Thomas textbook tradition).

Cover, T. M. and Thomas, J. A. (2006). *Elements of Information Theory*,
2nd edition. Wiley. Chapter 6: Gambling and data compression.

Griffith, R. M. (1949). Odds adjustments by American horse-race bettors.
*American Journal of Psychology* 62(2), 290–294.

Hanson, R. (2003). Combinatorial information market design.
*Information Systems Frontiers* 5(1), 107–119.

Harville, D. A. (1973). Assigning probabilities to the outcomes of
multi-entry competitions. *Journal of the American Statistical Association*
68(342), 312–316.

Henery, R. J. (1981). Permutation probabilities as models for horse races.
*Journal of the Royal Statistical Society B* 43(1), 86–91.

Kelly, J. L. (1956). A new interpretation of information rate.
*Bell System Technical Journal* 35(4), 917–926.

Snowberg, E. and Wolfers, J. (2010). Explaining the favorite-long shot bias:
is it risk-love or misperceptions? *Journal of Political Economy* 118(4), 723–746.

Stern, H. (1990). Models for distributions on permutations.
*Journal of the American Statistical Association* 85(410), 558–564.

Thorp, E. O. (1966). *Beat the Dealer*. Vintage.

*[All other references as per companion papers.]*
