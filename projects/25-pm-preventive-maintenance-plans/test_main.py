from datetime import date
from main import time_calls, counter_call

def test_time_based_calls_in_horizon():
    assert time_calls(date(2026, 1, 1), 90, date(2026, 12, 31), False) == [date(2026, 4, 1), date(2026, 6, 30), date(2026, 9, 28), date(2026, 12, 27)]

def test_open_order_blocks_new_call():
    assert time_calls(date(2026, 1, 1), 90, date(2026, 12, 31), True) == []

def test_counter_based_forecast_and_overdue():
    assert counter_call(1000, 1300, 20, 500, date(2026, 11, 23))["due"] == date(2026, 12, 3)
    assert counter_call(1000, 1550, 20, 500, date(2026, 11, 23))["overdue_hours"] == 50
