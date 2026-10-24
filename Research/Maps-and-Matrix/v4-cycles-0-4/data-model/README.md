# Data model 1.3.0 (JSON Schema draft 2020-12)

Frozen copy of `Research/tools/gaia_tools/schemas/` at data model 1.3.0. Change from 1.2.0 (v3): source and claim-source ID pattern allows the Cycle-4 prefix **Y** (`^[GSTUVWXY][0-9]{2}[a-z]?$`).

| Instances validated | C0 | C1 | C2 | C3 | C4 |
|---|---|---|---|---|---|
| claims | 100 | 142 | 177 | 216 | 239 |
| sources | 78 | 115 | 130 | 151 | 157 |
| links | 24 | 24 | 24 | 27 | 28 |
| execution records | 8 | 21 | 42 | 72 | 84 |

**0 errors**, 85 warnings:

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
| C4 | Q3 | 1 |

## Claim-source checks (`../validation/claim_source_C*.json`, offline, with local snapshots)
- C0: K-resolve {'Pass': 100}; K-access {'n/a': 100}; K-sim {'n/a': 87, 'Pass': 13}; K-phrase {'Pass': 81, 'n/a': 19}.
- C1: K-resolve {'Pass': 142}; K-access {'Pass': 67, 'n/a': 75}; K-sim {'n/a': 109, 'Pass': 33}; K-phrase {'Pass': 103, 'n/a': 39}.
- C2: K-resolve {'Pass': 177}; K-access {'Pass': 75, 'n/a': 102}; K-sim {'n/a': 124, 'Pass': 53}; K-phrase {'Pass': 118, 'n/a': 59}.
- C3: K-resolve {'Pass': 216}; K-access {'Pass': 81, 'n/a': 135}; K-sim {'n/a': 144, 'Pass': 72}; K-phrase {'Pass': 138, 'n/a': 78}.
- C4: K-resolve {'Pass': 239}; K-access {'Pass': 84, 'n/a': 155}; K-sim {'n/a': 150, 'Pass': 89}; K-phrase {'Pass': 144, 'n/a': 95}.
