# EDFB — Digital Finance & Banking Notebooks

A collection of Python and R notebooks for teaching and practicing core data science topics in Digital Finance & Banking. Notebooks are prepared for easy sharing via GitHub + Google Colab and include self-bootstrapping setup cells so they run end-to-end without manual environment setup.

## Repository structure

- notebooks/
  - Python/
    - EDFB_Digital_Finance_&_Banking_Linear_Models_1.ipynb
    - EDFB_Digital_Finance_&_Banking_Logistic_Regression.ipynb
    - Clustering_and_Credit_Risk.ipynb
  - R/
    - EDFB_Digital_Finance_&_Banking_Linear_Models_1_R.ipynb
    - EDFB_Digital_Finance_&_Banking_Logistic_Regression_R.ipynb
    - Clustering_and_Credit_Risk_R.ipynb
- data/
  - banking.csv (optional; auto-downloaded if missing)
  - borrower_companies.csv (optional; auto-downloaded if missing)
- data_BTC.csv (optional; auto-downloaded or simulated if missing)

## Open in Google Colab

You can run each notebook directly in your browser using Google Colab. You need a Google account (free) to use Colab.

- Python
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/EDFB_Digital_Finance_%26_Banking_Linear_Models_1.ipynb) Linear Models (Univariate)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/EDFB_Digital_Finance_%26_Banking_Logistic_Regression.ipynb) Logistic Regression
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/Clustering_and_Credit_Risk.ipynb) Clustering and Credit Risk
- R
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/R/EDFB_Digital_Finance_%26_Banking_Linear_Models_1_R.ipynb) Linear Models (Univariate, R)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/R/EDFB_Digital_Finance_%26_Banking_Logistic_Regression_R.ipynb) Logistic Regression (R)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/R/Clustering_and_Credit_Risk_R.ipynb) Clustering and Credit Risk (R)

Recommended student workflow:
1. Click the corresponding “Open in Colab” badge above.
2. In Colab, go to “File → Save a copy in Drive” to work on your own copy.
3. Run the first “Setup” cell, then “Runtime → Run all”.
4. Do not edit the original GitHub notebooks.

## Datasets

- banking.csv: expected at data/banking.csv. If not present, notebooks will download from:
  - https://raw.githubusercontent.com/umatter/EDFB/main/data/banking.csv
- borrower_companies.csv: expected at data/borrower_companies.csv. If not present, notebooks will download from:
  - https://raw.githubusercontent.com/umatter/EDFB/main/data/borrower_companies.csv
  Used in the Clustering and Credit Risk notebooks (both Python and R).
- data_BTC.csv: expected at repo root (./data_BTC.csv). If not present, notebooks will attempt to download the same filename from the repo; if unavailable, they simulate a small time series so the notebooks remain runnable.

## Reproducibility

- Python notebooks pin library versions in the top “Setup” cell (pip installs).
- R notebooks use a “Setup” cell that installs packages from the Posit Package Manager binary mirror for fast, reproducible installs on Colab.
- Notes at the top of each notebook indicate the runtime versions they were tested on.

## Contributing

Issues and pull requests are welcome. For changes to notebooks, please open a PR rather than editing the main branch directly.
