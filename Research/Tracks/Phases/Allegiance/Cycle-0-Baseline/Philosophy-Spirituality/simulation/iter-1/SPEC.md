# SIM-AL-PHI-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Hirschman's account of loyalty as reported in P51: in a declining but recoverable institution, do members without loyalty exit at once so that nobody voices and the institution collapses, while moderate loyalty keeps members voicing long enough for recovery?

## Phase operationalization tested
PHI Allegiance = loyalty: 'a practical disposition to persist in an intrinsically valued ... associational attachment' at potential cost (P51).

## Sources this run draws on
P51 (Kleinig, 'Loyalty', Stanford Encyclopedia of Philosophy, substantive revision 29 Apr 2026; read in full in AL0, bibliography not read): working definition; Hirschman's exit/voice/loyalty; forfeiture of loyalty.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | collapse at lam_max = 0, recovery to >= 0.45 at lam_max >= 0.2 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical: the dynamics are the agent's formalization of a verbal account (Hirschman as summarized in P51); parameters arbitrary (decline 0.02, voice 0.1, theta 0.5). Smoke foreknowledge: Q_end 0.001 at lam_max 0 and 0.50 at 0.2; with decline 0.06 (unrecoverable) everyone exits. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-PHI-0",
 "iteration": 1,
 "kind": "exit_voice",
 "seed": 24601,
 "theta": 0.5,
 "d": 0.02,
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
 "h1_text": "Q_end < 0.1 without loyalty and >= 0.45 with lam_max >= 0.2",
 "h1_expr": "o['0.0']['Q_end'] < 0.1 and all(o[k]['Q_end'] >= 0.45 for k in ['0.2', '0.6'])"
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
