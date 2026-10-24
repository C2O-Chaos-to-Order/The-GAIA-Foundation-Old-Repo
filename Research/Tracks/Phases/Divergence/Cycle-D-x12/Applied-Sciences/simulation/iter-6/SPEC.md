# SIM-DV-APP-D - iteration 6 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Serial-order effect (P24: 'response rates decrease while response originality increases'): does sampling ideas without replacement from a skewed accessibility distribution (a = 1) reproduce both trends?

## Phase operationalization tested
APP Divergence = divergent thinking, the generation of many ideas to an open-ended problem, measured by fluency, originality and flexibility (P24); its scores are design-process measures.

## Sources this run draws on
P24 (Barbot 2018, 'The Dynamics of Creative Ideation: Introducing a New Assessment Paradigm', Frontiers in Psychology 9:2529, CC BY; read in full in DVD). Section 'Measuring Creative Ideation'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | values in range |
| H1 | hypothesis | uncommonness rises with order |
| H2 | hypothesis | waits longer in the second half |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's mechanism (sampling without replacement from a skewed accessibility distribution); P24 reports the effect, not this mechanism. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-D",
 "iteration": 6,
 "kind": "serial_order",
 "seed": 18406,
 "K": 200,
 "a": 1.0,
 "c": 0.1,
 "responses": 15,
 "persons": 300,
 "tol_se": 4
}
```

## Command
`python sim_app.py iter-6` (run from `Applied-Sciences/simulation/`)
