# SIM-AL-SOC-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P48's labelling loop as a toy: if condemnation of deviance raises fusion with a deviant group and fusion raises deviance, is there a threshold (loop gain R = 1) above which a fused state 1 - 1/R persists, and does lowering stigma below it dissolve the state?

## Phase operationalization tested
SOC Allegiance = identity fusion: a visceral, hard-to-revoke oneness of personal and group identity that motivates costly pro-group action (P48).

## Sources this run draws on
P48 (Newson, Cunliffe & Whitehouse 2025, Theory and Society 54:651-670, CC BY 4.0; read in full in AL0): definition and four principles of identity fusion; labelling-theory loop 'external condemnation amplifies fusion to a deviant group'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | F_end > 0.4 for R >= 2 and < 0.01 for R < 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical: the equations are the agent's formalization of a verbal argument in P48; parameter values are arbitrary. Smoke foreknowledge: F_end 0, 0.5, 0.75 for R = 0.4, 2, 4. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-0",
 "iteration": 1,
 "kind": "fusion_loop",
 "seed": 24301,
 "a": 1.0,
 "beta": 0.5,
 "gamma": 0.5,
 "delta": 0.05,
 "dt": 0.01,
 "kappas": [
  0.02,
  0.1,
  0.2
 ],
 "F0": 0.01,
 "D0": 0.0,
 "T": 3000,
 "h1_text": "fused state above 0.4 when R >= 2, below 0.01 when R < 1",
 "h1_expr": "all((v['F_end'] > 0.4) if v['R'] >= 2 else (v['F_end'] < 0.01) for v in o.values() if v['R'] >= 2 or v['R'] < 1)"
}
```

## Command
`python sim_soc.py iter-1` (run from `Social-Sciences/simulation/`)
