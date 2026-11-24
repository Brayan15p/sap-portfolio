from dataclasses import dataclass, field

@dataclass
class OrderLine:
    line: int
    item: str
    ordered: float
    delivered: float = 0.0
    @property
    def open_qty(self) -> float:
        return round(self.ordered - self.delivered, 6)

@dataclass
class SalesOrder:
    doc_entry: int
    lines: dict = field(default_factory=dict)
    def add(self, line: int, item: str, qty: float):
        self.lines[line] = OrderLine(line, item, qty)
    def deliver(self, base_line: int, qty: float):
        ln = self.lines.get(base_line)
        if ln is None:
            raise KeyError(f"BaseLine {base_line} not in order {self.doc_entry}")
        if qty <= 0:
            raise ValueError("Delivery quantity must be > 0")
        if qty > ln.open_qty:
            raise ValueError(f"Line {base_line}: delivering {qty} exceeds open {ln.open_qty}")
        ln.delivered += qty
    @property
    def status(self) -> str:
        if all(l.open_qty == 0 for l in self.lines.values()):
            return "CLOSED"
        if any(l.delivered > 0 for l in self.lines.values()):
            return "PARTIAL"
        return "OPEN"
