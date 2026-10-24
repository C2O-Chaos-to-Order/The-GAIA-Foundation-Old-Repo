# SIM-AL-PHI-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Unrecoverable decline (d = 0.06 > v(1 - theta) = 0.05): does loyalty only delay collapse, so that quality collapses at every loyalty level?

## Phase operationalization tested
PHI Allegiance = loyalty to a failing institution.

## Sources this run draws on
P51 (Kleinig, SEP 'Loyalty', read in full in AL0): Hirschman's exit, voice and loyalty; loyalty persists while voice tries to bring the institution back on track.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | Q_end < 0.1 at every loyalty level |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Smoke in AL0 already showed this case (everyone exits).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-A",
 "iteration": 1,
 "kind": "exit_voice",
 "seed": 25601,
 "theta": 0.5,
 "d": 0.06,
 "v": 0.1,
 "dt": 0.05,
 "T": 300,
 "noise": 0.01,
 "lam_max": [
  0.0,
  0.2,
  0.6
 ],
 "N": 200,
 "reps": 40,
 "h1_text": "Q_end < 0.1 at every loyalty level",
 "h1_expr": "all(v['Q_end'] < 0.1 for v in o.values())"
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
