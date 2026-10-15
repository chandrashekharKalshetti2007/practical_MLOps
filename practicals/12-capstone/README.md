# Practical 12: Complete MLOps Workflow

## Output and report

This repository connects dataset generation/validation, feature materialization, experiment comparison and tuning, tests, CI, container packaging, and model serving. Run `python -m mlops_practicals.run_pipeline` and `python -m unittest discover -s tests -v` for the local workflow. Use the linked practical reports for DVC, Feast, MLflow, GitHub Actions, and Docker setup.

The run summary is `outputs/run_summary.json`; model metrics are `outputs/model_comparison.json`. The trained artifact is written to `artifacts/student_performance.joblib`. Add that artifact to DVC when a remote is configured, and commit the DVC metadata plus reports to GitHub.

**Demonstration checklist:** show data validation; compare experiment metrics; run the tests; inspect the CI artifact; build and run the container; call `/predict`; explain the synthetic-data caveat and how a DVC/Feast/MLflow remote would be configured for a real deployment.