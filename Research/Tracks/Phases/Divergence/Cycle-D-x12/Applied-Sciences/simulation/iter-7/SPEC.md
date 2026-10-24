# SIM-DV-APP-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Control: equal accessibility (a = 0). No serial-order effect is expected (H1 and H2 expected not supported).

## Phase operationalization tested
APP Divergence = divergent thinking, the generation of many ideas to an open-ended problem, measured by fluency, originality and flexibility (P24); its scores are design-process measures.

## Sources this run draws on
P24 (Barbot 2018, 'The Dynamics of Creative Ideation: Introducing a New Assessment Paradigm', Frontiers in Psychology 9:2529, CC BY; read in full in DVD).

## Refinement from previous iteration
Only a and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | values in range |
| H1 | hypothesis | uncommonness rises with order |
| H2 | hypothesis | waits longer in the second half |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's mechanism (sampling without replacement from a skewed accessibility distribution); P24 reports the effect, not this mechanism. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-D",
 "iteration": 7,
 "kind": "serial_order",
 "seed": 18407,
 "K": 200,
 "a": 0.0,
 "c": 0.1,
 "responses": 15,
 "persons": 300,
 "tol_se": 4
}
```

## Command
`python sim_app.py iter-7` (run from `Applied-Sciences/simulation/`)
