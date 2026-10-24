# SIM-DV-NAT-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same model with five times more gene flow (m = 0.05): does the neutral background homogenise while the linked island persists?

## Phase operationalization tested
As iteration 1.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Iteration 1 used m = 0.01; only m and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral mean frequency 0.5 within 4 SE |
| H1 | hypothesis | Fst(c=0) - Fst(c=0.5) > 4 SE |
| H2 | hypothesis | monotone in c |
| H3 | hypothesis | Fst(c=0.01) below midpoint |
| R1 | reporting | Fst by c |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-B",
 "iteration": 3,
 "kind": "wf_linked",
 "seed": 16103,
 "m": 0.05,
 "s": 0.1,
 "N": 200,
 "reps": 60,
 "generations": 400,
 "per_c": 8,
 "c_values": [
  0.0,
  0.001,
  0.01,
  0.05,
  0.5
 ],
 "c_mid": 0.01,
 "tol_se": 4,
 "mono_tol": 0.02
}
```

## Command
`python sim_nat.py iter-3` (run from `Natural-Sciences/simulation/`)
