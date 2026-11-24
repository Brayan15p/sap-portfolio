from datetime import date, timedelta
from statistics import pstdev
def predict(history, invoice_due: date, half_life=5):
    """history: list of days late, oldest first."""
    if not history: return {"date": invoice_due, "expected_delay": 0, "reliability": "LOW"}
    w = [0.5 ** ((len(history) - 1 - i) / half_life) for i in range(len(history))]
    delay = sum(d * wi for d, wi in zip(history, w)) / sum(w)
    sd = pstdev(history) if len(history) > 1 else 99
    rel = "HIGH" if sd <= 5 and len(history) >= 6 else "MEDIUM" if sd <= 15 else "LOW"
    return {"date": invoice_due + timedelta(days=round(delay)), "expected_delay": round(delay, 1), "reliability": rel}
