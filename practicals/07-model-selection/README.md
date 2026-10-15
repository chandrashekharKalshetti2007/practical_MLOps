# Practical 7: Baseline and Hyperparameter Search

## Output

The executable pipeline compares logistic regression, a decision tree selected by grid search, and a random forest selected by randomized search. It uses a fixed seed, stratified train/test split, macro-F1 selection metric, and a held-out test set.

```powershell
python -m mlops_practicals.run_pipeline
```

Review `outputs/model_comparison.json` for accuracy, macro precision/recall/F1, selected model, parameters, and split sizes. Results are from synthetic data and demonstrate the workflow only; they are not a valid estimate of student outcomes in production.