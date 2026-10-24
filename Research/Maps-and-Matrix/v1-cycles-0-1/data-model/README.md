# Data model 1.0.0 (JSON Schema draft 2020-12)

| Schema | Describes | Instances validated (C0 + C1) |
|---|---|---|
| `schemas/claim.schema.json` | a claims.csv row (source_ids and cross_links split on ';') | 100 + 142 |
| `schemas/source.schema.json` | a SOURCE_REGISTER.csv row (each report's sources.csv must be an exact subset) | 78 + 115 |
| `schemas/link.schema.json` | a link_register.csv row (basis split on ';'; per-cycle columns `c<N>_…`) | 24 + 24 |
| `schemas/simulation.schema.json` | one executed run in `simulations_index.json` | 8 + 21 |
| `schemas/execution_record.schema.json` | EXECUTION_RECORD.json (C0 form with embedded params; C1 iteration form with typed checks) | 8 + 21 |

These files are a frozen copy of `Research/tools/gaia_tools/schemas/` at data model 1.0.0. Later versions of the maps carry their own copy.

## Validation result (`../validation/schema_validation.json`)
**0 errors.** Besides the schemas, cross-file rules were checked:
- V1: unique IDs and report folder.
- V2: literature IDs are in the register.
- V3: every SIM citation resolves to a pre-registered check, with `C0:` resolving to Cycle 0.
- V4: link basis claims exist.
- V5: report sources.csv rows equal the register rows.
- V6: output and params hashes match the files on disk.

82 quality warnings (reported, not errors):

| Cycle | Warning | n |
|---|---|---|
| C0 | Q1 | 40 |
| C0 | Q2 | 2 |
| C0 | Q3 | 1 |
| C0 | Q4 | 1 |
| C1 | Q1 | 37 |
| C1 | Q3 | 1 |

- **Q1**: `counterevidence_limits` is empty. 40 Cycle-0 claims are affected, and 37 of them are carried into Cycle 1 unchanged. Cycle-0 files may not be modified, so the Cycle-1 carry-overs will be filled in Cycle 2: C0v2-R1-02, C0v2-R1-04, C0v2-R1-07, C0v2-R2-06, C0v2-R2-07, C0v2-R2-08, C0v2-R2-09, C0v2-R3-01, C0v2-R3-03, C0v2-R3-07, C0v2-R3-09, C0v2-R3-10, C0v2-R3-13, C0v2-R3-14, C0v2-R3-15, C0v2-R3-16, C0v2-R3-18, C0v2-R4-01, C0v2-R4-03, C0v2-R4-04, C0v2-R4-05, C0v2-R4-07, C0v2-R4-15, C0v2-R5-01, C0v2-R5-03, C0v2-R5-08, C0v2-R5-12, C0v2-R6-06, C0v2-R6-09, C0v2-R6-10, C0v2-R6-11, C0v2-R6-12, C0v2-R6-13, C0v2-R6-19, C0v2-R7-04, C0v2-R7-06, C0v2-R7-07.
- **Q2**: the access mode of S19 and S27 in Cycle 0 is outside the controlled prefixes. This was already normalized in the Cycle-1 register.
- **Q3**: L24's rejection criterion is '—'. L24 is a Philosophical/Spiritual 'unresolved question' link, and each open item has its own test in its source report.
- **Q4**: the Cycle-0 archived run (R4 archive_v1) records `outputs/results.json`, which was renamed to `results_v1.json` on archiving. The SHA-256 matches.

## Disclosed adjustments after the first validation run
The first run reported 98 errors. They were resolved as follows, without changing any data:
1. A schema bug: check IDs and SIM citations containing '_' (e.g. `V_Chen2021_mortality_pooled`, `A_bounded_5`) were rejected. The pattern now allows '_'.
2. Empty `counterevidence_limits` became warning Q1 instead of an error.
3. A non-controlled `access_mode` became warning Q2.
4. A dash rejection criterion became warning Q3.
5. A missing archived output became warning Q4, but only when a file with the identical SHA-256 exists in the archive folder.

Points 2–5 relax strictness. They are reported, not hidden, and they would have required editing Cycle-0 files, which the rules forbid.

## Other checks (`../validation/`)
- `claim_source_C0.json` / `claim_source_C1.json` (gaia_tools.claimsource, offline):
  - K-resolve: Pass 100/100 (C0) and 142/142 (C1).
  - K-access (C1 only; Established literature claims need full text): Pass 67, 0 Fail.
  - K-sim: Pass 13 (C0) and 33 (C1), 0 Fail.
  - Live phrase checks are not repeated here. They are in each cycle's own Verification folder.
- `rerun_C0.json` / `rerun_C1.json` (gaia_tools.rerun, fresh copy): C0 7/7 and C1 21/21 runs re-executed with exit 0. Outputs and check results are byte-identical: all_identical = True / True.
