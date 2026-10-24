# SIM-IN-PHI-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
A toy of continuing creation of new forms (read against Bergson's vital impulse, P08): in a Chinese-restaurant process (alpha 5), do new forms keep appearing between 1,000 and 100,000 draws while their rate falls?

## Phase operationalization tested
PHI Insurgence = the upsurge of the new from a common impulse (Bergson's élan vital, P08; interpretive).

## Sources this run draws on
P08 (SEP 'Henri Bergson', read in full in DVB): 'an original common impulse which explains the creation of all living species'. The CRP is the agent's formal stand-in, not Bergson's.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | means within 4 SE of the analytic sum |
| H1 | hypothesis | more forms at 100,000 than 1,000 |
| H2 | hypothesis | final rate < 0.01 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Interpretive toy; Bergson's thesis is metaphysical and is not tested by a stochastic process. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-0",
 "iteration": 1,
 "kind": "novelty_stream",
 "seed": 19601,
 "alpha": 5.0,
 "n_values": [
  1000,
  10000,
  100000
 ],
 "reps": 200,
 "tol_se": 4,
 "h2": 0.01
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
