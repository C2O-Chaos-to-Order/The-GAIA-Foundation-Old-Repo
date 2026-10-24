# SIM-AL-FOR-B - iteration 4 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
N = 500 with N s = 0.05: is the crossing within 5%?

## Phase operationalization tested
FOR Allegiance = 1/3 rule in finite populations.

## Sources this run draws on
P47 (Nowak 2006, read in full in AL0): direct reciprocity matrix and AD threshold (3 - 2w)/w; 1/3 rule in the limit of weak selection. Weak-selection crossing (4N - 5)/(N - 5) for w = 0.5 is the agent's derivation (standard theory, not sourced).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | rho below/above 1/N at the ends of the b/c range |
| H2 | hypothesis | crossing within 5% of the AD threshold |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Expected supported.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-FOR-B",
 "iteration": 4,
 "kind": "coop_rules",
 "seed": 26204,
 "q": 0.5,
 "r": 0.5,
 "k": 4,
 "n": 10,
 "m": 20,
 "N_sim": 20,
 "bc_sim": 6.0,
 "reps": 20000,
 "w": 0.5,
 "N": 500,
 "s_sel": 0.0001,
 "bc_values": [
  3.5,
  4.5
 ]
}
```

## Command
`python sim_for.py iter-4` (run from `Formal-Sciences/simulation/`)
