# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Commands

```bash
# Run tests
pytest

# Run a single test
pytest tests/test_main.py::test_backup_creates_timestamped_folder

# Run tests with coverage
pytest --cov=test_project_1

# Lint
ruff check src/ tests/

# Auto-fix lint issues
ruff check --fix src/ tests/

# Run the backup manually
python -m test_project_1.main
```

## Architecture

- `src/test_project_1/main.py` — two public functions: `backup()` and `purge_old_backups()`, called in sequence by `main()`
- `tests/test_main.py` — pytest tests using `tmp_path` fixtures; never touch real `~/Documents` or `~/Backups`
- `pyproject.toml` — single source of truth for dependencies, build config, ruff, and pytest settings

All source code lives under `src/` (src layout), so the package is not importable without installing it (editable install via `pip install -e .`).

## Backup behaviour

- `backup()` copies `~/Documents` to `~/Backups/Documents_YYYY-MM-DD_HH-MM-SS`
- `purge_old_backups()` deletes backup folders older than 7 days, using the timestamp in the folder name (not filesystem mtime, which is unreliable after `shutil.copytree`)
- A cron job runs `python -m test_project_1.main` daily at 2:00 AM; logs go to `~/Backups/backup.log`
