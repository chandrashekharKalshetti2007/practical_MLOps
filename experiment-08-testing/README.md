# Experiment 8 - Unit Testing for Data Validation and Model Serving

## Aim
Automate checks for data helpers, feature materialization, model artifacts, and prediction API behavior.

## Requirements
- Python dependencies from the repository-root `requirements.txt`, including pytest
- Run pytest from the repository root

## Procedure
1. Run `python -m pytest -v experiment-08-testing/tests`.
2. Review each test result and the captured summary in [`OUTPUT.txt`](./OUTPUT.txt).
3. Add boundary and invalid-input tests when changing data or API contracts.

## Test coverage
The suite covers deterministic data generation, CSV round trips, missing-value rejection, feature materialization, model artifact creation, valid prediction, and invalid-input rejection.

## Viva questions
1. Which failures should be unit tested before model training?
2. What is the distinction between a unit test and an integration test?
3. How do boundary tests improve API reliability?

## Concept summary
Automated tests make data and serving contracts executable and repeatable.

## Outcome summary
Seven local tests passed in the recorded run; see [`OUTPUT.txt`](./OUTPUT.txt).