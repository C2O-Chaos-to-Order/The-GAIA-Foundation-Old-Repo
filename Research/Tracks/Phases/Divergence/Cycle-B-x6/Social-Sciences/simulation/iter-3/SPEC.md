# SIM-DV-SOC-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Does random opinion noise erase bounded-confidence clustering? SD of opinions at noise 0, 0.001 and 0.1 per interaction.

## Phase operationalization tested
SOC Divergence = opinion dispersion maintained by noise vs clustering by homophily.

## Sources this run draws on
Bounded-confidence model as in DV0 (Deffuant); noise variant is the agent's choice, motivated by P03's finding that external events keep opinions spread. No source read for this noise rule.

## Refinement from previous iteration
New run family.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | noise 0 conserves opinion sum (1e-9) |
| H1 | hypothesis | noise 0.1: SD within 0.05 of uniform SD |
| H2 | hypothesis | noise 0.001: SD within 0.05 of noise-free SD |
| R1 | reporting | SD by noise |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Mean-field random pairs; SD is a coarse summary (clusters not counted). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-B",
 "iteration": 3,
 "kind": "bc_noise",
 "seed": 16303,
 "agents": 300,
 "eps": 0.2,
 "mu": 0.5,
 "steps": 150000,
 "noise": [
  0.0,
  0.001,
  0.1
 ],
 "reps": 10,
 "h_tol": 0.05
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
