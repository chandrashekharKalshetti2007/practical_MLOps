# Experiment 9 - Continuous Integration with GitHub Actions

## Aim
Run the same automated test suite and pipeline validation when changes are pushed or proposed for `main`.

## Requirements
- GitHub repository with Actions enabled
- Dependencies listed in `requirements.txt`

## Workflow
The canonical workflow is [`.github/workflows/ci.yml`](../.github/workflows/ci.yml). It checks out the repository, sets up Python, installs requirements, runs `python -m pytest -v experiment-08-testing/tests`, executes the training pipeline, and uploads the output summary.

## Captured result
Python CI run #2 completed successfully on commit `b158519` in 25 seconds and uploaded its output artifact. See [`OUTPUT.txt`](./OUTPUT.txt) for the run link and details.

## Viva questions
1. Which events trigger this workflow?
2. Why should CI use the same test command as local development?
3. What does a green test job establish, and what does it not establish?

## Concept summary
CI provides repeatable automated checks tied to source changes and their commit history.

## Outcome summary
The pipeline definition is ready for GitHub Actions; the hosted result must be captured after execution.