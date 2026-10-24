# SIM-AL-FOR-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P47's five rules for the evolution of cooperation: do the ESS/RD/AD thresholds computed from Table 1's payoff matrices equal the printed rules, and does the '1/3 rule' (advantageous strategy => fixation probability above 1/N) hold for tit-for-tat vs always-defect in a Moran process (N = 100, weak selection 0.005, w = 0.5, AD threshold b/c = 4)?

## Phase operationalization tested
FOR Allegiance = cooperation stabilised by a mechanism (repetition, reputation, networks, kinship, groups): individuals forgo payoff for one another (P47).

## Sources this run draws on
P47 (Nowak 2006, Science 314:1560-1563, NIH author manuscript PMC3279745; read in full in AL0, SOM not read): Eqs. 1-5, Table 1, ESS/RD/AD definitions and the 1/3 rule 'in the limit of weak selection'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | rho below/above 1/N at b/c 3.5/4.5 |
| H2 | hypothesis | finite-N crossing within 5% of 4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
The Moran fixation formula and fitness 1 - s + s * payoff are standard theory (agent's knowledge, not in P47). Smoke foreknowledge: thresholds matched exactly; the finite-N crossing was 4.23 (H2 expected not supported; kept as pre-registered to document the finite-N gap). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-FOR-0",
 "iteration": 1,
 "kind": "coop_rules",
 "seed": 24201,
 "w": 0.5,
 "q": 0.5,
 "r": 0.5,
 "k": 4,
 "n": 10,
 "m": 20,
 "N": 100,
 "s_sel": 0.005,
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
