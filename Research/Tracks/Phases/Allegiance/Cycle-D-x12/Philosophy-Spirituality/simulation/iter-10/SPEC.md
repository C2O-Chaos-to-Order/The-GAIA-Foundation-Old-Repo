# SIM-AL-PHI-D - iteration 10 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
theta 0.4.

## Phase operationalization tested
PHI Allegiance = loyalty buying time for voice.

## Sources this run draws on
P51 (read in full in AL0): Hirschman's exit, voice and loyalty.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | recovery at 0.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-D",
 "iteration": 10,
 "kind": "exit_voice",
 "seed": 28610,
 "dt": 0.05,
 "N": 200,
 "reps": 40,
 "theta": 0.4,
 "d": 0.02,
 "v": 0.1,
 "T": 300,
 "noise": 0.01,
 "lam_max": [
  0.0,
  0.2,
  0.6
 ],
 "h1_text": "recovery >= 0.45 at lam_max 0.2",
 "h1_expr": "o['0.2']['Q_end'] >= 0.45"
}
```

## Command
`python sim_phi.py iter-10` (run from `Philosophy-Spirituality/simulation/`)
