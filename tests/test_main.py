import shutil
from datetime import datetime, timedelta
from pathlib import Path

import pytest

from project_1.main import backup, purge_old_backups


@pytest.fixture
def tmp_source(tmp_path):
    source = tmp_path / "Documents"
    source.mkdir()
    (source / "file.txt").write_text("hello")
    return source


@pytest.fixture
def tmp_backup_dir(tmp_path):
    return tmp_path / "Backups"


def test_backup_creates_timestamped_folder(tmp_source, tmp_backup_dir):
    dest = backup(source=tmp_source, backup_dir=tmp_backup_dir)
    assert dest.exists()
    assert dest.name.startswith("Documents_")
    assert (dest / "file.txt").read_text() == "hello"


def test_backup_creates_backup_dir_if_missing(tmp_source, tmp_backup_dir):
    assert not tmp_backup_dir.exists()
    backup(source=tmp_source, backup_dir=tmp_backup_dir)
    assert tmp_backup_dir.exists()


def test_purge_removes_old_backups(tmp_backup_dir):
    tmp_backup_dir.mkdir()
    old = tmp_backup_dir / "Documents_2020-01-01_00-00-00"
    old.mkdir()
    purge_old_backups(backup_dir=tmp_backup_dir, keep_days=7)
    assert not old.exists()


def test_purge_keeps_recent_backups(tmp_backup_dir):
    tmp_backup_dir.mkdir()
    recent_name = (datetime.now() - timedelta(days=1)).strftime("Documents_%Y-%m-%d_%H-%M-%S")
    recent = tmp_backup_dir / recent_name
    recent.mkdir()
    purge_old_backups(backup_dir=tmp_backup_dir, keep_days=7)
    assert recent.exists()


def test_purge_ignores_unrelated_folders(tmp_backup_dir):
    tmp_backup_dir.mkdir()
    other = tmp_backup_dir / "some_other_folder"
    other.mkdir()
    purge_old_backups(backup_dir=tmp_backup_dir, keep_days=7)
    assert other.exists()
