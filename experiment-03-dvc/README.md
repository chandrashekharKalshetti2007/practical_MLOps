# Experiment 3 - Dataset Versioning with DVC

## Aim
Track datasets separately from source code, compare versions, and reproduce a training stage.

## Requirements
- Git
- DVC installed with `python -m pip install -r requirements-tracking.txt`
- A local or cloud remote you control

## Procedure
1. Review the training stage in the root `dvc.yaml`.
2. Initialize DVC with `dvc init` if needed.
3. Configure a remote, for example `dvc remote add --local -d storage ../dvc-storage`.
4. Run `dvc repro`, commit `dvc.yaml` and `dvc.lock`, then run `dvc push` after configuring the remote.
5. Change a data dependency and inspect the difference with `dvc diff`.

## Captured result
The reproducible stage definition is included. DVC was not installed in the captured environment, so initialization, remote transfer, and version comparison were not run; see [`OUTPUT.txt`](./OUTPUT.txt).

Do not commit credentials or local remote configuration. Store only DVC metadata in Git; store artifact content in the DVC remote.

## Viva questions
1. What does DVC store in Git, and what does it store in its remote?
2. How does `dvc repro` decide whether a stage must run again?
3. Why is a local remote different from shared cloud storage?

## Concept summary
DVC makes large data/model artifacts addressable and reproducible alongside Git-tracked code.

## Outcome summary
A pipeline stage is configured; artifact tracking requires installing DVC and configuring a remote.