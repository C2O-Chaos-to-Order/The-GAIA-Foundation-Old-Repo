# SIM-DV-PHI-D - iteration 9 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Seed replication of the CRP one-to-many run.

## Phase operationalization tested
PHI Divergence = differentiation from a single source (formal).

## Sources this run draws on
P07, P08 (DVB); P18 (read in full in DVC; ch. 42 'One gives birth to Two').

## Refinement from previous iteration
Derived from SIM-DV-PHI-C iteration 6: seed replication (only the seed changes).

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | mean K within 4 SE per alpha |
| H1 | hypothesis | largest-branch share > 0.3 |
| R1 | reporting | by alpha |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Formal only. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. Replication: same parameters, new seed; the hypothesis verdicts are expected to repeat DVC's.

## Parameters
```json
{
 "sim_id": "SIM-DV-PHI-D",
 "iteration": 9,
 "kind": "crp_one_many_se",
 "seed": 18609,
 "alphas": [
  5.0,
  10.0
 ],
 "n": 1000,
 "reps": 300,
 "tol_se": 4,
 "h1": 0.3
}
```

## Command
`python sim_phi.py iter-9` (run from `Philosophy-Spirituality/simulation/`)
