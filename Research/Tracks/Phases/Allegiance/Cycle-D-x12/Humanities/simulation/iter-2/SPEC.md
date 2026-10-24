# SIM-AL-HUM-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P65's Table 3 sample sizes: do the 17 explicit sizes sum to the printed 2,104 with Makarova et al. counted as 60 (30 parents + 30 children) or as 30, and is the median 74?

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
| H1 | hypothesis | sum with Makarova 60 equals 2,104 |
| H2 | hypothesis | sum with Makarova 30 equals 2,104 |
| H3 | hypothesis | median 74 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge by hand arithmetic after reading: 2,134 with 60 and 2,104 with 30; median 74 either way.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-D",
 "iteration": 2,
 "kind": "count_audit",
 "seed": 28502,
 "hyps": [
  [
   "sum with Makarova 60 equals 2,104",
   "abs(o['sums']['mak60']['diff']) < 1e-9"
  ],
  [
   "sum with Makarova 30 equals 2,104",
   "abs(o['sums']['mak30']['diff']) < 1e-9"
  ],
  [
   "median 74",
   "o['medians']['mak60']['computed'] == 74"
  ]
 ],
 "sums": {
  "mak60": {
   "parts": [
    25,
    179,
    45,
    301,
    292,
    117,
    177,
    54,
    70,
    290,
    18,
    60,
    17,
    284,
    74,
    127,
    4
   ],
   "printed": 2104
  },
  "mak30": {
   "parts": [
    25,
    179,
    45,
    301,
    292,
    117,
    177,
    54,
    70,
    290,
    18,
    30,
    17,
    284,
    74,
    127,
    4
   ],
   "printed": 2104
  }
 },
 "medians": {
  "mak60": {
   "values": [
    25,
    179,
    45,
    301,
    292,
    117,
    177,
    54,
    70,
    290,
    18,
    60,
    17,
    284,
    74,
    127,
    4
   ],
   "printed": 74
  }
 }
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
