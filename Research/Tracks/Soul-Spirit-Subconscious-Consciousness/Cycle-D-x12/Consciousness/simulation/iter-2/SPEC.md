# SIM-CONS-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K58 argues IIT's 'silent neuron' predictions are testable despite the objection that evidence would imply the test conditions were not met; it frames the dispute with Lakatos. If the auxiliary condition is verified only half the time, how much does one failed prediction weigh?

## Sources this run draws on
K58 (silent brain and disabled neuron predictions; testing conditions; Lakatos). Prior 0.5, power 0.8, failure probability 0.5 when the auxiliary fails ILLUSTRATIVE.

## Refinement from previous iteration
First iteration of this run family in this track cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim posterior = analytic |
| H1 | hypothesis | posterior >= .4 |
| R1 | reporting | posterior by q |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Two-state cartoon of auxiliary assumptions. Synthetic data only; seeded; nothing is fitted to any study's raw data. Results describe the model, not people.

## Parameters
```json
{
 "sim_id": "SIM-CONS-D",
 "iteration": 2,
 "kind": "auxiliary_test",
 "seed": 1402,
 "q_grid": [
  0.5,
  0.9
 ],
 "prior": 0.5,
 "power": 0.8,
 "f_aux": 0.5,
 "q_test": 0.5,
 "reps": 1000000,
 "h1": 0.4
}
```

## Command
`python sim_cons.py iter-2` (run from `Consciousness/simulation/`)
