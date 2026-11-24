from datetime import date

class CreditCheck:
    def __init__(self, limits, max_overdue_days=30):
        self.limits, self.max_overdue = limits, max_overdue_days
        self.released = {}
    def exposure(self, customer, receivables, open_orders, new_amount):
        ar = sum(i["open"] for i in receivables if i["customer"] == customer)
        oo = sum(o["amount"] for o in open_orders if o["customer"] == customer)
        return ar + oo + new_amount
    def check(self, order, receivables, open_orders, today: date):
        reasons = []
        exp = self.exposure(order["customer"], receivables, open_orders, order["amount"])
        limit = self.limits.get(order["customer"], 0)
        if exp > limit:
            reasons.append(f"exposure {exp} > limit {limit}")
        worst = max([(today - i["due"]).days for i in receivables if i["customer"] == order["customer"] and i["open"] > 0] or [0])
        if worst > self.max_overdue:
            reasons.append(f"oldest overdue {worst} days > {self.max_overdue}")
        if reasons and order["id"] in self.released:
            return {"status": "RELEASED", "reasons": reasons, "by": self.released[order["id"]]}
        return {"status": "BLOCKED" if reasons else "OK", "reasons": reasons, "exposure": exp}
    def release(self, order_id, manager, reason):
        if not reason: raise ValueError("Release needs a reason")
        if order_id in self.released: raise ValueError("Already released")
        self.released[order_id] = (manager, reason)
