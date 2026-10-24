# Ascendence in the Philosophy Spirituality — Cycle-0-Baseline (AS0)

Phase report: Ascendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: Diotima's ladder of love (P90); a Hypothetical toy shows ascent needs both incoherence and the disposition to resolve it.

## Claims (ledger: `claims/claims.csv`)
- **AS0-PHI-01** [PS] In P90's reading of Diotima's speech in the Symposium, correct love ascends from one beautiful body to all beautiful bodies, to beautiful souls, laws and practices, the sciences and finally the beautiful itself; what drives each step is the incoherence met at lower stages, which leads the lover under 'his rational desire for truth and consistency' to climb to the next stage. P90 rejects the reading that the beloved is kicked away with the ladder: the lover comes to value him appropriately, and 'valuing appropriately is still valuing'. Alcibiades shows love that does not lead up; the Phaedrus adds a winged soul that regains its wings after three successive philosophical lives. *Operationalization:* PHI Ascendence = the ascent of love (Diotima's ladder). *Sources:* P90. *Limits:* Interpretive (one author's reading; P90 lists rival readings, e.g. Nussbaum, Price, Sheffield). The Athenian pederastic context frames the account. Short phrases quoted only.
- **AS0-PHI-02** [H] In a six-rung toy (rungs cover 0.2, 0.4, 0.6, 0.8, 0.95 and 1 of the beautiful things met; climb on an uncovered case with probability q), q = 1 reached the top in a mean 30.2 encounters (analytic 30.4) and q = 0.5 in 60.5 (analytic 60.8), while q = 0 never left the first rung: meeting incoherence is not enough without the disposition to resolve it. Two-thirds of the encounters are spent on the last rung below the top (1/(1 - 0.95) = 20 of 30.4), so in the toy the final step is the hardest. *Operationalization:* PHI Ascendence = ascent driven by incoherence. *Sources:* SIM-AS-PHI-0/iter-1#V1;SIM-AS-PHI-0/iter-1#H1;SIM-AS-PHI-0/iter-1#H2;SIM-AS-PHI-0/iter-1#H3;SIM-AS-PHI-0/iter-1#H4. *Limits:* A toy of one reading of a philosophical text; coverage values and q are the agent's choices; the toy says nothing about whether the beautiful itself exists.

## Simulations (SIM-AS-PHI-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 4/4)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `349b9b97` | A toy of the ascent P90 reports from Diotima's speech: rungs covering more of the beautiful things met (0.2, 0.4, 0.6, 0.8, 0.95, 1); a lover climbs on meeting an uncovered case with probability q. Does q = 0 stop the ascent, does q = 1 always reach the top, does halving q double the encounters, and is the last step the longest? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Diotima's ascent and its driver (incoherence at lower stages) sourced (AS0-PHI-01, PS); Hypothetical ladder toy (AS0-PHI-02).

## Unresolved
- Only one SEP reading of Plato read; rival readings (Nussbaum, Price, Sheffield) not read.
- Non-Platonic ascent traditions (e.g. Plotinus, mystical ascent literature) not yet read.
