# MLOps Practicals

A single Git repository containing the 12 MLOps practicals, shared Python code, reports, and integration examples. Each practical has its own folder under `practicals/`.

## Important data note

The provided `processed_student_data.csv` has only five named records. Do not use it to claim model performance or commit it to a public repository. The project generates a deterministic synthetic dataset for training and evaluation; it is explicitly labeled synthetic. You may validate your local CSV with the command below, which reports schema and label counts without copying names into the repository.

## Setup and run

Use Python 3.10 or newer. In PowerShell from this folder:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mlops_practicals.run_pipeline
python -m unittest discover -s tests -v
```

The pipeline writes a synthetic CSV, a serialized model, feature-store demo files, and JSON summaries. Generated data and model files are git-ignored. Keep small reports and screenshots in the relevant practical folder; use DVC for data/model artifacts when configured.

To validate the supplied CSV without training on it:

```powershell
python -m mlops_practicals.run_pipeline --source-csv ..\processed_student_data.csv
```

## Practical index

1. [MLOps introduction and lifecycle](practicals/01-introduction/README.md)
2. [Git and collaboration workflow](practicals/02-git-workflow/README.md)
3. [DVC dataset versioning](practicals/03-dvc/README.md)
4. [Data pipeline](practicals/04-data-pipeline/README.md)
5. [Feature store](practicals/05-feature-store/README.md)
6. [MLflow experiment tracking](practicals/06-mlflow/README.md)
7. [Model selection and tuning](practicals/07-model-selection/README.md)
8. [Automated tests](practicals/08-testing/README.md)
9. [Continuous integration](practicals/09-ci/README.md)
10. [Docker packaging](practicals/10-docker/README.md)
11. [REST model API](practicals/11-api/README.md)
12. [Complete MLOps workflow](practicals/12-capstone/README.md)

## Tooling status

Git and Docker were not available in the creation environment, and no GitHub credentials were provided. Practical 2, 9, and 10 include the repository workflow, CI configuration, and Docker files, but their remote/engine-specific runs must be performed after installing and signing in to those tools. MLflow, DVC, and Feast examples are optional integrations in `requirements-tracking.txt` and require their setup steps in the corresponding practicals.