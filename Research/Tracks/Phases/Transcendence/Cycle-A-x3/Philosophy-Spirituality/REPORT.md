# Transcendence in the Philosophy Spirituality — Cycle-A-x3 (TRA)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x3: toy robust in size and noise; with shared heritage neither agreement nor its training trend separates core from heritage.

## Claims (ledger: `claims/claims.csv`)
- **TRA-PHI-01** [PS] P102 reports the central dispute over mystical experience, often described as transcending ordinary concepts: essentialists hold there is a 'common core' independent of culture, while constructivists (Katz) argue that experience is always shaped by concepts and, since mystics of different traditions have pervasively different conceptual schemes, there cannot be a common experience across cultural traditions. P102 notes that meditation inhibits ordinary cognitive processes (Deikman's deautomatization), which may limit cultural shaping, and that the dispute is hard to resolve because only post-experiential accounts, agreed by all parties to be culturally shaped, are available. *Operationalization:* PHI Transcendence = mystical experience and the common-core debate. *Sources:* P102. *Limits:* Interpretive (one SEP entry's survey). Spelling slip: the text writes 'deautomization' while its bibliography cites Deikman's 'Deautomatization'. Short phrases quoted only.
- **TRA-PHI-02** [H] In a toy with 6 traditions, 10 mystics each and 40 features, strong constructivism with independent schemes gave cross-tradition report correlations near 0 (|r| < 0.003), but a shared heritage component (h 0.5) gave 0.39 with no common core at all; with a core (w 0.5) correlation rose with deautomatization (0.07 to 0.10, thin reports 0.16 to 0.20), and fell with it under constructivism with heritage (0.39 to 0.29). So cross-tradition agreement alone does not distinguish a common core from shared heritage; its response to deautomatization does, in the toy. *Operationalization:* PHI Transcendence = common core versus construction. *Sources:* SIM-TR-PHI-0/iter-1#V1;SIM-TR-PHI-0/iter-1#H1;SIM-TR-PHI-0/iter-1#H2;SIM-TR-PHI-0/iter-1#H3;SIM-TR-PHI-0/iter-1#H4;SIM-TR-PHI-0/iter-1#H5. *Limits:* A toy of one framing of a philosophical debate; all parameters are the agent's choices; vector 'experiences' presuppose commensurability, which constructivists may deny.
- **TRA-PHI-03** [H] The TR0 toy patterns hold with 12 traditions and with doubled noise (independent schemes: |r| < 0.003; essentialist correlation rising with deautomatization, 0.071 to 0.102 and 0.037 to 0.044). But with shared heritage the pre-registered separation check was not supported: a core plus heritage also loses agreement as deautomatization rises (0.394 to 0.341, vs 0.396 to 0.294 without a core), so in the toy neither agreement nor its trend with training cleanly separates a common core from shared heritage. *Operationalization:* PHI Transcendence = common core vs heritage. *Sources:* SIM-TR-PHI-A/iter-1#V1;SIM-TR-PHI-A/iter-1#H1;SIM-TR-PHI-A/iter-1#H2;SIM-TR-PHI-A/iter-2#V1;SIM-TR-PHI-A/iter-2#H1;SIM-TR-PHI-A/iter-2#H2;SIM-TR-PHI-A/iter-3#V1;SIM-TR-PHI-A/iter-3#H1;SIM-TR-PHI-A/iter-3#H2. *Limits:* Toy; deautomatization here removes heritage and tradition alike (agent's modelling choice).

## Simulations (SIM-TR-PHI-A; 3 iteration(s), spec-first; validation 3/3, hypotheses supported 5/6)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `ade56bc1` | With 12 traditions instead of 6: does strong constructivism with independent schemes still give |r| < 0.03, and does correlation rise with deautomatization under essentialism? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `a5240c65` | With shared heritage for both models: does agreement fail to discriminate core from no core, and does deautomatization separate them? | V1 Pass; H1 Supported; H2 Not supported; R1 Reported |
| 3 | `97c81ff1` | With noise sigma 2: do the TR0 constructivist and essentialist patterns hold? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: TRA-PHI-03: TR0 toy patterns hold with 12 traditions.
- Pass 2: TRA-PHI-03 (shared heritage, iteration 2): deautomatization does not separate core from heritage.
- Pass 3: TRA-PHI-03 (noise sigma 2, iteration 3): patterns hold, weaker.

## Unresolved
- The toy's deautomatization removes heritage and tradition alike; alternative modelling not tried.
- Primary texts (Katz, Forman, Stace) not read.
