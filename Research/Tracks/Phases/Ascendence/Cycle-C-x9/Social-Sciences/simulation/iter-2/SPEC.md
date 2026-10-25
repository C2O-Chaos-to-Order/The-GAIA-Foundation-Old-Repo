# SIM-AS-SOC-C - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
2001: which scale (0.4-0.6) matches 67%?

## Phase operationalization tested
SOC Ascendence = upward and total intergenerational mobility (P87; P93 for women's educational mobility).

## Sources this run draws on
P87 (Paterson et al. 2025, social mobility in Scotland 1901-2001, Br J Sociol, PMC11890437, CC BY; read in full in AS0): Table 1 mobile/up/down; Table 2 origin and destination distributions (weighted in 1901 and 2001; sample sizes unweighted) and dissimilarity indices 0.12/0.16/0.23; Tables 3-4 outflow/inflow 1901 with sample sizes; Table 5 deviances 30,992/6865/1302 and printed reductions 78.8/95.8; text 'reduced by 79%', '17%', '46%', 'Fully 57%'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | point-estimate risk ratio equals the stated audit value within 1e-3 |
| H1 | hypothesis | 2001 margins: some inheritance scale in 0.4-0.6 gives % mobile within 1 point of Table 1's 67% |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As above. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-C",
 "iteration": 2,
 "kind": "mobility_qpm",
 "seed": 37302,
 "margins": {
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
  "x0.4": 0.4,
  "x0.5": 0.5,
  "x0.6": 0.6
 },
 "hyps": [
  [
   "2001 margins: some inheritance scale in 0.4-0.6 gives % mobile within 1 point of Table 1's 67%",
   "any(abs(o['by_year']['2001'][k]['pct_mobile'] - 67) <= 1 for k in ['x0.4','x0.5','x0.6'])"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
