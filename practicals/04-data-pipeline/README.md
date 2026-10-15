# Practical 4: Data Processing Pipeline

## Output

The shared pipeline creates deterministic synthetic records, validates required columns/types/labels, writes a CSV, materializes features, trains models, and writes JSON summaries. Run:

```powershell
python -m mlops_practicals.run_pipeline --source-csv ..\processed_student_data.csv
```

The supplied CSV is validation-only because it contains five named rows. The command reports row count, schema, label counts, and missing values without putting those rows into the repository. Model training uses generated synthetic records instead.

**Generated evidence:** `outputs/run_summary.json`, `outputs/model_comparison.json`, and `data/synthetic_student_performance.csv`.