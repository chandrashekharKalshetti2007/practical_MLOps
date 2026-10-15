# Experiment 4 - Data Collection and Processing Pipeline

## Aim
Load and validate tabular data, create a reproducible training pipeline, and record its processed outputs.

## Requirements
- Python dependencies from the repository-root `requirements.txt`
- Run commands from the repository root

## Procedure
1. Run `python -m mlops_practicals.run_pipeline --source-csv ..\processed_student_data.csv`.
2. Review schema, label counts, and validation output in `outputs/run_summary.json`.
3. Inspect the generated dataset and feature files.
4. Change a validation input to exercise missing-column or invalid-value handling.

## Implementation
The shared pipeline creates deterministic synthetic records, validates required columns/types/labels, materializes features, trains models, and writes JSON summaries. The supplied five-row CSV is validation-only so private names are not copied into the repository or used for model-quality claims.

## Observed result
The captured run validated 240 synthetic rows with no missing values and separately checked all five rows in the supplied CSV; counts are recorded in [`OUTPUT.txt`](./OUTPUT.txt).

## Viva questions
1. Why must preprocessing be fit on training data only?
2. Which checks belong in data validation before training?
3. How would you detect a change in the input schema?

## Concept summary
A repeatable pipeline validates data before transforming it and records outputs needed for downstream stages.

## Outcome summary
The end-to-end local data workflow and its row counts are reproducible from the repository root.