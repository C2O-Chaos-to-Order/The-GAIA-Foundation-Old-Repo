# SIM-DV-FOR-D - iteration 8 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Linear divergence at an even slower rate (x -> 1.001 x).

## Phase operationalization tested
FOR Divergence = exponential separation vs chaos (P09).

## Sources this run draws on
P09 (re-read in full in DVB).

## Refinement from previous iteration
Derived from SIM-DV-FOR-C iteration 8: only c and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | linear exponent = ln 1.01 (1e-12) |
| V2 | validation | logistic exponent within 0.01 of ln 2 |
| V3 | validation | logistic orbit in [0,1] |
| H1 | hypothesis | logistic local shrink share > 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-D",
 "iteration": 8,
 "kind": "linear_vs_chaotic",
 "seed": 18208,
 "c": 1.001,
 "n": 100000,
 "pairs": 1000,
 "d0": 1e-09,
 "steps": 1000,
 "h1": 0.1
}
```

## Command
`python sim_for.py iter-8` (run from `Formal-Sciences/simulation/`)
