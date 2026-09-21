# Dataset License Attribution

## ESG & Financial Performance Dataset

**File:** `company_esg_financial_dataset.csv`

**Original Source:** https://www.kaggle.com/datasets/shriyashjagtap/esg-and-financial-performance-dataset

**Author:** Shriyash Jagtap

**License:** Creative Commons Attribution 4.0 International License (CC BY 4.0)  
https://creativecommons.org/licenses/by/4.0/

### License Requirements

This dataset is licensed under CC BY 4.0, which requires:

1. **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.
2. **No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

### Attribution Statement

This work uses the "ESG & Financial Performance Dataset" by Shriyash Jagtap, available at https://www.kaggle.com/datasets/shriyashjagtap/esg-and-financial-performance-dataset, licensed under CC BY 4.0 (https://creativecommons.org/licenses/by/4.0/).

### Dataset Description

The dataset contains simulated financial and ESG data for 1,000 global companies across 9 industries and 7 regions from 2015 to 2025. It includes:

- Company identifiers and metadata
- Financial metrics (Revenue, Profit Margin, Market Cap, Growth Rate)
- ESG scores (Overall, Environmental, Social, Governance)
- Environmental impact measures (Carbon Emissions, Water Usage, Energy Consumption)

**Total Records:** 11,000 observations (1,000 companies × 11 years)  
**Columns:** 16 variables  
**File Size:** ~1.2 MB
## Bitcoin daily close series

**File:** `data_BTC.csv`

**Source:** Binance public market-data API (`GET /api/v3/klines`, symbol `BTCUSDT`, interval `1d`), retrieved 2026-09-16.

**Content:** one row per UTC day from 2017-08-17 onward with the daily close price of the BTC/USDT spot pair, used as a proxy for BTC-USD. Columns: `Date`, `BTC-USD.Close`. Only the close is included so that no same-day information can leak into a return-forecasting exercise.

**Terms:** Binance market data is provided for personal and non-commercial use; this copy is redistributed for teaching purposes only, with attribution. Reproduce it with the following script if a refresh is needed:

```python
import urllib.request, json, csv, datetime as dt
rows, start = [], 1502928000000
while True:
    url = f"https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1d&limit=1000&startTime={start}"
    batch = json.load(urllib.request.urlopen(url, timeout=30))
    if not batch: break
    rows += batch; start = batch[-1][0] + 86400000
    if len(batch) < 1000: break
with open("data_BTC.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["Date", "BTC-USD.Close"])
    for r in rows[:-1]:
        w.writerow([dt.datetime.utcfromtimestamp(r[0]/1000).strftime("%Y-%m-%d"), float(r[4])])
```

## Bank Marketing dataset

**File:** `banking.csv` (41,188 rows; used by units 01, 02, 03 and their solutions)

**Original source:** UCI Machine Learning Repository, "Bank Marketing" (bank-additional-full), donated by S. Moro, P. Cortez and P. Rita. https://archive.ics.uci.edu/dataset/222/bank+marketing

**Reference:** Moro, S., Cortez, P., and Rita, P. (2014). A Data-Driven Approach to Predict the Success of Bank Telemarketing. *Decision Support Systems*, 62, 22-31.

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0), as stated on the UCI repository page.

**Changes made:** this copy keeps 16 of the original attributes plus the outcome (`job`, `default`, `month`, `day_of_week` are not included) and recodes the outcome `y` from yes/no to 1/0.

## Graduate admission dataset

**File:** `Admission_Predict.csv` (400 rows, columns `GRE_score`, `Admit`; used by unit 01's univariate step)

**Original source:** Kaggle, "Graduate Admission" by Mohan S Acharya (Admission_Predict.csv, 400 rows). https://www.kaggle.com/datasets/mohansacharya/graduate-admissions

**Reference:** Acharya, M. S., Armaan, A., and Antony, A. S. (2019). A Comparison of Regression Models for Prediction of Graduate Admissions. IEEE International Conference on Computational Intelligence in Data Science.

**License:** listed on Kaggle as CC0 1.0 (public domain). Verify against the dataset page before redistributing beyond teaching use.

**Changes made:** only the GRE score and the chance-of-admit columns are kept, renamed to `GRE_score` and `Admit`.

## Cross-country growth data (Varian replication package)

**File:** `../activity/FLS-data.csv` (72 countries, `y` = average growth rate of GDP per capita 1960-1992, plus 41 regressors)

**Source:** replication package of Varian, H. R. (2014), "Big Data: New Tricks for Econometrics", *Journal of Economic Perspectives* 28(2): 3-28, openICPSR project 113925 (AEA Data and Code Repository), file from the variable-selection (lasso) example of section 6.3.

**Underlying data:** Fernández, C., Ley, E., and Steel, M. F. J. (2001). Model Uncertainty in Cross-Country Growth Regressions. *Journal of Applied Econometrics*, 16(5), 563-576 (data originally assembled by Sala-i-Martin, 1997). The column order in this file follows the Bayesian-model-averaging ranking of Varian's comparison table.

**Terms:** redistributed here for teaching with attribution; the openICPSR project's terms of use apply. Students are pointed to the openICPSR record as the authoritative source.

## data/esg2026/ (simulated ESG and stock-return panel)

Simulated by the EAIF course (Ulrich Matter, Bern University of Applied Sciences) in September 2026 for the
AS 2026 group assignment. No real firms; the generator is not part of this repository. Licence: CC BY 4.0.
The files deliberately contain data problems that the assignment asks students to find.

## Simulated mortgage book (take-home case, AS 2026)

**Files:** `mortgage2026/mortgages.csv`, `mortgage2026/applications_2026.csv`

**Source:** simulated by the course with `mortgage2026/generate_mortgage_data.py` (deterministic, seed 2026). No real bank, property or household is behind any row; the trouble rate is inflated for teaching.

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0), EAIF course, Bern University of Applied Sciences. Attribution: "Simulated mortgage book, EAIF: AI for Finance (BFH), CC BY 4.0."
