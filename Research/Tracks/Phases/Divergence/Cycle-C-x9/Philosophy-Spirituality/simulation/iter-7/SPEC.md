# SIM-DV-PHI-C - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
CFst scale sensitivity at a large true divergence (sb = 1.0).

## Phase operationalization tested
PHI Divergence = cross-population divergence of religious values via CFst (P15).

## Sources this run draws on
P15 (read in full in DVA).

## Refinement from previous iteration
sb -> 1.0.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | continuous CFst within max(4 SE, 0.005) |
| H1 | hypothesis | dichotomising lowers CFst >= 20% |
| R1 | reporting | means |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-C",
 "iteration": 7,
 "kind": "cfst_scale",
 "seed": 17607,
 "groups": 50,
 "n": 200,
 "sb": 1.0,
 "sw": 1.0,
 "reps": 200,
 "tol_se": 4,
 "bias_allow": 0.005,
 "h1": 0.2
}
```

## Command
`python sim_phi.py iter-7` (run from `Philosophy-Spirituality/simulation/`)
