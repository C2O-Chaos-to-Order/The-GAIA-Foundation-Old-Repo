# SIM-SOUL-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K61 finds a religious framing effect (logit mean 0.52, between-country SD 0.22) and reports one country (Morocco) where religious framing did not increase continuity judgments. Is one exception among 24 countries expected?

## Sources this run draws on
K61: framing effect mu_gamma = 0.52 [0.41, 0.61], sigma_gamma = 0.22 [0.15, 0.32]; 'in all but one country - Morocco'. Country-level estimation SE 0.15 is ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim = 1-(1-p)^m |
| H1 | hypothesis | P(>=1 negative estimate) >= .2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Normal random effects; the model's own country estimates are partially pooled, which this ignores. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-D",
 "iteration": 2,
 "kind": "hetero_sign",
 "seed": 1102,
 "mu": 0.52,
 "sigma": 0.22,
 "countries": 24,
 "se": 0.15,
 "reps": 200000,
 "h1": 0.2
}
```

## Command
`python sim_soul.py iter-2` (run from `Soul/simulation/`)
