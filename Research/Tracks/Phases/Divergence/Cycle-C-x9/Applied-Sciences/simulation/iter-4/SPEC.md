# SIM-DV-APP-C - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P17's oscillator growth at a coarse step (h = 0.1).

## Phase operationalization tested
APP Divergence = solver divergence from a bounded solution (P17).

## Sources this run draws on
P17 (Brorson; read in full in DVB).

## Refinement from previous iteration
h_values [0.01, 0.001] -> [0.1, 0.01].

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | amplitude = (1+h^2w^2)^(n/2) (1e-9) |
| H1 | hypothesis | growth > 1% at h = 0.01 over 10 periods |
| H2 | hypothesis | symplectic within 5% at h = 0.1 |
| R1 | reporting | amplitudes |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-C",
 "iteration": 4,
 "kind": "euler_sho",
 "seed": 17404,
 "omega": 1.0,
 "h_values": [
  0.1,
  0.01
 ],
 "periods": 10,
 "h1": 0.01,
 "h2": 0.05
}
```

## Command
`python sim_app.py iter-4` (run from `Applied-Sciences/simulation/`)
