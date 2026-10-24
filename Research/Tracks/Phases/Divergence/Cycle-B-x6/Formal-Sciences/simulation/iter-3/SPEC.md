# SIM-DV-FOR-B - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P09's counterexample: x -> 1.1 x has a positive Lyapunov exponent but is not chaotic (unbounded, no folding); compare with the logistic map at r = 4.

## Phase operationalization tested
FOR Divergence = exponential separation of nearby trajectories (Chaos_lambda) vs chaos requiring boundedness and stretching-and-folding (P09).

## Sources this run draws on
P09 (Bishop, SEP 'Chaos', re-read in full in DVB): the Kellert counterexample x_{n+1} = 1.1 x_n; stretching and folding 'cause some trajectories to converge rapidly while causing others to diverge rapidly'.

## Refinement from previous iteration
New run family (DV0 tested the logistic exponent only).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | linear exponent = ln 1.1 (1e-12) |
| V2 | validation | logistic exponent within 0.01 of ln 2 |
| V3 | validation | logistic orbit in [0,1] |
| H1 | hypothesis | logistic local shrink share > 0.1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
One-dimensional maps only. Pairs are renormalised to stay local after separation exceeds 1e-3. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself (two-sided; false-alarm probability about 6e-5 per check under a correct implementation); deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; thresholds were not changed after the smoke test.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-B",
 "iteration": 3,
 "kind": "linear_vs_chaotic",
 "seed": 16203,
 "c": 1.1,
 "n": 100000,
 "pairs": 1000,
 "d0": 1e-09,
 "steps": 1000,
 "h1": 0.1
}
```

## Command
`python sim_for.py iter-3` (run from `Formal-Sciences/simulation/`)
