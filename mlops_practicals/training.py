"""Model training and evaluation for the student-performance demo."""

from __future__ import annotations

import json
from pathlib import Path

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from mlops_practicals.data import FEATURES


def train_and_evaluate(records: list[dict[str, str]], project_root: Path) -> dict[str, object]:
    features = [[float(record[name]) for name in FEATURES] for record in records]
    labels = [record["Performance"] for record in records]
    train_x, test_x, train_y, test_y = train_test_split(
        features, labels, test_size=0.25, random_state=42, stratify=labels
    )

    candidates = {
        "baseline_logistic_regression": make_pipeline(
            StandardScaler(), LogisticRegression(max_iter=1000, random_state=42)
        ),
    }
    grid = GridSearchCV(
        DecisionTreeClassifier(random_state=42),
        {"max_depth": [2, 3, None], "min_samples_leaf": [1, 2, 4]},
        cv=3,
        scoring="f1_macro",
    ).fit(train_x, train_y)
    candidates["grid_search_decision_tree"] = grid.best_estimator_

    randomized = RandomizedSearchCV(
        RandomForestClassifier(random_state=42),
        {
            "n_estimators": [50, 100, 150],
            "max_depth": [3, None],
            "min_samples_leaf": [1, 2, 4],
        },
        n_iter=4,
        cv=3,
        scoring="f1_macro",
        random_state=42,
        n_jobs=1,
    ).fit(train_x, train_y)
    candidates["random_search_random_forest"] = randomized.best_estimator_

    results = {}
    for name, estimator in candidates.items():
        estimator.fit(train_x, train_y)
        predictions = estimator.predict(test_x)
        results[name] = {
            "accuracy": round(accuracy_score(test_y, predictions), 4),
            "precision_macro": round(precision_score(test_y, predictions, average="macro", zero_division=0), 4),
            "recall_macro": round(recall_score(test_y, predictions, average="macro", zero_division=0), 4),
            "f1_macro": round(f1_score(test_y, predictions, average="macro", zero_division=0), 4),
        }

    best_name = max(results, key=lambda name: results[name]["f1_macro"])
    best_model = candidates[best_name]
    artifact_path = project_root / "artifacts" / "student_performance.joblib"
    artifact_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(best_model, artifact_path)

    output = {
        "dataset": "deterministic synthetic student-performance data",
        "seed": 42,
        "records": len(records),
        "train_records": len(train_y),
        "test_records": len(test_y),
        "metric_for_selection": "f1_macro",
        "models": results,
        "selected_model": best_name,
        "best_parameters": (
            grid.best_params_ if best_name == "grid_search_decision_tree"
            else randomized.best_params_ if best_name == "random_search_random_forest"
            else {}
        ),
        "artifact": "artifacts/student_performance.joblib",
        "caveat": "Synthetic demonstration results are not evidence of real-world model quality.",
    }
    output_path = project_root / "outputs" / "model_comparison.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(output, indent=2), encoding="utf-8")
    return output