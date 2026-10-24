# SIM-IN-PHI-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P30's two-clique result (PHI pass 3): in a mean-field two-cluster version (sizes 0.1 and 0.9, out-group weight p), is the delay to x = 0.5 linear in -ln p/(2u - 1) as P30 reports?

## Phase operationalization tested
PHI Insurgence = a minority stance spreading out of its own clique.

## Sources this run draws on
P30 (Abrams, Yaple & Wiener, arXiv:1012.1375v2, arXiv licence; read in full in INA): Eq. 1, P_yx = c x^a u_x, the a = 1 logistic case, fixed points for a > 1, two-clique experiment and delay d ~ -ln p/(2u-1).

## Refinement from previous iteration
Follows iter-1/2: network structure (two cliques).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | all reach 0.5 |
| H1 | hypothesis | r^2 > 0.95 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Mean-field two-cluster ODE (agent's construction), not P30's N = 500 network simulation; u = 0.6. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-A",
 "iteration": 3,
 "kind": "abrams_groups",
 "seed": 20603,
 "mode": "cliques",
 "c": 1.0,
 "u": 0.6,
 "x0": 0.1,
 "p_values": [
  0.001,
  0.01,
  0.03,
  0.1,
  0.3,
  1.0
 ],
 "dt": 0.01,
 "tmax": 5000,
 "h1": 0.95
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
