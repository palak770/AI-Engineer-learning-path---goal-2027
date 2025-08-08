# gitignore.md

This file documents the **`.gitignore`** rules used for a Python + VS Code machine learning project and explains why each pattern is included. Put the actual `.gitignore` (the patterns below) in the repo root; this `gitignore.md` explains the choices and how to reproduce ignored items locally.

---

## Recommended `.gitignore` (put this in your repo as `.gitignore`)

```gitignore
# ----------------------------
# Python cache/compiled files
# ----------------------------
__pycache__/
*.py[cod]
*.so
*.egg
*.egg-info/
dist/
build/

# ----------------------------
# Jupyter Notebook checkpoints
# ----------------------------
.ipynb_checkpoints/

# ----------------------------
# Virtual environments
# ----------------------------
env/
venv/
.venv/
ENV/
env.bak/

# ----------------------------
# Data files (if you don't want datasets in repo)
# ----------------------------
*.csv
*.tsv
*.json
*.xlsx
*.xls

# ----------------------------
# Model files (large binaries)
# ----------------------------
*.pkl
*.joblib
*.h5
*.pt
*.onnx

# ----------------------------
# Logs
# ----------------------------
*.log

# ----------------------------
# VS Code settings
# ----------------------------
.vscode/
.history/
*.code-workspace

# ----------------------------
# OS-specific files
# ----------------------------
.DS_Store
Thumbs.db

# ----------------------------
# Environment variable files
# ----------------------------
.env
```

---

## Section-by-section explanation & learning notes

### 1) Python cache / compiled files

**Patterns:** `__pycache__/`, `*.py[cod]`, `*.so`, `*.egg`, `*.egg-info/`, `dist/`, `build/`

**What they are:**

* `__pycache__/` and `*.pyc`/`*.pyo` are Python bytecode caches created to speed up imports.
* `*.so` are compiled binary extension modules (C/C++ extensions).
* `*.egg`, `*.egg-info/`, `dist/`, `build/` are packaging/build artifacts produced when you build or package a Python project.

**Why ignore them:**

* They are machine-generated and platform-specific. They can be regenerated from source using Python.
* Committing them bloats repository size and creates useless diffs.

**How to reproduce locally:**

```bash
# regenerate after cloning
python -m pip install -r requirements.txt
# or when building a package
python setup.py sdist bdist_wheel
```

---

### 2) Jupyter Notebook checkpoints

**Pattern:** `.ipynb_checkpoints/`

**What it is:**

* Jupyter autosaves checkpoint copies of your notebooks in this directory.

**Why ignore it:**

* Checkpoints are temporary backups and clutter git history.

**Learning note:**

* Commit your main `.ipynb` file (or convert important notebooks to `.py` or export cleaned `.md`), but ignore the checkpoints.

---

### 3) Virtual environments

**Patterns:** `env/`, `venv/`, `.venv/`, `ENV/`, `env.bak/`

**What they are:**

* Local folders containing installed Python packages for your project (site-packages, bin/ scripts).

**Why ignore them:**

* They are large and system-specific. Instead, track `requirements.txt` or `pyproject.toml`/`poetry.lock`.

**How to recreate:**

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

---

### 4) Data files

**Patterns:** `*.csv`, `*.tsv`, `*.json`, `*.xlsx`, `*.xls`

**What they are:**

* Raw datasets or exported spreadsheets and JSON data.

**Why ignore them (often):**

* Datasets can be large, sensitive, or licensed.
* If datasets change frequently, git history will grow quickly.

**When to include:**

* Include very small sample datasets (e.g., `data/sample.csv`) if you want reproducibility out-of-the-box.

**Best practice:**

* Keep `data/sample.csv` or `data/README.md` (small) in repo.
* For full datasets provide a `scripts/download_data.py` or `Makefile` target that downloads data from a stable source (Kaggle, S3, Google Drive).

Example download script snippet:

```python
# scripts/download_data.py
import requests
url = "https://example.com/dataset.csv"
open("data/dataset.csv","wb").write(requests.get(url).content)
```

---

### 5) Model files (large binaries)

**Patterns:** `*.pkl`, `*.joblib`, `*.h5`, `*.pt`, `*.onnx`

**What they are:**

* Serialized model files saved after training (scikit-learn, Keras, PyTorch, ONNX exports).

**Why ignore them:**

* Very large, binary, not human-readable, and can be re-generated from training code.
* Storing models in git is inefficient; use a model registry, cloud storage, or Git LFS if needed.

**How to share models publicly:**

* Upload to cloud storage (S3 / Google Cloud Storage), GitHub Releases, or use DVC / MLflow / Weights & Biases.
* Provide a `scripts/download_model.py` or add a note in README with the download URL.

---

### 6) Logs

**Pattern:** `*.log`

**What they are:**

* Runtime logs from training runs, experiments, or server output.

**Why ignore them:**

* They change frequently and create noisy commits.

**Alternative:**

* Keep useful experiment summaries in `experiments/summary.md` or track runs with an experiment tracker (Weights & Biases, MLflow).

---

### 7) VS Code settings

**Patterns:** `.vscode/`, `.history/`, `*.code-workspace`

**What they are:**

* Editor-specific files that store workspace settings, debug launch configs, and local history/backups.

**Why ignore them:**

* Personal preferences (themes, extensions paths) should not be forced on collaborators.

**Tip:**

* If you want to share recommended workspace settings, commit a **minimal** `.vscode/settings.json` containing only project-relevant settings (e.g., Python interpreter path placeholder) and document in README. Otherwise ignore the whole `.vscode/`.

---

### 8) OS-specific files

**Patterns:** `.DS_Store`, `Thumbs.db`

**What they are:**

* macOS and Windows file-system helper files.

**Why ignore them:**

* Useless in repo; created automatically by OS GUIs.

---

### 9) Environment variable files

**Pattern:** `.env`

**What it is:**

* File that holds secrets and environment variables (API keys, DB passwords).

**Why ignore it:**

* Sensitive data should never be pushed to public repos.

**Safe alternative:**

* Commit `.env.example` with key names but no values. Example:

```.env.example
DATABASE_URL=
API_KEY=
```

* Use secret managers (GitHub Secrets for Actions) or environment variables on the deployment host.

---

## Extra learning tips

* **If you accidentally committed secrets:** rotate them immediately (change keys) and remove them from history using tools like `git filter-branch` or `bfg-repo-cleaner`.

* **If you need to store large files:** consider `Git LFS` for binaries or `DVC` for dataset + model versioning. Both keep git history usable while tracking large artifacts elsewhere.

* **Small reproducible demo:** keep a `data/sample.csv` (small), `requirements.txt`, `notebooks/demo.ipynb`, and `README.md` so others can run your project after `git clone`.

---

## Quick commands

```bash
# create .gitignore and commit
echo "__pycache__/" >> .gitignore
# (repeat or paste full content)
git add .gitignore
git commit -m "Add .gitignore for Python + VS Code ML project"

# create .env.example
cat > .env.example <<EOL
DATABASE_URL=
API_KEY=
EOL
git add .env.example
git commit -m "Add .env.example"
```

---

If you want, I can:

* Create the actual `.gitignore` file plus `.env.example` and commit-ready `README` and `download_data.py` templates for your repo structure.
* Or generate a shorter cheat-sheet PNG summarizing these rules for quick reference.

Tell me which one you want next.
