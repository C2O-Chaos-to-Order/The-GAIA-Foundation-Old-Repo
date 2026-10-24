# SIM-DV-NAT-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence with gene flow at a selected locus: does divergent selection keep one locus differentiated (an 'island') while migration homogenises neutral loci?

## Phase operationalization tested
NAT Divergence = locus-specific differentiation (Fst) under divergent selection with gene flow (the selected colour-pattern locus vs unlinked regions in P01, here only as a toy).

## Sources this run draws on
DV0 sources P01 (read at cited passages in DV0; not re-read in full in this cycle) for the motivating pattern; the model is textbook population genetics, not a source claim.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | s = 0: selected locus behaves as neutral (within 4 SE) |
| H1 | hypothesis | s = 0.05, Nm = 1: Fst_sel > 0.5 and Fst_neutral < 0.2 |
| H2 | hypothesis | Fst_sel non-decreasing in s |
| R1 | reporting | Fst by s |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Genic selection, unlinked loci, two demes, symmetric migration; no linkage, so no hitchhiking 'islands' in the genomic sense. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-A",
 "iteration": 1,
 "kind": "wf_selection",
 "seed": 15101,
 "N": 100,
 "loci": 400,
 "reps": 200,
 "generations": 200,
 "m": 0.01,
 "s_values": [
  0.0,
  0.05
 ],
 "tol_se": 4,
 "h1": 0.5,
 "h2": 0.2
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
