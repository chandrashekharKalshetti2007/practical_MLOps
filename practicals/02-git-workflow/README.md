# Practical 2: Git and Collaboration

## Output

Create one GitHub repository for all practicals. Keep each practical in its own folder and use one feature branch per exercise. From the repository root:

```powershell
git init -b main
git add README.md practicals/02-git-workflow
git commit -m "Add MLOps practical 2"
git switch -c practical/03-dvc
```

After a practical is ready, push its branch and open a pull request:

```powershell
git add practicals/03-dvc
git commit -m "Add DVC dataset versioning practical"
git push -u origin practical/03-dvc
```

Resolve a conflict by opening the marked file, keeping the correct combined change, then run tests before `git add` and `git commit`. Use `git log --oneline --graph --all` to show history. Never commit `.env`, credentials, private student records, virtual environments, or large generated artifacts.

**Evidence:** repository layout and command sequence. Execute these commands after installing Git and creating/authenticating to your GitHub repository; Git is not installed in the current environment.