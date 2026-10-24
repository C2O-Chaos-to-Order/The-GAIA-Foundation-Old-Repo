# Maps & Matrix — v4 (covers Cycles 0–4)

**Version:** v4 · **Covers:** Cycle 0 Baseline v2 and Cycles 1 (x3), 2 (x6), 3 (x9), 4 (x12) (`Research/Cycles/Cycle-4-x12`, branch `research/cycle-4-x12`) · **Date:** 2026-10-24 · **Tooling:** `Research/tools` (gaia_tools 0.4.0; data model 1.3.0). v1–v3 are kept unchanged.

| # | Deliverable | Files | Headline |
|---|---|---|---|
| 1 | Claim map | `claim_map/` | 874 rows: C0 100, C1 142, C2 177, C3 216, C4 239 (164 E / 52 P / 21 PS / 2 H) |
| 2 | 625-intersection matrix | `matrix/` | Placement from Cycle-4 claims. 0 claims placed exactly (Alchemy and Phase undefined). Being × Lens: 15 of 25 populated, 9 under-researched, 1 empty (Body×Justice, still empty after Cycle 4) |
| 3 | Link graph | `graph/` | GAIA + 7 reports; 7 motherthread edges (PS) and 28 typed links (1 new: L28 P); no label changed in Cycle 4 |
| 4 | Cross-cycle change log | `changes/` | C3 → C4 claims: 23 new, 216 unchanged, 0 updated with label unchanged, 0 dropped; links: 1 new |
| 5 | Data model + validation | `data-model/`, `validation/` | 0 errors over C0–C4; reruns C0 7/7, C1 21/21, C2 42/42, C3 63/63, C4 84/84 identical |

## Honest limits
- **Alchemy and Phase remain undefined**; every 625-cell row is a Being × Lens projection.
- **Lens placement is still the provisional keyword rule** (v1.0.1); 94 of 239 Cycle-4 claims match no lens. No new two-method comparison was made in Cycle 4 (v3's same-agent comparison, κ 0.59, is in `../v3-cycles-0-3/matrix/lens_two_method/`).
- Reports 6 and 7 have no Being category (61 claims outside the Being axis).
- **Diminishing returns:** 0 carried claims changed label or status from C3 to C4 (as from C1 to C2 and C2 to C3).
- `rerun_C0`–`rerun_C3.json` are copied from v3 (those trees are unchanged); `rerun_C4.json` is new; `claim_source_C*.json` regenerated with gaia_tools 0.4.0.

## Reproduce
```
cd Research/tools && pip install -r requirements.txt
python -m gaia_tools.maps .. ../Maps-and-Matrix/v4-cycles-0-4 --version-label "covers Cycles 0-4"
python -m gaia_tools.validate .. --out /tmp/schema_validation.json
python -m gaia_tools.claimsource .. C4 --snapshots <dir of source snapshots>
python -m gaia_tools.rerun .. C4
python -m pytest -q tests
```
`MANIFEST.sha256` lists the SHA-256 of every file in this version.
