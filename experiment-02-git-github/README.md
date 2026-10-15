# Experiment 2 - Git, GitHub, Branching, and Collaboration

## Aim
Create and maintain a Git repository, use branches and merges, preserve version history, and collaborate through GitHub.

## Requirements
- Git 2.x
- A GitHub account and authenticated remote

## Procedure
1. Inspect the current repository with `git status --short --branch`.
2. Create a feature branch with `git switch -c practical/03-dvc`.
3. Commit only the intended experiment files, then push the branch and open a pull request.
4. To practice a conflict, edit the same line on two branches, merge, resolve the conflict markers, rerun tests, and commit the resolution.
5. Review history with `git log --oneline --graph --all`.

## Captured result
The MLOps project was committed and pushed to the configured GitHub repository on `main`; the push is recorded in [`OUTPUT.txt`](./OUTPUT.txt). A deliberate two-branch conflict-resolution exercise has not been executed in this working copy.

Never commit `.env`, credentials, private student records, virtual environments, or large generated artifacts. Keep DVC metadata in Git and data content in the configured DVC remote.

## Viva questions
1. What is the difference between `git merge` and `git rebase`?
2. Why should a merge conflict be followed by tests?
3. Which files should be committed when DVC tracks a dataset?

## Concept summary
Git records code and documentation history; GitHub adds remote collaboration, review, and CI.

## Outcome summary
The repository history is available remotely; conflict resolution remains a separate exercise to demonstrate.