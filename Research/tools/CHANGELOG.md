# gaia_tools change log

## 0.2.0 — data model 1.1.0 (Cycle 2, 2026-10-24)
- Schemas: source/claim-source IDs allow the Cycle-2 prefix `W`; check IDs may contain '.' (e.g. `MR_0.05`). Both found as validation errors on the first Cycle-2 run (21 V2 errors for dotted IDs); fixed in the schema, no data changed.
- `data.lookup_sim`: SIM citations resolve against the cycle named in the SIM id (`SIM-Rk-C<n>`), so carried claims citing earlier runs resolve; the `C0:` prefix still works. Previously carried `SIM-R?-C1` citations in Cycle 2 were unresolved.
- `claimsource.parse_phrases`: splits verification phrases on ' || ' (0.1.0 split on ';', a bug). `phrase_found`: phrases are regular expressions (as in each cycle's live verification), with a literal fallback for invalid patterns.
- `maps`: link pressure also includes Report-7 `strict_rule` downgrades.
- Tests: `tests/test_units_v020.py` (versions, W ids, dotted check ids, cross-cycle lookup, phrase parsing/regex) and an optional corpus phrase test (`GAIA_SNAPSHOTS`).

## 0.1.0 — data model 1.0.0 (Maps & Matrix v1, 2026-10-24)
- Initial package: validate, rerun, claimsource, maps, data; 11 tests.
