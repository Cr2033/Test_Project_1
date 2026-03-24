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
pytest tests/test_main.py::test_main

# Run tests with coverage
pytest --cov=project_1

# Lint
ruff check src/ tests/

# Auto-fix lint issues
ruff check --fix src/ tests/

# Run the main entry point
python -m project_1.main
```

## Architecture

- `src/project_1/` — main package; add modules here
- `tests/` — pytest tests mirroring the package structure
- `pyproject.toml` — single source of truth for dependencies, build config, ruff, and pytest settings

All source code lives under `src/` (src layout), so the package is not importable without installing it (editable install via `pip install -e .`). Tests import from `project_1` directly after the editable install.
