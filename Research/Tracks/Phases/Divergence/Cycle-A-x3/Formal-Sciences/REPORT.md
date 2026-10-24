# Divergence in the Formal Sciences — Cycle-A-x3 (DVA)

Phase report: Divergence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3 checked three more formal senses (statistical, series, operator) by computation; none was sourced, so FOR gains only Plausible simulation claims and an open question on whether the senses share a core.

## Claims (ledger: `claims/claims.csv`)
- **DVA-FOR-01** [E] In dynamical-systems usage, the global Lyapunov exponent is taken to represent the average rate of divergence of neighbouring trajectories, and the most popular candidate definition of chaos (Chaos_lambda) is a positive global Lyapunov exponent. *Operationalization:* Divergence = exponential separation of nearby trajectories. *Sources:* P09. *Limits:* P09 also reports objections: Lyapunov exponents are asymptotic quantities and Chaos_lambda is one of several definitions.
- **DVA-FOR-02** [E] There is no consensus on a precise definition of chaotic behaviour: mathematicians often prefer one definition and scientists another, so 'divergence of trajectories' is one operationalization among competitors, not the definition of chaos. *Operationalization:* Competing definitions of chaos (sensitive dependence vs topological definitions). *Sources:* P09. *Limits:* Reference-work summary of the debate.
- **DVA-FOR-03** [P] For the logistic map the computed Lyapunov exponent at r = 4 was 0.69313 (ln 2 = 0.69315) and negative at r = 3.2; two orbits started 1e-10 apart at r = 4 separated beyond 0.1 after a median 31 steps, close to the predicted ln(1e9)/ln 2 = 29.9. *Operationalization:* Divergence = trajectory separation rate. *Sources:* SIM-DV-FOR-0/iter-1#V1;SIM-DV-FOR-0/iter-1#V2;SIM-DV-FOR-0/iter-1#H1. *Limits:* Code and analytic check of a textbook map; it shows what 'trajectory divergence' means formally and nothing about any physical or social system.
- **DVA-FOR-04** [P] For 1,000 random pairs of distributions on 10 points, Kullback-Leibler divergence was never negative, was zero for identical distributions, matched its Monte Carlo estimate within 4 standard errors in 50 of 50 pairs, and was asymmetric (median relative difference between D(p||q) and D(q||p) 0.20). *Operationalization:* Divergence = asymmetric statistical dissimilarity (not a distance). *Sources:* SIM-DV-FOR-A/iter-1#V1;SIM-DV-FOR-A/iter-1#V2;SIM-DV-FOR-A/iter-1#V3;SIM-DV-FOR-A/iter-1#H1. *Limits:* Code and analytic check only; no source on KL divergence was read in this track, so no Established claim is made about its literature.
- **DVA-FOR-05** [P] Harmonic partial sums tracked ln n + gamma within 1/(2n) up to n = 100,000 and first exceeded 10 only at n = 12,367, while the p = 2 and alternating harmonic series converged within their bounds: a divergent series can grow extremely slowly. *Operationalization:* Divergence = partial sums without a finite limit. *Sources:* SIM-DV-FOR-A/iter-2#V1;SIM-DV-FOR-A/iter-2#V2;SIM-DV-FOR-A/iter-2#V3;SIM-DV-FOR-A/iter-2#H1. *Limits:* Deterministic floating-point check of standard results; H1 was predictable from general knowledge.
- **DVA-FOR-06** [P] For F = (x^3 + y, x y^2, z x^2) on the unit cube, a finite-difference divergence matched the analytic one to 1e-8, and the Monte Carlo volume integral of div F (1.8380, SE 0.0034) matched the outward flux 11/6 = 1.8333, as the divergence theorem requires. *Operationalization:* Divergence = net outflow per unit volume (div F). *Sources:* SIM-DV-FOR-A/iter-3#V1;SIM-DV-FOR-A/iter-3#V2. *Limits:* One polynomial field; a code check of the operator sense only.
- **DVA-FOR-07** [H] The formal senses now covered (separation of trajectories, partial sums without a limit, asymmetric statistical dissimilarity, net outflow of a field) share a word, not a definition; this cycle found no common formal criterion that would make them one concept. *Operationalization:* Competing formal definitions of divergence. *Sources:* SIM-DV-FOR-A/iter-1#H1;SIM-DV-FOR-A/iter-2#H1. *Limits:* Absence of a common core in four examples is not proof that none exists; no source on the history of the term was read.

## Simulations (SIM-DV-FOR-A; 3 iteration(s), spec-first; validation 8/8, hypotheses supported 2/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `679c8afc` | Divergence as an asymmetric statistical dissimilarity: check non-negativity, zero self-divergence, a Monte Carlo estimator, and asymmetry of Kullback-Leibler divergence. | V1 Pass; V2 Pass; V3 Pass; H1 Supported; R1 Reported |
| 2 | `d0d06dad` | Divergence of a series: harmonic partial sums grow without bound (like ln n) while p = 2 and alternating harmonic series converge. | V1 Pass; V2 Pass; V3 Pass; H1 Supported; R1 Reported |
| 3 | `01c4d607` | The divergence operator: finite-difference divergence vs analytic, and the divergence theorem (volume integral of div F = outward flux) by Monte Carlo. | V1 Pass; V2 Pass; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: Added nothing: PMC hits were specialised applications or long (13,000-22,000-word) technical papers; arXiv timed out again. No KL source read, so the KL run supports only simulation claims.
- Pass 2: Added nothing: no expository text found; results were unrelated (e.g. molecular biology).
- Pass 3: Added nothing: series and operator senses were checked by simulation only (standard analytic results); no source read.

## Unresolved
- No source read for the series, operator or statistical senses; FOR has no new Established claim.
- Whether any common formal core exists remains open (DVA-FOR-07).
