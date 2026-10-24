# SIM-DV-PHI-C - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Control: no standardisation (u = 0): distance should keep rising.

## Phase operationalization tested
PHI Divergence = textual divergence of a classic's transmission lines followed by consolidation toward a received text (P18).

## Sources this run draws on
P18 (Chan, SEP 'Laozi', rev. 2025; read in full, end to end, in DVC): Guodian (c. 300 BCE), Mawangdui and Beida manuscripts; 'different collections of sayings ... overlapping to some extent'; 'The demand for textual uniformity rose ... the different textual traditions eventually gave way to the received text'. The model is the agent's formal analogue, not a reconstruction of the Laozi's history.

## Refinement from previous iteration
Control.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | divergence-phase distance within 4 SE |
| H1 | hypothesis | distance falls by > 30% (expected Not supported in a control) |
| R1 | reporting | distances |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-C",
 "iteration": 3,
 "kind": "text_consolidation",
 "seed": 17603,
 "lineages": 6,
 "M": 1000,
 "reps": 200,
 "t1": 20,
 "t2": 20,
 "mu": 0.01,
 "u": 0.0,
 "tol_se": 4,
 "h1": 0.3
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
