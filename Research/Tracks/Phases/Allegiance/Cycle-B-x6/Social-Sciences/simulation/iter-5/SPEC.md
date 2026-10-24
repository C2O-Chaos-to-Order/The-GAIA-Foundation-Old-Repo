# SIM-AL-SOC-B - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Fusion loop with slower decay of deviance (gamma 0.1): same threshold in R?

## Phase operationalization tested
SOC Allegiance = fusion loop sensitivity.

## Sources this run draws on
P48 (read in full in AL0): labelling loop.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | see SPEC |
| H1 | hypothesis | threshold behaviour as AL0 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Hypothetical toy.Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Existing kind; no new smoke test.

## Parameters
```json
{
 "sim_id": "SIM-AL-SOC-B",
 "iteration": 5,
 "kind": "fusion_loop",
 "seed": 26305,
 "beta": 0.5,
 "gamma": 0.1,
 "delta": 0.05,
 "dt": 0.01,
 "kappas": [
  0.004,
  0.02,
  0.04
 ],
 "T": 6000,
 "a": 1.0,
 "F0": 0.01,
 "D0": 0.0,
 "h1_text": "fused state above 0.4 when R >= 2, below 0.01 when R < 1",
 "h1_expr": "all((v['F_end'] > 0.4) if v['R'] >= 2 else (v['F_end'] < 0.01) for v in o.values() if v['R'] >= 2 or v['R'] < 1)"
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
