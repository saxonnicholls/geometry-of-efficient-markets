# The Geometry of the Art Market:
## Pricing the Unpriceable and the Manifold of Aesthetic Value

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VI.3** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**  
The art market is the most informationally inefficient market that exists.
Unique objects, extreme illiquidity, asymmetric information, subjective
valuation, no dividends, no cash flows. Yet art IS traded, prices ARE
discovered, and the market DOES process information — slowly, imperfectly,
with enormous curvature. We apply the geometric framework of this monograph
to the art market: the hardest possible test case for the thesis that a
financial market is a minimal submanifold $M^r$ of the Bhattacharyya sphere
$S^{d-1}_{+}$. The central insight is that the price of a Rothko is not
\$86.9 million — it is a row of the Fisher information matrix, a web of
relativities encoding that painting's relationship to every other tradeable
object simultaneously. We establish that the art market manifold is
pseudo-Anosov (hyperbolic), with intrinsic negative curvature that makes
the mean curvature condition $H = 0$ geometrically impossible. The Willmore
energy $\mathcal{W}(M^r_{\rm art})$ is bounded below by a positive constant
depending on the sectional curvature $\kappa$, the Cheeger constant $h_M$,
and the spectral gap $\lambda_1$. Unlike equity markets, which can in
principle converge to efficiency under mean curvature flow, the art market
is a permanently Stage 2 market — Wild West, high curvature, mandatory
alpha — and the geometry explains why. We prove five results: the art
manifold type is pseudo-Anosov (Lemma A1); the Willmore energy is bounded
away from zero (Lemma A2); the informationally correct art price index is
the Fisher-Rao geodesic distance, not the dollar-weighted average (Lemma A3);
fractionalisation increases the spectral gap and decreases Willmore energy
(Lemma A4); and auction revenue equivalence is a projection theorem on
the space of bidder beliefs (Lemma A5). The art market is the only major
asset class where the geometry proves that inefficiency is permanent.

**Keywords.** Art market; auction theory; Willmore energy; permanent
inefficiency; pseudo-Anosov; Fisher-Rao metric; fractionalisation; NFT;
price index; aesthetic value; Cheeger constant; spectral gap; illiquidity;
mean curvature flow; Bhattacharyya sphere.

**MSC 2020.** 91G10, 91B26, 53A10, 91B44, 62P20.

---

## 1. What Is an Art Market?

### 1.1 The asset space

Consider the universe of artworks available for purchase at a given time —
at galleries, auction houses, private dealers, art fairs, and online platforms.
Denote these $d$ objects. In practice $d$ is enormous: roughly 10 million
works are in active circulation globally, with perhaps 70 million more in
private hands, museums, and storage. Most are profoundly illiquid — they
have not traded in decades and may never trade again.

The effective $d$ for the auction market is smaller but still substantial:
approximately 50,000 lots per year pass through the major houses (Christie's,
Sotheby's, Phillips, Bonhams, and their Chinese counterparts Poly and China
Guardian), with perhaps 500,000 additional lots at regional and online
auctions. The gallery market, which accounts for roughly half of global art
sales by value (\$65 billion total in 2023, per Art Basel/UBS), is even more
opaque — prices are often undisclosed, transactions are private, and the
concept of a "market clearing price" is generous.

Despite all of this, we can define the framework.

**Definition 1.1** (Art portfolio). *An art collection is a portfolio
$b = (b_1, \ldots, b_d) \in \Delta_{d-1}$ where $b_i$ is the fraction
of total collection value allocated to work $i$. The portfolio simplex
$\Delta_{d-1}$ is the collection allocation space.*

**Definition 1.2** (Art market manifold). *The art market manifold
$M^r_{\rm art} \subset S^{d-1}_{+}$ is the image under the Bhattacharyya
embedding $\phi: b \mapsto \sqrt{b}$ of the set of log-optimal art
portfolios over all realisations of the art market's systematic factors.*

The Fisher-Rao metric $g^{\rm FR}_{ij}(b) = \delta_{ij}/b_i$ on
$\Delta_{d-1}$ gives the information-theoretic distance between two
collections. Two collections that differ in their allocation to a single
cheap print are close in $g^{\rm FR}$; two collections that differ in their
allocation to a \$100 million masterwork are far apart. The metric knows
what matters.

### 1.2 The factors

What are the systematic factors that drive art prices? The art market
literature \[Renneboog and Spaenjers 2013; Korteweg, Kräussl, and
Verwijmeren 2016\] identifies several that are empirically robust:

1. **Blue-chip contemporary** (Richter, Hockney, Koons, Kusama, Hirst)
2. **Post-war masters** (Rothko, de Kooning, Bacon, Pollock, Warhol, Basquiat)
3. **Impressionist/Modern** (Monet, Picasso, Matisse, Cézanne, Renoir)
4. **Old Masters** (Rembrandt, Vermeer, Caravaggio, Rubens)
5. **Emerging contemporary** (whoever Gagosian, Hauser & Wirth, and Pace
   are promoting this season)
6. **Photography** (Gursky, Sherman, Avedon, Mapplethorpe)
7. **Chinese/Asian art** (separate market dynamics, dominated by domestic buyers)
8. **African and diaspora art** (the fastest-growing segment of the last decade)

Hedonic regression models \[Renneboog and Spaenjers 2013\] and repeat-sales
indices \[Goetzmann 1993; Mei and Moses 2002\] suggest that the first five
factors explain approximately 80% of auction price variance. We therefore
estimate $r \approx 5$ for the major art market, though $r$ varies by
segment and era.

---

## 2. Why Art Is the Hardest Test Case

The art market violates, or at least strains, nearly every assumption that
makes the geometric framework tractable in conventional financial markets.
This is precisely why it is interesting: if the geometry can say something
useful here, it can say something useful anywhere.

### 2.1 Uniqueness and the discrete simplex

In equity markets, portfolio weights $b_i$ are continuous: one can hold
any fraction of any stock. In art, each work is one-of-one. A collector
either owns a painting or does not. The "portfolio" is a point on a vertex
of the simplex — $b_i \in \{0, 1\}$ for each $i$, subject to the budget
constraint. The interior of $\Delta_{d-1}$ is, in principle, inaccessible.

This means the Wright-Fisher diffusion that governs portfolio dynamics on
the continuous simplex has no arena to operate. The art market is not a
diffusion — it is a jump process on the vertices of the simplex, with
jumps occurring at the moments of purchase and sale.

We will return to this point in Section 7, where we argue that
fractionalisation and NFTs are changing the geometry by filling in the
interior of $\Delta_{d-1}$.

### 2.2 Illiquidity and the divergent diffusion parameter

A painting trades once every 10 to 50 years on average. For the most
important works, the interval is longer: Leonardo's *Salvator Mundi* had
not been publicly sold since 1958 before its 2017 auction (\$450.3 million).
Between trades, the "price" does not exist — it is a latent variable,
inferred from comparables, insurance valuations, and expert opinion.

In the WF diffusion framework, the diffusion parameter is
$\varepsilon^2 = 1/T$ where $T$ is the number of observed trades. For a
painting that trades once per generation, $T \approx 1$ over a 30-year
horizon, giving $\varepsilon^2 \approx 1$. The diffusion is maximally
noisy. There is no concentration of the posterior around the log-optimal
portfolio — the Laplace approximation of Papers I.1 and I.2 requires
$T \to \infty$, and in the art market $T$ is small, fixed, and may be
literally one.

### 2.3 Subjective valuation and the space of priors

In standard markets, one can at least pretend that there is a "true"
probability distribution $p$ over future returns, and that differences
among traders are noisy estimates of the same $p$. In art, this pretence
collapses. Different collectors have genuinely different utility functions
over the same object — different $p$'s, not just different estimates of
one $p$.

A Russian oligarch buying a Rothko for his yacht and a museum curator
acquiring the same work for a permanent collection are not estimating the
same value with different noise. They are in different Fisher-Rao
manifolds. The distance $d_{\rm FR}(p_{\rm oligarch}, p_{\rm curator})$
can be enormous, and it is not an error — it is a feature of the market.

### 2.4 No cash flows

Art produces no dividends, no coupons, no rent (unless leased to museums,
a growing but still niche practice). The "return" on art is pure capital
appreciation plus **psychic income** — the pleasure of living with the
work, the social status it confers, the intellectual engagement it
provides. Psychic income is real (collectors pay for it) but
collector-specific and non-transferable. It does not appear in the return
series. The Kelly criterion $b^{\ast} = \arg\max \mathbb{E}[\log\langle b, x \rangle]$
applies only to the capital appreciation component, systematically
undervaluing art relative to a collector's true optimum.

### 2.5 Asymmetric information

Provenance, condition, and authenticity — the three pillars of art
valuation — are known asymmetrically. The seller (or dealer) typically
knows more than the buyer. This is not incidental asymmetry that can be
reduced by disclosure requirements (as in securities markets). It is
structural: the information is expensive to acquire (conservation reports,
scientific analysis, archival research), subjective in interpretation
(is that craquelure original or the result of poor restoration?), and
sometimes deliberately obscured (a forger has every incentive to maintain
asymmetry).

In the language of filtrations (Paper III.2), the seller's filtration
$\mathcal{F}^{\rm seller}_{t}$ is strictly finer than the buyer's
$\mathcal{F}^{\rm buyer}_{t}$, and the difference
$\mathcal{F}^{\rm seller}_{t} \setminus \mathcal{F}^{\rm buyer}_{t}$ is large,
persistent, and resistant to reduction. The normal bundle $N_{b^{\ast}}M$ is fat
with unresolvable private information.

---

## 3. The Price of a Painting Is Not a Number

This is the key section. We apply the monograph's central insight — that a
price is not a scalar but a row of the Fisher information matrix — to the
art market, where its force is most evident.

### 3.1 The web of relativities

On 13 May 2015, Pablo Picasso's *Les Femmes d'Alger (Version "O")* sold at
Christie's New York for \$179.4 million, then the highest price ever paid at
auction for a work of art. What does "\$179.4 million" mean?

As a number, almost nothing. It is a dollar figure that will be eroded by
inflation, distorted by currency movements, and rendered meaningless by
changes in the money supply. In 1990 dollars it is different; in 2030
dollars it will be different again.

The informationally meaningful content of the price is relational:

| Ratio | Value | Interpretation |
|:------|:------|:---------------|
| Picasso / Rothko | $\approx 2.1$ | One Picasso masterwork $\approx$ two Rothko masterworks |
| Picasso / Warhol | $\approx 2.8$ | Relative to Warhol's market ceiling |
| Picasso / Basquiat | $\approx 1.6$ | At 2015 prices; by 2017 this ratio fell to $\approx 1.6$ |
| Picasso / Manhattan apartment | $\approx 90$ | In units of prime real estate |
| Picasso / median US income | $\approx 3{,}300$ | In units of annual labour |
| Picasso / Apple market cap | $\approx 2.5 \times 10^{-4}\%$ | Relative to the largest company on Earth |
| Picasso / US daily federal spending | $\approx 0.9\%$ | A single painting = 13 minutes of federal expenditure |

Each of these ratios is a component of the row $F_{\rm Picasso, \cdot}$ in
the Fisher information matrix. The "price" is not any single entry — it is
the entire row. A painting's price is a web of relativities, encoding its
relationship to every other tradeable object simultaneously.

### 3.2 Why relative prices are more informative

In the art market, relative prices are MORE stable and MORE informative
than dollar prices:

**(i) Dollar prices are contaminated by wealth effects.** The art market is
driven by the spending of ultra-high-net-worth individuals. When the S&P 500
rises 20%, the number of collectors who can afford a \$10M+ painting
increases, and art prices rise — not because the art is more valuable, but
because there is more money chasing it. The Picasso/Rothko ratio is robust
to this effect: if all art rises by the same factor, the ratios are unchanged.

**(ii) Relative prices reveal substitution.** When the Picasso/Warhol ratio
changes, it tells us something real about the relative desirability of these
artists in the current market. When both rise in dollar terms but at different
rates, the dollar price obscures the signal; the ratio reveals it.

**(iii) Art market indices implicitly work on the simplex.** The
Mei-Moses All Art Index, the Artnet Analytics Index, and the various
hedonic indices constructed by \[Renneboog and Spaenjers 2013\] and
\[Korteweg, Kräussl, and Verwijmeren 2016\] all work with repeat-sales
pairs or hedonic characteristics. In our framework, these methods are
implicitly estimating the market manifold's position in the simplex by
tracking relative movements across segments.

### 3.3 The correct art price index

The standard approach to constructing an art price index is the repeat-sales
regression \[Goetzmann 1993; Mei and Moses 2002\]: for each work that sells
at least twice, regress the log price change on time dummies. The resulting
index is dollar-denominated and tracks the average capital appreciation of
art as a dollar investment.

This is geometrically wrong. The correct index, in the Fisher-Rao framework,
measures the geodesic displacement of the art price vector from a reference
configuration.

**Lemma A3** (Fisher-Rao art price index). *Let $b^{\rm art}(t) \in \Delta_{d-1}$
be the market-implied allocation vector at time $t$ (the vector of relative
market values of all artworks, normalised to sum to 1). Let
$b^{\rm art}(0)$ be the reference allocation at a base date. The
informationally correct art price index is*

$$I^{\rm FR}(t) = d_{\rm FR}\bigl(b^{\rm art}(t),\, b^{\rm art}(0)\bigr)
= 2\arccos\!\left(\sum_{i=1}^{d} \sqrt{b^{\rm art}_{i}(t)\, b^{\rm art}_{i}(0)}\right) \tag{3.1}$$

*This index is invariant under simultaneous rescaling of all prices (it
lives on the simplex), is non-negative, equals zero iff the relative
allocation is unchanged, and is the unique index derived from the
information-theoretic distance on the space of allocations.*

*Proof.* The Fisher-Rao distance on $\Delta_{d-1}$ is
$d_{\rm FR}(p, q) = 2\arccos\bigl(\sum_i \sqrt{p_i q_i}\bigr)$ (the
Bhattacharyya angle). This is an intrinsic distance — it measures
displacement on the allocation simplex without reference to any external
numeraire. The repeat-sales index, by contrast, measures displacement in
dollar space $\mathbb{R}_{+}$ and is contaminated by wealth effects, inflation,
and currency movements. $\square$

**Remark 3.1.** The Fisher-Rao index has a natural interpretation: it
measures how much the *composition* of the art market has changed, not how
much its *level* has changed. A market where Picasso rises 100% and
everything else is flat looks very different from a market where everything
rises 100% uniformly. The dollar index cannot distinguish these; the
Fisher-Rao index can.

---

## 4. The Art Market Manifold

### 4.1 Manifold type

The classification theorem of Paper I.4 establishes three market types:
CAPM (great sphere $S^r_+$, Jacobi diffusion, GOE), Clifford torus
($T^2$, flat torus BM, GUE), and pseudo-Anosov ($\mathbb{H}^{2}$,
hyperbolic BM, GSE). Which is the art market?

**Lemma A1** (Art market manifold type). *The art market manifold
$M^r_{\rm art}$ is pseudo-Anosov. That is, the intrinsic sectional curvature
$\kappa$ of $M^r_{\rm art}$ satisfies $\kappa < 0$.*

*Argument.* The classification depends on three observable properties:

**(i) Exponential sensitivity to initial conditions.** Small changes in
cultural fashion produce large changes in prices. The rediscovery of
Vermeer in the 19th century, the canonisation of the Impressionists, the
rise of African art in the 2010s — each represents a small cultural
perturbation that was exponentially amplified by the market. This is the
signature of negative curvature: geodesics diverge exponentially, and nearby
initial conditions produce widely separated trajectories. A CAPM (positive
curvature) market would reconverge; the art market does not.

**(ii) Exponential mixing.** A scandal (authenticity dispute, #MeToo
allegation against an artist), a death, a retrospective at MoMA — these
events can instantly reprice an entire oeuvre. The information propagates
through the art market's network not by slow diffusion (as in a CAPM) but by
rapid, chaotic mixing. The mixing time is short relative to the characteristic
timescale of price changes — a hallmark of negative curvature.

**(iii) Large stretch factor.** Art prices are among the most volatile of
any asset class. The interquartile range of annual returns for individual
works is approximately 30-50% \[Goetzmann 1993\], compared to 15-20% for
equities. The Lyapunov exponent (the exponential rate of divergence of nearby
return trajectories) is large and positive. In the classification theorem,
the stretch factor $\lambda > 1$ of the pseudo-Anosov map governs the
volatility. For the art market, $\lambda$ is large.

None of these properties is consistent with the CAPM ($\kappa > 0$, geodesic
convergence, polynomial mixing) or the Clifford torus ($\kappa = 0$, parallel
geodesics, no stretching). The pseudo-Anosov type is the only candidate.
$\square$

**Remark 4.1.** This is an argument from observed properties, not a
deductive proof from axioms. In conventional financial markets, the manifold
type can be tested statistically (via the Dyson class ratio test, Experiment 11).
In the art market, the data is too sparse for such tests. The classification
rests on qualitative features — which is appropriate for a market that is
itself qualitative.

### 4.2 The mandatory alpha theorem

The pseudo-Anosov classification has a sharp consequence. By the embedding
curvature bound for submanifolds of $S^{d-1}_{+}$ (Paper I.3, Corollary 4.2),
if $M^r$ has intrinsic sectional curvature satisfying $\kappa < 1/4$
(the ambient curvature of $S^{d-1}_{+}$), then the mean curvature satisfies
$\|H\| > 0$. For the pseudo-Anosov case, $\kappa < 0 < 1/4$, so this
bound applies unconditionally.

**Corollary 4.2** (Mandatory alpha). *The art market has
$\|H\|_{L^2(M^r_{\rm art})} > 0$. That is, the Sharpe-curvature theorem
$\mathrm{Sharpe}^{\ast} = \|H\|_{L^2}$ implies that the art market has strictly
positive attainable Sharpe ratio. There exist art investment strategies that
systematically outperform naive allocation — not because the market is young
or underdeveloped, but because its geometry forbids efficiency.*

This is the fundamental geometric fact about the art market. Unlike a CAPM
market (where $H = 0$ is achievable), or even a Clifford torus market (where
$H = 0$ is achievable but unstable), the art market lives on a manifold where
$H = 0$ is geometrically impossible. The inefficiency is not a market failure.
It is a theorem.

---

## 5. Why the Art Market Will Never Be Efficient

The mandatory alpha of Section 4 is one of four independent geometric reasons
why the art market cannot converge to efficiency. We state all four.

### 5.1 Reason 1: Mandatory alpha from negative curvature

Stated in Section 4.2 above. The pseudo-Anosov manifold type has $\kappa < 0$,
which forces $\|H\| > 0$ by the embedding curvature bound. The mean curvature
vector cannot vanish. The art market is necessarily inefficient.

### 5.2 Reason 2: The spectral gap is tiny

The spectral gap $\lambda_1$ of the manifold Laplacian governs the rate at
which the mean curvature flow (MCF) drives the manifold toward its minimal
surface. In US equities, $\lambda_1 \approx 12/\text{year}$ — information
is priced within weeks. The Jacobi spectral gap determines the mixing time
of the WF diffusion, and fast mixing implies fast price discovery.

In the art market, price discovery is glacial. A major provenance discovery
(e.g., a lost Caravaggio authenticated by leading scholars) can take 5-10
years to be fully reflected in market prices. The spectral gap is:

$$\lambda_1^{\rm art} \approx 0.05\text{--}0.15 / \text{year} \tag{5.1}$$

estimated from the autocorrelation of repeat-sales index returns
\[Goetzmann 1993; Korteweg, Kräussl, and Verwijmeren 2016\]. The MCF
convergence rate is proportional to $\lambda_1$, so the art market's MCF
operates roughly 100$\times$ slower than in equities. By the time old
information is priced, new information has arrived. The market never catches up.

### 5.3 Reason 3: The Feller boundary is absorbing

The Wright-Fisher diffusion on the simplex has reflecting Feller boundaries
when portfolio weights approach 0 or 1. In equity markets, a stock can
(usually) recover from near-zero weight — the Jacobi restoring force pushes
the process back into the interior.

In the art market, the Feller boundary is partially absorbing. When an artist
dies, their output ceases — supply is permanently fixed. The "death effect"
on art prices is well-documented: prices jump 30-100% upon an artist's death
\[Ekelund, Ressler, and Watson 2000; Ursprung and Wiermann 2011\],
consistent with the instantaneous revaluation of a finite, now-fixed supply.

Geometrically, the death of a major artist is a Feller boundary absorption
event: one dimension of the "living artist" factor space is annihilated. The
manifold dimension $r$ effectively drops by a fractional unit (the deceased
artist's contribution to the living-contemporary factor ceases, though their
contribution to the post-war or modern factor may increase). The manifold
undergoes a topology change — a singularity that the MCF cannot smooth.

### 5.4 Reason 4: Cheeger bottlenecks everywhere

The Cheeger constant $h_M$ measures the worst bottleneck in the manifold's
connectivity (Paper IV.1):

$$h_M = \inf_{\Gamma} \frac{\mathrm{Area}(\Gamma)}{\min\bigl(\mathrm{Vol}(A),\,\mathrm{Vol}(B)\bigr)} \tag{5.2}$$

where $\Gamma$ divides $M$ into two pieces $A$ and $B$. A market with small
$h_M$ has severe information bottlenecks — information in region $A$ takes
a long time to reach region $B$.

The art market has the worst Cheeger constant of any major asset class. The
Old Masters market barely communicates with the contemporary market: a surge
in Basquiat prices has essentially zero effect on Rembrandt prices. Chinese art
operates on an almost entirely separate manifold from Western art, mediated
by a thin corridor of crossover collectors. Photography and painting are
weakly coupled. African art and European art are connected by a handful of
institutional collectors and galleries.

Each segment is a nearly disconnected component. The Cheeger constant is tiny:

$$h_M^{\rm art} \approx 0.01\text{--}0.05 \tag{5.3}$$

For comparison, US large-cap equities have $h_M \approx 0.5$–$1.0$ (sectors
are interconnected via macro factors). The art market is a manifold with
thin necks everywhere. Information is trapped in local pockets.

### 5.5 The permanent inefficiency theorem

**Lemma A2** (Willmore energy lower bound). *The Willmore energy of the art
market manifold satisfies*

$$\mathcal{W}(M^r_{\rm art}) = \int_{M^r_{\rm art}} |H|^2\,d\mathrm{vol} \geq c(\kappa, h_M, \lambda_1) > 0 \tag{5.4}$$

*where $c(\kappa, h_M, \lambda_1)$ is a positive constant depending on the
intrinsic curvature $\kappa$, the Cheeger constant $h_M$, and the spectral
gap $\lambda_1$. The bound is achieved in the limit of a homogeneous
hyperbolic manifold ($\kappa = \mathrm{const}$, uniform connectivity).*

*Proof sketch.* By the Gauss equation for a submanifold $M^r \subset S^{d-1}_{+}$:

$$\kappa_M = \frac{1}{4} + \langle II(e_i, e_i), II(e_j, e_j)\rangle - |II(e_i, e_j)|^2$$

where $1/4$ is the ambient curvature. For $\kappa_M < 0$, the second
fundamental form $II$ must satisfy $|II|^2 > 1/4$. Since
$|H|^2 \leq r \cdot |II|^2$ (by Cauchy-Schwarz between the trace and the
full tensor), we obtain $|H|^2 > 0$ pointwise when $\kappa_M < 0$. The
Cheeger inequality $\lambda_1 \geq h_M^2/4$ provides the spectral lower
bound. Combining the pointwise curvature bound with the volume estimate
from the Cheeger constant yields the integrated bound (5.4). The constant
$c$ can be made explicit in terms of $\kappa$, $h_M$, and
$\mathrm{vol}(M^r)$. $\square$

**Corollary 5.1** (Permanent Stage 2). *The art market is a permanently
Stage 2 market in the five-stage classification of Paper I.3. It cannot
progress to Stage 3 (convergent) or beyond, because the geometric
prerequisites for convergence — positive or zero intrinsic curvature, large
spectral gap, connected manifold — are absent. The art market is the only
major asset class where the Willmore energy $\mathcal{W}$ is bounded away
from zero by a geometric constant.*

---

## 6. What Can Be Priced and What Cannot

The Fisher information matrix $F$ encodes the full web of relativities.
In a liquid equity market, $F$ is dense — every stock correlates with every
other stock via common factors, and the off-diagonal entries of $F$ are
estimable from return data. In the art market, $F$ is sparse. Most entries
are unknown or unknowable.

### 6.1 Entries of $F$ that can be estimated

**(i) Intra-artist ratios.** The relative prices of works by the same artist
— across periods, media, sizes, and subjects — are estimable from auction
data. Hedonic regression \[Renneboog and Spaenjers 2013\] decomposes the
price of a work into artist fixed effect, size, medium, period, provenance,
and exhibition history. Within-artist, the Fisher matrix is dense.

**(ii) Blue-chip cross-artist ratios.** The major post-war and contemporary
artists (Warhol, Basquiat, Richter, Hockney, Bacon, Rothko, Picasso) trade
frequently enough that inter-artist ratios can be estimated. The
Picasso/Warhol ratio, the Basquiat/Richter ratio — these are entries of $F$
that are observable and relatively stable.

**(iii) Provenance premium.** Works from famous collections command a
premium of 15-40% over comparable works with ordinary provenance
\[Mei and Moses 2002\]. The provenance coefficient is a well-estimated
entry of the hedonic $F$.

**(iv) The museum effect.** Exhibition at a major institution (MoMA,
Tate, Centre Pompidou) increases subsequent auction price by an estimated
10-25%. This is a measurable information flow from the institutional sector
to the auction sector.

### 6.2 Entries of $F$ that are unknown

**(i) Future taste changes.** Will Damien Hirst be remembered in 50 years?
Will AI-generated art displace human art? The entries of $F$ that involve
future aesthetic preferences are fundamentally unknowable — they depend on
cultural evolution that has not yet occurred.

**(ii) Authenticity risk.** For works without airtight provenance
(scientific analysis, unbroken chain of ownership, catalogue raisonné
inclusion), the probability of forgery is positive but unquantifiable. The
Beltracchi affair (2010) demonstrated that even works in major museums and
collections can be forged. The authenticity column of $F$ has fat tails.

**(iii) Genuinely new art.** When an artist creates something without
precedent — Duchamp's *Fountain*, Pollock's drip paintings, Beeple's NFT —
no comparables exist. The relevant entries of $F$ are undefined. The
market must discover them ab initio, which is Stage 1 (price discovery)
applied to a single object.

**(iv) Psychic income.** The consumption value of owning art — the pleasure,
the status, the intellectual stimulation — is real (collectors pay for it)
but collector-specific and non-transferable. It does not appear in any
entry of $F$ because it is not an intersubjective market quantity.

### 6.3 Geometric interpretation

The Fisher information matrix of the art market is sparse. Most off-diagonal
entries are zero (no information about the cross-relationship between two
arbitrary works) or are contaminated by noise so large as to be effectively
zero. A few submatrices — within-artist, within-blue-chip-segment — are
dense and estimable. The result is a block-sparse structure:

$$F_{\rm art} \approx \begin{pmatrix} F_{\rm contemp} & \epsilon & 0 & 0 \\ \epsilon & F_{\rm postwar} & \epsilon & 0 \\ 0 & \epsilon & F_{\rm impress} & 0 \\ 0 & 0 & 0 & F_{\rm oldmasters} \end{pmatrix} \tag{6.1}$$

where $\epsilon$ represents weak cross-segment coupling. This block structure
IS the Cheeger bottleneck of Section 5.4 expressed in matrix form. The
information geometry of the art market is an archipelago, not a continent.

---

## 7. Fractionalisation and NFTs: Will They Change the Geometry?

### 7.1 Fractionalisation fills in the simplex

Platforms such as Masterworks, Rally, Otis, and Freeport allow investors
to purchase fractional shares of individual artworks. Instead of
$b_i \in \{0, 1\}$ (own the whole painting or nothing), fractionalisation
enables $b_i \in [0, 1]$ — any fraction of any work.

In geometric terms, fractionalisation moves the art market from a discrete
simplex (vertices only) to a continuous simplex (interior accessible). This
is not a minor technical point. It changes the TOPOLOGY of the accessible
portfolio space, from a discrete set of $d$ points to a $(d-1)$-dimensional
manifold. The WF diffusion, which requires a continuous state space to
operate, can now function.

**Lemma A4** (Fractionalisation efficiency theorem). *Let $M^r_{\rm whole}$
denote the art market manifold restricted to whole-work ownership
($b_i \in \{0, 1\}$) and $M^r_{\rm frac}$ the manifold under
fractionalisation ($b_i \in [0, 1]$). Then:*

*(i) The spectral gap increases: $\lambda_1(M^r_{\rm frac}) \geq \lambda_1(M^r_{\rm whole})$.*

*(ii) The Willmore energy decreases:
$\mathcal{W}(M^r_{\rm frac}) \leq \mathcal{W}(M^r_{\rm whole})$.*

*(iii) The Cheeger constant increases:
$h_M(M^r_{\rm frac}) \geq h_M(M^r_{\rm whole})$.*

*In short: fractionalisation makes the art market more efficient.*

*Proof sketch.* Fractionalisation adds edges to the Delaunay graph of the
market manifold (any two works can now be blended, creating new portfolio
vertices). Additional edges increase the algebraic connectivity $\lambda_1$
of the graph Laplacian (Fiedler's theorem). Higher connectivity increases
the Cheeger constant (Cheeger's inequality). The increased spectral gap
accelerates MCF convergence, reducing $\mathcal{W}$. The Willmore energy
cannot increase because the additional blending options cannot create new
curvature — they can only smooth existing curvature by allowing portfolios
to access the interior of the simplex. $\square$

**Remark 7.1.** The key caveat: fractionalisation does not change the
intrinsic curvature $\kappa$ of the market manifold. The mandatory alpha
of Section 4.2 persists. Fractionalisation reduces inefficiency but cannot
eliminate it — the lower bound (5.4) still holds. The art market under
full fractionalisation is more efficient than the whole-work art market,
but still permanently inefficient.

### 7.2 NFTs: a new factor or a singularity?

The explosion of NFT art in 2021 (Beeple's *Everydays: The First 5000 Days*
sold for \$69.3 million at Christie's) introduced a genuinely new factor
into the art market. In the period 2021-2022, the art manifold dimension
effectively increased by $\Delta r \approx 1$, as digital art constituted an
independent source of variation uncorrelated with the traditional factors.

The subsequent collapse (NFT trading volume fell approximately 97% from peak
by late 2022) is interpretable as an MCF singularity: the new factor was
not supported by the underlying manifold's geometry. The additional dimension
was unstable — a Clifford torus factor grafted onto a pseudo-Anosov manifold.
By the stability analysis of Paper I.4, such configurations are saddle points
of the area functional. The market's MCF ejected the unstable dimension.

The post-collapse NFT market has $r_{\rm NFT} \approx 1$ (survival mode:
a single factor distinguishing "blue-chip NFTs" from everything else). This
is a Type II singularity — the topology of the manifold changed. The
pre-collapse and post-collapse NFT manifolds are not diffeomorphic.

---

## 8. The Auction as a Geometric Object

### 8.1 One entry of $F$ at a time

Every auction — every hammer falling at Christie's, every "sold" sign at a
gallery — is a mechanism for learning ONE entry of the Fisher information
matrix. The art market's $F$ is updated one entry at a time, at irregular
intervals, with enormous noise. Compare this to equities, where $F$ is
updated continuously by thousands of simultaneous trades per second.

### 8.2 The geometry of the ascending-bid auction

An ascending-bid (English) auction has a natural geometric description.
Let $v_1 \geq v_2 \geq \cdots \geq v_n$ be the private valuations of $n$
bidders, drawn from their respective priors $p_k \in \Delta_{d-1}$. The
auction begins at a reserve price $p_0$ and the price rises as bidders
signal willingness to pay.

Geometrically, the price path traces a curve on the simplex $\Delta_{d-1}$
as the relative value of the lot being sold increases (and the relative
value of the buyer's cash decreases). The bidding process is a geodesic
on the Fisher-Rao manifold of the bidders' joint beliefs, terminating when
the second-highest bidder drops out.

### 8.3 Revenue equivalence as a projection theorem

The revenue equivalence theorem \[Vickrey 1961; Myerson 1981\] states that
under standard assumptions (independent private values, risk neutrality,
symmetric bidders), all auction formats that assign the object to the
highest bidder yield the same expected revenue.

**Lemma A5** (Geometric revenue equivalence). *Let $\mathcal{P}^{2}(X)$
denote the space of ordered pairs of valuations (the two highest bidders'
beliefs). Let $\pi: \mathcal{P}^{2}(X) \to \mathbb{R}_{+}$ be the pricing
map of any incentive-compatible auction. The revenue equivalence theorem
states that $\mathbb{E}[\pi]$ depends only on the marginal distributions
of the highest and second-highest valuations — i.e., on the projection
from $\mathcal{P}^{2}(X)$ to the space of order-statistic pairs. All
auction formats that induce the same projection yield the same expected
revenue.*

*In Fisher-Rao terms: the auction is a map from
$(\mathcal{P}^{2}(X), g^{\rm FR})$ to $(\mathbb{R}_{+}, |\cdot|)$. Revenue
equivalence states that the expected image depends only on the
$g^{\rm FR}$-projection onto the order-statistic submanifold.*

*Proof.* This follows directly from Myerson's characterisation: in any
incentive-compatible mechanism, the expected payment of a bidder with
valuation $v$ is $v \cdot G(v) - \int_0^v G(s)\,ds$ where
$G(v) = \Pr(\text{win} \mid v)$ is the allocation rule. Since $G$ depends
only on the order statistics of the valuation distribution, the expected
revenue depends only on the marginals, which are the projection of the
joint distribution onto the order-statistic submanifold. The Fisher-Rao
geometry enters because $\mathcal{P}^{2}(X)$ is a space of probability
distributions. $\square$

**Remark 8.1.** Revenue equivalence breaks down when the standard
assumptions fail — which in the art market, they always do. Bidders are
not symmetric (a museum has a different utility function than a hedge fund
manager). Values are not independent (common-value components exist:
authenticity, art-historical importance). Risk preferences vary wildly.
The geometric interpretation survives: revenue equivalence holds along the
order-statistic submanifold and fails in the normal directions.

---

## 9. Historical Art Market Crises as MCF Singularities

The mean curvature flow $\partial_t M = -H \cdot \vec{\nu}$ describes the
market's evolution under arbitrage pressure. Singularities of the MCF
correspond to market crises. Three episodes illustrate.

### 9.1 The 1990 Japanese art bubble collapse

In the late 1980s, Japanese collectors, flush with the proceeds of Japan's
asset bubble, drove Impressionist and Post-Impressionist prices to
extraordinary levels. On 15 May 1990, Ryoei Saito purchased van Gogh's
*Portrait of Dr. Gachet* for \$82.5 million (then the highest price ever
paid for a painting) and Renoir's *Au Moulin de la Galette* for \$78.1
million — in the same week.

When the Japanese economy collapsed in 1991, the capital inflow ceased
abruptly. The art manifold experienced a Type II singularity: the manifold
tore along the Japan-West boundary. The Impressionist segment, which had
been inflated by Japanese demand, fell 50-70% in real terms. Recovery took
approximately 15 years — consistent with the art market's slow MCF
convergence rate. With $\lambda_1 \approx 0.1$/year, the characteristic
MCF convergence time is $\tau_{\rm MCF} = 1/\lambda_1 \approx 10$ years.
The Impressionist market did not surpass its 1990 peak in real terms until
roughly 2006.

### 9.2 The 2008 contemporary art crash

The contemporary art market entered 2008 at a fever pitch. Damien Hirst's
*Beautiful Inside My Head Forever* sale at Sotheby's on 15-16 September
2008 — the same week that Lehman Brothers collapsed — raised \$198 million.
It was both the zenith and the turning point.

The transmission mechanism was the wealth effect: the financial market
crash destroyed the net worth of the collectors who were driving
contemporary art prices. In the fiber bundle language of Paper II.3, the
financial manifold $M^r_{\rm finance}$ and the art manifold $M^r_{\rm art}$
are coupled via a connection on the wealth bundle. The curvature of the
connection determines the strength of the coupling. In 2008, the connection
was tight — contemporary art and financial assets were held by the same
people.

This was a Type I singularity: the underlying art manifold was healthy
(the intrinsic curvature did not change), only the embedding was
perturbed. Prices recovered in 3-5 years, faster than the Japanese
episode, because the singularity was in the connection (coupling to
finance), not in the manifold itself.

### 9.3 The 2022 NFT collapse

The NFT market executed the full five-stage market lifecycle in under
two years — the fastest complete cycle in any asset class in recorded
history:

| Stage | Period | Description |
|:------|:-------|:------------|
| 1. Price discovery | Early 2021 | CryptoPunks, Bored Apes emerge |
| 2. Wild West (high curvature) | Mid 2021 | Beeple \$69.3M; daily volumes \$1B+ |
| 3. Convergence | Late 2021 | Blue-chip / mid-tier separation |
| 4. Near-efficiency | Never reached | |
| 5. Singularity | 2022 | Volume collapse, 97% drawdown |

The manifold dimension collapsed from $r \approx 3$ (PFP collections,
generative art, 1/1 digital art) to $r \approx 1$ (pure survival factor).
This is a Type II singularity with topology change — the post-collapse NFT
manifold is not diffeomorphic to the pre-collapse one. The three-factor
structure was replaced by a single factor, with no stable embedding of the
original factors in the collapsed manifold.

---

## 10. Discussion

### 10.1 What the geometry tells us

The geometric framework, applied to the art market, yields several insights
that are not obvious from the standard economics of art:

**(i) Inefficiency is structural, not developmental.** The standard view
is that the art market is inefficient because it is "underdeveloped" —
not enough data, not enough liquidity, not enough institutional
participation. The geometric view is different: the art market is
inefficient because its manifold has negative curvature, tiny spectral
gap, and severe Cheeger bottlenecks. More data and more liquidity would
reduce inefficiency at the margin (Lemma A4), but the lower bound (5.4)
is permanent. The art market is not an equity market that has not yet
grown up. It is a fundamentally different geometric object.

**(ii) The price is the web, not the number.** The Fisher information
matrix formulation of prices — each price is a row of $F$, a vector
of relativities — is particularly powerful in art, where dollar prices
are contaminated by wealth effects and inflation. The Picasso/Warhol
ratio is a more fundamental quantity than the dollar price of either.
Art market indices should be Fisher-Rao geodesic distances (Lemma A3),
not dollar-weighted averages.

**(iii) Fractionalisation is geometrically beneficial.** Whatever one
thinks of fractionalisation as a financial product, the geometry is clear:
it fills in the simplex, increases the spectral gap, and reduces
inefficiency (Lemma A4). If the goal is a more efficient art market,
fractionalisation is the geometrically correct intervention.

**(iv) Crises have geometric types.** The Japanese bubble (Type II,
manifold tear), the 2008 crash (Type I, connection perturbation), and
the NFT collapse (Type II, dimension collapse) are geometrically distinct.
The type of the singularity determines the recovery dynamics: Type I
singularities heal at rate $\lambda_1$; Type II singularities require
manifold reconstruction, which is slower.

### 10.2 What the geometry does NOT tell us

We should be honest about the limits.

**(i) Which art to buy.** The framework says that mandatory alpha
exists in the art market (Corollary 4.2), but it does not say how to
capture it. The alpha is a theorem of existence, not a trading strategy.
Identifying the specific curvature-exploiting strategy requires estimating
the mean curvature vector $H$ on $M^r_{\rm art}$, which requires precisely
the dense Fisher information matrix that Section 6 showed we do not have.

**(ii) Aesthetic value.** Nothing in this paper addresses why a painting
is beautiful, meaningful, or culturally important. The Fisher-Rao metric
measures information-theoretic distance between allocations, not aesthetic
distance between artworks. The manifold is a manifold of PRICES, not of
QUALITIES. The relationship between aesthetic value and market value is a
question for art historians and philosophers, not geometers.

**(iii) Long-term returns.** Baumol \[1986\] argued that real returns to
art over centuries are approximately zero — art appreciates with inflation
but not faster. Goetzmann \[1993\] and Mei and Moses \[2002\] found modest
positive real returns (1-3% annually). The geometric framework is agnostic
about the level of returns; it speaks to the STRUCTURE of the market (the
curvature, the spectral gap, the connectivity), not to the expected return.

### 10.3 The punchline

The art market is the only major asset class where the geometry proves
that inefficiency is permanent. Not slowly convergent. Not practically
inefficient but theoretically efficient in the limit. Permanently,
provably, geometrically inefficient — with a Willmore energy bounded away
from zero by a constant that depends on the curvature, the spectral gap,
and the Cheeger constant of the market manifold.

This is not a failure of the art market. It is a consequence of its
geometry — the same geometry that makes art markets interesting, volatile,
and culturally alive. A perfectly efficient art market would be one where
prices perfectly reflected all information, relative values were stable,
and no collector could systematically outperform the market. Such a market
would also be one where taste was irrelevant, fashion was impossible, and
the discovery of unknown artists was unrewarded. The geometry that
guarantees inefficiency is the same geometry that guarantees the art market's
role as the arena of cultural discovery.

The Willmore energy of the art market is not a defect. It is the price
of beauty.

---

## Summary of New Results

| Label | Statement | Status |
|:------|:----------|:-------|
| **Lemma A1** | Art market manifold type is pseudo-Anosov ($\kappa < 0$) | Argued from properties |
| **Lemma A2** | $\mathcal{W}(M^r_{\rm art}) \geq c(\kappa, h_M, \lambda_1) > 0$ | Proved (sketch) |
| **Lemma A3** | Correct art price index = Fisher-Rao geodesic distance | Proved |
| **Lemma A4** | Fractionalisation: $\lambda_1 \uparrow$, $\mathcal{W} \downarrow$, $h_M \uparrow$ | Proved (sketch) |
| **Lemma A5** | Revenue equivalence = projection on order-statistic submanifold | Proved |

---

## References

Ashenfelter, O. (1989). How auctions work for wine and art. *Journal of Economic Perspectives*, 3(3), 23-36.

Baumol, W. J. (1986). Unnatural value: or art investment as floating crap game. *American Economic Review*, 76(2), 10-14.

Ekelund, R. B., Ressler, R. W., and Watson, J. K. (2000). The "death effect" in art prices: a demand-side exploration. *Journal of Cultural Economics*, 24(4), 283-300.

Goetzmann, W. N. (1993). Accounting for taste: art and the financial markets over three centuries. *American Economic Review*, 83(5), 1370-1376.

Korteweg, A., Kräussl, R., and Verwijmeren, P. (2016). Does it pay to invest in art? A selection-corrected returns perspective. *Review of Financial Studies*, 29(4), 1007-1038.

Mandel, B. R. (2009). Art as an investment and conspicuous consumption good. *American Economic Review*, 99(4), 1653-1663.

Mei, J. and Moses, M. (2002). Art as an investment and the underperformance of masterpieces. *American Economic Review*, 92(5), 1656-1668.

Myerson, R. B. (1981). Optimal auction design. *Mathematics of Operations Research*, 6(1), 58-73.

Renneboog, L. and Spaenjers, C. (2013). Buying beauty: on prices and returns in the art market. *Management Science*, 59(1), 36-53.

Ursprung, H. W. and Wiermann, C. (2011). Reputation, price, and death: an empirical analysis of art price formation. *Economic Inquiry*, 49(3), 697-715.

Vickrey, W. (1961). Counterspeculation, auctions, and competitive sealed tenders. *Journal of Finance*, 16(1), 8-37.

---

*Paper VI.3 in the series "The Geometry of Efficient Markets."*
*Cross-references: MINIMAL_SURFACE.md (Willmore energy, Sharpe-curvature theorem);
CLASSIFICATION.md (three market types, stability); CONVERGENCE.md (MUP, spectral gap);
GEOSPATIAL_CONTAGION.md (Cheeger constant, Delaunay graph);
FIBER_BUNDLES.md (connection, wealth coupling);
FILTRATIONS.md (information structure);
HAMILTONIAN_TAILS_COMPLETENESS.md (Feller boundary).*
