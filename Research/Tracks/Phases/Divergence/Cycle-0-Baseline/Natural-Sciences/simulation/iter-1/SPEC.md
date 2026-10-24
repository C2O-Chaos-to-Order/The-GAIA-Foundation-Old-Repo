# SIM-DV-NAT-0 - iteration 1 SPEC

Written before execution. The parameters are the JSON block below (hashed as `params_sha256` in EXECUTION_RECORD.json; this file's bytes as `spec_sha256`).

## Purpose
Divergence as population differentiation: do two demes diverge (Fst rises) under drift alone, and does gene flow hold divergence back?

## Phase operationalization tested
NAT Divergence = genetic differentiation between populations (Fst), the population-genetic face of 'divergence with gene flow' (P01).

## Sources this run draws on
P01 (divergence with gene flow across a Heliconius speciation continuum; genomic divergence increases with ecological and reproductive isolation).

## Refinement from previous iteration
First iteration of this run family in this cycle.

## Pre-registered checks
| id | kind | expectation |
|---|---|---|
| V1 | validation | m = 0: heterozygosity ratio within 10% of (1-1/2N)^t |
| H1 | hypothesis | m = 0: Fst at t=200 > 0.25 |
| H2 | hypothesis | Nm = 1: Fst at t=200 < 0.2 |
| R1 | reporting | 1/(1+4Nm) reference |

Kinds: *validation* = code/analytic correctness (must Pass); *hypothesis* = substantive test that may go either way (Supported / Not supported; 'Not supported' is a finding, not an error); *reporting* = value recorded.

## Limits
Neutral loci, two demes, no selection, no linkage: the model cannot represent the selected colour-pattern locus or genomic islands in P01. H1 threshold 0.25 is the conventional 'very great differentiation' benchmark (not taken from a source read in this cycle); it replaced 0.5 after the pre-spec smoke test showed 0.5 exceeds what the two-deme (HT-HS)/HT statistic reaches at t = N (disclosed).

## Parameters
```json
{
 "sim_id": "SIM-DV-NAT-0",
 "iteration": 1,
 "kind": "wf_divergence",
 "seed": 1501,
 "N": 100,
 "loci": 400,
 "generations": 200,
 "m": 0.01,
 "checkpoints": [
  10,
  50,
  100,
  200
 ],
 "h2": 0.2,
 "h1": 0.25
}
```

## Command
`python sim_nat.py iter-1` (run from `Natural-Sciences/simulation/`)
