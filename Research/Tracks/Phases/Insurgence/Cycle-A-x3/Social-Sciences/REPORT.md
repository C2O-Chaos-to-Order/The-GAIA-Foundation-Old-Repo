# Insurgence in the Social Sciences — Cycle-A-x3 (INA)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: threshold cascades are fragile (one changed threshold stops a full cascade) and sudden in the spread of thresholds; P25's optimal ratio is fixed by its specification.

## Claims (ledger: `claims/claims.csv`)
- **INA-SOC-03** [E] P25 states that it draws on Granovetter's threshold models of collective behaviour: each individual has a personal threshold and joins collective action, such as a riot or a strike, if the number of people already participating exceeds it. *Operationalization:* SOC Insurgence = joining once enough others have joined. *Sources:* P25. *Limits:* Secondary report of Granovetter (1978), which was not read; the claim is about P25's text, classed interpretive because it reports a theoretical stance.
- **INA-SOC-01** [P] In P25's agent-based model of violent revolutions (citizens, revolutionaries, police on a 40 x 40 torus) spontaneous riots by the poorest citizens precede an organised uprising that starts when rebels outnumber police by a threshold n; the same start can end in successful revolution, anarchy or a return to the status quo, and revolutions arrive as 'random events' that cannot be anticipated, in line with Kuran's observation that most historical revolutions were unanticipated. *Operationalization:* SOC Insurgence = a threshold-triggered uprising with multiple possible outcomes. *Sources:* P25. *Limits:* Model results, not observations; historical parallels (Tunisia, Syria, Bahrain) are P25's illustrations; parameters mostly taken from Epstein's civil-violence model.
- **INA-SOC-02** [P] P25's design counts reproduce (8 x 9 x 4 x 60 = 17,280 runs; 480 per cell; 2,160 per n), and with its Table 2 coefficients all four link functions put the peak of k(0.9, 0.3, n) inside [1.0, 1.1] (1.03-1.09), as P25 states. The fall after the peak is not 'marked' under every link: from peak to n = 1.4 k drops by 0.16 (complementary log-log) but only 0.04-0.09 under the others, below the 0.05 threshold for the linear model (not supported). *Operationalization:* SOC Insurgence = optimal uprising threshold. *Sources:* SIM-IN-SOC-0/iter-1#V1;SIM-IN-SOC-0/iter-1#H1;SIM-IN-SOC-0/iter-1#H2. *Limits:* Uses rounded printed coefficients; 0.05 threshold is the agent's reading of 'markedly'.
- **INA-SOC-04** [P] In a threshold cascade (join when the number already participating reaches one's threshold) thresholds 0..N-1 gave a full cascade for N = 100 and 1,000, and raising one threshold from 1 to 2 stopped it at a single person. With normal thresholds (mean N/4) the final size went from near 0 to near N as the spread grew (N = 100: 15% at sd 12, 47% at 13, 75% at 14; N = 1,000: 21% at sd 120, 54% at 125, 85% at 130); the largest jump between adjacent spreads was 0.31 and 0.33. More dispersed thresholds (more low-threshold instigators) made a total cascade more likely. *Operationalization:* SOC Insurgence = threshold cascade. *Sources:* SIM-IN-SOC-A/iter-1#V1;SIM-IN-SOC-A/iter-1#H1;SIM-IN-SOC-A/iter-1#H2;SIM-IN-SOC-A/iter-2#V1;SIM-IN-SOC-A/iter-2#H1;SIM-IN-SOC-A/iter-2#H2. *Limits:* Agent's toy; the sim uses 'reaches' where P25's wording is 'exceeds'; the uniform and one-change cases are constructions, not numbers from P25; jumps only just above the pre-set 0.3.
- **INA-SOC-05** [P] At another design cell (p = 0.3, r = 0.1) P25's four fitted links peak at n = 1.03-1.09, as at (0.9, 0.3); the fall by more than 0.05 to n = 1.4 under every link is again not supported (linear link 0.036). Because p and r enter P25's index additively, the optimal rebel-to-police ratio is a property of the specification and cannot vary with p or r. *Operationalization:* SOC Insurgence = optimal threshold of P25's fitted model. *Sources:* SIM-IN-SOC-A/iter-3#V1;SIM-IN-SOC-A/iter-3#H1;SIM-IN-SOC-A/iter-3#H2. *Limits:* Foreknown by reasoning before the run (disclosed); says nothing about P25's underlying simulations.

## Simulations (SIM-IN-SOC-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 5/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `58c625d1` | Threshold cascades (SOC pass 2; threshold model as described in P25): N = 100, thresholds 0..99 give a full cascade, and raising one threshold stops it; with normal thresholds (mean 25) does the final size jump as the spread grows from 5 to 20? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `3e49a380` | Threshold cascades at N = 1000 (SOC pass 2): same check with thresholds mean 250 and spread 40 to 140 (step 5); is the jump still sudden? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 3 | `0a5d9d6d` | Is P25's optimal threshold a property of its additive specification (SOC pass 3)? Repeat IN0's Table 2 check at another design cell (p = 0.3, r = 0.1, both on P25's grid): does every link still peak in n = [1.0, 1.1]? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: INA-SOC-03 (P25's threshold-model basis) and INA-SOC-04 (threshold cascades: fragile with uniform thresholds, sudden with normal ones).
- Pass 2: INA-SOC-05: P25's optimal threshold is fixed by its additive specification (H2 again not supported); foreknown by reasoning (disclosed).
- Pass 3: Added nothing: no empirical study of insurgency or revolution was searched or read; SOC rests on one model paper (P25).

## Unresolved
- No empirical insurgency source; SOC rests on P25 (one model) and toys.
- Granovetter (1978) known only through P25.
