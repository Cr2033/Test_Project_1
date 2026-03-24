import shutil
import logging
from datetime import datetime
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SOURCE = Path.home() / "Documents"
BACKUP_DIR = Path.home() / "Backups"


def backup(source: Path = SOURCE, backup_dir: Path = BACKUP_DIR) -> Path:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dest = backup_dir / f"Documents_{timestamp}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    log.info(f"Backing up {source} → {dest}")
    shutil.copytree(source, dest)
    log.info("Backup complete.")
    return dest


def purge_old_backups(backup_dir: Path = BACKUP_DIR, keep_days: int = 7) -> None:
    cutoff = datetime.now().timestamp() - keep_days * 86400
    for entry in backup_dir.glob("Documents_????-??-??_??-??-??"):
        try:
            ts = datetime.strptime(entry.name, "Documents_%Y-%m-%d_%H-%M-%S").timestamp()
        except ValueError:
            continue
        if entry.is_dir() and ts < cutoff:
            log.info(f"Removing old backup: {entry.name}")
            shutil.rmtree(entry)


def main() -> None:
    backup()
    purge_old_backups()


if __name__ == "__main__":
    main()
