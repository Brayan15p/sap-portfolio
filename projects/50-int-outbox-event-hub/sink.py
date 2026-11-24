"""Fake subscriber (carrier / shop) that logs what it receives."""
from http.server import BaseHTTPRequestHandler, HTTPServer
class S(BaseHTTPRequestHandler):
    def do_POST(self):
        print(self.rfile.read(int(self.headers["Content-Length"])).decode(), flush=True)
        self.send_response(200); self.end_headers()
HTTPServer(("0.0.0.0", 9000), S).serve_forever()
