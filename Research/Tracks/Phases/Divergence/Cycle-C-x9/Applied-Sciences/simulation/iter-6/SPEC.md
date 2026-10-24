# SIM-DV-APP-C - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P17 stability condition on a wider grid (h lam 0.5, 1.5, 2.5, 3).

## Phase operationalization tested
APP Divergence = instability beyond the stability region (P17).

## Sources this run draws on
P17 (read in full in DVB).

## Refinement from previous iteration
New grid.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | final |y| = |1 - h lam|^steps |
| V2 | validation | < 2 decays, > 2 grows |
| R1 | reporting | factors |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic. h lam = 1.5 has factor 0.5 (oscillating decay). Steps reduced to 500 after the first SPEC (3000 steps) crashed with a floating-point overflow (2^3000) before producing any result; disclosed.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-C",
 "iteration": 6,
 "kind": "euler_stability",
 "seed": 17406,
 "hlam": [
  0.5,
  1.5,
  2.5,
  3.0
 ],
 "steps": 500
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
