import json, sqlite3, time

class Hub:
    def __init__(self, path=":memory:", max_attempts=5, base_delay=1.0):
        self.db = sqlite3.connect(path, isolation_level=None, check_same_thread=False)
        self.max_attempts, self.base_delay = max_attempts, base_delay
        self.db.executescript("""
          CREATE TABLE IF NOT EXISTS deliveries_doc(doc TEXT PRIMARY KEY, payload TEXT);
          CREATE TABLE IF NOT EXISTS outbox(id INTEGER PRIMARY KEY, type TEXT, payload TEXT);
          CREATE TABLE IF NOT EXISTS dispatch(event_id INT, subscriber TEXT, status TEXT, attempts INT DEFAULT 0,
                                             next_at REAL DEFAULT 0, last_error TEXT, PRIMARY KEY(event_id, subscriber));
          CREATE TABLE IF NOT EXISTS dead_letter(event_id INT, subscriber TEXT, error TEXT);""")
        self.subscribers = {}
    def subscribe(self, name, handler): self.subscribers[name] = handler
    def post_delivery(self, doc, payload):
        """Business write + event in ONE transaction: either both exist or neither."""
        self.db.execute("BEGIN")
        try:
            self.db.execute("INSERT INTO deliveries_doc VALUES(?,?)", (doc, json.dumps(payload)))
            eid = self.db.execute("INSERT INTO outbox(type,payload) VALUES('DeliveryPosted',?)", (json.dumps({"doc": doc, **payload}),)).lastrowid
            for s in self.subscribers:
                self.db.execute("INSERT INTO dispatch(event_id,subscriber,status) VALUES(?,?,'PENDING')", (eid, s))
            self.db.execute("COMMIT"); return eid
        except Exception:
            self.db.execute("ROLLBACK"); raise
    def relay(self, now=None):
        now = time.time() if now is None else now
        rows = self.db.execute("""SELECT d.event_id,d.subscriber,d.attempts,o.payload FROM dispatch d JOIN outbox o ON o.id=d.event_id
                                  WHERE d.status='PENDING' AND d.next_at<=? ORDER BY d.event_id""", (now,)).fetchall()
        for eid, sub, attempts, payload in rows:
            try:
                self.subscribers[sub](json.loads(payload))
                self.db.execute("UPDATE dispatch SET status='DONE', attempts=? WHERE event_id=? AND subscriber=?", (attempts + 1, eid, sub))
            except Exception as e:
                attempts += 1
                if attempts >= self.max_attempts:
                    self.db.execute("UPDATE dispatch SET status='DEAD', attempts=?, last_error=? WHERE event_id=? AND subscriber=?", (attempts, str(e), eid, sub))
                    self.db.execute("INSERT INTO dead_letter VALUES(?,?,?)", (eid, sub, str(e)))
                else:
                    delay = self.base_delay * 2 ** (attempts - 1)
                    self.db.execute("UPDATE dispatch SET attempts=?, next_at=?, last_error=? WHERE event_id=? AND subscriber=?", (attempts, now + delay, str(e), eid, sub))
    def status(self):
        return dict(self.db.execute("SELECT status, COUNT(*) FROM dispatch GROUP BY status").fetchall())
