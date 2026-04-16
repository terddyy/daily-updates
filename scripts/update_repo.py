from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import subprocess
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


DEFAULT_TIMEZONE = "Asia/Manila"
README_PATH = Path("README.md")
KNOWLEDGE_POOL_PATH = Path("data/knowledge_pool.json")
ARCHIVE_PATH = Path("archive/knowledge_archive.json")
NOTES_DIR = Path("notes")
SLOT_MINUTES = 5


@dataclass
class UpdateResult:
    changed: bool
    committed: bool
    pushed: bool
    entry_id: str | None
    reason: str


def now_in_timezone(tz_name: str, now: datetime | None = None) -> datetime:
    tz = ZoneInfo(tz_name)
    if now is None:
        return datetime.now(tz)
    if now.tzinfo is None:
        return now.replace(tzinfo=tz)
    return now.astimezone(tz)


def build_slot_key(local_now: datetime, slot_minutes: int = SLOT_MINUTES) -> str:
    minute_bucket = (local_now.minute // slot_minutes) * slot_minutes
    return local_now.strftime(f"%Y-%m-%dT%H:{minute_bucket:02d}")


def load_json(path: Path, default_value: Any) -> Any:
    if not path.exists():
        return default_value
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def make_entry_id(date_str: str, slot_key: str) -> str:
    digest = hashlib.sha256(f"{date_str}|{slot_key}".encode("utf-8")).hexdigest()[:10]
    return f"entry-{date_str}-{digest}"


def select_pool_item(pool: list[dict[str, Any]], archive_entries: list[dict[str, Any]], slot_key: str) -> dict[str, Any]:
    if not pool:
        raise ValueError("Knowledge pool is empty.")
    base_index = len(archive_entries) % len(pool)
    rng = random.Random(slot_key)
    max_offset = min(3, len(pool) - 1)
    offset = rng.randint(0, max_offset)
    candidate_index = (base_index + offset) % len(pool)

    recent_titles = {item.get("title", "") for item in archive_entries[-5:]}
    for i in range(len(pool)):
        idx = (candidate_index + i) % len(pool)
        candidate = pool[idx]
        if candidate.get("title", "") not in recent_titles:
            return candidate
    return pool[candidate_index]


def ensure_today_note_header(note_path: Path, date_str: str) -> None:
    if note_path.exists():
        return
    note_path.parent.mkdir(parents=True, exist_ok=True)
    note_path.write_text(
        (
            f"# Daily Knowledge Note - {date_str}\n\n"
            "This file is maintained automatically. Each entry below should carry practical value.\n\n"
            "---\n\n"
        ),
        encoding="utf-8",
    )


def append_note_entry(note_path: Path, record: dict[str, Any]) -> None:
    entry_block = (
        f"## {record['timestamp']}\n\n"
        f"**{record['title']}**\n\n"
        f"- Category: {record['category']}\n"
        f"- Source: {record['source']}\n\n"
        f"{record['content']}\n\n"
    )
    with note_path.open("a", encoding="utf-8") as handle:
        handle.write(entry_block)


def render_readme(entries: list[dict[str, Any]], today_count: int, today_note_path: Path) -> str:
    total = len(entries)
    categories: dict[str, int] = {}
    for item in entries:
        category = item.get("category", "Uncategorized")
        categories[category] = categories.get(category, 0) + 1

    latest = entries[-1] if entries else None
    latest_block = (
        (
            f"- Timestamp: `{latest['timestamp']}`\n"
            f"- Title: **{latest['title']}**\n"
            f"- Category: `{latest['category']}`\n"
            f"- Source: {latest['source']}\n"
            f"- Summary: {latest['content']}\n"
        )
        if latest
        else "- No entries yet.\n"
    )

    top_categories = sorted(categories.items(), key=lambda x: (-x[1], x[0]))[:5]
    category_lines = "\n".join(f"- `{name}`: {count}" for name, count in top_categories) or "- No categories yet."

    recent_lines = []
    for item in reversed(entries[-10:]):
        recent_lines.append(
            f"- `{item['timestamp']}` | **{item['title']}** ({item['category']})"
        )
    recent_block = "\n".join(recent_lines) or "- No recent entries."

    return (
        "# Daily Knowledge Repo MVP\n\n"
        "Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.\n\n"
        "## Dashboard\n\n"
        f"- Total archive entries: **{total}**\n"
        f"- Today's entries: **{today_count}**\n"
        f"- Today's note: `{today_note_path.as_posix()}`\n\n"
        "### Latest Entry\n\n"
        f"{latest_block}\n"
        "### Top Categories\n\n"
        f"{category_lines}\n\n"
        "### Recent Timeline\n\n"
        f"{recent_block}\n"
    )


def has_repo_changes_for_targets(repo_root: Path, targets: list[Path]) -> bool:
    rel_targets = [str(t.as_posix()) for t in targets]
    cmd = ["git", "status", "--porcelain", "--", *rel_targets]
    result = subprocess.run(cmd, cwd=repo_root, text=True, capture_output=True, check=False)
    return bool(result.stdout.strip())


def is_git_repo(repo_root: Path) -> bool:
    check = subprocess.run(
        ["git", "rev-parse", "--is-inside-work-tree"],
        cwd=repo_root,
        text=True,
        capture_output=True,
        check=False,
    )
    return check.returncode == 0 and check.stdout.strip() == "true"


def git_commit_and_push(repo_root: Path, targets: list[Path], message: str, author_name: str, author_email: str) -> tuple[bool, bool]:
    rel_targets = [str(t.as_posix()) for t in targets]
    subprocess.run(["git", "add", "--", *rel_targets], cwd=repo_root, check=True)
    staged = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=repo_root, check=False)
    if staged.returncode == 0:
        return False, False

    env = {
        "GIT_AUTHOR_NAME": author_name,
        "GIT_AUTHOR_EMAIL": author_email,
        "GIT_COMMITTER_NAME": author_name,
        "GIT_COMMITTER_EMAIL": author_email,
    }
    full_env = {**os.environ, **env}
    subprocess.run(["git", "commit", "-m", message], cwd=repo_root, check=True, env=full_env)
    push = subprocess.run(["git", "push"], cwd=repo_root, check=False)
    return True, push.returncode == 0


def run_update(repo_root: Path, timezone: str, now: datetime | None = None, skip_git: bool = False) -> UpdateResult:
    local_now = now_in_timezone(timezone, now)
    date_str = local_now.strftime("%Y-%m-%d")
    iso_timestamp = local_now.isoformat(timespec="seconds")
    slot_key = build_slot_key(local_now)
    entry_id = make_entry_id(date_str, slot_key)

    pool = load_json(repo_root / KNOWLEDGE_POOL_PATH, [])
    archive_doc = load_json(repo_root / ARCHIVE_PATH, {"entries": []})
    archive_entries: list[dict[str, Any]] = archive_doc.get("entries", [])

    if any(item.get("id") == entry_id for item in archive_entries):
        return UpdateResult(False, False, False, entry_id, "Slot already processed.")

    selected = select_pool_item(pool, archive_entries, slot_key)
    record = {
        "id": entry_id,
        "date": date_str,
        "timestamp": iso_timestamp,
        "category": selected["category"],
        "title": selected["title"],
        "content": selected["content"],
        "source": selected["source"],
    }

    note_path = repo_root / NOTES_DIR / f"{date_str}.md"
    ensure_today_note_header(note_path, date_str)
    append_note_entry(note_path, record)

    archive_entries.append(record)
    archive_doc["entries"] = archive_entries
    write_json(repo_root / ARCHIVE_PATH, archive_doc)

    today_count = sum(1 for item in archive_entries if item.get("date") == date_str)
    readme_content = render_readme(archive_entries, today_count, NOTES_DIR / f"{date_str}.md")
    (repo_root / README_PATH).write_text(readme_content, encoding="utf-8")

    if skip_git:
        return UpdateResult(True, False, False, entry_id, "Files updated; git operations skipped.")

    if not is_git_repo(repo_root):
        return UpdateResult(True, False, False, entry_id, "Files updated; not a git repository.")

    targets = [README_PATH, ARCHIVE_PATH, NOTES_DIR / f"{date_str}.md"]
    if not has_repo_changes_for_targets(repo_root, targets):
        return UpdateResult(False, False, False, entry_id, "No tracked file changes.")

    message = f"chore(knowledge): update {date_str} {local_now.strftime('%H:%M')}"
    author_name = os.environ.get("GIT_AUTHOR_NAME", "knowledge-bot")
    author_email = os.environ.get("GIT_AUTHOR_EMAIL", "knowledge-bot@users.noreply.github.com")
    committed, pushed = git_commit_and_push(repo_root, targets, message, author_name, author_email)
    return UpdateResult(True, committed, pushed, entry_id, "Update completed.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Daily Knowledge Repo updater")
    parser.add_argument("--timezone", default=os.environ.get("TZ", DEFAULT_TIMEZONE))
    parser.add_argument("--skip-git", action="store_true", help="Update files without git commit/push.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    result = run_update(repo_root=repo_root, timezone=args.timezone, skip_git=args.skip_git)
    print(
        json.dumps(
            {
                "changed": result.changed,
                "committed": result.committed,
                "pushed": result.pushed,
                "entry_id": result.entry_id,
                "reason": result.reason,
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
