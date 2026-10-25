# Transcendence in the Natural Sciences — Cycle-0-Baseline (TR0)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: transcendence as an evolutionary transition in individuality (P97); fitness decoupling is a metaphor with limits; tradeoff breaking as a proposed marker.

## Claims (ledger: `claims/claims.csv`)
- **TR0-NAT-01** [P] P97 argues that 'fitness decoupling' between particles and collectives in an evolutionary transition in individuality (ETI) is a metaphor with limits: computed commensurably over equivalent time intervals, particle and collective fitness are the same once a stable collective size distribution is reached. Instead it proposes that early stages of ETIs involve tradeoffs among particle traits and later, critical stages their rupture ('tradeoff breaking'), which could be used to detect an ETI. In its projection model the optimum for counterfactual fitness f2 is always zero investment in collective survival, while the optimum for whole-life-cycle fitness is positive. *Operationalization:* NAT Transcendence = an evolutionary transition in individuality. *Sources:* P97. *Limits:* The eLife reviewers state that the incommensurability result is not novel (Michod 2005; Shelton & Michod 2014; Bourrat 2015) and that tradeoff breaking is not sufficient as an ETI marker; P97's revision softens the claim. Notation slips: the investment trait is called theta in Section 3 and p in Section 4; the Fig. 7 caption's t1/t2 ordering conflicts with the main text.
- **TR0-NAT-02** [P] In the agent's implementation of P97's projection model (N 30 size classes, eta 8, p1 0.1, mu 0), the counterfactual f2 is maximised at theta 0 while the life-cycle growth rate F is maximised at theta* = 0.348; moving from 0 to theta* raises F from 0.512 to 0.809 and lowers f2 from 0.400 to 0.007, the pattern read as 'fitness decoupling'. Breaking the s + b = 1 tradeoff by 0.05 raises both (F 0.843, f2 0.074). Particle fitness f1 stays near 0.095 and differs from F. The particle growth rate from iterating the model equals ln(lambda) at theta* within 1e-8. *Operationalization:* NAT Transcendence = life-cycle fitness versus counterfactual fitness. *Sources:* SIM-TR-NAT-0/iter-1#V1;SIM-TR-NAT-0/iter-1#H1;SIM-TR-NAT-0/iter-1#H2;SIM-TR-NAT-0/iter-1#H3;SIM-TR-NAT-0/iter-1#H4;SIM-TR-NAT-0/iter-1#H5. *Limits:* beta_i is the agent's reading of a formula garbled in the extracted text; reproduces P97's qualitative Fig. 5 result, not its exact numbers.

## Simulations (SIM-TR-NAT-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 5/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `36a29600` | P97's projection model of a proto-multicellular life cycle (N 30, eta 8, p1 0.1, mu 0): is zero investment optimal for the counterfactual f2, is theta* > 0 for the life-cycle growth rate F, does moving from 0 to theta* raise F and lower f2, does breaking the s + b = 1 tradeoff raise both, and does particle fitness f1 differ from F? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; H5 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Fitness-decoupling critique and tradeoff breaking as an ETI model sourced, with reviewers' novelty caveat (TR0-NAT-01); f2 optimum at 0, F optimum at theta* 0.348 and tradeoff breaking raising both reproduced under the agent's reading of a garbled formula (TR0-NAT-02).

## Unresolved
- beta_i reading of P97's garbled formula unconfirmed; P97's exact Fig. 5 numbers not compared.
- Competing readings (major transitions in general, Szathmary & Maynard Smith; emergence of new levels) not yet sourced beyond P97.
