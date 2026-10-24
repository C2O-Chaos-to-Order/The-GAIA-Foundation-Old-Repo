# SIM-AL-PHI-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Higher standard (theta 0.7, voice margin v(1 - theta) = 0.03 vs decline 0.02): is there a minimum loyalty below which members leave too early for voice to save the institution?

## Phase operationalization tested
PHI Allegiance = how much loyalty is enough.

## Sources this run draws on
P51 (Kleinig, SEP 'Loyalty', read in full in AL0): Hirschman's exit, voice and loyalty; loyalty persists while voice tries to bring the institution back on track.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | collapse (Q_end < 0.1) at lam_max 0 and 0.1, recovery (>= 0.6) at 0.3 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy. Foreknowledge by reasoning: at lam_max 0.1, once quality falls 0.05 below theta half the members have left and the voice term (about 0.0175) is below the decline (0.02), so collapse was expected; at 0.3 recovery was expected.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-A",
 "iteration": 3,
 "kind": "exit_voice",
 "seed": 25603,
 "theta": 0.7,
 "d": 0.02,
 "v": 0.1,
 "dt": 0.05,
 "T": 400,
 "noise": 0.01,
 "lam_max": [
  0.0,
  0.1,
  0.3
 ],
 "N": 200,
 "reps": 40,
 "h1_text": "collapse at lam_max 0 and 0.1, recovery to >= 0.6 at 0.3",
 "h1_expr": "o['0.0']['Q_end'] < 0.1 and o['0.1']['Q_end'] < 0.1 and o['0.3']['Q_end'] >= 0.6"
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
