# Practical 3: Dataset Versioning with DVC

## Output

The root `dvc.yaml` defines the reproducible training stage and its data/model/report outputs. Initialize DVC and configure a remote that you control:

```powershell
git init -b main
dvc init
dvc remote add -d storage <your-supported-remote-url>
python -m pip install dvc
dvc repro
dvc push
```

To compare versions, change the generator seed, rerun the stage, and inspect the DVC/Git history:

```powershell
git log --oneline -- data/synthetic_student_performance.csv.dvc
dvc diff HEAD~1
```

Commit `dvc.yaml`, `dvc.lock`, and `.dvc` metadata to Git; data/model content belongs in DVC storage. Configure remote credentials through your machine or CI secrets, never in this repository. The current environment has no Git or DVC executable, so remote storage and version comparison need to be run after setup.