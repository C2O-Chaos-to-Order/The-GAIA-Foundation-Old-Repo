# gaia_tools change log

## 0.4.0 — data model 1.3.0 (Cycle 4, 2026-10-24)
- Schemas: source and claim-source IDs allow the Cycle-4 prefix `Y` (Y01-Y08). No other schema change.
- Tests: `tests/test_units_v040.py` (versions, Y ids, C4 SIM ids). The exact-version assertion in `test_units_v030.py` was relaxed to ">= 0.3.0", and the "Y01 is invalid" assertions in `test_units_v020.py` and `test_units_v030.py` were replaced by "Z01 is invalid", because both are intentionally changed in 0.4.0.

## 0.3.0 — data model 1.2.0 (Cycle 3, 2026-10-24)
- Schemas: source and claim-source IDs allow the Cycle-3 prefix `X`; link registers may carry `c<n>_strict_rule` and `c<n>_essential_rule` columns (Report 7's rule checks, Cycle 3).
- `data.is_archived` / `data.simulations`: runs under a `superseded-run-N/` folder are indexed as archived (kept for the record, not re-run, not citable), like Cycle 0's `archive/`; their script is looked up one level up (`superseded-run-N/sim_*.py`). Used for SIM-R4-C3 run 1, superseded after a coding error.
- Tests: `tests/test_units_v030.py` (versions, X ids, link rule columns, archived/superseded indexing, citation index excludes superseded runs). `tests/test_units_v020.py`: the exact-version assertion was relaxed to ">= 0.2.0" and its "X01 is invalid" assertion replaced by "Y01 is invalid", because both are intentionally changed in 0.3.0.
- First run on Cycle 3: `claimsource` K-sim flagged two claims (C3-R1-06 cited a not-supported check without saying so; C3-R4-03 cited a failed validation check while Established). Both ledger rows were corrected before verification (see `Cycles/Cycle-3-x9/CHANGELOG.md`); the tool was not changed.

## 0.2.0 — data model 1.1.0 (Cycle 2, 2026-10-24)
- Schemas: source/claim-source IDs allow the Cycle-2 prefix `W`; check IDs may contain '.' (e.g. `MR_0.05`). Both found as validation errors on the first Cycle-2 run (21 V2 errors for dotted IDs); fixed in the schema, no data changed.
- `data.lookup_sim`: SIM citations resolve against the cycle named in the SIM id (`SIM-Rk-C<n>`), so carried claims citing earlier runs resolve; the `C0:` prefix still works. Previously carried `SIM-R?-C1` citations in Cycle 2 were unresolved.
- `claimsource.parse_phrases`: splits verification phrases on ' || ' (0.1.0 split on ';', a bug). `phrase_found`: phrases are regular expressions (as in each cycle's live verification), with a literal fallback for invalid patterns.
- `maps`: link pressure also includes Report-7 `strict_rule` downgrades.
- Tests: `tests/test_units_v020.py` (versions, W ids, dotted check ids, cross-cycle lookup, phrase parsing/regex) and an optional corpus phrase test (`GAIA_SNAPSHOTS`).

## 0.1.0 — data model 1.0.0 (Maps & Matrix v1, 2026-10-24)
- Initial package: validate, rerun, claimsource, maps, data; 11 tests.
