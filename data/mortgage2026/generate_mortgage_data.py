#!/usr/bin/env python3
"""Simulated mortgage book of Aare-Säntis Regionalbank AG (EAIF take-home case, AS 2026).

Writes, next to this script,
  mortgages.csv          the book: 10,000 mortgages originated 2019-2022 with the 36-month outcome
  applications_2026.csv  500 new applications, same columns, no outcome, no post-origination column

Deterministic: the same seed gives byte-identical files. No real bank, property or household
is behind any row; the trouble rate is inflated for teaching. Licence: CC BY 4.0 (EAIF course).

    python3 generate_mortgage_data.py           # write the two CSVs
    python3 generate_mortgage_data.py --check   # also fit a logit and a boosted model, print test AUCs
"""
import pathlib
import sys

import numpy as np
import pandas as pd

SEED = 2026
N_BOOK, N_APPS = 10_000, 500
HERE = pathlib.Path(__file__).resolve().parent

CANTONS = ["ZH", "BE", "AG", "LU", "SO", "SG", "TG"]
CANTON_P = [0.30, 0.20, 0.15, 0.10, 0.07, 0.10, 0.08]
CANTON_LEVEL = {"ZH": 9.75, "LU": 9.45, "AG": 9.35, "SG": 9.30, "BE": 9.25, "TG": 9.20, "SO": 9.10}
ENERGY = np.array(["A", "B", "C", "D", "E", "F", "G"])
ENERGY_EFFECT = {"A": 0.06, "B": 0.04, "C": 0.02, "D": 0.0, "E": -0.02, "F": -0.04, "G": -0.06}
# (fixed-rate, SARON) mortgage rates in percent by origination year
RATES = {2019: (1.10, 0.95), 2020: (1.05, 0.90), 2021: (1.10, 0.90), 2022: (2.30, 1.60), 2026: (1.50, 1.00)}

# trouble model (log-odds); see the design spec for what each term plants
B0, B_LTV, B_AFF, B_SE, B_AGE, B_CORNER, B_INTER, B_BUR, B_CONV, B_OVER = -4.5, 0.3, 0.3, 0.0, 1.0, 3.2, 2.2, 10.0, 600.0, 0.5


def simulate(n, years, rng, with_outcome, prefix):
    canton = rng.choice(CANTONS, size=n, p=CANTON_P)
    house = rng.random(n) < 0.42
    area = np.where(house, rng.lognormal(np.log(150), 0.22, n), rng.lognormal(np.log(100), 0.25, n))
    area = np.clip(area, 45, 320).round(0)
    rooms = np.round(np.clip(area / 28 + rng.normal(0, 0.5, n), 1.5, 9) * 2) / 2
    year_built = np.where(rng.random(n) < 0.35, rng.integers(2000, 2023, n), rng.integers(1900, 2000, n))
    age_p = 2023 - year_built
    dist = np.clip(rng.exponential(8, n), 0.3, 40).round(1)
    energy = ENERGY[np.clip(np.round(age_p / 25 + rng.normal(0, 1.0, n)), 0, 6).astype(int)]
    price_resid = rng.normal(0, 0.12, n)
    log_price = (np.vectorize(CANTON_LEVEL.get)(canton) + 0.92 * np.log(area) + 0.10 * house
                 - 0.004 * age_p + 0.00003 * age_p ** 2 - 0.022 * dist
                 + np.vectorize(ENERGY_EFFECT.get)(energy) + price_resid)
    price = np.round(np.exp(log_price), -3)
    income = np.exp(np.log(150_000) + 0.45 * (log_price - log_price.mean()) + rng.normal(0, 0.30, n))
    income = np.round(np.clip(income, 55_000, 900_000), -2)
    age_b = np.clip(rng.normal(44, 10, n), 25, 72).round(0).astype(int)
    emp = rng.choice(["employed", "self_employed", "retired"], size=n, p=[0.78, 0.14, 0.08])
    emp = np.where(age_b >= 66, "retired", np.where((emp == "retired") & (age_b < 60), "employed", emp))
    years_client = np.clip(rng.exponential(6, n), 0, 30).round(0).astype(int)
    ltv = np.clip(rng.normal(0.70, 0.10, n), 0.30, 0.90)
    loan = np.round(ltv * price, -3)
    ltv = (loan / price).round(3)
    saron = rng.random(n) < 0.35
    year = rng.choice(years, size=n)
    fixed_years = np.where(saron, 0, rng.choice([5, 10], size=n, p=[0.45, 0.55]))
    base_rate = np.array([RATES[y][1] if s else RATES[y][0] for y, s in zip(year, saron)])
    rate = np.round(base_rate + rng.normal(0, 0.12, n) + np.where(fixed_years == 10, 0.25, 0), 2)
    amort_type = rng.choice(["direct", "indirect"], size=n, p=[0.6, 0.4])
    amort = np.maximum(0, loan - (2 / 3) * price) / 15
    afford = ((0.05 * loan + 0.01 * price + amort) / income).round(3)
    burden = (rate / 100 * loan / income).round(4)
    df = pd.DataFrame({
        "id": [f"{prefix}{i:05d}" for i in range(1, n + 1)],
        "canton": canton, "property_type": np.where(house, "house", "apartment"),
        "living_area_m2": area, "rooms": rooms, "year_built": year_built,
        "distance_center_km": dist, "energy_label": energy, "purchase_price": price,
        "household_income": income, "age": age_b, "employment": emp, "years_client": years_client,
        "loan_amount": loan, "rate_type": np.where(saron, "saron", "fixed"), "fixed_years": fixed_years,
        "interest_rate": rate, "amortisation": amort_type, "origination_year": year,
        "ltv": ltv, "affordability": afford, "actual_burden": burden,
    })
    if with_outcome:
        self_emp = (emp == "self_employed").astype(float)
        corner = ((afford > 1 / 3) & (ltv > 0.80)).astype(float)
        z = (B0 + B_LTV * (ltv - 0.70) + B_AFF * (afford - 0.33) + B_SE * self_emp
             + B_AGE * ((age_b - 45) / 15) ** 2
             + saron * (B_BUR * burden + B_CONV * np.maximum(burden - 0.06, 0) ** 2)
             + B_CORNER * corner + B_INTER * self_emp * saron
             + B_OVER * price_resid / 0.12)
        p = 1 / (1 + np.exp(-z))
        df["trouble_36m"] = (rng.random(n) < p).astype(int)
        df["reminders_sent"] = rng.poisson(0.25 + 4.0 * df["trouble_36m"], n)
    return df


def write_files():
    rng = np.random.default_rng(SEED)
    book = simulate(N_BOOK, [2019, 2020, 2021, 2022], rng, True, "M")
    apps = simulate(N_APPS, [2026], rng, False, "A")
    book.to_csv(HERE / "mortgages.csv", index=False, lineterminator="\n")
    apps.to_csv(HERE / "applications_2026.csv", index=False, lineterminator="\n")
    print(f"mortgages.csv: {len(book)} rows, trouble rate {book.trouble_36m.mean():.3f}")
    print(f"applications_2026.csv: {len(apps)} rows")
    return book


def check(book):
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler
    drop = ["id", "purchase_price", "loan_amount", "origination_year", "trouble_36m", "reminders_sent"]
    X = pd.get_dummies(book.drop(columns=drop), drop_first=True).astype(float)
    y = book["trouble_36m"]
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)
    sc = StandardScaler().fit(X_tr)
    logit = LogisticRegression(max_iter=3000).fit(sc.transform(X_tr), y_tr)
    gbm = HistGradientBoostingClassifier(learning_rate=0.05, max_iter=500, early_stopping=True,
                                         random_state=0).fit(X_tr, y_tr)
    a_logit = roc_auc_score(y_te, logit.predict_proba(sc.transform(X_te))[:, 1])
    a_gbm = roc_auc_score(y_te, gbm.predict_proba(X_te)[:, 1])
    corner = (book.affordability > 1 / 3) & (book.ltv > 0.80)
    print(f"test AUC  logit {a_logit:.3f}  gradient boosting {a_gbm:.3f}  gap {a_gbm - a_logit:.3f}")
    print(f"trouble rate in the corner {y[corner].mean():.3f} vs elsewhere {y[~corner].mean():.3f}")
    assert 0.04 <= y.mean() <= 0.10, "base rate outside 4-10%"
    assert a_gbm - a_logit >= 0.03, "planted non-linearity too weak"


if __name__ == "__main__":
    book = write_files()
    if "--check" in sys.argv:
        check(book)
