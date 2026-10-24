# SIM-IN-APP-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Near the threshold (APP pass 2): R0 = 0.95, 1.05, 1.2 (P26's threshold reading); how close is the major-outbreak share (1,000 cases) to 1 - q when R0 is just above 1?

## Phase operationalization tested
APP Insurgence = outbreak emergence just above R0 = 1.

## Sources this run draws on
P26 (read in full in IN0). Branching model standard (not from P26).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | share within 4 SE (+0.002) of 1 - q |
| H1 | hypothesis | no major outbreak when R0 (1 - v) < 1 |
| H2 | hypothesis | calendar time scales with generation time |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Finite K = 1000: just above 1 many chains reach K and still die later, so the share can exceed 1 - q; the 0.002 allowance was set before running and may be too small (disclosed). 20,000 replicates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-APP-A",
 "iteration": 1,
 "kind": "branching_outbreak",
 "seed": 20401,
 "R0": [
  0.95,
  1.05,
  1.2
 ],
 "reps": 20000,
 "K": 1000,
 "Tg": [
  3,
  15
 ],
 "tol_se": 4
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
