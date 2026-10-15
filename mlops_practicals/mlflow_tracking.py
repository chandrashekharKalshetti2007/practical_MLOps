"""Optional MLflow logging wrapper for the model comparison exercise."""

from __future__ import annotations

from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn

from mlops_practicals.data import generate_synthetic_records
from mlops_practicals.training import train_and_evaluate


def log_demo_run() -> None:
    mlflow.set_experiment("student-performance-practicals")
    with mlflow.start_run(run_name="grid-and-random-search"):
        result = train_and_evaluate(generate_synthetic_records(), Path.cwd())
        mlflow.log_param("dataset", result["dataset"])
        mlflow.log_param("seed", result["seed"])
        mlflow.log_param("selected_model", result["selected_model"])
        mlflow.log_params(result["best_parameters"])
        for model_name, metrics in result["models"].items():
            for metric_name, value in metrics.items():
                mlflow.log_metric(f"{model_name}.{metric_name}", value)
        mlflow.log_artifact("outputs/model_comparison.json")
        model = joblib.load("artifacts/student_performance.joblib")
        model_info = mlflow.sklearn.log_model(model, artifact_path="student-performance-model")
        mlflow.register_model(model_info.model_uri, "student-performance-demo")


if __name__ == "__main__":
    log_demo_run()