# Maps & Matrix — v6 (covers Cycles 0-4, Master Report, Track Cycles A-B (x3, x6))

**Version:** v6 · **Date:** 2026-10-24 · **Tooling:** `Research/tools` gaia_tools 0.5.1, data model 1.4.0 (`python -m gaia_tools.maps_all`). Earlier versions (v1–v5) are kept unchanged.

The owner asked that the Soul, Spirit, Subconscious and Consciousness track be **mapped and matrixed to all current work**. This version therefore covers the five main cycles, the Master Report and every track cycle to date in one set of artefacts.

| # | Deliverable | Files | Headline |
|---|---|---|---|
| 1 | Claim map | `claim_map/` | 1019 rows: C0 100, C1 142, C2 177, C3 216, C4 239, MR 36, TA 37, TB 72 |
| 2 | 625-intersection matrix | `matrix/` | Placement = Cycle-4 claims + Master Report + Track Cycle B claims. Being × Lens: 20 populated, 4 under-researched, 1 empty (Body×Justice). Alchemy and Phase remain undefined |
| 3 | Link graph | `graph/` | GAIA + 7 reports + Master Report + 4 track topics; 12 motherthread edges (PS), 28 main-cycle links, 18 track links (E 8 / P 5 / PS 3 / H 2); 12 organisational structure edges (unlabelled) |
| 4 | Cross-cycle change log | `changes/` | Track Cycle B claims: {'unchanged': 34, 'updated (label unchanged)': 3, 'new': 35}; track links: {'re-assessed (label unchanged)': 11, 'new': 7} |
| 5 | Data model + validation | `data-model/`, `validation/` | Track validation 0 errors; main-cycle validation unchanged since v4 (not duplicated) |

## Matrix movement since the previous version
- Spirit×Justice: UNDER-RESEARCHED → populated
- Consciousness×Love: UNDER-RESEARCHED → populated
- Consciousness×Wisdom: UNDER-RESEARCHED → populated

Still under-researched: Body×Love, Body×Wisdom, Mind×Justice, Consciousness×Justice.

## Honest limits
- Alchemy and Phase are still undefined, so every 625-cell row is a Being × Lens projection.
- Lens placement uses the provisional keyword rule (v1.0.1), unchanged. It is a navigation aid, not a classification.
- Subconscious is placed on Being = Mind by a pre-declared rule (the axis has no Subconscious category).
- Track links (TL-*) are typed and labelled by the same agent that wrote the claims, with no independent check (gate INDETERMINATE).

## Reproduce
```
cd Research/tools && pip install -r requirements.txt
python -m gaia_tools.maps_all .. ../Maps-and-Matrix/v6-cycles-0-4-mr-track-ab --version-label "covers Cycles 0-4, Master Report, Track Cycles A-B (x3, x6)"
python -m gaia_tools.tracks validate ..
python -m gaia_tools.tracks rerun .. TB
python -m pytest -q tests
```
`MANIFEST.sha256` lists the SHA-256 of every file in this version.
