from datetime import date, timedelta

def time_calls(last_done: date, cycle_days: int, horizon_end: date, open_order: bool):
    if open_order:
        return []
    calls, nxt = [], last_done + timedelta(days=cycle_days)
    while nxt <= horizon_end:
        calls.append(nxt); nxt += timedelta(days=cycle_days)
    return calls

def counter_call(last_reading_at_done: float, current: float, daily_rate: float, cycle: float, today: date):
    remaining = last_reading_at_done + cycle - current
    if remaining <= 0:
        return {"due": today, "overdue_hours": -remaining}
    return {"due": today + timedelta(days=int(remaining // daily_rate)), "overdue_hours": 0}
