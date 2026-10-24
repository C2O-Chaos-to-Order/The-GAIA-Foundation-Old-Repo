# Insurgence in the Social Sciences — Cycle-0-Baseline (IN0)

Phase report: Insurgence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: insurgence as a threshold-triggered uprising (P25's model of revolutions), whose start is unpredictable and whose outcome can be success, anarchy or status quo; P25's arithmetic checks out, its 'marked' decline only partly.

## Claims (ledger: `claims/claims.csv`)
- **IN0-SOC-01** [P] In P25's agent-based model of violent revolutions (citizens, revolutionaries, police on a 40 x 40 torus) spontaneous riots by the poorest citizens precede an organised uprising that starts when rebels outnumber police by a threshold n; the same start can end in successful revolution, anarchy or a return to the status quo, and revolutions arrive as 'random events' that cannot be anticipated, in line with Kuran's observation that most historical revolutions were unanticipated. *Operationalization:* SOC Insurgence = a threshold-triggered uprising with multiple possible outcomes. *Sources:* P25. *Limits:* Model results, not observations; historical parallels (Tunisia, Syria, Bahrain) are P25's illustrations; parameters mostly taken from Epstein's civil-violence model.
- **IN0-SOC-02** [P] P25's design counts reproduce (8 x 9 x 4 x 60 = 17,280 runs; 480 per cell; 2,160 per n), and with its Table 2 coefficients all four link functions put the peak of k(0.9, 0.3, n) inside [1.0, 1.1] (1.03-1.09), as P25 states. The fall after the peak is not 'marked' under every link: from peak to n = 1.4 k drops by 0.16 (complementary log-log) but only 0.04-0.09 under the others, below the 0.05 threshold for the linear model (not supported). *Operationalization:* SOC Insurgence = optimal uprising threshold. *Sources:* SIM-IN-SOC-0/iter-1#V1;SIM-IN-SOC-0/iter-1#H1;SIM-IN-SOC-0/iter-1#H2. *Limits:* Uses rounded printed coefficients; 0.05 threshold is the agent's reading of 'markedly'.

## Simulations (SIM-IN-SOC-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 1/2)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `1c5dd011` | Check P25's printed design counts (17,280 runs; 480 per (p, r) cell; 2,160 per n) and its statement that the fitted probability of killing a policeman k(0.9, 0.3, n) peaks for n in [1.0, 1.1] and then 'decreases markedly', using P25's Table 2 coefficients for all four link functions. | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Revolutions as threshold-triggered uprisings with multiple outcomes sourced (IN0-SOC-01); printed counts and the optimal-threshold statement checked (IN0-SOC-02).

## Unresolved
- Insurgency in political science (empirical studies) unsourced; P25 is one model.
- 'Decreases markedly' only partly supported (link-dependent).
