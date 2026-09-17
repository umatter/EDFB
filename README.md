# EAIF — AI for Finance Notebooks

A collection of Python and R notebooks for teaching and practicing core data science topics in the module EAIF (AI for Finance). The repository keeps its historical name `EDFB` so that existing links to it stay valid; the notebooks and data are loaded from it by URL. Notebooks are prepared for easy sharing via GitHub + Google Colab: each one loads its data from this repository by URL and, for R, installs its packages in a setup cell, so it runs end-to-end without manual environment setup. The course arc is linear regression (01), logistic regression and the campaign decision (02), trees, ensembles and an optional causal-ML coda (03), clustering (04), a graded group project, and a flipped-class replication of Varian (2014).

## Repository structure

- notebooks/
  - Python/
    - 01_EAIF_Linear_Models_1.ipynb
    - 02_EAIF_Logistic_Regression.ipynb
    - 03_EAIF_Advanced_Models_Python.ipynb
    - 04_EAIF_Comparison_clustering_methods.ipynb
    - 04_EAIF_Clustering_in_Finance.ipynb
    - solutions/
      - 01_EAIF_Linear_Models_1_Exercise_Solutions.ipynb
      - 02_EAIF_Logistic_Regression_Solutions.ipynb
    - groupwork/
      - Group_Work_AS_2026.ipynb
  - R/
    - 01_EAIF_Linear_Models_1.ipynb
    - 02_EAIF_Logistic_Regression.ipynb
    - 03_EAIF_Advanced_Models_R.ipynb
    - solutions/
      - 02_EAIF_Logistic_Regression_Solutions.ipynb
    - archive/ (superseded R versions, kept for reference; not maintained)
- activity/
  - EAIF_SML3_Flipped_Class_Instructions_Varian.pdf (and .docx source): pre-class reading questions, in-class plan
  - Varian_Replication_Starter.ipynb, Varian_Replication_Solutions.ipynb
  - FLS-data.csv
- data/
  - banking.csv (units 01 to 03)
  - Admission_Predict.csv (unit 01)
  - data_BTC.csv (unit 01; daily BTC close, see LICENSE_ATTRIBUTION.md)
  - company_esg_financial_dataset.csv (unit 04 optional exercise; simulated data, CC BY 4.0, see LICENSE_ATTRIBUTION.md)
  - esg2026/ (AS 2026 group work; simulated ESG and stock-return panel, CC BY 4.0, see LICENSE_ATTRIBUTION.md)
    - firm_year_panel.csv
    - esg_scores_restated.csv
    - stock_returns_monthly.csv
    - factors_monthly.csv
    - universe_current.csv
    - README.md
  - LICENSE_ATTRIBUTION.md

**Missing data for unit 04.** `04_EAIF_Clustering_in_Finance.ipynb` Parts 2 and 3 expect
`data/borrower_companies.csv`, `data/financialdata_original.csv` and `data/financialdata_extra.csv`,
which are not in this repository. Until they are added (with a licence entry in
`data/LICENSE_ATTRIBUTION.md`), only Part 1 of that notebook runs.

## Open in Google Colab

You can run each notebook directly in your browser using Google Colab. You need a Google account (free) to use Colab.

- Python
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/01_EAIF_Linear_Models_1.ipynb) Linear Regression (synthetic data, univariate admission example, multivariate banking model, Bitcoin returns)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/solutions/01_EAIF_Linear_Models_1_Exercise_Solutions.ipynb) Linear Regression: Exercise Solutions
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/02_EAIF_Logistic_Regression.ipynb) Logistic Regression (linear probability model, logit, odds ratios, threshold and campaign profit)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/solutions/02_EAIF_Logistic_Regression_Solutions.ipynb) Logistic Regression: Exercise Solutions
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/03_EAIF_Advanced_Models_Python.ipynb) Advanced Models: Lasso, Trees, Random Forests, Boosting, plus an optional causal-ML section (about one minute of extra runtime)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/activity/Varian_Replication_Starter.ipynb) Varian (2014) Replication: Starter (lasso variable selection on the growth data, OLS vs random forest; read the paper before class, see the instruction sheet)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/activity/Varian_Replication_Solutions.ipynb) Varian (2014) Replication: Solutions (instructor version)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/04_EAIF_Comparison_clustering_methods.ipynb) Clustering Methods Comparison (Toy Datasets)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/04_EAIF_Clustering_in_Finance.ipynb) Clustering in Finance (Credit Risk & Company Valuation; Parts 2 and 3 need the missing data files)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/Python/groupwork/Group_Work_AS_2026.ipynb) **Group Work AS 2026: ESG and Firm Performance with Machine Learning** (scaffold plus graded tasks; the assignment brief, rubric and deadline placeholder are in the notebook; the dataset is simulated)
- R
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/R/01_EAIF_Linear_Models_1.ipynb) Linear Regression (R)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/R/02_EAIF_Logistic_Regression.ipynb) Logistic Regression (R)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/R/solutions/02_EAIF_Logistic_Regression_Solutions.ipynb) Logistic Regression: Exercise Solutions (R)
  - [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/umatter/EDFB/blob/main/notebooks/R/03_EAIF_Advanced_Models_R.ipynb) Advanced Models: Lasso, Trees, Random Forests, Boosting, plus an optional causal-ML section (R)

Recommended student workflow:
1. Click the corresponding "Open in Colab" badge above.
2. In Colab, go to "File → Save a copy in Drive" to work on your own copy.
3. Run the first "Setup" cell, then "Runtime → Run all".
4. Do not edit the original GitHub notebooks.

## Datasets

Every dataset a notebook needs is in this repository (see the structure above), with the one
exception of the three unit 04 files noted there. Data are loaded from
`https://raw.githubusercontent.com/umatter/EDFB/main/...` at the top of the relevant section,
so a notebook works only once its data file is on the `main` branch; there are no fallbacks
to other sources. Sources and licences for all five datasets are recorded in
`data/LICENSE_ATTRIBUTION.md`. The ESG dataset used in the group
work is simulated, which the notebook states and asks students to discuss.

## Reproducibility

- Python notebooks use only packages preinstalled on Colab (pandas, numpy, scikit-learn, statsmodels, matplotlib, seaborn, scipy); nothing is pip-installed.
- R notebooks use a "Setup" cell that installs packages from the Posit Package Manager binary mirror for fast installs on Colab.
- Seeds are fixed throughout (`random_state` / `set.seed`), and the explanatory text refers to results "in this run", since library versions on Colab change over time.
- Before a notebook is linked here it should be executed end-to-end on a fresh Colab runtime. Notebooks are stored with outputs cleared.

## For maintainers

`CLAUDE.md` documents the conventions (URL-loaded data, Python/R mirrors in units 01 and 02, the decision-time leakage rule, stripped outputs) and a local execution workflow. `code_review_report.md` is the full code-and-didactics review of 2026-09-16 with a resolution log of what was fixed and what is still open (the unit 04 data files, the group-work deadline).

## Acknowledgements

Original Python notebooks were created by [Branka Hadji Misheva](https://www.bfh.ch/en/about-bfh/people/w76zvjktchs5/). R notebooks and groupwork notebook by [Ulrich Matter](umatter.github.io) with assistance from [Claude Code](https://www.anthropic.com/claude-code) and reviewed by o3 and GPT-5.

## Contributing

Issues and pull requests are welcome. For changes to notebooks, please open a PR rather than editing the main branch directly.
