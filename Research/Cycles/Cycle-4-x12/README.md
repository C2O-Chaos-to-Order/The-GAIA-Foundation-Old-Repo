# Cycle 4 (x12)

Twelve successive research passes and twelve chained simulate+report iterations for each of the seven foundational reports, then one Verification. Builds on `../Cycle-0-Baseline/` … `../Cycle-3-x9/` (none modified).

| Path | What |
|---|---|
| `SUMMARY.md` | one-page summary and gate |
| `FRAMEWORK.md` | reference to the governing framework + rules in force |
| `CHANGELOG.md` | what changed from Cycle 3 and why, incl. development disclosures |
| `INDEPENDENT_REVIEW_CHECKLIST.md` | what an independent reviewer should check |
| `Report-1-Body/` … `Report-7-Unified/` | REPORT.md, claims/, sources/, research/pass-1..12/, simulation/iter-1..12/, CHANGELOG.md |
| `Verification/` | VERIFICATION.md + raw outputs |
| `Provenance/` | SOURCE_REGISTER.csv, SEARCH_LOG.jsonl, FETCH_LOG.jsonl, MANIFEST.sha256 |
| `tools/runner.py` | shared simulation runner (byte-identical to Cycles 1–3) |

Reproduce all simulations: `cd Research/tools && python -m gaia_tools.rerun .. C4` (or per report `python sim_rN.py iter-1` … `iter-12`; Report 7 last, it reads the other reports and Cycle 3). Maps for Cycles 0–4: `../../Maps-and-Matrix/v4-cycles-0-4/`.

Integrity: no invented sources or results; Indeterminate is never Pass; implementation is not authorized by this research.
