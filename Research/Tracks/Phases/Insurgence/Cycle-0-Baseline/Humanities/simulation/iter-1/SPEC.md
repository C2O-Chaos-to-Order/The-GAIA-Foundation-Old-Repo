# SIM-IN-HUM-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P21 reports a rap-enriched style that 'is very rare before the mid-1980s but then rapidly expands'. In a Wright-Fisher toy (N = 1000 songs, advantage s = 0.05), how often does a new style entering at one copy take over, and is a successful takeover S-shaped?

## Phase operationalization tested
HUM Insurgence = a rare new style rising to dominance (P21's style 2).

## Sources this run draws on
P21 (Mauch et al. 2015, R. Soc. Open Sci., CC BY; read in full in DVC). Kimura's fixation formula and the logistic are standard (not from P21).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | fixation share within 4 SE of Kimura |
| H1 | hypothesis | fixation share < 0.5 |
| H2 | hypothesis | 10%-90% time within 15% of logistic |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's toy; P21 gives frequencies, not a mechanism; s and N are not estimates. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-IN-HUM-0",
 "iteration": 1,
 "kind": "insurgent_style",
 "seed": 19501,
 "N": 1000,
 "s": 0.05,
 "reps": 4000,
 "tmax": 20000,
 "tol_se": 4,
 "h1": 0.5,
 "h2": 0.15
}
```

## Command
`python sim_hum.py iter-1` (run from `Humanities/simulation/`)
