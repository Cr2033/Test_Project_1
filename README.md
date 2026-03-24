# Test_Project_1

Automates daily backups of `~/Documents` with 7-day retention.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

Run manually:

```bash
python -m test_project_1.main
```

Or schedule via cron to run daily at 2:00 AM:

```
0 2 * * * /path/to/.venv/bin/python3 -m test_project_1.main >> ~/Backups/backup.log 2>&1
```

## How it works

- Copies `~/Documents` to `~/Backups/Documents_YYYY-MM-DD_HH-MM-SS`
- Deletes backups older than 7 days
- Logs are written to `~/Backups/backup.log`

## Development

```bash
pytest          # run tests
ruff check .    # lint
```
