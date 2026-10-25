# Transcendence in the Philosophy Spirituality — Cycle-0-Baseline (TR0)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
Baseline: mysticism and the common-core debate (P102); a Hypothetical toy shows agreement alone cannot separate a core from shared heritage.

## Claims (ledger: `claims/claims.csv`)
- **TR0-PHI-01** [PS] P102 reports the central dispute over mystical experience, often described as transcending ordinary concepts: essentialists hold there is a 'common core' independent of culture, while constructivists (Katz) argue that experience is always shaped by concepts and, since mystics of different traditions have pervasively different conceptual schemes, there cannot be a common experience across cultural traditions. P102 notes that meditation inhibits ordinary cognitive processes (Deikman's deautomatization), which may limit cultural shaping, and that the dispute is hard to resolve because only post-experiential accounts, agreed by all parties to be culturally shaped, are available. *Operationalization:* PHI Transcendence = mystical experience and the common-core debate. *Sources:* P102. *Limits:* Interpretive (one SEP entry's survey). Spelling slip: the text writes 'deautomization' while its bibliography cites Deikman's 'Deautomatization'. Short phrases quoted only.
- **TR0-PHI-02** [H] In a toy with 6 traditions, 10 mystics each and 40 features, strong constructivism with independent schemes gave cross-tradition report correlations near 0 (|r| < 0.003), but a shared heritage component (h 0.5) gave 0.39 with no common core at all; with a core (w 0.5) correlation rose with deautomatization (0.07 to 0.10, thin reports 0.16 to 0.20), and fell with it under constructivism with heritage (0.39 to 0.29). So cross-tradition agreement alone does not distinguish a common core from shared heritage; its response to deautomatization does, in the toy. *Operationalization:* PHI Transcendence = common core versus construction. *Sources:* SIM-TR-PHI-0/iter-1#V1;SIM-TR-PHI-0/iter-1#H1;SIM-TR-PHI-0/iter-1#H2;SIM-TR-PHI-0/iter-1#H3;SIM-TR-PHI-0/iter-1#H4;SIM-TR-PHI-0/iter-1#H5. *Limits:* A toy of one framing of a philosophical debate; all parameters are the agent's choices; vector 'experiences' presuppose commensurability, which constructivists may deny.

## Simulations (SIM-TR-PHI-0; 1 iteration(s), spec-first; validation 1/1, hypotheses supported 5/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `630b1b4a` | A toy of the essentialism / strong-constructivism debate P102 reports: without a common core, are cross-tradition reports uncorrelated (or correlated only via shared heritage); with a core, does deautomatization raise agreement and do thick interpretive overlays lower it? | V1 Pass; H1 Supported; H2 Supported; H3 Supported; H4 Supported; H5 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (1; details `research/PASSES.md`)
- Pass 1: Essentialism vs constructivism and the limits of post-experiential reports sourced (TR0-PHI-01, PS); Hypothetical toy: agreement alone cannot separate a common core from shared heritage (TR0-PHI-02).

## Unresolved
- Only one SEP survey read; primary texts (Katz 1978, Forman 1990, Stace) not read.
- Transcendence in other senses (Kantian transcendental, theological transcendence) not covered.
