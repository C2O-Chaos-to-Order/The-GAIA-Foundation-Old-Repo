# SIM-IN-FOR-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of IN0-FOR-02 giant component on a third seed.

## Phase operationalization tested
FOR Insurgence = giant component (replication).

## Sources this run draws on
P27.

## Refinement from previous iteration
Iteration 8 of the x9 family for FOR; follows iteration 7 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | subcritical within 4 SE |
| H1 | hypothesis | 5.45 within 4 SE |
| H2 | hypothesis | within 0.02 of s for c >= 1.1 |
| H3 | hypothesis | <= 0.02 at 0.9, >= 0.5 at 1.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-FOR-C",
 "iteration": 8,
 "kind": "er_giant",
 "seed": 22208,
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
 "n": 100000,
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
`python sim_for.py iter-8` (run from `Formal-Sciences/simulation/`)
