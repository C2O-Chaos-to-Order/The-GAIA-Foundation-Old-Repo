# SIM-IN-PHI-B - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Abrupt loss of perceived utility (the case P30 excludes): a stance growing from 1% with u = 0.65 loses utility (u = 0.4) at t = 10; does it then die out (< 5%) by t = 60?

## Phase operationalization tested
PHI Insurgence = a rising hope or stance reversed by a shock (read against P35's account).

## Sources this run draws on
P30 (read in full in INA): Eq. 1 and its a = 1 logistic case; P30 notes abrupt utility changes are not in its model. P35 (van der Hoek 2023, Int J Lat Am Relig, CC BY; read in full in INB) for the historical case of a prophetic hope abandoned after news of the 1906 earthquake.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | x in [0, 1] |
| H1 | hypothesis | below 0.05 by t = 60 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Deterministic toy; P35 describes a historical case, not a model. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-PHI-B",
 "iteration": 1,
 "kind": "abrams_groups",
 "seed": 21601,
 "mode": "shock",
 "c": 1.0,
 "u": 0.65,
 "u_after": 0.4,
 "x0": 0.01,
 "t_shock": 10,
 "dt": 0.01,
 "tmax": 60,
 "h1": 0.05
}
```

## Command
`python sim_phi.py iter-1` (run from `Philosophy-Spirituality/simulation/`)
