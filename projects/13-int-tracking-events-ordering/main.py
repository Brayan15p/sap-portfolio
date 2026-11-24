RANK = {"CREATED": 0, "PICKED_UP": 1, "IN_TRANSIT": 2, "OUT_FOR_DELIVERY": 3, "DELIVERED": 4}

class Shipment:
    def __init__(self, guide, delivery_doc):
        self.guide, self.delivery_doc = guide, delivery_doc
        self.status, self.ts, self.history = "CREATED", "", []
    def apply(self, ev):
        self.history.append(ev)
        newer = ev["ts"] > self.ts
        forward = RANK[ev["status"]] >= RANK[self.status]
        if newer and forward:
            self.status, self.ts = ev["status"], ev["ts"]
            return True
        return False
