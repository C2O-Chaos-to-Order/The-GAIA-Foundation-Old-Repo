# SIM-IN-HUM-D - iteration 7 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-HUM iter-7 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
HUM Insurgence = a linguistic innovation spreading by outside push (exogenous) or imitation (endogenous) (P29).

## Sources this run draws on
P29 (Ghanbarnejad, Gerlach, Miotto & Altmann 2014, arXiv:1406.4498v2 = J R Soc Interface 11:20141044; arXiv HTML read in full in INB): Bass model Eq. 1, exogenous share G Eq. 3, G = (a/b) ln((a+b)/a) Eq. 6; a = b gives ln 2 = 0.69.

## Refinement from previous iteration
Iteration 7 of the x12 family for HUM; follows iteration 6 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | G in [0, 1] |
| H1 | hypothesis | within 4 SE + 0.005 of Eq. 6 |
| H2 | hypothesis | G < 0.2 for strong imitation and > 0.9 for strong push |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-D",
 "iteration": 7,
 "kind": "bass_factors",
 "seed": 23507,
 "ab": [
  [
   0.01,
   0.5
  ],
  [
   0.5,
   0.01
  ]
 ],
 "N": 2000,
 "dt": 0.01,
 "reps": 50,
 "tol_se": 4,
 "bias": 0.005,
 "h2_text": "G < 0.2 for strong imitation and > 0.9 for strong push",
 "h2_expr": "o[\"0.01,0.5\"][\"G\"] < 0.2 and o[\"0.5,0.01\"][\"G\"] > 0.9"
}
```

## Command
`python sim_hum.py iter-7` (run from `Humanities/simulation/`)
