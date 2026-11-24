# zavora-sap-b1-orders

Idempotent connector that turns a **confirmed WhatsApp order** into a **SAP Business One sales order** through the Service Layer (OData V4, `/b1s/v2/Orders`).

The business question it answers: *if SAP creates the order but the response is lost, how do we make sure the distributor does not ship it twice?*

## How it works

```
WhatsApp order ─► validate ─► atomic claim (SQLite ledger, UNIQUE company+externalId)
                                  │
                                  ▼
                           POST /b1s/v2/Orders  (NumAtCard = ZAV-<company>-<externalId>)
                       ┌──────────┼───────────────┐
                    201 OK      4xx            timeout / socket lost
                   CREATED     REVIEW            UNCERTAIN
                                                    │  redelivery or recovery job
                                                    ▼
                                GET Orders?$filter=NumAtCard eq '…'
                                found → CREATED (no second POST)
                                absent → POST once
                                SAP unreachable → stays UNCERTAIN (never blind re-POST)
```

| State | Meaning |
|---|---|
| `REJECTED` | Bad input (unknown SKU, customer, warehouse, quantity). Zero calls to SAP. |
| `SENDING` | A worker holds the lease and is posting now. Concurrent duplicates do nothing. |
| `CREATED` | SAP returned or confirmed a `DocEntry`. |
| `UNCERTAIN` | The order may exist in SAP. Resolved only by lookup, never by blind retry. |
| `REVIEW` | SAP rejected the data (4xx). A person fixes master data. |

## Run it

```bash
npm install
npm test        # 12 tests
npm run demo    # end-to-end against the simulator
```

Demo output:

```
1) Valid order                 -> CREATED, DocEntry 1001, 1 POST
2) Same WhatsApp event         -> CREATED, 0 POSTs
3) SAP creates, response lost  -> UNCERTAIN
4) Redelivery reconciles       -> CREATED, 0 POSTs
SAP orders: 2 (expected 2)
```

## Tested scenarios

- Valid order; unknown SKU (no SAP call); invalid quantity
- Body mapping to `Orders` (`CardCode`, `DocDueDate`, `DocCurrency`, `NumAtCard`, `DocumentLines`)
- Same event twice; two concurrent deliveries → one POST
- Same external id in two companies → two orders (multi-tenant)
- Response lost after create → reconciled without a second order
- Process restart with persistent ledger
- SAP down before send; SAP still down during retry
- Worker crash mid-send (lease expiry)

## Verification status

| Level | Status |
|---|---|
| Unit + integration tests against HTTP simulator | ✅ passing |
| Real SAP Business One company (Service Layer) | ⏳ pending: needs demo company access. Steps: login (`POST /b1s/v2/Login`), check `$metadata` for the fields above, send `examples/order.json`, keep sanitized `DocEntry` evidence. |

Field names follow the SAP Business One Service Layer API reference; confirm them against the `$metadata` of your installation.

## Stack

TypeScript · Node 22 (`node:sqlite`) · Vitest · native `fetch`. No credentials in the repo; real server cookie goes through environment.
