# Divergence in the Social Sciences — Cycle-0-Baseline (DV0)

Phase report: Divergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
In social science, divergence appears as fragmentation and polarisation; the evidence read here is model-based, so labels stay at E (about models) or P.

## Claims (ledger: `claims/claims.csv`)
- **DV0-SOC-01** [E] In opinion-dynamics models, bounded assimilative influence (only individuals with similar opinions influence each other) makes opinions fragment into two or more converging clusters, while adding noise broadens the distribution again. *Operationalization:* Divergence = fragmentation of a population into opinion clusters. *Sources:* P03. *Limits:* Describes model behaviour, not observed societies.
- **DV0-SOC-02** [P] Condie and Condie propose, with an agent-based bounded-confidence model, that stochastic external events can sustain polarisation even when all interpersonal interactions are noisy and assimilative, because events act on much of the population at once. *Operationalization:* Divergence = persistent polarisation driven by shared external events. *Sources:* P03. *Limits:* A model-based possibility proof; empirical calibration against real opinion data is limited.
- **DV0-SOC-03** [P] In a noise-free Deffuant model (500 agents), confidence bound 0.5 gave consensus in 10/10 replicates and bound 0.15 gave three major clusters in 10/10, with the mean opinion conserved exactly. *Operationalization:* Divergence = number of separated opinion clusters. *Sources:* SIM-DV-SOC-0/iter-1#V1;SIM-DV-SOC-0/iter-1#H1;SIM-DV-SOC-0/iter-1#H2. *Limits:* No network, no events, no noise; cluster counting rule is a convention.

## Simulations (SIM-DV-SOC-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 2/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `855b6b26` | Divergence as opinion fragmentation: does bounded confidence split a population into several clusters while wide confidence yields consensus? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: P03 gives the model taxonomy (assimilative, bounded, noisy, differentiative influence) and an event-driven polarisation mechanism.

## Unresolved
- P03's event-driven mechanism is not yet simulated.
- No empirical polarisation data read.
