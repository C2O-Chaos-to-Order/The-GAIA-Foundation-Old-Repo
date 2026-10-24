# SIM-DV-FOR-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence as an asymmetric statistical dissimilarity: check non-negativity, zero self-divergence, a Monte Carlo estimator, and asymmetry of Kullback-Leibler divergence.

## Phase operationalization tested
FOR Divergence = statistical divergence D(p||q) (listed as unsourced in DV0 DEFINITIONS).

## Sources this run draws on
No source read in this track for KL divergence (PMC searches gave no short expository text; arXiv timed out). Claims from this run are labelled as simulation/code results only.

## Refinement from previous iteration
New run family (statistical sense of divergence).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | D >= 0 |
| V2 | validation | D(p||p) = 0 |
| V3 | validation | MC estimate within 4 SE in >= 49/50 pairs |
| H1 | hypothesis | median relative asymmetry > 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Dirichlet(1) random distributions on 10 points; says nothing about any empirical use. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-A",
 "iteration": 1,
 "kind": "kl_divergence",
 "seed": 15201,
 "K": 10,
 "pairs": 1000,
 "mc_pairs": 50,
 "mc_n": 20000,
 "tol_se": 4,
 "mc_min": 49,
 "h1": 0.1
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
