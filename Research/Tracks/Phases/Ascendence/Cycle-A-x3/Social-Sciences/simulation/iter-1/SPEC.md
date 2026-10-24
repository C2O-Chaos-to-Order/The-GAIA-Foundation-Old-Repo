# SIM-AS-SOC-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Structural vs relative mobility with P87's quasi-perfect-mobility form: holding 1901 class inheritance (Table 6) fixed and fitting each year's Table 2 margins by IPF, does % mobile rise by at least 5 points 1901 to 2001, is 1901 within 5 points of Table 1's 52%, and does structural change alone account for half of the 15-point rise?

## Phase operationalization tested
SOC Ascendence = upward (and total) intergenerational mobility (P87).

## Sources this run draws on
P87 (Paterson et al. 2025, social mobility in Scotland 1901-2001, Br J Sociol, PMC11890437, CC BY; read in full in AS0): Table 1 mobile/up/down; Table 2 origin and destination distributions (weighted in 1901 and 2001; sample sizes unweighted) and dissimilarity indices 0.12/0.16/0.23; Tables 3-4 outflow/inflow 1901 with sample sizes; Table 5 deviances 30,992/6865/1302 and printed reductions 78.8/95.8; text 'reduced by 79%', '17%', '46%', 'Fully 57%'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | IPF reproduces both margins within 1e-9 |
| H1 | hypothesis | with 1901 class inheritance held fixed, % mobile rises by at least 5 points from 1901 to 2001 margins (structural change alone) |
| H2 | hypothesis | 1901 margins with 1901 inheritance give % mobile within 5 points of P87's Table 1 (52%) |
| H3 | hypothesis | structural change alone (fixed 1901 inheritance) accounts for at least half of Table 1's 15-point rise (52 to 67) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's model: Table 6's parameters are for 1901 only and the 7-class Table 2 margins are weighted; Table 1 may be computed on a different scheme. Up/down needs a class ranking, so only total mobility is modelled. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-A",
 "iteration": 1,
 "kind": "mobility_qpm",
 "seed": 35301,
 "margins": {
  "1901": [
   [
    4.9,
    1.7,
    6.6,
    11.4,
    38.4,
    20.3,
    16.9
   ],
   [
    7.3,
    5.2,
    8.7,
    5.4,
    41.1,
    21.2,
    11.1
   ]
  ],
  "1974": [
   [
    9.5,
    6.4,
    7.7,
    2.6,
    37.6,
    30.9,
    5.3
   ],
   [
    23.9,
    7.8,
    8.0,
    1.0,
    31.4,
    25.6,
    2.2
   ]
  ],
  "2001": [
   [
    27.4,
    17.1,
    7.1,
    1.5,
    22.5,
    22.9,
    1.5
   ],
   [
    46.9,
    8.9,
    4.8,
    0.05,
    26.3,
    13.1,
    0.1
   ]
  ]
 },
 "delta": [
  1.44,
  0.84,
  1.13,
  2.79,
  0.91,
  0.32,
  1.84
 ],
 "delta_scale": {
  "delta1901": 1.0
 },
 "hyps": [
  [
   "with 1901 class inheritance held fixed, % mobile rises by at least 5 points from 1901 to 2001 margins (structural change alone)",
   "o['by_year']['2001']['delta1901']['pct_mobile'] - o['by_year']['1901']['delta1901']['pct_mobile'] >= 5"
  ],
  [
   "1901 margins with 1901 inheritance give % mobile within 5 points of P87's Table 1 (52%)",
   "abs(o['by_year']['1901']['delta1901']['pct_mobile'] - 52) <= 5"
  ],
  [
   "structural change alone (fixed 1901 inheritance) accounts for at least half of Table 1's 15-point rise (52 to 67)",
   "o['by_year']['2001']['delta1901']['pct_mobile'] - o['by_year']['1901']['delta1901']['pct_mobile'] >= 7.5"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
