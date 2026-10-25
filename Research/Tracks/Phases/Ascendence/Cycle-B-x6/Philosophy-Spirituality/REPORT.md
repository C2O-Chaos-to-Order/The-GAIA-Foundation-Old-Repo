# Ascendence in the Philosophy Spirituality — Cycle-B-x6 (ASB)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: in the toy, time and disposition decide ascent; weak disposition plus regress stops it (Hypothetical).

## Claims (ledger: `claims/claims.csv`)
- **ASB-PHI-01** [PS] In P90's reading of Diotima's speech in the Symposium, correct love ascends from one beautiful body to all beautiful bodies, to beautiful souls, laws and practices, the sciences and finally the beautiful itself; what drives each step is the incoherence met at lower stages, which leads the lover under 'his rational desire for truth and consistency' to climb to the next stage. P90 rejects the reading that the beloved is kicked away with the ladder: the lover comes to value him appropriately, and 'valuing appropriately is still valuing'. Alcibiades shows love that does not lead up; the Phaedrus adds a winged soul that regains its wings after three successive philosophical lives. *Operationalization:* PHI Ascendence = the ascent of love (Diotima's ladder). *Sources:* P90. *Limits:* Interpretive (one author's reading; P90 lists rival readings, e.g. Nussbaum, Price, Sheffield). The Athenian pederastic context frames the account. Short phrases quoted only.
- **ASB-PHI-02** [H] In a six-rung toy (rungs cover 0.2, 0.4, 0.6, 0.8, 0.95 and 1 of the beautiful things met; climb on an uncovered case with probability q), q = 1 reached the top in a mean 30.2 encounters (analytic 30.4) and q = 0.5 in 60.5 (analytic 60.8), while q = 0 never left the first rung: meeting incoherence is not enough without the disposition to resolve it. Two-thirds of the encounters are spent on the last rung below the top (1/(1 - 0.95) = 20 of 30.4), so in the toy the final step is the hardest. *Operationalization:* PHI Ascendence = ascent driven by incoherence. *Sources:* SIM-AS-PHI-0/iter-1#V1;SIM-AS-PHI-0/iter-1#H1;SIM-AS-PHI-0/iter-1#H2;SIM-AS-PHI-0/iter-1#H3;SIM-AS-PHI-0/iter-1#H4. *Limits:* A toy of one reading of a philosophical text; coverage values and q are the agent's choices; the toy says nothing about whether the beautiful itself exists.
- **ASB-PHI-03** [H] With dispositions q ~ Beta(1, 3), 95.5% of 20,000 lovers reached the top within 2000 encounters; those who did had mean q 0.26 against 0.011 for those who did not. With q 1, stepping down a rung with probability 0.05 or even 0.5 on each covered encounter still let every lover reach the top (the two pre-registered checks that r 0.5 would stop most were not supported), because the top rung is absorbing and every uncovered case lifts with certainty. In the toy, regress delays but does not prevent ascent unless the disposition itself is weak. *Operationalization:* PHI Ascendence = ascent with regress and varied dispositions. *Sources:* SIM-AS-PHI-A/iter-1#V1;SIM-AS-PHI-A/iter-1#H1;SIM-AS-PHI-A/iter-1#H2;SIM-AS-PHI-A/iter-2#V1;SIM-AS-PHI-A/iter-2#H1;SIM-AS-PHI-A/iter-3#V1;SIM-AS-PHI-A/iter-3#H1;SIM-AS-PHI-A/iter-3#H2. *Limits:* Toy of one reading of P90; the absorbing top rung and the regress rule are the agent's choices.
- **ASB-PHI-04** [H] In the ladder toy, time and disposition together decide ascent: with polarised dispositions (Beta(0.5, 0.5)) 92.6% reach the top in 2000 encounters (mean q 0.54 for those who do, 0.007 for those who do not); with only 100 encounters and Beta(1, 3) 40.8% do, and with 50 encounters and Beta(2, 2) 46.6%. *Operationalization:* PHI Ascendence = ascent with limited encounters. *Sources:* SIM-AS-PHI-B/iter-1#V1;SIM-AS-PHI-B/iter-1#H1;SIM-AS-PHI-B/iter-2#V1;SIM-AS-PHI-B/iter-2#H1;SIM-AS-PHI-B/iter-5#V1;SIM-AS-PHI-B/iter-5#H1. *Limits:* Toy of one reading of P90.
- **ASB-PHI-05** [H] Weak disposition plus regress stops ascent in the toy: q 0.1 with r 0.5 gives 0.26% at the top (mean rung 0.40) and q 0.05 with r 0.2 gives 0.26% (mean rung 0.49), whereas q 1 reaches the top every time even when the penultimate rung covers 99% of cases. *Operationalization:* PHI Ascendence = ascent with regress. *Sources:* SIM-AS-PHI-B/iter-3#V1;SIM-AS-PHI-B/iter-3#H1;SIM-AS-PHI-B/iter-4#V1;SIM-AS-PHI-B/iter-4#H1;SIM-AS-PHI-B/iter-6#V1;SIM-AS-PHI-B/iter-6#H1. *Limits:* The absorbing top rung and the regress rule are the agent's choices.

## Simulations (SIM-AS-PHI-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 6/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `8693e49e` | Polarised dispositions q ~ Beta(0.5, 0.5): >= 80% reach the top? | V1 Pass; H1 Supported; R1 Reported |
| 2 | `f4563564` | A short life (100 encounters), q ~ Beta(1, 3): < 50% reach the top? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `cd4002f2` | Weak disposition q 0.1 with strong regress r 0.5: < 50% reach the top? | V1 Pass; H1 Supported; R1 Reported |
| 4 | `1c36365f` | Near-complete penultimate rung (coverage 0.99), q 1: all reach the top? | V1 Pass; H1 Supported; R1 Reported |
| 5 | `be3b103a` | 50 encounters, q ~ Beta(2, 2): 20-80% reach the top? | V1 Pass; H1 Supported; R1 Reported |
| 6 | `3dbbc8de` | q 0.05 with regress r 0.2: mean rung below 4? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: Search logged; 5 hits (chiropractic philosophy, myth and madness), none relevant, none read. ASB-PHI-04: polarised dispositions.
- Pass 2: ASB-PHI-04: a short life halves ascent.
- Pass 3: ASB-PHI-05: weak disposition plus regress stops ascent.
- Pass 4: ASB-PHI-05: near-complete rung does not stop q 1.
- Pass 5: ASB-PHI-04: 50 encounters, Beta(2, 2).
- Pass 6: ASB-PHI-05: q 0.05 with r 0.2.

## Unresolved
- No Neoplatonic or non-Platonic ascent source found in PMC; non-PMC sources needed.
- The toy's absorbing top rung is an assumption.
