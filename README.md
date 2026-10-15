# MLOps Practical Laboratory

**Department of Computer Engineering - Practical Experiments 01-12**

This repository is the practical record for a twelve-part MLOps laboratory. Each experiment includes its aim, requirements, procedure, implementation references, captured output, and result.

## Experiments

| No. | Experiment | Open |
|---:|---|---|
| 01 | Introduction to MLOps and lifecycle | [Experiment 01](./experiment-01-mlops-introduction/README.md) |
| 02 | Git, GitHub, branching, and collaboration | [Experiment 02](./experiment-02-git-github/README.md) |
| 03 | Dataset versioning with DVC | [Experiment 03](./experiment-03-dvc/README.md) |
| 04 | Data validation and processing pipeline | [Experiment 04](./experiment-04-data-pipeline/README.md) |
| 05 | Feature management and feature-store concepts | [Experiment 05](./experiment-05-feature-store/README.md) |
| 06 | Model training and experiment tracking with MLflow | [Experiment 06](./experiment-06-mlflow/README.md) |
| 07 | Baseline model and hyperparameter search | [Experiment 07](./experiment-07-model-selection/README.md) |
| 08 | Unit testing for data validation and serving | [Experiment 08](./experiment-08-testing/README.md) |
| 09 | Continuous integration with GitHub Actions | [Experiment 09](./experiment-09-ci/README.md) |
| 10 | Containerization with Docker | [Experiment 10](./experiment-10-docker/README.md) |
| 11 | REST API model serving | [Experiment 11](./experiment-11-rest-api/README.md) |
| 12 | Integrated MLOps workflow and results | [Experiment 12](./experiment-12-integrated-workflow/README.md) |

## Run the Python practicals

Python 3.10 or later is recommended. From the repository root:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m mlops_practicals.run_pipeline
python -m pytest -v experiment-08-testing/tests
```

The experiment-specific READMEs explain each procedure. Docker requires Docker Engine/Desktop to be installed and running. DVC, Feast, and MLflow integrations are optional dependencies listed in `requirements-tracking.txt`.

## Repository files

- `requirements.txt` installs the core ML, API, and test dependencies.
- `.gitignore` excludes local environments, caches, and secrets.
- `.github/workflows/ci.yml` runs tests and the demo pipeline on GitHub Actions.
- [`reports/MLOps_Practical_Lab_Report.md`](./reports/MLOps_Practical_Lab_Report.md) summarizes all experiments and verified results.
- Each experiment's `OUTPUT.txt` records commands and results. If a tool or service was unavailable, the output states that limitation instead of presenting a sample as a successful run.

## Data and reproducibility

The supplied `processed_student_data.csv` contains only five named records. It is validated locally but is not copied into this repository or used to claim model quality. Training uses a deterministic synthetic dataset; the generated target is derived from its input features, so the perfect demonstration scores are not evidence of real-world performance.

Re-run the pipeline and tests in your own environment if your course requires individually witnessed or machine-specific execution. Remote DVC storage, Feast services, MLflow registry, GitHub Actions, and Docker results are recorded only after they are actually configured and run.