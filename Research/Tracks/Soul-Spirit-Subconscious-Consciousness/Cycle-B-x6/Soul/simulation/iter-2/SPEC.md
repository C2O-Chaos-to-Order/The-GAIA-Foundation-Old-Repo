# SIM-SOUL-B - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
K02 reports that 76% of respondents mentioned some annihilation after death and 35% some continuity. How many must have mentioned both?

## Sources this run draws on
K02 (Haimila & Muraja 2023): 76% annihilation, 35% continuity (open answers, overlapping categories).

## Refinement from previous iteration
Same bound logic applied to K02.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | LP = Frechet |
| H1 | hypothesis | co-mention forced >= 10% |
| R1 | reporting | bound |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; a 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic; marginals only.

## Parameters
```json
{
 "sim_id": "SIM-SOUL-B",
 "iteration": 2,
 "kind": "marginals_pairs",
 "seed": 212,
 "marginals": {
  "annihilation": 0.76,
  "continuity": 0.35
 },
 "pair": [
  "annihilation",
  "continuity"
 ],
 "h1_threshold": 0.1
}
```

## Command
`python sim_soul.py iter-2` (run from `Soul/simulation/`)
