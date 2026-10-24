# SIM-SOUL-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K01 reports that across 24 countries mental states were judged more likely to continue after death than physical states, yet the modal answer was cessation for all states. Can both summaries hold at once, and what does each license?

## Sources this run draws on
K01 (van Elk 2022, describing Hoogeveen & van Elk's 24-country vignette study; no numbers are given in K01, so the marginals here are ILLUSTRATIVE, not K01's).

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | marginals within 0.01 |
| H1 | hypothesis | mental > physical significant at N = 10,000 |
| H2 | hypothesis | modal pattern = all cease (> 0.5) |
| H3 | hypothesis | 'dualist' pattern < 25% |
| R1 | reporting | power at n = 100 |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Illustrative marginals; latent-threshold item model. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-A",
 "iteration": 1,
 "kind": "continuity_vignette",
 "seed": 201,
 "N": 10000,
 "p_phys": 0.08,
 "p_ment": 0.18,
 "item_noise": 0.6,
 "n_small": 100,
 "reps_small": 2000
}
```

## Command
`python sim_soul.py iter-1` (run from `Soul/simulation/`)
