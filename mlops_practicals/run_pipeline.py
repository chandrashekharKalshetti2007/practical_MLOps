"""Generate demo data, validate it, train models, and materialize features."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from mlops_practicals.data import generate_synthetic_records, read_records, validate_records, write_records
from mlops_practicals.feature_store import materialize_features
from mlops_practicals.training import train_and_evaluate

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def run(source_csv: str | None = None) -> dict[str, object]:
    records = generate_synthetic_records()
    write_records(PROJECT_ROOT / "data" / "synthetic_student_performance.csv", records)
    summary: dict[str, object] = {
        "synthetic_data_validation": validate_records(records),
        "feature_store_demo": materialize_features(records, PROJECT_ROOT),
        "model_training": train_and_evaluate(records, PROJECT_ROOT),
    }
    if source_csv:
        summary["provided_csv_validation"] = validate_records(read_records(source_csv))

    output_path = PROJECT_ROOT / "outputs" / "run_summary.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-csv", help="Validate a local CSV without training on its records")
    arguments = parser.parse_args()
    print(json.dumps(run(arguments.source_csv), indent=2))


if __name__ == "__main__":
    main()