# SIM-DV-FOR-D - iteration 12 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
KL check with a peaked q (Dirichlet concentration 0.2).

## Phase operationalization tested
FOR Divergence = statistical divergence D(p||q) (P16).

## Sources this run draws on
P16 (Shlens 2014; read in full in DVB).

## Refinement from previous iteration
Derived from SIM-DV-FOR-C iteration 6: only conc and seed change.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | LR rate within 4 SE of D at every n |
| H1 | hypothesis | within 0.01 nats at n = 1e5 |
| H2 | hypothesis | error decreases with n |
| R1 | reporting | by n |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
As DVB. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds.

## Parameters
```json
{
 "sim_id": "SIM-DV-FOR-D",
 "iteration": 12,
 "kind": "kl_likelihood",
 "seed": 18212,
 "K": 10,
 "conc": 0.2,
 "n_values": [
  100,
  1000,
  10000,
  100000
 ],
 "reps": 200,
 "tol_se": 4,
 "h1": 0.01
}
```

## Command
`python sim_for.py iter-12` (run from `Formal-Sciences/simulation/`)
