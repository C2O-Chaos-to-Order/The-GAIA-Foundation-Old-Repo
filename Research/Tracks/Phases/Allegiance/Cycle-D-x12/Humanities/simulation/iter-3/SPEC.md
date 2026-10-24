# SIM-AL-HUM-D - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P65 calls structured ambivalence 'the most frequently observed' configuration: is its unit count (10, or 10 including 4 domain-differentiated) the largest of the three patterns (assimilation 6, resistance 11)?

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
| H1 | hypothesis | ambivalence count exceeds resistance and assimilation |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge from reading: resistance has 11 units.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-AL-HUM-D",
 "iteration": 3,
 "kind": "count_audit",
 "seed": 28503,
 "hyps": [
  [
   "ambivalence count exceeds resistance and assimilation",
   "o['sums']['ambivalence']['computed'] > max(o['sums']['resistance']['computed'], o['sums']['assimilation']['computed'])"
  ]
 ],
 "sums": {
  "ambivalence": {
   "parts": [
    10
   ],
   "printed": 10
  },
  "resistance": {
   "parts": [
    11
   ],
   "printed": 11
  },
  "assimilation": {
   "parts": [
    6
   ],
   "printed": 6
  }
 }
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
