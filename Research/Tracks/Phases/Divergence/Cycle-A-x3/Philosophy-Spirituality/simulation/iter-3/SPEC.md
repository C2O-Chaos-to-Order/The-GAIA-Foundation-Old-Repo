# SIM-DV-PHI-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Nested schisms as branching: does a constant-rate splitting process give the expected number of groups, and does heritable variation in splitting rates make schism trees more lopsided?

## Phase operationalization tested
PHI Divergence = religious schism/denominational branching as a tree (P14: world religions may show tree-like nested schisms).

## Sources this run draws on
P14 (Evans et al. 2021, read in full): 'the spread of major world religions might show relatively tree-like structure in their nested pattern of schisms'; tree vs network caveats.

## Refinement from previous iteration
New run family. Design changed after a reduced-size smoke test: growing trees to a fixed time let heritable rates explode group numbers, confounding the imbalance comparison, so imbalance is compared at a fixed number of groups (30). Thresholds were not changed.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | Yule mean count within 4 SE of exp(lam T) |
| H1 | hypothesis | heritable rates raise normalised Colless by > 4 SE |
| R1 | reporting | results |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Pure-birth model: no extinction, mergers or reticulation (P14 stresses horizontal transmission). Models no real tradition. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-A",
 "iteration": 3,
 "kind": "schism_yule",
 "seed": 15603,
 "lam": 1.0,
 "T": 3.0,
 "tips": 30,
 "het": 0.5,
 "reps": 1000,
 "cap": 2000,
 "tol_se": 4
}
```

## Command
`python sim_phi.py iter-3` (run from `Philosophy-Spirituality/simulation/`)
