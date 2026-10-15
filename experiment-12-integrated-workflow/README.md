# Experiment 12 - Integrated MLOps Workflow and Results

## Aim
Connect source control, data validation/versioning, feature management, training, experiment tracking, tests, CI, containerization, and serving.

## Requirements
- Python 3.10 or later and dependencies from the repository root
- Git; optional DVC, Feast, and MLflow integrations
- Docker Engine for container execution

## Procedure
1. Run `python -m mlops_practicals.run_pipeline`.
2. Run `python -m pytest -v experiment-08-testing/tests`.
3. Review model metrics and the consolidated report.
4. Execute DVC, Feast, MLflow, GitHub Actions, and Docker steps only after configuring each tool.
5. Demonstrate `/predict` and explain which results are synthetic or local-only.

## Integrated result
The local workflow exercises generated-data validation, feature materialization, model comparison, artifact creation, tests, and API behavior. DVC/Feast/MLflow services, hosted Actions, and Docker remain unverified here; see [`OUTPUT.txt`](./OUTPUT.txt) and the [consolidated report](../reports/MLOps_Practical_Lab_Report.md).

## Viva questions
1. Which identifiers link code, data, experiment, and deployed model versions?
2. Which infrastructure in this project is local-only?
3. What additional monitoring and rollback controls would a production service need?

## Concept summary
An MLOps workflow connects artifacts and checks across the model lifecycle while retaining reproducibility and explicit provenance.

## Outcome summary
The local workflow is integrated and tested. Unavailable services are recorded as limitations rather than completed deployments.