from __future__ import annotations

from datetime import datetime
import unittest
from zoneinfo import ZoneInfo

from scripts.scheduler_gate import choose_schedule, enumerate_slots, should_run


class SchedulerGateTests(unittest.TestCase):
    def test_enumerate_slots_count(self) -> None:
        slots = enumerate_slots("2026-04-16", start_hour=6, end_hour=22, interval_minutes=15)
        self.assertEqual(len(slots), 64)
        self.assertEqual(slots[0], "2026-04-16T06:00")
        self.assertEqual(slots[-1], "2026-04-16T21:45")

    def test_choose_schedule_within_bounds_and_unique(self) -> None:
        target, slots = choose_schedule(
            local_date="2026-04-16",
            min_commits=10,
            max_commits=20,
            start_hour=6,
            end_hour=22,
            interval_minutes=15,
            seed_salt="test",
        )
        self.assertTrue(10 <= target <= 20)
        self.assertEqual(len(slots), target)
        self.assertEqual(len(set(slots)), len(slots))

    def test_should_run_matches_bucket(self) -> None:
        now = datetime(2026, 4, 16, 9, 7, tzinfo=ZoneInfo("Asia/Manila"))
        self.assertTrue(should_run(now, ["2026-04-16T09:00"], interval_minutes=15))
        self.assertFalse(should_run(now, ["2026-04-16T09:15"], interval_minutes=15))

    def test_schedule_changes_across_days(self) -> None:
        day1 = choose_schedule("2026-04-16", 10, 20, 6, 22, 15, "salt")
        day2 = choose_schedule("2026-04-17", 10, 20, 6, 22, 15, "salt")
        self.assertNotEqual(day1, day2)


if __name__ == "__main__":
    unittest.main()
