# Practical 8: Automated Testing

## Output

Tests cover deterministic data generation, CSV round trips, validation failures, feature-store materialization, and the trained model artifact/metrics.

```powershell
python -m unittest discover -s tests -v
```

The same command runs in GitHub Actions. Add tests when adding transformations or changing prediction contracts; include invalid and boundary inputs as well as the expected path.