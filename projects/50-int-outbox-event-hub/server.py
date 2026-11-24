"""Minimal HTTP API: POST /deliveries {doc, ...} ; GET /status. Relay runs in a background thread."""
import json, os, threading, time, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from main import Hub

hub = Hub(os.environ.get("DB_PATH", "/data/hub.db"))
for name, url in (s.split("=", 1) for s in os.environ.get("SUBSCRIBERS", "").split(",") if s):
    def send(e, url=url):
        req = urllib.request.Request(url, json.dumps(e).encode(), {"Content-Type": "application/json"})
        urllib.request.urlopen(req, timeout=5)
    hub.subscribe(name, send)

class H(BaseHTTPRequestHandler):
    def _json(self, code, body):
        self.send_response(code); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps(body).encode())
    def do_POST(self):
        if self.path != "/deliveries": return self._json(404, {})
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        try: self._json(201, {"event_id": hub.post_delivery(body.pop("doc"), body)})
        except Exception as e: self._json(409, {"error": str(e)})
    def do_GET(self):
        self._json(200, hub.status()) if self.path == "/status" else self._json(404, {})

def loop():
    while True: hub.relay(); time.sleep(1)

if __name__ == "__main__":
    threading.Thread(target=loop, daemon=True).start()
    ThreadingHTTPServer(("0.0.0.0", 8080), H).serve_forever()
