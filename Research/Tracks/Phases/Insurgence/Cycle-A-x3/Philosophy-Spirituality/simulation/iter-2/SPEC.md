# SIM-IN-PHI-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P30's model with a = 1.5 (PHI pass 2): an interior unstable fixed point appears; does a minority with the higher utility (u = 0.6) decline if it starts below it and rise if above?

## Phase operationalization tested
PHI Insurgence = a new stance needing a critical mass even when it is preferred.

## Sources this run draws on
P30 (Abrams, Yaple & Wiener, arXiv:1012.1375v2, arXiv licence; read in full in INA): Eq. 1, P_yx = c x^a u_x, the a = 1 logistic case, fixed points for a > 1, two-clique experiment and delay d ~ -ln p/(2u-1).

## Refinement from previous iteration
Follows iter-1 (a = 1): nonlinear attraction a > 1.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | one interior fixed point |
| H1 | hypothesis | below: declines |
| H2 | hypothesis | above: dominates |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
a = 1.5 is illustrative; P30's data favoured a near 1. Euler dt 0.01, 200 time units. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-A",
 "iteration": 2,
 "kind": "abrams_groups",
 "seed": 20602,
 "mode": "bistable",
 "a": 1.5,
 "c": 1.0,
 "u": 0.6,
 "x0_values": [
  0.05,
  0.2,
  0.4,
  0.6
 ],
 "dt": 0.01,
 "steps": 20000
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
