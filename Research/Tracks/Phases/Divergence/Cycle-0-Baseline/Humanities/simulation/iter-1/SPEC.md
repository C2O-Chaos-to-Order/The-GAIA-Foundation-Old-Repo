# SIM-DV-HUM-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence as language splitting: how well does a constant-rate shared-cognate estimate recover split time, with and without rate heterogeneity?

## Phase operationalization tested
HUM Divergence = lexical divergence of daughter languages from a common ancestor, measured by shared cognates (P06 cognacy-based phylogenies).

## Sources this run draws on
P06 (cognacy-based vs qualitative classifications of Andic; geographic distance correlates with linguistic divergence).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | homogeneous: T_hat bias within 5% |
| V2 | validation | mean C within 0.02 of analytic |
| H1 | hypothesis | shape-1 heterogeneity -> underestimate by >= 10% |
| R1 | reporting | by shape |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Ignores borrowing, chance resemblance and coding error; the rate r = 0.07 per millennium is an illustrative value, not taken from a source read in this cycle.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-0",
 "iteration": 1,
 "kind": "lexical_divergence",
 "seed": 1505,
 "M": 200,
 "r": 0.07,
 "T": 3.0,
 "shapes": [
  0,
  1.0
 ],
 "reps": 2000
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
