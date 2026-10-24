# SIM-DV-NAT-A - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Same model over a grid of selection strengths (s from 0 to 0.1 at m = 0.01) to locate where selected-locus divergence takes off relative to migration.

## Phase operationalization tested
NAT Divergence = migration-selection balance: divergence at a locus persists when selection is strong relative to gene flow.

## Sources this run draws on
As iteration 1.

## Refinement from previous iteration
Iteration 1 tested one s; this iteration sweeps s to see the dose-response (H2 becomes informative with six grid points).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | s = 0 neutral equivalence (4 SE) |
| H1 | hypothesis | s = 0.1: Fst_sel > 0.5 and Fst_neutral < 0.2 |
| H2 | hypothesis | Fst_sel non-decreasing in s (tolerance 0.02) |
| R1 | reporting | Fst by s |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As iteration 1. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-A",
 "iteration": 2,
 "kind": "wf_selection",
 "seed": 15102,
 "N": 100,
 "loci": 400,
 "reps": 200,
 "generations": 200,
 "m": 0.01,
 "s_values": [
  0.0,
  0.005,
  0.01,
  0.02,
  0.05,
  0.1
 ],
 "tol_se": 4,
 "h1": 0.5,
 "h2": 0.2
}
```

## Command
`python sim_nat.py iter-2` (run from `Natural-Sciences/simulation/`)
