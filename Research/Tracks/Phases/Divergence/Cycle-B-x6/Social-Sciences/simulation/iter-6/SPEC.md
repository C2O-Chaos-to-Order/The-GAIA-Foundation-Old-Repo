# SIM-DV-SOC-B - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Noise run at a wider confidence bound (eps 0.3), where the noise-free model tends toward fewer clusters.

## Phase operationalization tested
As iteration 3.

## Sources this run draws on
As iteration 3.

## Refinement from previous iteration
Only eps and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sum conserved |
| H1 | hypothesis | noise 0.1 near uniform SD |
| H2 | hypothesis | noise 0.001 near noise-free SD |
| R1 | reporting | SD by noise |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 3. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-B",
 "iteration": 6,
 "kind": "bc_noise",
 "seed": 16306,
 "agents": 300,
 "eps": 0.3,
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
`python sim_soc.py iter-6` (run from `Social-Sciences/simulation/`)
