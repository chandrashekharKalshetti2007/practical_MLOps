# Practical 5: Feature Store

## Output

`mlops_practicals.feature_store` demonstrates reusable feature definitions and local offline/online retrieval. The pipeline writes an offline CSV and an online JSON lookup for generated student IDs. These are teaching artifacts, not a production online database.

For the Feast extension, install `requirements-tracking.txt`, then define the entity/view and source in `feature_store.py` and `feature_store.yaml`. Register and retrieve features with `feast apply`, `feast materialize-incremental`, and `FeatureStore.get_online_features`. Use the Feast CLI only after supplying a timestamped feature source; the generated local-store output is already recorded in `outputs/run_summary.json`.

Benefits analyzed: one definition shared across models, consistent training/serving features, point-in-time offline retrieval, and lower duplicated feature logic. Watch for stale online values, leakage, and ownership/access controls.