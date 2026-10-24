# Data model 1.2.0 (JSON Schema draft 2020-12)

Frozen copy of `Research/tools/gaia_tools/schemas/` at data model 1.2.0. Changes from 1.1.0 (v2):
1. Source and claim-source ID pattern allows the Cycle-3 prefix **X** (`^[GSTUVWX][0-9]{2}[a-z]?$`).
2. Link registers may carry `c<n>_strict_rule` and `c<n>_essential_rule` columns.
3. Runs under `superseded-run-N/` are indexed as archived (not re-run, not citable), like Cycle 0's `archive/`.

| Instances validated | C0 | C1 | C2 | C3 |
|---|---|---|---|---|
| claims | 100 | 142 | 177 | 216 |
| sources | 78 | 115 | 130 | 151 |
| links | 24 | 24 | 24 | 27 |
| execution records | 8 | 21 | 42 | 72 |

**0 errors**, 84 warnings:

| Cycle | Warning | n |
|---|---|---|
| C0 | Q1 | 40 |
| C0 | Q2 | 2 |
| C0 | Q3 | 1 |
| C0 | Q4 | 1 |
| C1 | Q1 | 37 |
| C1 | Q3 | 1 |
| C2 | Q3 | 1 |
| C3 | Q3 | 1 |

C3's single Q3 is L24 (carried Philosophical/Spiritual link; placeholder rejection criterion). C3 has no empty limits field (Q1 = 0).

## Claim-source checks (`../validation/claim_source_C*.json`, offline, with local snapshots)
- C0: K-resolve {'Pass': 100}; K-access {'n/a': 100}; K-sim {'n/a': 87, 'Pass': 13}; K-phrase {'Pass': 81, 'n/a': 19}.
- C1: K-resolve {'Pass': 142}; K-access {'Pass': 67, 'n/a': 75}; K-sim {'n/a': 109, 'Pass': 33}; K-phrase {'Pass': 103, 'n/a': 39}.
- C2: K-resolve {'Pass': 177}; K-access {'Pass': 75, 'n/a': 102}; K-sim {'n/a': 124, 'Pass': 53}; K-phrase {'Pass': 118, 'n/a': 59}.
- C3: K-resolve {'Pass': 216}; K-access {'Pass': 81, 'n/a': 135}; K-sim {'n/a': 144, 'Pass': 72}; K-phrase {'Pass': 138, 'n/a': 78}.

On its first Cycle-3 run, K-sim flagged two claims (C3-R1-06, C3-R4-03); the ledger was corrected before these outputs were made (see `Research/Cycles/Cycle-3-x9/CHANGELOG.md`).
