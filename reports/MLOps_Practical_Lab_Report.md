# MLOps Practical Laboratory - Consolidated Report

**Department:** Computer Engineering  
**Experiments:** 01-12  
**Execution environment:** Windows, Python 3.13.6

## Summary of verified results

| No. | Practical | Verified result |
|---:|---|---|
| 01 | MLOps lifecycle | Lifecycle script and Mermaid workflow are included; command output is captured. |
| 02 | Git and GitHub | Project repository was pushed to GitHub on `main`; a merge-conflict exercise is documented but was not run. |
| 03 | DVC | Reproduction stage is configured; DVC remote tracking/push was not run because DVC is not installed. |
| 04 | Data pipeline | 240 synthetic rows validated with no missing values; the supplied CSV was checked separately (5 rows, 0 missing). |
| 05 | Feature store | Local demonstration materialized four features for 240 entities with offline and online example files; Feast was not run. |
| 06 | MLflow | Tracking/model-registry wrapper is included; an MLflow run was not captured because the optional dependency/service was unavailable. |
| 07 | Model selection | Baseline logistic regression, grid-search decision tree, and randomized-search random forest each scored 1.0000 accuracy and macro-F1 on the synthetic holdout. |
| 08 | Automated tests | Seven tests passed for data, feature materialization, model artifacts, and API behavior. |
| 09 | Continuous integration | GitHub Actions Python CI run #2 passed on commit `b158519` and uploaded its output artifact. |
| 10 | Docker | Dockerfile is included; Docker Engine was unavailable, so no image/container run is claimed. |
| 11 | Model API | Automated HTTP tests passed for valid prediction and invalid input; network latency was not measured. |
| 12 | Integrated workflow | Local data, feature, model, test, and API components were exercised; external-service limitations remain explicit. |

## Experiment 4 - data validation

The generated demonstration dataset has 240 records, 6 columns, and no missing values. The provided `processed_student_data.csv` has five named rows (Good=3, Needs Improvement=2) and no missing cells. It was validation-only; no model metrics are reported from it.

## Experiment 7 - model comparison

The 240-row deterministic synthetic dataset was split into 180 training rows and 60 held-out test rows using a stratified split. All three estimators achieved 1.0000 for accuracy, macro-precision, macro-recall, and macro-F1. This is expected because the synthetic class label is calculated from the synthetic input features. These scores validate the code path, not generalization to real student data.

## Reproducibility and limitations

- Per-experiment commands and observed results are in the corresponding `OUTPUT.txt` files.
- DVC, Feast, and MLflow dependencies and remote/service configuration were not installed or executed in this environment.
- GitHub Actions run #2 passed on commit `b158519`; the workflow and run log are linked from Experiment 9.
- Docker was unavailable; the Dockerfile was not built.
- Prediction endpoint tests use an in-process ASGI transport; no network benchmark or calibrated-confidence analysis was run.
- Synthetic data is suitable for demonstrating deterministic workflow behavior only. Replace it with approved, sufficiently large data before drawing domain conclusions.
