# Practical 9: Continuous Integration

## Output

`.github/workflows/ci.yml` installs core dependencies, runs unit tests, executes the end-to-end training pipeline, and uploads the output summaries as a workflow artifact on pushes and pull requests to `main`.

To view the report, push the repository to GitHub and inspect the **Actions** tab. The workflow file is prepared locally; an actual build report exists only after GitHub runs it. Keep CI credentials in repository secrets if a private DVC remote is added later.