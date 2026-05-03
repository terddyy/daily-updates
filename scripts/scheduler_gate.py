from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


DEFAULT_TZ = "Asia/Manila"
DEFAULT_START_HOUR = 6
DEFAULT_END_HOUR = 23
DEFAULT_INTERVAL_MINUTES = 15
DEFAULT_SEED_SALT = "daily-knowledge-repo"
DEFAULT_WEEKDAY_WEIGHT = 1.0
DEFAULT_WEEKEND_WEIGHT = 0.65
DEFAULT_MONTH_CAP = 1800
DEFAULT_MINUTES_PER_RUN = 1
DEFAULT_STATE_PATH = "data/scheduler_usage.json"


def now_local(tz_name: str, now: datetime | None = None) -> datetime:
    tz = ZoneInfo(tz_name)
    if now is None:
        return datetime.now(tz)
    if now.tzinfo is None:
        return now.replace(tzinfo=tz)
    return now.astimezone(tz)


def build_rng_seed(*parts: object) -> int:
    raw = "|".join(str(p) for p in parts)
    return int(hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16], 16)


def enumerate_slots(date: str, start_hour: int, end_hour: int, interval_minutes: int) -> list[str]:
    if end_hour <= start_hour:
        raise ValueError("end_hour must be greater than start_hour")
    if interval_minutes <= 0 or interval_minutes > 60:
        raise ValueError("interval_minutes must be between 1 and 60")

    slots: list[str] = []
    for hour in range(start_hour, end_hour):
        minute = 0
        while minute < 60:
            slots.append(f"{date}T{hour:02d}:{minute:02d}")
            minute += interval_minutes
    return slots


def day_weight_for_weekday(weekday: int, weekday_weight: float, weekend_weight: float) -> float:
    return weekday_weight if weekday <= 4 else weekend_weight


def _load_usage_state(state_path: Path) -> dict[str, object]:
    if not state_path.exists():
        return {"months": {}}
    loaded = json.loads(state_path.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        return {"months": {}}
    months = loaded.get("months")
    if not isinstance(months, dict):
        loaded["months"] = {}
    return loaded


def _write_usage_state(state_path: Path, state: dict[str, object]) -> None:
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def read_month_usage(state_path: Path, month_key: str) -> dict[str, int]:
    state = _load_usage_state(state_path)
    months = state.get("months", {})
    if not isinstance(months, dict):
        return {"used_minutes": 0, "runs_count": 0}
    month_obj = months.get(month_key, {})
    if not isinstance(month_obj, dict):
        return {"used_minutes": 0, "runs_count": 0}
    return {
        "used_minutes": int(month_obj.get("used_minutes", 0)),
        "runs_count": int(month_obj.get("runs_count", 0)),
    }


def record_success(state_path: Path, month_key: str, minutes_per_run: int, timestamp: str) -> dict[str, int | str]:
    state = _load_usage_state(state_path)
    months = state.setdefault("months", {})
    if not isinstance(months, dict):
        months = {}
        state["months"] = months

    month_obj = months.get(month_key)
    if not isinstance(month_obj, dict):
        month_obj = {"used_minutes": 0, "runs_count": 0, "last_updated": ""}

    month_obj["used_minutes"] = int(month_obj.get("used_minutes", 0)) + minutes_per_run
    month_obj["runs_count"] = int(month_obj.get("runs_count", 0)) + 1
    month_obj["last_updated"] = timestamp

    months[month_key] = month_obj
    _write_usage_state(state_path, state)
    return {
        "used_minutes": int(month_obj["used_minutes"]),
        "runs_count": int(month_obj["runs_count"]),
        "last_updated": str(month_obj["last_updated"]),
    }


def choose_schedule(
    local_date: str,
    start_hour: int,
    end_hour: int,
    interval_minutes: int,
    seed_salt: str,
    weekday_weight: float,
    weekend_weight: float,
) -> tuple[int, list[str], float]:
    local_dt = datetime.strptime(local_date, "%Y-%m-%d")
    weight = day_weight_for_weekday(local_dt.weekday(), weekday_weight, weekend_weight)
    slots = enumerate_slots(local_date, start_hour, end_hour, interval_minutes)
    if not slots:
        raise ValueError("No candidate slots were generated.")

    weighted_target = max(1, int(round(len(slots) * weight)))
    target = min(weighted_target, len(slots))

    rng_seed = build_rng_seed(local_date, start_hour, end_hour, interval_minutes, seed_salt, weekday_weight, weekend_weight)
    rng = random.Random(rng_seed)
    chosen = sorted(rng.sample(slots, target))
    return target, chosen, weight


def should_run(now: datetime, selected_slots: list[str], interval_minutes: int) -> bool:
    minute_bucket = (now.minute // interval_minutes) * interval_minutes
    slot_key = now.strftime(f"%Y-%m-%dT%H:{minute_bucket:02d}")
    return slot_key in set(selected_slots)


def can_run_with_budget(month_remaining: int, minutes_per_run: int) -> bool:
    return month_remaining >= minutes_per_run


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scheduler gate and usage recorder.")
    parser.add_argument("--mode", choices=["gate", "record-success"], default="gate")
    parser.add_argument("--tz", default=DEFAULT_TZ)
    parser.add_argument("--start", type=int, default=DEFAULT_START_HOUR)
    parser.add_argument("--end", type=int, default=DEFAULT_END_HOUR)
    parser.add_argument("--interval", type=int, default=DEFAULT_INTERVAL_MINUTES)
    parser.add_argument("--seed-salt", default=DEFAULT_SEED_SALT)
    parser.add_argument("--weekday-weight", type=float, default=DEFAULT_WEEKDAY_WEIGHT)
    parser.add_argument("--weekend-weight", type=float, default=DEFAULT_WEEKEND_WEIGHT)
    parser.add_argument("--month-cap", type=int, default=DEFAULT_MONTH_CAP)
    parser.add_argument("--minutes-per-run", type=int, default=DEFAULT_MINUTES_PER_RUN)
    parser.add_argument("--state-path", default=DEFAULT_STATE_PATH)
    return parser.parse_args()


def gate_mode(args: argparse.Namespace) -> int:
    local_now = now_local(args.tz)
    local_date = local_now.strftime("%Y-%m-%d")
    month_key = local_now.strftime("%Y-%m")
    state_path = Path(args.state_path)

    target, slots, day_weight = choose_schedule(
        local_date=local_date,
        start_hour=args.start,
        end_hour=args.end,
        interval_minutes=args.interval,
        seed_salt=args.seed_salt,
        weekday_weight=args.weekday_weight,
        weekend_weight=args.weekend_weight,
    )

    usage = read_month_usage(state_path, month_key)
    month_used = usage["used_minutes"]
    month_remaining = max(0, args.month_cap - month_used)

    run = should_run(local_now, slots, args.interval) and can_run_with_budget(month_remaining, args.minutes_per_run)

    payload = {
        "should_run": run,
        "local_timestamp": local_now.isoformat(timespec="seconds"),
        "local_date": local_date,
        "month_key": month_key,
        "candidate_slots": len(slots),
        "today_target": target,
        "day_weight": day_weight,
        "month_used": month_used,
        "month_remaining": month_remaining,
        "scheduled_slots": slots,
    }

    print(json.dumps(payload), file=sys.stderr)
    print(f"should_run={'true' if run else 'false'}")
    print(f"today_target={target}")
    print(f"month_remaining={month_remaining}")
    return 0


def record_success_mode(args: argparse.Namespace) -> int:
    local_now = now_local(args.tz)
    month_key = local_now.strftime("%Y-%m")
    state_path = Path(args.state_path)

    updated = record_success(
        state_path=state_path,
        month_key=month_key,
        minutes_per_run=args.minutes_per_run,
        timestamp=local_now.isoformat(timespec="seconds"),
    )

    payload = {
        "recorded": True,
        "month_key": month_key,
        "used_minutes": updated["used_minutes"],
        "runs_count": updated["runs_count"],
        "last_updated": updated["last_updated"],
    }
    print(json.dumps(payload), file=sys.stderr)
    print("recorded=true")
    return 0


def main() -> int:
    args = parse_args()
    if args.minutes_per_run < 1:
        raise ValueError("minutes_per_run must be at least 1")
    if args.month_cap < 1:
        raise ValueError("month_cap must be at least 1")

    if args.mode == "record-success":
        return record_success_mode(args)
    return gate_mode(args)


if __name__ == "__main__":
    raise SystemExit(main())
