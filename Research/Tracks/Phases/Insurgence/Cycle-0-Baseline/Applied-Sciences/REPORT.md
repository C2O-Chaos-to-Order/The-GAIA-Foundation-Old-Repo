# Insurgence in the Applied Sciences — Cycle-0-Baseline (IN0)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: insurgence as outbreak emergence above R0 = 1 (P26), with P26's cautions that R0 is not a rate or a constant; a branching model shows many introductions fail even above 1.

## Claims (ledger: `claims/claims.csv`)
- **IN0-APP-01** [E] R0, the expected number of secondary cases one case produces in a completely susceptible population, is usually read as a threshold (an outbreak continues if R0 > 1 and ends if R0 < 1), but it is not a biological constant, not a rate (it says nothing about how fast cases appear), not a measure of severity, and vaccination lowers the effective reproduction number R, not R0; reported values vary widely (measles 3.7-203.3 in one review) and some are obsolete. *Operationalization:* APP Insurgence = emergence of an outbreak when cases more than replace themselves. *Sources:* P26. *Limits:* Perspective article; the figures are P26's citations.
- **IN0-APP-02** [P] In a branching model of one introduced case, no outbreak reached 1,000 cases at R0 = 0.8; at R0 = 1.5 and 3 major outbreaks occurred in 58.1% and 94.1% of 20,000 runs (theory 58.3%, 94.0%), so even above the threshold many introductions die out. Changing the generation time from 3 to 15 days left the outbreak probability unchanged and stretched the time to 1,000 cases five-fold (44 vs 219 days at R0 = 1.5), illustrating P26's point that R0 is not a rate. *Operationalization:* APP Insurgence = outbreak emergence above R0 = 1. *Sources:* SIM-IN-APP-0/iter-1#V1;SIM-IN-APP-0/iter-1#H1;SIM-IN-APP-0/iter-1#H2. *Limits:* Homogeneous Poisson offspring; fully susceptible population.

## Simulations (SIM-IN-APP-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 2/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `0b9df5b2` | P26's threshold reading (an outbreak continues if R0 > 1 and ends if R0 < 1) in a branching-process model: share of major outbreaks (1000 cases) for R0 = 0.8, 1.5, 3 vs 1 - q, and P26's point that R0 is not a rate (same R0, generation time 3 vs 15 days). | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Outbreak emergence and the limits of R0 sourced (IN0-APP-01); branching-process check (IN0-APP-02).

## Unresolved
- Heterogeneous transmission (superspreading) not modelled.
- Emergence in engineering (cascading failure) unsourced.
