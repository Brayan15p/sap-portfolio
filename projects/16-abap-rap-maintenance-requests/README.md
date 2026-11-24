# abap-rap-maintenance-requests

ABAP Cloud / RAP app for **hospital equipment maintenance requests**: a technician creates a request, submits it, and a supervisor (never the creator) approves or rejects it once. The decision is stored with user and timestamp.

## What it shows

| Topic | Where |
|---|---|
| Managed RAP BO with draft, strict(2) | `src/zr_mr_request.bdef.asbdef` |
| State machine N → S → A/R via **instance features** (a second approval is impossible) | `get_instance_features` |
| **Segregation of duties**: creator cannot approve own request | `get_instance_authorizations` |
| Validations on save (priority, cost/currency) and determination on create | behavior pool |
| Audit trail (`DecidedBy`, `DecidedAt`) | `decide` |
| CDS root + projection, Fiori Elements annotations, OData V4 service | `zr_*`, `zc_*`, `.ddlx`, `.srvd` |
| ABAP Unit with EML and CDS test doubles | `zbp_r_mr_request.clas.testclasses.abap` |

## Status

| Level | Status |
|---|---|
| Source code written | ✅ |
| Activated in an ABAP Cloud system (BTP trial / SAP Learning practice system) | ⏳ pending |
| ABAP Unit run, Fiori Elements preview | ⏳ pending |

## How to run it (ADT for Eclipse, Mac works)

1. Get an ABAP environment: SAP BTP trial ABAP or the SAP Learning student practice system.
2. In ADT create package `ZMR_MAINT`. Create objects in this order: table `ZMR_REQUEST` (+ draft table `ZMR_REQUEST_D` via quick fix), `ZR_MR_REQUEST`, behavior `ZR_MR_REQUEST` (quick fix generates class `ZBP_R_MR_REQUEST`), paste the local types, `ZC_MR_REQUEST` + projection behavior + metadata extension, service definition `ZUI_MR_REQUEST`, service binding `ZUI_MR_REQUEST_O4` (OData V4 UI) → Publish.
3. Run ABAP Unit (Ctrl+Shift+F10) and the Fiori Elements preview from the service binding.
4. Record a 2-minute video: create → submit → approve → approve button disabled; same user cannot approve own request.

Note: files use plain-text extensions for readability; with abapGit you can import the objects after creating them once in ADT.
