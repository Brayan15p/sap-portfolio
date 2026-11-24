class Pipeline:
    def __init__(self, mapping):
        self.mapping, self.dlq, self.delivered = mapping, {}, []
    def handle(self, msg):
        try:
            self.delivered.append({"corr": msg["corr"], **self.mapping(msg)})
        except Exception as e:
            self.dlq[msg["corr"]] = {"msg": msg, "error": f"{type(e).__name__}: {e}"}
    def reprocess(self, corr_ids=None):
        for corr in list(corr_ids or self.dlq):
            entry = self.dlq.pop(corr)
            self.handle(entry["msg"])
