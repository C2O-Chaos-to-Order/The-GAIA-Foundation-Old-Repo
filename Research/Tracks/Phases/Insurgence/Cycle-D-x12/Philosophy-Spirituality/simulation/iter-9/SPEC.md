# SIM-IN-PHI-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-PHI iter-9 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
PHI Insurgence = growth of a once-marginal stance (religious non-affiliation) by conversion (P30); read here as a formal model, not a verdict on religion.

## Sources this run draws on
P30 (Abrams, Yaple & Wiener, arXiv:1012.1375v2, arXiv licence; read in full in INA): Eq. 1, P_yx = c x^a u_x, the a = 1 logistic case, fixed points for a > 1, two-clique experiment and delay d ~ -ln p/(2u-1).

## Refinement from previous iteration
Iteration 9 of the x12 family for PHI; follows iteration 8 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | RK4 matches logistic within 1e-6 |
| H1 | hypothesis | t_half <= 20 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-D",
 "iteration": 9,
 "kind": "abrams_groups",
 "seed": 23609,
 "mode": "logistic",
 "c": 1.0,
 "u": 0.65,
 "x0": 0.01,
 "dt": 0.01,
 "steps": 5000,
 "quantiles": [
  0.1,
  0.5,
  0.9
 ],
 "t_check": 20
}
```

## Command
`python sim_phi.py iter-9` (run from `Philosophy-Spirituality/simulation/`)
