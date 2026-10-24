# SIM-DV-NAT-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
DVA migration-selection run repeated with double deme size (N = 200, Nm = 2): is the s = 0.1 'island' criterion robust to population size?

## Phase operationalization tested
NAT Divergence = migration-selection balance at an unlinked selected locus.

## Sources this run draws on
P01 (re-read in full in DVB) for the motivating pattern; model is textbook.

## Refinement from previous iteration
DVA iteration 2 used N = 100; N, generations and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | s = 0 neutral equivalence (4 SE) |
| H1 | hypothesis | s = 0.1: Fst_sel > 0.5 and Fst_neutral < 0.2 |
| H2 | hypothesis | Fst_sel non-decreasing in s |
| R1 | reporting | Fst by s |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVA: genic selection, unlinked loci, two demes. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-B",
 "iteration": 5,
 "kind": "wf_selection",
 "seed": 16105,
 "N": 200,
 "loci": 400,
 "reps": 200,
 "generations": 300,
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
`python sim_nat.py iter-5` (run from `Natural-Sciences/simulation/`)
