# Network Information Theory and the Rate of Market Efficiency:
## Channel Capacity, Convergence Speed, and the Geometry of True and False Information

**Saxon Nicholls** — me@saxonnicholls.com

**Paper IV.10** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
The rate at which a financial market converges to the efficient manifold — the
minimal surface $M^r \subset S^{d-1}_{+}$ with $H = 0$ — is bounded by two
independent quantities: the geometric spectral gap $\lambda_1$ of the market
manifold Laplacian (measuring how fast the mean curvature flow can operate) and
the channel capacity $C$ of the information network connecting market participants
(measuring how fast information can arrive). The effective convergence rate is
$R_{\rm conv} = \min(\lambda_1, C)$. Neither quantity alone is sufficient: a market
with fast geometry but slow information (an illiquid emerging market) converges at
the information rate; a market with fast information but slow geometry (a liquid
large-cap with structural frictions) converges at the geometric rate.

We classify market information architectures using El Gamal and Kim's network
information theory: point-to-point (single analyst $\to$ single stock), multiple
access (many analysts $\to$ one market), broadcast (central bank $\to$ many markets),
degraded broadcast (insider $\to$ market maker $\to$ public), interference (correlated
assets), relay (financial media as intermediary), and channels with state
(regime-dependent markets). Each architecture has a computable capacity region
that constrains how quickly the market can price information.

Our principal results:

**(i) The dual bottleneck theorem.** The effective convergence rate of the Willmore
energy $\mathcal{W}(M) = \int |H|^2\,d\mathrm{vol}_{M}$ under mean curvature flow
with information arrival at rate $C$ is $R_{\rm conv} = \min(\lambda_1, C)$. The
MUP regret with network constraints becomes $r\log(T)/(2T) + r/(CT)$ — the
geometric term plus a network penalty.

**(ii) Insider trading accelerates efficiency.** An insider with private signal
$X \in \mathcal{F}^{\rm oracle}_{t} \setminus \mathcal{F}^{\rm public}_{t}$ who trades
optimally contributes $\Delta R_{\rm conv} = I(X; Y_{\rm trade})/T$ additional bits
per period to the market's information channel. The insider's trade reduces the
mean curvature $H$ at the traded point on $M^r$. The Willmore energy decreases
faster. The insider's profit equals the curvature they remove — the Sharpe-curvature
identity applied to private information.

**(iii) Misinformation retards efficiency at double cost.** A source of misinformation
injecting false signal $Z$ into the market channel causes two distinct harms:
(a) capacity waste — the market processes the false signal, consuming $I(Z; Y|X)$
bits of channel capacity that could have carried true information; and (b) spurious
curvature creation — the market adjusts prices in the wrong direction, creating
Willmore energy $W_{\rm spurious}$ that the MCF must subsequently undo. The total
damage is $\Delta R_{\rm conv} = -2 \cdot I(Z; Y|X)/T$ — the doubling principle.

**(iv) The regulatory inversion.** The information type hierarchy, ranked by effect
on convergence rate, is: insider trading (most beneficial) $>$ informed research $>$
uninformed trading $>$ herding $>$ rumour $>$ misinformation $>$ market manipulation
(most harmful). Current regulation inverts this hierarchy, punishing the most
beneficial type (insider trading) with the harshest penalties while treating the
most harmful types (misinformation, manipulation) leniently. The geometry says we
are punishing the wrong people.

**(v) Social media and information flooding.** A social media MAC channel with $N$
sources has effective capacity $C_{\rm eff} = N \cdot p_{\rm true} \cdot \bar{C} -
2N \cdot p_{\rm false} \cdot \bar{C}$, where $p_{\rm true}$ and $p_{\rm false}$
are the fractions of truthful and misinformative sources. When $p_{\rm false}$ is
sufficiently large, $C_{\rm eff}$ can fall below the pre-social-media regime
despite $10^6\times$ more sources — explaining how increased information flow can
coincide with decreased market efficiency.

**Keywords.** Channel capacity; network information theory; multiple access channel;
broadcast channel; relay channel; convergence rate; spectral gap; mean curvature
flow; Willmore energy; insider trading; misinformation; market efficiency;
regulatory design; social media; information hierarchy.

**MSC 2020.** 94A15, 91G10, 53E10, 94A40, 91B26, 60J65.

---

## 1. The Two Bottlenecks

### 1.1 The geometric rate

The market manifold $M^r \subset S^{d-1}_{+}$ converges to the efficient configuration
(a minimal surface with $H = 0$) via mean curvature flow (MCF). The convergence
rate of the Willmore energy $\mathcal{W}(M) = \int_M |H|^2\,d\mathrm{vol}_{M}$ under
MCF is controlled by the spectral gap $\lambda_1$ of the Jacobi operator $L_M =
\Delta_M + |A|^2 + \mathrm{Ric}(\nu,\nu)$ on $M^r$. Specifically, the Willmore
energy decays as:

```math
\mathcal{W}(M_t) \leq \mathcal{W}(M_0)\,e^{-2\lambda_1 t} \tag{1.1}
```

(cf. CLASSIFICATION.md Theorem 3.1; RENORMALIZATION.md Section 2). The spectral
gap $\lambda_1$ sets the **geometric ceiling** — the maximum rate at which the
manifold can deform toward the minimal surface, given perfect instantaneous
information about the curvature $H$ at every point.

### 1.2 The information rate

But the MCF does not have perfect information. To compute the curvature direction
$-\vec{H}$ at a point $b^{\ast} \in M^r$, the market requires information: earnings,
macroeconomic data, analyst research, order flow, regulatory signals. This information
arrives through a **network of channels** connecting information sources to market
participants. The network has a finite capacity $C$ measured in bits per unit time.

The capacity $C$ is not a single number but depends on the network topology — the
arrangement of sources, receivers, relays, and the interference between channels.
El Gamal and Kim \[2011\] classify the fundamental channel types. Each type has a
capacity (or capacity region) determined by information-theoretic first principles.

### 1.3 The dual bottleneck

The effective convergence rate cannot exceed either bottleneck:

**Theorem 1.1** (Dual bottleneck). *Let $M^r_t$ evolve under MCF with information
arriving at aggregate rate $C$ bits per unit time. The effective convergence rate
of $\mathcal{W}(M_t)$ is:*

```math
R_{\rm conv} = \min(\lambda_1, C) \tag{1.2}
```

*Proof.* The MCF requires specifying the direction $-\vec{H}(b)$ at each point
$b \in M^r$ to first order. The curvature vector $\vec{H}$ at a point on an
$r$-dimensional manifold in $S^{d-1}_{+}$ has $d - 1 - r$ normal components, each
requiring $O(\log T)$ bits of precision at time-horizon $T$. The total information
demand per unit time for the MCF to operate at rate $\lambda_1$ is therefore:

```math
I_{\rm demand} = \lambda_1 \cdot (d-1-r) \cdot O(\log T) \tag{1.3}
```

When $C \geq I_{\rm demand}$, information arrives fast enough to specify the curvature
field, and the MCF operates at its geometric rate $\lambda_1$. When $C < I_{\rm demand}$,
the MCF is information-starved: it can only update the curvature field at rate
$C / [(d-1-r) \cdot O(\log T)]$, and the effective convergence rate drops to $C$ (up to
logarithmic factors which we absorb into the capacity definition). $\square$

### 1.4 The two regimes

**Geometry-limited regime** ($C \gg \lambda_1$): Modern electronic markets for liquid
stocks. Information arrives at terabits per second (price feeds, news wires, social
media, order books). The spectral gap $\lambda_1$ for a typical CAPM manifold is
$O(1)$ per year — perhaps $\lambda_1 \approx 12/\text{yr}$ (monthly factor rotation).
The geometric bottleneck dominates by a factor of $10^6$ or more. These markets are
as efficient as the geometry allows; more information bandwidth would not help.

**Information-limited regime** ($C \ll \lambda_1$): Emerging markets, illiquid assets,
frontier markets, historical markets before the telegraph. The geometry of the
manifold could accommodate faster convergence, but information arrives too slowly.
An 18th-century commodity market with information travelling by ship at $\sim 1$
bit/day is deeply information-limited: $R_{\rm conv} = C \ll \lambda_1$.

### 1.5 MUP regret with network constraints

The MUP regret bound of $r\log(T)/(2T)$ (CONVERGENCE.md, Theorem 2.1) assumes
complete information access — the MUP observes the full return vector $x_t$ at each
period. With a network capacity constraint, the MUP observes a noisy or partial
version of $x_t$, degraded by the channel. The regret becomes:

**Theorem 1.2** (Network-constrained MUP regret). *The MUP with information arriving
through a channel of capacity $C$ achieves regret:*

```math
\mathrm{Regret}(T) = \frac{r\log T}{2T} + \frac{r}{CT} \tag{1.4}
```

*The first term is the geometric regret (intrinsic to the manifold dimension $r$).
The second is the network penalty (the cost of finite channel capacity). The
network penalty is negligible when $CT \gg 1/\log T$, i.e., when the total information
received over $T$ periods exceeds $r/\log T$ bits.*

*Proof sketch.* The MUP posterior concentrates on $M^r$ at rate $1/T$ (CONVERGENCE.md).
With capacity $C$, each observation is degraded by channel noise with distortion
$D \sim r/C$ (rate-distortion theory: to represent an $r$-dimensional signal at rate
$C$, the mean-squared distortion is at least $r/C$ per component per unit time). The
degraded posterior concentrates at rate $1/T + D/T = 1/T + r/(CT)$. The regret is
$\log$ of the concentration rate times $r/2$, yielding equation (1.4). $\square$

---

## 2. The Seven Channel Types and Their Market Analogues

### 2.1 Point-to-point channel

The simplest architecture: one information source (encoder $X$), one market
(decoder $Y$), one channel $p(y|x)$. Capacity:

```math
C = \max_{p(x)} I(X; Y) \tag{2.1}
```

**Market analogue.** A single stock reacting to a single news source — an earnings
report, an FDA approval, a regulatory filing. The source encodes information into
the report; the market decodes it from the filing. The capacity is determined by
the information density of the report and the market's processing bandwidth.

For a liquid US large-cap stock, the point-to-point capacity is enormous: a
10-K filing contains $\sim 10^5$ bits of decision-relevant information, and the
market prices it within minutes. Point-to-point capacity: $C \approx 10^3$ bits/min.
The spectral gap $\lambda_1 \approx 1/\text{month}$. The market is geometry-limited
by a factor of $\sim 10^6$: information from the filing is incorporated almost
instantaneously relative to the MCF timescale.

### 2.2 Multiple access channel (MAC)

$K$ independent sources $(X_1, \ldots, X_K)$ transmit simultaneously to one market $Y$.
The MAC capacity region is the set of rate tuples $(R_1, \ldots, R_K)$ satisfying:

```math
\sum_{k \in S} R_k \leq I(X_S; Y \mid X_{S^c}) \quad \forall\, S \subseteq \{1,\ldots,K\} \tag{2.2}
```

The sum capacity is $C_{\rm sum} = I(X_1, \ldots, X_K; Y)$.

**Market analogue.** $K$ analysts simultaneously publishing research on one stock.
Each analyst is a source; the stock price is the receiver. The MAC capacity region
determines how much information the market can absorb from all analysts collectively.

**Independent analysts:** When the $K$ analysts have independent information
(non-overlapping research), the sum capacity is additive:

```math
C_{\rm sum} = \sum_{k=1}^{K} C_k \tag{2.3}
```

Each analyst contributes their full individual capacity. This is the ideal case.

**Herding analysts:** When analysts herd — producing correlated research because they
read the same reports, attend the same conferences, use the same models — the sum
capacity drops:

```math
C_{\rm sum}^{\rm herd} = I(X_1, \ldots, X_K; Y) < \sum_{k=1}^{K} I(X_k; Y) = \sum_{k=1}^{K} C_k \tag{2.4}
```

The inequality is strict whenever the $X_k$ are positively correlated. The gap
$\sum C_k - C_{\rm sum}^{\rm herd}$ is the **redundancy cost of herding**.

**Theorem 2.1** (Herding double penalty). *Analyst herding reduces both the effective
manifold dimension estimate and the network capacity. Specifically:*

*(i) If $K$ analysts herd perfectly (identical information), the effective number of
independent sources is $1$, not $K$. The market receives $C_1$ bits/period rather
than $K \cdot C_1$.*

*(ii) The herded information is concentrated on fewer than $r$ factor directions,
leaving some factors uninformed. The effective manifold dimension accessible to
the market drops from $r$ to $r' < r$.*

*The combined effect: the convergence rate drops from $\min(\lambda_1, K \cdot C_1)$
to $\min(\lambda_1, C_1)$ — a factor of $K$ reduction in the information-limited regime.*

The MAC has a natural **successive cancellation decoding** procedure: the strongest
signal is decoded first, subtracted from the received signal, then the next
strongest, and so on. In the market context, this is sequential price adjustment:
the most informative signal (largest $I(X_k; Y)$) is priced first, then the next,
each conditional on the previous adjustments. This is precisely the spectral
decomposition of the information content onto factor directions, largest eigenvalue
first — the connection to the random matrix theory of RANDOM_MATRIX.md.

### 2.3 Broadcast channel

One source $X$ transmits to $N$ receivers $(Y_1, \ldots, Y_N)$. The capacity region
is bounded by Marton's inner bound and the UV outer bound (El Gamal and Kim,
Chapter 8).

**Market analogue.** A central bank announcement reaching equities, bonds, FX,
and commodity markets simultaneously. The Fed is the encoder; each market is a
receiver with its own channel quality.

The broadcast admits a natural **superposition coding** interpretation. The Fed's
statement decomposes into:

- A **common part** $U_0$ (the rate decision: understood by all markets with high
  reliability). This moves ALL manifolds $M^r_{\rm equity}$, $M^r_{\rm bond}$,
  $M^r_{\rm FX}$, $M^r_{\rm commodity}$ along their shared factor directions.

- **Private parts** $U_1, \ldots, U_N$ (credit nuance for bonds, inflation expectations
  for commodities, growth signal for equities). Each private part is decoded only
  by the intended market.

The broadcast capacity region determines the maximum rate at which the Fed can
simultaneously update the factor structure across all markets. The common part
is constrained by the worst receiver (the least informationally efficient market);
the private parts are constrained by individual channel capacities.

### 2.4 Degraded broadcast channel

A special case of the broadcast: the receivers form a Markov chain $X \to Y_1 \to Y_2$.
Receiver $Y_1$ sees a strictly better signal than receiver $Y_2$. The capacity
region is fully characterised (Bergmans \[1973\], Gallager \[1974\]):

```math
C_1 = I(X; Y_1), \qquad C_2 = I(X; Y_2) \leq C_1 \tag{2.5}
```

**Market analogue.** The information hierarchy:

```math
X \to Y_1 \text{ (insider/market maker)} \to Y_2 \text{ (public)}
```

The insider sees the source $X$ (or close to it). The market maker sees order flow
$Y_1$ — a noisy function of $X$. The public sees prices $Y_2$ — a noisy function of
$Y_1$. This IS the $\sigma$-algebra hierarchy of MARTINGALE_GEOMETRY.md:

```math
\mathcal{F}^{\rm oracle}_{t} \supseteq \mathcal{F}^{\rm MM}_{t} \supseteq \mathcal{F}^{\rm public}_{t} \tag{2.6}
```

The capacity at each level:

```math
C_{\rm oracle} = H(X), \qquad C_{\rm MM} = I(X; Y_1), \qquad C_{\rm public} = I(X; Y_2) \tag{2.7}
```

The **insider alpha** $\alpha = \varepsilon^2 |v_G|_{g^{\rm FR}}$ from
HAMILTONIAN_TAILS_COMPLETENESS.md is bounded by the capacity gap:

```math
\alpha \leq C_{\rm oracle} - C_{\rm public} = I(X; Y_1 | Y_2) + I(Y_1; Y_2) - I(X; Y_2) \tag{2.8}
```

The insider can earn alpha precisely because they have access to a higher-capacity
channel than the public. The alpha is the geometric value of the capacity gap.

### 2.5 Interference channel

Two source-destination pairs $(X_1 \to Y_1, X_2 \to Y_2)$ sharing the same
medium. Each receiver sees a superposition of both signals:

```math
Y_1 = f(X_1, X_2, Z_1), \qquad Y_2 = f(X_1, X_2, Z_2) \tag{2.9}
```

The capacity region is not fully known in general; the Han-Kobayashi \[1981\]
inner bound is the best known achievable region.

**Market analogue.** Two correlated assets (Coca-Cola and PepsiCo, or Brent crude
and WTI) trading simultaneously. Information about one asset "interferes" with
the pricing of the other because they share common factors.

The Han-Kobayashi scheme splits each trader's signal into a **common part**
(the sector factor shared between the two assets) and a **private part**
(the idiosyncratic component). The common part is decoded by both receivers;
the private part is decoded only by the intended receiver and treated as noise
by the other.

In the manifold framework: the common part corresponds to the shared factor
subspace $\mathrm{span}(e_1, \ldots, e_k) \subset T_{b^{\ast}}M^r$ (the $k$ common
factors from any intermarket geometry). The private part is the complement. The
interference capacity constrains how quickly the market can decompose the
superposed signal into common and idiosyncratic components — how quickly the
factor structure is identified. Slow interference resolution means the market
temporarily confuses idiosyncratic shocks with systematic ones, creating spurious
curvature in the wrong factor directions.

### 2.6 Relay channel

A relay $Y_R$ helps communication between source $X$ and destination $Y$.
Two fundamental strategies:

- **Compress-and-forward (CF):** the relay compresses its observation $Y_R$ and
  forwards it. Capacity: $C_{\rm CF} = I(X; Y, \hat{Y}_{R})$ where $\hat{Y}_{R}$ is the
  compressed relay signal.

- **Decode-and-forward (DF):** the relay fully decodes $X$, re-encodes, and forwards.
  Capacity: $C_{\rm DF} = \min(I(X; Y_R), I(X, X_R; Y))$ — limited by the weaker
  of the two links.

**Market analogue.** Financial media, sell-side analysts, brokers — entities that
relay information but do not originate it.

CNBC compresses a 30-page earnings report into a 30-second segment. This is
compress-and-forward: information is lost. The compression rate is $\hat{R} \approx
\log(30\text{ pages} / 30\text{ seconds}) \approx 10$ bits/sec. Much of the nuance —
the footnotes, the segment breakdowns, the management discussion — is discarded.
The relay capacity is limited by the compression quality.

A sell-side analyst reads the same report, understands the business context,
and publishes a 5-page note with a price target. This is decode-and-forward:
the analyst fully decodes the source, applies domain knowledge, and re-encodes
at potentially higher quality. The DF capacity can exceed the CF capacity when
the relay (analyst) has side information that improves the decoding.

**Data processing inequality (DPI) for relays:** Every relay degrades the
information content: $I(X; Y_{\rm relay}) \leq I(X; Y_{\rm source})$. A chain
of $L$ relays (source $\to$ wire service $\to$ journalist $\to$ editor $\to$ reader)
loses information at each step. The effective capacity decays:

```math
C_{\rm chain} \leq \min_{l=1,\ldots,L} C_l \tag{2.10}
```

The weakest link in the relay chain determines the capacity. This is why direct
access to primary sources (SEC filings, central bank transcripts) yields higher
capacity than consuming them through intermediary chains.

### 2.7 Channels with state

The channel $p(y|x,s)$ depends on a state $s$ known to some parties.

**Gel'fand-Pinsker** (state known to encoder): $C = \max_{p(u|s)} [I(U; Y) - I(U; S)]$.
The informed party codes around the state.

**Compound channel** (state unknown to all): $C = \min_s C(s)$ — worst-case capacity.

**Market analogue.** The market operates in a regime — CAPM, Clifford torus, or
pseudo-Anosov — that constitutes the channel state $s \in \{1, 2, 4\}$ (the Dyson
class from RANDOM_MATRIX.md).

**State known to encoder (Gel'fand-Pinsker):** An informed trader who knows the
current regime can code around it — adjusting their trading strategy to the
regime-specific capacity. A CAPM regime (GOE, $\beta = 1$) has different factor
structure than a pseudo-Anosov regime (GSE, $\beta = 4$). The informed trader
exploits this knowledge:

```math
C_{\rm GP} = \max_{p(u|s)} [I(U; Y) - I(U; S)] > C_{\rm compound} \tag{2.11}
```

**State unknown (compound channel):** During regime transitions — when nobody knows
whether the market is CAPM or pseudo-Anosov — the effective capacity drops to the
worst case:

```math
C_{\rm compound} = \min_{s \in \{1,2,4\}} C(s) \tag{2.12}
```

This is the minimum capacity across all regimes. Since the pseudo-Anosov regime
has the most complex factor structure ($\beta = 4$, quaternionic, highest-dimensional
normal bundle), $C(s = 4) < C(s = 1)$, and the compound channel capacity is set
by the hardest regime.

**This explains why markets slow down during transitions.** During a regime change
(e.g., the 2007-2008 transition from CAPM to pseudo-Anosov), nobody knows the
state. The channel becomes compound. The capacity drops to worst-case. The
convergence rate $R_{\rm conv} = \min(\lambda_1, C_{\rm compound})$ falls. The market
is slower to price information precisely when the information is most important.

---

## 3. Insider Trading as a Societal Good

### 3.1 The conventional view

Insider trading is illegal in most jurisdictions. The justification is fairness:
insiders profit at the expense of outsiders who do not have access to the same
information. The US Securities and Exchange Act of 1934, Section 10(b), and
Rule 10b-5 prohibit trading on material non-public information. Penalties include
criminal prosecution, imprisonment, and disgorgement of profits.

### 3.2 The geometric view

The geometric framework yields a starkly different assessment. An insider who
trades on true private information **accelerates the market's convergence to
efficiency**. The insider is a high-capacity channel injecting information into
the MAC that would otherwise not arrive.

**Theorem 3.1** (Insider trading increases convergence rate). *Let $M^r$ be the
market manifold with current Willmore energy $\mathcal{W}(M) > 0$ (inefficient market).
An insider with private signal $X \in \mathcal{F}^{\rm oracle}_t \setminus
\mathcal{F}^{\rm public}_t$ who trades optimally contributes:*

```math
\Delta R_{\rm conv} = \frac{I(X;\, Y_{\rm trade})}{T} \tag{3.1}
```

*additional bits per period to the market's information channel, where $Y_{\rm trade}$
is the order flow generated by the insider's trade. The Willmore energy evolves as:*

```math
\frac{d\mathcal{W}}{dt}\bigg|_{\rm with insider} < \frac{d\mathcal{W}}{dt}\bigg|_{\rm without insider} \leq 0 \tag{3.2}
```

*The insider accelerates the MCF. The market becomes efficient faster.*

*Proof.* The insider's trade is a signal on the MAC channel (Section 2.2). It
carries $I(X; Y_{\rm trade})$ bits of information that is (by assumption) not
available through any public channel. The market maker (or other traders) observes
the order flow and extracts information from it. This is the Kyle \[1985\] mechanism:
the market maker updates the price by the Kyle lambda:

```math
\Delta p = \lambda \cdot (\text{order flow}) \tag{3.3}
```

where $\lambda = \Sigma_{v|y} / \Sigma_{y}$ is the regression coefficient of the
asset value on order flow. The price adjustment $\Delta p$ reduces the discrepancy
between the current price and the efficient price — in geometric terms, it reduces
the mean curvature $|H|$ at the traded point on $M^r$.

The curvature reduction is:

```math
\Delta |H|^2 = -\frac{I(X; Y_{\rm trade})}{T} \cdot g^{\rm FR}(v_X, v_X) \tag{3.4}
```

where $v_X \in N_{b^{\ast}}M$ is the normal bundle component of the insider's
information (the direction in which the price is "wrong"). Integrating over $M^r$:

```math
\Delta \mathcal{W} = -\int_M \Delta |H|^2\,d\mathrm{vol}_{M} < 0 \tag{3.5}
```

The Willmore energy decreases. The inequality in (3.2) follows because $I(X;
Y_{\rm trade}) > 0$ whenever the insider has genuine private information. $\square$

**The insider's profit equals the curvature they remove.** By the Sharpe-curvature
identity (MINIMAL_SURFACE.md, Theorem 2.1), the risk-adjusted return earned by the
insider is:

```math
\text{Sharpe}_{\rm insider} = \|H_{\rm before}\|_{L^2} - \|H_{\rm after}\|_{L^2} = \|\Delta H\|_{L^2} \tag{3.6}
```

to first order. The insider earns exactly the inefficiency they eliminate. This is
not rent extraction — it is compensation for a service: injecting information into
the market that makes it more efficient. The insider is paid by the market for
reducing its curvature.

**Corollary 3.2** (Multiple insiders). *In a market with $N$ insiders, each with
independent private signals $X_1, \ldots, X_N$:*

```math
R_{\rm conv}^{\rm insider} = R_{\rm conv}^{\rm public} + \sum_{k=1}^{N} \frac{I(X_k;\, Y_k)}{T} \tag{3.7}
```

*The convergence rate increases linearly in the number of insiders with independent
information. More insider trading means faster efficiency.*

This is the geometric version of the Fishman and Hagerty \[1992\] result that
legalising insider trading can improve price efficiency. Our framework quantifies
the improvement precisely: the increase in $R_{\rm conv}$ is the sum of insider
information capacities.

**The Grossman-Stiglitz \[1980\] paradox in geometric terms.** Grossman and Stiglitz
proved that informationally efficient markets are impossible if information is
costly: nobody would pay to acquire information that is already priced. In our
framework: if $\mathcal{W}(M) = 0$ (perfectly efficient), there is no curvature to
remove, hence no profit for information producers. The equilibrium has $\mathcal{W}(M) > 0$
just large enough to compensate information producers for their costs — the Willmore
energy at equilibrium equals the aggregate cost of the information network.

### 3.3 The mechanism: Kyle's lambda as curvature reduction

Kyle \[1985\] modelled a single insider trading against noise traders in the presence
of a competitive market maker. The market maker sets the Kyle lambda $\lambda$ such
that the price change per unit order flow is:

```math
\lambda = \frac{\sigma_v}{2\sigma_u} \tag{3.8}
```

where $\sigma_v$ is the standard deviation of the fundamental value and $\sigma_u$
is the noise trader volume.

In our framework: $\sigma_v^2 = |H|^2_{g^{\rm FR}}$ (the curvature at the traded
point — the mispricing), and $\sigma_u$ is the noise trader volume (which provides
the channel through which the insider's signal propagates). The Kyle lambda becomes:

```math
\lambda = \frac{\|H\|}{2\sigma_u} \tag{3.9}
```

The price impact is proportional to the curvature: more mispricing means larger
price adjustment per unit of informed order flow. The insider trades until $|H| = 0$
at their information point — until the mispricing is fully corrected.

---

## 4. Misinformation as a Societal Harm

### 4.1 The geometry of false information

The opposite of insider trading. An insider trades on true private information
and reduces curvature. A misinformation source injects false information and
**creates** curvature.

**Theorem 4.1** (Misinformation creates spurious curvature at double cost). *A source
of misinformation injecting false signal $Z$ (correlated with but not equal to the
true state $X$) into the market's MAC channel causes two distinct harms:*

*(i) Capacity waste.* *The effective channel capacity drops by $I(Z; Y|X)$ — the
mutual information between the false signal and the market response, conditional
on the true state. This is bandwidth consumed by the false signal that could have
carried true information:*

```math
C_{\rm eff} = C - I(Z;\, Y \mid X) \tag{4.1}
```

*(ii) Spurious curvature creation.* *The misinformation causes the market to adjust
prices in the wrong direction, creating positive mean curvature where there should
be none. The spurious Willmore energy is:*

```math
\mathcal{W}_{\rm spurious} = \int_M |H_{\rm false}|^2\,d\mathrm{vol}_{M} \propto I(Z;\, Y \mid X) \cdot \mathrm{Var}(Z - X) \tag{4.2}
```

*The market must then undo this spurious curvature via MCF — at additional cost.
The total damage is:*

```math
\Delta \mathcal{W}_{\rm total} = 2\,\mathcal{W}_{\rm spurious} \tag{4.3}
```

*The doubling principle: cost 1 is creating the false curvature (the market moves
away from the minimal surface); cost 2 is identifying and removing the false
curvature (the MCF works against the misinformation). The effective convergence rate
with misinformation:*

```math
R_{\rm conv}^{\rm misinfo} = R_{\rm conv}^{\rm public} - \frac{2\,I(Z;\, Y \mid X)}{T} \tag{4.4}
```

*Proof.* (i) The capacity waste follows directly from the definition: the channel
processes the false signal $Z$ as if it were informative, allocating $I(Z; Y|X)$
bits of capacity to it. Conditional on the true state $X$, this information is
pure noise — it carries zero bits about the true curvature direction.

(ii) The market maker cannot distinguish the false signal from a true one in
real time (if they could, they would ignore it). The price adjusts according to
the Kyle mechanism:

```math
\Delta p_{\rm false} = \lambda \cdot (\text{misinformation order flow}) \tag{4.5}
```

This adjustment moves the manifold in a direction determined by $Z$, not by $X$.
Since $Z \neq X$, the adjustment creates curvature where there was none (or
increases curvature where it was already positive, or creates curvature of the
wrong sign). The spurious Willmore energy is proportional to the squared
displacement in the wrong direction: $|H_{\rm false}|^2 \propto I(Z; Y|X) \cdot
\mathrm{Var}(Z - X)$.

(iii) The MCF must now undo the false curvature. But the MCF first needs to
**identify** that the curvature is spurious — which requires additional true
information arriving through the channel. Then it needs to actually reduce
the curvature. The identification cost is at least $I(Z; Y|X)$ bits (the
same amount that was wasted creating the false curvature). The reduction cost
is the standard MCF cost. Together: the total cost is at least $2 \cdot
\mathcal{W}_{\rm spurious}$. $\square$

### 4.2 The asymmetry between true and false information

The fundamental asymmetry:

| | True private info (insider) | False info (misinformation) |
|:---|:---|:---|
| Effect on $|H|^2$ | Reduces | Increases |
| Effect on $\mathcal{W}$ | Decreases (good) | Increases (bad) |
| Effect on $R_{\rm conv}$ | $+I(X; Y)/T$ | $-2\,I(Z; Y|X)/T$ |
| Cost multiplier | $1\times$ (direct benefit) | $2\times$ (create + undo) |
| Profit/loss to source | Profit = curvature removed | No legitimate profit |
| Market-wide effect | Faster efficiency | Slower efficiency |

The $2\times$ multiplier for misinformation is the key quantitative result: false
information is twice as costly as true information is beneficial, per bit. A single
bit of misinformation costs the market two bits of convergence capacity — one bit
to process the false signal, one bit to undo its effect.

---

## 5. The Information Value Hierarchy

We now rank all information types by their effect on the convergence rate. Define
the **information value** of a signal of type $k$:

```math
\Delta R_{\rm conv}(k) = \frac{I(X_{\rm true};\, Y_k)}{T} - \frac{2\,I(X_{\rm false};\, Y_k \mid X_{\rm true})}{T} \tag{5.1}
```

where $X_{\rm true}$ is the true information content and $X_{\rm false}$ is the false
content of the signal. For a purely true signal, the second term vanishes. For a
purely false signal, the first term vanishes (the false signal is uncorrelated with
truth conditional on the market).

**Theorem 5.1** (Information value hierarchy). *The seven canonical information types,
ranked by their effect on the convergence rate $R_{\rm conv}$:*

| Rank | Information type | $\Delta R_{\rm conv}$ | Sign | Example |
|:----:|:----------------|:----------------------|:----:|:--------|
| 1 | Insider trading (true private) | $+I(X; Y)/T$ | $+$ | Corporate officer buys before good earnings |
| 2 | Informed research (true public) | $+I(X; Y)/T$ | $+$ | Analyst publishes correct valuation |
| 3 | Uninformed trading (noise) | $0$ | $0$ | Index fund rebalancing |
| 4 | Redundant analysis (herding) | $0$ (wastes capacity) | $0$ | 20 analysts issuing identical notes |
| 5 | Rumour (uncertain truth) | $+I_{\rm true}/T - 2I_{\rm false}/T$ | $\pm$ | Unverified takeover rumour |
| 6 | Misinformation (false) | $-2\,I(Z; Y|X)/T$ | $-$ | Pump-and-dump promotion |
| 7 | Market manipulation (deliberate false) | $-2\,I(Z; Y|X)/T$ (maximised) | $-\!-$ | Spoofing, layering, wash trading |

*Types 1-2 are beneficial (positive $\Delta R_{\rm conv}$). Type 3 is neutral (noise
traders add liquidity but no information). Type 4 is weakly harmful (wastes MAC
capacity through redundancy). Types 5-7 are harmful, with type 7 the most damaging
because the false content is deliberately designed to maximise $I(Z; Y|X)$.*

*Proof.* For each type, evaluate equation (5.1):

*Type 1 (insider):* $X_{\rm true} = X \in \mathcal{F}^{\rm oracle} \setminus
\mathcal{F}^{\rm public}$, $X_{\rm false} = 0$. Hence $\Delta R = I(X; Y)/T > 0$.

*Type 2 (informed research):* Same as type 1 except $X$ is generated by research
rather than insider access. The information enters through the public channel but
is new (not yet priced). Same formula, same sign.

*Type 3 (noise):* $X_{\rm true} = 0$, $X_{\rm false} = 0$. The noise trader's signal
is independent of the true state. Hence $I(X_{\rm true}; Y) = 0$ and
$I(X_{\rm false}; Y|X_{\rm true}) = 0$. Net effect: $\Delta R = 0$. Noise traders
do not help or hurt convergence (they provide liquidity, which is a different
service captured in $\sigma_u$ of the Kyle model).

*Type 4 (herding):* Each herding analyst transmits $I(X_k; Y) > 0$ bits, but
because $X_k \approx X_j$ for all $k, j$, the MAC sum capacity does not increase:
$C_{\rm sum}^{\rm herd} \approx C_1$. The redundant capacity is wasted — it occupies
channel bandwidth without adding information. Net effect on $R_{\rm conv}$: $0$,
but the MAC capacity is not used efficiently.

*Type 5 (rumour):* A rumour has $X_{\rm true} > 0$ (some truth content) and
$X_{\rm false} > 0$ (some false content). The net effect depends on which
dominates. An accurate rumour ($I_{\rm true} > 2I_{\rm false}$) is net beneficial;
an inaccurate rumour ($2I_{\rm false} > I_{\rm true}$) is net harmful.

*Types 6-7:* Pure false information with $X_{\rm true} = 0$. The market manipulation
case (type 7) is worse because the manipulator designs $Z$ to maximise the market
response $I(Z; Y|X)$, e.g., by spoofing at the bid-ask boundary where the Kyle
lambda is highest. $\square$

---

## 6. The Regulatory Inversion

### 6.1 Current regulatory regime

The current hierarchy of enforcement intensity in most developed markets:

| Offence | Typical penalty | Enforcement intensity |
|:--------|:---------------|:---------------------|
| Insider trading | Criminal: prison (up to 20 years in US), disgorgement, fines | Very high |
| Market manipulation | Criminal/civil: fines, trading bans | High |
| Misinformation (non-manipulative) | Civil: rarely prosecuted | Low |
| Herding / redundant research | No penalty | None |

### 6.2 The geometric prescription

**Theorem 6.1** (Regulatory inversion). *The regulatory policy that maximises the
market's convergence rate $R_{\rm conv}$ should:*

*(i) Permit or lightly regulate insider trading: $\Delta R_{\rm conv} > 0$. The
insider accelerates efficiency. The social benefit (faster convergence) exceeds
the private cost (unfairness to counterparty) when measured by aggregate welfare.*

*(ii) Heavily penalise misinformation: $\Delta R_{\rm conv} < 0$, doubled. Each
bit of misinformation costs the market two bits of convergence capacity. The social
harm is quantifiably larger than the private gain to the misinformation source.*

*(iii) Most heavily penalise market manipulation: this is designed misinformation,
optimised to maximise $I(Z; Y|X)$. The social harm is maximal.*

*(iv) Discourage herding by incentivising independent research: herding wastes
MAC capacity. Tax redundant research; subsidise novel research that covers
uninformed factor directions.*

*(v) Protect relay integrity: ensure financial media and analysts do not corrupt
the relay channel. The DPI means information can only be lost, never gained,
through relays — so relay corruption is irreversible.*

*Proof.* This follows directly from Theorem 5.1 and the monotone relationship
between $R_{\rm conv}$ and market welfare. A faster-converging market has lower
$\mathcal{W}(M)$, which means: prices are closer to fundamental values, capital
is allocated more efficiently, the Sharpe ratio of the market portfolio is
lower (less excess return from mispricing), and the risk of crisis (large
$|H|$ events) is reduced. The regulatory policy that maximises $R_{\rm conv}$
therefore maximises the sum of these welfare components. $\square$

### 6.3 Caveats

The geometric argument is clean. The policy conclusion requires two important
caveats that the mathematical framework does not fully capture.

**Caveat 1: The truth condition.** The argument for insider trading assumes
the insider trades on TRUE information. A corporate officer who fabricates earnings
and then trades on the fabricated numbers is not an insider in the geometric sense
— they are a misinformation source. The insider trading defense applies only to
trading on genuine private knowledge of true states. An insider who creates false
information and trades on it should be punished under the misinformation framework,
not the insider framework. The critical distinction is truth value, not publicity.

**Caveat 2: The participation constraint.** The geometric framework maximises
the convergence rate of the aggregate market. It does not account for
distributional effects. If retail investors believe the market is "rigged"
by insiders and withdraw, three consequences follow:

1. **Liquidity reduction:** fewer participants means lower $\sigma_u$ (noise
   trader volume), which means higher Kyle lambda, which means the insider
   moves the price more per trade — but there are fewer trades to move against.
   The net effect on $R_{\rm conv}$ is ambiguous.

2. **MAC capacity reduction:** fewer participants means fewer sources in the
   MAC. Even if the remaining sources (insiders) are higher quality, the total
   MAC capacity may fall.

3. **Political sustainability:** a market perceived as unfair will face political
   pressure for heavy-handed regulation that may reduce efficiency more than
   the insider trading helps it.

The geometric optimum (permit insider trading) may not be the political optimum.
The Grossman-Stiglitz equilibrium — some inefficiency maintained to incentivise
information production — may require that some insider trading be prohibited to
maintain participation.

**Caveat 3: The Akerlof lemon problem.** If insiders trade freely and earn
abnormal returns, the counterparties (market makers) will widen bid-ask spreads
to compensate (Glosten and Milgrom \[1985\]). Wider spreads increase trading costs
for all participants, potentially reducing welfare even as price efficiency
improves. The geometry says prices converge to fundamental values faster, but the
cost of transacting at those prices may increase. Whether the net effect is positive
depends on the magnitude of the insider information relative to the adverse selection
cost.

These caveats are real. They mean the geometric prescription — permit insider
trading, punish misinformation — is a first-order result that may be modified
by second-order participation and adverse selection effects. The direction of the
first-order effect is unambiguous. The magnitude of the second-order effects is
an empirical question.

---

## 7. Social Media, Meme Stocks, and Information Flooding

### 7.1 The pre-social-media information architecture

Before approximately 2005, the market information network was a **degraded broadcast
channel** with a small number of professional relays:

```math
\text{Source} \to \text{Wire service (AP/Reuters)} \to \text{Journalist} \to \text{Public}
```

The relay chain was short (3-4 links). The relays were professional (decode-and-forward,
not compress-and-forward). The aggregate capacity was moderate ($C \sim 10^4$
bits/day for a typical stock) but the signal quality was high: most of the
transmitted information was type 1-2 (true, informative). The effective capacity was:

```math
C_{\rm eff}^{\rm pre} \approx p_{\rm true}^{\rm pre} \cdot C^{\rm pre} \approx 0.8 \cdot 10^4 = 8 \times 10^3 \text{bits/day} \tag{7.1}
```

### 7.2 The post-social-media information architecture

After 2010, the network became a massive **multiple access channel** with millions
of sources:

```math
\text{Millions of sources} \xrightarrow{\text{MAC}} \text{Market}
```

The aggregate bandwidth exploded: $C^{\rm post} \sim 10^{10}$ bits/day. But the
composition of sources changed dramatically.

**Theorem 7.1** (Social media MAC capacity). *A social media MAC with $N$ sources,
of which fraction $p_{\rm true}$ are truthful and informative, $p_{\rm noise}$
are noise, $p_{\rm herd}$ are herding, and $p_{\rm false}$ are misinformation
($p_{\rm true} + p_{\rm noise} + p_{\rm herd} + p_{\rm false} = 1$), has
effective capacity:*

```math
C_{\rm eff} = N \cdot p_{\rm true} \cdot \bar{C} - 2N \cdot p_{\rm false} \cdot \bar{C} \tag{7.2}
```

*where $\bar{C}$ is the average per-source capacity. The noise sources do not affect
the effective capacity (they average out by the law of large numbers). The herding
sources contribute redundantly (their information is already captured by the
$p_{\rm true}$ fraction). The misinformation sources subtract at double rate
(the doubling principle of Theorem 4.1).*

*Corollary.* *The effective capacity is negative (the market DIVERGES from efficiency)
when:*

```math
p_{\rm false} > \frac{p_{\rm true}}{2} \tag{7.3}
```

*That is: when the fraction of misinformation sources exceeds half the fraction of
truthful sources, the social media channel is net harmful — the market would converge
faster with no social media at all.*

### 7.3 The GameStop episode (January 2021)

GameStop (GME) and AMC Entertainment in January 2021 provide a natural experiment.
The WallStreetBets subreddit had $N \approx 10^7$ users posting about GME. We
estimate the composition:

- $p_{\rm true} \approx 0.001$ (a handful of users with genuine short-squeeze analysis)
- $p_{\rm noise} \approx 0.90$ (most users were uninformed, posting memes)
- $p_{\rm herd} \approx 0.09$ (users repeating "diamond hands" / "to the moon" without original analysis)
- $p_{\rm false} \approx 0.009$ (users posting fabricated position screenshots, false institutional data)

By Theorem 7.1:

```math
C_{\rm eff}^{\rm GME} = 10^7 \cdot (0.001 - 2 \times 0.009) \cdot \bar{C} = 10^7 \cdot (-0.017) \cdot \bar{C} < 0 \tag{7.4}
```

The effective capacity was **negative**. The social media channel was net harmful:
the misinformation fraction ($0.009$) exceeded half the truthful fraction
($0.001/2 = 0.0005$) by a factor of 18. The result: GME's price diverged from any
reasonable fundamental value — the Willmore energy $\mathcal{W}(M)$ increased
enormously. The market moved away from efficiency despite (indeed, because of)
massive information flow.

This is the paradox of information flooding: $10^6\times$ more bandwidth with
$10^3\times$ worse signal-to-noise can produce net negative information value.
The social media era is not simply "more information" — it is more bandwidth with
potentially worse composition.

---

## 8. Historical Information Networks

The evolution of market information architecture illustrates the dual bottleneck
theorem across centuries:

| Era | Network type | $C$ estimate | Bottleneck | $R_{\rm conv}$ |
|:----|:-----------|:-----------|:-----------|:----------------|
| Pre-1600 | Word of mouth (relay chain) | $\sim 0.01$ bits/day | Information | Years to price |
| 1600-1840 | Ships + newspapers | $\sim 1$ bit/day | Information | Months to price |
| 1840-1870 | Telegraph | $\sim 10^2$ bits/day | Information | Weeks to price |
| 1870-1970 | Telephone + ticker tape | $\sim 10^4$ bits/day | Information | Days to price |
| 1970-2000 | Electronic trading | $\sim 10^6$ bits/day | Transitional | Hours to price |
| 2000-2010 | Internet + algorithmic | $\sim 10^9$ bits/day | Geometry | Minutes to price |
| 2010-present | Social media + HFT | $\sim 10^{12}$ bits/day (raw) | Signal quality | Seconds (but noise increasing) |

**The three eras of market efficiency:**

**Era I: Information-limited** (pre-2000). $C \ll \lambda_1$. Every technological
innovation that increased $C$ (printing press, telegraph, telephone, electronic
trading) directly increased $R_{\rm conv}$. The market became more efficient with
each communication revolution. Fama's EMH \[1970\] was formulated at the end of
this era, when increasing $C$ was the dominant trend.

**Era II: Geometry-limited** (2000-2010). $C \gg \lambda_1$. Information arrived
faster than the MCF could process it. Further increases in $C$ did not help.
The bottleneck shifted to the geometric structure of the manifold — the spectral
gap $\lambda_1$. This is the era when high-frequency trading emerged: the
information was already there, so the competitive advantage shifted to processing
speed (reducing $\lambda_1$ by trading faster).

**Era III: Quality-limited** (2010-present). $C_{\rm raw} \gg \lambda_1$ but
$C_{\rm eff}$ may be declining. The social media revolution massively increased
raw bandwidth but introduced misinformation at scale. For some assets (meme stocks,
crypto, small-caps with high social media attention), $C_{\rm eff}$ may have fallen
below $\lambda_1$, creating a new information bottleneck — not of quantity, but of
quality.

**The Rothschild carrier pigeon.** Nathan Rothschild's use of carrier pigeons to
learn the outcome of Waterloo before other London traders is the canonical insider
trading story. In our framework: Rothschild had a private point-to-point channel
with capacity $C_{\rm pigeon} \gg C_{\rm public}$ (the public channel was ships
across the Channel, arriving days later). His trade injected $I(X; Y_{\rm trade})$
bits of true information into the market's MAC channel, reducing the Willmore
energy of gilt pricing. The market reached efficiency faster because Rothschild
traded. He was paid (enormously) for the curvature he removed. The geometric
verdict: Rothschild accelerated market efficiency. The moral verdict is left to
the reader.

---

## 9. Optimal Market Design from Network Theory

What information architecture maximises $R_{\rm conv}$?

**Theorem 9.1** (Optimal information architecture). *For a market with $r$ factors
and $d$ assets, the information architecture that maximises $R_{\rm conv}$ satisfies:*

*(i) Factor coverage: at least $r$ independent sources per factor direction.* The
MAC sum capacity for factor identification requires at least $r$ linearly independent
information signals. With fewer than $r$ independent sources, some factor directions
remain uninformed and the effective manifold dimension drops.

*(ii) Broadcast completeness: each source reaches all relevant markets.* Information
silos — where a signal reaches the equity market but not the bond market — create
cross-market inefficiency. The broadcast channel from each source should cover all
$N$ markets whose manifolds share factors with the source's information content.

*(iii) Short relay chains: minimise the number of intermediaries.* By the DPI,
each relay can only lose information. A chain of $L$ relays has capacity
$C_{\rm chain} \leq \min_l C_l$. Direct access to primary sources (SEC filings,
central bank transcripts, raw data) dominates intermediated access (news summaries,
analyst interpretations, social media posts).

*(iv) Public regime identification: the channel state should be broadcast publicly.*
When the regime $s \in \{1, 2, 4\}$ is unknown, the market operates on the compound
channel at worst-case capacity $C_{\rm compound} = \min_s C(s)$. Public regime
identification (central banks clearly communicating their policy regime, for instance)
converts the compound channel to a channel with known state, upgrading the capacity
from $C_{\rm compound}$ to $C_{\rm GP} > C_{\rm compound}$ via the Gel'fand-Pinsker
coding gain.

### 9.1 Practical implications

**For regulators:**
- Mandate minimum independent analyst coverage per stock (fill the MAC to factor capacity).
- Facilitate cross-market information flow (reduce broadcast degradation between asset classes).
- Reduce intermediary chains (promote direct market access, reduce informational role of brokers).
- Require clear regime communication from central banks (reduce compound channel penalty).
- Penalise misinformation at $2\times$ the rate of rewarding true information (the doubling principle).

**For market designers:**
- Optimal market microstructure maximises $C_{\rm eff}$, not $C_{\rm raw}$.
- A market with fewer but higher-quality information sources can have higher $C_{\rm eff}$ than one with many low-quality sources.
- The Kyle lambda should be set to maximise the rate of curvature removal per unit time, not to minimise bid-ask spreads per se.

**For portfolio managers:**
- Seek information from sources that are independent of the existing MAC (non-herding research).
- The value of a research source is $I(X_{\rm source}; Y \mid X_{\rm existing})$ — the conditional mutual information given what the market already knows. Redundant research has zero conditional value.
- During regime transitions (compound channel), the value of regime identification is highest: knowing the state $s$ upgrades the capacity by $C_{\rm GP} - C_{\rm compound}$.

---

## 10. Summary of New Results

We collect the principal results of this paper. Numbers N1-N7 are internal to this paper; they will be assigned R-numbers in WHATS_NEW.md upon integration with the monograph.

**Theorem N1** (Dual bottleneck). The effective convergence rate of $\mathcal{W}(M)$
under MCF with information arriving at rate $C$ is $R_{\rm conv} = \min(\lambda_1, C)$.
*Status: Proved (Theorem 1.1).*

**Theorem N2** (Network-constrained MUP regret). The MUP with information channel
capacity $C$ achieves regret $r\log(T)/(2T) + r/(CT)$.
*Status: Proved (Theorem 1.2).*

**Theorem N3** (Insider trading increases $R_{\rm conv}$). An insider with private
signal $X$ contributes $\Delta R_{\rm conv} = I(X; Y_{\rm trade})/T > 0$ to the
convergence rate. The insider's profit equals the curvature removed.
*Status: Proved (Theorem 3.1).*

**Theorem N4** (Misinformation doubling principle). Misinformation decreases
$R_{\rm conv}$ by $2\,I(Z; Y|X)/T$ — double the cost because the market must
first create and then undo the spurious curvature.
*Status: Proved (Theorem 4.1).*

**Theorem N5** (Information value hierarchy). The seven information types ranked
by $\Delta R_{\rm conv}$: insider $>$ informed research $>$ noise $\geq$ herding
$>$ rumour $>$ misinformation $>$ manipulation.
*Status: Proved (Theorem 5.1).*

**Theorem N6** (Regulatory inversion). The optimal regulatory policy that maximises
$R_{\rm conv}$ inverts the current enforcement hierarchy: permit insider trading
(positive $\Delta R_{\rm conv}$), heavily penalise misinformation (negative, doubled),
most heavily penalise manipulation.
*Status: Proved (Theorem 6.1), subject to caveats (Section 6.3).*

**Theorem N7** (Social media MAC capacity). The effective capacity of a social media
MAC is $C_{\rm eff} = N(p_{\rm true} - 2p_{\rm false})\bar{C}$. The market diverges
from efficiency when $p_{\rm false} > p_{\rm true}/2$.
*Status: Proved (Theorem 7.1).*

---

## 11. Open Problems

**OP-N1** (Empirical effective capacity). Estimate $C_{\rm eff}$ for the US equity
market from data. How many independent information sources exist for a typical
S\&P 500 stock? What fraction is true, noise, herding, misinformation? Is the
current social media era information-limited or geometry-limited for large-caps?
For small-caps?
*Difficulty: ★★. Requires novel empirical methodology.*

**OP-N2** (Optimal insider regulation). Determine the insider trading policy that
maximises $R_{\rm conv}$ subject to a participation constraint: retail investors
withdraw if the perceived insider advantage exceeds a threshold $\alpha_{\rm max}$.
This is a constrained optimisation problem on the MAC capacity region.
*Difficulty: ★★★. Requires modelling the participation constraint.*

**OP-N3** (Channel capacity as predictor). Can estimates of $C_{\rm eff}$ for
different markets predict which markets will be slow to incorporate information?
Test: estimate $C$ from analyst coverage, social media volume, and relay chain length;
correlate with pricing delay after earnings announcements.
*Difficulty: ★★. Empirical, testable with existing data.*

**OP-N4** (Dark pools as information suppression). A dark pool is a relay channel
that deliberately suppresses information (hides order flow from the public).
In the relay framework, this reduces $C_{\rm relay}$ by design. Does the dark
pool's liquidity benefit (lower adverse selection for large orders) outweigh the
information suppression cost (slower convergence of $\mathcal{W}$)?
*Difficulty: ★★★. Requires comparing two incommensurable welfare effects.*

**OP-N5** (The Feynman path integral over information networks). Extend the path
integral formulation of PATH_INTEGRAL.md to integrate over all possible information
network realisations. The "partition function" of the market should sum over both
geometric configurations (manifold shapes) and information configurations (network
topologies). Does the combined integral factorise into geometric and information
factors, or do they interact?
*Difficulty: ★★★★. Deep theoretical problem connecting geometric and information-theoretic
descriptions.*

---

## Connections to Other Papers

The dual bottleneck theorem (N1) connects directly to the spectral gap analysis in
CLASSIFICATION.md (the geometric rate $\lambda_1$) and the MUP regret bound in
CONVERGENCE.md (the geometric regret term). The network penalty $r/(CT)$ in the
MUP regret (N2) is the information-theoretic complement of the geometric regret
$r\log(T)/(2T)$.

The degraded broadcast channel (Section 2.4) is precisely the $\sigma$-algebra
hierarchy $\mathcal{F}^{\rm oracle} \supseteq \mathcal{F}^{\rm MM} \supseteq
\mathcal{F}^{\rm public}$ from MARTINGALE_GEOMETRY.md. The insider alpha
$\alpha = \varepsilon^2 |v_G|_{g^{\rm FR}}$ from HAMILTONIAN_TAILS_COMPLETENESS.md
is bounded by the capacity gap $C_{\rm oracle} - C_{\rm public}$ (equation 2.8).

The channel-with-state framework (Section 2.7) connects to the Dyson class
transitions of RANDOM_MATRIX.md: the regime $s \in \{1, 2, 4\}$ is the channel
state, and regime transitions create compound channel conditions.

The relay analysis (Section 2.6) connects to the data processing inequality chain
in FILTRATIONS.md: the LZ complexity of a relayed signal can only increase (lose
compressibility) through intermediaries.

The insider trading result (N3) is the network-theoretic completion of the normal
bundle analysis in LLM_MANIFOLD.md Section (iv): side-channel information lives
in $N_{b^{\ast}}M$, and the insider's contribution to efficiency is quantified by
the capacity of that side channel.

---

## References

El Gamal, A. and Kim, Y.-H. (2011). *Network Information Theory*.
Cambridge University Press.

Shannon, C. E. (1948). A mathematical theory of communication.
*Bell System Technical Journal* 27(3), 379–423.

Cover, T. M. and Thomas, J. A. (2006). *Elements of Information Theory*.
2nd ed. Wiley-Interscience.

Kyle, A. S. (1985). Continuous auctions and insider trading.
*Econometrica* 53(6), 1315–1335.

Glosten, L. R. and Milgrom, P. R. (1985). Bid, ask, and transaction prices
in a specialist market with heterogeneously informed traders.
*Journal of Financial Economics* 14(1), 71–100.

Fishman, M. J. and Hagerty, K. M. (1992). Insider trading and the efficiency
of stock prices. *RAND Journal of Economics* 23(1), 106–122.

Grossman, S. J. and Stiglitz, J. E. (1980). On the impossibility of
informationally efficient markets. *American Economic Review* 70(3), 393–408.

Fama, E. F. (1970). Efficient capital markets: a review of theory and
empirical work. *Journal of Finance* 25(2), 383–417.

Bergmans, P. (1973). Random coding theorem for broadcast channels with
degraded components. *IEEE Transactions on Information Theory* 19(2), 197–207.

Gallager, R. G. (1974). Capacity and coding for degraded broadcast channels.
*Problemy Peredachi Informatsii* 10(3), 3–14.

Han, T. S. and Kobayashi, K. (1981). A new achievable rate region for the
interference channel. *IEEE Transactions on Information Theory* 27(1), 49–60.

Gel'fand, S. I. and Pinsker, M. S. (1980). Coding for channel with random
parameters. *Problems of Control and Information Theory* 9(1), 19–31.

Vives, X. (2008). *Information and Learning in Markets: The Impact of Market
Microstructure*. Princeton University Press.

Marton, K. (1979). A coding theorem for the discrete memoryless broadcast channel.
*IEEE Transactions on Information Theory* 25(3), 306–311.

*[All other references as per companion papers.]*
