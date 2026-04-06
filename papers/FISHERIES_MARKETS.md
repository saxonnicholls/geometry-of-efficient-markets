# The Geometry of Fisheries Markets:
## Quotas, Commons, Coupled Simplices, and the Market
## That Created the Geometry

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VI.7** — Accessible

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
A fishery is two simplices coupled by a directed graph. The **quota simplex**
$\Delta^Q_{d-1}$ allocates shares of the Total Allowable Catch (TAC) among
$d$ licence holders: $q = (q_1, \ldots, q_d)$, $\sum q_i = 1$, $q_i \geq 0$.
The **population simplex** $\Delta^P_{s-1}$ describes the species composition
of the fish stock: $p = (p_1, \ldots, p_s)$, $\sum p_j = 1$, $p_j \geq 0$.
The coupling: what you're allowed to catch (quota) determines what you do
catch (harvest), which determines what survives (population next period),
which determines what's available to catch (future quota value). This is a
self-referential channel (MANIFOLD_IS_THE_CHANNEL.md): the channel rewires
itself from its own output.

This paper develops the geometric theory of fisheries within the framework
of the monograph, using Australia's Southern Bluefin Tuna (SBT) fishery
as the central case — a fishery the author watched from infancy in Port
Lincoln, South Australia, and which in many ways generated the intuitions
that became this monograph.

**Principal results:**

**(i) The quota IS a portfolio.** An Individual Transferable Quota (ITQ)
giving the right to catch $q_i$ tonnes of species $j$ is a portfolio weight
on the quota simplex. The Fisher-Rao metric at position $q$ is
$g^{\rm FR}_{ij}(q) = \delta_{ij}/q_i$ — the same metric, the same geometry,
the same theory. A large quota holder is insensitive to small changes (low
$g_{ii}$). A marginal operator with a tiny quota is hypersensitive (high
$g_{ii}$). The quota market IS a financial market on a simplex.

**(ii) The fish stock is a Wright-Fisher population.** The population simplex
evolves under a modified Wright-Fisher diffusion with harvest:

$$dp_j = p_j(r_j - \bar{r} - h_j)\,dt + \sqrt{\frac{p_j(1-p_j)}{2N_e}}\,dW_j$$

where $r_j$ is the natural growth rate of species $j$, $\bar{r}$ is the mean
growth rate, $h_j$ is the harvest rate, and $N_e$ is the effective population
size. This IS the Jacobi diffusion from MARKET_PROCESSES.md with a harvest
term. Every result about the Jacobi process — spectral gap, Feller boundary,
detailed balance, palindromic structure — applies to the fish stock.

**(iii) The tragedy of the commons is a Feller boundary problem.** Open-access
fishing (no quotas) sets $h_j$ proportional to the fishing effort, which is
proportional to the stock size $p_j$ (fishermen target abundant species).
This creates a POSITIVE FEEDBACK: fishing reduces stock, reduced stock is
still fished, stock collapses. In geometric terms: the harvest pushes the
population simplex toward the Feller boundary ($p_j \to 0$ for
over-harvested species). At the boundary, the Jacobi restoring force
$p_j(1-p_j)$ goes to zero — the species cannot recover. Extinction is
ABSORBING. The tragedy of the commons is the market approaching the Feller
boundary with no restoring force.

**(iv) The ITQ system creates a restoring force.** By capping total harvest
at the TAC and distributing quotas, the ITQ system constrains
$\sum h_j \leq H_{\rm TAC}$. If the TAC is set below the maximum
sustainable yield, the constraint keeps the population away from the Feller
boundary. The quota system IS a geometric intervention: it imposes a
REFLECTING boundary condition on the population simplex, replacing the
absorbing boundary of open access.

**(v) The Port Lincoln tuna farming revolution is a non-palindromic break.**
Before 1991, SBT fishing in Port Lincoln was catch-and-sell — a palindromic
cycle (fish → sell → fish → sell). In 1991, fishermen began ranching
wild-caught juveniles in sea pens, fattening them on pilchards, and
exporting to the Japanese sashimi market at 10-100× the price of fresh-caught
tuna. This was a topological change: the manifold of the fishery acquired a
new dimension (time-in-pen), a new projection (sashimi quality vs fresh
quality), and a new connected-sum neck to the Japanese market. The directed
graph CHANGED. No amount of palindromic analysis of the pre-1991 fishery
would have predicted the post-1991 fishery. It was a Type II reverse
singularity — the creation of a new market.

**(vi) The coupled directed graph.** The fishery is a directed graph on TWO
simplices connected by harvest and stock assessment edges:

$$\Delta^Q \xrightleftharpoons[\text{stock assessment}]{\text{harvest}} \Delta^P$$

The quota simplex influences the population simplex (through harvest). The
population simplex influences the quota simplex (through stock assessment,
which sets the TAC, which determines quota values). This feedback IS the
self-referential channel. The equilibrium of the coupled system — the
Maximum Sustainable Yield (MSY) — IS the palindromic fixed point where
forward dynamics equal reverse dynamics and the directed graph is effectively
undirected.

**Keywords.** Fisheries; quota; ITQ; Southern Bluefin Tuna; Port Lincoln;
commons; Feller boundary; Wright-Fisher; harvest; population dynamics;
coupled simplex; directed graph; palindromic; self-referential channel;
MSY; TAC; tuna farming; aquaculture.

**MSC 2020.** 91B76, 92D25, 91G10, 60J70, 53A10, 05C20, 94A15.

---

## 1. Two Simplices

### 1.1 The quota simplex

Consider a fishery with $d$ licence holders (individuals, companies, or
cooperatives) and a Total Allowable Catch (TAC) of $H$ tonnes. Each licence
holder $i$ owns quota $Q_i$ tonnes, with $\sum_{i=1}^d Q_i = H$. The
normalised quota vector:

$$q = \left(\frac{Q_1}{H}, \ldots, \frac{Q_d}{H}\right) \in \Delta_{d-1} \tag{1.1}$$

is a point on the quota simplex. This IS a portfolio: $q_i$ is the fraction
of the total resource allocated to holder $i$.

The Fisher-Rao metric on the quota simplex:

$$g^{\rm FR}_{ij}(q) = \frac{\delta_{ij}}{q_i} \tag{1.2}$$

A holder with a large share ($q_i$ large) is insensitive to small changes in
quota allocation — they have a secure position. A holder with a tiny share
($q_i$ small) is hypersensitive — a small change in their allocation is a
large fraction of their livelihood. This IS the same observer-dependence as
OBSERVERS_AND_CHANNELS.md: the market looks different depending on where you
stand.

### 1.2 The population simplex

The fish stock consists of $s$ species (or age classes within a single
species) with abundances $(N_1, \ldots, N_s)$. The normalised abundance:

$$p = \left(\frac{N_1}{N_{\rm total}}, \ldots, \frac{N_s}{N_{\rm total}}\right) \in \Delta_{s-1} \tag{1.3}$$

is a point on the population simplex. For a single-species fishery managed
by age class (juveniles, sub-adults, adults, spawners), $s$ is the number
of age classes. For a multi-species fishery, $s$ is the number of species.

The population simplex also carries the Fisher-Rao metric:

$$g^{\rm FR}_{jk}(p) = \frac{\delta_{jk}}{p_j} \tag{1.4}$$

Species (or age classes) at low abundance have high metric sensitivity —
small changes in their numbers are disproportionately important. This is
ecologically correct: a species near extinction is infinitely more
"informative" (in the Fisher sense) than an abundant species.

### 1.3 The coupling

The two simplices are coupled by two maps:

**Harvest map** $\mathcal{H}: \Delta^Q \times \Delta^P \to \Delta^P$. Given
the quota allocation $q$ and current population $p$, the harvest map
determines the post-harvest population:

$$p' = \mathcal{H}(q, p) = \frac{p - h(q, p)}{1 - \|h(q, p)\|_1} \tag{1.5}$$

where $h(q, p)$ is the harvest vector (how much of each species/age class
is removed). The harvest depends on the quota (what you're allowed to catch)
AND the population (what's available to catch).

**Stock assessment map** $\mathcal{S}: \Delta^P \to \mathbb{R}_+$. The stock
assessment estimates the population state and recommends a TAC:

$$H_{\rm TAC} = \mathcal{S}(p) \tag{1.6}$$

A lower population triggers a lower TAC, which reduces quota values. A higher
population triggers a higher TAC, which increases quota values. The TAC IS
the channel capacity of the fishery: the maximum sustainable information
extraction rate.

---

## 2. The Wright-Fisher Dynamics of Fish Stocks

### 2.1 The population process

Between harvest events, the fish population evolves under birth, death,
growth, and stochastic environmental variation. For a single-species fishery
with $s$ age classes, the population dynamics on $\Delta_{s-1}$ are:

$$dp_j = p_j\left(r_j(p) - \bar{r}(p) - h_j\right)dt + \sqrt{\frac{p_j(1-p_j)}{2N_e}}\,dW_j \tag{2.1}$$

where:
- $r_j(p)$ = per-capita growth rate of age class $j$ (depends on total
  population through density dependence)
- $\bar{r}(p) = \sum_k p_k r_k(p)$ = population mean growth rate
- $h_j$ = harvest rate of age class $j$
- $N_e$ = effective population size
- $dW_j$ = environmental stochasticity

**This IS the Jacobi diffusion** from MARKET_PROCESSES.md with a harvest term.
The identification (extending BLOODSTOCK_MARKETS.md Theorem BM7):

| Wright-Fisher (fishery) | Jacobi (market) |
|:---|:---|
| Age-class frequency $p_j$ | Portfolio weight $b_j$ |
| Growth rate $r_j$ | Expected return $\mu_j$ |
| Harvest rate $h_j$ | Transaction cost / dividend extraction |
| Effective population $N_e$ | Sample size $T$ |
| Density dependence | Factor interaction |
| Environmental noise | Market volatility |
| Feller boundary ($p_j = 0$: extinction) | Feller boundary ($b_j = 0$: delisting) |
| Maximum Sustainable Yield | Kelly rate $h_{\rm Kelly}$ |

### 2.2 The MSY as the Kelly rate

The Maximum Sustainable Yield (MSY) is the largest harvest that can be
sustained indefinitely:

$$H_{\rm MSY} = \max_{h} \sum_j h_j p_j \quad \text{subject to} \quad \bar{r}(p) - \bar{h} \geq 0 \tag{2.2}$$

**Theorem 2.1** (MSY = Kelly rate). *The MSY of a fishery is the Kelly
growth rate of the population simplex:*

$$H_{\rm MSY} = h_{\rm Kelly}(\Delta^P) \tag{2.3}$$

*The MSY-achieving harvest policy is the Kelly-optimal strategy: it maximises
the long-run sustainable extraction rate, analogous to the Kelly criterion
maximising long-run wealth growth.*

*Proof sketch.* The MSY is the maximum rate at which biomass can be
extracted without driving the population to extinction. The Kelly rate is the
maximum rate at which wealth can be extracted from a market without
bankruptcy. Both are the supremum of a long-run growth rate over feasible
strategies, constrained to remain in the interior of the simplex (away from
the Feller boundary). The mathematical structure — maximise a concave
functional on $\Delta$ subject to a non-negativity constraint — is
identical. $\square$

**Consequence:** Overfishing ($H > H_{\rm MSY}$) IS overbetting ($f > f^{\ast}_{\rm Kelly}$). Both lead to ruin — extinction of the stock or
bankruptcy of the portfolio. The geometry forbids it: the Feller boundary
absorbs, and there is no recovery.

### 2.3 The Feller boundary and species extinction

At the Feller boundary ($p_j = 0$ for some $j$), the species or age class
is extinct. The diffusion coefficient $\sqrt{p_j(1-p_j)/(2N_e)}$ goes to
zero — no noise can bring it back. The boundary is ABSORBING.

**The tragedy of the commons in geometric language:** Without quotas, each
fisher maximises their individual harvest rate $h_j^{(i)}$ given their
expectation of others' harvest. The Nash equilibrium harvest exceeds the MSY:
$H_{\rm Nash} > H_{\rm MSY}$. The population is driven toward the Feller
boundary. Each fisher is "over-Kelly" — betting more than the optimal
fraction, guaranteeing eventual ruin.

In the palindromic framework (FILTRATIONS.md Section 11): open-access
fishing breaks the palindromic symmetry of the population dynamics.
Without harvest, the population has detailed balance — good years and bad
years cancel over time, the stock fluctuates palindromically around its
carrying capacity. With excessive harvest, the palindromic symmetry is
broken: the directed graph acquires a systematic bias toward lower
population. The palindromic deficit $\delta = H - H_{\rm MSY}$ IS the
overfishing rate.

---

## 3. The ITQ System as Geometric Intervention

### 3.1 What the quota does

An Individual Transferable Quota (ITQ) system:
1. Sets a Total Allowable Catch ($H_{\rm TAC} \leq H_{\rm MSY}$)
2. Allocates quota shares $q_i$ to licence holders ($\sum q_i = 1$)
3. Allows quota to be traded (bought, sold, leased)

The geometric effect: **the ITQ replaces the absorbing Feller boundary
with a reflecting boundary.** The TAC constraint keeps total harvest below
MSY, which keeps the population away from $p_j = 0$. The Jacobi restoring
force $p_j(1 - p_j)$ remains positive. The population bounces back from
perturbations instead of collapsing.

**Theorem 3.1** (ITQ = reflecting boundary). *Under an ITQ system with
$H_{\rm TAC} \leq H_{\rm MSY}$, the modified population process on
$\Delta_{s-1}$ has a reflecting boundary condition at a positive distance
from the Feller boundary:*

$$p_j \geq p_{\rm min}(H_{\rm TAC}) > 0 \quad \text{for all } j \tag{3.1}$$

*The minimum population fraction $p_{\rm min}$ is determined by the TAC: a
lower TAC gives a larger $p_{\rm min}$ (more conservative, further from
extinction). The reflecting boundary ensures the population process is
ergodic — it returns to equilibrium after perturbations.*

### 3.2 The quota market as a financial market

Once quotas are tradeable, they ARE a financial market. The quota price
$P_i$ reflects the present value of the right to catch $q_i$ fraction of
the TAC in perpetuity:

$$P_i = \sum_{t=0}^{\infty} \frac{\mathbb{E}[q_i \cdot H_{\rm TAC}(t) \cdot \text{price}_{\rm fish}(t)]}{(1+\delta)^t} \tag{3.2}$$

where $\delta$ is the discount rate.

The quota market has all the structure of the monograph:
- **Fisher-Rao metric** on the quota simplex
- **Mean curvature** measuring inefficiency (mispriced quotas)
- **Spectral gap** measuring how fast information is incorporated
- **Palindromic structure** (seasonal fishing cycles)
- **Non-palindromic breaks** (TAC changes, stock assessments, regulatory
  interventions)

For Australia's SBT fishery, the quota market is a well-defined financial
market with:
- ~100 quota holders (the $d$ dimension)
- Annual TAC set by CCSBT (Commission for the Conservation of Southern
  Bluefin Tuna)
- Active trading of quota (lease and permanent transfer)
- Quota prices of A\$3,000-10,000 per tonne (varying with TAC and tuna
  market price)

### 3.3 Three fishery management regimes

| Regime | Harvest rule | Boundary condition | Geometric type | Palindromic? |
|:---|:---|:---|:---|:---|
| Open access | $h = \max$ (no limit) | Absorbing (extinction) | Pseudo-Anosov | No (ruin) |
| TAC only | $h \leq H_{\rm TAC}$ | Reflecting (aggregate) | Transitional | Partially |
| ITQ | $h_i = q_i H_{\rm TAC}$ | Reflecting (individual) | CAPM | Yes (equilibrium) |

The ITQ system pushes the fishery toward CAPM-type dynamics: the quota
market processes information, the population is stabilised, the system
approaches palindromic equilibrium. Open access is pseudo-Anosov: chaotic,
non-palindromic, doomed to the Feller boundary.

---

## 4. The Port Lincoln Case: Southern Bluefin Tuna

### 4.1 Before quotas (pre-1984)

Port Lincoln, South Australia. The largest town on the Eyre Peninsula.
Economy: fishing, farming, and the desert beyond. The Southern Bluefin Tuna
(SBT, *Thunnus maccoyii*) fishery was the town's lifeblood.

Before 1984: open access. Any licensed fisher could catch as much SBT as
they could find. The fleet grew. The catch peaked at 21,000 tonnes in 1961.
By 1982, the stock had collapsed to an estimated 10-15% of its unfished
biomass. The directed graph of the fishery was non-palindromic: the stock
declined year after year with no recovery. The Feller boundary — extinction
of the spawning stock — was approaching.

In the language of the monograph: the fishery was in a pseudo-Anosov phase.
The palindromic deficit was large and growing. The Sharpe ratio of
"investing" in the fishery (catching tuna year after year) was high but
unsustainable — it was the mandatory alpha of a permanently inefficient
market (ART_MARKET.md), except that the inefficiency was self-liquidating.
You were eating the principal.

### 4.2 The quota revolution (1984)

In 1984, the Australian government introduced ITQs for SBT. The initial TAC
was set at 14,500 tonnes (Australia's share of the global TAC agreed with
Japan and New Zealand). Quotas were allocated to existing fishers based on
catch history.

**The geometric effect was immediate.** The directed graph acquired a
reflecting boundary. The absorbing Feller boundary was replaced by the TAC
constraint. The population process became ergodic.

But the deeper effect was on the QUOTA SIMPLEX. Overnight, a fishing licence
— previously worth nothing beyond the right to fish — became a TRADEABLE
ASSET with a capitalised value. The quota itself became the market. Fishers
who wanted to exit could sell quota to those who wanted to expand. The quota
market developed its own price dynamics, its own spectral gap, its own
approach to efficiency.

**The quota IS a financial instrument.** It is a perpetual right to a share
of a renewable resource, analogous to a perpetual dividend-paying stock. The
"dividend" is $q_i \times H_{\rm TAC} \times P_{\rm tuna}$ per year (your
share of the catch, times the market price per tonne). The quota price
capitalises the future dividend stream.

### 4.3 The tuna farming revolution (1991-)

In 1991, Port Lincoln fishermen began a practice that changed the
manifold permanently: instead of killing wild-caught SBT, they towed them
alive in sea pens back to the Port Lincoln coast, fattened them on pilchards
for 3-6 months, and sold the fattened fish to the Japanese sashimi market
at vastly higher prices.

Before farming: whole SBT sold for A\$2-5/kg (fresh/frozen commodity).
After farming: fattened SBT sold for A\$20-80/kg (sashimi grade, exported
to Tsukiji/Toyosu market in Tokyo).

**This was a topological transition — a Type II reverse MCF singularity.**
The manifold of the fishery acquired a new dimension: TIME IN PEN.
Previously, the only variable was QUOTA (how much you can catch). Now
there were two: quota AND farming capacity (how many pens, how many
pilchards, how long to fatten).

The directed graph CHANGED:

Before 1991:
```
Catch → Sell → Catch → Sell   (palindromic cycle)
```

After 1991:
```
Catch → Pen → Fatten → Grade → Export → Catch → ...   (new directed graph)
```

The new graph had:
- More nodes (catch, pen, fatten, grade, export)
- More edges (each transition is a separate market operation)
- A new connected-sum neck to the Japanese market (the export channel)
- Higher Kelly rate (more value extracted per unit of quota)

The palindromic analysis of the pre-1991 fishery was USELESS for predicting
the post-1991 fishery. The symmetry had been broken not by a crisis but
by INNOVATION — the creation of an entirely new dimension of the manifold.

### 4.4 Port Lincoln today

Port Lincoln is now the "tuna capital of the world" and one of the
wealthiest per-capita towns in Australia. The SBT farming industry generates
approximately A\$300-500 million annually. SBT quota is worth
A\$5,000-10,000 per tonne. The total quota for Australia is approximately
6,000 tonnes, making the total quota asset value approximately
A\$30-60 million.

The quota market is a functioning financial market on $\Delta_{d-1}$ with
$d \approx 100$ holders. It has:
- A spectral gap (quota prices adjust to TAC changes within weeks)
- Palindromic seasonal structure (fishing season = catching season = farming
  season, repeated annually)
- Non-palindromic shocks (TAC changes, stock assessment surprises,
  Japanese market shifts)
- A connected-sum neck to the global tuna market (through the export channel)

### 4.5 What Port Lincoln teaches about market geometry

The SBT fishery demonstrates every major concept in the monograph:

| Concept | SBT fishery manifestation |
|:---|:---|
| Simplex | Quota simplex $\Delta_{d-1}$ |
| Fisher-Rao metric | Large holders are insensitive; small holders are hypersensitive |
| Feller boundary | Stock extinction (pre-quota) |
| Reflecting boundary | ITQ system (post-quota) |
| Wright-Fisher = Jacobi | Fish population dynamics on $\Delta_{s-1}$ |
| Kelly rate = MSY | Maximum sustainable extraction |
| Palindromic equilibrium | Seasonal fishing cycle |
| Non-palindromic break | Tuna farming revolution |
| Type II reverse singularity | Creation of farming dimension |
| Connected sum neck | Export channel to Japan |
| Self-referential channel | Harvest → population → stock assessment → TAC → quota value → harvest |
| Directed graph | The complete structure of the fishery |
| Confidence σ-algebra | Fishermen's assessment of stock health |
| Observation cost | Stock assessment surveys (expensive) |
| Insider information | Fishermen know the stock better than scientists |

---

## 5. Other Fisheries Cases

### 5.1 The Icelandic cod fishery

Iceland's cod quota system (ITQs introduced 1984) provides a contrasting case:

- Cod stocks collapsed in the early 1990s despite quotas
- The TAC was set too high ($H_{\rm TAC} > H_{\rm MSY}$) due to political
  pressure
- The reflecting boundary was too close to the Feller boundary — the
  "buffer zone" was insufficient
- Recovery required a severe TAC reduction in the late 1990s

**Geometric diagnosis:** The TAC was set in the confidence σ-algebra of
politicians, not scientists. The politicians' σ-algebra was coarser (they
distinguished only "good for jobs" and "bad for jobs"). The scientists'
σ-algebra was finer (they could distinguish stock levels at higher
resolution). The political override of the scientific assessment was a
coarsening of the effective σ-algebra — exactly the confidence collapse
mechanism from CONFIDENCE.md.

### 5.2 The Chilean abalone fishery

Chile's abalone (*loco*) fishery introduced Territorial User Rights (TURFs)
rather than ITQs: fishing communities were assigned AREAS of the coast
rather than shares of the catch.

In our framework: TURFs are a different partitioning of the simplex. ITQs
partition by SHARE (the quota simplex). TURFs partition by SPACE (a
Voronoi-like partition of the coastline). The TURF system creates a
spatial directed graph — each community manages its own area, and the
connections between areas (through larval dispersal, adult migration) are
the edges.

The TURF system is geometrically more complex (it involves spatial
structure that ITQs average out) but potentially more robust (spatial
structure provides natural reflecting boundaries — a depleted area can be
recolonised from neighbours).

### 5.3 The global tuna market

The global market for bluefin tuna connects three simplices:

| Simplex | Coordinates | Dimension |
|:---|:---|:---|
| Quota simplex (Australia) | SBT quota shares | $d \approx 100$ |
| Quota simplex (Japan) | Pacific Bluefin quota shares | $d \approx 50$ |
| Auction simplex (Tsukiji/Toyosu) | Buyer shares of auction lots | $d \approx 200$ |

These are connected by trade — the connected-sum structure:

$$M_{\rm SBT}^{\rm Aus} \#_{\rm export} M_{\rm tuna}^{\rm Japan} \#_{\rm auction} M_{\rm buyer}^{\rm Toyosu}$$

The neck widths are determined by:
- Export regulations (Australia → Japan: customs, health certification)
- Transport capacity (refrigerated container shipping)
- Auction rules (Toyosu market procedures)

The first tuna of the year at Toyosu auction (the *hatsu-seri*) regularly
sells for millions of dollars — a non-palindromic event driven by cultural
significance rather than food value. The directed graph of the tuna market
has edges that no purely economic model would predict.

---

## 6. Coupled Simplices and the Fishery Feedback Loop

### 6.1 The formal coupling

The fishery feedback loop is a map between the two simplices:

$$\Phi: \Delta^Q \times \Delta^P \to \Delta^Q \times \Delta^P \tag{6.1}$$

$$(q, p) \mapsto (q', p')$$

where:
- $p' = \mathcal{G}(\mathcal{H}(q, p))$ — harvest the population, then let it
  grow for one period
- $q'$ is determined by the TAC $\mathcal{S}(p')$ applied to the quota
  allocation (TAC change affects all quota values proportionally, or
  differentially if some quotas are adjusted)

**Theorem 6.1** (Fishery fixed point). *The coupled system $(q, p)$ has a
fixed point $(q^{\ast}, p^{\ast})$ where:*

$$\mathcal{H}(q^{\ast}, p^{\ast}) = \text{MSY harvest at } p^{\ast} \tag{6.2}$$
$$\mathcal{S}(p^{\ast}) = H_{\rm MSY} \tag{6.3}$$

*At the fixed point: the harvest equals the MSY, the TAC equals the MSY, the
population is at the MSY equilibrium, and the quota market is in palindromic
equilibrium. This is the state where the coupled directed graph is
effectively undirected — forward and reverse are equally likely.*

### 6.2 The self-referential structure

The fishery is a self-referential channel (MANIFOLD_IS_THE_CHANNEL.md
Definition 7.1):

- The channel is the population process $p_t \to p_{t+1}$
- The channel's parameters (growth rates $r_j$, carrying capacity) depend on
  the CURRENT population (density dependence)
- The harvest $h_j$ depends on the quota allocation, which depends on past
  population assessments, which depend on past harvests

The channel rewires itself from its own output. The equilibrium IS the
rational expectations equilibrium: the price of quota reflects the expected
future catch, which depends on the expected future population, which depends
on the expected future harvest, which depends on the price of quota.

The incompleteness of fisheries management (the fact that scientists cannot
perfectly predict stock recovery) IS the native incompleteness of the
self-referential channel (MANIFOLD_IS_THE_CHANNEL.md Theorem MC4). The
fishery cannot fully predict its own future because its future depends on
its current predictions.

---

## 7. UNCLOS, the Donut Hole, and the Geometry of Ocean Jurisdiction

### 7.1 The ocean as a partitioned simplex

The United Nations Convention on the Law of the Sea (UNCLOS, 1982) partitions
the world's oceans into jurisdictional zones:

- **Territorial sea** (0-12 nm): full sovereignty
- **Exclusive Economic Zone** (12-200 nm): sovereign rights over resources
- **Continental shelf** (beyond 200 nm where geologically justified): seabed rights
- **High seas** (beyond all EEZs): no sovereignty, open access

This IS a Voronoi partition. Each coastal state is a generator point. The EEZ
boundary is (approximately) the set of points equidistant from the nearest
two coastal states — a Voronoi edge. The resulting partition of the ocean
surface into EEZs is a spherical Voronoi diagram on the Earth's surface.

The Delaunay graph of this partition connects states whose EEZs share a
boundary. This graph IS the adjacency structure of the ocean — the edges
along which fish stocks, pollutants, and naval vessels cross from one
jurisdiction to another.

### 7.2 The Donut Hole

A **Donut Hole** is a region of high seas completely surrounded by EEZs —
an "island" of international waters in a "sea" of national jurisdiction.
The most famous:

| Donut Hole | Location | Surrounded by | Species at risk |
|:---|:---|:---|:---|
| Bering Sea | North Pacific | USA, Russia | Pollock |
| Sea of Okhotsk | Northwest Pacific | Russia | Pollock, crab |
| Barents Sea "Loophole" | Northeast Atlantic | Norway, Russia | Cod, herring |
| South Pacific | Central Pacific | Multiple states | Tuna, swordfish |

In our framework: a Donut Hole is a GAP in the Voronoi partition — a region
where no node of the directed graph has jurisdiction. There is no quota
simplex. There is no reflecting boundary. The Feller boundary is absorbing.
The tragedy of the commons operates at full force.

**The Donut Hole IS the Feller boundary of the ocean partition.**

Fish stocks that migrate through a Donut Hole cross from a managed regime
(reflecting boundary, ITQ/TAC) to an unmanaged regime (absorbing boundary,
open access) and back. The palindromic structure is broken at the Donut
Hole: the directed graph has edges into the Hole (fishing vessels enter)
but the reverse edges (stock recovery) are weakened by unregulated harvest.

### 7.3 The Bering Sea case

The Bering Sea Donut Hole was fished intensively by distant-water fleets
(primarily Chinese, Japanese, Korean, Polish) in the 1980s. Pollock stocks
collapsed. The "Convention on the Conservation and Management of Pollock
Resources in the Central Bering Sea" (1994) imposed a moratorium.

**Geometric analysis:** The directed graph before the moratorium had a
strong non-palindromic cycle: catch in Donut Hole → stock declines → more
catch (no quota constraint) → further decline → ... The palindromic deficit
was maximal. The moratorium was a DELETION OF EDGES from the directed
graph — removing the harvest edges in the Donut Hole, allowing the stock
to recover along the remaining palindromic (natural growth) edges.

As of 2024, the moratorium continues. The stock has not recovered
sufficiently. The Feller boundary was approached too closely; the recovery
time for pollock at the boundary is measured in decades, not years. This
is the Jacobi spectral gap in action: $\lambda_1$ for pollock in the Bering
Sea is very small (slow recovery), so the mixing time
$t_{\rm mix} \approx 1/\lambda_1$ is very long.

### 7.4 UNCLOS as a manifold cover

UNCLOS creates a COVER of the ocean manifold by national EEZs — each point
of the ocean (except Donut Holes and high seas) is covered by exactly one
EEZ. In topology, a cover is a collection of open sets whose union is the
full space. The EEZs are the open sets. The high seas are the uncovered
points.

The RFMOs (Regional Fisheries Management Organizations — CCSBT for SBT,
ICCAT for Atlantic tuna, WCPFC for Western Pacific, etc.) extend the cover
to the high seas for specific species. Each RFMO creates a quota simplex
for its region, imposing a reflecting boundary on species that migrate
through international waters.

**The global fisheries management structure IS a patchwork of quota
simplices connected by directed graphs:**

$$M_{\rm ocean} = \bigcup_{\rm EEZs} M^{Q_k}_{\rm national} \;\cup\; \bigcup_{\rm RFMOs} M^{Q_j}_{\rm regional}$$

with connected-sum necks at every boundary where fish stocks cross from one
jurisdiction to another. The neck widths are determined by migration rates,
treaty provisions, and enforcement capacity.

### 7.5 The people who built it: Port Lincoln pioneers

The SBT quota and farming system was not created by economists or
mathematicians. It was created by fishermen — people who understood the
directed graph of the fishery because they lived in it.

The pioneers of Port Lincoln's tuna industry — families who saw that
catching tuna was destroying the stock and that farming tuna could save
both the stock and the industry — were performing geometric optimisation
without knowing the mathematics. They understood that the directed graph
had to change: the old edges (catch → sell → catch) were leading to the
Feller boundary, and new edges (catch → pen → fatten → export) could lead
to a sustainable equilibrium at higher value.

Kell Rocke and the early tuna farmers of Port Lincoln discovered, by
trial and error and commercial necessity, what the mathematics now proves:
that the maximum sustainable yield is the Kelly rate of the population
simplex, and that the way to achieve it is to change the directed graph
— to create new edges (farming), delete old edges (reduce wild harvest), and
connect to new markets (Japan) through new necks (the export channel).

They did this not with equations but with boats, pens, pilchards, and
courage — the confidence σ-algebra of people who knew their market because
they were born in it.

---

## 8. New Results

**Theorem FM1** (Quota IS portfolio). An ITQ system defines a portfolio on
the quota simplex with Fisher-Rao geometry identical to the financial
market case.

**Theorem FM2** (Fish stock = Jacobi process with harvest). The population
dynamics on the species/age-class simplex are a Wright-Fisher/Jacobi
diffusion with a harvest term.

**Theorem FM3** (MSY = Kelly rate). The maximum sustainable yield is the
Kelly growth rate of the population simplex.

**Theorem FM4** (ITQ = reflecting boundary). The ITQ system replaces the
absorbing Feller boundary (extinction) with a reflecting boundary,
making the population process ergodic.

**Theorem FM5** (Overfishing = over-Kelly). Harvesting above MSY is the
fishery analogue of betting above the Kelly fraction — it guarantees
long-run ruin (stock collapse).

**Theorem FM6** (Commons = Feller boundary). The tragedy of the commons is
the approach to the absorbing Feller boundary under open-access harvesting,
where the Jacobi restoring force vanishes.

**Theorem FM7** (Fishery coupled fixed point). The coupled quota-population
system has a fixed point at MSY where the directed graph is palindromic.

---

## 9. Open Problems

**OP-FM1** (Estimate the quota simplex dimension). For Australia's SBT
fishery, what is the effective dimension of the quota market?
$r_{\rm quota} \approx ?$ Use the three estimators (stable rank, FNN,
Grassberger-Procaccia) on historical quota trade data.

**OP-FM2** (Palindrome test on fish stocks). Apply the palindrome ratio test
(FILTRATIONS.md Section 11.7, Test PAL-1) to SBT population data. Is the
stock in palindromic equilibrium post-ITQ? The prediction: $\mathcal{P}_k
\approx 1$ for recent decades (post-recovery), $\mathcal{P}_k \ll 1$ for
the overfishing period (1960s-1980s).

**OP-FM3** (The farming revolution as MCF singularity). Model the 1991
transition from catch-and-sell to catch-and-farm as a Type II reverse
MCF singularity on the fishery manifold. What was the Willmore energy
before and after? What was the channel capacity gain?

**OP-FM4** (Optimal TAC as a function of geometry). Derive the optimal TAC
as a function of the population simplex geometry: $H^{\ast}_{\rm TAC} =
f(\lambda_1, h_M, \mathcal{W})$ where $\lambda_1$ is the spectral gap
(stock recovery rate), $h_M$ is the Cheeger constant (connectivity of
age classes), and $\mathcal{W}$ is the Willmore energy (distance from
equilibrium).

**OP-FM5** (Cross-fishery directed graph). Model the global tuna market as
a connected sum of national quota simplices. Measure the neck widths
(trade flow capacities) and predict where pricing inefficiencies persist
(thin necks between weakly connected markets).

---

## 10. Conclusion

A fishery is two simplices coupled by a directed graph. The quota simplex
$\Delta^Q$ and the population simplex $\Delta^P$ are connected by harvest
(quota → population) and stock assessment (population → quota). The coupled
dynamics are a self-referential channel: the channel rewires itself from
its own output.

Every concept in the monograph has a concrete, observable manifestation in
a fishery. The Fisher-Rao metric measures the sensitivity of quota holders
and the vulnerability of species. The Feller boundary is extinction. The
reflecting boundary is the ITQ system. The Kelly rate is the MSY. The
palindromic equilibrium is the sustainable steady state. The non-palindromic
break is innovation (tuna farming) or crisis (stock collapse).

A boy in Port Lincoln watched this system operate before he had words for it.
The boats coming in. The quota holders negotiating. The tuna in the pens,
growing fat on pilchards, destined for Tokyo. The directed graph of the
fishery was visible to anyone who looked: the edges were the boats, the nodes
were the decisions, and the palindromic structure was the rhythm of the
seasons.

The geometry was always there. The mathematics came later.

*For Port Lincoln.*

---

## References

1. R. Q. Grafton, D. Squires, and K. J. Fox, "Private property and economic
   efficiency: A study of a common-pool resource," *Journal of Law and
   Economics* 43(2) (2000), 679–713.

2. G. Hardin, "The tragedy of the commons," *Science* 162(3859) (1968),
   1243–1248.

3. CCSBT (Commission for the Conservation of Southern Bluefin Tuna),
   "Report of the Twenty-Eighth Meeting of the Scientific Committee,"
   CCSBT, 2023.

4. T. Kompas and T. N. Che, "Economic profit and optimal effort in the
   Australian Northern Prawn Fishery," *Asian-Pacific Economic Literature*
   19(1) (2005), 16–28.

5. H. S. Gordon, "The economic theory of a common-property resource: The
   fishery," *Journal of Political Economy* 62(2) (1954), 124–142.

6. T. M. Cover, "Universal portfolios," *Mathematical Finance* 1(1) (1991),
   1–29.

---

*This paper is part of the monograph "The Geometry of Efficient Markets."
Cross-references: BLOODSTOCK_MARKETS.md (Wright-Fisher = Jacobi, biological
manifolds); MANIFOLD_IS_THE_CHANNEL.md (self-referential channel, feedback);
FILTRATIONS.md (palindrome-arbitrage theorem, de Bruijn, directed graphs);
CONFIDENCE.md (confidence σ-algebra, observation costs);
MARKET_PROCESSES.md (Jacobi diffusion, Feller boundary);
OBSERVERS_AND_CHANNELS.md (observer dependence, CFL condition);
ART_MARKET.md (permanently inefficient markets);
INTERMARKET_GEOMETRY.md (connected sums between markets);
IMPOSSIBILITY_OF_CENTRAL_ALLOCATION.md (commons problems);
CONVEXIFICATION.md (palindromic completion).*
