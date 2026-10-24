# gaia_tools change log

## 0.5.1 — data model 1.4.0 (Track Cycle B, 2026-10-24)
- `maps_all`: track claims are compared across track cycles on their ID stem (`TA-SOUL-01` -> `TB-SOUL-01`), so carried claims are classified as carried/changed instead of 'new' + 'dropped'. No schema change.
- Tests: `tests/test_tracks_v051.py` (stem matching; carried Cycle A claims are not reported as dropped in Cycle B). `test_tracks_v050.py`: exact-version assertion relaxed to ">= 0.5.0".

## 0.5.0 — data model 1.4.0 (Soul/Spirit/Subconscious/Consciousness track, 2026-10-24)
- New `gaia_tools.tracks`: loader, `validate` (E1–E9, W1–W2), `claimsource` (K-resolve, K-access, K-sim, K-phrase) and `rerun` for `Research/Tracks/<track>/Cycle-<L>-x<N>/`. Track SIM citations: `SIM-<TOPIC>-<L>/iter-k#check`.
- New `gaia_tools.maps_all`: runs `maps.build` unchanged for the main cycles, then extends every artefact with the Master Report and all track cycles (claim map rows, matrix placement and the n_main/n_mr/n_track split, graph nodes MR + four topics with GAIA motherthread edges, typed track links TL-*, unlabelled structure edges, change log, simulation index).
- New schemas `track_claim.schema.json` and `track_execution_record.schema.json` (track run layout: SPEC.md with params block + EXECUTION_RECORD.json with embedded results and spec/params/results hashes). Main-cycle schemas are unchanged.
- Tests: `tests/test_tracks_v050.py` (versions, SIM-ref parsing, schema accept/reject, corpus schema conformance, validate 0 errors, claimsource no Fail, SPEC tampering detected (E8), unstated 'not supported' detected (E6), maps_all deterministic and complete). `test_units_v040.py`: exact-version assertion relaxed to ">= 0.4.0".

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
