# SIM-SUBC-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Test the post-hoc selection problem: if 'unaware' participants are selected because their (noisy) awareness score is below chance, do they still show priming when ALL priming is carried by conscious knowledge?

## Sources this run draws on
K09 (awareness tests are insensitive); K08 (debriefing suggestive of awareness of primes). The selection argument itself is a statistical consequence of measurement error (regression to the mean), modelled here; no source's data are used.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | b = 0: selected-subgroup positive-significance rate <= 0.08 |
| H1 | hypothesis | b = 0.4: selected 'unaware' subgroup shows significant priming in >= 50% of studies |
| R1 | reporting | true knowledge of the selected subgroup |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Linear-normal latent model; one awareness measure; the cut (score < 0 = below chance) is illustrative. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-SUBC-A",
 "iteration": 2,
 "kind": "posthoc_unaware",
 "seed": 102,
 "mu": 0.5,
 "reliability": 0.5,
 "N": 100,
 "cut": 0.0,
 "b_list": [
  0.0,
  0.2,
  0.4
 ],
 "alpha": 0.05,
 "reps": 4000
}
```

## Command
`python sim_subc.py iter-2` (run from `Subconscious/simulation/`)
