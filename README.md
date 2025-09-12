# EDFB — Digital Finance & Banking Notebooks

A collection of Python and R notebooks for teaching and practicing core data science topics in Digital Finance & Banking. Notebooks are prepared for easy sharing via GitHub + Google Colab and include self-bootstrapping setup cells so they run end-to-end without manual environment setup.

## Repository structure

- notebooks/
  - Python/
    - EDFB_Digital_Finance_&_Banking_Linear_Models_1.ipynb
    - EDFB_Digital_Finance_&_Banking_Logistic_Regression.ipynb
    - Clustering_and_Credit_Risk.ipynb
    - groupwork/
      - Group_Work_AS_2025.ipynb
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
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/groupwork/Group_Work_AS_2025.ipynb) **Group Work AS 2025: ESG Investment Analysis & ML Portfolio Optimization**
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

Datasets are either provided in the `data/` folder or are directly downloaded by the notebooks from other sources. See the noteboooks for details on the datasets used.

## Reproducibility

- Python notebooks pin library versions in the top “Setup” cell (pip installs).
- R notebooks use a “Setup” cell that installs packages from the Posit Package Manager binary mirror for fast, reproducible installs on Colab.
- Notes at the top of each notebook indicate the runtime versions they were tested on.

## Acknowledgements

Original Python notebooks were created by [Branka Hadji Misheva](https://www.bfh.ch/en/about-bfh/people/w76zvjktchs5/). R notebooks and groupwork notebook by [Ulrich Matter]((umatter.github.io) with assistance from [Claude Code](https://www.anthropic.com/claude-code) and reviewed by o3 and GPT-5.

## Contributing

Issues and pull requests are welcome. For changes to notebooks, please open a PR rather than editing the main branch directly.
