# SIM-IN-FOR-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication at larger n (FOR pass 3): repeat IN0's giant-component run with n = 200,000 (5 graphs per c) and a fresh subcritical sample; is the largest-component fraction within 0.02 of s from c = 1.1 upward?

## Phase operationalization tested
FOR Insurgence = giant-component emergence (replication).

## Sources this run draws on
P27 (read in full in IN0); Eq. 2.2 and the printed experiment.

## Refinement from previous iteration
Follows iter-1/2: replication of IN0-FOR-02 at four times the size.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | subcritical mean within 4 SE of 1/(1-c) |
| H1 | hypothesis | P27's 5.45 within 4 SE |
| H2 | hypothesis | within 0.02 of s for c >= 1.1 |
| H3 | hypothesis | <= 0.02 at c <= 0.9, >= 0.5 at c = 1.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Five graphs per c. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-A",
 "iteration": 3,
 "kind": "er_giant",
 "seed": 20203,
 "n_sub": 5000,
 "c_sub": 0.8,
 "reps_sub": 1000,
 "printed": 5.45,
 "c_values": [
  0.5,
  0.7,
  0.9,
  1.0,
  1.1,
  1.2,
  1.3,
  1.5
 ],
 "n": 200000,
 "reps": 5,
 "h2": 0.02,
 "h2_from": 1.1,
 "below": 0.9,
 "above": 1.5,
 "h3_lo": 0.02,
 "h3_hi": 0.5,
 "tol_se": 4
}
```

## Command
`python sim_for.py iter-3` (run from `Formal-Sciences/simulation/`)
