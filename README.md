# SAP Portfolio — Brayan Pedraza

100 projects on real SAP business processes: Business One sales and finance, S/4HANA Finance (FI/CO), MM sourcing, integration patterns and modern ABAP (RAP).
Each project states the business problem, encodes the rule in code and **proves it with automated tests**.

```bash
./run_all_tests.sh     # 99 runnable projects, 179 automated tests
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
| 17 | [Colombian withholding taxes](projects/17-fi-co-withholding-taxes) | FI Colombia | Retefuente by UVT minimum base, ReteIVA, ReteICA; balanced entry | Python |
| 18 | [Credit limit check](projects/18-sd-credit-limit-check) | SD Credit | Exposure = AR + open orders + order; overdue blocks; one-time release with reason | Python |
| 19 | [Three-way match](projects/19-mm-three-way-match) | MM / FI-AP (MIRO) | Invoice > received or price above tolerance → payment block with reason | Python |
| 20 | [Pricing procedure](projects/20-sd-pricing-procedure) | SD Pricing | Access sequence, customer discount, volume scale, IVA, step by step | Python |
| 21 | [MRP reorder](projects/21-mm-mrp-reorder) | MM/PP MRP | Safety stock, lead time, minimum lot, pack rounding; shortage alert | Python |
| 22 | [Bank statement reconciliation](projects/22-fi-bank-statement-reconciliation) | FI Bank | Reference/amount matching, GMF and fees to expense, worklist for the rest | Python |
| 23 | [FX revaluation](projects/23-fi-fx-revaluation) | FI Valuation | USD open items at closing TRM, gain/loss and reversal next day | Python |
| 24 | [Asset depreciation](projects/24-fi-aa-depreciation) | FI-AA | Straight line from next month, salvage value, partial retirement | Python |
| 25 | [Preventive maintenance plans](projects/25-pm-preventive-maintenance-plans) | PM | Time- and counter-based calls; open order blocks duplicate | Python |
| 26 | [ATP check](projects/26-sd-atp-check) | SD/MM ATP | Confirms partial now, rest after receipt, never steals committed stock | Python |
| 27 | [Batch FEFO picking](projects/27-mm-batch-fefo-picking) | MM Batches | First-expired-first-out, minimum shelf life, quality block | Python |
| 28 | [Payment run proposal](projects/28-fi-payment-run-proposal) | FI F110 | Early-payment discounts first, blocked vendors, bank limit | Python |
| 29 | [Overhead assessment](projects/29-co-overhead-assessment) | CO KSU5 | Sequential cycles by drivers; sender zero; total preserved to the peso | Python |
| 30 | [IDoc ORDERS05 inbound](projects/30-int-idoc-orders-inbound) | Integration | Status 51 with messages, reprocess to 53 after master data fix | Python |
| 31 | [AMS ticket SLA](projects/31-ams-ticket-sla-triage) | AMS Support | Impact x urgency priority, business-hours SLA clock, pauses, escalation | Python |
| 32 | [Period close cockpit](projects/32-fi-period-close-cockpit) | FI Close | Task dependencies, cycle detection, no close with critical tasks open | Python |
| 33 | [DIAN e-invoice validator](projects/33-b1-dian-e-invoice-validator) | B1 Colombia | NIT check digit, IVA by rate group, totals, CUFE SHA-384 | Python |
| 34 | [Landed costs (imports)](projects/34-b1-landed-costs-import) | B1 Landed Costs | Freight/insurance by value, handling by weight, duty on CIF; exact to the peso | Python |
| 35 | [Moving average inventory](projects/35-b1-moving-average-inventory) | B1 Inventory | Average cost on receipts, returns at receipt price, negative stock refused | Python |
| 36 | [Branch stock rebalancing](projects/36-b1-branch-stock-rebalancing) | B1 Multi-warehouse | Transfers from surplus to deficit, cheapest route, safety stock kept | Python |
| 37 | [Volume rebates](projects/37-sd-volume-rebates) | SD Rebates | Retroactive tiers, monthly accruals with catch-up, exact settlement | Python |
| 38 | [Vendor evaluation](projects/38-mm-vendor-evaluation) | MM | Price, on-time and quality scores; cheapest is not automatically best | Python |
| 39 | [13-week cash forecast](projects/39-fi-13-week-cash-forecast) | FI Cash | Collections by real customer delay, first week below minimum flagged | Python |
| 40 | [Product cost estimate](projects/40-co-product-cost-estimate) | CO-PC | Multi-level BOM with scrap, routing x activity rates, overhead, recursion check | Python |
| 41 | [Finite capacity scheduling](projects/41-pp-finite-capacity-scheduling) | PP | Backward scheduling, capacity never exceeded, late orders with bottleneck | Python |
| 42 | [Short dump analyzer](projects/42-ams-short-dump-analyzer) | AMS | Groups ST22 dumps by exception/program/line, ranks, suggests first check | Python |
| 43 | [Brazil NF-e access key](projects/43-br-nfe-access-key) | Localization Brazil | 44-digit chave de acesso, mod-11 DV, CNPJ validation, tamper detection | Python |
| 44 | [India GSTIN + GST](projects/44-in-gstin-gst-calculator) | Localization India | Base-36 GSTIN checksum; CGST+SGST vs IGST by state | Python |
| 45 | [EU VAT determination](projects/45-eu-vat-determination) | Tax EU | Domestic, reverse charge, OSS destination rate, export | Python |
| 46 | [Mexico CFDI 4.0 totals](projects/46-mx-cfdi-totals) | Localization Mexico | RFC type, IVA 16%, withheld IVA/ISR, totals the PAC checks | Python |
| 47 | [IFRS 16 leases](projects/47-ifrs16-lease-accounting) | RE-FX / IFRS | Lease liability at PV, right-of-use asset, interest/principal split | Python |
| 48 | [Multi-currency consolidation](projects/48-group-consolidation-multicurrency) | Group Reporting | Closing/average/historical rates, CTA, intercompany mismatch report | Python |
| 49 | [US sales tax nexus](projects/49-us-sales-tax-nexus) | Tax US | Economic nexus by sales/transactions with AND/OR state rules | Python |
| 50 | [Outbox event hub](projects/50-int-outbox-event-hub) | Integration infrastructure | Atomic write+event, per-subscriber retries with backoff, dead letter; HTTP API, Dockerfile, docker-compose | Python, SQLite, Docker |


## Projects 51–100: built from the biggest real SAP problems

Research basis: public post-mortems of Lidl (~€500M written off; heavy customization to mimic its legacy purchase-price valuation), Haribo (S/4HANA go-live with processes incompatible with the software) and Revlon (shipping disruption attributed to lack of design and effective controls), plus the most cited S/4HANA migration risks (data quality, Business Partner/CVI, custom code) and recurring ABAP interview topics (performance, authorizations, transports).

## Block A — Migration and data quality (Lidl, Haribo, S/4HANA conversions)

| # | Project | Area | Rule proven by tests | Stack |
|---|---|---|---|---|
| 51 | [Mig Business Partner Duplicates](projects/51-mig-business-partner-duplicates) | S/4HANA migration · Business Partner (CVI) | see README | Python |
| 52 | [Mig Cvi Readiness Check](projects/52-mig-cvi-readiness-check) | S/4HANA migration · CVI readiness | see README | Python |
| 53 | [Mig Custom Code S4 Scanner](projects/53-mig-custom-code-s4-scanner) | S/4HANA migration · Custom code analysis | see README | Python |
| 54 | [Mig Mock Load Reconciliation](projects/54-mig-mock-load-reconciliation) | Data migration · Mock load reconciliation | see README | Python |
| 55 | [Mig Material Master Completeness](projects/55-mig-material-master-completeness) | Master data · Material master | see README | Python |
| 56 | [Mig Value Mapping Validator](projects/56-mig-value-mapping-validator) | Data migration · Value mapping | see README | Python |
| 57 | [Mig Cutover Critical Path](projects/57-mig-cutover-critical-path) | Go-live · Cutover planning | see README | Python |
| 58 | [Golive Hypercare Burndown](projects/58-golive-hypercare-burndown) | Go-live · Hypercare | see README | Python |

## Block B — Controls and fraud (Revlon: "lack of design and effective controls")

| # | Project | Area | Rule proven by tests | Stack |
|---|---|---|---|---|
| 59 | [O2C Stuck Orders Monitor](projects/59-o2c-stuck-orders-monitor) | SD · Order-to-cash monitoring | see README | Python |
| 60 | [Grc Sod Conflicts](projects/60-grc-sod-conflicts) | GRC · Segregation of duties | see README | Python |
| 61 | [Grc Vendor Bank Change Fraud](projects/61-grc-vendor-bank-change-fraud) | FI-AP · Fraud detection | see README | Python |
| 62 | [Mm Grir Clearing Analyzer](projects/62-mm-grir-clearing-analyzer) | MM/FI · GR/IR clearing | see README | Python |
| 63 | [Sox Control Sampling](projects/63-sox-control-sampling) | Audit · SOX / internal control testing | see README | Python |
| 64 | [Grc Critical Access Firefighter](projects/64-grc-critical-access-firefighter) | GRC · Emergency access | see README | Python |

## Block C — Performance and operations (most asked in interviews)

| # | Project | Area | Rule proven by tests | Stack |
|---|---|---|---|---|
| 65 | [Perf Sql Trace Analyzer](projects/65-perf-sql-trace-analyzer) | ABAP performance · ST05 SQL trace | see README | Python |
| 66 | [Perf Internal Table Choice](projects/66-perf-internal-table-choice) | ABAP performance · Internal tables | see README | Python |
| 67 | [Basis Job Chain Scheduler](projects/67-basis-job-chain-scheduler) | Basis · Background jobs (SM36/SM37) | see README | Python |
| 68 | [Basis Transport Collision](projects/68-basis-transport-collision) | Basis · Transport management (STMS) | see README | Python |
| 69 | [Basis Job Runtime Anomaly](projects/69-basis-job-runtime-anomaly) | Basis / AMS · Proactive monitoring | see README | Python |
| 70 | [Int Qrfc Queue Monitor](projects/70-int-qrfc-queue-monitor) | Integration · qRFC/bgRFC queues (SMQ1/SMQ2) | see README | Python |

## Block D — Retail and inventory (Lidl's retail vs purchase price valuation)

| # | Project | Area | Rule proven by tests | Stack |
|---|---|---|---|---|
| 71 | [Retail Method Vs Cost Valuation](projects/71-retail-method-vs-cost-valuation) | IS-Retail · Inventory valuation (Lidl case) | see README | Python |
| 72 | [Retail Promo Replenishment](projects/72-retail-promo-replenishment) | IS-Retail · Store replenishment with promotions | see README | Python |
| 73 | [Mm Abc Xyz Classification](projects/73-mm-abc-xyz-classification) | MM · Inventory segmentation | see README | Python |
| 74 | [Mm Obsolete Stock Provision](projects/74-mm-obsolete-stock-provision) | MM/FI · Slow-moving and obsolete stock | see README | Python |
| 75 | [Wm Slotting By Velocity](projects/75-wm-slotting-by-velocity) | EWM/WM · Warehouse slotting | see README | Python |

## Block E — Innovation: AI, ESG, treasury, logistics, governance

| # | Project | Area | Rule proven by tests | Stack |
|---|---|---|---|---|
| 76 | [Ai Gl Account Suggestion](projects/76-ai-gl-account-suggestion) | AI · Accounts payable automation | see README | Python |
| 77 | [Ai Benford Journal Anomalies](projects/77-ai-benford-journal-anomalies) | Audit analytics · Journal entries | see README | Python |
| 78 | [Ai Invoice Text Extraction](projects/78-ai-invoice-text-extraction) | AI · Document capture | see README | Python |
| 79 | [Ai Payment Date Prediction](projects/79-ai-payment-date-prediction) | AI · Receivables | see README | Python |
| 80 | [Ai Demand Forecast Holt](projects/80-ai-demand-forecast-holt) | AI · Demand planning (IBP) | see README | Python |
| 81 | [Ai Cash Application Remittance](projects/81-ai-cash-application-remittance) | AI · Cash application | see README | Python |
| 82 | [Ai Spend Classification](projects/82-ai-spend-classification) | Procurement analytics · Spend cube | see README | Python |
| 83 | [Ai Natural Language Report Query](projects/83-ai-natural-language-report-query) | Innovation · Natural-language analytics | see README | Python |
| 84 | [Pm Reliability Mtbf](projects/84-pm-reliability-mtbf) | PM · Reliability engineering | see README | Python |
| 85 | [Esg Purchase Carbon Footprint](projects/85-esg-purchase-carbon-footprint) | ESG · Scope 3 emissions (Sustainability Footprint) | see README | Python |
| 86 | [Fin Dynamic Discounting](projects/86-fin-dynamic-discounting) | Treasury · Dynamic discounting / supply chain finance | see README | Python |
| 87 | [Contract Price Escalation](projects/87-contract-price-escalation) | MM/SD · Contract price adjustment | see README | Python |
| 88 | [Supplier Risk Scoring](projects/88-supplier-risk-scoring) | Procurement · Supplier risk | see README | Python |
| 89 | [Global E Invoice Router](projects/89-global-e-invoice-router) | Global compliance · E-invoicing | see README | Python |
| 90 | [Ps Earned Value](projects/90-ps-earned-value) | SAP PS · Project control (EVM) | see README | Python |
| 91 | [Ams Sla Penalties](projects/91-ams-sla-penalties) | AMS / Outsourcing · Service credits | see README | Python |
| 92 | [Tm Freight Cost Allocation](projects/92-tm-freight-cost-allocation) | SAP TM · Freight settlement | see README | Python |
| 93 | [Tm Truck Load Building](projects/93-tm-truck-load-building) | SAP TM · Load planning | see README | Python |
| 94 | [Treasury Intercompany Netting](projects/94-treasury-intercompany-netting) | Treasury · Multilateral netting | see README | Python |
| 95 | [Treasury Fx Exposure Hedging](projects/95-treasury-fx-exposure-hedging) | Treasury · FX risk | see README | Python |
| 96 | [Qm Acceptance Sampling](projects/96-qm-acceptance-sampling) | SAP QM · Inspection lots | see README | Python |
| 97 | [Sd Customer Rfm Churn](projects/97-sd-customer-rfm-churn) | SD / CX · Customer analytics | see README | Python |
| 98 | [Mdg Change Request Workflow](projects/98-mdg-change-request-workflow) | SAP MDG · Master data governance | see README | Python |
| 99 | [Btp Api Rate Limit Client](projects/99-btp-api-rate-limit-client) | SAP BTP · Resilient API consumption | see README | Python |

## Capstone

| # | Project | Area | Rule proven by tests | Stack |
|---|---|---|---|---|
| 100 | [Capstone Go Live Readiness Score](projects/100-capstone-go-live-readiness-score) | Capstone · Go-live readiness (lessons from Lidl, Haribo, Revlon) | see README | Python |

## Verification status (honest)

- **01–14, 17–100:** business logic verified locally with pytest. They model SAP processes; they are not yet connected to a live SAP system.
- **15:** verified against a Service Layer HTTP simulator. Real B1 company test pending.
- **16:** ABAP source complete; activation and ABAP Unit run in an ABAP Cloud system pending.

## Author

Brayan Pedraza · Systems + Industrial Engineering · Bogotá, Colombia · Remote · apedrazacespedes@gmail.com
