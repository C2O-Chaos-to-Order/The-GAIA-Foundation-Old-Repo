# SIM-DV-APP-D - iteration 2 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
P24's fluency-dependency: if fluency and true originality are unrelated, does a summative originality score still correlate with fluency above 0.8, and does the average score become less reliable for low-fluency people?

## Phase operationalization tested
APP Divergence = divergent thinking, the generation of many ideas to an open-ended problem, measured by fluency, originality and flexibility (P24); its scores are design-process measures.

## Sources this run draws on
P24 (Barbot 2018, 'The Dynamics of Creative Ideation: Introducing a New Assessment Paradigm', Frontiers in Psychology 9:2529, CC BY; read in full in DVD). Section 'Response Quality and Fluency-Dependency'.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | corr(average, fluency) within 4 SE (+0.02) of corr(mu, fluency) |
| H1 | hypothesis | corr(summative, fluency) > 0.8 (the range P24 reports, citing Said-Metwaly et al. 2017) |
| H2 | hypothesis | average score tracks true originality worse in the low-fluency half |
| R1 | reporting | correlations |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Agent's toy; uncommonness is a logistic score, persons independent, no raters. The 0.8 threshold is P24's reported range. Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-APP-D",
 "iteration": 2,
 "kind": "fluency_confound",
 "seed": 18402,
 "n": 500,
 "reps": 40,
 "rho": 0.0,
 "lam_mean": 12,
 "sdlog": 0.4,
 "sd_mu": 0.5,
 "sd_item": 1.0,
 "tol_se": 4,
 "h1": 0.8
}
```

## Command
`python sim_app.py iter-2` (run from `Applied-Sciences/simulation/`)
