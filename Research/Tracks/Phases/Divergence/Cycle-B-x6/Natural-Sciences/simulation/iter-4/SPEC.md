# SIM-DV-NAT-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Negative control: with no selection (s = 0) Fst should not depend on linkage to locus A.

## Phase operationalization tested
As iteration 1 (control).

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Control for iterations 1-3; only s and seed change. A 'Supported' H1 here would indicate a code artefact.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | neutral mean frequency 0.5 within 4 SE |
| H1 | hypothesis | Fst(c=0) - Fst(c=0.5) > 4 SE (expected Not supported in a control) |
| H2 | hypothesis | monotone in c |
| H3 | hypothesis | Fst(c=0.01) below midpoint |
| R1 | reporting | Fst by c |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. In a control, H2/H3 may pass or fail by chance. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-B",
 "iteration": 4,
 "kind": "wf_linked",
 "seed": 16104,
 "m": 0.01,
 "s": 0.0,
 "N": 200,
 "reps": 60,
 "generations": 400,
 "per_c": 8,
 "c_values": [
  0.0,
  0.001,
  0.01,
  0.05,
  0.5
 ],
 "c_mid": 0.01,
 "tol_se": 4,
 "mono_tol": 0.02
}
```

## Command
`python sim_nat.py iter-4` (run from `Natural-Sciences/simulation/`)
