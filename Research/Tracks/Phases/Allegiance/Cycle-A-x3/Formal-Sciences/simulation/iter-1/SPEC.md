# SIM-AL-FOR-A - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
1/3 rule at larger N and weaker selection (N = 1000, s = 0.00005, w = 0.5): does the crossing of rho = 1/N move to within 5% of P47's AD threshold 4?

## Phase operationalization tested
FOR Allegiance = cooperation thresholds in finite populations.

## Sources this run draws on
P47 (Nowak 2006, read in full in AL0): direct reciprocity matrix, AD threshold (3 - 2w)/w, '1/3 rule' in the limit of weak selection. Moran formula and its weak-selection crossing (N - 2)a + (2N - 1)b > (N + 1)c + (2N - 4)d are standard theory from the agent's knowledge, not from a source read in this track.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | rho below/above 1/N at b/c 3.5/4.5 |
| H2 | hypothesis | crossing within 5% of 4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Foreknowledge by reasoning (not smoke): the agent's weak-selection condition gives a crossing at b/c = (4N - 5)/(N - 5) for w = 0.5 (4.016 at N = 1000, 4.158 at N = 100) and (7N - 11)/(4N - 11) = 1.752 for w = 0.8, N = 1000, so H2 was expected to be supported in all three runs; AL0's failure at N = 100 used N s = 0.5, not weak selection. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-FOR-A",
 "iteration": 1,
 "kind": "coop_rules",
 "seed": 25201,
 "w": 0.5,
 "q": 0.5,
 "r": 0.5,
 "k": 4,
 "n": 10,
 "m": 20,
 "N": 1000,
 "s_sel": 5e-05,
 "bc_values": [
  3.5,
  4.5
 ],
 "N_sim": 20,
 "bc_sim": 6.0,
 "reps": 20000
}
```

## Command
`python sim_for.py iter-1` (run from `Formal-Sciences/simulation/`)
