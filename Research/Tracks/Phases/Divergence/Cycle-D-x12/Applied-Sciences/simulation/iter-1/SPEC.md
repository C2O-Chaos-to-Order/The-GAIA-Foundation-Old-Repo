# SIM-DV-APP-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Recompute P24's printed conversions between average response time and fluency in a 10-minute task (50 s -> 12; Sj1 23 s -> about 26; Sj2 48 s -> about 12; 15 responses -> 40 s) and the reversal when only Exploration time (Sj1 14 s, Sj2 10 s) is used.

## Phase operationalization tested
APP Divergence = divergent thinking, the generation of many ideas to an open-ended problem, measured by fluency, originality and flexibility (P24); its scores are design-process measures.

## Sources this run draws on
P24 (Barbot 2018, 'The Dynamics of Creative Ideation: Introducing a New Assessment Paradigm', Frontiers in Psychology 9:2529, CC BY; read in full in DVD). Sections 'Response Time as a Measure of Fluency' and 'Response Process Markers'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | arithmetic computed |
| H1 | hypothesis | printed fluency within 1 of 600/s |
| H2 | hypothesis | reverse conversion exact |
| H3 | hypothesis | ranking reverses with Exploration time |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Consistency check of printed numbers ('about' read as within 1); P24's subjects are fictive (P24 footnote 1). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-D",
 "iteration": 1,
 "kind": "fluency_arith",
 "seed": 18401,
 "window": 600,
 "rows": {
  "50s": [
   50,
   12
  ],
  "Sj1": [
   23,
   26
  ],
  "Sj2": [
   48,
   12
  ]
 },
 "tol": 1,
 "reverse": [
  15,
  40
 ],
 "phases": {
  "Sj1": [
   23,
   14
  ],
  "Sj2": [
   48,
   10
  ]
 }
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
