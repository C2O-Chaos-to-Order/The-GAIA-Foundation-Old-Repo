# SIM-IN-HUM-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P29's measure of exogenous versus endogenous adoption: for (a, b) = [[0.1, 0.5]], does the agent-level share of exogenous adoptions match P29's Eq. 6?

## Phase operationalization tested
HUM Insurgence = a linguistic innovation spreading by outside push (exogenous) or imitation (endogenous) (P29).

## Sources this run draws on
P29 (Ghanbarnejad, Gerlach, Miotto & Altmann 2014, arXiv:1406.4498v2 = J R Soc Interface 11:20141044; arXiv HTML read in full in INB): Bass model Eq. 1, exogenous share G Eq. 3, G = (a/b) ln((a+b)/a) Eq. 6; a = b gives ln 2 = 0.69.

## Refinement from previous iteration
Iteration 2 of the x6 family for HUM; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | G in [0, 1] |
| H1 | hypothesis | within 4 SE + 0.005 of Eq. 6 |
| H2 | hypothesis | G < 0.5 at P29's Fig. 2 values (endogenous dominate) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
P29 Fig. 2 parameters (P29 reports G = 0.397 on a scale-free network). N = 2,000 agents, dt 0.01, 50 replicates; well mixed (P29 also uses networks). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-B",
 "iteration": 2,
 "kind": "bass_factors",
 "seed": 21502,
 "ab": [
  [
   0.1,
   0.5
  ]
 ],
 "N": 2000,
 "dt": 0.01,
 "reps": 50,
 "tol_se": 4,
 "bias": 0.005,
 "h2_text": "G < 0.5 at P29's Fig. 2 values (endogenous dominate)",
 "h2_expr": "o[\"0.1,0.5\"][\"G\"] < 0.5"
}
```

## Command
`python sim_hum.py iter-2` (run from `Humanities/simulation/`)
