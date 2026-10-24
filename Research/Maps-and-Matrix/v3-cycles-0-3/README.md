# Maps & Matrix — v3 (covers Cycles 0–3)

**Version:** v3 · **Covers:** Cycle 0 Baseline v2, Cycle 1 (x3), Cycle 2 (x6) and Cycle 3 (x9) (`Research/Cycles/Cycle-3-x9`, branch `research/cycle-3-x9`) · **Date:** 2026-10-24 · **Tooling:** `Research/tools` (gaia_tools 0.3.0; data model 1.2.0). v1 and v2 are kept unchanged.

| # | Deliverable | Files | Headline |
|---|---|---|---|
| 1 | Claim map | `claim_map/` | 635 rows: C0 100 (65 E / 14 P / 19 PS / 2 H), C1 142 (91 E / 28 P / 21 PS / 2 H), C2 177 (119 E / 35 P / 21 PS / 2 H), C3 216 (144 E / 49 P / 21 PS / 2 H) |
| 2 | 625-intersection matrix | `matrix/` | Placement from Cycle-3 claims. **0 claims placed exactly** (Alchemy and Phase undefined). Being × Lens: 15 of 25 populated, 9 under-researched, 1 empty (Body×Justice; v2 had 6 empty). New: `matrix/lens_two_method/` — keyword rule vs hand coding on 40 claims, mean κ 0.59 (same agent) |
| 3 | Link graph | `graph/` | GAIA + 7 reports; 7 motherthread edges (PS) and 27 typed links (3 new: L25 P, L26 H, L27 PS); no label changes in Cycle 3 |
| 4 | Cross-cycle change log | `changes/` | C2 → C3 claims: 39 new, 175 unchanged, 2 updated with label unchanged (full-text source added), 0 dropped. Links: 3 new, 24 re-assessed, 0 weakened |
| 5 | Data model + validation | `data-model/`, `validation/` | 635 claims, 474 source rows, 99 links, 143 execution records (incl. 9 superseded): **0 errors**, 84 warnings. Reruns identical: C0 7/7, C1 21/21, C2 42/42, C3 63/63 |

## Honest limits
- **Alchemy and Phase remain undefined**; every 625-cell row is a Being × Lens projection.
- **Lens placement is still the provisional keyword rule** (v1.0.1); 88 of 216 Cycle-3 claims match no lens. The two-method comparison was coded by the same agent who wrote the rule — not independent two-coder reliability. Per-lens κ: Integrity 0.50 (rule 9, hand 13), Justice 1.00 (rule 1, hand 1), Love 1.00 (rule 3, hand 3), Truth 0.44 (rule 15, hand 18), Wisdom 0.00 (rule 2, hand 0). Justice and Love rest on 1 and 3 positives.
- Filled cells can be shallow: Body×Love is filled by a social-relationships meta-analysis because 'social' and 'relationship' are Love keywords.
- Reports 6 and 7 have no Being category (56 claims outside the Being axis).
- 0 carried claims changed label or status from C2 to C3 (as from C1 to C2): diminishing returns on revising conclusions.
- `rerun_C0/C1/C2.json` are copied from v2 (those trees are unchanged); `rerun_C3.json` is new. `claim_source_C*.json` were regenerated with gaia_tools 0.3.0.

## Reproduce
```
cd Research/tools && pip install -r requirements.txt
python -m gaia_tools.maps .. ../Maps-and-Matrix/v3-cycles-0-3 --version-label "v3 - covers Cycles 0-3"
python -m gaia_tools.validate .. --out /tmp/schema_validation.json
python -m gaia_tools.claimsource .. C3 --snapshots <dir of source snapshots>
python -m gaia_tools.rerun .. C3
python -m pytest -q tests
```
`MANIFEST.sha256` lists the SHA-256 of every file in this version.
