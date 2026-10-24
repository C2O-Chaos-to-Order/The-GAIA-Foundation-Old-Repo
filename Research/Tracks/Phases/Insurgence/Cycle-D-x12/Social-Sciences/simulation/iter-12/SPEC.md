# SIM-IN-SOC-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Replication of INC-SOC iter-6 on a new seed (x12 replication pass; adds no new source).

## Phase operationalization tested
SOC Insurgence = an armed conflict growing from its first year to a large war by escalation (P39).

## Sources this run draws on
P39 (Clauset, Walter, Cederman & Gleditsch 2026, Sci Adv 12:eaeb1705, CC BY-NC 4.0; read in full in INC): Eq. 2 model, alpha = 2.1, q_hat = 0.47, x_min = 1000, Richardson alpha_hat = 1.53 for x >= 7061; 44% of civil-war escalation factors are 1; 'roughly a 10% ex ante risk of a doubling ... about a 1% risk of increasing by an order of magnitude'. Double Pareto form and clamping are the agent's readings (P39's SI not read).

## Refinement from previous iteration
Iteration 12 of the x12 family for SOC; follows iteration 11 (see Purpose).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | sim vs analytic |
| H1 | hypothesis | density reading |
| H2 | hypothesis | CCDF reading |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Replication or variant of an earlier run (new seed); no new source. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-IN-SOC-D",
 "iteration": 12,
 "kind": "escalation_war",
 "seed": 23312,
 "mode": "exante",
 "q0": 0.44,
 "n": 1000000
}
```

## Command
`python sim_soc.py iter-12` (run from `Social-Sciences/simulation/`)
