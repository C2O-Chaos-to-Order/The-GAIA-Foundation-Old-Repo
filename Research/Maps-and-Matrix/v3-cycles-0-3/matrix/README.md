# 625-intersection matrix (v3, placement from Cycle 3)

Axes, cell IDs and placement rules as in v1 (`../../v1-cycles-0-1/matrix/README.md`): Being from the report, Lens from the provisional keyword rule (`lens_rules.json` v1.0.1), Alchemy and Phase **not assigned**. `claims_placed_exactly` = 0 for all 625 cells.

Cell flags: EMPTY 25, UNDER-RESEARCHED 225, UNPLACED (projection populated) 375. No cell is fully researched.

## Being × Lens projection (Cycle-3 claims)
| Being \ Lens | Truth | Integrity | Love | Justice | Wisdom |
|---|---|---|---|---|---|
| Body | 6 (4E/2P/0PS/0H) | 9 (6E/3P/0PS/0H) | 1 (1E/0P/0PS/0H) *under* | 0 (0E/0P/0PS/0H) **EMPTY** | 2 (2E/0P/0PS/0H) *under* |
| Mind | 18 (12E/6P/0PS/0H) | 4 (0E/2P/2PS/0H) | 3 (1E/2P/0PS/0H) | 1 (1E/0P/0PS/0H) *under* | 3 (1E/2P/0PS/0H) |
| Soul | 3 (3E/0P/0PS/0H) | 3 (1E/0P/2PS/0H) | 2 (2E/0P/0PS/0H) *under* | 4 (4E/0P/0PS/0H) | 4 (2E/0P/2PS/0H) |
| Spirit | 18 (15E/1P/1PS/1H) | 1 (1E/0P/0PS/0H) *under* | 6 (3E/1P/1PS/1H) | 1 (0E/0P/1PS/0H) *under* | 3 (0E/3P/0PS/0H) |
| Consciousness | 13 (9E/4P/0PS/0H) | 5 (3E/1P/1PS/0H) | 1 (0E/1P/0PS/0H) *under* | 1 (0E/1P/0PS/0H) *under* | 1 (1E/0P/0PS/0H) *under* |

Cells EMPTY in v2 and populated now (SIM-R7-C3 iteration 6): BodyxLove, MindxJustice, ConsciousnessxLove, ConsciousnessxJustice, ConsciousnessxWisdom; still empty: BodyxJustice. Each new cell rests on one Cycle-3 claim (under-researched).

## Two-method lens placement (`lens_two_method/`)
Seeded sample of 40 claims (seed 20261025) from the 212-claim ledger; hand-coded with `LENS_CODEBOOK.md` before SIM-R7-C3 iteration 7 compared it with the keyword rule. Mean Cohen's κ 0.59; per lens in `agreement.json`. Same agent for both; an independent coder is still needed.

## Report placement
| Report | Being | Claims | Truth | Integrity | Love | Justice | Wisdom | Unassigned | Cells in 625 |
|---|---|---|---|---|---|---|---|---|---|
| R1 Body | Body | 34 | 6 | 9 | 1 | 0 | 2 | 19 | 125 |
| R2 Mind | Mind | 28 | 18 | 4 | 3 | 1 | 3 | 8 | 125 |
| R3 Soul | Soul | 31 | 3 | 3 | 2 | 4 | 4 | 17 | 125 |
| R4 Spirit | Spirit | 35 | 18 | 1 | 6 | 1 | 3 | 12 | 125 |
| R5 Consciousness | Consciousness | 32 | 13 | 5 | 1 | 1 | 1 | 15 | 125 |
| R6 Earth | outside Being axis | 39 | 11 | 19 | 3 | 1 | 0 | 14 | 0 |
| R7 Unified | outside Being axis | 17 | 7 | 7 | 2 | 1 | 6 | 3 | 0 |

Lens counts are a lexical coverage aid, not a coding of meaning; 88 of 216 claims are Unassigned.
