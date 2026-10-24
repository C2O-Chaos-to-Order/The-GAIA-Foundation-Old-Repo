# SIM-AL-SOC-A - iteration 3 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Fusion loop just around the threshold (R = 0.9, 1.1, 1.5): does a small fused state (F* = 0.09 at R = 1.1) appear just above R = 1 and vanish just below?

## Phase operationalization tested
SOC Allegiance = threshold of the fusion loop.

## Sources this run draws on
P48 (read in full in AL0): labelling loop.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | F_end > 0.05 for R > 1 and < 0.01 for R < 1 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy; convergence near R = 1 is slow (T = 6000).Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind (smoke-tested in AL0); no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-A",
 "iteration": 3,
 "kind": "fusion_loop",
 "seed": 25303,
 "a": 1.0,
 "beta": 0.5,
 "gamma": 0.5,
 "delta": 0.05,
 "dt": 0.01,
 "kappas": [
  0.045,
  0.055,
  0.075
 ],
 "F0": 0.01,
 "D0": 0.0,
 "T": 6000,
 "h1_text": "fused state above 0.05 when R > 1, below 0.01 when R < 1",
 "h1_expr": "all((v['F_end'] > 0.05) if v['R'] > 1 else (v['F_end'] < 0.01) for v in o.values())"
}
```

## Command
`python sim_soc.py iter-3` (run from `Social-Sciences/simulation/`)
