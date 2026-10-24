# SIM-DV-APP-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence as clonal branching in a growing tumour: does neutral growth from one cell produce the 1/f subclonal-mutation signature?

## Phase operationalization tested
APP Divergence = branching clonal evolution producing intratumour heterogeneity (P05 neutral branching; P04 branched vs linear models).

## Sources this run draws on
P05 (parental clone branched into numerous subclones; simulation suggests neutral evolution can generate extensive heterogeneity); P04 (branched evolution common; linear model less frequent).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | N reached and bookkeeping exact |
| H1 | hypothesis | M(f) linear in 1/f on [0.1, 0.4], R^2 >= 0.98 |
| R1 | reporting | slope, clonal count |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Cell fractions, not sequencing allele frequencies; no sampling noise, no spatial structure, single run. Started from a mutation-free founder, so there are no clonal mutations by construction.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-0",
 "iteration": 1,
 "kind": "clonal_branching",
 "seed": 1504,
 "N": 5000,
 "birth": 1.0,
 "death": 0.3,
 "u": 2.0,
 "s": 0.0,
 "p_driver": 0.0,
 "fmin": 0.1,
 "fmax": 0.4,
 "h1": 0.98
}
```

## Command
`python sim_app.py iter-1` (run from `Applied-Sciences/simulation/`)
