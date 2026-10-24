# SIM-DV-PHI-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
One-to-many process across concentration values (0.5, 1, 2).

## Phase operationalization tested
PHI Divergence = differentiation from a single source, formal skeleton (P07, P08, P18).

## Sources this run draws on
P07, P08 (re-read in full in DVB); P18 (cited passages).

## Refinement from previous iteration
DVA iteration 1 used alpha = 1 only.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean K within 4 SE per alpha |
| H1 | hypothesis | largest-branch share > 0.3 |
| R1 | reporting | by alpha |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Formal process only. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-B",
 "iteration": 4,
 "kind": "crp_one_many_se",
 "seed": 16604,
 "alphas": [
  0.5,
  1.0,
  2.0
 ],
 "n": 1000,
 "reps": 300,
 "tol_se": 4,
 "h1": 0.3
}
```

## Command
`python sim_phi.py iter-4` (run from `Philosophy-Spirituality/simulation/`)
