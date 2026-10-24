# Cycle 1 (x3)

Three successive research passes and three chained simulate+report iterations for each of the seven foundational reports, then one Verification. Builds on `../Cycle-0-Baseline/` (never modified).

| Path | What |
|---|---|
| `SUMMARY.md` | one-page summary and gate |
| `FRAMEWORK.md` | reference to the governing framework (Cycle-0 copy, by hash) |
| `CHANGELOG.md` | what changed from Cycle 0 and why, incl. development disclosures |
| `INDEPENDENT_REVIEW_CHECKLIST.md` | what an independent reviewer should check |
| `Report-1-Body/` … `Report-7-Unified/` | REPORT.md, claims/, sources/, research/pass-1..3/, simulation/iter-1..3/, CHANGELOG.md |
| `Verification/` | VERIFICATION.md + raw outputs |
| `Provenance/` | SOURCE_REGISTER.csv, FETCH_LOG.jsonl, MANIFEST.sha256 |
| `tools/runner.py` | shared simulation runner (EXECUTION_RECORD writer) |

Reproduce all simulations: for each report, `cd Report-N-*/simulation && python sim_rN.py iter-1 && … iter-3` (Report 7 last; it reads the others' records and `../Cycle-0-Baseline`).

Integrity: no invented sources or results; Indeterminate is never Pass; implementation is not authorized by this research.
