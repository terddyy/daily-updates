from __future__ import annotations

import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from zoneinfo import ZoneInfo

from scripts.update_repo import run_burst_update, run_update


def seed_repo(root: Path) -> None:
    (root / "data").mkdir(parents=True, exist_ok=True)
    (root / "archive").mkdir(parents=True, exist_ok=True)
    (root / "scripts").mkdir(parents=True, exist_ok=True)
    (root / "notes").mkdir(parents=True, exist_ok=True)

    (root / "README.md").write_text(
        "# Daily Knowledge Repo MVP\n\n"
        "Automated knowledge maintenance repository.\n",
        encoding="utf-8",
    )
    (root / "archive" / "knowledge_archive.json").write_text('{"entries":[]}\n', encoding="utf-8")
    (root / "data" / "knowledge_pool.json").write_text(
        json.dumps(
            [
                {
                    "category": "Testing",
                    "title": "Entry A",
                    "content": "Practical content A",
                    "source": "https://example.com/a",
                },
                {
                    "category": "Testing",
                    "title": "Entry B",
                    "content": "Practical content B",
                    "source": "https://example.com/b",
                },
            ]
        ),
        encoding="utf-8",
    )


class UpdateRepoTests(unittest.TestCase):
    def test_run_update_without_gemini_key_uses_local_pool(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            seed_repo(root)
            previous = os.environ.pop("GEMINI_API_KEY", None)
            try:
                now = datetime(2026, 4, 16, 9, 3, tzinfo=ZoneInfo("Asia/Manila"))
                result = run_update(root, "Asia/Manila", now=now, skip_git=True)
                self.assertTrue(result.changed)
                self.assertFalse((root / "data" / "daily_tech_trends.json").exists())
            finally:
                if previous is not None:
                    os.environ["GEMINI_API_KEY"] = previous

    def test_run_update_appends_archive_and_note(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            seed_repo(root)

            now = datetime(2026, 4, 16, 9, 3, tzinfo=ZoneInfo("Asia/Manila"))
            result = run_update(root, "Asia/Manila", now=now, skip_git=True)
            self.assertTrue(result.changed)
            self.assertFalse(result.committed)

            archive = json.loads((root / "archive" / "knowledge_archive.json").read_text(encoding="utf-8"))
            self.assertEqual(len(archive["entries"]), 1)
            entry = archive["entries"][0]
            self.assertEqual(entry["date"], "2026-04-16")
            self.assertTrue({"id", "date", "timestamp", "category", "title", "content", "source"}.issubset(entry.keys()))

            note_path = root / "notes" / "2026-04-16.md"
            self.assertTrue(note_path.exists())
            note_text = note_path.read_text(encoding="utf-8")
            self.assertIn("Daily Knowledge Note - 2026-04-16", note_text)
            self.assertIn(entry["title"], note_text)

    def test_run_update_is_idempotent_for_same_slot(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            seed_repo(root)

            now = datetime(2026, 4, 16, 9, 3, tzinfo=ZoneInfo("Asia/Manila"))
            first = run_update(root, "Asia/Manila", now=now, skip_git=True)
            second = run_update(root, "Asia/Manila", now=now, skip_git=True)

            self.assertTrue(first.changed)
            self.assertFalse(second.changed)
            self.assertEqual(second.reason, "Slot already processed.")

            archive = json.loads((root / "archive" / "knowledge_archive.json").read_text(encoding="utf-8"))
            self.assertEqual(len(archive["entries"]), 1)

    def test_second_slot_creates_second_entry(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            seed_repo(root)

            base = datetime(2026, 4, 16, 9, 3, tzinfo=ZoneInfo("Asia/Manila"))
            run_update(root, "Asia/Manila", now=base, skip_git=True)
            run_update(root, "Asia/Manila", now=base + timedelta(minutes=5), skip_git=True)

            archive = json.loads((root / "archive" / "knowledge_archive.json").read_text(encoding="utf-8"))
            self.assertEqual(len(archive["entries"]), 2)

            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertIn("Total archive entries: **2**", readme)
            self.assertIn("Today's entries: **2**", readme)
            self.assertIn("Set `GEMINI_API_KEY` as a GitHub Actions secret", readme)

    def test_burst_update_creates_exact_count_for_one_day(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            seed_repo(root)
            result = run_burst_update(
                repo_root=root,
                timezone="Asia/Manila",
                burst_count=5,
                burst_date="2026-04-18",
                skip_git=True,
                skip_gemini_in_burst=True,
            )
            self.assertTrue(result.changed)
            self.assertIn("skipped", result.reason.lower())

            archive = json.loads((root / "archive" / "knowledge_archive.json").read_text(encoding="utf-8"))
            self.assertEqual(len(archive["entries"]), 5)
            self.assertTrue(all(item["date"] == "2026-04-18" for item in archive["entries"]))
            self.assertEqual(len({item["id"] for item in archive["entries"]}), 5)

            note_path = root / "notes" / "2026-04-18.md"
            self.assertTrue(note_path.exists())
            readme = (root / "README.md").read_text(encoding="utf-8")
            self.assertIn("Total archive entries: **5**", readme)
            self.assertIn("Today's entries: **5**", readme)

    def test_burst_update_bypasses_gemini_when_flag_enabled(self) -> None:
        with TemporaryDirectory() as td:
            root = Path(td)
            seed_repo(root)
            os.environ["GEMINI_API_KEY"] = "dummy-key"
            try:
                result = run_burst_update(
                    repo_root=root,
                    timezone="Asia/Manila",
                    burst_count=3,
                    burst_date="2026-04-19",
                    skip_git=True,
                    skip_gemini_in_burst=True,
                )
            finally:
                os.environ.pop("GEMINI_API_KEY", None)

            self.assertTrue(result.changed)
            self.assertFalse((root / "data" / "daily_tech_trends.json").exists())


if __name__ == "__main__":
    unittest.main()
