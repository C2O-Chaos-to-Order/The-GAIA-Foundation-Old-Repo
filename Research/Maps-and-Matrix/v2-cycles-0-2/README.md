# Maps & Matrix — v2 (covers Cycles 0–2)

**Version:** v2 · **Covers:** Cycle 0 Baseline v2, Cycle 1 (x3) and Cycle 2 (x6) (`Research/Cycles/Cycle-2-x6`, branch `research/cycle-2-x6`) · **Date:** 2026-10-24 · **Tooling:** `Research/tools` (gaia_tools 0.2.0; data model 1.1.0). v1 (`../v1-cycles-0-1/`) is kept unchanged.

| # | Deliverable | Files | Headline |
|---|---|---|---|
| 1 | Claim map | `claim_map/` | 419 rows: C0 100 (65 E / 14 P / 19 PS / 2 H), C1 142 (91 E / 28 P / 21 PS / 2 H), C2 177 (119 E / 35 P / 21 PS / 2 H) |
| 2 | 625-intersection matrix | `matrix/` | Placement from Cycle-2 claims. **0 claims placed exactly** (Alchemy and Phase undefined). Being × Lens: 14 of 25 populated, 5 under-researched, 6 empty |
| 3 | Link graph | `graph/` | GAIA + 7 reports; 7 motherthread edges (PS) and 24 typed links; 3 links downgraded E → P by the strict rule (procedural) |
| 4 | Cross-cycle change log | `changes/` | C1 → C2 claims: 35 new, 142 label/status unchanged, 0 dropped. Links: 3 weakened (L04, L08, L16), 0 dropped |
| 5 | Data model + validation | `data-model/`, `validation/` | 419 claims, 323 source rows, 72 links, 71 execution records: **0 errors**, 83 warnings. Reruns identical: C0 7/7, C1 21/21, C2 42/42 |

## Honest limits
- **Alchemy and Phase remain undefined** in the governing documents; no claim is assigned to them, so every 625-cell row is a Being × Lens projection.
- **Lens placement is still the provisional keyword rule** (v1.0.1); 81 of 177 Cycle-2 claims match no lens. The hand-coded two-coder lens placement pre-registered for Cycle 2 was **not done** in Cycle 2 (time was spent on the R3 re-coding); it is carried to Cycle 3.
- Reports 6 and 7 have no Being category (47 claims outside the Being axis).
- The C1 → C2 change log shows that no carried claim changed label or status: a diminishing-returns signal.
- `rerun_C0.json` and `rerun_C1.json` are copied from v1 (the C0/C1 trees are unchanged; their files are byte-identical); `rerun_C2.json` is new.

## Reproduce
```
cd Research/tools && pip install -r requirements.txt
python -m gaia_tools.maps .. ../Maps-and-Matrix/v2-cycles-0-2 --version-label "v2 - covers Cycles 0-2"
python -m gaia_tools.validate .. --out /tmp/schema_validation.json
python -m gaia_tools.claimsource .. C2 --snapshots <dir of source snapshots>
python -m gaia_tools.rerun .. C2
python -m pytest -q tests
```
`MANIFEST.sha256` lists the SHA-256 of every file in this version.
