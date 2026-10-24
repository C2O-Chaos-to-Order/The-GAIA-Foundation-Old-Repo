# SIM-SOUL-C - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Robustness/sensitivity re-run of an earlier Cycle C iteration with changed assumptions; it is not a new source-based question. If one feature truly differs by 20 points, how often does the 23 vs 25 design show it as 15 or more points higher?

## Sources this run draws on
K46 (as iteration 4).

## Refinement from previous iteration
Iteration 4 had no true difference.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | null share ~ normal approx |
| H1 | hypothesis | P(any >= 15) >= .5 |
| R1 | reporting | shares |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 4.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-C",
 "iteration": 9,
 "kind": "descriptive_differences",
 "seed": 619,
 "n1": 23,
 "n2": 25,
 "base_rates": [
  0.5,
  0.4,
  0.3,
  0.3,
  0.2,
  0.15
 ],
 "true_shift": 0.2,
 "delta": 0.15,
 "reps": 100000
}
```

## Command
`python sim_soul.py iter-9` (run from `Soul/simulation/`)
