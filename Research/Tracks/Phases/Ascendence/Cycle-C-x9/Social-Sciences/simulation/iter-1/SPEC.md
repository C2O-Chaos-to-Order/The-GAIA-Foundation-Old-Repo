# SIM-AS-SOC-C - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
1974: which inheritance scale (0.5-0.8) matches Table 1's 64%?

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
| H1 | hypothesis | 1974 margins: some inheritance scale in 0.5-0.8 gives % mobile within 1 point of Table 1's 64% |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's model (QPM diagonal scaling). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-C",
 "iteration": 1,
 "kind": "mobility_qpm",
 "seed": 37301,
 "margins": {
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
  "x0.5": 0.5,
  "x0.6": 0.6,
  "x0.7": 0.7,
  "x0.8": 0.8
 },
 "hyps": [
  [
   "1974 margins: some inheritance scale in 0.5-0.8 gives % mobile within 1 point of Table 1's 64%",
   "any(abs(o['by_year']['1974'][k]['pct_mobile'] - 64) <= 1 for k in ['x0.5','x0.6','x0.7','x0.8'])"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
