# Maps & Matrix — v7 (covers Cycles 0-4, Master Report, Track Cycles A-C (x3, x6, x9))

**Version:** v7 · **Date:** 2026-10-24 · **Tooling:** `Research/tools` gaia_tools 0.5.1, data model 1.4.0 (`python -m gaia_tools.maps_all`). Earlier versions (v1–v6) are kept unchanged.

The owner asked that the Soul, Spirit, Subconscious and Consciousness track be **mapped and matrixed to all current work**. This version therefore covers the five main cycles, the Master Report and every track cycle to date in one set of artefacts.

| # | Deliverable | Files | Headline |
|---|---|---|---|
| 1 | Claim map | `claim_map/` | 1124 rows: C0 100, C1 142, C2 177, C3 216, C4 239, MR 36, TA 37, TB 72, TC 105 |
| 2 | 625-intersection matrix | `matrix/` | Placement = Cycle-4 claims + Master Report + Track Cycle C claims. Being × Lens: 22 populated, 2 under-researched, 1 empty (Body×Justice). Alchemy and Phase remain undefined |
| 3 | Link graph | `graph/` | GAIA + 7 reports + Master Report + 4 track topics; 12 motherthread edges (PS), 28 main-cycle links, 26 track links (E 13 / P 6 / PS 4 / H 3); 12 organisational structure edges (unlabelled) |
| 4 | Cross-cycle change log | `changes/` | Track Cycle C claims: {'unchanged': 70, 'updated (label unchanged)': 2, 'new': 33}; track links: {'re-assessed (label unchanged)': 18, 'new': 8} |
| 5 | Data model + validation | `data-model/`, `validation/` | Track validation 0 errors; main-cycle validation unchanged since v4 (not duplicated) |

## Matrix movement since the previous version
- Mind×Justice: UNDER-RESEARCHED → populated
- Consciousness×Justice: UNDER-RESEARCHED → populated

Still under-researched: Body×Love, Body×Wisdom.

## Honest limits
- Alchemy and Phase are still undefined, so every 625-cell row is a Being × Lens projection.
- Lens placement uses the provisional keyword rule (v1.0.1), unchanged. It is a navigation aid, not a classification.
- Subconscious is placed on Being = Mind by a pre-declared rule (the axis has no Subconscious category).
- Track links (TL-*) are typed and labelled by the same agent that wrote the claims, with no independent check (gate INDETERMINATE).

## Reproduce
```
cd Research/tools && pip install -r requirements.txt
python -m gaia_tools.maps_all .. ../Maps-and-Matrix/v7-cycles-0-4-mr-track-abc --version-label "covers Cycles 0-4, Master Report, Track Cycles A-C (x3, x6, x9)"
python -m gaia_tools.tracks validate ..
python -m gaia_tools.tracks rerun .. TC
python -m pytest -q tests
```
`MANIFEST.sha256` lists the SHA-256 of every file in this version.
