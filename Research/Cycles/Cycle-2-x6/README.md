# Cycle 2 (x6)

Six successive research passes and six chained simulate+report iterations for each of the seven foundational reports, then one Verification. Builds on `../Cycle-0-Baseline/` and `../Cycle-1-x3/` (neither modified).

| Path | What |
|---|---|
| `SUMMARY.md` | one-page summary and gate |
| `FRAMEWORK.md` | reference to the governing framework + rules in force |
| `CHANGELOG.md` | what changed from Cycle 1 and why, incl. development disclosures |
| `INDEPENDENT_REVIEW_CHECKLIST.md` | what an independent reviewer should check |
| `Report-1-Body/` … `Report-7-Unified/` | REPORT.md, claims/, sources/, research/pass-1..6/, simulation/iter-1..6/, CHANGELOG.md |
| `Verification/` | VERIFICATION.md + raw outputs |
| `Provenance/` | SOURCE_REGISTER.csv, SEARCH_LOG.jsonl (new), FETCH_LOG.jsonl, MANIFEST.sha256 |
| `tools/runner.py` | shared simulation runner (byte-identical to Cycle 1) |

Reproduce all simulations: `cd Research/tools && python -m gaia_tools.rerun .. C2` (or per report `python sim_rN.py iter-1` … `iter-6`; Report 7 last, it reads the other reports and Cycles 0–1). Maps for Cycles 0–2: `../../Maps-and-Matrix/v2-cycles-0-2/`.

Integrity: no invented sources or results; Indeterminate is never Pass; implementation is not authorized by this research.
