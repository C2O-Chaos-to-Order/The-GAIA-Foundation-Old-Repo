# Transcendence in the Natural Sciences — Cycle-A-x3 (TRA)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: the decoupling pattern holds at N 15 and under two parameter changes; theta* is sensitive to eta and p1.

## Claims (ledger: `claims/claims.csv`)
- **TRA-NAT-01** [P] P97 argues that 'fitness decoupling' between particles and collectives in an evolutionary transition in individuality (ETI) is a metaphor with limits: computed commensurably over equivalent time intervals, particle and collective fitness are the same once a stable collective size distribution is reached. Instead it proposes that early stages of ETIs involve tradeoffs among particle traits and later, critical stages their rupture ('tradeoff breaking'), which could be used to detect an ETI. In its projection model the optimum for counterfactual fitness f2 is always zero investment in collective survival, while the optimum for whole-life-cycle fitness is positive. *Operationalization:* NAT Transcendence = an evolutionary transition in individuality. *Sources:* P97. *Limits:* The eLife reviewers state that the incommensurability result is not novel (Michod 2005; Shelton & Michod 2014; Bourrat 2015) and that tradeoff breaking is not sufficient as an ETI marker; P97's revision softens the claim. Notation slips: the investment trait is called theta in Section 3 and p in Section 4; the Fig. 7 caption's t1/t2 ordering conflicts with the main text.
- **TRA-NAT-02** [P] In the agent's implementation of P97's projection model (N 30 size classes, eta 8, p1 0.1, mu 0), the counterfactual f2 is maximised at theta 0 while the life-cycle growth rate F is maximised at theta* = 0.348; moving from 0 to theta* raises F from 0.512 to 0.809 and lowers f2 from 0.400 to 0.007, the pattern read as 'fitness decoupling'. Breaking the s + b = 1 tradeoff by 0.05 raises both (F 0.843, f2 0.074). Particle fitness f1 stays near 0.095 and differs from F. The particle growth rate from iterating the model equals ln(lambda) at theta* within 1e-8. *Operationalization:* NAT Transcendence = life-cycle fitness versus counterfactual fitness. *Sources:* SIM-TR-NAT-0/iter-1#V1;SIM-TR-NAT-0/iter-1#H1;SIM-TR-NAT-0/iter-1#H2;SIM-TR-NAT-0/iter-1#H3;SIM-TR-NAT-0/iter-1#H4;SIM-TR-NAT-0/iter-1#H5. *Limits:* beta_i is the agent's reading of a formula garbled in the extracted text; reproduces P97's qualitative Fig. 5 result, not its exact numbers.
- **TRA-NAT-03** [P] At P97's Fig. 7 size (N 15, eta 8, p1 0.1) the TR0 pattern holds: f2 is maximised at zero investment, F at theta* = 0.326; moving from 0 to theta* raises F (0.512 to 0.798) and lowers f2 (0.400 to 0.037); breaking the tradeoff by 0.05 raises both (F 0.837, f2 0.102). *Operationalization:* NAT Transcendence = life-cycle vs counterfactual fitness. *Sources:* SIM-TR-NAT-A/iter-1#V1;SIM-TR-NAT-A/iter-1#H1;SIM-TR-NAT-A/iter-1#H2;SIM-TR-NAT-A/iter-1#H3;SIM-TR-NAT-A/iter-1#H4. *Limits:* Agent's implementation; P97's Fig. 7 adds a cell-type-switching model (rho -0.9) not implemented here.
- **TRA-NAT-04** [P] The decoupling pattern is robust to the two variations tried, but theta* moves a lot: with a smaller growth benefit (eta 4) theta* = 0.519 and F rises from -0.108 (a declining population at theta 0) to 0.532 while f2 falls from -0.229 to -0.833; with high single-cell survival (p1 0.5) theta* is only 0.056 and F rises by 0.010 (1.811 to 1.822). In every case f2's optimum is zero investment. *Operationalization:* NAT Transcendence = sensitivity of the transition optimum. *Sources:* SIM-TR-NAT-A/iter-2#V1;SIM-TR-NAT-A/iter-2#H1;SIM-TR-NAT-A/iter-2#H2;SIM-TR-NAT-A/iter-2#H3;SIM-TR-NAT-A/iter-3#V1;SIM-TR-NAT-A/iter-3#H1;SIM-TR-NAT-A/iter-3#H2;SIM-TR-NAT-A/iter-3#H3. *Limits:* Two variations only; beta_i reading as in TR0.

## Simulations (SIM-TR-NAT-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 10/10)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `55f25ecc` | P97's Fig. 7 size (N 15, eta 8, p1 0.1): do the TR0 results (f2 optimum 0, theta* > 0, decoupling, tradeoff breaking) hold? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; R1 Reported |
| 2 | `a1b83558` | Lower growth benefit (eta 4, N 30, p1 0.1): do the f2 optimum at 0, theta* > 0 and the decoupling pattern hold? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |
| 3 | `2e82de08` | Higher single-cell survival (p1 0.5, N 30, eta 8): do the f2 optimum at 0, theta* > 0 and the decoupling pattern hold? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: TRA-NAT-03: TR0 pattern holds at P97's Fig. 7 size (N 15).
- Pass 2: TRA-NAT-04: decoupling robust to eta 4; theta* rises to 0.519.
- Pass 3: TRA-NAT-04 (p1 0.5, iteration 3): theta* falls to 0.056.

## Unresolved
- beta_i reading unconfirmed; P97's cell-type switching model (Fig. 7, rho) not implemented.
- Competing readings of ETIs (major transitions generally) not yet sourced.
