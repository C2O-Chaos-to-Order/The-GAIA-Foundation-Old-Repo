# SIM-AL-HUM-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P65's screening and pattern counts: do they add up (245 - 184 = 60? 60 - 25 = 35; 35 - 17 = 18; 14 + 4 - 1 = 17 PCC exclusions; 6 + 11 + 10 + 2 + 5 = 34 units)?

## Phase operationalization tested
HUM Allegiance = auditing a review of minority language attitudes (P65).

## Sources this run draws on
P65 (Chen, Lee, Roshida Binti Ab. Razak, Binti Ab. Majid & Lv 2026, 'Ethnic minorities' language attitudes toward heritage dialects and official standard languages: a narrative review', Front Psychol 17:1818757, PMC13655717, CC BY; read in full in ALD): screening counts (245 records, 184 duplicates, 60 screened, 25 excluded, 35 full texts, 17 excluded, 18 included), 34 analytical units (6 assimilation, 11 resistance, 10 structured ambivalence, 2 transition, 5 partial), Table 3 sample sizes, reported total 2,104 and median 74.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | deduplication count adds up |
| H2 | hypothesis | all other counts add up |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
count_audit kind added to sim_hum in ALD (smoke-tested at seed 99 on a toy sum). Foreknowledge from reading: 245 - 184 = 61, not 60.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-D",
 "iteration": 1,
 "kind": "count_audit",
 "seed": 28501,
 "hyps": [
  [
   "deduplication count adds up",
   "abs(o['sums']['dedup']['diff']) < 1e-9"
  ],
  [
   "all other counts add up",
   "all(abs(o['sums'][k]['diff']) < 1e-9 for k in ['pub_screen', 'pcc', 'pcc_excl', 'units'])"
  ]
 ],
 "sums": {
  "dedup": {
   "parts": [
    245,
    -184
   ],
   "printed": 60
  },
  "pub_screen": {
   "parts": [
    60,
    -25
   ],
   "printed": 35
  },
  "pcc": {
   "parts": [
    35,
    -17
   ],
   "printed": 18
  },
  "pcc_excl": {
   "parts": [
    14,
    4,
    -1
   ],
   "printed": 17
  },
  "units": {
   "parts": [
    6,
    11,
    10,
    2,
    5
   ],
   "printed": 34
  }
 }
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
