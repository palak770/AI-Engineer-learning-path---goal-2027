# Git Learning — Complete Guide for Absolute Beginners

This `gitlearning.md` is a single-file, beginner-friendly guide that explains **what Git is**, **why use it**, **how to set it up**, and **how to use it in daily work** (terminal + VS Code GUI). It also covers branches, pull requests, `.gitignore`, handling datasets/models, troubleshooting, and good habits. Use this as your personal reference and checklist while you learn.

---

## Table of contents

1. What is Git and GitHub?
2. Why use Git?
3. Key Git concepts (simple)
4. Setup (install & configure)
5. Create a repo and push to GitHub (step-by-step)
6. Daily workflow: edit → commit → push (with clear "why" for each step)
7. VS Code GUI: step-by-step
8. Branches & Pull Requests — why and when to use them
9. .gitignore: Why, examples, and how to write it
10. Handling datasets and model files (best practices)
11. Common problems & how to fix them
12. Git cheat sheet (commands you’ll use every day)
13. Extra tips: security, history cleanups, large files

---

## 1) What is Git and GitHub?

* **Git** is a tool on your computer that tracks changes to files and lets you save versions (called commits).
* **GitHub** is a website that stores Git repositories online so you can backup, share, and collaborate.

**Analogy:** Git = your local notebook with saved versions. GitHub = cloud folder where you upload that notebook so others can see it.

---

## 2) Why use Git?

* Keeps a history of your project so you can go back to earlier versions.
* Makes collaboration safe — multiple people can work in parallel.
* Helps you manage experiments: branches for experiments, commits for checkpoints.
* Makes your learning or portfolio reproducible: others can clone and run your code.

---

## 3) Key Git concepts (simple)

* **Repository (repo):** A folder tracked by Git.
* **Commit:** A saved snapshot with a message explaining what changed.
* **Branch:** A separate line of development (like a sandbox).
* **Master/Main:** The main branch (stable). Use `main` as default.
* **Remote:** A copy of the repo on a server (e.g., GitHub). Common name: `origin`.
* **Push:** Send commits from local → remote.
* **Pull:** Get commits from remote → local.
* **Clone:** Copy a remote repo to your machine.
* **Stage:** Mark changes you want to include in the next commit (`git add`).

---

## 4) Setup (install & configure)

### A. Install Git

* Windows / macOS / Linux: download from [https://git-scm.com](https://git-scm.com) or use package manager.
* Verify installation:

```bash
git --version
```

### B. Configure your identity (do this once)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

This sets the author info for all commits you make.

---

## 5) Create a repo and push to GitHub (step-by-step)

### Scenario A — New project from scratch (recommended flow)

1. Create a folder and open it in VS Code.
2. Initialize git:

```bash
git init
```

3. Create important starter files: `README.md`, `.gitignore`, `requirements.txt` (as per your project ).
4. Stage & commit:

git commit -m "Initial commit"
```

5. Create an empty repo on GitHub (do not initialize with README if you already have one locally).
6. Link remote and push:

```bash
git remote add origin https://github.com/YOURNAME/REPO.git
git branch -M main
git push -u origin main
```

### Scenario B — Clone an existing GitHub repo

```bash
git clone https://github.com/username/repo.git
cd repo
```

Now you have the repo locally and can make changes.

**Why these steps?**

* `git init` tells Git to track this folder.
* `git add` selects files to include.
* `git commit` saves a snapshot.
* `git remote add origin` links to GitHub so you can push your commits.

---

## 6) Daily workflow: edit → commit → push (with why/when/where)

**Why**: commits are checkpoints; push sends them to GitHub for backup and sharing.

**Good daily flow:**

1. Before starting work, **pull** remote updates:

```bash
git pull --rebase origin main
```

*Why?* ensures you work on the latest code and reduces conflicts.

2. Make changes in VS Code.
3. Check what changed:

```bash
git status
```

4. Stage files to save in commit (choose which changes to include):

```bash
git add file1.py file2.ipynb
# or stage all changes
git add .
```

5. Commit with a clear message:

```bash
git commit -m "Day 05 - added RandomForest training notebook and results"
```

*Why?* commit messages explain what changed; you’ll thank yourself later.

6. Push to GitHub:

```bash
git push origin main
```

*Where?* changes are now on GitHub in the `main` branch.

**When to push?**

* After a meaningful chunk of work (end of the day, or after finishing a feature). Frequent small pushes are fine.

---

## 7) VS Code GUI: step-by-step

* Open VS Code and click Source Control (left vertical bar) or press `Ctrl+Shift+G`.
* You’ll see changed files — click the `+` next to each file to stage, or click `+` at top to stage all.
* Type a commit message and click the checkmark ✓ to commit.
* Use the three-dot menu to Pull or Push. VS Code will show conflict markers if any and help you resolve.

**Why use GUI?**

* Easier to visualize changes and conflicts when you’re starting out.

---

## 8) Branches & Pull Requests — why and when to use them

**What is a branch?** A branch is a copy of the project where you can work independently.

**Why use branches?**

* Keep `main` stable (no broken code).
* Experiment without risk.
* Create a Pull Request (PR) to review and merge changes safely.

**Simple branch workflow:**

```bash
# create and switch to branch
git checkout -b day-06-feature
# work, stage, commit
git add .
git commit -m "Add new feature"
# push branch to GitHub
git push -u origin day-06-feature
```

Then on GitHub open a Pull Request from `day-06-feature` → `main`. Review and merge when ready.

**When to use branches?**

* Always for big or risky changes.
* For daily small changes, some beginners commit directly to `main` (OK), but branching is best practice.

---

## 9) .gitignore: Why, examples, and how to write it

**Why**: stops certain files from being tracked (temporary files, secrets, large files).

**Common patterns for Python + VS Code ML projects:**

```
__pycache__/
*.py[cod]
.ipynb_checkpoints/
venv/
.venv/
*.csv
*.pkl
*.joblib
.vscode/
.env
.DS_Store
```

**When to include data in repo?**

* Small demo data: include in `data/sample.csv`.
* Large/private data: exclude from repo and provide a download script.

**How to add/remove patterns:**

* Add patterns to `.gitignore` at repo root.
* If a file was already committed, remove it from Git tracking:

```bash
git rm --cached bigfile.csv
git commit -m "Remove bigfile from tracking"
```

---

## 10) Handling datasets and model files (best practices)

* **Small datasets** (<= a few MB): keep in `data/` folder and track them.
* **Large datasets**: keep them out of Git. Provide `scripts/download_data.py` that downloads data from a URL.
* **Trained models**: do not push binary model files to Git. Use cloud storage (S3, Google Drive) or tools such as `DVC` or `Git LFS`.
* **Secrets**: never push `.env` with API keys; use `.env.example` and GitHub secrets for CI.

---

## 11) Common problems & how to fix them

* **Auth issues when pushing**: Use GitHub Personal Access Token (PAT) for HTTPS or set up SSH keys.
* **Non-fast-forward / push rejected**: Someone updated remote. Fix by pulling:

```
git pull --rebase origin main
# resolve conflicts, then
git push origin main
```

* **I accidentally committed a secret**: rotate the secret (generate new key) immediately and remove it from history using `bfg` or `git filter-branch` (advanced). Ask for help.
* **Large files accidentally committed**: remove from history and use Git LFS.

---

## 12) Git cheat sheet (everyday commands)

```bash
# see status of files
git status

# stage changes
git add file.py
git add .   # stage everything

# commit staged changes
git commit -m "Short meaningful message"

# view history
git log --oneline --graph --all

# get updates from remote
git pull --rebase origin main

# push local commits to remote
git push origin main

# create a branch and switch to it
git checkout -b new-branch

# switch back to main
git checkout main

# delete a branch locally
git branch -d new-branch

# remove a file from tracking but keep locally
git rm --cached path/to/file
```

---

## 13) Extra tips & recommended workflow for learners

* **Commit messages:** short title + optional longer description. E.g., `Day 06 - Add RandomForest training`.
* **Commit often:** makes it easy to revert to small steps.
* **Use branches** for experiments.
* **Protect `main`**: later, enable GitHub branch protection to require PRs for merges.
* **Track experiments**: use a tool like Weights & Biases or MLflow for reproducible metrics rather than committing logs.

---

## 14) Quick start checklist (copy and use)

1. `git init` (if new)
2. `git add .`
3. `git commit -m "Initial commit"`
4. `git remote add origin <URL>`
5. `git push -u origin main`

Daily:

1. `git pull --rebase origin main`
2. Make changes
3. `git add .`
4. `git commit -m "..."`
5. `git push origin main`

---

## 15) What I can do next for you

* Create a ready-to-copy `.gitignore`, `.env.example`, `README.md` in your repo structure.
* Generate a one-page PNG cheat sheet from this file.
* Walk you through your first real push step-by-step while you share the terminal output.

---

*End of gitlearning.md*
