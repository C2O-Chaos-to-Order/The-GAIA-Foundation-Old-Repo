# SIM-DV-APP-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Boundary of P17's stability condition |1 + a h| < 1 for real negative a: behaviour just inside and just outside h|lambda| = 2 (1.99 and 2.01), with 3000 steps so the DVA thresholds (final < 1e-6 or > 1e6) can resolve the near-boundary cases.

## Phase operationalization tested
APP Divergence = solver instability beyond the stability region.

## Sources this run draws on
P17 (read in full): |1 + a h| < 1 condition and stability region (fig. 2.10). DVA run used the same kind.

## Refinement from previous iteration
DVA iteration 3 used a coarse grid; this grid brackets the boundary.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | final |y| = |1 - h lam|^steps (1e-9) |
| V2 | validation | h lam < 2 decays below 1e-6, > 2 grows above 1e6 |
| R1 | reporting | factors |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic floating point. h lam = 2 exactly (|factor| = 1) is excluded because the DVA kind's V2 has no neutral case; this exclusion was decided before running.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-B",
 "iteration": 6,
 "kind": "euler_stability",
 "seed": 16406,
 "hlam": [
  1.9,
  1.99,
  2.01,
  2.1
 ],
 "steps": 3000
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
