"""Data helpers shared by the MLOps practicals."""

from __future__ import annotations

import csv
import random
from pathlib import Path

FIELDS = ("Name", "Marks", "Attendance", "Study_Hours", "Performance_Score", "Performance")
FEATURES = ("Marks", "Attendance", "Study_Hours", "Performance_Score")
LABELS = ("Good", "Needs Improvement")


def generate_synthetic_records(count: int = 240, seed: int = 42) -> list[dict[str, str]]:
    """Create deterministic, explicitly synthetic records for model exercises."""
    if count < 2:
        raise ValueError("count must be at least 2")

    randomizer = random.Random(seed)
    records = []
    for index in range(1, count + 1):
        marks = round(randomizer.uniform(35, 100), 1)
        attendance = round(randomizer.uniform(40, 100), 1)
        study_hours = randomizer.randint(1, 8)
        score = round(0.55 * marks + 0.30 * attendance + 1.5 * study_hours, 3)
        performance = "Good" if score >= 67 else "Needs Improvement"
        records.append({
            "Name": f"Synthetic_{index:03d}",
            "Marks": str(marks),
            "Attendance": str(attendance),
            "Study_Hours": str(study_hours),
            "Performance_Score": str(score),
            "Performance": performance,
        })
    return records


def write_records(path: str | Path, records: list[dict[str, str]]) -> Path:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("w", newline="", encoding="utf-8") as output:
        writer = csv.DictWriter(output, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(records)
    return destination


def read_records(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8-sig") as source:
        return list(csv.DictReader(source))


def validate_records(records: list[dict[str, str]]) -> dict[str, object]:
    if not records:
        raise ValueError("dataset must contain at least one record")

    for index, record in enumerate(records, start=2):
        missing = [field for field in FIELDS if not record.get(field, "").strip()]
        if missing:
            raise ValueError(f"row {index} has missing values: {', '.join(missing)}")
        for feature in FEATURES:
            try:
                float(record[feature])
            except ValueError as error:
                raise ValueError(f"row {index} has non-numeric {feature}") from error
        if record["Performance"] not in LABELS:
            raise ValueError(f"row {index} has an unsupported Performance label")

    return {
        "rows": len(records),
        "columns": list(FIELDS),
        "labels": {label: sum(row["Performance"] == label for row in records) for label in LABELS},
        "missing_values": 0,
    }