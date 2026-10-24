# SIM-DV-NAT-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Closer to onset (r = -0.004, 0.004) with 500,000 steps: does a long enough run reach the branch?

## Phase operationalization tested
As iteration 6.

## Sources this run draws on
As iteration 6.

## Refinement from previous iteration
Derived from SIM-DV-NAT-C iteration 9: r grid, steps and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | supercritical final = sqrt(r) (1e-6) |
| V2 | validation | r <= 0 decays |
| H1 | hypothesis | subcritical escapes for every r > 0 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 6; near onset the 1e-6 validation bound may fail for a slow approach (critical slowing down), which would be a run-length limit, not a code error. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-D",
 "iteration": 6,
 "kind": "pitchfork_types",
 "seed": 18106,
 "r_values": [
  -0.004,
  0.004
 ],
 "eps": 0.01,
 "dt": 0.01,
 "steps": 500000,
 "cap": 10,
 "tol": 1e-06
}
```

## Command
`python sim_nat.py iter-6` (run from `Natural-Sciences/simulation/`)
