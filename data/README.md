# Data Directory

**Saxon Nicholls** — me@saxonnicholls.com

## Structure

```
data/
├── raw/              ← Downloaded from sources (not checked into git)
├── processed/        ← Cleaned, aligned, ready for experiments
├── download_all.py   ← Master download script (run once)
├── process_all.py    ← Master processing script (run after download)
└── README.md         ← This file
```

## Data Sources (All Free)

| Dataset | Source | Method | Size | Updates |
|:--------|:-------|:-------|:-----|:--------|
| Fama-French 25 portfolios (5×5 size/value) | Kenneth French Data Library | HTTP | ~5MB | Monthly |
| Fama-French 5 factors (daily) | Kenneth French Data Library | HTTP | ~8MB | Monthly |
| Fama-French 100 portfolios (10×10) | Kenneth French Data Library | HTTP | ~15MB | Monthly |
| S&P 500 constituent prices | Yahoo Finance (yfinance) | API | ~200MB | Daily |
| US Treasury yield curve | FRED (Federal Reserve) | API | ~2MB | Daily |
| VIX / VVIX / SKEW indices | CBOE via FRED | API | ~1MB | Daily |
| Fed funds rate | FRED | API | ~0.5MB | Daily |
| CPI components (for inflation paper) | FRED / BLS | API | ~3MB | Monthly |
| 10Y sovereign yields (DE, FR, IT, ES, GR) | FRED | API | ~2MB | Daily |
| BTC/ETH/SOL daily prices | Yahoo Finance (yfinance) | API | ~5MB | Daily |

**Total download: ~240MB. Total processed: ~50MB.**

## How to Download

### Step 1: Set up API keys

```bash
cp .env.example .env
# Edit .env and add your API keys
```

**FRED key (free):** Go to https://fred.stlouisfed.org/docs/api/api_key.html
→ Create account → My Account → API Keys → Request API Key. Takes 2 minutes.

**Databento key (paid):** https://databento.com — institutional market data.
Provides tick-level ITCH, OHLCV, options (OPRA), futures (CME/ICE), crypto.

**Massive key (paid):** https://massive.com (formerly Polygon.io) — equities,
options, forex, crypto. REST API.

### Step 2: Download free data (no API key needed for Fama-French)

```bash
cd data/
python download_all.py          # FF, yfinance, FRED, crypto, sectors → raw/
python process_all.py            # Clean and align → processed/
```

### Step 3: Download institutional data (requires API keys)

```bash
python download_databento.py     # Equities, futures, options, crypto (tick-level)
python download_massive.py       # S&P 500 daily, options snapshots
python download_itch.py          # NASDAQ ITCH L3 order book (for microstructure)
```

### Requirements

```bash
pip install pandas numpy scipy pyarrow requests yfinance
pip install databento              # Databento SDK
pip install polygon-api-client     # Massive/Polygon SDK
pip install itch                   # ITCH parser (martinobdl/ITCH)
```

## Reproducibility

The processed data is deterministic given the download date. For exact
reproducibility of published results, we fix the data snapshot to:

**Snapshot date: 2024-12-31**

All experiments use data up to this date. The download scripts accept a
`--end-date` parameter to reproduce this exact snapshot.

## Licence

All data sources are freely available for academic and research use.
Fama-French data: public domain. Yahoo Finance: personal use licence.
FRED: public domain (US government data).
