# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repository is

Teaching notebooks (Python and R, `.ipynb`) for the module EAIF (AI for Finance; the repository
keeps the module's former code `EDFB` as its name so that URLs stay valid), plus the
CSV datasets they use and one flipped-class activity (`activity/`, a Varian 2014 replication
with starter and solutions notebooks). There is no build, no package, no test suite, no
lint config and no requirements file. Students run the notebooks in Google Colab via the
badges in `README.md`; nothing here is meant to be installed locally.

`code_review_report.md` (2026-09-16) is the last full code-and-didactics review; its
Appendix A lists every finding and its "Resolution log" says what was fixed and what is
still open. Read it before making substantive changes to a unit.

## The contract that makes notebooks work: paths are load-bearing

Two things are hard-wired to the `main` branch of `github.com/umatter/EDFB`:

- **Data is fetched from raw GitHub URLs**, e.g.
  `https://raw.githubusercontent.com/umatter/EDFB/main/data/banking.csv`. A notebook only
  works once the data file it names is committed and pushed to `main`. Renaming or moving a
  file under `data/` or `activity/` silently breaks every notebook that fetches it, in Python
  *and* R. Grep for the old URL across all `.ipynb` files before renaming. No notebook falls
  back to different data (no KaggleHub, no simulated series); a missing file is an error.
  The one exception is the Varian starter/solutions, which offer a Colab upload of the *same*
  `FLS-data.csv` only if the URL load fails, for offline use.
- **Colab badges in `README.md`** point at `blob/main/<path>`. Renaming a notebook without
  updating its badge produces a dead link. Keep the README's structure list equal to
  `git ls-files`.

**Data still missing for unit 04.** `04_EAIF_Clustering_in_Finance.ipynb` Parts 2 and 3
load `data/borrower_companies.csv`, `data/financialdata_original.csv` and
`data/financialdata_extra.csv`, which are not in the repo or its history. The code was
verified against synthetic mocks; the cluster-naming prose carries marked placeholders that
must be rewritten from the real data once the files are added (with a licence entry in
`data/LICENSE_ATTRIBUTION.md`).

## Notebook conventions

- **Self-bootstrapping setup cell first.** Python notebooks assume Colab's preinstalled
  stack and install extras inline. R notebooks set the Posit Package Manager binary mirror
  (`packagemanager.posit.co/cran/__linux__/jammy/latest`) before an `install_if_missing`
  loop; keep the mirror, source builds time out on Colab.
- **Python and R notebooks are paired translations.** Units 01 and 02 are cell-for-cell
  mirrors (same cell count, headings, order and prose); unit 03 shares structure but not
  cell numbering. A change to one side must be mirrored on the other, or the divergence
  stated in the prose (e.g. sklearn's default L2 penalty vs `glm`, rpart's `cp` vs sklearn's
  `ccp_alpha`, stratified vs random split).
- **The decision-time leakage rule** ("at the moment the decision is made, which columns
  are already known?") is stated in each unit and drives every feature-set choice.
  `duration` is dropped from predictors in units 02 and 03 and used only as the target in
  unit 01; the BTC section uses lagged log returns only. Do not reintroduce leaky columns.
- **Every metric sits next to its baseline** (majority class, zero forecast, or the global
  model) and AUC is computed from probabilities. Insight cells are written from an actual
  run and say "in this run"; do not write conclusions before running.
- **Fixed seeds everywhere** (`random_state=0/42/123`, `set.seed(...)`). Keep them; the
  prose quotes numbers that depend on them.
- **Outputs are stripped** in the repo. Execute to verify, then strip before committing.
- **Solutions live beside starters**: `notebooks/{Python,R}/solutions/` and
  `activity/Varian_Replication_Solutions.ipynb`. Every exercise in a student notebook has a
  matching solution; do not leak solution code into the student notebook.
- `notebooks/R/archive/` holds superseded R versions, unmaintained; one of them
  (`CFA_Challenge_*_R`) has markdown pasted into code cells and does not parse. Do not
  promote or edit them; delete when convenient.
- **The take-home case (`notebooks/Python/takehome/`) is Python-only** and its data
  (`data/mortgage2026/`) are simulated by the committed `generate_mortgage_data.py`
  (seed 2026; `--check` prints the planted logit-vs-boosting AUC gap). The student and
  solutions notebooks differ only in the exercise cells; the student notebook must run top to
  bottom with the exercise cells left as comments. **The solutions notebook is deliberately not
  in the repo yet**: it lives in the gitignored `_solutions/` (removed from `main` on 2026-09-22
  so students cannot see it before the deadline; it is still in the pushed history before that
  date). When it is released, move it back to `notebooks/Python/solutions/` and restore its
  README badge. Design spec and plan under `docs/superpowers/`.

## Working with notebooks from the shell

No Jupyter is installed system-wide; `python3` and `Rscript` are. The workflow that was used
for the 2026-09 fix pass, and that should be repeated for any substantive change:

1. Create a venv with `pandas numpy scikit-learn statsmodels matplotlib seaborn scipy
   nbformat nbclient ipykernel` and register its kernel (`python -m ipykernel install --user
   --name edfb-venv`).
2. Edit notebooks as JSON (a small helper with `dump/get/set/insert/delete/strip/check/run`
   subcommands is easy to rebuild: `check` compiles every Python code cell or parses every R
   cell with `Rscript -e 'parse(file=...)'`; `run` executes with `nbclient`, comments out
   `!`/`%` lines and forces the Agg backend).
3. Execute a **temp copy** in which `https://raw.githubusercontent.com/umatter/EDFB/main/`
   is replaced by the local repo path, so unpushed data files resolve. Never leave a local
   path in a repo notebook.
4. R notebooks: extract the code cells to a script with the same URL substitution and the
   install lines neutralised, install the needed packages into a scratch library, and run
   `R_LIBS=<lib> Rscript script.R`; exit 0 with no `Error` lines is the bar. Unit 03 needs
   `gamlr`, `xgboost` (2.x API), `grf`, `rpart`, `randomForest`, `data.table`, `pROC`.
5. Strip outputs, run `check` on every touched notebook, and confirm `git status` shows only
   the intended files.

The final verification is still a fresh "Runtime → Run all" on Colab from the README badge
after pushing. Say so if that step was not done.

## Data licensing

`data/LICENSE_ATTRIBUTION.md` has an entry for every dataset in use: the ESG dataset
(Kaggle, CC BY 4.0, simulated), the BTC daily close series (Binance public API, with the
script that rebuilds it), the UCI bank-marketing data (CC BY 4.0), the Kaggle graduate
admission data, and the Fernández-Ley-Steel growth data from Varian's openICPSR replication
package. Any new dataset under `data/` or `activity/` needs an entry there. The group-work
notebook must keep stating that the ESG data are simulated.

## Git hygiene

`.gitignore` excludes `slides/`, anything starting with `_`, and `.aider*`. The README asks
for changes to notebooks to arrive as pull requests rather than direct edits to `main`.
