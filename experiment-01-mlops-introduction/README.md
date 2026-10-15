# Experiment 1 - Introduction to MLOps

## Aim
Compare software development, DevOps, and MLOps; explain the lifecycle, key components, production challenges, and tool choices.

## Requirements
- Python 3.10 or later for the workflow demonstration
- A Markdown viewer that renders Mermaid for the lifecycle diagram

## Procedure
1. Compare the responsibilities and outputs in the table below.
2. Review the lifecycle diagram in [`mlops-lifecycle.mmd`](./mlops-lifecycle.mmd).
3. Run `python experiment-01-mlops-introduction/workflow_demo.py` from the repository root.
4. Identify the data, feature, model, and monitoring artifacts that need versioning.

## Comparison

| Software development | DevOps | MLOps |
| --- | --- | --- |
| Versions application code and releases | Automates build, test, release, and infrastructure | Versions code, data, features, experiments, and models; validates and monitors model behavior |
| Output is deterministic for a fixed build and input | Production system is the deployed application | Results also depend on training data, feature logic, parameters, and model artifacts |

Key components include source control, data/version management, feature stores, automated pipelines, experiment tracking, model registries, tests/CI, packaging, serving, and monitoring. Production challenges include data and concept drift, training-serving skew, reproducibility, latency, privacy, explainability, rollback, and artifact costs. Tools surveyed here: Git/GitHub Actions, DVC, Feast, MLflow, scikit-learn, FastAPI, and Docker.

## Observed result
The lifecycle demonstration ran successfully. Its captured terminal output is in [`OUTPUT.txt`](./OUTPUT.txt); the diagram is a conceptual workflow reference.

## Viva questions
1. Which artifacts must be versioned in an ML system besides source code?
2. How does concept drift differ from data quality failure?
3. Which lifecycle stage would detect training-serving skew?

## Concept summary
MLOps extends DevOps practices to data, features, experiments, models, and production feedback.

## Outcome summary
The comparison and lifecycle diagram provide an overview of an operational ML system.