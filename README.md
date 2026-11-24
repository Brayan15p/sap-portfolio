# SAP Portfolio — Brayan Pedraza

16 small, focused projects on real SAP business processes: Business One sales and finance, S/4HANA Finance (FI/CO), MM sourcing, integration patterns and modern ABAP (RAP).
Each project states the business problem, encodes the rule in code and **proves it with automated tests**.

```bash
./run_all_tests.sh     # 15 projects, 47 automated tests
```

| # | Project | Area | Business rule proven by tests | Stack |
|---|---|---|---|---|
| 01 | [Partial deliveries](projects/01-b1-partial-deliveries) | B1 Sales | Order of 20, delivery of 12 → 8 open; over-delivery rejected | Python |
| 02 | [AR aging](projects/02-b1-ar-aging) | B1 Finance | Partial payment shows only open balance, by aging bucket | Python |
| 03 | [Price list importer](projects/03-b1-price-list-importer) | B1 Master data | Invalid file → per-row report, nothing applied | Python |
| 04 | [Returns control](projects/04-b1-returns-control) | B1 Sales | Several returns never exceed delivered qty | Python |
| 05 | [Incremental catalog sync](projects/05-b1-catalog-incremental-sync) | B1 Integration | Network cut mid-sync → resume with no loss, no duplicates | Python |
| 06 | [E-commerce vs B1 totals](projects/06-b1-ecommerce-totals-recon) | B1 Reconciliation | Difference explained by tax, discount or rounding | Python |
| 07 | [Invoice-payment matcher](projects/07-fi-invoice-payment-matcher) | FI-AR | Two invoices with same amount and no reference → review | Python |
| 08 | [Journal entry validator](projects/08-fi-journal-entry-validator) | FI-GL | Balance, currency, cost center rules with line numbers | Python |
| 09 | [Duplicate invoice detector](projects/09-fi-duplicate-invoice-detector) | FI-AP | "FE-00123" and "fe 123" flagged, with reasons | Python |
| 10 | [Budget vs actual](projects/10-co-budget-vs-actual) | CO | Reallocation moves cost, total unchanged | Python |
| 11 | [Historical open items](projects/11-fi-historical-open-items) | FI-AR/AP | Payment after key date doesn't change past balance | Python |
| 12 | [Dead-letter queue](projects/12-int-dead-letter-queue) | Integration | After fixing a mapping, only failed messages are reprocessed | Python |
| 13 | [Tracking events ordering](projects/13-int-tracking-events-ordering) | Integration / Logistics | Old event never regresses a delivered shipment | Python |
| 14 | [Quotation comparator](projects/14-mm-quotation-comparator) | MM Sourcing | Box of 12 vs 12 units normalized; freight changes ranking | Python |
| 15 | [WhatsApp → B1 Orders connector](projects/15-zavora-sap-b1-orders) | B1 Service Layer | Lost response after create → reconciled, never a second order (12 tests) | TypeScript, SQLite |
| 16 | [Maintenance request approval](projects/16-abap-rap-maintenance-requests) | ABAP Cloud / RAP | Approve once; creator can't approve own request | ABAP RAP, CDS, Fiori |

## Verification status (honest)

- **01–14:** business logic verified locally with pytest. They model SAP processes; they are not yet connected to a live SAP system.
- **15:** verified against a Service Layer HTTP simulator. Real B1 company test pending.
- **16:** ABAP source complete; activation and ABAP Unit run in an ABAP Cloud system pending.

## Author

Brayan Pedraza · Systems + Industrial Engineering · Bogotá, Colombia · Remote · apedrazacespedes@gmail.com
