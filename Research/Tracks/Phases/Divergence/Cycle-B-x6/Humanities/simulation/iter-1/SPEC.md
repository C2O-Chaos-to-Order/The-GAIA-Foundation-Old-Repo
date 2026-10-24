# SIM-DV-HUM-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P06 found four of six Andic classifications significantly correlated with geography (permutation statistics 0-0.046; the two Swadesh-list classifications 0.088 and 0.116). With eight tips, how much power does a tree-geography permutation test have when geography does follow the tree?

## Phase operationalization tested
HUM Divergence = language-family divergence reflected in geography (P06's 'bombshell' picture), and the statistical power to detect it.

## Sources this run draws on
P06 (re-read in full in DVB): permutation statistics 0 to 0.116 across six classifications; 'the more assumedly precise the classification is ..., the lower the correlation'. Test design is the agent's (Mantel-type), not P06's exact statistic.

## Refinement from previous iteration
New run family.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | null rejection rate <= alpha + 4 SE |
| H1 | hypothesis | power >= 0.8 |
| R1 | reporting | power, null rate |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Balanced trees with equal branch lengths; P06's trees are not balanced and its statistic differs. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-HUM-B",
 "iteration": 1,
 "kind": "geo_tree_mantel",
 "seed": 16501,
 "depth": 3,
 "L0": 1.0,
 "noise": 0.5,
 "perms": 999,
 "reps": 400,
 "alpha": 0.05,
 "tol_se": 4,
 "h1": 0.8
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
