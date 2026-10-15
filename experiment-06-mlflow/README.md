# Experiment 6 - Model Training and Experiment Tracking with MLflow

## Aim
Train candidate models, log parameters/metrics/artifacts, compare runs, and register the selected model.

## Requirements
- Core dependencies plus MLflow from `requirements-tracking.txt`
- Run from the repository root so the shared pipeline can find its artifacts

## Procedure
1. Run `python -m mlops_practicals.run_pipeline` to train candidates and write the selected model.
2. Run `python -m mlops_practicals.mlflow_tracking` to log the comparison and register the selected model.
3. Start `mlflow ui` and inspect the `student-performance-practicals` experiment.

## Captured result
The tracking wrapper is implemented, but no MLflow run ID or registry version is claimed because MLflow was not installed/run in the captured environment. See [`OUTPUT.txt`](./OUTPUT.txt).

## Viva questions
1. Which parameters and metrics should be logged to reproduce a model run?
2. How does a model registry differ from an artifact store?
3. Why should model selection use a declared validation metric?

## Concept summary
MLflow connects training runs, metrics, artifacts, and model lifecycle metadata.

## Outcome summary
The logging/registration workflow is prepared and requires the optional MLflow dependency and local tracking store to execute.