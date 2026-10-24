# SIM-DV-PHI-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Re-test DV0's 'one -> many' process with a validation tolerance sized by the Monte Carlo standard error (DV0's V1 failed under a fixed 5% band).

## Phase operationalization tested
PHI Divergence = differentiation from a single source, formal skeleton only (P07, P08 motifs).

## Sources this run draws on
DV0 sources P07, P08 (read at cited passages in DV0; not re-read in full in this cycle). The process is a standard Chinese restaurant process.

## Refinement from previous iteration
Same model and sizes as SIM-DV-PHI-0 iter-1; only the tolerance (4 SE instead of 5%) and seed differ. DV0's Fail stays on record.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean K within 4 SE of analytic |
| H1 | hypothesis | largest-branch share > 0.3 |
| R1 | reporting | by alpha |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Formal process only; models no tradition. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-A",
 "iteration": 1,
 "kind": "crp_one_many_se",
 "seed": 15601,
 "alphas": [
  1.0
 ],
 "n": 1000,
 "reps": 300,
 "tol_se": 4,
 "h1": 0.3
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
