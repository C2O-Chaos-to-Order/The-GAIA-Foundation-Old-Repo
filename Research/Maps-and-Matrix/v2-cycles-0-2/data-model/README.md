# Data model 1.1.0 (JSON Schema draft 2020-12)

Frozen copy of `Research/tools/gaia_tools/schemas/` at data model 1.1.0. Changes from 1.0.0 (v1):
1. Source and claim-source ID pattern allows the Cycle-2 prefix **W** (`^[GSTUVW][0-9]{2}[a-z]?$`).
2. Check IDs may contain '.' (e.g. `MR_0.05`), in SIM citations and in execution-record check IDs.
3. Cross-cycle SIM resolution (validator V3 and claimsource): a citation `SIM-Rk-C<n>/…` resolves against Cycle n's records (carried claims cite earlier runs without a prefix); the 1.0.0 `C0:` prefix is still accepted.
Changes 1–2 were made after the first Cycle-2 validation run reported them as errors (21 V2 errors for dotted IDs); no data were changed. They are disclosed here and in `Research/tools/CHANGELOG.md`.

| Instances validated | C0 | C1 | C2 |
|---|---|---|---|
| claims | 100 | 142 | 177 |
| sources | 78 | 115 | 130 |
| links | 24 | 24 | 24 |
| execution records | 8 | 21 | 42 |

**0 errors**, 83 warnings:

| Cycle | Warning | n |
|---|---|---|
| C0 | Q1 | 40 |
| C0 | Q2 | 2 |
| C0 | Q3 | 1 |
| C0 | Q4 | 1 |
| C1 | Q1 | 37 |
| C1 | Q3 | 1 |
| C2 | Q3 | 1 |

Q1 (empty limits field) is now 0 for Cycle 2: the 37 carried Cycle-1 gaps were filled. The C0/C1 warnings are historical (those files are not modified). C2's single Q3 is L24 (Philosophical/Spiritual link; placeholder rejection criterion).

## Claim-source checks (`../validation/claim_source_C*.json`, offline, with local snapshots)
- C0: K-resolve {'Pass': 100}; K-access {'n/a': 100}; K-sim {'n/a': 87, 'Pass': 13}; K-phrase {'Pass': 81, 'n/a': 19}.
- C1: K-resolve {'Pass': 142}; K-access {'Pass': 67, 'n/a': 75}; K-sim {'n/a': 109, 'Pass': 33}; K-phrase {'Pass': 103, 'n/a': 39}.
- C2: K-resolve {'Pass': 177}; K-access {'Pass': 75, 'n/a': 102}; K-sim {'n/a': 124, 'Pass': 53}; K-phrase {'Pass': 118, 'n/a': 59}.

K-phrase in 0.2.0 treats ledger phrases as regular expressions (as the cycles' live verification does) with a literal fallback, and splits on ' || ' (0.1.0 split on ';' and mis-parsed). Snapshots for S13/S20/S23 are the PubMed abstract files retrieved in Cycle 0 (their landing-page snapshots were bot-wall stubs).
