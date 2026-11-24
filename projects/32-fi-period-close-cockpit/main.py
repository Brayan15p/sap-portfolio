class Close:
    def __init__(self, tasks):
        self.tasks = tasks          # {id: {"deps": [...], "critical": bool}}
        self.done = set()
        self._check_cycles()
    def _check_cycles(self):
        seen, stack = set(), set()
        def visit(t):
            if t in stack: raise ValueError(f"Dependency cycle at {t}")
            if t in seen: return
            stack.add(t)
            for d in self.tasks[t]["deps"]: visit(d)
            stack.discard(t); seen.add(t)
        for t in self.tasks: visit(t)
    def ready(self):
        return sorted(t for t, v in self.tasks.items() if t not in self.done and all(d in self.done for d in v["deps"]))
    def complete(self, t, evidence):
        if t not in self.ready(): raise ValueError(f"{t} is blocked by {[d for d in self.tasks[t]['deps'] if d not in self.done]}")
        if not evidence: raise ValueError("Evidence required")
        self.done.add(t)
    def close_period(self):
        pending = [t for t, v in self.tasks.items() if v["critical"] and t not in self.done]
        if pending: raise ValueError(f"Cannot close: critical tasks pending {sorted(pending)}")
        return "PERIOD CLOSED"
