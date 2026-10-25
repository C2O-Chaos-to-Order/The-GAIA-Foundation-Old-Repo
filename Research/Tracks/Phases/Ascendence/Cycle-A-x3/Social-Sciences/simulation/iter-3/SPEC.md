# SIM-AS-SOC-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Sensitivity of total mobility to inheritance on 2001 margins: does % mobile fall monotonically as Table 6's inheritance is scaled 0, 0.5, 1, 1.5, 2, and never below the dissimilarity-index bound?

## Phase operationalization tested
SOC Ascendence = mobility as a function of fluidity (P87's QPM form).

## Sources this run draws on
P87 (Paterson et al. 2025, social mobility in Scotland 1901-2001, Br J Sociol, PMC11890437, CC BY; read in full in AS0): Table 1 mobile/up/down; Table 2 origin and destination distributions (weighted in 1901 and 2001; sample sizes unweighted) and dissimilarity indices 0.12/0.16/0.23; Tables 3-4 outflow/inflow 1901 with sample sizes; Table 5 deviances 30,992/6865/1302 and printed reductions 78.8/95.8; text 'reduced by 79%', '17%', '46%', 'Fully 57%'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | IPF reproduces both margins within 1e-9 |
| H1 | hypothesis | on 2001 margins, % mobile falls monotonically as inheritance is scaled 0, 0.5, 1, 1.5, 2 |
| H2 | hypothesis | % mobile never falls below the dissimilarity-index minimum (structural lower bound) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's sensitivity analysis. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Smoke test (seed 99, temporary directory, before this SPEC) used this exact configuration, so the outcome was seen in advance (disclosed); hypotheses and thresholds were written before the smoke test and not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AS-SOC-A",
 "iteration": 3,
 "kind": "mobility_qpm",
 "seed": 35303,
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
  "x0.5": 0.5,
  "x1": 1.0,
  "x1.5": 1.5,
  "x2": 2.0
 },
 "hyps": [
  [
   "on 2001 margins, % mobile falls monotonically as inheritance is scaled 0, 0.5, 1, 1.5, 2",
   "(lambda r: r['independence']['pct_mobile'] > r['x0.5']['pct_mobile'] > r['x1']['pct_mobile'] > r['x1.5']['pct_mobile'] > r['x2']['pct_mobile'])(o['by_year']['2001'])"
  ],
  [
   "% mobile never falls below the dissimilarity-index minimum (structural lower bound)",
   "all(v['pct_mobile'] >= o['by_year']['2001']['min_mobility_pct'] - 1e-6 for k, v in o['by_year']['2001'].items() if isinstance(v, dict))"
  ]
 ]
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
