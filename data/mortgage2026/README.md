# Mortgage book of Aare-Säntis Regionalbank AG (EAIF take-home case, AS 2026)

Simulated by the course with `generate_mortgage_data.py` in this folder. There is no real
bank, property or household behind any row, and the rate of payment trouble is several
times higher than in a real Swiss mortgage book so that the exercises have enough cases
to learn from. Licence: CC BY 4.0 (EAIF course, Bern University of Applied Sciences).

| File | Rows | Content |
|---|---|---|
| `mortgages.csv` | 10,000 | the bank's book: mortgages originated 2019–2022 with the outcome after 36 months |
| `applications_2026.csv` | 500 | this year's applications: the same columns without the outcome and without `reminders_sent` |

## Columns

| Column | Unit / values | Known at decision time? |
|---|---|---|
| `id` | `M00001…` (book), `A00001…` (applications) | yes |
| `canton` | ZH, BE, AG, LU, SO, SG, TG | yes |
| `property_type` | apartment, house | yes |
| `living_area_m2` | m² | yes |
| `rooms` | number of rooms (Swiss counting, halves allowed) | yes |
| `year_built` | year | yes |
| `distance_center_km` | km to the nearest regional centre | yes |
| `energy_label` | A (best) to G | yes |
| `purchase_price` | CHF | yes |
| `household_income` | CHF gross per year | yes |
| `age` | borrower's age in years | yes |
| `employment` | employed, self_employed, retired | yes |
| `years_client` | years as a client of the bank | yes |
| `loan_amount` | CHF | yes |
| `rate_type` | fixed, saron (variable) | yes |
| `fixed_years` | 5 or 10 for fixed, 0 for saron | yes |
| `interest_rate` | percent per year at origination | yes |
| `amortisation` | direct, indirect (via pillar 3a) | yes |
| `origination_year` | 2019–2022 (book), 2026 (applications) | yes |
| `ltv` | loan / purchase price | yes |
| `affordability` | (5 % imputed interest on the loan + 1 % of the price for maintenance + amortisation of the part above two-thirds LTV over 15 years) / income; the Swiss lending rule says at most 1/3 | yes |
| `actual_burden` | interest_rate / 100 × loan / income (the interest actually paid; `interest_rate` is in percent) | yes |
| `trouble_36m` | 1 if arrears of 90 days or more, or a forced restructuring, within 36 months | outcome |
| `reminders_sent` | payment reminders sent during the 36 months | **no** (known only afterwards) |
