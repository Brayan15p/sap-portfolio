/** Minimal Service Layer client (OData V4, /b1s/v2). Session login omitted in simulator mode; add B1SESSION cookie for a real server. */
export class B1Client {
  constructor(private baseUrl: string, private cookie = "", private timeoutMs = 3000) {}
  private async req(path: string, init: RequestInit = {}) {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), this.timeoutMs);
    try {
      return await fetch(`${this.baseUrl}${path}`, { ...init, signal: ctrl.signal,
        headers: { "Content-Type": "application/json", ...(this.cookie ? { Cookie: this.cookie } : {}) } });
    } finally { clearTimeout(t); }
  }
  async createOrder(body: unknown): Promise<{ DocEntry: number }> {
    const r = await this.req(`/b1s/v2/Orders`, { method: "POST", body: JSON.stringify(body) });
    if (!r.ok) throw new B1HttpError(r.status, await r.text());
    return r.json() as Promise<{ DocEntry: number }>;
  }
  /** Lookup by our external reference. Used to resolve an uncertain create. */
  async findByRef(ref: string): Promise<number | null> {
    const q = encodeURIComponent(`NumAtCard eq '${ref.replace(/'/g, "''")}'`);
    const r = await this.req(`/b1s/v2/Orders?$select=DocEntry&$filter=${q}`);
    if (!r.ok) throw new B1HttpError(r.status, await r.text());
    const j = (await r.json()) as { value: { DocEntry: number }[] };
    return j.value[0]?.DocEntry ?? null;
  }
}
export class B1HttpError extends Error { constructor(public status: number, body: string) { super(`B1 HTTP ${status}: ${body}`); } }
