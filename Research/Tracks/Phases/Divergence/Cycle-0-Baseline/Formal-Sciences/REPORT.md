# Divergence in the Formal Sciences — Cycle-0-Baseline (DV0)

Phase report: Divergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
In the formal sciences 'divergence' is polysemous; the trajectory sense is precisely defined but is only one of several competing definitions of chaos.

## Claims (ledger: `claims/claims.csv`)
- **DV0-FOR-01** [E] In dynamical-systems usage, the global Lyapunov exponent is taken to represent the average rate of divergence of neighbouring trajectories, and the most popular candidate definition of chaos (Chaos_lambda) is a positive global Lyapunov exponent. *Operationalization:* Divergence = exponential separation of nearby trajectories. *Sources:* P09. *Limits:* P09 also reports objections: Lyapunov exponents are asymptotic quantities and Chaos_lambda is one of several definitions.
- **DV0-FOR-02** [E] There is no consensus on a precise definition of chaotic behaviour: mathematicians often prefer one definition and scientists another, so 'divergence of trajectories' is one operationalization among competitors, not the definition of chaos. *Operationalization:* Competing definitions of chaos (sensitive dependence vs topological definitions). *Sources:* P09. *Limits:* Reference-work summary of the debate.
- **DV0-FOR-03** [P] For the logistic map the computed Lyapunov exponent at r = 4 was 0.69313 (ln 2 = 0.69315) and negative at r = 3.2; two orbits started 1e-10 apart at r = 4 separated beyond 0.1 after a median 31 steps, close to the predicted ln(1e9)/ln 2 = 29.9. *Operationalization:* Divergence = trajectory separation rate. *Sources:* SIM-DV-FOR-0/iter-1#V1;SIM-DV-FOR-0/iter-1#V2;SIM-DV-FOR-0/iter-1#H1. *Limits:* Code and analytic check of a textbook map; it shows what 'trajectory divergence' means formally and nothing about any physical or social system.

## Simulations (SIM-DV-FOR-0; 1 iteration(s), spec-first; validation 2/2, hypotheses supported 1/1)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `d31ceb59` | Divergence as separation of nearby trajectories: check the Lyapunov exponent of the logistic map and the predicted separation time. | V1 Pass; V2 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: P09 fixes the trajectory sense of divergence (Lyapunov exponent) and documents that chaos has no agreed definition. The arXiv API timed out for these queries (logged); PMC hits were applied EEG/heart-rate papers, not used. Other formal senses (divergent series, the divergence operator, statistical divergences such as Kullback-Leibler) are recorded in DEFINITIONS.md as not yet sourced.

## Unresolved
- Series divergence, the divergence operator and statistical divergences are listed but unsourced.
- Whether 'divergence' has any common formal core across these senses is open.
