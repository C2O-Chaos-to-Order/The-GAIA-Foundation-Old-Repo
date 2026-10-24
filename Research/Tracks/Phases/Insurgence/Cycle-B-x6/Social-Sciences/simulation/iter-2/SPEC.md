# SIM-IN-SOC-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Pillar strategies toy (SOC x6, after P31): movement strength A = 0.1, threshold spread sd = 0.2: success share for spreading pressure, focusing on random pillars, focusing on the least loyal pillars.

## Phase operationalization tested
SOC Insurgence = a movement winning by inducing defections of regime pillars (P31).

## Sources this run draws on
P31 (Chenoweth, Hocking & Marks 2022, PLoS ONE 17:e0269976, CC BY; read in full in INB): pillar-proximity strategies raise success most when participation is small (about 20% to 50% and 85% at 0.1% participation). The toy is the agent's, not P31's model.

## Refinement from previous iteration
Iteration 2 of the x6 family for SOC; follows iteration 1 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | probabilities |
| H1 | hypothesis | weakest > focus > spread (medium movement) |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Medium movement. 50 pillars, focus on 10, boost 0.005 per defection, success = 30% defected within 50 steps; 300 replicates. Parameters chosen after one smoke run showed a degenerate regime (disclosed). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-B",
 "iteration": 2,
 "kind": "pillar_toy",
 "seed": 21302,
 "strategies": [
  "spread",
  "focus",
  "weakest"
 ],
 "Np": 50,
 "mu": 0.5,
 "sd": 0.2,
 "A": 0.1,
 "m": 10,
 "boost": 0.005,
 "v": 0.3,
 "T": 50,
 "reps": 300,
 "h1_text": "weakest > focus > spread (medium movement)",
 "h1_expr": "s[2] > s[1] > s[0]"
}
```

## Command
`python sim_soc.py iter-2` (run from `Social-Sciences/simulation/`)
