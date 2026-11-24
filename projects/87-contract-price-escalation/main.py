from decimal import Decimal, ROUND_HALF_UP
def q(x): return Decimal(x).quantize(Decimal("1"), ROUND_HALF_UP)
def adjust(base_price, indices, weights=None, cap_pct=None):
    """indices: list per year of dict {component: pct_change}; weights: {component: weight} or None for single index 'ipc'."""
    price = Decimal(base_price); history = []
    for year, idx in enumerate(indices, 1):
        pct = sum(Decimal(str(weights[c])) * Decimal(str(idx[c])) for c in weights) if weights else Decimal(str(idx["ipc"]))
        if cap_pct is not None: pct = min(pct, Decimal(str(cap_pct)))
        price = q(price * (1 + pct / 100)); history.append((year, float(pct), price))
    return history
def back_billing(old_price, new_price, months_late, volume_per_month):
    return q((Decimal(new_price) - Decimal(old_price)) * months_late * volume_per_month)
