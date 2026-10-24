# SIM-DV-FOR-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
The divergence operator: finite-difference divergence vs analytic, and the divergence theorem (volume integral of div F = outward flux) by Monte Carlo.

## Phase operationalization tested
FOR Divergence = div F, net outflow per unit volume.

## Sources this run draws on
No source read in this track; vector-calculus identities only.

## Refinement from previous iteration
New run family (operator sense).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | finite difference within 1e-6 |
| V2 | validation | MC integral within 4 SE of flux 11/6 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One polynomial field on the unit cube. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-A",
 "iteration": 3,
 "kind": "divergence_operator",
 "seed": 15203,
 "fd_points": 1000,
 "h": 0.0001,
 "fd_tol": 1e-06,
 "mc_n": 200000,
 "tol_se": 4
}
```

## Command
`python sim_for.py iter-3` (run from `Formal-Sciences/simulation/`)
