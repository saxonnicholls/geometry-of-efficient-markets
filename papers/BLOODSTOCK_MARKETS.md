# The Geometry of Bloodstock Markets:
## Yearlings, Stallions, Polo Ponies, and the Manifold
## of Biological Potential

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VI.6** — Accessible

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
The thoroughbred yearling market — Magic Millions on the Gold Coast,
Inglis Easter in Sydney, Tattersalls in Newmarket, Keeneland September in
Kentucky — is a US$4 billion annual market in which buyers pay for
biological potential that will not be resolved for years. A yearling is a
bundle of genetic, phenotypic, and environmental signals: a point on a
high-dimensional manifold of characteristics whose future racing performance
lives in an enormous fiber. We develop the complete geometric theory of
bloodstock markets within the framework of this monograph.

The central insight: **a horse is a point on the characteristic manifold
$M_{\rm horse}$, and its price under any discipline is a projection of
that point onto a discipline-specific sub-manifold.** The same physical
animal has different values for flat racing, steeplechasing, polo, dressage,
showjumping, and eventing — because each discipline defines a different
projection $\pi_{\rm discipline}: M_{\rm horse} \to M_{\rm discipline}$,
and the fiber (the characteristics irrelevant to that discipline) differs.
The Fisher-Rao metric weights each characteristic by its predictive power
for performance in the target discipline.

**Principal results:**

**(i) The characteristic manifold.** The space of all horses is a manifold
$M_{\rm horse}$ of dimension $d_{\rm char} \approx 15\text{-}25$, embedded
in the simplex of normalised characteristics. The Fisher-Rao metric at a
point (a specific horse) is $g^{\rm FR}_{ij}(h) = \delta_{ij}/h_i$, where
$h_i$ is the normalised weight of characteristic $i$. Sire quality has large
weight (high information, low sensitivity); conformation minutiae have small
weight (low information, high sensitivity). The auction market operates on
this manifold.

**(ii) The fiber of unrealised potential.** At the yearling sale, the
horse's future racing performance is in the fiber
$F_{\rm yearling} = \pi^{-1}(h_{\rm observed})$ — the set of all possible
futures consistent with the observed characteristics. This fiber is ENORMOUS
for a yearling (most of its career is unknown) and shrinks as information
arrives: after trials ($F_{\rm trial}$), after maiden race ($F_{\rm maiden}$),
after Group race ($F_{\rm Group}$), and essentially vanishes for a retired
stallion with 10 crops on the ground. The channel capacity of the yearling
sale is $C_{\rm sale} = h^{\rm horse}_{\rm Kelly} - h^{\rm fiber}_{\rm Kelly}$
(MANIFOLD_IS_THE_CHANNEL.md Theorem MC2): the Kelly rate of the full
characteristic manifold minus the Kelly rate of the unrealised fiber.

**(iii) The Magic Millions is a confidence σ-algebra measurement.** Each
bidder at a yearling sale has a confidence σ-algebra
$\mathcal{F}^{\rm conf}_{\rm bidder}$ (CONFIDENCE.md): the set of
characteristics they believe they can evaluate reliably enough to bid on.
A veteran horseman with 40 years' experience has a finer σ-algebra than a
first-time buyer — they can distinguish subtle conformation differences,
gait qualities, and temperament signals that the novice cannot. The auction
price is determined by the COARSEST common refinement of all bidders'
confidence σ-algebras — and the vendor's reserve by their own. The
information gap between the vendor (who has observed the horse daily for
18 months) and the buyer (who sees it for 5 minutes in the parade ring) is
a fiber bundle projection: the vendor's manifold has a smaller fiber than the
buyer's.

**(iv) Discipline-specific projections.** A horse's value depends on the
discipline:

| Discipline | Projection $\pi$ | Key factors in base | Key factors in fiber |
|:---|:---|:---|:---|
| Flat racing | Speed, precocity, sire | Stamina, temperament, soundness |
| Steeplechasing | Stamina, jumping ability, constitution | Speed, precocity |
| Polo | Temperament, agility, acceleration | Speed over distance, sire ranking |
| Dressage | Movement quality, trainability, conformation | Speed, courage |
| Showjumping | Scope, power, courage | Temperament under rider, endurance |
| Eventing | All-round athleticism, bravery | Specialisation in any discipline |
| Breeding (sire) | Progeny statistics, pedigree, type | Racing ability (already resolved) |
| Breeding (broodmare) | Pedigree, conformation, progeny | Racing ability (already resolved) |

The same physical horse is a different point on each discipline manifold.
A horse that is worthless for flat racing (wrong fiber) may be a champion
polo pony (right base under a different projection). **The market for horses
is not one market — it is a family of markets, one per discipline, connected
by the shared characteristic manifold.** Each discipline market is a
sub-channel of the full horse channel, and the inter-discipline trade (a
failed racehorse becoming a polo pony) is information flowing between
sub-channels.

**(v) The sire market is a futures market on the characteristic manifold.**
A stallion's stud fee is a futures contract on the weighted average value of
his progeny. The Black-type statistics (winners, stakes winners, Group
winners as a percentage of runners) are the REALISED performance of the
projection $\pi_{\rm flat}$ applied to the stallion's progeny sample. The
stud fee adjusts as the sample grows — it IS the Bayesian posterior mean of
the stallion's genetic value, updated with each crop. The Fisher-Rao distance
between successive crop statistics measures the information arrival rate. A
"hot" young sire (rapid stud fee appreciation) is a channel with high
capacity — each new crop delivers a lot of information. A proven sire
(stable stud fee) is a channel near capacity — further crops deliver
diminishing information.

**(vi) The pinhook is a geometric arbitrage.** Pinhooking — buying a yearling
and reselling as a 2-year-old after breaking and early training — is an
explicit bet on reducing the fiber. The pinhooker pays the yearling price
(large fiber, low channel capacity), adds information by training and
trialling (shrinks the fiber, increases capacity), and sells the 2-year-old
at the updated price (smaller fiber, higher capacity). The pinhook profit is:

```math
\alpha_{\rm pinhook} = C_{\rm 2yo} - C_{\rm yearling} - \text{Cost}_{\rm training} \tag{0.1}
```

— the capacity gain from fiber reduction minus the cost of producing the
information. This is positive when the cost of training is less than the
value of the information it reveals.

**Keywords.** Bloodstock; yearling; Magic Millions; Tattersalls; Keeneland;
Inglis; thoroughbred; auction; pedigree; conformation; Fisher-Rao metric;
characteristic manifold; fiber bundle; discipline projection; pinhook;
stallion; stud fee; polo pony; dressage; confidence σ-algebra; channel
capacity; biological potential.

**MSC 2020.** 91G10, 62P20, 91B26, 53A10, 94A15, 92D15.

---

## 1. The Horse as a Point on a Manifold

### 1.1 The characteristic space

A horse at any moment is described by a vector of characteristics:

**Genetic characteristics** (fixed at conception):
- Sire (and sire's race record, progeny record, stud fee history)
- Dam (and dam's race record, produce record)
- Damsire (second-generation maternal effect)
- Inbreeding coefficient (closeness of pedigree cross)
- Mitochondrial line (X-factor, dam line depth)

**Phenotypic characteristics** (observable at inspection):
- Height (hands), weight, bone measurement
- Conformation: shoulder angle, hip angle, length of back, stride length
- Gait quality: walk, trot (assessed subjectively at parade)
- Coat and condition
- Temperament (box behaviour, parade behaviour, reaction to stimuli)

**Performance characteristics** (revealed over time):
- Breeze-up time (for 2-year-olds sold at breeze-up sales)
- Trial times and placings
- Race record: wins, places, prizemoney, pattern-race performance
- Timeform rating, Racing Post Rating, or equivalent

**Environmental characteristics:**
- Trainer (and trainer's strike rate, stable quality)
- Preparation (reported work, travel history)
- Veterinary status (wind, joints, scope reports)

Denote these $d_{\rm char}$ characteristics. Not all are independent —
they are correlated through genetics, management, and the laws of
biomechanics. The effective dimension is:

```math
r_{\rm horse} = \text{srank}(\Sigma_{\rm char}) \approx 15\text{-}25 \tag{1.1}
```

where $\Sigma_{\rm char}$ is the covariance matrix of characteristics across
the horse population and $\text{srank}$ is the stable rank.

### 1.2 The characteristic manifold

**Definition 1.1** (Characteristic manifold). *The characteristic manifold
$M_{\rm horse}$ is the $r_{\rm horse}$-dimensional submanifold of
$S^{d_{\rm char}-1}_{+}$ obtained by projecting the characteristic vector
onto its principal components and embedding via the Bhattacharyya isometry
$h \mapsto \sqrt{h}$.*

The Fisher-Rao metric on $M_{\rm horse}$:

```math
g^{\rm FR}_{ij}(h) = \frac{\delta_{ij}}{h_i} \tag{1.2}
```

where $h_i$ is the normalised weight of characteristic $i$ for the horse at
the point in question. This metric encodes a fundamental truth of horse
assessment:

- **High-weight characteristics** (sire quality, overall type): $g_{ii}$
  small. The market is INSENSITIVE to small variations. A horse by Frankel
  is a horse by Frankel; minor differences in type don't move the price much.
- **Low-weight characteristics** (minor conformation details, temperament
  nuances): $g_{ii}$ large. The market is HYPERSENSITIVE. A small difference
  in fetlock angle or a hint of nervousness can dramatically change the
  assessment — because these are rare signals in a sea of noise.

This is exactly the same structure as the portfolio simplex
(OBSERVERS_AND_CHANNELS.md Section 1): the observer at position $h$ experiences
the market through the lens of their own position. A breeding farm with 50
mares by the same sire is INSENSITIVE to sire effects (large $h_{\rm sire}$)
and HYPERSENSITIVE to individual variation (small $h_{\rm individual}$). A
buyer with no other horses by that sire has the reverse sensitivity profile.

### 1.3 The horse IS an intermarket

Each horse is simultaneously:
- A point on $M_{\rm flat}$ (flat racing value)
- A point on $M_{\rm jumps}$ (steeplechasing value)
- A point on $M_{\rm polo}$ (polo value)
- A point on $M_{\rm dressage}$ (dressage value)
- A point on $M_{\rm breeding}$ (breeding value)

These are different projections of the same point on $M_{\rm horse}$. A
trade that moves a horse from one discipline to another (a failed racehorse
becomes a polo pony) is information flowing between sub-channels — exactly
the inter-market channel of MANIFOLD_IS_THE_CHANNEL.md.

The connected sum structure:

```math
M_{\rm horse} = M_{\rm flat} \#_{\rm retraining} M_{\rm jumps} \#_{\rm retraining} M_{\rm polo} \#_{\rm retraining} M_{\rm dressage} \tag{1.3}
```

The necks are the retraining pathways. A horse that retrains easily has a
wide neck (high channel capacity between disciplines). A horse that cannot
retrain (too specialised) has a thin neck (low capacity).

---

## 2. The Yearling Sale as Information Market

### 2.1 The information hierarchy at the sale

At a yearling sale, information arrives in stages:

| Stage | Information added | Fiber reduction | Who learns |
|:---|:---|:---|:---|
| Catalogue entry | Pedigree, vendor, lot number | Genetic factors resolved | Everyone |
| Parade ring inspection | Conformation, gait, temperament | Phenotype partially resolved | Attendees |
| Veterinary inspection | Wind, joints, scope | Soundness resolved | Buyers who pay for scope |
| Private inspection | Handler's assessment, dam's history | Soft information | Connected buyers |
| Bidding | Other buyers' valuations | Market consensus revealed | All participants |

Each stage is a **channel** that transmits information from the horse to the
buyer. The total information available at the fall of the hammer is the
union of all channels:

```math
\mathcal{F}^{\rm sale}_{\rm total} = \mathcal{F}^{\rm catalogue} \vee \mathcal{F}^{\rm parade} \vee \mathcal{F}^{\rm vet} \vee \mathcal{F}^{\rm private} \vee \mathcal{F}^{\rm bidding} \tag{2.1}
```

But no buyer observes all channels. The information hierarchy at a typical
Magic Millions sale:

| Buyer type | Channels observed | Effective σ-algebra | Typical spend |
|:---|:---|:---|:---|
| Remote catalogue buyer | Catalogue only | Coarsest | \$20k-\$100k |
| Attending agent | Catalogue + parade | Medium | \$50k-\$500k |
| Major syndicate | All channels | Finest | \$200k-\$5M+ |
| Vendor buying back | All + 18 months daily observation | Vendor's full σ-algebra | Reserve price |

The vendor's information advantage is STRUCTURAL — they have observed the
horse daily for 18 months. No amount of parade-ring inspection can close
this gap. The vendor's fiber is much smaller than any buyer's fiber:

```math
\dim(F_{\rm vendor}) \ll \dim(F_{\rm buyer}) \tag{2.2}
```

This is the classic lemons problem (Akerlof [1970]) in geometric language:
the vendor's channel has higher capacity than the buyer's. The reserve price
reflects the vendor's smaller fiber; the hammer price reflects the buyer's
larger fiber. The spread between them is the value of the information
asymmetry.

### 2.2 The catalogue page as a channel

The catalogue page is a LOSSY CHANNEL from the horse to the buyer. It
transmits:
- Pedigree (lossless — fully specified)
- Vendor (partial — reputation is a summary statistic)
- Physical description (very lossy — "bay colt" tells you almost nothing)
- Dam's produce (partial — you know results but not why)

The capacity of the catalogue channel:

```math
C_{\rm cat} = H(M_{\rm horse}) - H(M_{\rm horse} | \text{catalogue}) \tag{2.3}
```

Empirically, pedigree alone explains approximately 30-40% of yearling sale
price variance (Chezum and Wimmer [1997], Vickner and Koch [2001]). So:

```math
C_{\rm cat} \approx 0.35 \cdot h^{\rm horse}_{\rm Kelly}
```

The remaining 65% is in the physical inspection, veterinary reports, and
private channels. A buyer who bids off the catalogue alone is using a
channel with only 35% of total capacity.

### 2.3 The parade ring as a channel

The 5-minute parade ring inspection adds conformation, gait, and
temperament information. Professional judges claim they can assess:
- Overall type and balance
- Structural correctness (leg alignment, joint angles)
- Quality of movement (walk, and sometimes trot)
- Temperament (calm, nervous, aggressive, switched-off)
- "Presence" — an ill-defined quality that experienced judges claim correlates
  with racing ability

The capacity of the parade channel is harder to estimate. Experienced
bloodstock agents claim that physical inspection adds substantially to
pedigree-based valuation. Empirical studies suggest an additional 15-25% of
price variance is explained by conformation scores (Burns, Engle, and
Hennessy [2006]).

```math
C_{\rm parade} \approx 0.20 \cdot h^{\rm horse}_{\rm Kelly} \tag{2.4}
```

The confidence σ-algebra (CONFIDENCE.md) is critical here. Two buyers may
look at the same horse in the parade ring but extract very different amounts
of information. The experienced judge uses a fine σ-algebra (they can
distinguish 50 conformational categories). The novice uses a coarse
σ-algebra (they see "nice horse" or "not nice horse"). The effective channel
capacity for each buyer is:

```math
C^{(k)}_{\rm parade} = \rho^{(k)} \cdot C_{\rm parade} \tag{2.5}
```

where $\rho^{(k)}$ is buyer $k$'s confidence ratio. The experienced judge has
$\rho \approx 0.8$; the novice has $\rho \approx 0.1$.

---

## 3. The Fiber of Unrealised Potential

### 3.1 The shrinking fiber

A horse's fiber $F_t$ at time $t$ is the set of future outcomes consistent
with all information known at time $t$. The fiber shrinks monotonically as
information arrives:

```math
F_{\rm conception} \supsetneq F_{\rm foal} \supsetneq F_{\rm yearling} \supsetneq F_{\rm breeze} \supsetneq F_{\rm maiden} \supsetneq F_{\rm Group} \supsetneq F_{\rm retired} \tag{3.1}
```

At each stage, the channel capacity increases (less fiber = less uncertainty):

| Life stage | Fiber dimension | Channel capacity | Market event |
|:---|:---|:---|:---|
| Conception | $\sim r$ (everything unknown) | $\sim 0$ | Mating fee ≈ stud fee |
| Foal (at foot) | $\sim r - 3$ | $\sim 20\%$ | Foal sales (rare) |
| Yearling | $\sim r - 6$ | $\sim 35\%$ | Yearling sales (Magic Millions, Inglis, etc.) |
| 2-year-old (breeze-up) | $\sim r - 10$ | $\sim 55\%$ | Breeze-up sales |
| After maiden win | $\sim r - 12$ | $\sim 65\%$ | Horses-in-training sales |
| After Group win | $\sim r - 15$ | $\sim 80\%$ | Private sales, syndication |
| Retired to stud | $\sim 2\text{-}3$ | $\sim 90\%$ | Stud fee negotiations |
| 10 crops on ground | $\sim 0$ | $\sim 100\%$ | Market consensus |

**Theorem 3.1** (Fiber monotonicity). *The fiber dimension
$\dim(F_t)$ is monotonically non-increasing in time $t$ for any horse on the
characteristic manifold $M_{\rm horse}$. The channel capacity
$C_t = h^{\rm horse}_{\rm Kelly} - h^{\rm fiber_t}_{\rm Kelly}$ is
monotonically non-decreasing.*

*Proof.* Each new observation (race, trial, veterinary report) is a
projection that reduces the set of consistent futures. The filtration
$\mathcal{F}_{t}$ is non-decreasing. The fiber $F_t = \pi^{-1}(\mathcal{F}_{t})$
is non-increasing. The channel capacity, as the difference between total
entropy and fiber entropy, is non-decreasing. $\square$

### 3.2 The value at each stage

The price at each life stage is the expected value under the buyer's
confidence σ-algebra, discounted by the fiber uncertainty:

```math
P_t = \mathbb{E}[V_{\rm lifetime} | \mathcal{F}^{\rm conf}_{t}] \cdot e^{-\lambda \cdot \dim(F_t)} \tag{3.2}
```

where $V_{\rm lifetime}$ is the total lifetime value (prizemoney + breeding
value + sale value), $\mathcal{F}^{\rm conf}_{t}$ is the buyer's confidence
σ-algebra at time $t$, and $\lambda > 0$ is the risk premium per unit of
fiber dimension (the market's required compensation for uncertainty).

The risk premium $\lambda$ varies by market:
- Magic Millions (commercial sale, precocious types): $\lambda$ low
  (buyers accept uncertainty, hope for early runners)
- Tattersalls Book 1 (elite sale, classic types): $\lambda$ medium
  (buyers want quality but accept longer development)
- NZB Ready to Run (breeze-up, fiber already reduced): $\lambda$ high
  relative to residual fiber (but fiber is small, so total risk premium
  is moderate)

### 3.3 The pinhook as geometric arbitrage

A pinhooker buys a yearling at time $t_1$ and sells as a 2-year-old at
time $t_2 > t_1$. Their profit:

```math
\Pi_{\rm pinhook} = P_{t_2} - P_{t_1} - \text{Cost}(t_1, t_2) \tag{3.3}
```

In channel terms:

```math
\Pi_{\rm pinhook} = [C_{t_2} - C_{t_1}] \cdot V_{\rm avg} - \text{Cost}(t_1, t_2) \tag{3.4}
```

The pinhook is profitable when the VALUE of the fiber reduction (the
information produced by breaking, training, and trialling) exceeds the COST
of producing it.

**The pinhooker IS a relay in the ambient channel**
(MANIFOLD_IS_THE_CHANNEL.md Section 3.3). They sit between the yearling
market and the racing market, relaying information by shrinking the fiber.
Their profit is the relay capacity — the Willmore energy of the yearling
manifold's curvature in the information direction.

The best pinhookers are those with the highest relay capacity: they can
extract the most information per dollar of training cost. This is a function
of their confidence σ-algebra (CONFIDENCE.md) — experienced horsemen with
fine σ-algebras extract more information from the same training program.

---

## 4. The Sire Market

### 4.1 A stallion is a futures contract

A stallion's stud fee at the start of a breeding season is a price for
access to his genetic contribution. The fee is set by the stallion's owner
based on:
- Racing record (already resolved — in the base, not the fiber)
- Pedigree (already resolved)
- First-crop indicators (weanling/yearling inspection reports)
- Running crop results (if any crops are racing)
- Comparable stallions (market positioning)

The stud fee is effectively a FUTURES CONTRACT on the weighted average
performance of the stallion's progeny. The underlying asset is the stallion's
genetic value $G_{\rm sire}$, which is revealed progressively as crops race:

```math
\hat{G}_{\rm sire}(n) = \frac{\sum_{k=1}^{n} w_k \cdot \text{Performance}_{k}}{\sum_{k=1}^{n} w_k} \tag{4.1}
```

where $n$ is the number of crops, $\text{Performance}_{k}$ is the aggregate
performance of crop $k$ (winners-to-runners, stakes winners, Group winners,
average earnings index), and $w_k$ is the weight given to crop $k$ (more
recent crops may be weighted more heavily if breeding quality changes).

### 4.2 The information arrival rate

Each new crop that races delivers information about $G_{\rm sire}$. The
Fisher-Rao distance between successive estimates:

```math
d_{\rm FR}(\hat{G}(n), \hat{G}(n+1)) = \text{information in crop } n+1 \tag{4.2}
```

A "hot" young sire (e.g., his first crop dramatically outperforms
expectations): large $d_{\rm FR}$ — each crop delivers a lot of new
information, the stud fee adjusts rapidly. The channel capacity is high.

A proven sire (e.g., 10+ crops, statistics stable): small $d_{\rm FR}$ —
each new crop confirms what was already known. The channel is near capacity.
The stud fee is stable.

A "bust" sire (first crop underperforms): large $d_{\rm FR}$ in the
negative direction. The channel delivers bad news rapidly. The stud fee
collapses.

**Theorem 4.1** (Sire fee is a Bayesian posterior). *The optimal stud fee
at time $n$ (after $n$ crops have raced) is:*

```math
\text{Fee}(n) = \mathbb{E}[G_{\rm sire} | \text{crops } 1, \ldots, n] \cdot \frac{\text{mares}_{\rm demand}}{\text{mares}_{\rm supply}} \tag{4.3}
```

*where the expectation is the Bayesian posterior mean of $G_{\rm sire}$
given the observed performance of $n$ crops, multiplied by the supply-demand
ratio. The posterior variance (the residual fiber) decreases as $O(1/n)$
for independent crops.*

### 4.3 Shuttle stallions and the FX analogy

Elite stallions that shuttle between hemispheres (e.g., standing in Kentucky
August-February and in Hunter Valley February-August) create a direct
analogy with the FX market. The same stallion has:
- A Northern Hemisphere stud fee (in USD or GBP)
- A Southern Hemisphere stud fee (in AUD or NZD)

The ratio is NOT simply the exchange rate. It incorporates:
- Southern Hemisphere mares are (on average) of different quality
- Different racing programs reward different traits
- Different seasons mean different foaling dates and sale timings

The shuttle stallion IS a connected sum neck between the NH and SH bloodstock
manifolds:

```math
M_{\rm NH} \#_{\rm shuttle} M_{\rm SH} \tag{4.4}
```

The neck width (shuttle capacity) is limited by the stallion's fertility,
the logistics of transport, and quarantine regulations. When Australia
tightened quarantine rules, the neck narrowed — information flowed more
slowly between the hemispheres, and pricing inefficiencies between NH and SH
yearlings by the same sire persisted longer.

---

## 5. Race Day: The Conflagration of Variables

### 5.1 The race as a multi-fiber projection

A horse race is not a test of the horse alone. It is the simultaneous
projection of MULTIPLE manifolds through a single event — the 90 seconds
(or 3 minutes, or 6 minutes) from barrier to post. Every variable that
matters is a separate manifold, and the race result is the composition of
all their projections:

```math
\text{Result} = \pi_{\rm horse} \circ \pi_{\rm jockey} \circ \pi_{\rm trainer} \circ \pi_{\rm track} \circ \pi_{\rm barrier} \circ \pi_{\rm weight} \circ \pi_{\rm pace} \circ \pi_{\rm field} \tag{5.1}
```

Each projection has its own base (what you observe), its own fiber (what you
don't), and its own channel capacity (how much information it carries about
the outcome). The race is the COMPOSITION of eight channels — and by the
data processing inequality, the total information about the outcome is
limited by the NARROWEST channel in the chain.

### 5.2 The jockey manifold

A jockey is a point on $M_{\rm jockey}$ — a manifold of riding
characteristics:

| Factor | Dimension | Observable? | Information content |
|:---|:---|:---|:---|
| Weight (riding weight) | 1 | Yes (declared) | Low (everyone knows) |
| Fitness/strength | ~2 | Partially (recent rides) | Medium |
| Tactical skill | ~3 | Partially (replays, stats) | High |
| Affinity with horse type | ~2 | Poorly (requires deep analysis) | Very high |
| Track knowledge | ~2 | Partially (track stats) | Medium |
| Barrier skill (jump starts) | 1 | Partially | Medium-high |
| Pace judgement | ~2 | Poorly | Very high |
| Whip technique | 1 | Partially | Low-medium |
| Nerve under pressure | ~1 | Poorly (Group 1 record) | Very high in big races |

The effective dimension: $r_{\rm jockey} \approx 8\text{-}12$. Most of the
important factors (tactical skill, affinity with horse type, pace judgement,
nerve) are in the FIBER of public observation. You can see a jockey's
strike rate, but the strike rate is a lossy projection of the full jockey
manifold.

**The jockey-horse interaction is NOT separable.** A great jockey on the
wrong horse type produces a mediocre result. A moderate jockey on a horse
that suits their style produces an excellent result. In geometric terms:
the projection $\pi_{\rm jockey \times horse}: M_{\rm jockey} \times M_{\rm horse} \to M_{\rm result}$ is NOT the product of individual
projections. There is curvature in the interaction term — epistasis between
jockey and horse, analogous to genetic epistasis (Section 8).

**This is where the expert's σ-algebra pays.** A racing manager who
understands which jockeys suit which horses has a FINER σ-algebra on the
jockey-horse interaction manifold. They can distinguish "James McDonald on
a front-running sprinter" (excellent) from "James McDonald on a backmarker
needing cover" (still good, but different). The casual punter sees only the
jockey's name — a coarse projection that loses the interaction information.

### 5.3 The trainer manifold

A trainer is a point on $M_{\rm trainer}$:

| Factor | Observable? | Information content |
|:---|:---|:---|
| Strike rate (overall) | Yes | Low (publicly known) |
| Strike rate by class/distance/track | Partially | Medium |
| Preparation patterns (spacing, trials) | Yes (public form) | Medium-high |
| Stable condition (current form) | Partially (recent results) | High |
| Feeding/nutrition program | No (private) | Unknown but potentially high |
| Veterinary management | No (private) | High |
| Track work quality | Partially (clockers/reports) | Medium |
| Gear changes (blinkers, tongue tie) | Yes (declared) | Medium-high (signals intent) |
| First-up vs second-up vs peak | Yes (public form) | Very high |
| Confidence in the horse (betting moves) | Partially (market signals) | Very high |

The trainer's PREPARATION of the horse is the largest single fiber in the
racing projection — it contains information about the horse's current
fitness, soundness, and readiness that is largely invisible to the public.

**Gear changes are signals.** When a trainer adds blinkers, a tongue tie, or
cross-over nosebands, they are transmitting information through the public
channel. The gear change is a SIGNAL — a deliberately chosen act that reveals
something about the trainer's assessment. In our channel framework: a gear
change is the trainer increasing their channel capacity to the betting
market. The punter who ignores gear changes is ignoring a free channel.

**First-up patterns are palindromic.** Most trainers follow a cyclic
preparation: spell → trial → first-up → second-up → peak → decline → spell.
This cycle IS a palindrome on the preparation manifold. The horse gets fitter
(uphill), peaks, then gets tired (downhill — the mirror). A trainer who
consistently produces peak performances at a specific point in the cycle has
a highly palindromic preparation pattern — the second half of the cycle is
predictable from the first half. The punter who tracks the preparation
palindrome gets free information.

### 5.4 The track manifold

The track is NOT a neutral venue. It is a manifold of conditions that
interacts with every other variable:

| Factor | Range | Effect |
|:---|:---|:---|
| Distance | 800m–3200m | Determines which genotype wins (MSTN, Section 8.3) |
| Surface | Turf, dirt, synthetic | Different biomechanics, different form lines |
| Going (condition) | Firm → Good → Soft → Heavy | Massive effect; some horses gain 10+ lengths on soft |
| Track configuration | Straight, turning, undulating | Affects barrier draw value, pace shape |
| Rail position | True → +1m → +3m → +7m | Changes the effective distance by barrier |
| Altitude | Sea level → 2000m | Affects oxygen, stamina (important at some tracks) |
| Climate | Temperature, humidity, wind | Affects going, affects horse physiology |

**The going IS a coordinate on the Fisher-Rao simplex.** Going conditions
(Firm, Good, Soft, Heavy) define a simplex $\Delta_3$ of track states.
Each horse has a performance profile across going conditions — a function
$f: \Delta_3 \to \mathbb{R}$ mapping track state to expected performance.
The Fisher-Rao distance between two going conditions measures how DIFFERENT
the performance profiles are:

```math
d_{\rm FR}(\text{Good}, \text{Heavy}) \gg d_{\rm FR}(\text{Good}, \text{Firm}) \tag{5.2}
```

The distance from Good to Heavy is much larger than Good to Firm — because
heavy going changes the biomechanics radically (favouring strong, heavy
horses over light, fast ones), while the Good-to-Firm transition is more
moderate. The simplex captures this nonlinear structure.

**A track specialist has low fiber on that track.** A horse that consistently
performs well at Randwick (but not Flemington) has had its fiber reduced AT
RANDWICK by the accumulated data. At Flemington, the fiber is still large —
you don't know how it handles the different configuration. Track specialists
are horses whose characteristic manifold projects cleanly onto specific track
sub-manifolds.

### 5.5 The barrier draw

The barrier draw (starting position) is a discrete variable with enormous
impact — especially in sprint races and on tight-turning tracks.

The barrier draw effect IS a curvature on the race manifold. On a
perfectly fair track, barrier draw would have zero effect — the race manifold
would be flat in the barrier direction. On a real track, inside barriers
have an advantage (shorter path on turns) or a disadvantage (traffic,
kickback) depending on distance, pace, and rail position.

```math
\alpha_{\rm barrier}(k) = \mathbb{E}[\text{performance} | \text{barrier} = k] - \mathbb{E}[\text{performance}] \tag{5.3}
```

This is directly measurable from historical data. For a typical 1200m race
at Randwick: barrier 1 has $\alpha \approx +5\%$; barrier 12 has
$\alpha \approx -8\%$. The barrier effect is the CURVATURE of the race
manifold in the barrier direction — and by the Sharpe-curvature identity,
this curvature is exploitable alpha.

**The barrier draw is priced imperfectly.** The betting market adjusts for
barrier draw, but not enough (Ali [1977], Canfield, Fauman, and Ziemba
[1987]). The residual mispricing IS the mean curvature in the barrier
direction that the market has not yet flattened. This is a direct test of
our framework: the palindromic deficit of the barrier-conditioned return
sequence should be nonzero (non-palindromic) and proportional to the
barrier bias.

### 5.6 The weight manifold

In handicap races, the handicapper assigns weight to each horse based on
past performance — an explicit attempt to FLATTEN the race manifold.
The handicapper is performing mean curvature flow by hand: they observe
$\|H\| > 0$ (some horses are better than others) and add weight to reduce
the curvature (bringing the better horses closer to the others in expected
performance).

```math
w_i = w_{\rm base} + \lambda \cdot \text{rating}_{i} \tag{5.4}
```

where $\lambda$ is the weight-for-ratings scale (typically 0.5 kg per rating
point in Australia).

**The handicapper IS performing MCF.** The mean curvature of the race
manifold, without handicapping, is $\|H\|_{\rm raw} = \sigma_{\rm ability}$
(the standard deviation of ability across the field). After handicapping:

```math
\|H\|_{\rm handicapped} = \|H\|_{\rm raw} \cdot (1 - \rho_{\rm handicap}) \tag{5.5}
```

where $\rho_{\rm handicap}$ is the correlation between the handicapper's
weight assignment and true ability. A perfect handicapper
($\rho_{\rm handicap} = 1$) achieves $\|H\| = 0$ — a perfectly flat race
where every horse has equal chance. In practice, $\rho_{\rm handicap} \approx 0.6\text{-}0.8$ — good but not perfect, leaving residual curvature
(residual alpha) for astute punters.

**Weight-for-age races have no handicapping.** In WFA races (like the
Cox Plate, Melbourne Cup at WFA, or the Prix de l'Arc de Triomphe), the
manifold is NOT flattened. The curvature is the RAW ability difference.
These races produce the most reliable form — the winner beat the field on
merit, not on handicap. The information content of a WFA result is higher
than a handicap result (less noise from the handicapping projection).

### 5.7 The pace manifold

How the race is run — the distribution of energy over the distance — is
one of the most important and least observable variables.

| Pace shape | Description | Suits |
|:---|:---|:---|
| Fast early → slow late | Leader burns out | Closers, backmarkers |
| Slow early → fast late | Sprint finish | Horses with acceleration |
| Even pace | Sustained effort | Stamina horses, on-pacers |
| Muddling (variable) | No clear rhythm | Tactically adept horses/jockeys |

The pace of a race is determined by the FIELD — specifically by the
interaction of all horses' running styles. A race with three leaders and no
backmarkers will have fast early pace. A race with no leaders will have slow
early pace.

**The pace is a NASH EQUILIBRIUM on the field manifold.** Each jockey
chooses a position given the positions of the others. The resulting pace
shape is the Nash equilibrium of the positional game. This is a directed
graph on the field: the edges are "horse $i$ is in front of horse $j$" at
each point of the race, and the graph evolves dynamically.

**Pace modelling is the highest-value fiber in race analysis.** Most public
handicapping ignores pace (it's too hard to model). The few punters who
model pace effectively have a much finer σ-algebra — they can distinguish
"this horse will lead in a fast-paced race" from "this horse will lead in a
slow-paced race" — and the expected performance differs enormously between
these two states.

In our confidence framework: pace is in the fiber for most punters
($\rho_{\rm pace} \approx 0.1$ for the public) but in the base for expert
pace analysts ($\rho_{\rm pace} \approx 0.6\text{-}0.8$). The confidence gap
on pace is one of the largest exploitable edges in racing.

### 5.8 The field manifold: competitive interaction

A race is not a time trial. It is a COMPETITION — the result depends on
the other runners. The field manifold $M_{\rm field}$ encodes the
competitive structure:

```math
M_{\rm field} = \prod_{i=1}^{n} M^{(i)}_{\rm horse} / \sim \tag{5.6}
```

where $n$ is the field size and $\sim$ identifies configurations that
produce the same race dynamics (e.g., two midfield runners swapping
positions doesn't change the pace shape).

**The field size determines the effective manifold dimension.** A race
with 5 runners has a low-dimensional field manifold (few competitive
interactions). A race with 20 runners has a high-dimensional field manifold
(many interactions, many possible pace shapes, many barrier/traffic
scenarios).

```math
r_{\rm field} \approx \min(n - 1, r_{\rm horse} + r_{\rm jockey}) \tag{5.7}
```

The field manifold dimension is bounded by the number of runners minus one
(the competitive degrees of freedom) and by the sum of horse and jockey
dimensions (the total information available per runner).

**Class drop/rise is a connected-sum neck.** A horse dropping in class
(from Group 1 to Listed, or from city to provincial) is moving from one
sub-manifold of the field space to another. The connected-sum neck between
class levels has a width determined by how similar the competitive
environments are. A horse dropping from Group 1 to a Benchmark 72 handicap
is crossing a WIDE neck — the competitive environments are very different,
and the form line may not translate.

### 5.9 The conflagration: composing all projections

The race result is the composition of all eight projections:

```math
\pi_{\rm result}: M_{\rm horse} \times M_{\rm jockey} \times M_{\rm trainer} \times M_{\rm track} \times M_{\rm barrier} \times M_{\rm weight} \times M_{\rm pace} \times M_{\rm field} \to \{1, 2, \ldots, n\} \tag{5.8}
```

mapping the full state to a finishing order. The total dimension of the
input space is approximately:

```math
r_{\rm total} = r_{\rm horse} + r_{\rm jockey} + r_{\rm trainer} + r_{\rm track} + 1 + 1 + r_{\rm pace} + r_{\rm field}
```
```math
\approx 20 + 10 + 8 + 5 + 1 + 1 + 4 + 15 \approx 64 \tag{5.9}
```

But the output is a single ranking — a point on $\Delta_{n-1}$ (the
finishing order probabilities). The projection from a 64-dimensional input
to an $(n-1)$-dimensional output has an enormous fiber:

```math
\dim(F_{\rm race}) = 64 - (n-1) \approx 50 \tag{5.10}
```

**Fifty dimensions of information are LOST in the projection from the full
state to the race result.** This is why racing is hard to predict — not
because the variables are random, but because the projection is lossy. The
information is there (in the horse, the jockey, the trainer, the track, the
barrier, the weight, the pace, the field) but most of it lands in the fiber
and never reaches the result.

**The betting market IS the projection.** The odds for each horse are the
market's best estimate of $\pi_{\rm result}$ given the public σ-algebra.
The favourite-longshot bias (HORSE_RACING.md result (iii)) is the mean
curvature of this projection — the systematic direction in which the
market's lossy projection deviates from truth.

### 5.10 Where the edge lives

The exploitable edge in racing lives in the FIBER — the 50 dimensions that
the public projection doesn't capture. The most valuable fibers:

| Fiber | Typical public $\rho$ | Expert $\rho$ | Capacity gap |
|:---|:---|:---|:---|
| Pace (Section 5.7) | 0.1 | 0.7 | Very large |
| Jockey-horse interaction (Section 5.2) | 0.2 | 0.6 | Large |
| Trainer preparation pattern (Section 5.3) | 0.3 | 0.7 | Large |
| Going suitability (Section 5.4) | 0.4 | 0.8 | Moderate |
| Barrier × pace interaction | 0.1 | 0.5 | Large |
| Field composition effect (Section 5.8) | 0.2 | 0.5 | Moderate |
| Class transition (Section 5.8) | 0.3 | 0.6 | Moderate |

The total capacity gap between an expert and the public:

```math
\Delta C = \sum_{\rm fibers} (\rho_{\rm expert} - \rho_{\rm public}) \cdot C_{\rm fiber} \tag{5.11}
```

This is the expert's edge — measured in bits per race. An expert who
models pace, jockey-horse interaction, and preparation patterns has access
to approximately $0.5 \times 3 = 1.5$ bits of additional information per
race. Over a season of 1,000 bets, this is 1,500 bits — more than enough
to overcome the bookmaker's margin ($\Omega \approx 15\%$, costing
approximately 0.2 bits per race).

**The geometry explains why some punters consistently win.** It's not luck.
It's not cheating. It's a finer σ-algebra on the fibers that the public
market doesn't price. The expert has a wider lightcone — they see into
fibers that the market treats as noise.

---

## 6. Polo Ponies and the Alternative Disciplines

### 5.1 The projection onto the polo manifold

A polo pony is valued on a completely different projection of the
characteristic manifold. The key factors:

| Factor | Weight in flat racing | Weight in polo | Reason |
|:---|:---|:---|:---|
| Speed (top end) | Very high | Low | Polo is played at moderate pace |
| Acceleration (0-40km/h) | Moderate | Very high | Stop-start game |
| Agility (turning, stopping) | Low | Very high | Constant direction changes |
| Temperament (calmness) | Low | Very high | Must tolerate stick, ball, contact |
| Stamina (sustained effort) | Moderate | High | 6 chukkas of 7.5 minutes |
| Conformation (correctness) | High | Moderate | Less wear than racing |
| Pedigree (sire ranking) | Very high | Low | Performance matters, not bloodlines |
| Trainability | Moderate | Very high | Must learn complex game skills |
| Soundness | High | High | Both demand soundness |

The projection $\pi_{\rm polo}: M_{\rm horse} \to M_{\rm polo}$ has a large
fiber — most of what makes a racehorse valuable (speed, sire, precocity) is
IRRELEVANT for polo. Conversely, what makes a polo pony valuable
(temperament, agility, trainability) is largely in the fiber of the RACING
projection.

**This is why failed racehorses can become champion polo ponies.** A horse
at position $h \in M_{\rm horse}$ with $\pi_{\rm flat}(h)$ in the low-value
region of $M_{\rm flat}$ may have $\pi_{\rm polo}(h)$ in the high-value
region of $M_{\rm polo}$. The information that makes it worthless for racing
(slow, poor pedigree) is in the fiber of the polo projection and hence
irrelevant.

### 5.2 The polo market as a self-referential channel

The high-goal polo pony market (ponies for 6+ goal players) is one of the
most informationally inefficient markets on the characteristic manifold:

- **Tiny market:** Perhaps 500-1000 high-goal ponies traded globally per year
- **Extreme subjectivity:** Assessment depends on the player's style and handicap
- **No standardised reporting:** Unlike racing (times, ratings, prizemoney),
  polo has no objective performance metrics
- **Private transactions:** Most sales are private, not at auction
- **Relationship-driven:** The best ponies are sold through networks, not markets

In our framework: the polo market has very few observers ($N_{\rm observers}$
small), each with a different confidence σ-algebra, trading through private
channels (no public price discovery). The effective channel capacity is
extremely low:

```math
C_{\rm polo} \ll C_{\rm flat} \tag{5.1}
```

The Willmore energy is correspondingly high — the polo market is permanently
inefficient, like the art market (ART_MARKET.md). It is a pseudo-Anosov
market: intrinsic negative curvature makes $H = 0$ geometrically impossible.

### 5.3 Other disciplines

**Showjumping:** A moderate-efficiency market. Public competitions with
objective results (faults, time). Significant auction infrastructure
(Zangersheide, Performance Sales). Channel capacity moderate. The key
projection factors: scope (jumping ability), power, carefulness (avoidance
of poles), courage (willingness to jump difficult courses).

**Dressage:** Lower efficiency than showjumping. Subjective judging
introduces noise in the performance channel. The key projection factors:
movement quality (expression, cadence, elasticity), trainability, and
temperament. The market for Grand Prix-level horses is extremely thin.

**Eventing:** The broadest projection — eventing requires dressage,
showjumping, AND cross-country. The base of the eventing projection is
large (many factors matter) but the market is thin. Few horses can do all
three phases at elite level, so the supply is constrained.

**Racing to polo pipeline:** The most common inter-discipline flow.
Approximately 5-10% of retired flat racehorses go to polo. The neck
connecting $M_{\rm flat}$ to $M_{\rm polo}$ is moderately wide. The
retraining period (typically 6-12 months) is the neck length. The cost
of retraining is the observation cost for the relay.

---

## 7. The Geometry of Conformation Assessment

### 6.1 Conformation as a manifold

The space of possible conformations (body geometry) for a horse is a manifold
$M_{\rm conform} \subset M_{\rm horse}$. Key coordinates:

- Shoulder angle: $\theta_{\rm shoulder} \in [40°, 60°]$
- Pastern angle: $\theta_{\rm pastern} \in [45°, 60°]$
- Hip angle: $\theta_{\rm hip} \in [75°, 95°]$
- Back length: $\ell_{\rm back} \in [0.8, 1.2]$ (normalised to height)
- Cannon bone length: $\ell_{\rm cannon} \in [0.15, 0.25]$ (normalised)
- Chest width: $w_{\rm chest} \in [0.20, 0.35]$ (normalised)

These are not independent — they are constrained by biomechanics. A long back
typically correlates with a more horizontal shoulder angle. Short cannons
correlate with heavier bone.

The conformation manifold has dimension $r_{\rm conform} \approx 5\text{-}8$
(the number of independent conformational factors). The assessment of
conformation by a judge is a LOSSY PROJECTION from $M_{\rm conform}$ to a
low-dimensional score space — typically a single number ("I'd give him an 8
out of 10") or a verbal assessment ("beautiful type, a touch long in the back").

The Fisher-Rao distance between two horses' conformations:

```math
d_{\rm FR}(h_1, h_2) = 2\arccos\left(\sum_i \sqrt{c^{(1)}_{i} \cdot c^{(2)}_{i}}\right) \tag{6.1}
```

where $c^{(k)}_{i}$ is the normalised conformation vector of horse $k$. This
distance measures how DIFFERENTLY two horses are built, weighted by the
information content of each measurement.

### 6.2 The expert's σ-algebra vs the novice's

An expert conformation assessor distinguishes perhaps 50-100 conformational
features. Their σ-algebra on $M_{\rm conform}$ has $\sim 100$ atoms — each
atom is a conformational type they can reliably identify.

A novice distinguishes perhaps 5-10 features ("big horse, small horse,
pretty horse, ugly horse"). Their σ-algebra has $\sim 10$ atoms.

The expert's channel capacity from the parade ring:

```math
C^{\rm expert}_{\rm parade} = \log_2(100) \approx 6.6 \text{ bits per horse}
```

The novice's channel capacity:

```math
C^{\rm novice}_{\rm parade} = \log_2(10) \approx 3.3 \text{ bits per horse}
```

The expert extracts twice the information from the same 5-minute inspection.
This capacity difference, compounded over a career of buying hundreds of
horses, is the geometric source of the expert's edge.

---

## 8. The Genetic Manifold: DNA as Geometry

### 7.1 The genome is a point on a simplex

A horse's genome is a sequence of approximately 2.7 billion base pairs across
32 chromosome pairs. But the dimension that matters for performance is
vastly lower. Quantitative trait locus (QTL) studies in thoroughbreds
(Hill et al. [2010], Gu et al. [2009], Binns et al. [2010]) identify
perhaps 50-200 significant loci affecting speed, stamina, temperament,
and conformation. The myostatin gene (MSTN) alone — the "speed gene" —
explains approximately 18% of variance in optimal racing distance
(Hill et al. [2010]).

At each locus $\ell$, the horse has a pair of alleles (one from sire, one
from dam). For a biallelic locus with alleles $A$ and $a$, the genotype
frequency in the population defines a point on $\Delta_2$:

```math
p = (p_{AA}, p_{Aa}, p_{aa}), \qquad p_{AA} + p_{Aa} + p_{aa} = 1 \tag{7.1}
```

For a breed with $L$ relevant loci, the population's genetic state is a
point on the product simplex:

```math
\mathbf{p} = (p^{(1)}, p^{(2)}, \ldots, p^{(L)}) \in \prod_{\ell=1}^{L} \Delta_2^{(\ell)} \tag{7.2}
```

Under linkage equilibrium (loci evolving independently), this product space
IS the genetic manifold $M_{\rm genetic}$ — with the product Fisher-Rao
metric:

```math
g^{\rm FR} = \bigoplus_{\ell=1}^{L} g^{\rm FR}_{(\ell)} \tag{7.3}
```

where $g^{\rm FR}_{(\ell)}$ is the Fisher-Rao metric on the $\ell$-th locus
simplex. The total dimension is $\sum_\ell (\text{alleles at } \ell - 1) \approx L$
for biallelic loci.

### 7.2 Wright-Fisher IS Jacobi

The Wright-Fisher diffusion model for allele frequency evolution in a
population of effective size $N_e$ is:

```math
dp_i = p_i(f_i - \bar{f})\,dt + \sqrt{\frac{p_i(1-p_i)}{2N_e}}\,dW_i \tag{7.4}
```

where $p_i$ is the frequency of allele $i$, $f_i$ is its fitness, and
$\bar{f} = \sum_j p_j f_j$ is the population mean fitness.

**This IS the Jacobi diffusion on $\Delta_{d-1}$ from MARKET_PROCESSES.md.**
The identification:

| Wright-Fisher (genetics) | Jacobi diffusion (markets) | Identity |
|:---|:---|:---|
| Allele frequency $p_i$ | Portfolio weight $b_i$ | Same variable on $\Delta$ |
| Fitness $f_i$ | Expected return $\mu_i$ | Both drive drift toward optimal |
| Population size $N_e$ | Sample size $T$ | $\varepsilon^2 = 1/(2N_e) = 1/T$ |
| Selection $s$ | Alpha (excess return) | Drift toward higher-fitness alleles |
| Genetic drift | Estimation noise | Random fluctuations on $\Delta$ |
| Hardy-Weinberg equilibrium | Efficient market (H = 0) | Stationary distribution |
| Mutation | Exogenous shock / innovation | Perturbation to new region |
| Migration | Capital inflow from other markets | New alleles / new investors |
| Fixation (allele → 1) | Monopoly / market corner | Feller boundary absorption |

**This is not an analogy. It is the same equation.** The Fokker-Planck
equation for the Wright-Fisher diffusion is the same Fokker-Planck equation
we solve in FOKKER_PLANCK_CFD.md. The stationary distribution is the same
Jacobi polynomial measure. The spectral gap is the same first non-trivial
eigenvalue. The Bhattacharyya embedding maps the allele simplex to $S^{d-1}_{+}$
with the same curvature $K = 1/4$.

**Theorem 7.1** (Wright-Fisher = Market process). *The Wright-Fisher
diffusion for $d$ alleles at a single locus with selection coefficients
$(s_1, \ldots, s_d)$ in a population of effective size $N_e$ is identical
to the CAPM-type market process on $\Delta_{d-1}$ with expected returns
$(\mu_1, \ldots, \mu_d) = (s_1, \ldots, s_d)$ and diffusion parameter
$\varepsilon^2 = 1/(2N_e)$. Every result in this monograph about the Jacobi
diffusion on the portfolio simplex applies verbatim to allele frequency
evolution, and vice versa.*

### 7.3 The effective population size of the thoroughbred

Despite approximately 100,000 thoroughbred foals registered worldwide
annually, the effective population size is shockingly small. The reason:
a tiny number of stallions sire a disproportionate share of foals.

| Year | Top 5 sires (% of foals) | Top 20 sires (% of foals) | Estimated $N_e$ |
|:---|:---|:---|:---|
| 1970 | ~8% | ~25% | ~1,500 |
| 1990 | ~12% | ~35% | ~800 |
| 2010 | ~15% | ~45% | ~400 |
| 2024 | ~18% | ~50% | ~250-350 |

(Estimates from Cunningham et al. [2001], Todd et al. [2018], and extrapolation.)

The effective population size has been HALVING every 20-30 years. In our
framework, this means the diffusion parameter $\varepsilon^2 = 1/(2N_e)$
has been DOUBLING. The genetic manifold is becoming increasingly volatile.
Random genetic drift is overwhelmig selection at an accelerating rate.

In market terms: this is a market where the "number of observations" ($T$)
is falling while the volatility is rising. The MUP regret
$r \log T / (2T)$ is INCREASING — the market is getting HARDER to beat,
not easier, because the signal-to-noise ratio is deteriorating.

### 7.4 What this means for the breed

The consequences of small $N_e$ map directly from our theory:

**1. Loss of heterozygosity = approach to Feller boundary.**
As $N_e$ shrinks, rare alleles drift to fixation or loss. In our framework:
portfolio weights approach 0 or 1. The Fisher-Rao metric diverges:
$g_{ii} = 1/p_i \to \infty$ as $p_i \to 0$. The genetic manifold becomes
increasingly curved near the boundary. The breed becomes hypersensitive to
small perturbations in the remaining variable alleles.

Empirically: thoroughbred heterozygosity has declined approximately 10-15%
since 1970 (Todd et al. [2018]). Several alleles associated with soundness
and constitution are approaching fixation-loss — they are being bred out
not by selection against them but by genetic drift in a small population.

**2. Loss of genetic variance = shrinking manifold.**
The genetic manifold $M_{\rm genetic}$ is shrinking. As alleles fix, the
effective dimension $r_{\rm genetic}$ decreases — fewer independent genetic
directions remain variable. The manifold is collapsing toward a
lower-dimensional submanifold.

```math
\frac{dr_{\rm genetic}}{dt} \approx -\frac{r_{\rm genetic}}{2N_e} \tag{7.5}
```

This is the rate of dimension loss from drift alone (without selection or
mutation to counteract it). At $N_e = 300$, one effective genetic dimension
is lost every $\sim 600$ generations. A thoroughbred generation is $\sim 10$
years, so one dimension per $\sim 6,000$ years — seemingly slow, but the
breed is only $\sim 300$ years old ($\sim 30$ generations), and the
dimension loss accelerates as $N_e$ continues to fall.

**3. Inbreeding depression = Willmore energy rising.**
As the breed becomes more inbred, the Willmore energy of the genetic
manifold increases — the manifold becomes more curved, more distant from
the efficient (Hardy-Weinberg) surface. This curvature manifests as
inbreeding depression: reduced fitness, reduced fertility, increased
susceptibility to injury and disease.

The Sharpe-curvature identity applied to genetics: the "Sharpe ratio" of
a mating (the expected fitness gain per unit of fitness variance) equals
$\|H\|$ — the mean curvature of the genetic manifold at the population's
current position. As the manifold becomes more curved (higher Willmore
energy), the "Sharpe ratio" increases — but this is a BAD sign, because
it means the breed is far from the efficient surface and vulnerable to
sudden fitness collapse.

---

## 9. Inbreeding, Outcrossing, and the Exploration-Exploitation Tradeoff

### 8.1 Inbreeding as manifold exploitation

Inbreeding — mating related individuals — is a CONTRACTION of the genetic
manifold. The offspring's allele frequencies are pulled toward the parents'
shared alleles, reducing heterozygosity and moving toward the Feller boundary.

In portfolio terms: inbreeding is CONCENTRATION. You are doubling down on
the alleles you already have, accepting reduced diversity for increased
predictability.

The inbreeding coefficient $F$ measures how close you are to the boundary:

```math
F = 1 - \frac{H_{\rm observed}}{H_{\rm expected}} \tag{8.1}
```

where $H_{\rm observed}$ is the observed heterozygosity and $H_{\rm expected}$
is the expected heterozygosity under random mating. In our framework:

```math
F \propto \frac{d_{\rm FR}(p, \partial\Delta)^{-2}}{d_{\rm FR}(p_0, \partial\Delta)^{-2}} \tag{8.2}
```

where $\partial\Delta$ is the Feller boundary and $p_0$ is the ancestral
(fully outcrossed) population. Higher $F$ = closer to the boundary = more
concentrated portfolio = higher Fisher-Rao sensitivity to perturbations.

**Why breeders inbreed:** Inbreeding to a great ancestor (e.g., Northern
Dancer, Sadler's Wells, Danehill) is an attempt to REPLICATE a known-good
portfolio. The logic: "Northern Dancer was at a high-fitness point on
$M_{\rm genetic}$. By inbreeding to him, I move my offspring's allele
frequencies toward his, hoping to land near his position."

The problem: Northern Dancer's fitness depended on HETEROZYGOSITY at key
loci — the combination of different alleles from his sire and dam. Inbreeding
to him collapses that heterozygosity. You approach his position on the
allele simplex but by a route that loses the variance that MADE him great.
You are approaching the right point on the manifold but by a path that pushes
you through the Feller boundary.

### 8.2 Outcrossing as manifold exploration

Outcrossing — mating distantly related individuals — is an EXPANSION of the
genetic manifold. The offspring has high heterozygosity, sits far from the
Feller boundary, and occupies a potentially novel region of $M_{\rm genetic}$.

In portfolio terms: outcrossing is DIVERSIFICATION. You accept
unpredictability (large fiber) in exchange for access to new regions of the
manifold that may contain high-fitness points.

The MUP-Kelly tension applies directly:

| Strategy | Genetic version | Portfolio version | Risk profile |
|:---|:---|:---|:---|
| Pure exploitation | Tight inbreeding | Concentrated portfolio | Low variance, boundary risk |
| Pure exploration | Extreme outcross | Uniform portfolio | High variance, large fiber |
| Optimal | Moderate linebreeding | MUP (manifold-restricted) | Balanced |

The MUP (CONVERGENCE.md) is the optimal strategy: it concentrates on the
market manifold (restricting to proven genetic combinations) while
maintaining enough diversity to capture the full manifold dimension.
In breeding terms: the MUP breeder uses linebreeding (moderate inbreeding
to proven families) rather than tight inbreeding (which risks the Feller
boundary) or extreme outcrossing (which wastes the manifold structure).

### 8.3 The speed gene and the simplex

The myostatin gene (MSTN) provides a concrete example. The C/T polymorphism
at a specific locus determines racing aptitude:

| Genotype | Allele frequency (approx) | Optimal distance | Type |
|:---|:---|:---|:---|
| C/C | ~40% | Sprint (1000-1400m) | Speed |
| C/T | ~45% | Middle distance (1400-2000m) | Balanced |
| T/T | ~15% | Staying (2000m+) | Stamina |

The allele frequencies $(p_C, p_T)$ define a point on $\Delta_1$ (the 1-simplex
= the unit interval). The current thoroughbred population sits at approximately
$p_C \approx 0.63, p_T \approx 0.37$.

Selection for speed racing (which dominates the commercial market because
sprinters are precocious and sell well as yearlings) pushes $p_C$ upward.
Each generation:

```math
\Delta p_C \approx p_C p_T \cdot s_{\rm speed} + O(1/N_e) \tag{8.3}
```

where $s_{\rm speed}$ is the selective advantage of the C allele in the
commercial market. As $p_C$ increases, the breed loses staying ability.
The T/T genotype becomes rarer. In Fisher-Rao terms: the breed moves toward
the Feller boundary in the T direction.

**The market is driving the genetics.** Commercial incentives (yearling sale
prices favour speed) create selection pressure ($s_{\rm speed} > 0$) that
moves allele frequencies toward fixation of C. The market IS the selection
force. The Sharpe-curvature identity applied here: the "alpha" from breeding
sprinters is the mean curvature that pushes the genetic manifold toward the
C-fixation boundary.

This is a tragedy of the commons in geometric language. Each individual
breeder maximises their own Kelly rate by breeding for the commercial market
(sprinters). But the collective effect is to shrink the genetic manifold,
reduce $N_e$, increase $\varepsilon^2$, and accelerate the approach to the
Feller boundary — making the breed less fit in the long run.

### 8.4 Dominance, epistasis, and manifold curvature

**Dominance** — the nonlinear interaction between alleles at the same locus —
is CURVATURE of the fitness landscape on the allele simplex.

For a biallelic locus with fitness values $w_{AA}, w_{Aa}, w_{aa}$:
- No dominance ($w_{Aa} = (w_{AA} + w_{aa})/2$): the fitness landscape
  is LINEAR on $\Delta_1$. Zero curvature. The manifold is flat in this
  direction.
- Complete dominance ($w_{Aa} = w_{AA}$): the fitness landscape is KINKED.
  Nonzero curvature at the kink. The manifold bends.
- Overdominance ($w_{Aa} > \max(w_{AA}, w_{aa})$): the fitness landscape is
  CONCAVE. The heterozygote is fittest. The manifold curves TOWARD the
  interior of the simplex (away from the Feller boundary). This is the
  geometric mechanism of heterosis (hybrid vigour).

**Theorem 8.1** (Overdominance = interior-pointing curvature). *At a locus
with overdominance, the mean curvature vector $\vec{H}$ of the genetic
manifold points INWARD (toward the interior of the simplex). This creates a
geometric restoring force: selection pushes the population AWAY from the
Feller boundary and toward the heterozygous equilibrium.*

*This is the genetic version of the Jacobi restoring force from
MARKET_PROCESSES.md: the $b_i(1-b_i)$ volatility structure that prevents
the Jacobi diffusion from hitting the boundary.*

**Epistasis** — the nonlinear interaction between alleles at DIFFERENT
loci — is curvature of the genetic manifold in cross-locus directions. High
epistasis means the fitness of a genotype at locus A depends on the genotype
at locus B. In our framework: the genetic manifold is not a product manifold;
the loci are coupled. The off-diagonal terms of the Fisher information matrix
are nonzero.

This is why inbreeding is dangerous even when each individual locus looks
fine: the epistatic interactions create a curved manifold where the fitness
of the whole genome is NOT the sum of the fitnesses at individual loci.
Approaching the boundary at one locus can cause fitness collapse at another
locus through epistatic coupling — the geometric mechanism of inbreeding
depression.

### 8.5 RNA, epigenetics, and the time-varying manifold

The genetic manifold $M_{\rm genetic}$ defined by DNA is STATIC within a
horse's lifetime — the genome doesn't change. But the EXPRESSION of the
genome — which genes are active, at what level, in which tissues — is
regulated by RNA and epigenetic mechanisms (methylation, histone modification,
non-coding RNA). These mechanisms create a TIME-VARYING manifold:

```math
M_{\rm phenotype}(t) = \pi_{\rm expression}(M_{\rm genetic}, \text{environment}(t)) \tag{8.4}
```

The phenotype manifold is a PROJECTION of the genetic manifold, modulated by
the environment. The same genome produces different phenotypes depending on
nutrition, training, climate, and stress. The fiber of this projection is the
set of phenotypes compatible with the fixed genome.

In our self-referential channel framework (MANIFOLD_IS_THE_CHANNEL.md
Section 7): the horse's physiology is a self-referential channel. Gene
expression depends on the current phenotype (through feedback loops in
hormone regulation, neural adaptation, muscle development), which depends on
past gene expression, which depends on earlier phenotype. The epigenetic
state $\theta_t$ updates based on its own output:

```math
\theta_{t+1} = \Phi(\theta_t, \text{phenotype}_{t}) \tag{8.5}
```

This is exactly the self-referential channel of Definition 7.1 in
MANIFOLD_IS_THE_CHANNEL.md. The horse's development is a feedback loop
between genome and environment, mediated by RNA and epigenetics.

**Implication for breeding:** Two genetically identical horses (hypothetically)
raised in different environments will develop differently — they will be at
different points on the phenotype manifold even though they share the same
point on the genetic manifold. The environment is part of the channel. The
dam's uterine environment, the foal's early nutrition, the yearling's
handling — these are all INPUTS to the epigenetic channel that shape the
phenotype from the genotype.

**Implication for sale assessment:** A yearling's current phenotype
(what you see in the parade ring) reflects BOTH the genome AND the
epigenetic history. Two yearlings with the same genome but different
upbringing will present differently. The expert judge who reads "this horse
was well raised" from its condition and development is implicitly estimating
the epigenetic channel — a remarkably sophisticated inference from a
5-minute observation.

---

## 10. The Breed as an Evolving Market

### 9.1 Three timescales

The thoroughbred breed operates on three distinct timescales, each with its
own geometric dynamics:

**Fast (months-years): Individual horse assessment.** The fiber of a single
horse shrinks as information arrives: yearling → 2yo → stakes horse. This is
the timescale of the auction market, the pinhook, the racing career.

**Medium (decades): Breeding fashion and selection.** Allele frequencies
shift as breeders select for commercial traits. The genetic manifold deforms.
New sire lines rise, old lines decline. The MSTN allele frequency drifts.
The effective population size changes. This is the timescale of the stud
market, the sire championship, the breed structure.

**Slow (centuries): Breed evolution.** The breed's position on the species
manifold shifts. Thoroughbreds become taller, faster, more fragile. The
Feller boundary is approached. Genetic diseases accumulate. The breed's
long-term fitness trajectory is determined. This is the timescale of breed
management, genetic conservation, and the question of whether the
thoroughbred is sustainable.

### 9.2 The breed as a market approaching the Feller boundary

The Feller boundary theory from MARKET_PROCESSES.md and
HAMILTONIAN_TAILS_COMPLETENESS.md has a precise application here. The Jacobi
restoring force $b_i(1 - b_i)$ keeps the process in the interior of the
simplex — provided the "reflecting" boundary condition holds.

For the thoroughbred breed, the boundary condition depends on heterozygote
advantage (overdominance). At loci with overdominance: the boundary is
reflecting — the breed bounces back from fixation-loss. At loci without
overdominance (or with directional selection favouring one allele): the
boundary is ABSORBING — once an allele is lost, it is gone forever.

The thoroughbred Stud Book is a CLOSED SYSTEM — no genetic material enters
from outside the breed (unlike most livestock breeds, which allow grading-up
from other breeds or wild populations). In our framework: the breed is a
market with no capital inflows. The total "capital" (genetic diversity) can
only decrease. This is unlike equity markets, where new IPOs and innovation
inject new securities.

**Theorem 9.1** (Closed breed approaches Feller boundary). *A closed breeding
population with effective size $N_e$ and no mutation or migration loses
heterozygosity at rate:*

```math
\frac{dH}{dt} = -\frac{H}{2N_e} \tag{9.1}
```

*The expected time to fixation-loss of an allele with frequency $p_0$ is:*

```math
t_{\rm fix} \approx -4N_e \cdot [(1-p_0)\log(1-p_0) + p_0 \log p_0] \tag{9.2}
```

*For $N_e = 300$ and $p_0 = 0.15$ (the approximate frequency of the T/T
staying allele at MSTN): $t_{\rm fix} \approx 480$ generations $\approx 4,800$
years. The breed is not in immediate danger but is on a trajectory that,
without intervention, leads to fixation-loss of multiple alleles associated
with soundness, fertility, and constitutional vigor.*

### 9.3 What can be done (geometrically)

The geometric framework suggests three interventions:

**1. Increase $N_e$.** Restrict the number of mares per stallion. Currently
a popular stallion may cover 200+ mares per year. Limiting this to 100 or
150 would roughly double $N_e$, halving the rate of diversity loss. In
market terms: prevent monopoly. Diversify the supply side.

**2. Open the Stud Book.** Allow limited introduction of genetic material
from other breeds (as the Irish Sport Horse Stud Book allows, or as various
warmblood studbooks allow). This is capital injection — new alleles entering
the market. It is deeply controversial in thoroughbred racing.

**3. Use genomic selection to maintain diversity.** Instead of selecting
purely for racing speed (which drives $p_C \to 1$ at MSTN), select for a
portfolio of traits including soundness, fertility, and constitution. This
is the MUP approach: optimise across the MANIFOLD of desirable traits
rather than along a single direction. The MUP regret bound guarantees that
this diversified selection strategy loses at most $r \log T / (2T)$ relative
to the Kelly-optimal strategy — a negligible cost for maintaining breed
viability.

---

## 11. The Burrows-Wheeler Transform and Genomic Filtrations

### 10.1 BWT as a context-sorting filtration

The Burrows-Wheeler Transform (BWT) (Burrows and Wheeler [1994]) is a
reversible string transformation that rearranges a sequence so that
characters with similar contexts cluster together. Given a string $s$ of
length $n$, the BWT:

1. Forms all $n$ cyclic rotations of $s$
2. Sorts them lexicographically
3. Takes the last column of the sorted matrix

The result is a permutation of $s$ in which characters that are preceded by
the same context (suffix) are adjacent. This clustering enables superior
compression (BWT + move-to-front + entropy coding achieves near-optimal
compression rates).

**In our framework, the BWT is a filtration sorter.** The FILTRATIONS.md
result establishes that any grammar-based compressor maintains a set of
"seen phrases" that form the atoms of a filtration. The BWT goes further:
it SORTS the sequence by filtration atom. Characters in the same BWT run
belong to the same context = the same Voronoi cell = the same filtration
atom.

### 10.2 Application to genetic sequences

A horse's genome is a string $s \in \{A, C, G, T\}^{2.7 \times 10^9}$.
The BWT of this string clusters nucleotides by their genomic context:
regions of similar sequence context (e.g., regulatory regions, coding
regions, repetitive elements) appear as runs in the BWT output.

Modern genomic alignment tools — BWA (Li and Durbin [2009]), Bowtie
(Langmead et al. [2009]) — use the FM-index (a compressed BWT) to align
short reads to the reference genome. In our framework, this alignment IS
filtration membership testing: given a new observation (a short read), which
Voronoi cell (genomic context) does it belong to?

**Theorem 10.1** (BWT filtration of the genome). *The BWT of a genetic
sequence $s$ defines a filtration $\mathcal{F}^{\rm BWT}$ on the sequence
space. The atoms of $\mathcal{F}^{\rm BWT}$ are the BWT runs — maximal
subsequences of characters sharing the same context. The number of runs
$r_{\rm BWT}$ measures the complexity of the sequence:*

```math
r_{\rm BWT}(s) = |\{\text{maximal runs in BWT}(s)\}| \tag{10.1}
```

*For a maximally random sequence: $r_{\rm BWT} \approx n$ (every character
is its own run — no context structure). For a highly structured sequence:
$r_{\rm BWT} \ll n$ (long runs of shared context — highly compressible).*

### 10.3 Genetic complexity and market complexity

The BWT run count $r_{\rm BWT}$ of a horse's genome measures its
**genetic complexity** — how many distinct genomic contexts exist. This
connects to our framework through three identities:

**1. BWT runs ↔ Voronoi cells.** The number of BWT runs in the genetic
sequence is analogous to the number of Voronoi cells on the market manifold.
More runs = finer partition = more information resolved.

**2. BWT compression ratio ↔ LZ complexity rate.** The BWT compression
ratio converges to the same entropy rate as LZ78 (they are both
asymptotically optimal for stationary ergodic sources). So the BWT
compression of the genome gives the same information rate as the LZ
complexity, which equals $h_{\rm Kelly}$ of the underlying process
(FILTRATIONS.md, INFORMATION_THEORY.md).

**3. FM-index queries ↔ filtration membership.** Querying the FM-index
("does pattern $P$ occur in $s$?") is deciding whether an observation belongs
to a specific filtration atom. The query time is $O(|P|)$ — independent of
genome length. This is the computational efficiency that BWT brings: once
the filtration is built, membership testing is fast.

### 10.4 Comparing horses via BWT distance

Two horses' genomes $s_1, s_2$ can be compared via BWT-derived distances.
The BWT edit distance — the minimum number of operations to transform
$\text{BWT}(s_1)$ into $\text{BWT}(s_2)$ — measures how different their
genomic CONTEXTS are (not just their raw sequences).

**Definition 10.2** (BWT-Fisher distance). *Define the BWT-Fisher distance
between two genomes as:*

```math
d_{\rm BWT\text{-}FR}(s_1, s_2) = d_{\rm FR}(\hat{p}_{1}, \hat{p}_{2}) \tag{10.2}
```

*where $\hat{p}_{k}$ is the empirical distribution of BWT run lengths for
genome $k$, and $d_{\rm FR}$ is the Fisher-Rao distance on the simplex of
run-length distributions.*

This distance measures how differently the two genomes are STRUCTURED —
not just how many SNPs differ (which is the Hamming distance), but how
different their context patterns are. Two horses with similar BWT-Fisher
distance have similar genomic architecture even if they differ at many
individual SNPs.

### 10.5 The BWT of the market return sequence

The BWT applies not only to genetic sequences but to market return sequences
— closing the loop between bloodstock genetics and market geometry.

Discretise the market return sequence into symbols using the Voronoi
partition (as in test 15V from the experiments): each day's return vector is
assigned to a Voronoi cell, producing a symbolic sequence
```math
\sigma = (\sigma_1, \sigma_2, \ldots, \sigma_T) \in \{1, \ldots, N\}^{T}.
```

The BWT of $\sigma$ sorts trading days by their factor context. Days in
the same BWT run experienced the same market regime. The number of BWT runs
measures the market's regime complexity:

```math
r_{\rm BWT}(\text{market}) = \text{number of distinct regime contexts} \tag{10.3}
```

A market with few regimes (stable CAPM): $r_{\rm BWT}$ small, high
compression, low entropy. A market with many regime changes (crisis-prone,
pseudo-Anosov): $r_{\rm BWT}$ large, low compression, high entropy.

**This connects genetics and markets through the same compression framework.**
The BWT of a genome and the BWT of a market return sequence are the same
mathematical operation — applied to different sequences on different
alphabets, but both measuring the complexity of the underlying process via
context-sorted filtrations.

### 10.6 The Chen-Fox-Lyndon factorisation: a canonical decomposition

The BWT sorts by context but does not decompose the sequence into canonical
units. For that, we need the **Chen-Fox-Lyndon theorem** (Chen, Fox, and
Lyndon [1958]).

**Definition 10.3** (Lyndon word). *A string $\ell$ over an ordered alphabet
is a **Lyndon word** if it is strictly smaller (lexicographically) than every
proper rotation of itself. Equivalently, $\ell$ is primitive (not a power of
a shorter string) and is the lexicographically smallest rotation of itself.*

Examples over $\{A, C, G, T\}$ with $A < C < G < T$:
- $A$, $C$, $G$, $T$ are Lyndon words (single characters)
- $AC$, $ACG$, $ACGT$ are Lyndon words
- $AA$, $CC$, $ACAC$ are NOT Lyndon words (they are powers)

**Theorem 10.4** (Chen-Fox-Lyndon). *Every finite string $w$ has a unique
factorisation into a non-increasing sequence of Lyndon words:*

```math
w = \ell_1 \ell_2 \cdots \ell_k, \qquad \ell_1 \geq_{\rm lex} \ell_2 \geq_{\rm lex} \cdots \geq_{\rm lex} \ell_k \tag{10.4}
```

*This factorisation is canonical — it depends only on the string and the
alphabet ordering. It is computable in $O(n)$ time (Duval [1983]).*

The beauty: this factorisation is **bijective**. The string $w$ and its
Lyndon factorisation $(\ell_1, \ldots, \ell_k)$ carry exactly the same
information. No compression, no lossy projection, no arbitrary choices.
The factorisation IS the string, viewed through the lens of its irreducible
structure.

### 10.7 Lyndon words as irreducible market patterns

Apply the Chen-Fox-Lyndon factorisation to a discretised market return
sequence $\sigma = (\sigma_1, \ldots, \sigma_T)$ over the Voronoi alphabet
$\{1, \ldots, N\}$. Each Lyndon factor $\ell_j$ is an **irreducible market
pattern** — a minimal sequence of regime transitions that cannot be
decomposed into repetitions of shorter patterns.

**Example.** Suppose the Voronoi alphabet is $\{1, 2, 3, 4\}$ (four market
regimes: bull, bear, crisis, recovery). A return sequence might factorise as:

```math
\underbrace{1234}_{\ell_1} \underbrace{123}_{\ell_2} \underbrace{12}_{\ell_3} \underbrace{12}_{\ell_4} \underbrace{1}_{\ell_5} \underbrace{1}_{\ell_6}
```

Each Lyndon factor is an irreducible market cycle. The longest factors
($\ell_1 = 1234$: a full four-regime cycle) appear first. As the sequence
progresses, the Lyndon factors shorten — the market visits fewer regimes
per cycle. The non-increasing property $\ell_1 \geq \ell_2 \geq \cdots$ is
a structural constraint: the market's "narrative complexity" can only
decrease within a Lyndon factorisation.

### 10.8 The Lyndon-Lie connection

The deepest connection: **Lyndon words form a basis for the free Lie algebra
$\mathrm{Lie}(A)$ over the alphabet $A$.** This is the Shirshov-Lyndon
theorem (Shirshov [1958], Chen-Fox-Lyndon [1958]).

The free Lie algebra over an alphabet is the algebra generated by the
letters under the Lie bracket $[x, y] = xy - yx$. Its dimension in degree
$n$ is given by the necklace polynomial:

```math
\dim(\mathrm{Lie}_{n}(A)) = \frac{1}{n}\sum_{d | n} \mu(d) \cdot |A|^{n/d} \tag{10.5}
```

where $\mu$ is the Möbius function.

**For the market:** The Lyndon words over the Voronoi alphabet are the
generators of the Lie algebra of market dynamics. The Lie bracket
$[\ell_1, \ell_2] = \ell_1 \ell_2 - \ell_2 \ell_1$ captures the
**non-commutativity of market regimes** — the fact that a bull followed by
a bear is fundamentally different from a bear followed by a bull. This
non-commutativity is the Lie-algebraic content of the braid group structure
from BRAIDS.md.

**For the FX market (FOREIGN_EXCHANGE.md):** The Lie algebra of FX is
generated by the three factors (dollar, carry, risk). The Lyndon words over
$\{D, C, R\}$ are the irreducible FX patterns. The Chen-Fox-Lyndon
factorisation of the FX return sequence decomposes it into these
Lie-algebraic generators — connecting the compression-theoretic view
(BWT, LZ78) to the algebraic view (Lie groups, braid groups).

**For the genome:** The Lyndon words over $\{A, C, G, T\}$ are the
irreducible genetic motifs. The Chen-Fox-Lyndon factorisation of a genome
decomposes it into these motifs. The number and distribution of Lyndon
factors measures the Lie-algebraic complexity of the genome — how many
independent "directions" of genetic variation exist.

### 10.9 The bijective transform connecting genetics and markets

We now have a complete bijective chain:

```math
\text{String } w \xrightarrow{\text{CFL}} (\ell_1, \ldots, \ell_k) \xrightarrow{\text{BWT}} \tilde{w} \xrightarrow{\text{MTF+RLE}} \text{compressed}
```

Each step is reversible. The chain applies identically to:

1. **A genome** $s \in \{A, C, G, T\}^{n}$: CFL decomposes into irreducible
   genetic motifs; BWT sorts by genomic context; compression measures
   genetic complexity.

2. **A market return sequence** $\sigma \in \{1, \ldots, N\}^{T}$: CFL
   decomposes into irreducible market patterns; BWT sorts by market regime;
   compression measures market entropy (= Kelly rate).

3. **A pedigree** (encoded as a string over the sire/dam alphabet): CFL
   decomposes into irreducible genetic lineages; BWT sorts by ancestral
   context; compression measures pedigree diversity.

The bijective transform is the SAME mathematical object applied to three
different sequences. This is the deepest connection between genetics and
market geometry: **the combinatorial structure of a genome, a market, and a
pedigree are all instances of the same Lyndon-BWT factorisation on different
alphabets.**

**Theorem 10.5** (Lyndon-BWT-market identity). *The Chen-Fox-Lyndon
factorisation of a Voronoi-discretised return sequence decomposes the market
history into irreducible patterns (Lyndon words) that generate the free Lie
algebra of market dynamics. The number of distinct Lyndon factors $k$ equals
the dimension of the Lie algebra truncated at the longest factor length.
The BWT of the sequence sorts these factors by their context, and the
compression ratio converges to $h_{\rm Kelly}$ — the same entropy rate
measured by the LZ78 filtration (FILTRATIONS.md).*

### 10.10 Practical applications

**For breeders:** BWT-based genomic comparison can identify mating
combinations whose genomes have complementary context structure — i.e.,
the offspring's genome will have high BWT complexity (many distinct contexts
= high heterozygosity in functional regions). This is a principled
alternative to inbreeding coefficient: instead of measuring raw
homozygosity, measure CONTEXT diversity via BWT runs.

**For buyers at sales:** As genetic testing becomes standard (Equinome,
Plusvital, and newer panels), BWT-derived metrics could supplement
traditional pedigree analysis. The BWT-Fisher distance between a yearling
and successful racehorses measures structural genomic similarity, not just
SNP matching.

**For the market:** The BWT complexity of the bloodstock market return
sequence (yearling prices over time) measures the regime complexity of the
auction market. High BWT complexity → many pricing regimes → inefficient
market. Low BWT complexity → few regimes → more predictable.

---

## 12. Market Efficiency Across Horse Markets

### 7.1 The efficiency hierarchy

| Market | Observers | Data quality | Liquidity | Willmore energy | Market type |
|:---|:---|:---|:---|:---|:---|
| US flat racing (Keeneland) | Very high | Excellent | High | Low | Near-CAPM |
| Australian flat (Magic Millions) | High | Good | Moderate-high | Moderate | CAPM |
| European flat (Tattersalls) | High | Good | Moderate | Moderate | CAPM |
| NH jumps (Cheltenham) | Moderate | Moderate | Moderate | Moderate-high | Transitional |
| Showjumping | Low-moderate | Moderate | Low | High | Pseudo-Anosov |
| Polo | Very low | Poor | Very low | Very high | Pseudo-Anosov |
| Dressage | Low | Moderate | Very low | Very high | Pseudo-Anosov |

The efficiency of each horse market is determined by the observation cost
hierarchy (MANIFOLD_IS_THE_CHANNEL.md Section 9.2):

- **US flat racing:** Cheap data (free race replays, public Beyer figures),
  many expert observers, liquid auction market. The yearling market approaches
  CAPM efficiency: sire-based pricing is near-correct, and deviations from
  sire-based pricing are small and short-lived.

- **Polo ponies:** Expensive data (must see horse played in person), few
  expert observers, private transactions. The polo market is permanently
  pseudo-Anosov: the Willmore energy is bounded away from zero by the
  observation cost floor.

### 7.2 The rise of data in bloodstock

The bloodstock market is undergoing a data revolution:
- Stride analysis (Trakus, RaceWatch) provides objective biomechanical data
- Genetic testing (Equinome, Plusvital) provides speed/stamina gene profiles
- AI-assisted conformation scoring (emerging technology)
- Real-time veterinary imaging (dynamic respiratory endoscopy)

Each new data source adds a channel to the observation hierarchy, increasing
the effective capacity and reducing the fiber. The Fisher-Rao distance
between the pre-data and post-data characteristic manifolds measures the
information gain:

```math
d_{\rm FR}(M_{\rm pre\text{-}data}, M_{\rm post\text{-}data}) = \text{value of the new data} \tag{7.1}
```

Buyers who adopt new data sources first gain a temporary information advantage
— a wider lightcone (LIGHTCONE_OF_PRICE.md) — until the rest of the market
adopts. At that point, the advantage moves to the CONFIDENCE σ-algebra:
everyone has the data, but not everyone has the expertise to interpret it.

---

## 13. New Results

**Theorem BM1** (Characteristic manifold). The space of horses is a manifold
$M_{\rm horse}$ of dimension $r \approx 15\text{-}25$ with Fisher-Rao
metric $g^{\rm FR}_{ij} = \delta_{ij}/h_i$, where $h_i$ is the normalised
characteristic weight.

**Theorem BM2** (Fiber monotonicity). The fiber dimension is monotonically
non-increasing as information about the horse arrives. Channel capacity is
monotonically non-decreasing.

**Theorem BM3** (Discipline projection). Each equestrian discipline defines
a projection $\pi_{\rm discipline}: M_{\rm horse} \to M_{\rm discipline}$.
The same horse has different values under different projections. A horse
worthless for flat racing may be valuable for polo because the relevant
factors lie in different fibers.

**Theorem BM4** (Pinhook = relay). The pinhooker is a relay in the ambient
channel between the yearling market and the racing market. Their profit
equals the relay capacity minus the cost of producing the information.

**Theorem BM5** (Sire fee = posterior mean). The optimal stud fee is the
Bayesian posterior mean of the stallion's genetic value, with residual
fiber decreasing as $O(1/n)$ in the number of crops.

**Theorem BM6** (Shuttle stallion = connected sum). A shuttle stallion
creates a connected sum neck between the NH and SH bloodstock manifolds.
Quarantine restrictions narrow the neck, reducing channel capacity and
allowing pricing inefficiencies to persist.

**Theorem BM7** (Wright-Fisher = Market process). The Wright-Fisher
diffusion for allele frequencies IS the Jacobi diffusion on the portfolio
simplex, with $\varepsilon^2 = 1/(2N_e)$. Every result about the Jacobi
process applies verbatim to allele frequency evolution.

**Theorem BM8** (Overdominance = interior curvature). At a locus with
heterozygote advantage, the mean curvature vector points inward — creating
a geometric restoring force away from the Feller boundary. This is the
genetic analogue of the Jacobi restoring force $b_i(1-b_i)$.

**Theorem BM9** (Closed breed approaches Feller boundary). A closed
breeding population with effective size $N_e$ loses heterozygosity at rate
$dH/dt = -H/(2N_e)$. The thoroughbred ($N_e \approx 300$) is on a
trajectory toward fixation-loss of alleles associated with soundness and
constitution.

**Theorem BM10** (BWT filtration of the genome). The BWT of a genetic
sequence defines a filtration whose atoms are BWT runs (maximal subsequences
sharing the same context). The number of runs $r_{\rm BWT}$ measures genetic
complexity, analogous to the number of Voronoi cells on the market manifold.

---

## 14. Open Problems

**OP-BM1** (Empirical characteristic manifold). Estimate $r_{\rm horse}$
empirically from yearling sale data. Use the same three estimators as for
equities (stable rank, FNN, Grassberger-Procaccia) applied to the catalogue
+ result data from 10 years of Magic Millions sales.

**OP-BM2** (Conformation scoring efficiency). Compare expert conformation
scores with AI-based conformation scoring. Measure the Fisher-Rao distance
between expert and AI assessments. If AI achieves higher channel capacity
from photos than experts achieve from live inspection, the expert edge
in conformation assessment will erode.

**OP-BM3** (Pinhook profitability and fiber reduction). Estimate the
average fiber reduction achieved by pinhooking (the information gain from
yearling to 2-year-old) and compare to pinhook profits. The prediction:
pinhook profit should be proportional to $\Delta C = C_{2\rm yo} - C_{\rm yearling}$
minus training costs.

**OP-BM4** (Sire market efficiency). Test whether stud fee adjustments
are efficient: does $d_{\rm FR}(\text{Fee}(n), \text{Fee}(n+1))$ decrease
as $O(1/\sqrt{n})$ (consistent with Bayesian updating), or do stud fees
overreact to recent crops (mean curvature in the time direction)?

**OP-BM5** (Cross-discipline information flow). Measure the channel
capacity of the racing-to-polo pipeline. How much of a horse's polo value
is predictable from its racing record? This is $C_{\rm flat \to polo} =
H(M_{\rm polo}) - H(M_{\rm polo} | M_{\rm flat})$.

**OP-BM6** (The optimal inspection time). Given the channel capacity of
the parade ring ($C_{\rm parade}$), how long should a buyer inspect each
horse? The CFL condition (OBSERVERS_AND_CHANNELS.md) gives a minimum
inspection time below which the observation is too coarse to be useful.
Is this consistent with the observed 3-5 minute inspection times at sales?

---

## 15. Conclusion

The bloodstock market is a uniquely rich testing ground for the geometric
theory of markets. It has:
- A well-defined characteristic manifold with observable coordinates
- Massive information asymmetry (vendor vs buyer) quantifiable as fiber dimension
- Temporal resolution of uncertainty (yearling → 2yo → stakes horse → stallion)
- Multiple discipline-specific projections of the same underlying manifold
- Connected sums between hemispheres (shuttle stallions) and between
  disciplines (retraining)
- A clear observation cost hierarchy from catalogue buyers to major syndicates
- Public auction data for calibration

A yearling in the Magic Millions parade ring IS a point on a manifold with a
large fiber. The 5-minute inspection IS a channel with limited capacity.
The expert judge's advantage IS a finer confidence σ-algebra. The pinhooker
IS a relay in the ambient channel. The stud fee IS a Bayesian posterior.
And the polo pony that was once a failed racehorse IS an inter-market
arbitrage — the same point on $M_{\rm horse}$, repriced under a different
projection.

Every concept in the monograph — the manifold, the channel, the fiber, the
σ-algebra, the connected sum, the relay, the lightcone — has a concrete,
testable interpretation in the bloodstock market. This is the geometry of
efficient markets applied to the most ancient market of all: the market for
a good horse.

*"All you need for happiness is a good gun, a good horse, and a good wife."*
— Daniel Boone

*We can now say: all you need is a point on $M_{\rm horse}$ with small fiber,
a fine σ-algebra, and a reliable channel.*

---

## References

1. G. A. Akerlof, "The market for 'lemons': Quality uncertainty and the
   market mechanism," *Quarterly Journal of Economics* 84(3) (1970), 488–500.

2. B. Chezum and B. Wimmer, "Roses or lemons: Adverse selection in the market
   for thoroughbred yearlings," *Review of Economics and Statistics* 79(3)
   (1997), 521–526.

3. S. S. Vickner and S. F. Koch, "Hedonic pricing, information, and the
   market for thoroughbred yearlings," *Journal of Agribusiness* 19(2)
   (2001), 173–189.

4. W. A. Burns, R. F. Engle, and D. A. Hennessy, "Hedonic price estimation
   of thoroughbred yearlings: A Bayesian approach," *Applied Economics* 38
   (2006), 1075–1089.

5. T. M. Cover, "Universal portfolios," *Mathematical Finance* 1(1) (1991),
   1–29.

6. S. Harville, "Assigning probabilities to the outcomes of multi-entry
   competitions," *Journal of the American Statistical Association* 68(342)
   (1973), 312–316.

7. E. W. Hill, J. Gu, S. S. Eivers, R. G. Fonseca, B. A. McGivney,
   P. Govindarajan, N. Orr, L. M. Katz, and D. E. MacHugh, "A sequence
   polymorphism in MSTN predicts sprinting ability and racing stamina in
   thoroughbred horses," *PLoS ONE* 5(1) (2010), e8645.

8. E. P. Cunningham, J. J. Dooley, R. K. Splan, and D. G. Bradley,
   "Microsatellite diversity, pedigree relatedness and the contributions of
   founder lineages to thoroughbred horses," *Animal Genetics* 32(6)
   (2001), 360–364.

9. E. T. Todd, P. C. Thomson, and N. A. Hamilton, "The genomic architecture
   of inbreeding and its consequences in the thoroughbred horse," *Genetics*
   211(4) (2018), 1459–1472.

10. M. Burrows and D. J. Wheeler, "A block-sorting lossless data compression
    algorithm," Technical Report 124, Digital Equipment Corporation (1994).

11. H. Li and R. Durbin, "Fast and accurate short read alignment with
    Burrows-Wheeler transform," *Bioinformatics* 25(14) (2009), 1754–1760.

12. B. Langmead, C. Trapnell, M. Pop, and S. L. Salzberg, "Ultrafast and
    memory-efficient alignment of short DNA sequences to the human genome,"
    *Genome Biology* 10(3) (2009), R25.

13. K.-T. Chen, R. H. Fox, and R. C. Lyndon, "Free differential calculus,
    IV. The quotient groups of the lower central series," *Annals of
    Mathematics* 68(1) (1958), 81–95.

14. J.-P. Duval, "Factorizing words over an ordered alphabet," *Journal of
    Algorithms* 4(4) (1983), 363–381.

15. A. I. Shirshov, "On free Lie rings," *Matematicheskii Sbornik* 45(87)
    (1958), 113–122.

---

*This paper is part of the monograph "The Geometry of Efficient Markets."
Cross-references: HORSE_RACING_SPORTS_BETTING_GAMBLING.md (racetrack as
financial market, Kelly on horses); ART_MARKET.md (permanently inefficient
markets, pseudo-Anosov); MANIFOLD_IS_THE_CHANNEL.md (channel-manifold
identity, fiber bundle as channel, relay capacity, self-referential channel);
CONFIDENCE.md (confidence σ-algebra, observation hierarchy);
OBSERVERS_AND_CHANNELS.md (shared filtrations, CFL condition);
LIGHTCONE_OF_PRICE.md (information advantage as wider lightcone);
FOREIGN_EXCHANGE.md (connected sums between markets, shuttle = cross-listing);
INTERMARKET_GEOMETRY.md (connected sums, neck width);
FILTRATIONS.md (LZ78, BWT, grammar-based compressors as filtrations);
MARKET_PROCESSES.md (Jacobi diffusion = Wright-Fisher);
FOKKER_PLANCK_CFD.md (Fokker-Planck on the simplex);
INFORMATION_THEORY.md (entropy rate = Kelly rate).*
