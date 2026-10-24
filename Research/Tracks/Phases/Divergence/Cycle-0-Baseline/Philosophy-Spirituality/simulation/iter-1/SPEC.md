# SIM-DV-PHI-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence as 'one becoming many': formal properties of a branching process that starts from a single group.

## Phase operationalization tested
PHI Divergence = differentiation from a common source (Bergson's 'principle of divergence and differentiation', P08; Plotinian procession from the One, P07) - here only its formal skeleton.

## Sources this run draws on
P07 (SEP 'Plotinus': emanation, theory of the two activities); P08 (SEP 'Henri Bergson': principle of divergence and differentiation; diverging tendencies).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean K within 5% of analytic |
| H1 | hypothesis | largest-branch share > 0.3 |
| R1 | reporting | entropy, alpha ln n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
A Chinese restaurant process models neither Plotinus nor Bergson; it shows only what a formal 'single source, many branches' structure does. Any reading of it as metaphysics is metaphor (PS).

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-0",
 "iteration": 1,
 "kind": "crp_one_many",
 "seed": 1506,
 "alpha": 1.0,
 "n": 1000,
 "reps": 300,
 "h1": 0.3
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
