# SIM-SUBC-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K23's meta-analysis of affective priming by brief faces reports g = .32 with a 95% prediction interval reaching below zero. What share of settings does that interval imply have no priming at all?

## Sources this run draws on
K23 (Zhou et al. 2026, BMC Psychology): g = 0.32, 95% CI [0.22, 0.42], 95% PI [-0.23, 0.88]; 62 studies, 182 effect sizes.

## Refinement from previous iteration
Extends iteration 1 of Cycle A (power) to between-setting heterogeneity.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | simulated share = analytic |
| H1 | hypothesis | >= 10% of settings have true effect <= 0 |
| R1 | reporting | tau |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal random-effects approximation with z quantiles; ignores K23's three-level structure (the PI was computed by K23 with its own model).

## Parameters
```json
{
 "sim_id": "SIM-SUBC-B",
 "iteration": 2,
 "kind": "prediction_interval",
 "seed": 112,
 "g": 0.32,
 "ci": [
  0.22,
  0.42
 ],
 "pi": [
  -0.23,
  0.88
 ],
 "draws": 2000000
}
```

## Command
`python sim_subc.py iter-2` (run from `Subconscious/simulation/`)
