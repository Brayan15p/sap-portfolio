class ReturnsLedger:
    def __init__(self, delivered: dict):
        self.delivered = delivered          # (doc, line) -> qty delivered
        self.returned = {}
    def returnable(self, doc, line):
        return self.delivered[(doc, line)] - self.returned.get((doc, line), 0)
    def request(self, doc, line, qty, reason):
        if (doc, line) not in self.delivered:
            raise KeyError("Return must reference a delivered document line")
        if not reason:
            raise ValueError("Reason is mandatory")
        if qty <= 0 or qty > self.returnable(doc, line):
            raise ValueError(f"Max returnable is {self.returnable(doc, line)}")
        self.returned[(doc, line)] = self.returned.get((doc, line), 0) + qty
        return self.returnable(doc, line)
