# Ascendence in the Philosophy Spirituality — Cycle-A-x3 (ASA)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: in a toy, regress delays but does not stop ascent; weak dispositions do (Hypothetical).

## Claims (ledger: `claims/claims.csv`)
- **ASA-PHI-01** [PS] In P90's reading of Diotima's speech in the Symposium, correct love ascends from one beautiful body to all beautiful bodies, to beautiful souls, laws and practices, the sciences and finally the beautiful itself; what drives each step is the incoherence met at lower stages, which leads the lover under 'his rational desire for truth and consistency' to climb to the next stage. P90 rejects the reading that the beloved is kicked away with the ladder: the lover comes to value him appropriately, and 'valuing appropriately is still valuing'. Alcibiades shows love that does not lead up; the Phaedrus adds a winged soul that regains its wings after three successive philosophical lives. *Operationalization:* PHI Ascendence = the ascent of love (Diotima's ladder). *Sources:* P90. *Limits:* Interpretive (one author's reading; P90 lists rival readings, e.g. Nussbaum, Price, Sheffield). The Athenian pederastic context frames the account. Short phrases quoted only.
- **ASA-PHI-02** [H] In a six-rung toy (rungs cover 0.2, 0.4, 0.6, 0.8, 0.95 and 1 of the beautiful things met; climb on an uncovered case with probability q), q = 1 reached the top in a mean 30.2 encounters (analytic 30.4) and q = 0.5 in 60.5 (analytic 60.8), while q = 0 never left the first rung: meeting incoherence is not enough without the disposition to resolve it. Two-thirds of the encounters are spent on the last rung below the top (1/(1 - 0.95) = 20 of 30.4), so in the toy the final step is the hardest. *Operationalization:* PHI Ascendence = ascent driven by incoherence. *Sources:* SIM-AS-PHI-0/iter-1#V1;SIM-AS-PHI-0/iter-1#H1;SIM-AS-PHI-0/iter-1#H2;SIM-AS-PHI-0/iter-1#H3;SIM-AS-PHI-0/iter-1#H4. *Limits:* A toy of one reading of a philosophical text; coverage values and q are the agent's choices; the toy says nothing about whether the beautiful itself exists.
- **ASA-PHI-03** [H] With dispositions q ~ Beta(1, 3), 95.5% of 20,000 lovers reached the top within 2000 encounters; those who did had mean q 0.26 against 0.011 for those who did not. With q 1, stepping down a rung with probability 0.05 or even 0.5 on each covered encounter still let every lover reach the top (the two pre-registered checks that r 0.5 would stop most were not supported), because the top rung is absorbing and every uncovered case lifts with certainty. In the toy, regress delays but does not prevent ascent unless the disposition itself is weak. *Operationalization:* PHI Ascendence = ascent with regress and varied dispositions. *Sources:* SIM-AS-PHI-A/iter-1#V1;SIM-AS-PHI-A/iter-1#H1;SIM-AS-PHI-A/iter-1#H2;SIM-AS-PHI-A/iter-2#V1;SIM-AS-PHI-A/iter-2#H1;SIM-AS-PHI-A/iter-3#V1;SIM-AS-PHI-A/iter-3#H1;SIM-AS-PHI-A/iter-3#H2. *Limits:* Toy of one reading of P90; the absorbing top rung and the regress rule are the agent's choices.

## Simulations (SIM-AS-PHI-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 3/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `62d7e0a2` | P90's ascent with varied dispositions: with q ~ Beta(1, 3) across 20,000 lovers, do at least 80% reach the top within 2000 encounters, and do those who reach it have a higher mean q? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `20153d8c` | Fall-back (P90's Alcibiades 'regressively' returning to the crowd) as a toy: with q 1 and a 5% chance of stepping down per covered encounter, do at least 95% still reach the top? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `fc6ea087` | Strong fall-back: with r 0.5, do fewer than half reach the top within 2000 encounters and is the mean rung below 3? | V1 Pass; H1 Not supported; H2 Not supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: ASA-PHI-03: varied dispositions; 95.5% reach the top.
- Pass 2: ASA-PHI-03 (weak regress, iteration 2).
- Pass 3: ASA-PHI-03 (strong regress does not stop ascent in the toy, iteration 3).

## Unresolved
- Only one SEP reading of Plato read; rival readings and non-Platonic ascent traditions not read.
- The toy's absorbing top rung is an assumption.
