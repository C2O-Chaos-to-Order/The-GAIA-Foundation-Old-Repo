# SIM-DV-FOR-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same check with 50 categories, where the Stirling correction term is larger at a given n.

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Iteration 1 used K = 6; only K and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | LR rate within 4 SE of D |
| H1 | hypothesis | Eq. A2 within 0.01 nats at n = 1e5 |
| H2 | hypothesis | error decreases with n |
| R1 | reporting | by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-B",
 "iteration": 2,
 "kind": "kl_likelihood",
 "seed": 16202,
 "K": 50,
 "conc": 1.0,
 "n_values": [
  100,
  1000,
  10000,
  100000
 ],
 "reps": 200,
 "tol_se": 4,
 "h1": 0.01
}
```

## Command
`python sim_for.py iter-2` (run from `Formal-Sciences/simulation/`)
