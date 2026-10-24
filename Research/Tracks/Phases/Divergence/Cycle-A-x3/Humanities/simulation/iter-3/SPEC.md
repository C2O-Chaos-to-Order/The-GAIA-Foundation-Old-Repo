# SIM-DV-HUM-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Manuscript divergence: does tree reconstruction from copied texts recover the copying history, and how much does contamination (copying from two exemplars) degrade it?

## Phase operationalization tested
HUM Divergence = textual divergence of manuscript copies (stemmatics); contamination = horizontal transfer (P13).

## Sources this run draws on
P13 (Howe & Windram 2011, read in full): phylogenetic programs applied to manuscripts generally agree with conventional scholarship and with 'artificial' traditions; contamination is the main objection.

## Refinement from previous iteration
New run family (stemmatics was unsourced in DV0).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | changes per copy within 4 SE of M mu |
| H1 | hypothesis | clean triplet accuracy >= 0.95 |
| H2 | hypothesis | contamination lowers accuracy by >= 0.05 |
| R1 | reporting | per replicate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Balanced, clock-like copying tree with 8 surviving copies; UPGMA suits clock-like data, so H1 is favourable to the method; no lost exemplars. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-A",
 "iteration": 3,
 "kind": "stemma_copying",
 "seed": 15503,
 "depth": 3,
 "M": 500,
 "mu": 0.02,
 "reps": 50,
 "cont_frac": 0.3,
 "cont_leaves": 2,
 "tol_se": 4,
 "h1": 0.95,
 "h2": 0.05
}
```

## Command
`python sim_hum.py iter-3` (run from `Humanities/simulation/`)
