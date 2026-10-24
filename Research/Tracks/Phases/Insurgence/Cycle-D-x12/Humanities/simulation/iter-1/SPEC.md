# SIM-IN-HUM-D - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-HUM iter-1 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
HUM Insurgence = a sudden personal transformation without an identifiable trigger (P43), modelled as noise-induced escape.

## Sources this run draws on
P43 (Chirico et al. 2022, Front Psychol 13:790300, CC BY; main text read in full in INC): transformative experiences as brief, sudden, irreversible changes (integrated definition); James's volitional (gradual) and self-surrender (sudden) conversion; Carel & Kidd: cumulative small changes. Drift from P41 Eq. 3; the mapping to experience is the agent's (interpretive). P41 (Hessler & Kamps 2025, Nat Commun 16.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | no censoring |
| H1 | hypothesis | r^2 > 0.95 |
| H2 | hypothesis | slope within 0.15 of 0.5 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-D",
 "iteration": 1,
 "kind": "kramers_switch",
 "seed": 23501,
 "mode": "kramers",
 "sigmas": [
  0.35,
  0.4,
  0.45,
  0.5,
  0.6
 ],
 "reps": 400,
 "max_steps": 3000000,
 "h2": 0.15
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
