from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import subprocess
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


DEFAULT_TIMEZONE = "Asia/Manila"
README_PATH = Path("README.md")
KNOWLEDGE_POOL_PATH = Path("data/knowledge_pool.json")
ARCHIVE_PATH = Path("archive/knowledge_archive.json")
NOTES_DIR = Path("notes")
SLOT_MINUTES = 5
DAILY_TRENDS_CACHE_PATH = Path("data/daily_tech_trends.json")
DASHBOARD_STATE_PATH = Path("data/dashboard_state.json")
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent"


@dataclass
class UpdateResult:
    changed: bool
    committed: bool
    pushed: bool
    entry_id: str | None
    reason: str
    timings_ms: dict[str, int] | None = None


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


def make_burst_slot_key(date_str: str, sequence: int) -> str:
    return f"{date_str}Tburst-{sequence:05d}"


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


def parse_json_object(text: str) -> dict[str, Any]:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        loaded = json.loads(stripped)
        if isinstance(loaded, dict):
            return loaded
    except json.JSONDecodeError:
        pass

    start = stripped.find("{")
    end = stripped.rfind("}")
    if start >= 0 and end > start:
        candidate = stripped[start : end + 1]
        loaded = json.loads(candidate)
        if isinstance(loaded, dict):
            return loaded
    raise ValueError("Gemini did not return a valid JSON object.")


def fetch_daily_trend_from_gemini(api_key: str, local_now: datetime, timeout_seconds: float) -> dict[str, Any]:
    prompt = (
        "Use Google Search to find one latest significant software/AI tech advancement from the last 7 days. "
        "Prioritize developer-relevant topics (examples: OpenClaw, major model releases, framework/runtime updates, tooling). "
        "Return STRICT JSON object only with keys: title, content, source. "
        "content must be one concise sentence with practical relevance. "
        "source must be the most authoritative URL for the claim."
    )
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "tools": [{"googleSearch": {}}],
        "generationConfig": {
            "responseMimeType": "application/json",
            "responseJsonSchema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "content": {"type": "string"},
                    "source": {"type": "string"},
                },
                "required": ["title", "content", "source"],
            },
        },
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        GEMINI_API_URL,
        data=body,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "x-goog-api-key": api_key,
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=timeout_seconds) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"Gemini request failed: {exc}") from exc

    candidates = raw.get("candidates", [])
    if not candidates:
        raise RuntimeError("Gemini returned no candidates.")
    parts = candidates[0].get("content", {}).get("parts", [])
    if not parts:
        raise RuntimeError("Gemini returned no content parts.")
    text = parts[0].get("text", "")
    parsed = parse_json_object(text)

    title = str(parsed.get("title", "")).strip()
    content = str(parsed.get("content", "")).strip()
    source = str(parsed.get("source", "")).strip()
    if not (title and content and source):
        raise RuntimeError("Gemini response missing title/content/source.")

    return {
        "category": "Tech Trends",
        "title": title,
        "content": content,
        "source": source,
        "fetched_at": local_now.isoformat(timespec="seconds"),
    }


def get_daily_trend_item(
    repo_root: Path,
    date_str: str,
    local_now: datetime,
    gemini_timeout_seconds: float,
    gemini_max_retries: int,
) -> dict[str, Any] | None:
    api_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if not api_key:
        return None

    cache = load_json(repo_root / DAILY_TRENDS_CACHE_PATH, {"days": {}})
    days = cache.get("days", {})
    day_entry = days.get(date_str)
    if isinstance(day_entry, dict) and {"title", "content", "source"}.issubset(day_entry.keys()):
        return {
            "category": "Tech Trends",
            "title": day_entry["title"],
            "content": day_entry["content"],
            "source": day_entry["source"],
        }

    attempts = max(1, gemini_max_retries + 1)
    last_error: Exception | None = None
    for _ in range(attempts):
        try:
            fresh = fetch_daily_trend_from_gemini(
                api_key=api_key,
                local_now=local_now,
                timeout_seconds=gemini_timeout_seconds,
            )
            days[date_str] = {
                "title": fresh["title"],
                "content": fresh["content"],
                "source": fresh["source"],
                "fetched_at": fresh["fetched_at"],
            }
            cache["days"] = days
            write_json(repo_root / DAILY_TRENDS_CACHE_PATH, cache)
            return {
                "category": fresh["category"],
                "title": fresh["title"],
                "content": fresh["content"],
                "source": fresh["source"],
            }
        except Exception as exc:
            last_error = exc

    if last_error is not None:
        print(f"Warning: failed to fetch daily trend from Gemini: {last_error}")
    return None


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


def build_dashboard_state(entries: list[dict[str, Any]], today_note_path: Path) -> dict[str, Any]:
    categories: dict[str, int] = {}
    for item in entries:
        category = item.get("category", "Uncategorized")
        categories[category] = categories.get(category, 0) + 1

    latest = entries[-1] if entries else None
    if latest is not None:
        latest_summary: dict[str, Any] = {
            "timestamp": latest.get("timestamp"),
            "title": latest.get("title"),
            "category": latest.get("category"),
            "source": latest.get("source"),
            "content": latest.get("content"),
        }
    else:
        latest_summary = {}

    recent = []
    for item in entries[-10:]:
        recent.append(
            {
                "timestamp": item.get("timestamp"),
                "title": item.get("title"),
                "category": item.get("category"),
            }
        )

    day_counts: dict[str, int] = {}
    for item in entries:
        day = str(item.get("date", ""))
        day_counts[day] = day_counts.get(day, 0) + 1

    return {
        "total_entries": len(entries),
        "latest": latest_summary,
        "top_categories": sorted(categories.items(), key=lambda x: (-x[1], x[0]))[:5],
        "recent_timeline": recent,
        "today_note": today_note_path.as_posix(),
        "day_counts": day_counts,
    }


def render_readme_from_state(state: dict[str, Any], today_date: str) -> str:
    total = int(state.get("total_entries", 0))
    day_counts = state.get("day_counts", {})
    today_count = int(day_counts.get(today_date, 0)) if isinstance(day_counts, dict) else 0

    latest = state.get("latest", {}) if isinstance(state.get("latest", {}), dict) else {}
    if latest:
        latest_block = (
            f"- Timestamp: `{latest.get('timestamp', '')}`\n"
            f"- Title: **{latest.get('title', '')}**\n"
            f"- Category: `{latest.get('category', '')}`\n"
            f"- Source: {latest.get('source', '')}\n"
            f"- Summary: {latest.get('content', '')}\n"
        )
    else:
        latest_block = "- No entries yet.\n"

    top_categories = state.get("top_categories", [])
    category_lines = "\n".join(f"- `{name}`: {count}" for name, count in top_categories) or "- No categories yet."

    recent = state.get("recent_timeline", [])
    recent_lines = []
    for item in reversed(recent):
        recent_lines.append(
            f"- `{item.get('timestamp', '')}` | **{item.get('title', '')}** ({item.get('category', '')})"
        )
    recent_block = "\n".join(recent_lines) or "- No recent entries."

    today_note = state.get("today_note", f"notes/{today_date}.md")

    return (
        "# Daily Knowledge Repo MVP\n\n"
        "Automated knowledge maintenance repository. It appends practical daily notes and keeps metadata fresh.\n\n"
        "## AI Trend Source\n\n"
        "- Optional daily live trend fetch uses Gemini API with Google Search grounding.\n"
        "- Set `GEMINI_API_KEY` as a GitHub Actions secret to enable one daily `Tech Trends` entry.\n"
        "- Without API key, the repo falls back to local `data/knowledge_pool.json` entries.\n\n"
        "## Dashboard\n\n"
        f"- Total archive entries: **{total}**\n"
        f"- Today's entries: **{today_count}**\n"
        f"- Today's note: `{today_note}`\n\n"
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


def git_commit_no_push(repo_root: Path, targets: list[Path], message: str, author_name: str, author_email: str) -> bool:
    rel_targets = [str(t.as_posix()) for t in targets]
    subprocess.run(["git", "add", "--", *rel_targets], cwd=repo_root, check=True)
    staged = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=repo_root, check=False)
    if staged.returncode == 0:
        return False

    env = {
        "GIT_AUTHOR_NAME": author_name,
        "GIT_AUTHOR_EMAIL": author_email,
        "GIT_COMMITTER_NAME": author_name,
        "GIT_COMMITTER_EMAIL": author_email,
    }
    full_env = {**os.environ, **env}
    subprocess.run(["git", "commit", "-m", message], cwd=repo_root, check=True, env=full_env)
    return True


def git_push(repo_root: Path) -> bool:
    push = subprocess.run(["git", "push"], cwd=repo_root, check=False)
    return push.returncode == 0


def _build_timings(start_perf: float, load_perf: float, select_perf: float, write_perf: float, git_perf: float, end_perf: float) -> dict[str, int]:
    return {
        "load_ms": int((load_perf - start_perf) * 1000),
        "select_ms": int((select_perf - load_perf) * 1000),
        "write_ms": int((write_perf - select_perf) * 1000),
        "git_ms": int((git_perf - write_perf) * 1000),
        "total_ms": int((end_perf - start_perf) * 1000),
    }


def run_burst_update(
    repo_root: Path,
    timezone: str,
    burst_count: int,
    burst_date: str | None = None,
    skip_git: bool = False,
    skip_gemini_in_burst: bool = False,
    max_attempts: int | None = None,
    burst_commit_mode: str = "single",
    gemini_timeout_seconds: float = 6.0,
    gemini_max_retries: int = 1,
    include_timing: bool = False,
) -> UpdateResult:
    start_perf = time.perf_counter()
    if burst_count < 1:
        return UpdateResult(False, False, False, None, "Burst count must be at least 1.")

    local_now = now_in_timezone(timezone)
    date_str = burst_date or local_now.strftime("%Y-%m-%d")
    datetime.strptime(date_str, "%Y-%m-%d")

    pool = load_json(repo_root / KNOWLEDGE_POOL_PATH, [])
    archive_doc = load_json(repo_root / ARCHIVE_PATH, {"entries": []})
    archive_entries: list[dict[str, Any]] = archive_doc.get("entries", [])
    existing_ids = {item.get("id") for item in archive_entries}

    note_path = repo_root / NOTES_DIR / f"{date_str}.md"
    ensure_today_note_header(note_path, date_str)

    load_perf = time.perf_counter()

    can_use_git = not skip_git and is_git_repo(repo_root)
    author_name = os.environ.get("GIT_AUTHOR_NAME", "terddyy")
    author_email = os.environ.get("GIT_AUTHOR_EMAIL", "terddy03@gmail.com")

    attempts_limit = max_attempts if max_attempts is not None else burst_count * 3
    committed_count = 0
    last_entry_id: str | None = None

    targets = [README_PATH, ARCHIVE_PATH, NOTES_DIR / f"{date_str}.md", DASHBOARD_STATE_PATH]
    if (repo_root / DAILY_TRENDS_CACHE_PATH).exists():
        targets.append(DAILY_TRENDS_CACHE_PATH)

    for sequence in range(attempts_limit):
        if committed_count >= burst_count:
            break
        slot_key = make_burst_slot_key(date_str, sequence)
        entry_id = make_entry_id(date_str, slot_key)
        if entry_id in existing_ids:
            continue

        selected = None
        if not skip_gemini_in_burst:
            todays_trend_exists = any(
                item.get("date") == date_str and item.get("category") == "Tech Trends"
                for item in archive_entries
            )
            if not todays_trend_exists:
                selected = get_daily_trend_item(
                    repo_root=repo_root,
                    date_str=date_str,
                    local_now=local_now,
                    gemini_timeout_seconds=gemini_timeout_seconds,
                    gemini_max_retries=gemini_max_retries,
                )
        if selected is None:
            selected = select_pool_item(pool, archive_entries, slot_key)

        record_time = local_now + timedelta(seconds=sequence)
        record = {
            "id": entry_id,
            "date": date_str,
            "timestamp": record_time.isoformat(timespec="seconds"),
            "category": selected["category"],
            "title": selected["title"],
            "content": selected["content"],
            "source": selected["source"],
        }

        append_note_entry(note_path, record)
        archive_entries.append(record)
        existing_ids.add(entry_id)
        last_entry_id = entry_id
        committed_count += 1

        if can_use_git and burst_commit_mode == "per-entry":
            archive_doc["entries"] = archive_entries
            write_json(repo_root / ARCHIVE_PATH, archive_doc)
            state = build_dashboard_state(archive_entries, NOTES_DIR / f"{date_str}.md")
            write_json(repo_root / DASHBOARD_STATE_PATH, state)
            readme_content = render_readme_from_state(state, date_str)
            (repo_root / README_PATH).write_text(readme_content, encoding="utf-8")
            message = f"chore(knowledge): burst update {date_str} #{committed_count}"
            git_commit_no_push(repo_root, targets, message, author_name, author_email)

    select_perf = time.perf_counter()

    if committed_count == 0:
        end_perf = time.perf_counter()
        timings = _build_timings(start_perf, load_perf, select_perf, select_perf, select_perf, end_perf) if include_timing else None
        return UpdateResult(False, False, False, None, f"Burst stopped early: created 0/{burst_count} entries.", timings)

    archive_doc["entries"] = archive_entries
    write_json(repo_root / ARCHIVE_PATH, archive_doc)
    state = build_dashboard_state(archive_entries, NOTES_DIR / f"{date_str}.md")
    write_json(repo_root / DASHBOARD_STATE_PATH, state)
    readme_content = render_readme_from_state(state, date_str)
    (repo_root / README_PATH).write_text(readme_content, encoding="utf-8")

    write_perf = time.perf_counter()

    committed = False
    pushed = False
    reason = "Burst update completed."

    if can_use_git:
        if burst_commit_mode == "single":
            message = f"chore(knowledge): burst update {date_str} x{committed_count}"
            committed, pushed = git_commit_and_push(repo_root, targets, message, author_name, author_email)
        else:
            pushed = git_push(repo_root)
            committed = True
    else:
        if skip_git:
            reason = "Burst files updated; git operations skipped."
        else:
            reason = "Burst files updated; not a git repository."

    if committed_count < burst_count:
        reason = f"Burst stopped early: created {committed_count}/{burst_count} entries within max attempts {attempts_limit}."

    git_perf = time.perf_counter()
    end_perf = git_perf
    timings = _build_timings(start_perf, load_perf, select_perf, write_perf, git_perf, end_perf) if include_timing else None

    return UpdateResult(True, committed, pushed, last_entry_id, reason, timings)


def run_update(
    repo_root: Path,
    timezone: str,
    now: datetime | None = None,
    skip_git: bool = False,
    gemini_timeout_seconds: float = 6.0,
    gemini_max_retries: int = 1,
    include_timing: bool = False,
) -> UpdateResult:
    start_perf = time.perf_counter()
    local_now = now_in_timezone(timezone, now)
    date_str = local_now.strftime("%Y-%m-%d")
    iso_timestamp = local_now.isoformat(timespec="seconds")
    slot_key = build_slot_key(local_now)
    entry_id = make_entry_id(date_str, slot_key)

    pool = load_json(repo_root / KNOWLEDGE_POOL_PATH, [])
    archive_doc = load_json(repo_root / ARCHIVE_PATH, {"entries": []})
    archive_entries: list[dict[str, Any]] = archive_doc.get("entries", [])
    existing_ids = {item.get("id") for item in archive_entries}
    load_perf = time.perf_counter()

    if entry_id in existing_ids:
        end_perf = time.perf_counter()
        timings = _build_timings(start_perf, load_perf, load_perf, load_perf, load_perf, end_perf) if include_timing else None
        return UpdateResult(False, False, False, entry_id, "Slot already processed.", timings)

    todays_trend_exists = any(
        item.get("date") == date_str and item.get("category") == "Tech Trends"
        for item in archive_entries
    )
    selected = None
    if not todays_trend_exists:
        selected = get_daily_trend_item(
            repo_root=repo_root,
            date_str=date_str,
            local_now=local_now,
            gemini_timeout_seconds=gemini_timeout_seconds,
            gemini_max_retries=gemini_max_retries,
        )
    if selected is None:
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

    select_perf = time.perf_counter()

    note_path = repo_root / NOTES_DIR / f"{date_str}.md"
    ensure_today_note_header(note_path, date_str)
    append_note_entry(note_path, record)

    archive_entries.append(record)
    archive_doc["entries"] = archive_entries
    write_json(repo_root / ARCHIVE_PATH, archive_doc)

    state = build_dashboard_state(archive_entries, NOTES_DIR / f"{date_str}.md")
    write_json(repo_root / DASHBOARD_STATE_PATH, state)
    readme_content = render_readme_from_state(state, date_str)
    (repo_root / README_PATH).write_text(readme_content, encoding="utf-8")

    write_perf = time.perf_counter()

    if skip_git:
        end_perf = time.perf_counter()
        timings = _build_timings(start_perf, load_perf, select_perf, write_perf, write_perf, end_perf) if include_timing else None
        return UpdateResult(True, False, False, entry_id, "Files updated; git operations skipped.", timings)

    if not is_git_repo(repo_root):
        end_perf = time.perf_counter()
        timings = _build_timings(start_perf, load_perf, select_perf, write_perf, write_perf, end_perf) if include_timing else None
        return UpdateResult(True, False, False, entry_id, "Files updated; not a git repository.", timings)

    targets = [README_PATH, ARCHIVE_PATH, NOTES_DIR / f"{date_str}.md", DASHBOARD_STATE_PATH]
    trend_cache_path = repo_root / DAILY_TRENDS_CACHE_PATH
    if trend_cache_path.exists():
        targets.append(DAILY_TRENDS_CACHE_PATH)
    if not has_repo_changes_for_targets(repo_root, targets):
        end_perf = time.perf_counter()
        timings = _build_timings(start_perf, load_perf, select_perf, write_perf, write_perf, end_perf) if include_timing else None
        return UpdateResult(False, False, False, entry_id, "No tracked file changes.", timings)

    message = f"chore(knowledge): update {date_str} {local_now.strftime('%H:%M')}"
    author_name = os.environ.get("GIT_AUTHOR_NAME", "terddyy")
    author_email = os.environ.get("GIT_AUTHOR_EMAIL", "terddy03@gmail.com")
    committed, pushed = git_commit_and_push(repo_root, targets, message, author_name, author_email)

    git_perf = time.perf_counter()
    end_perf = git_perf
    timings = _build_timings(start_perf, load_perf, select_perf, write_perf, git_perf, end_perf) if include_timing else None
    return UpdateResult(True, committed, pushed, entry_id, "Update completed.", timings)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Daily Knowledge Repo updater")
    parser.add_argument("--timezone", default=os.environ.get("TZ", DEFAULT_TIMEZONE))
    parser.add_argument("--skip-git", action="store_true", help="Update files without git commit/push.")
    parser.add_argument("--burst-count", type=int, default=0, help="Create this many commits/entries in burst mode.")
    parser.add_argument("--burst-date", default="", help="Override burst date in YYYY-MM-DD format.")
    parser.add_argument("--skip-gemini-in-burst", action="store_true", help="Force local pool selection during burst mode.")
    parser.add_argument("--max-attempts", type=int, default=0, help="Max attempts to create unique burst entries.")
    parser.add_argument("--burst-commit-mode", choices=["single", "per-entry"], default="single")
    parser.add_argument("--gemini-timeout-seconds", type=float, default=6.0)
    parser.add_argument("--gemini-max-retries", type=int, default=1)
    parser.add_argument("--timing", action="store_true", help="Include timing telemetry in output JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    if args.burst_count > 0:
        result = run_burst_update(
            repo_root=repo_root,
            timezone=args.timezone,
            burst_count=args.burst_count,
            burst_date=args.burst_date or None,
            skip_git=args.skip_git,
            skip_gemini_in_burst=args.skip_gemini_in_burst,
            max_attempts=args.max_attempts if args.max_attempts > 0 else None,
            burst_commit_mode=args.burst_commit_mode,
            gemini_timeout_seconds=args.gemini_timeout_seconds,
            gemini_max_retries=args.gemini_max_retries,
            include_timing=args.timing,
        )
    else:
        result = run_update(
            repo_root=repo_root,
            timezone=args.timezone,
            skip_git=args.skip_git,
            gemini_timeout_seconds=args.gemini_timeout_seconds,
            gemini_max_retries=args.gemini_max_retries,
            include_timing=args.timing,
        )

    payload: dict[str, Any] = {
        "changed": result.changed,
        "committed": result.committed,
        "pushed": result.pushed,
        "entry_id": result.entry_id,
        "reason": result.reason,
    }
    if args.timing and result.timings_ms is not None:
        payload["timings_ms"] = result.timings_ms

    print(json.dumps(payload))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
