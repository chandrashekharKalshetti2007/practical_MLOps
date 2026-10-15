# Experiment 5 - Feature Management and Feature Store

## Aim
Define reusable features and compare offline historical retrieval with low-latency online retrieval.

## Requirements
- Core Python dependencies for the local CSV/JSON demonstration
- Feast from `requirements-tracking.txt` for the optional registry/provider extension

## Procedure
1. Review the shared feature definitions in `mlops_practicals/feature_store.py` and the Feast files in this directory.
2. Run `python -m mlops_practicals.run_pipeline` from the repository root.
3. Inspect `feature_store/offline_features.csv` and `feature_store/online_features.json`.
4. For Feast, supply a timestamped source, apply definitions, materialize data, and query historical and online features.

## Observed result
The local demonstration materialized four features for 240 synthetic entities and retrieved an online example. Feast registration/materialization was not executed; see [`OUTPUT.txt`](./OUTPUT.txt).

Benefits include shared feature definitions, less duplicated logic, and improved training/serving consistency. Risks include stale online values, leakage, ownership, and access controls.

## Viva questions
1. Why does historical retrieval need event timestamps?
2. What causes training-serving skew?
3. Which components are still missing from a local CSV/JSON demo?

## Concept summary
A feature store centralizes feature definitions and retrieval for both training and serving.

## Outcome summary
Offline and online retrieval concepts are demonstrated locally; the Feast service workflow remains an optional extension.