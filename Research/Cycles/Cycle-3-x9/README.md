# Cycle 3 (x9)

Nine successive research passes and nine chained simulate+report iterations for each of the seven foundational reports, then one Verification. Builds on `../Cycle-0-Baseline/`, `../Cycle-1-x3/` and `../Cycle-2-x6/` (none modified).

| Path | What |
|---|---|
| `SUMMARY.md` | one-page summary and gate |
| `FRAMEWORK.md` | reference to the governing framework + rules in force |
| `CHANGELOG.md` | what changed from Cycle 2 and why, incl. development disclosures |
| `INDEPENDENT_REVIEW_CHECKLIST.md` | what an independent reviewer should check |
| `Report-1-Body/` … `Report-7-Unified/` | REPORT.md, claims/, sources/, research/pass-1..9/, simulation/iter-1..9/, CHANGELOG.md |
| `Verification/` | VERIFICATION.md + raw outputs |
| `Provenance/` | SOURCE_REGISTER.csv, SEARCH_LOG.jsonl, FETCH_LOG.jsonl, MANIFEST.sha256 |
| `tools/runner.py` | shared simulation runner (byte-identical to Cycles 1–2) |

Reproduce all simulations: `cd Research/tools && python -m gaia_tools.rerun .. C3` (or per report `python sim_rN.py iter-1` … `iter-9`; Report 7 last, it reads the other reports and Cycles 1–2). Maps for Cycles 0–3: `../../Maps-and-Matrix/v3-cycles-0-3/`.

Integrity: no invented sources or results; Indeterminate is never Pass; implementation is not authorized by this research.
