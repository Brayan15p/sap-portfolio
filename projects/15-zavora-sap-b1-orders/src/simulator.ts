import http from "node:http";

/** Fake Service Layer. mode "drop-after-create" stores the order then kills the socket (lost response). */
export function startSimulator(port = 0) {
  const orders: { DocEntry: number; NumAtCard: string; body: any }[] = [];
  const state = { mode: "ok" as "ok" | "drop-after-create" | "down", posts: 0 };
  const server = http.createServer((req, res) => {
    if (state.mode === "down") { req.socket.destroy(); return; }
    let raw = ""; req.on("data", (c) => (raw += c));
    req.on("end", () => {
      const url = new URL(req.url!, "http://x");
      if (req.method === "POST" && url.pathname === "/b1s/v2/Orders") {
        state.posts++;
        const body = JSON.parse(raw);
        if (!body.CardCode) { res.writeHead(400).end(JSON.stringify({ error: { message: "CardCode missing" } })); return; }
        const o = { DocEntry: 1000 + orders.length + 1, NumAtCard: body.NumAtCard, body };
        orders.push(o);
        if (state.mode === "drop-after-create") { req.socket.destroy(); return; }
        res.writeHead(201, { "Content-Type": "application/json" }).end(JSON.stringify({ DocEntry: o.DocEntry, ...body }));
        return;
      }
      if (req.method === "GET" && url.pathname === "/b1s/v2/Orders") {
        const m = /NumAtCard eq '(.*)'/.exec(url.searchParams.get("$filter") ?? "");
        const ref = m?.[1].replace(/''/g, "'");
        res.writeHead(200, { "Content-Type": "application/json" })
          .end(JSON.stringify({ value: orders.filter((o) => o.NumAtCard === ref).map((o) => ({ DocEntry: o.DocEntry })) }));
        return;
      }
      res.writeHead(404).end();
    });
  });
  return new Promise<{ url: string; orders: typeof orders; state: typeof state; close: () => void }>((resolve) => {
    server.listen(port, () => {
      const p = (server.address() as any).port;
      resolve({ url: `http://127.0.0.1:${p}`, orders, state, close: () => server.close() });
    });
  });
}
