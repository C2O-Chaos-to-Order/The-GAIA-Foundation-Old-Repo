# Transcendence in the Philosophy Spirituality — Cycle-B-x6 (TRB)

Phase report: Transcendence (`../../README.md`). Definitions and competing definitions: `../DEFINITIONS.md`. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA's Phase axis is a framework category (PS), kept separate from the findings.

## Reading of this cycle
x6: P105 added (critique of the common-core measures); a templated instrument favours its tradition only if experience is constructed.

## Claims (ledger: `claims/claims.csv`)
- **TRB-PHI-01** [PS] P102 reports the central dispute over mystical experience, often described as transcending ordinary concepts: essentialists hold there is a 'common core' independent of culture, while constructivists (Katz) argue that experience is always shaped by concepts and, since mystics of different traditions have pervasively different conceptual schemes, there cannot be a common experience across cultural traditions. P102 notes that meditation inhibits ordinary cognitive processes (Deikman's deautomatization), which may limit cultural shaping, and that the dispute is hard to resolve because only post-experiential accounts, agreed by all parties to be culturally shaped, are available. *Operationalization:* PHI Transcendence = mystical experience and the common-core debate. *Sources:* P102. *Limits:* Interpretive (one SEP entry's survey). Spelling slip: the text writes 'deautomization' while its bibliography cites Deikman's 'Deautomatization'. Short phrases quoted only.
- **TRB-PHI-04** [PS] P105 argues that mystical-experience measures in psychedelic science (from Pahnke's Mystical Consciousness Typology to the MEQ) descend from Stace's perennialist 'common core' view and carry a Christian-Protestant template, so they treat mystical experience as positive and culture-independent; it does not ask that the term be dropped but that it be historicised, decomposed into psychological constructs (ego dissolution, connectedness, self-experience) and measured with culturally validated items, as in Taves's Inventory of Non-Ordinary Experiences, whose item meta-data showed inconsistent interpretation across US and Indian samples. *Operationalization:* PHI Transcendence = the common-core assumption built into measures. *Sources:* P105. *Limits:* A review's argument; empirical claims are cited, not tested. Slips: 'William Stace' and 'Walter Stace' for W. T. Stace; 'MEQ-43' in the text vs 'MEQ-45' in Table 1; 'Eveylnn Underhill'; 'In order words'.
- **TRB-PHI-02** [H] In a toy with 6 traditions, 10 mystics each and 40 features, strong constructivism with independent schemes gave cross-tradition report correlations near 0 (|r| < 0.003), but a shared heritage component (h 0.5) gave 0.39 with no common core at all; with a core (w 0.5) correlation rose with deautomatization (0.07 to 0.10, thin reports 0.16 to 0.20), and fell with it under constructivism with heritage (0.39 to 0.29). So cross-tradition agreement alone does not distinguish a common core from shared heritage; its response to deautomatization does, in the toy. *Operationalization:* PHI Transcendence = common core versus construction. *Sources:* SIM-TR-PHI-0/iter-1#V1;SIM-TR-PHI-0/iter-1#H1;SIM-TR-PHI-0/iter-1#H2;SIM-TR-PHI-0/iter-1#H3;SIM-TR-PHI-0/iter-1#H4;SIM-TR-PHI-0/iter-1#H5. *Limits:* A toy of one framing of a philosophical debate; all parameters are the agent's choices; vector 'experiences' presuppose commensurability, which constructivists may deny.
- **TRB-PHI-03** [H] The TR0 toy patterns hold with 12 traditions and with doubled noise (independent schemes: |r| < 0.003; essentialist correlation rising with deautomatization, 0.071 to 0.102 and 0.037 to 0.044). But with shared heritage the pre-registered separation check was not supported: a core plus heritage also loses agreement as deautomatization rises (0.394 to 0.341, vs 0.396 to 0.294 without a core), so in the toy neither agreement nor its trend with training cleanly separates a common core from shared heritage. *Operationalization:* PHI Transcendence = common core vs heritage. *Sources:* SIM-TR-PHI-A/iter-1#V1;SIM-TR-PHI-A/iter-1#H1;SIM-TR-PHI-A/iter-1#H2;SIM-TR-PHI-A/iter-2#V1;SIM-TR-PHI-A/iter-2#H1;SIM-TR-PHI-A/iter-2#H2;SIM-TR-PHI-A/iter-3#V1;SIM-TR-PHI-A/iter-3#H1;SIM-TR-PHI-A/iter-3#H2. *Limits:* Toy; deautomatization here removes heritage and tradition alike (agent's modelling choice).
- **TRB-PHI-05** [H] In a toy of P105's critique, an instrument whose items follow one tradition's scheme (a 0.7) shows no template advantage when experiences share only a core (-0.001 SD) but a large one when they are constructed by tradition (2.35 SD; 1.97 with a half core); generic items (a 0) remove it (-0.03), and deautomatization shrinks it (1.96 to 0.62). The core/construct toy's patterns also held with weaker heritage (0.19 at h 0.25), a lighter overlay (0.111 vs 0.071) and 30 mystics per tradition. So a templated scale's tradition differences are informative only if experiences are partly constructed, which is the point in dispute. *Operationalization:* PHI Transcendence = instrument template and measured transcendence. *Sources:* SIM-TR-PHI-B/iter-1#V1;SIM-TR-PHI-B/iter-1#H1;SIM-TR-PHI-B/iter-1#H2;SIM-TR-PHI-B/iter-2#V1;SIM-TR-PHI-B/iter-2#H1;SIM-TR-PHI-B/iter-3#V1;SIM-TR-PHI-B/iter-3#H1;SIM-TR-PHI-B/iter-4#V1;SIM-TR-PHI-B/iter-4#H1;SIM-TR-PHI-B/iter-5#V1;SIM-TR-PHI-B/iter-5#H1;SIM-TR-PHI-B/iter-6#V1;SIM-TR-PHI-B/iter-6#H1. *Limits:* Toy; item and experience vectors and all parameters are the agent's choices.

## Simulations (SIM-TR-PHI-B; 6 iteration(s), spec-first; validation 6/6, hypotheses supported 7/7)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `2aae9df7` | A templated instrument (P105's critique): template advantage with core-only vs constructed experiences? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |
| 2 | `a43cd6e3` | Do generic items (Taves's aim) remove the template advantage under constructivism? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `0f8916f5` | Does deautomatization shrink the template advantage under a mixed model? | V1 Pass; H1 Supported; R1 Reported |
| 4 | `7ef409c0` | Weaker heritage (h 0.25): cross-tradition correlation between 0.05 and 0.35? | V1 Pass; H1 Supported; R1 Reported |
| 5 | `c73540ad` | Lighter overlay (lam 0.5) vs lam 1: higher agreement? | V1 Pass; H1 Supported; R1 Reported |
| 6 | `5901c028` | 30 mystics per tradition: independent schemes still |r| < 0.03? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (6; details `research/PASSES.md`)
- Pass 1: Critique of mystical-experience measures sourced (TRB-PHI-04); instrument-template toy (TRB-PHI-05).
- Pass 2: TRB-PHI-05 (generic items, iteration 2): template advantage removed.
- Pass 3: TRB-PHI-05 (deautomatization, iteration 3): advantage shrinks 1.96 to 0.62.
- Pass 4: TRB-PHI-05 (h 0.25, iteration 4): agreement 0.19.
- Pass 5: TRB-PHI-05 (lam 0.5, iteration 5): 0.111 vs 0.071.
- Pass 6: TRB-PHI-05 (M 30, iteration 6): independent schemes near zero.

## Unresolved
- Primary texts (Stace, Katz, Forman, Taves) not read.
- Instrument toy's parameters are the agent's choices.
