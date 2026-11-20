---
name: qc-inspection
description: Plan, run and judge third-party style product quality inspections in China the way QC firms (SGS, QIMA, Bureau Veritas, Intertek, TÜV, V-Trust, AQF) do. Use when the user asks about AQL, ISO 2859-1 / ANSI Z1.4 sample sizes, accept/reject numbers, pre-shipment inspection (PSI), during-production inspection (DUPRO), initial production check (IPC), container loading check (CLC), factory audits (ISO 9001, BSCI/amfori, SMETA, Sedex, GSV), defect classification (critical/major/minor), writing an inspection checklist or QC protocol, reading an inspection report, golden samples, on-site tests (drop test, carton, barcode, function, moisture, colour fastness), or deciding pass/fail/pending. 中文触发词：验货、AQL、抽检、出货前检验、中期检验、首件检验、监装、验厂、质检报告、缺陷分类。
---

# QC Inspection (China, third-party QC firm method)

## Ground rules
- This skill gives method, not proof. A pass/fail decision is only as good as the inspection data. Never claim a lot is good without an inspection report, photos, and the AQL math shown.
- Always state which standard, inspection level and AQLs were used. Default for consumer goods: **ISO 2859-1, single sampling, normal inspection, General Level II, AQL Critical 0 / Major 2.5 / Minor 4.0**. Higher-risk or premium goods: Major 1.5, Minor 2.5. On-site tests use special levels (S-2/S-3/S-4) because they are slow or destructive.
- Compute sample sizes with `scripts/aql.py` (run `python3 scripts/aql.py <lot> [--level II] [--aql 0,2.5,4.0]`; `--selftest` checks it against known table values). Show the user the code letter, sample size, Ac and Re for each class.
- Note on practice: many QC firms use the code-letter sample size for every class and read Ac/Re for that sample size, instead of following the table arrows to a different sample size. If the user's QC firm does this, follow their method and say so. The script follows the standard (arrows resolved, with that plan's sample size).
- Samples are drawn **at random from finished, packed goods** (at least 80% packed for PSI, 100% produced). The inspector picks the cartons, not the factory. Carton count drawn = square root of total cartons, rounded up.

## Inspection types (when to use what)
| Type | When | Purpose |
|---|---|---|
| Factory audit (social / quality / technical) | Before first order | Is the supplier capable and legitimate? ISO 9001 audit, BSCI/amfori, SMETA, technical capability audit |
| Sample check / golden sample | Before mass production | Approve one reference sample, sign and seal it, keep one at factory and one with buyer |
| IPC – Initial Production Check | 0–20% produced | Raw materials, components, first-off products vs golden sample |
| DUPRO – During Production | 20–60% produced | Catch systemic defects while there is time to fix |
| PSI – Pre-Shipment Inspection | 100% produced, ≥80% packed | AQL sampling, the final pass/fail before balance payment |
| CLC – Container Loading Check | At loading | Quantity, carton condition, loading, container condition (7-point check), seal number photo |
| 100% sorting | After a failed PSI | Factory or QC firm checks every unit, then re-inspection |

## PSI checklist (standard sections in QC firm reports)
1. **Quantity**: produced, packed, carton count vs PO.
2. **Packing & marking**: shipping marks, carton dimensions/weight, inner packing, labels, warnings, barcodes (scan test), CE/UKCA/WEEE marks, country of origin, importer name/address (EU GPSR requires EU economic operator details).
3. **Workmanship / visual**: per defect list, against golden sample, at the viewing distance and light the protocol sets (often arm's length, about 60–90 cm, depending on product type and buyer).
4. **Product specs & dimensions**: measured vs spec sheet with tolerances.
5. **Function & safety tests**: product-specific (power-on, hi-pot, earth continuity for electrics; seam strength for textiles; small parts and sharp edges for toys).
6. **On-site tests (special level, usually S-2 or S-3)**: carton drop test (ISTA 1A style: 1 corner, 3 edges, 6 faces), barcode scan, moisture content (wood/paper/textile), colour fastness rub, assembly test, odour, weight check, adhesion tape test for coatings, stability.
7. **Results**: defects found per class vs Ac/Re → Pass / Fail / Pending (pending = something the inspector could not judge, e.g. missing golden sample or spec).

## Defect classification
- **Critical**: could cause injury, breaks a mandatory regulation, or makes the product illegal to sell (sharp edge, exposed live wire, small parts on a 0–3 toy, missing CE mark where it is required, mould). AQL 0: one found = lot fails.
- **Major**: product likely to fail, be returned, or unsellable (does not work, wrong colour, wrong size outside tolerance, visible stain, broken part).
- **Minor**: departs from spec but customer would probably still keep it (small thread end, tiny scratch on a hidden surface).
Write the defect list **before** the inspection, product-specific, with photos of acceptable vs unacceptable where possible. Disputes almost always come from defects that were never defined.

## Decision rules
- For each class: defects found ≤ Ac → accept; ≥ Re → reject. Any class failing = lot fails.
- One unit with several defects: count the most serious one (standard practice), unless the protocol says otherwise.
- Failed lot: options are rework + re-inspection (factory usually pays re-inspection), 100% sorting, discount, or reject. Do not release balance payment until the lot passes or the user accepts it in writing.
- Switching rules (tightened/reduced inspection) apply to a continuing series of lots. Mention them only when the user ships the same product repeatedly.

## Factory audit essentials (what QC firms check)
- Legal: business licence (营业执照) with USCC, scope covers the product, matches the company name on the invoice and bank account; export rights / customs registration.
- Capacity: lines, machines, headcount on site vs claimed, monthly output, subcontracting (ask directly and walk the floor).
- Quality system: incoming material inspection (IQC), in-process (IPQC), final (FQC/OQC), calibration records, defect records, corrective actions (CAPA), traceability.
- Social / ethical (BSCI, SMETA): working hours, wages, child labour, fire exits, dormitories.
- Red flags: audit only allowed at a "showroom", different address from licence, refuses unannounced audit, no records, all workers absent "on holiday".

## Writing a QC protocol for the user
Produce: product description and PO details → reference (golden sample, spec sheet, artwork) → inspection type and timing → standard, level, AQLs and computed sample sizes → defect list by class → on-site tests with method and sample size → packing/marking requirements per destination market → reporting requirements (photos of every defect, carton marks, seal number) → who pays re-inspection.

## Verification
When the user asks you to judge a report: recompute sample size and Ac/Re yourself, check that defect counts and classes are consistent with photos, and flag missing sections. If a figure in a report cannot be checked, say so instead of assuming it is right.
