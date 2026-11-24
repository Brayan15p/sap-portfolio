from decimal import Decimal, ROUND_HALF_UP

def q(x): return Decimal(x).quantize(Decimal("0.0001"), ROUND_HALF_UP)

class Item:
    def __init__(self):
        self.qty, self.value, self.journal = Decimal(0), Decimal(0), []
    @property
    def avg(self): return q(self.value / self.qty) if self.qty else Decimal(0)
    def receive(self, qty, unit_cost, doc):
        qty, unit_cost = Decimal(qty), Decimal(unit_cost)
        self.qty += qty; self.value += qty * unit_cost
        self.journal.append((doc, "GRPO", qty, unit_cost, self.avg))
    def issue(self, qty, doc):
        qty = Decimal(qty)
        if qty > self.qty: raise ValueError(f"{doc}: negative stock not allowed ({self.qty} on hand)")
        cost = q(qty * self.avg)
        self.qty -= qty; self.value -= cost
        self.journal.append((doc, "ISSUE", qty, self.avg, cost)); return cost
    def return_to_vendor(self, qty, receipt_cost, doc):
        qty = Decimal(qty)
        if qty > self.qty: raise ValueError("Cannot return more than on hand")
        self.qty -= qty; self.value -= qty * Decimal(receipt_cost)
        self.journal.append((doc, "RETURN", qty, Decimal(receipt_cost), self.avg))
