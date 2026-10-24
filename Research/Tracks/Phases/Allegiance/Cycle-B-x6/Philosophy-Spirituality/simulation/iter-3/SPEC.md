# SIM-AL-PHI-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Stronger voice (v 0.2) under the noisy setting of ALA iter-2 (noise 0.05): does more effective voice restore the benefit of moderate loyalty?

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
| H1 | hypothesis | recovery >= 0.45 with lam_max >= 0.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-B",
 "iteration": 3,
 "kind": "exit_voice",
 "seed": 26603,
 "dt": 0.05,
 "N": 200,
 "reps": 40,
 "theta": 0.5,
 "d": 0.02,
 "v": 0.2,
 "T": 300,
 "noise": 0.05,
 "lam_max": [
  0.0,
  0.2,
  0.6
 ],
 "h1_text": "recovery >= 0.45 with lam_max >= 0.2",
 "h1_expr": "all(o[k]['Q_end'] >= 0.45 for k in ['0.2', '0.6'])"
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
