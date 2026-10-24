# 625-intersection matrix (v1, placement from Cycle 1)

**Axes** (from `Research/README.md` §9.3–9.4, governing document G01):
- Alchemy (transformation mode): Body, Mind, Soul, Spirit, Consciousness Alchemy.
- Being (domain): Body, Mind, Soul, Spirit, Consciousness.
- Phase (Transformative Intelligence): Divergence, Insurgence, Allegiance, Convergence, Ascendence.
- Lens (ethical orientation): Truth, Integrity, Love, Justice, Wisdom.

5⁴ = 625 cells, each with ID `X-A<i>-B<j>-P<k>-L<m>` (the same IDs as Cycle 0's `intersections_625.csv`). Status for all cells: *Proposed — category only*. The grid identifies questions; it does not establish mechanisms (G01 §9.3).

## How claims and reports are placed
| Axis | Rule | Result |
|---|---|---|
| Being | Taken from the report: R1→Body, R2→Mind, R3→Soul, R4→Spirit, R5→Consciousness. R6 Earth and R7 Unified have no Being category | 104 claims placed; 38 are outside the Being axis |
| Lens | Provisional keyword rule `lens_rules.json` v1.0.1, applied to the claim wording (a claim may get 0–n lenses) | 73 placed; 69 Unassigned |
| Alchemy | **Not assigned**: undefined in G01 (§12 Q3) | all Unassigned |
| Phase | **Not assigned**: undefined in G01 (§12 Q4: fixed sequence vs recurring states unresolved) | all Unassigned |

Consequently `claims_placed_exactly` = 0 for all 625 cells. Each cell's flag comes from its Being × Lens projection:
- **EMPTY**: no claim in the projection (175 cells).
- **UNDER-RESEARCHED**: fewer than 3 claims, a threshold set before generation (175 cells).
- **UNPLACED**: the projection is populated, but Alchemy and Phase are undefined (275 cells).

So **no cell is fully researched**. That is the honest state of the grid until Alchemy and Phase are defined.

## Being × Lens projection (Cycle-1 claims; counts by label)
| Being \ Lens | Truth | Integrity | Love | Justice | Wisdom |
|---|---|---|---|---|---|
| Body | 1 (0E/1P/0PS/0H) *under* | 7 (5E/2P/0PS/0H) | 0 (0E/0P/0PS/0H) **EMPTY** | 0 (0E/0P/0PS/0H) **EMPTY** | 1 (1E/0P/0PS/0H) *under* |
| Mind | 12 (8E/4P/0PS/0H) | 3 (0E/1P/2PS/0H) | 1 (0E/1P/0PS/0H) *under* | 0 (0E/0P/0PS/0H) **EMPTY** | 3 (1E/2P/0PS/0H) |
| Soul | 1 (1E/0P/0PS/0H) *under* | 3 (1E/0P/2PS/0H) | 2 (2E/0P/0PS/0H) *under* | 3 (3E/0P/0PS/0H) | 3 (1E/0P/2PS/0H) |
| Spirit | 10 (7E/1P/1PS/1H) | 0 (0E/0P/0PS/0H) **EMPTY** | 3 (1E/0P/1PS/1H) | 1 (0E/0P/1PS/0H) *under* | 3 (0E/3P/0PS/0H) |
| Consciousness | 3 (2E/1P/0PS/0H) | 2 (1E/0P/1PS/0H) *under* | 0 (0E/0P/0PS/0H) **EMPTY** | 0 (0E/0P/0PS/0H) **EMPTY** | 0 (0E/0P/0PS/0H) **EMPTY** |

EMPTY projections: Body–Love, Body–Justice, Mind–Justice, Spirit–Integrity, Consciousness–Love, Consciousness–Justice, Consciousness–Wisdom. Under-researched (<3): Body–Truth, Body–Wisdom, Mind–Love, Soul–Truth, Soul–Love, Spirit–Justice, Consciousness–Integrity.

## Report placement
| Report | Being | Claims | Truth | Integrity | Love | Justice | Wisdom | Unassigned | Cells in 625 |
|---|---|---|---|---|---|---|---|---|---|
| R1 Body | Body | 20 | 1 | 7 | 0 | 0 | 1 | 12 | 125 |
| R2 Mind | Mind | 20 | 12 | 3 | 1 | 0 | 3 | 6 | 125 |
| R3 Soul | Soul | 23 | 1 | 3 | 2 | 3 | 3 | 13 | 125 |
| R4 Spirit | Spirit | 24 | 10 | 0 | 3 | 1 | 3 | 10 | 125 |
| R5 Consciousness | Consciousness | 17 | 3 | 2 | 0 | 0 | 0 | 13 | 125 |
| R6 Earth | outside Being axis | 28 | 5 | 12 | 1 | 1 | 0 | 12 | 0 |
| R7 Unified | outside Being axis | 10 | 3 | 5 | 1 | 0 | 2 | 3 | 0 |

Each Being report spans 125 cells (5 Alchemy × 5 Phase × 5 Lens). Earth and Unified sit outside the grid's Being axis. Their relation to the grid is carried by the link graph, not by the matrix.

## Known limits of the lens rule
It is lexical. It finds words, not meanings. Examples of mis-hits found in the spot-check:
- 'identity theory' (mind–body philosophy) → Integrity.
- 'integrity, stability' in Leopold's land ethic → Integrity, Love and Justice. Arguably right, but by word match.

Many claims match nothing, for example the Chinese hun/po soul description. Lens counts are a coverage aid, not a coding of meaning. A hand-coded, two-coder lens placement with agreement statistics is pre-registered for Cycle 2.

Files: `intersections_625.csv`, `being_x_lens_25.csv`, `claim_placement.csv`, `report_placement.csv`, `lens_rules.json`.
