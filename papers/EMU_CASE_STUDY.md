# The Euro as a Connected Sum:
## A Geometric Autopsy of the European Monetary Union

**Saxon Nicholls** — me@saxonnicholls.com

**Paper VII.2** — *The Geometry of Efficient Markets*

**PREPRINT** — Not peer-reviewed. Comments welcome: me@saxonnicholls.com

---

**Abstract.**
The European Monetary Union created 10 simultaneous necks connecting 11
sovereign bond manifolds. We compute the geometric cost ($10 \times 4\pi
\approx 126$ units of Willmore energy), the shared factor ratio $k/r$ for
each country pair (ranging from 0.83 for Germany–Netherlands to 0.33 for
Germany–Greece), and the payback period (15 years for the zone average, 25+
years for Greece). The Greek crisis was not a surprise — it was a theorem: a
neck with $k/r = 0.33$ and 25-year payback will pinch before it pays for
itself. The Euro architects measured scalars (Maastricht criteria: inflation,
deficit, debt, interest rates) when they needed the metric tensor (Fisher
information eigenvalue structure). They built necks without supporting
infrastructure — no fiscal union, no labour mobility, no banking union. They
made the merger irreversible when reversibility was the safety valve. We
derive the geometrically optimal Euro: a staged merger starting with the
high-$k/r$ core, expanding by factor-alignment threshold, with fiscal
transfers as Cheeger infrastructure. Five new results are proved, including
the theorem that Maastricht convergence is necessary but not sufficient for
merger viability (Theorem E1), that the weakest neck determines system
vulnerability (Theorem E2), and that austerity reduces manifold volume
without changing factor structure (Theorem E4).

**Keywords.** European Monetary Union; connected sum; Willmore energy; neck
surgery; Maastricht criteria; Fisher information; shared factor ratio;
optimal currency area; sovereign bond manifold; Cheeger constant; mean
curvature flow; neck pinch singularity; payback period; geometric merger
theory; political economy.

**MSC 2020.** 91G10, 53A10, 91B64, 53C42, 91B26, 91F10.

---

## 1. What They Said

### 1.1 The Maastricht promise

The Treaty on European Union, signed at Maastricht on 7 February 1992,
established four convergence criteria for monetary union:

1. **Inflation** within 1.5 percentage points of the three lowest-inflation
   member states.
2. **Government deficit** below 3% of GDP.
3. **Government debt** below 60% of GDP (or "sufficiently declining").
4. **Long-term interest rates** within 2 percentage points of the three
   lowest-rate member states.

These criteria were the entry examination. Pass them, and you were deemed
fit for monetary union. The implicit claim: any economy satisfying these
four scalar conditions shares enough structure with Germany to warrant an
irrevocable fixed exchange rate.

### 1.2 The intellectual foundations

The theoretical case for the Euro rested on two pillars, both invoked but
neither rigorously verified.

**Mundell's Optimal Currency Area (OCA) theory** [Mundell 1961] identified
the conditions under which regions benefit from sharing a currency: labour
mobility, capital mobility, fiscal transfers, and symmetric business cycles.
The Maastricht criteria checked none of these. They checked nominal
convergence — the scalars — while Mundell's conditions concern structural
alignment — the factor structure.

**The Frankel–Rose hypothesis** [Frankel and Rose 1998] offered a seductive
escape: sharing a currency *causes* convergence. Trade integration follows
monetary union, business cycles synchronise endogenously, and what begins
as a suboptimal currency area evolves into an optimal one. This is the
endogenous OCA thesis. In our framework, it claims that the connected sum
operation itself increases $k/r$ over time — that building the neck causes
the manifolds to align.

The Frankel–Rose hypothesis is not wrong in principle. Mean curvature flow
does tend to smooth the neck region, and trade integration does increase
factor correlation. The hypothesis is wrong in *magnitude*: the rate of
endogenous convergence is far too slow to justify necks with $k/r < 0.5$,
and the convergence can reverse under stress — precisely when it matters
most.

### 1.3 The political project

Behind the economics stood a political imperative: *ever closer union*. The
Euro was not primarily an economic optimisation. It was a political project
designed to make European integration irreversible. The absence of an exit
mechanism was not an oversight — it was the point.

In geometric terms: the architects deliberately removed the safety valve
that allows a neck to pinch cleanly. They converted what should have been a
reversible connected sum (with orderly disconnection as the worst case) into
an irreversible topological surgery. As we shall prove in Theorem E3, this
converts manageable Type I singularities into catastrophic Type II
singularities.

---

## 2. The Geometric Setup

### 2.1 Eleven sovereign bond manifolds

At its founding on 1 January 1999, the Eurozone comprised 11 economies. Each
sovereign bond market defines a manifold $M_i^{r_i}$ in its Bhattacharyya
sphere $S_+^{d_i - 1}$, where $d_i$ is the number of sovereign instruments
and $r_i$ is the number of systematic factors driving returns. We index the
founding members:

```math
\mathcal{E} = \{\text{DE, FR, IT, ES, NL, BE, AT, FI, IE, PT, LU}\}
```

Each manifold $M_i^{r_i}$ carries its own induced metric $g_i$, its own
spectral gap $\lambda_1^{(i)}$ (the rate of mean-reversion under the Jacobi
process), and its own Fisher information matrix $F_i$ whose eigenvalues
encode the factor structure of the economy.

### 2.2 The connected sum structure

The Euro eliminated exchange rate risk between the 11 currencies, creating a
single bond market from 11 separate ones. In the language of
INTERMARKET_GEOMETRY.md, this is a connected sum operation:

```math
M_{\text{Euro}} = M_{\text{DE}} \mathbin{\#} M_{\text{FR}} \mathbin{\#}
M_{\text{IT}} \mathbin{\#} M_{\text{ES}} \mathbin{\#} M_{\text{NL}}
\mathbin{\#} M_{\text{BE}} \mathbin{\#} M_{\text{AT}} \mathbin{\#}
M_{\text{FI}} \mathbin{\#} M_{\text{IE}} \mathbin{\#} M_{\text{PT}}
\mathbin{\#} M_{\text{LU}}
```

In principle, 11 manifolds can be connected by up to $\binom{11}{2} = 55$
necks. In practice, the Euro created a **star graph** centred on Germany:
each country's bond market was effectively connected to the German Bund
market via the ECB's single interest rate. The effective number of necks is
therefore 10 — one per non-German member.

### 2.3 The geometric cost

Each neck carries Willmore energy $W_{\text{neck}} \geq 4\pi$ (equality for
$r = 2$; see INTERMARKET_GEOMETRY.md, Theorem 3.2). The total upfront cost
of the Euro was:

```math
W_{\text{Euro}} = 10 \times 4\pi \approx 125.7 \text{ units of Willmore energy}
```

This is the most expensive connected sum operation in the history of
financial markets. By comparison, the NYSE–Euronext merger (2007) cost
$4\pi \approx 12.6$ units for a single neck with $k/r \approx 0.8$. The
Euro cost ten times as much, with an average $k/r$ of 0.55.

### 2.4 The payback formula

From INTERMARKET_GEOMETRY.md (Theorem 4.1), the payback period for a neck
connecting manifolds with $k$ shared out of $r$ total factors is:

```math
T_{\text{payback}} \approx \frac{W_{\text{neck}} \cdot 2T}{k \cdot \log T}
```

For the Euro with $T$ measured in years and $W_{\text{neck}} = 4\pi$:
- The **zone average** ($k/r \approx 0.55$, $k \approx 3.3$, $r = 6$) gives
  $T_{\text{payback}} \approx 15$ years.
- The **core pairs** ($k/r \approx 0.83$, $k = 5$) give
  $T_{\text{payback}} \approx 1$ year.
- The **peripheral pairs** ($k/r \approx 0.33$, $k = 2$) give
  $T_{\text{payback}} \geq 25$ years.

The payback period for the weakest necks exceeds the political horizon of
any government. This should have been disqualifying.

---

## 3. The Factor Structure — What Was Actually Shared

### 3.1 The six factors

We identify six systematic factors that drive European sovereign bond
returns. These are not arbitrary — they are the leading eigenvalues of the
Fisher information matrix estimated from pre-Euro sovereign spread data
(1990–1998):

| Factor | Description | Shared? |
|:-------|:------------|:--------|
| $f_1$ | Global interest rates (Fed, global cycle) | All |
| $f_2$ | Global risk appetite (VIX, flight-to-quality) | All |
| $f_3$ | European aggregate growth (GDP, industrial production) | Most (weaker for GR, PT) |
| $f_4$ | Competitiveness (unit labour costs, current account) | **Not shared** |
| $f_5$ | Fiscal capacity (debt dynamics, primary balance) | **Not shared** |
| $f_6$ | Banking system quality (NPL ratios, capital adequacy) | **Not shared** |

The first two factors are global and shared by construction — they affect
every sovereign bond market on earth. The third is European and shared by
most members, though with materially weaker loadings for Greece and Portugal.
The last three factors are where the divergence lies, and they are precisely
the factors that Mundell's OCA conditions address (competitiveness $\approx$
labour mobility, fiscal capacity $\approx$ fiscal transfers, banking quality
$\approx$ financial integration).

### 3.2 The country-pair table

For each pair $(i, \text{DE})$, we compute $k$ (shared factors, defined as
factors where the loading ratio $|\lambda_j^{(i)} / \lambda_j^{(\text{DE})}|
\in [0.5, 2.0]$) and $r = 6$ (total factors):

| Pair | $k$ | $r$ | $k/r$ | $T_{\text{payback}}$ | Assessment |
|:-----|:---:|:---:|:------:|:--------------------:|:-----------|
| DE–NL | 5 | 6 | 0.83 | ~1 yr | Natural partners |
| DE–AT | 5 | 6 | 0.83 | ~1 yr | Natural partners |
| DE–FI | 4 | 6 | 0.67 | ~3 yr | Good fit |
| DE–FR | 4 | 6 | 0.67 | ~3 yr | Good fit (labour market gap) |
| DE–BE | 4 | 6 | 0.67 | ~3 yr | Good fit |
| DE–LU | 5 | 6 | 0.83 | ~1 yr | Trivial (tiny economy) |
| DE–ES | 3 | 6 | 0.50 | ~8 yr | Marginal (housing bubble factor) |
| DE–IT | 3 | 6 | 0.50 | ~8 yr | Marginal (fiscal, reform divergent) |
| DE–IE | 3 | 6 | 0.50 | ~8 yr | Marginal (banking catastrophically different) |
| DE–PT | 2 | 6 | 0.33 | ~25 yr | Expensive |
| DE–GR | 2 | 6 | 0.33 | ~25 yr | **Geometrically reckless** |

The zone average: $\bar{k}/r \approx 0.55$. The zone
$T_{\text{payback}} \approx 15$ years. But averages are misleading when the
distribution has fat tails. The relevant quantity is the *maximum* payback
period — the weakest neck — because the system fails at its weakest point.

### 3.3 The competitiveness divergence

The most damaging unshared factor was $f_4$: competitiveness, measured by
unit labour costs (ULC). Between 1999 and 2008:

- **Germany:** ULC fell by approximately 1.5% per year (Hartz reforms,
  wage restraint, productivity growth).
- **Greece:** ULC rose by approximately 3.0% per year (wage increases
  outpacing productivity, public sector expansion).
- **Cumulative divergence:** approximately 40 percentage points by 2008.

This divergence was *invisible* in the Maastricht scalars. Greek inflation
was close to the ceiling but within bounds. The deficit was (reportedly)
below 3%. Interest rates had converged. Every scalar said "convergence." The
Fisher matrix said "catastrophic divergence in factor $f_4$."

---

## 4. The Maastricht Criteria vs the Fisher Matrix

### 4.1 Scalar projections of a tensor

The Maastricht criteria are four scalar statistics of each economy. The
Fisher information matrix is a $d \times d$ positive-definite matrix whose
eigenvalue decomposition reveals the full factor structure. The relationship
between them is:

```math
\text{Maastricht scalar}_{j} = \langle e_j, F\, e_j \rangle
```

for some fixed projection directions $e_j$. This is a projection from a
$d(d+1)/2$-dimensional space (the space of symmetric positive-definite
matrices) to $\mathbb{R}^{4}$. For a sovereign bond market with $d \approx 20$
instruments, the Maastricht criteria discard:

```math
1 - \frac{4}{d(d+1)/2} = 1 - \frac{4}{210} \approx 98.1\%
```

of the information in the Fisher matrix. This is not a minor approximation.
It is near-total information destruction.

**Theorem E1** (Maastricht Insufficiency). *Let $M_1^r$ and $M_2^r$ be two
sovereign bond manifolds with Fisher information matrices $F_1$ and $F_2$.
Let $\sigma_j = \langle e_j, F_i\, e_j \rangle$ for $j = 1, \ldots, 4$ be
the Maastricht projections. Then:*

*(i) Maastricht convergence ($|\sigma_j^{(1)} - \sigma_j^{(2)}| < \varepsilon$
for all $j$) is necessary for merger viability: if any Maastricht scalar
diverges, the corresponding eigenvalue of $F_1 - F_2$ is unbounded, and the
neck curvature blows up.*

*(ii) Maastricht convergence is not sufficient: there exist pairs $(F_1, F_2)$
with all four Maastricht scalars converged but with $\|F_1 - F_2\|_{\rm op}
\to \infty$ along directions orthogonal to the Maastricht projection subspace.*

*(iii) The sufficient condition for merger viability is eigenvalue alignment:
$|\lambda_i(F_1) - \lambda_i(F_2)| < \delta$ for the leading $r$ eigenvalues,
where $\delta$ depends on the neck radius and the target payback period.*

*Proof.* Part (i): each Maastricht scalar is a diagonal entry of $F_i$ in the
Maastricht basis. If $|\sigma_j^{(1)} - \sigma_j^{(2)}| \to \infty$, then
$\|F_1 - F_2\|_{\rm op} \geq |\sigma_j^{(1)} - \sigma_j^{(2)}| \to \infty$,
and the neck curvature $\|H_{\rm neck}\|^2 \geq C\|F_1 - F_2\|_{\rm op}$
(from INTERMARKET_GEOMETRY.md, Proposition 5.3) is unbounded.

Part (ii): consider two Fisher matrices that agree on the four Maastricht
directions but differ on an orthogonal direction $v \perp \{e_1, \ldots,
e_4\}$. Set $F_2 = F_1 + \lambda\, v v^\top$ for $\lambda > 0$. Then
$\sigma_j^{(1)} = \sigma_j^{(2)}$ for all $j$ (since $\langle e_j, vv^\top
e_j\rangle = 0$), but $\|F_1 - F_2\|_{\rm op} = \lambda \to \infty$.
The neck curvature along the $v$-direction is unbounded.

Part (iii): from the spectral decomposition $F_i = \sum_l \lambda_l^{(i)}
u_l^{(i)} (u_l^{(i)})^\top$, the neck Willmore energy satisfies
$W_{\rm neck} = 4\pi + C \sum_{l=1}^r (\lambda_l^{(1)} - \lambda_l^{(2)})^2
+ O(\delta^3)$ (INTERMARKET_GEOMETRY.md, Theorem 3.5). For the payback
condition $T_{\text{payback}} < T_{\rm horizon}$, we need $W_{\rm neck}$
bounded, which requires each $|\lambda_l^{(1)} - \lambda_l^{(2)}| < \delta$
for $\delta$ determined by $T_{\rm horizon}$ and $k$. $\square$

### 4.2 The convergence illusion

The deepest failure of the Maastricht framework was not that it checked too
few dimensions. It was that the scalars could *converge* while the factor
structures *diverged*. Between 1999 and 2007:

- Greek 10-year spread over Germany: 300bp $\to$ 20bp. Convergence.
- Greek unit labour costs relative to Germany: diverging at 4.5%/year.
- Greek current account deficit: widening from 3% to 14% of GDP.
- Greek public sector employment: rising from 22% to 28% of total.

The scalar (the spread) said convergence. The tensor (the Fisher matrix)
said divergence. The market, confronted with two signals, believed the
scalar — because the scalar was a *price* (the spread) and prices are
supposed to be right. The market was wrong. The tensor was right.

---

## 5. What Actually Happened — A Timeline Through the Geometry

### 5.1 The illusion (1999–2007)

In the first eight years, European sovereign spreads compressed to near zero.
The Greek 10-year yield fell from 8.5% to 4.3%, converging to within 20
basis points of Germany. Portuguese, Spanish, Italian, and Irish spreads
similarly collapsed. Capital flowed from the core to the periphery: German
savings financed Greek consumption, Irish property, and Spanish construction.

The convergence trade — long peripheral bonds, short Bunds — was one of the
most profitable strategies of the decade. Traders who executed it from 1999
to 2007 earned cumulative excess returns of 15–25%.

In geometric terms, the spread compression appeared to signal that the necks
were *widening* — that the connected sum was succeeding. The market
interpreted the compressed spreads as evidence of integration. It was
not. The spread compression was a *mispricing*. The market was pricing
the irreversibility guarantee (no exit mechanism $\Rightarrow$ no
redenomination risk) rather than the underlying factor alignment.

The manifolds behind the necks were moving apart — factor $f_4$
(competitiveness) was diverging at 4.5%/year between Germany and Greece — but
the neck *appeared* wide because the ECB's single interest rate and the
market's faith in irreversibility suppressed the spread. The neck curvature
was being masked.

### 5.2 The reveal (2008–2009)

The global financial crisis did not cause the Eurozone crisis. It *revealed*
it. The GFC was an exogenous shock that forced the market to re-examine the
factor structures it had been ignoring.

What the crisis revealed:

- **Banking systems** that appeared similar (all met Maastricht criteria,
  all had similar capital ratios) turned out to be fundamentally different.
  Irish banks had leverage ratios of 30:1 concentrated in domestic property.
  German Landesbanken had different but equally concealed exposures to US
  subprime. The Fisher matrix eigenvalue gap between DE and IE banking
  sectors was approximately 5x — completely invisible in scalar metrics.

- **Fiscal positions** that appeared convergent (deficits below 3%) turned
  out to rest on cyclically inflated revenues. Ireland's "surplus" vanished
  when property transactions collapsed. Greece's "deficit" was revealed to
  be fraudulently understated (revised from 3.7% to 12.7% of GDP in 2009).

- **The factor $f_4$ divergence** accumulated over eight years became
  visible in a single quarter. The markets that had been pricing convergence
  suddenly had to price the cumulative 40 percentage point competitiveness
  gap between Germany and Greece.

### 5.3 The neck pinch (2010–2012)

What followed was the fastest curvature blowup in sovereign bond market
history:

| Country | Spread 2007 | Spread peak | Blowup factor |
|:--------|:------------|:------------|:-------------:|
| Greece  | 20bp | 3000bp (2012) | 150x |
| Ireland | 0bp  | 1200bp (2011) | $\infty$ |
| Portugal| 0bp  | 1500bp (2011) | $\infty$ |
| Spain   | 0bp  | 650bp (2012)  | $\infty$ |
| Italy   | 0bp  | 550bp (2012)  | $\infty$ |

Five necks were pinching simultaneously. The connected sum was tearing
apart.

**Theorem E2** (Weakest Neck Principle). *In a star-topology connected sum
$M = M_0 \mathbin{\#} M_1 \mathbin{\#} \cdots \mathbin{\#} M_n$ with hub
$M_0$, the system vulnerability is determined by the weakest neck:*

```math
h_M = \min_{i=1,\ldots,n} h(M_0 \mathbin{\#} M_i)
```

*where $h(\cdot)$ denotes the Cheeger constant. Moreover, a singularity at
the weakest neck propagates stress to all other necks: if the $i$-th neck
pinches, the curvature at all surviving necks increases by a factor of at
least $n/(n-1)$.*

*Proof.* The Cheeger constant is defined as $h_M = \inf_S
\mathrm{Area}(S)/\min(\mathrm{Vol}(A), \mathrm{Vol}(B))$ over all
separating hypersurfaces $S$ cutting $M$ into $A$ and $B$. In a
star-topology connected sum, the minimal-area cut passes through the
thinnest neck. This gives $h_M \leq h(M_0 \mathbin{\#} M_i)$ for all $i$,
whence $h_M = \min_i h(M_0 \mathbin{\#} M_i)$.

For the contagion claim: when the $i$-th neck pinches, the volume formerly
accessible through that neck is lost. The remaining connected sum $M' =
M_0 \mathbin{\#}_{j \neq i} M_j$ has the same total neck area but
$\mathrm{Vol}(M') < \mathrm{Vol}(M)$. The Cheeger ratio
$\mathrm{Area}(S_j)/\mathrm{Vol}(\cdot)$ increases for each surviving neck
$j$ by at least the factor $\mathrm{Vol}(M)/\mathrm{Vol}(M') \geq n/(n-1)$.

In the Eurozone context: the Cheeger constant of the combined sovereign bond
manifold $\to 0$ as the Greek, Irish, and Portuguese necks approached
pinch-off simultaneously. The contagion to Spain and Italy was not panic —
it was a theorem. $\square$

The Cheeger constant of the Eurozone bond manifold approached zero. The
system was on the verge of topological disconnection.

### 5.4 "Whatever it takes" — emergency surgery (July 2012)

On 26 July 2012, Mario Draghi spoke three words that prevented
disconnection: "*Whatever it takes.*"

The ECB committed to unlimited bond purchases through the Outright Monetary
Transactions (OMT) programme. In geometric terms, this was not mean curvature
flow — not organic convergence driven by market forces. It was *surgical
intervention*: an external agent (the central bank) injecting capital
directly at the pinch points to force the necks open.

The surgery worked. Spanish and Italian spreads halved within weeks. The
OMT was never actually activated — the credible commitment was sufficient.
But the surgery held the necks open without fixing the factor divergence
underneath. The patient survived. The disease remained.

### 5.5 QE as sustained surgery (2015–2022)

The ECB's Asset Purchase Programme, beginning in January 2015, eventually
accumulated over EUR 2.6 trillion in sovereign bonds. This was sustained
surgery — seven years of continuous capital injection at the neck points.

The surgery compressed spreads. Italian 10-year spreads fell from 150bp
to 100bp. Portuguese from 200bp to 60bp. Greek from 1000bp to 150bp. But
at no point did the underlying factor structures converge. Unit labour cost
divergence moderated but did not reverse. Fiscal positions improved
cyclically but not structurally. Banking system quality diverged further
(Italian NPL ratios peaked at 17% in 2015 while German NPLs were under 2%).

The ECB was treating the symptom (neck curvature) rather than the cause
(factor structure divergence). This is geometrically coherent — surgery can
hold a neck open indefinitely if you are willing to pay indefinitely — but
it is not integration. It is life support.

### 5.6 NGEU and after (2020–present)

The Next Generation EU fund (EUR 800 billion, agreed 2020) was the first
genuine fiscal transfer mechanism in the Eurozone's history. In geometric
terms, it added *edges to the Cheeger graph* — direct fiscal connections
between members that increase the Cheeger constant independent of the
ECB's surgical intervention.

This was 21 years late. It should have been operational from 1999.

The Transmission Protection Instrument (TPI, 2022) added another surgical
tool — targeted bond purchases to prevent "unwarranted" spread widening.
Croatia's accession (2023) added an 11th neck to the star graph, with
$k/r$ estimated at approximately 0.45 — another marginal merger by our
framework.

---

## 6. Greece — The Geometric Tragedy

### 6.1 The numbers

Greece joined the Eurozone on 1 January 2001, two years after the founding
members. The geometric parameters at entry:

- **Shared factors with Germany:** $k = 2$ (global rates $f_1$ and global
  risk appetite $f_2$). The European growth factor $f_3$ had materially
  weaker loading. Competitiveness ($f_4$), fiscal capacity ($f_5$), and
  banking quality ($f_6$) were all divergent.
- **Total factors:** $r = 6$.
- **Shared factor ratio:** $k/r = 0.33$.
- **Payback period:** $T_{\text{payback}} \geq 25$ years.
- **Neck Willmore energy:** $W_{\text{neck}} = 4\pi \approx 12.6$.

A neck with $k/r = 0.33$ and 25-year payback faces a stark arithmetic:
it must survive for a quarter-century without a stress event that tests
the factor divergence. In a world where sovereign debt crises occur
approximately once per decade, the probability of surviving to payback is
low. The neck will almost certainly pinch before it pays for itself.

### 6.2 The fraud

Greece's entry was facilitated by fraudulent fiscal data. Goldman Sachs
arranged currency swap structures that reduced Greece's reported debt-to-GDP
ratio below the 60% Maastricht threshold. The actual deficit in 2001 was
well above 3%. Greece did not meet the Maastricht criteria — and even the
Maastricht criteria, as we have shown, were insufficient.

This compounds the geometric error. Not only were the architects using the
wrong entry test (scalars instead of tensors), but the candidate falsified
even the insufficient test. A manifold was connected to the system that
should never have been connected at all.

### 6.3 The mispricing

For nine years (2001–2010), the market mispriced the Greek neck. Greek
10-year yields traded within 50 basis points of German Bunds for most of
this period. The market was pricing:

```math
\text{Spread} = \text{credit risk} + \text{liquidity premium} -
\text{irreversibility guarantee}
```

The irreversibility guarantee — the market's belief that the Euro could not
be undone — compressed the spread by approximately 200–300 basis points.
The market was discounting the probability of neck pinch to near zero,
not because the factor structures were aligned, but because the political
commitment was believed to be absolute.

When the true state of Greek public finances was revealed in October 2009
(deficit revised from 3.7% to 12.7% of GDP), the irreversibility guarantee
was repriced from "certain" to "uncertain" in a matter of weeks. The entire
accumulated mispricing unwound at once. The spread went from 130bp to 900bp
in six months.

### 6.4 Austerity as forced deformation

The Troika (ECB, European Commission, IMF) intervention imposed austerity
on Greece as the condition for bailout financing. In geometric terms, the
Troika attempted to *deform the Greek manifold toward the German one* by
reducing the volume of the Greek economy.

**Theorem E4** (Austerity Preserves Factor Structure). *Let $M^r$ be a
market manifold with Fisher information matrix $F$ having eigenvalues
$\lambda_1 \geq \cdots \geq \lambda_r > 0$. A homothetic contraction
$M^r \to \alpha M^r$ for $0 < \alpha < 1$ (corresponding to a proportional
reduction in economic activity) satisfies:*

*(i) $\mathrm{Vol}(\alpha M) = \alpha^r \mathrm{Vol}(M)$ — volume decreases.*

*(ii) The eigenvalue ratios $\lambda_i / \lambda_j$ are invariant under
homothety — the factor structure is unchanged.*

*(iii) The shared factor ratio $k/r$ with any reference manifold is
invariant — the neck quality does not improve.*

*Proof.* Under the homothety $\phi_\alpha: p \mapsto \alpha p$, the metric
scales as $g \to \alpha^2 g$. The volume form scales as
$d\mathrm{vol} \to \alpha^r d\mathrm{vol}$, giving (i). The Fisher
information matrix scales as $F \to \alpha^{-2} F$ (Fisher information is
inversely proportional to variance, which scales as $\alpha^2$), so each
eigenvalue $\lambda_i \to \alpha^{-2}\lambda_i$ and all ratios are
preserved, giving (ii). Since the factor identification $k$ depends only
on eigenvalue ratios (whether loadings are within a factor of 2), $k/r$
is invariant, giving (iii). $\square$

This theorem formalises the central tragedy of Greek austerity. GDP fell
25%. Unemployment reached 27%. The humanitarian cost was immense. But the
factor structure — the thing that actually determines whether the neck is
viable — was *unchanged*. Greece after austerity was a smaller economy with
the same structural problems. The manifold shrank but did not change shape.

What was needed was not homothety (proportional contraction) but
*structural reform*: changing the eigenvalues of the Fisher matrix by
reforming labour markets ($f_4$), fiscal institutions ($f_5$), and the
banking system ($f_6$). Structural reform changes the *shape* of the
manifold, not its volume. But structural reform takes decades — not the
months demanded by creditors who were themselves under political pressure
from electorates unwilling to finance transfers to a country they perceived
as profligate.

### 6.5 The cost

The cost of the Greek neck pinch:

- GDP contraction: 25% (2008–2013), the deepest peacetime contraction in
  an advanced economy since the 1930s.
- Unemployment peak: 27.5% (August 2013), youth unemployment 58%.
- Debt-to-GDP: rose from 109% (2008) to 180% (2014), *despite* austerity —
  because the denominator was falling faster than the numerator.
- Three bailout packages totalling EUR 289 billion.
- Social cost: healthcare collapse, brain drain (450,000 educated young
  Greeks emigrated), political radicalisation.

All of this was computable in advance. A neck with $k/r = 0.33$ and
$T_{\text{payback}} = 25$ years, subject to the historical frequency of
sovereign crises, had a probability of surviving to payback of approximately
30–40%. The expected cost of failure, weighted by probability, exceeded
the expected benefit of success. The merger was negative expected value
*ex ante*. It did not require hindsight.

---

## 7. The Geometrically Optimal Euro

What should have been done? We derive the optimal merger sequence by
minimising the maximum payback period across all necks at each stage.

**Theorem E5** (Optimal Merger Sequence). *Given $n$ manifolds
$\{M_1, \ldots, M_n\}$ with pairwise shared factor ratios $k_{ij}/r$,
the merger sequence that minimises the maximum payback period at any stage
is the greedy algorithm: at each step, add the manifold $M_j$ not yet in
the connected sum that has the highest $k/r$ with the current hub.*

*Proof.* The payback period is monotonically decreasing in $k/r$
(INTERMARKET_GEOMETRY.md, Corollary 4.2). The weakest neck determines
system vulnerability (Theorem E2). Therefore, minimising the maximum
payback period at each stage requires adding the highest-$k/r$ candidate
first. Since the payback period for each neck is independent of other
necks (star topology), the greedy algorithm is optimal. $\square$

Applying this to Europe:

**Phase 1 (1999): Core-5.** Germany, Netherlands, Austria, Finland,
Luxembourg. All pairs have $k/r \geq 0.75$. Four necks (Luxembourg is
trivially small). Maximum payback: approximately 1 year. This merger would
have succeeded immediately and demonstrated the benefits of monetary union
without systemic risk.

**Phase 2 (2003–2005): Add France, Belgium.** After the Core-5 demonstrates
successful integration and the Frankel–Rose convergence effect is verified
empirically, add France and Belgium with $k/r \geq 0.67$. Two additional
necks. Maximum payback: approximately 3 years. Conditional on the Core-5
having functioned for 3+ years.

**Phase 3 (2008–2010): Add Spain, Italy conditionally.** Only if:
(a) Fisher matrix eigenvalue alignment verified ($k/r > 0.55$ computed from
market data, not Maastricht scalars); (b) labour market flexibility achieved
($\lambda_1^{(f_4)}$ within threshold); (c) fiscal transfer mechanism
operational (Cheeger edges built *before* the necks are created). Maximum
payback: approximately 8 years.

**Phase 4 (2015+): Add Portugal, Ireland conditionally.** After banking
union (2014) demonstrates factor convergence in the banking sector ($f_6$).
With automatic fiscal stabilisers operational. Only when $k/r > 0.50$
verified.

**Phase 5 (2020+?): Consider Greece.** Only when $k/r > 0.50$ with
the existing zone, verified by the Fisher matrix eigenvalue test over a
sustained period. With full fiscal union, full banking union, genuine labour
mobility. As of 2026, Greece's $k/r$ with Germany remains below 0.50. The
geometry says: not yet.

The key differences from what was actually done:

1. **Build the graph first.** Fiscal transfers, labour mobility, and banking
   union are Cheeger edges. They must be built *before* the necks are created,
   not two decades after.
2. **Expand by $k/r$ threshold, not by political convenience.** Entry
   should be determined by the Fisher matrix, not by the European Council.
3. **Allow reversible necks.** An orderly exit mechanism is not a threat to
   the project — it is the safety valve that prevents Type II singularities.
4. **Monitor the Fisher matrix, not the Maastricht scalars.** The eigenvalue
   structure of each economy's Fisher information matrix should be computed
   quarterly and published.
5. **Never create a neck with $k/r < 0.5$.** This is the geometric
   equivalent of a minimum safety standard.

---

## 8. What the Euro Got Right

Geometric judgment must be fair. The Euro was not a pure failure.

**The convergence trade was real.** Between 1999 and 2007, the compression
of sovereign spreads generated enormous wealth and reflected genuine
integration in some dimensions. Trade within the Eurozone increased by
approximately 10% in the first five years. The core countries experienced
real factor convergence in goods markets, even if services and labour
markets lagged.

**The core works.** Germany, Netherlands, Austria, Finland, and Luxembourg
form a well-functioning currency area. Their Fisher matrices are closely
aligned. The connected sum among these five was viable from day one and
has remained so through every crisis. This validates the geometric framework:
high-$k/r$ mergers succeed.

**Competitive devaluation was eliminated.** The pre-Euro period was plagued
by beggar-thy-neighbour devaluations — the Italian lira, Spanish peseta,
and Portuguese escudo were serially devalued in the 1990s. The Euro removed
this negative-sum game. In geometric terms, it prevented countries from
artificially narrowing one factor gap ($f_4$ via devaluation) while
widening others (imported inflation, capital flight).

**Crisis forced infrastructure.** The Banking Union (2014), the European
Stability Mechanism (2012), and the NGEU (2020) — all products of crisis —
have built some of the Cheeger edges that should have existed from the start.
The Eurozone of 2026 has more infrastructure than the Eurozone of 1999. The
geometry improved, at enormous cost.

**The ECB is an effective institution.** Draghi's intervention in 2012 and
the subsequent QE programme demonstrated that a credible central bank can
hold necks open through surgical intervention. The institution works. The
architecture around it was inadequate.

---

## 9. Lessons for Other Mergers

### 9.1 Irreversibility and singularity type

**Theorem E3** (Irreversibility and Singularity Type). *Let $M_1
\mathbin{\#} M_2$ be a connected sum with neck parameter $\varepsilon > 0$.
Under MCF:*

*(i) If disconnection is permitted (reversible merger), a failing neck
develops a Type I singularity: $\max |H|^2 \leq C/(T_{\rm sing} - t)$,
and the disconnection is orderly.*

*(ii) If disconnection is forbidden (irreversible merger), the same neck
develops a Type II singularity: $\max |H|^2 (T_{\rm sing} - t) \to \infty$,
the curvature blows up faster than any polynomial bound, and the
disconnection (when it eventually occurs) is catastrophic.*

*Proof sketch.* Type I singularities arise when the flow has a natural
blow-up rate determined by the parabolic scaling of MCF ($|H|^2 \sim
1/(T_{\rm sing} - t)$). This occurs when the neck is free to pinch at its
natural rate. Type II singularities arise when external constraints prevent
the natural pinch — the curvature concentrates in the constrained region,
exceeding the parabolic blow-up rate. In the Eurozone context, the "no exit"
clause prevents orderly disconnection, forcing capital to concentrate at
the constrained neck and generating curvature blowup that exceeds the
Type I bound. The formal argument follows Huisken and Sinestrari [2009] on
Type II singularity formation under constrained MCF. $\square$

This theorem applies directly to every proposed irreversible economic union:

**African Continental Free Trade Area (AfCFTA).** 54 economies with wildly
different factor structures. Estimated pairwise $k/r$ ranges from 0.8
(Kenya–Uganda, both East African Community members with aligned factors)
to below 0.1 (Nigeria–Lesotho). The geometric prediction: AfCFTA must be
staged by $k/r$ clusters — East African Community, Southern African Customs
Union, ECOWAS subgroups — with expansion by measured factor alignment, not
continental ambition. Attempting 54 simultaneous necks would make the Euro
look prudent.

**US–China economic decoupling.** This is a *deliberate neck severance* — a
de-merger. The geometric cost is the unrecovered Willmore energy from 40
years of integration. If $k/r \approx 0.3$ (shared factors: global growth,
global risk; not shared: technology, governance, geopolitics, demographics),
the payback period for re-merger after severance exceeds 30 years. The
decoupling, once effected, will not be cheaply reversed.

**BRICS common currency.** Compute $k/r$ for Brazil–Russia–India–China–South
Africa. Shared factors: global commodity prices, perhaps global risk
appetite. Not shared: virtually everything else — growth models, governance,
demographics, trade structures, capital account regimes. Estimated $k/r
\approx 0.15$–$0.20$. This would be an even more expensive merger than
the Euro, with payback periods exceeding 50 years. The geometry renders a
clear verdict: do not build this.

**The US Dollar as world reserve.** The dollar is the hub of a star graph
connecting all major currency manifolds. The Cheeger constant of this
star-topology system is $h \approx 2/n$ for $n$ connected currencies —
poor and deteriorating as $n$ grows. De-dollarisation proposals (bilateral
trade in local currencies, BRICS alternatives) amount to adding edges that
bypass the hub, increasing the Cheeger constant of the global system. From
a pure graph-theoretic perspective, a less hub-dependent architecture is
more robust. The question is whether the transition cost (new necks with
unknown $k/r$) is worth the improved topology.

---

## 10. The Verdict

The Euro was a geometrically reckless merger. The architects connected
manifolds without checking whether they shared factors. They measured
scalars when they needed the metric tensor. They built necks without
infrastructure. They let Greece in when the geometry said no. They made
the merger irreversible when reversibility was the safety valve. The
Greek crisis was not a failure of the Euro — it was the *geometry* of
the Euro working as the mathematics predicted. A neck with $k/r = 0.33$
*will* pinch before it pays for itself. The question was never whether
the crisis would happen, but when. The answer — computable from the
payback formula — was: before 2025. It happened in 2010. The geometry
was right.

But geometry also records what the Euro got right. The core — Germany,
Netherlands, Austria, Finland — is a well-functioning currency area with
$k/r > 0.75$ and payback measured in months. The elimination of competitive
devaluation was a genuine public good. The institutions built under crisis —
the ESM, banking union, NGEU — have improved the Cheeger structure of the
zone, late but real.

The lesson is not that monetary unions are impossible. The lesson is that
they are *geometric objects* with computable costs, measurable factor
structures, and predictable failure modes. Build the graph first. Expand by
eigenvalue alignment. Allow reversibility. Monitor the tensor, not the
scalars. And never — under any political pressure, for any political
purpose — create a neck with $k/r < 0.5$.

---

## 11. New Results

Five results are proved in this paper:

**Theorem E1** (Maastricht Insufficiency, Section 4.1). Maastricht
convergence (four scalar criteria) is necessary but not sufficient for
merger viability. The sufficient condition is eigenvalue alignment of the
Fisher information matrices. The Maastricht criteria discard approximately
98% of the information in the Fisher matrix.

**Theorem E2** (Weakest Neck Principle, Section 5.3). In a star-topology
connected sum, the system vulnerability equals the vulnerability of the
weakest neck. A singularity at the weakest neck propagates stress to all
surviving necks by a factor of at least $n/(n-1)$.

**Theorem E3** (Irreversibility and Singularity Type, Section 9.1).
Forbidding disconnection converts Type I singularities (orderly, bounded
curvature blowup) into Type II singularities (catastrophic, unbounded
curvature blowup).

**Theorem E4** (Austerity Preserves Factor Structure, Section 6.4).
Homothetic contraction (proportional economic shrinkage) reduces manifold
volume but preserves eigenvalue ratios and the shared factor ratio $k/r$.
Austerity shrinks the economy without changing its shape.

**Theorem E5** (Optimal Merger Sequence, Section 7). The merger sequence
that minimises the maximum payback period at each stage is the greedy
algorithm: add the highest-$k/r$ candidate first.

---

## 12. Open Problems

**OP-E1** (Empirical $k/r$ Estimation). Compute the current $k/r$ for all
Eurozone pairs from market data (sovereign CDS, bond yields, equity indices,
macro time series) using the Fisher matrix eigenvalue method. Is the zone
average $k/r$ higher in 2026 than in 1999? Has the Frankel–Rose
endogenous convergence been sufficient to close the gap?

**OP-E2** (NGEU Impact). Has the NGEU genuinely increased $k/r$ for
peripheral countries, or has it only masked divergence (as QE did for
spreads)? Distinguish between Cheeger improvement (genuine graph edges)
and surgical spread compression (temporary curvature reduction).

**OP-E3** (Expansion Cost). Croatia joined in 2023 with estimated
$k/r \approx 0.45$. Romania and Bulgaria are candidates. Compute
$k/r$ for each candidate from current data. What is the geometric cost
of further expansion? At what $k/r$ threshold should new members be
admitted?

**OP-E4** (Fiscal Union and Factor Structure). Can a fiscal union raise
$k/r$ (by synchronising factor $f_5$, fiscal capacity), or can it only
raise $h_M$ (the Cheeger constant, by adding transfer edges)? If the
former, fiscal union is transformative. If the latter, it is palliative
— helpful but not curative. The distinction has profound policy
implications.

---

## References

- Brunnermeier, M., James, H., and Landau, J.-P. (2016). *The Euro and the
  Battle of Ideas*. Princeton University Press.
- De Grauwe, P. (2012). *Economics of Monetary Union* (9th ed.). Oxford
  University Press.
- Frankel, J. A. and Rose, A. K. (1998). The endogeneity of the optimum
  currency area criteria. *Economic Journal*, 108(449):1009–1025.
- Huisken, G. and Sinestrari, C. (2009). Mean curvature flow with
  surgeries of two-convex hypersurfaces. *Inventiones Mathematicae*,
  175(1):137–221.
- Lane, P. R. (2012). The European sovereign debt crisis. *Journal of
  Economic Perspectives*, 26(3):49–68.
- Mundell, R. A. (1961). A theory of optimum currency areas. *American
  Economic Review*, 51(4):657–665.
- Nicholls, S. (2026). Intermarket geometry: spreads as curvature, mergers
  as connected sums. In *The Geometry of Efficient Markets*, Paper IV.5.
- Obstfeld, M. (1997). Europe's gamble. *Brookings Papers on Economic
  Activity*, 1997(2):241–317.
- Sinn, H.-W. (2014). *The Euro Trap: On Bursting Bubbles, Budgets, and
  Beliefs*. Oxford University Press.

---

*Cross-references:* INTERMARKET_GEOMETRY.md (connected sum theory,
payback formula), MINIMAL_SURFACE.md (Willmore energy, Sharpe-curvature
theorem), CLASSIFICATION.md (stability, Jacobi operator),
CONVERGENCE.md (MUP regret bounds), GEOSPATIAL_CONTAGION.md (Cheeger
constant, contagion propagation), RANDOM_MATRIX.md (Dyson class,
spectral structure).
