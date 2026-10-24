# SIM-DV-APP-C - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Oscillator growth at very small steps (h = 0.001, 0.0001): growth over 10 periods should be tiny but non-zero.

## Phase operationalization tested
As iteration 4.

## Sources this run draws on
P17 (read in full in DVB).

## Refinement from previous iteration
Smaller steps.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | amplitude formula |
| H1 | hypothesis | growth > 1% at h = 0.0001 |
| H2 | hypothesis | symplectic within 5% at h = 0.001 |
| R1 | reporting | amplitudes |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Expected growth at h = 1e-4 over 10 periods is about 0.03%, so H1 is expected Not supported (stated before running). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-C",
 "iteration": 8,
 "kind": "euler_sho",
 "seed": 17408,
 "omega": 1.0,
 "h_values": [
  0.001,
  0.0001
 ],
 "periods": 10,
 "h1": 0.01,
 "h2": 0.05
}
```

## Command
`python sim_app.py iter-8` (run from `Applied-Sciences/simulation/`)
