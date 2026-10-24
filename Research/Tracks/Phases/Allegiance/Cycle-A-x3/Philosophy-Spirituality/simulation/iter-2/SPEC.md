# SIM-AL-PHI-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Noisier institution (noise 0.05): does moderate loyalty still allow recovery to near the threshold while no loyalty means collapse?

## Phase operationalization tested
PHI Allegiance = loyalty buying time for voice (noisy).

## Sources this run draws on
P51 (Kleinig, SEP 'Loyalty', read in full in AL0): Hirschman's exit, voice and loyalty; loyalty persists while voice tries to bring the institution back on track.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | Q_end < 0.1 without loyalty and >= 0.45 with lam_max >= 0.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-A",
 "iteration": 2,
 "kind": "exit_voice",
 "seed": 25602,
 "theta": 0.5,
 "d": 0.02,
 "v": 0.1,
 "dt": 0.05,
 "T": 300,
 "noise": 0.05,
 "lam_max": [
  0.0,
  0.2,
  0.6
 ],
 "N": 200,
 "reps": 40,
 "h1_text": "Q_end < 0.1 without loyalty and >= 0.45 with lam_max >= 0.2",
 "h1_expr": "o['0.0']['Q_end'] < 0.1 and all(o[k]['Q_end'] >= 0.45 for k in ['0.2', '0.6'])"
}
```

## Command
`python sim_phi.py iter-2` (run from `Philosophy-Spirituality/simulation/`)
