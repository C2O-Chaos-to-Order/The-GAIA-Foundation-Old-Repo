# SIM-IN-PHI-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P30's group-competition model with a = 1 (PHI pass 2): with utility u = 0.65 for the unaffiliated (P30's collapse value) and x0 = 0.01, does the solution follow the logistic with rate c(2u - 1), and pass 0.5 by t = 20?

## Phase operationalization tested
PHI Insurgence = growth of a once-marginal stance (religious non-affiliation) by conversion (P30); read here as a formal model, not a verdict on religion.

## Sources this run draws on
P30 (Abrams, Yaple & Wiener, arXiv:1012.1375v2, arXiv licence; read in full in INA): Eq. 1, P_yx = c x^a u_x, the a = 1 logistic case, fixed points for a > 1, two-clique experiment and delay d ~ -ln p/(2u-1).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | RK4 matches logistic within 1e-6 |
| H1 | hypothesis | t_half <= 20 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; c = 1 sets the time unit. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-A",
 "iteration": 1,
 "kind": "abrams_groups",
 "seed": 20601,
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
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
