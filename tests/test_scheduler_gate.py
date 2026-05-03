from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from zoneinfo import ZoneInfo

from scripts.scheduler_gate import (
    can_run_with_budget,
    choose_schedule,
    day_weight_for_weekday,
    enumerate_slots,
    read_month_usage,
    record_success,
    should_run,
)


class SchedulerGateTests(unittest.TestCase):
    def test_enumerate_slots_count(self) -> None:
        slots = enumerate_slots("2026-04-16", start_hour=6, end_hour=23, interval_minutes=15)
        self.assertEqual(len(slots), 68)
        self.assertEqual(slots[0], "2026-04-16T06:00")
        self.assertEqual(slots[-1], "2026-04-16T22:45")

    def test_should_run_matches_bucket(self) -> None:
        now = datetime(2026, 4, 16, 9, 7, tzinfo=ZoneInfo("Asia/Manila"))
        self.assertTrue(should_run(now, ["2026-04-16T09:00"], interval_minutes=15))
        self.assertFalse(should_run(now, ["2026-04-16T09:15"], interval_minutes=15))

    def test_weekday_weight_is_higher_than_weekend(self) -> None:
        weekday = day_weight_for_weekday(2, weekday_weight=1.0, weekend_weight=0.65)
        weekend = day_weight_for_weekday(6, weekday_weight=1.0, weekend_weight=0.65)
        self.assertGreater(weekday, weekend)

    def test_choose_schedule_weekday_target_higher_than_weekend(self) -> None:
        weekday_target, weekday_slots, _ = choose_schedule(
            local_date="2026-04-15",  # Wednesday
            start_hour=6,
            end_hour=23,
            interval_minutes=15,
            seed_salt="test",
            weekday_weight=1.0,
            weekend_weight=0.65,
        )
        weekend_target, weekend_slots, _ = choose_schedule(
            local_date="2026-04-18",  # Saturday
            start_hour=6,
            end_hour=23,
            interval_minutes=15,
            seed_salt="test",
            weekday_weight=1.0,
            weekend_weight=0.65,
        )
        self.assertGreater(weekday_target, weekend_target)
        self.assertEqual(len(set(weekday_slots)), len(weekday_slots))
        self.assertEqual(len(set(weekend_slots)), len(weekend_slots))

    def test_read_month_usage_defaults_to_zero(self) -> None:
        with TemporaryDirectory() as td:
            usage = read_month_usage(Path(td) / "missing.json", "2026-05")
            self.assertEqual(usage["used_minutes"], 0)
            self.assertEqual(usage["runs_count"], 0)

    def test_record_success_updates_state(self) -> None:
        with TemporaryDirectory() as td:
            state_path = Path(td) / "scheduler_usage.json"
            month_key = "2026-05"
            first = record_success(state_path, month_key, minutes_per_run=1, timestamp="2026-05-01T08:00:00+08:00")
            second = record_success(state_path, month_key, minutes_per_run=1, timestamp="2026-05-01T08:15:00+08:00")

            self.assertEqual(first["used_minutes"], 1)
            self.assertEqual(second["used_minutes"], 2)
            self.assertEqual(second["runs_count"], 2)

            raw = json.loads(state_path.read_text(encoding="utf-8"))
            self.assertEqual(raw["months"][month_key]["used_minutes"], 2)
            self.assertEqual(raw["months"][month_key]["runs_count"], 2)

    def test_budget_cap_logic(self) -> None:
        self.assertTrue(can_run_with_budget(month_remaining=1, minutes_per_run=1))
        self.assertFalse(can_run_with_budget(month_remaining=0, minutes_per_run=1))


if __name__ == "__main__":
    unittest.main()
