"""Small local feature-store exercise, separate from the Feast integration."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from mlops_practicals.data import FEATURES


def materialize_features(records: list[dict[str, str]], project_root: Path) -> dict[str, object]:
    feature_rows = [
        {"student_id": row["Name"], **{name: row[name] for name in FEATURES}}
        for row in records
    ]
    store_path = project_root / "feature_store"
    store_path.mkdir(parents=True, exist_ok=True)

    offline_path = store_path / "offline_features.csv"
    with offline_path.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=["student_id", *FEATURES])
        writer.writeheader()
        writer.writerows(feature_rows)

    online_path = store_path / "online_features.json"
    online_path.write_text(
        json.dumps({row["student_id"]: row for row in feature_rows}, indent=2),
        encoding="utf-8",
    )
    retrieved = json.loads(online_path.read_text(encoding="utf-8"))[feature_rows[0]["student_id"]]
    return {
        "feature_count": len(FEATURES),
        "entities_ingested": len(feature_rows),
        "online_lookup_example": retrieved,
        "offline_store": "feature_store/offline_features.csv",
        "online_store": "feature_store/online_features.json",
        "implementation": "local teaching demo; practical 5 also includes Feast configuration",
    }