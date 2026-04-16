from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from datetime import datetime
from zoneinfo import ZoneInfo


DEFAULT_TZ = "Asia/Manila"
DEFAULT_MIN = 10
DEFAULT_MAX = 20
DEFAULT_START_HOUR = 6
DEFAULT_END_HOUR = 22
DEFAULT_INTERVAL_MINUTES = 15
DEFAULT_SEED_SALT = "daily-knowledge-repo"


def now_local(tz_name: str, now: datetime | None = None) -> datetime:
    tz = ZoneInfo(tz_name)
    if now is None:
        return datetime.now(tz)
    if now.tzinfo is None:
        return now.replace(tzinfo=tz)
    return now.astimezone(tz)


def build_rng_seed(local_date: str, min_commits: int, max_commits: int, start_hour: int, end_hour: int, interval_minutes: int, seed_salt: str) -> int:
    raw = f"{local_date}|{min_commits}|{max_commits}|{start_hour}|{end_hour}|{interval_minutes}|{seed_salt}"
    return int(hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16], 16)


def enumerate_slots(date: str, start_hour: int, end_hour: int, interval_minutes: int) -> list[str]:
    if end_hour <= start_hour:
        raise ValueError("end_hour must be greater than start_hour")
    slots: list[str] = []
    for hour in range(start_hour, end_hour):
        minute = 0
        while minute < 60:
            slots.append(f"{date}T{hour:02d}:{minute:02d}")
            minute += interval_minutes
    return slots


def choose_schedule(local_date: str, min_commits: int, max_commits: int, start_hour: int, end_hour: int, interval_minutes: int, seed_salt: str) -> tuple[int, list[str]]:
    slots = enumerate_slots(local_date, start_hour, end_hour, interval_minutes)
    if not slots:
        raise ValueError("No candidate slots were generated.")

    if min_commits < 1 or max_commits < min_commits:
        raise ValueError("Invalid min/max commit bounds.")
    max_allowed = min(max_commits, len(slots))
    min_allowed = min(min_commits, max_allowed)
    if min_allowed < 1:
        min_allowed = 1

    rng_seed = build_rng_seed(local_date, min_commits, max_commits, start_hour, end_hour, interval_minutes, seed_salt)
    rng = random.Random(rng_seed)
    target = rng.randint(min_allowed, max_allowed)
    chosen = sorted(rng.sample(slots, target))
    return target, chosen


def should_run(now: datetime, selected_slots: list[str], interval_minutes: int) -> bool:
    minute_bucket = (now.minute // interval_minutes) * interval_minutes
    slot_key = now.strftime(f"%Y-%m-%dT%H:{minute_bucket:02d}")
    return slot_key in set(selected_slots)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Decide whether the update job should run for this tick.")
    parser.add_argument("--min", type=int, default=DEFAULT_MIN)
    parser.add_argument("--max", type=int, default=DEFAULT_MAX)
    parser.add_argument("--tz", default=DEFAULT_TZ)
    parser.add_argument("--start", type=int, default=DEFAULT_START_HOUR)
    parser.add_argument("--end", type=int, default=DEFAULT_END_HOUR)
    parser.add_argument("--interval", type=int, default=DEFAULT_INTERVAL_MINUTES)
    parser.add_argument("--seed-salt", default=DEFAULT_SEED_SALT)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    local_now = now_local(args.tz)
    local_date = local_now.strftime("%Y-%m-%d")
    target, slots = choose_schedule(
        local_date=local_date,
        min_commits=args.min,
        max_commits=args.max,
        start_hour=args.start,
        end_hour=args.end,
        interval_minutes=args.interval,
        seed_salt=args.seed_salt,
    )
    run = should_run(local_now, slots, args.interval)
    payload = {
        "should_run": run,
        "local_timestamp": local_now.isoformat(timespec="seconds"),
        "local_date": local_date,
        "target_commits": target,
        "candidate_slots": len(slots),
        "scheduled_slots": slots,
    }

    print(json.dumps(payload), file=sys.stderr)
    print(f"should_run={'true' if run else 'false'}")
    print(f"target_commits={target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
