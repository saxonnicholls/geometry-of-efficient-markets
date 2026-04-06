# Experiment Plan: Using Institutional Data

**Saxon Nicholls** — me@saxonnicholls.com

## Data Budget

Databento charges ~$0.50/GB. We design experiments to be data-efficient.

| Download | Dataset | Schema | Symbols | Period | Est. Size | Est. Cost |
|:---------|:--------|:-------|:--------|:-------|:----------|:----------|
| **Batch 1: Daily bars** | GLBX.MDP3 | ohlcv-1d | ES, CL, ZN, ZB, ZF, ZT, GC, SI, NG | 2010-2024 | ~50MB | ~$0.03 |
| **Batch 2: Equity daily** | XNAS.ITCH | ohlcv-1d | Top 50 S&P 500 stocks | 2018-2024 | ~100MB | ~$0.05 |
| **Batch 3: LOB sample** | XNAS.ITCH | mbp-10 | AAPL, MSFT, SPY | 1 week (Dec 2024) | ~2GB | ~$1.00 |
| **Batch 4: Options daily** | OPRA.PILLAR | ohlcv-1d | SPX, SPY options | 2020-2024 | ~500MB | ~$0.25 |
| **Batch 5: Futures minute** | GLBX.MDP3 | ohlcv-1m | ES, CL, ZN | 2020-2024 | ~1GB | ~$0.50 |
| **Batch 6: LOB deep** | XNAS.ITCH | mbo | AAPL | 1 day | ~5GB | ~$2.50 |
| **Total** | | | | | ~9GB | **~$4.33** |

Well within the $125 free credit.

## Experiments Mapped to Data

### Tests 6-10 (Classification) — Use Batch 1 + 2

| Test | What we need | Databento source |
|:-----|:-----------|:----------------|
| 6. Three market types | Sector ETFs + futures daily | Batch 1 (futures) + existing sector ETFs |
| 7. Dyson class (eigenvalue spacings) | 50 stocks daily | Batch 2 |
| 8. Fat tail index | 50 stocks daily | Batch 2 |
| 9. Jacobi diffusion fit | Portfolio weight changes daily | Batch 2 |
| 10. LTCM stability index | Spread strategies daily | Batch 1 (ZN, ES futures) |

### Tests 11-15 (Applications) — Use Batch 1 + 2 + 4

| Test | What we need | Databento source |
|:-----|:-----------|:----------------|
| 11. MIF vs cap-weight | 50 stocks daily | Batch 2 |
| 12. Pairs trading threshold | Correlated stock pairs daily | Batch 2 |
| 13. Cheeger vs VIX | Sector ETFs daily | Existing + Batch 1 |
| 14. Kelly-Shapley attribution | 25 portfolios monthly | Existing FF data |
| 15. LZ-Kelly correspondence | Daily returns discretised | Existing |

### Microstructure Tests (NEW) — Use Batch 3 + 6

| Test | What we need | Databento source |
|:-----|:-----------|:----------------|
| M1. Bid-ask = Fisher-Rao distance | L2 order book (mbp-10) | Batch 3 |
| M2. Market impact = curvature | L2 + trades | Batch 3 |
| M3. Kyle's lambda = Fisher info | Trades + order flow | Batch 3 |
| M4. Flash crash anatomy | L3 order book (mbo) | Batch 6 |
| M5. Spectral hierarchy | Daily + minute + tick | Batch 2 + 5 + 3 |

### Vol Surface Tests (NEW) — Use Batch 4

| Test | What we need | Databento source |
|:-----|:-----------|:----------------|
| V1. Smile = curvature | SPX options daily OHLCV | Batch 4 |
| V2. No-arb = curvature bounds | SPX options by strike/expiry | Batch 4 |
| V3. VVIX = Willmore energy | VIX + VVIX + SPX options | Batch 4 + FRED |
| V4. Vol surface MCF | Options time series | Batch 4 |

### Intermarket Tests (NEW) — Use Batch 1 + 5

| Test | What we need | Databento source |
|:-----|:-----------|:----------------|
| I1. Brent-WTI spread geometry | CL futures + BZ (ICE Brent) | Batch 1 |
| I2. Treasury curve factors | ZT, ZF, ZN, ZB futures | Batch 1 |
| I3. Cross-asset correlations | ES + CL + ZN + GC | Batch 1 |

## Execution Order

**Phase 1 (now):** Download Batches 1-2 (~$0.08). Run Tests 6-15.
**Phase 2:** Download Batch 4 (~$0.25). Run vol surface tests.
**Phase 3:** Download Batch 3 (~$1.00). Run microstructure tests.
**Phase 4:** Download Batch 5-6 (~$3.00). Run deep microstructure + intermarket.

Total estimated cost: ~$4.33 out of $125 free credit.
