# Practical 6: Experiment Tracking with MLflow

## Output

Install optional tools with `python -m pip install -r requirements-tracking.txt`, then run:

```powershell
python -m mlops_practicals.mlflow_tracking
mlflow ui
```

The wrapper logs dataset/seed/model parameters, comparison metrics, and the comparison JSON artifact to the `student-performance-practicals` experiment, then registers the selected model as `student-performance-demo`. Use the MLflow UI to compare runs and inspect the registered version. Do not claim an MLflow run until the command has completed; the base environment did not include MLflow.