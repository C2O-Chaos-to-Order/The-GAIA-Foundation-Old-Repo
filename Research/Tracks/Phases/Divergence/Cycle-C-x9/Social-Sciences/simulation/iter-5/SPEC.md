# SIM-DV-SOC-C - iteration 5 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Recompute P19's printed richest/poorest ratios from P19's own printed levels (Table 2: USA 2063, 9895, 18054; poorest 250, 257, 399; printed ratios 8.7, 38.5, 45.2) and the US growth factor 1870-1960 ('about four-fold').

## Phase operationalization tested
SOC Divergence = ratio of richest to poorest incomes (P19).

## Sources this run draws on
P19 (read in full): Table 2, Figure 1 and text. The arithmetic is a consistency check of the printed numbers, not of Maddison's or the Penn World Tables' data.

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | arithmetic reproducible |
| H1 | hypothesis | all printed ratios within 0.1 |
| H2 | hypothesis | US factor within 0.5 of 4 |
| R1 | reporting | values |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Text extracted by pdftotext from a scanned JSTOR PDF; digits read from the converted table could be misaligned (checked against the Figure 1 inset, which prints 8.7 / 38.5 / 45.2 too). Statistical tolerance (owner standard, set before running): Monte Carlo validation checks use a band of 4 standard errors computed from the run itself; deterministic checks use explicit numerical bounds. New kind smoke-tested once at reduced size (seed 99, temporary directory, nothing kept) before this SPEC was written; the smoke test showed some outcomes in advance (disclosed); thresholds were not changed after it.

## Parameters
```json
{
 "sim_id": "SIM-DV-SOC-C",
 "iteration": 5,
 "kind": "pritchett_arithmetic",
 "seed": 17305,
 "rows": {
  "1870": [
   2063,
   250,
   8.7
  ],
  "1960": [
   9895,
   257,
   38.5
  ],
  "1990": [
   18054,
   399,
   45.2
  ]
 },
 "tol": 0.1,
 "us_growth": [
  2063,
  9895
 ]
}
```

## Command
`python sim_soc.py iter-5` (run from `Social-Sciences/simulation/`)
