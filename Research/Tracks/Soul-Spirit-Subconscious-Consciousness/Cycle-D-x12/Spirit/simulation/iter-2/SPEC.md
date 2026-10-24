# SIM-SPIRIT-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K49's criterion needs >= 60% on all four MEQ30 subscales. Given the subscale reliabilities K49 reports, how often would two parallel measurements of the same experience disagree on 'complete'?

## Sources this run draws on
K49: alphas 0.97, 0.92, 0.86, 0.90; criterion >= 60% on each subscale. Second-order loading 0.8, mean 0.6 and SD 0.2 on the 0-1 scale are ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | error-free: no disagreement |
| H1 | hypothesis | disagreement >= 10% |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Cronbach alpha treated as parallel-test reliability; normal scores without ceiling. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SPIRIT-D",
 "iteration": 2,
 "kind": "cutoff_reliability",
 "seed": 1202,
 "alphas": [
  0.97,
  0.92,
  0.86,
  0.9
 ],
 "lam": 0.8,
 "mean": 0.6,
 "sd": 0.2,
 "n": 400000,
 "h1": 0.1
}
```

## Command
`python sim_spirit.py iter-2` (run from `Spirit/simulation/`)
