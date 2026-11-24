import math

def mrp(stock, safety, daily_demand, open_pos, lead_time, horizon, min_lot, rounding):
    """open_pos: {day: qty}. Returns proposals [(order_day, receipt_day, qty)] and projected stock."""
    proposals, projected, planned = [], [], {}
    level = stock
    for day in range(horizon):
        level += open_pos.get(day, 0) + planned.get(day, 0) - daily_demand[day]
        if level < safety:
            receipt = day
            order_day = receipt - lead_time
            if order_day < 0:
                raise RuntimeError(f"Shortage on day {day}: lead time {lead_time} too long, expedite needed")
            qty = max(min_lot, safety - level)
            qty = math.ceil(qty / rounding) * rounding
            planned[day] = planned.get(day, 0) + qty
            level += qty
            proposals.append((order_day, receipt, qty))
        projected.append(level)
    return proposals, projected
