import { DatabaseSync } from "node:sqlite";
import type { OrderState } from "./types.js";

export interface Row { updated_at: string; company: string; external_id: string; state: OrderState; doc_entry: number | null; attempts: number; last_error: string | null; }

/** Persistent idempotency ledger. UNIQUE(company, external_id) is the guard against duplicates. */
export class Store {
  db: DatabaseSync;
  constructor(path = ":memory:") {
    this.db = new DatabaseSync(path);
    this.db.exec(`CREATE TABLE IF NOT EXISTS orders(
      company TEXT NOT NULL, external_id TEXT NOT NULL, state TEXT NOT NULL,
      doc_entry INTEGER, attempts INTEGER NOT NULL DEFAULT 0, last_error TEXT,
      updated_at TEXT NOT NULL DEFAULT (datetime('now')),
      PRIMARY KEY(company, external_id))`);
  }
  /** Atomically claims the order. Returns true only for the first caller. */
  claim(company: string, id: string): boolean {
    const r = this.db.prepare(`INSERT OR IGNORE INTO orders(company, external_id, state, attempts) VALUES(?,?,'SENDING',1)`).run(company, id);
    return Number(r.changes) === 1;
  }
  get(company: string, id: string): Row | undefined {
    return this.db.prepare(`SELECT * FROM orders WHERE company=? AND external_id=?`).get(company, id) as Row | undefined;
  }
  ageMs(row: Row): number { return Date.now() - Date.parse(row.updated_at.replace(" ", "T") + "Z"); }
  set(company: string, id: string, state: OrderState, docEntry: number | null = null, err: string | null = null) {
    this.db.prepare(`UPDATE orders SET state=?, doc_entry=COALESCE(?, doc_entry), last_error=?, updated_at=datetime('now') WHERE company=? AND external_id=?`)
      .run(state, docEntry, err, company, id);
  }
}
