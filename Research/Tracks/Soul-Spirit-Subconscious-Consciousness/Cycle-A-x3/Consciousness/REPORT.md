# Consciousness — Track Cycle A (x3)

Track: Soul, Spirit, Subconscious and Consciousness (`../../README.md`). Scope and boundary: `../../FRAMEWORK.md` § Consciousness. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA is the motherthread (PS framing) and is kept separate from the science.

## Reading of this cycle
Cycle A deepened Report 5 on **how theories are tested**. No-report results need not refute cognitive theories, because report demands add late activity (K13, with a toy check in SIM-CONS-A iter-1 that adds logic, not evidence). IIT's silent-neuron predictions are argued to be testable (K12). The structure of meditators' 'pure awareness' reports is statistically plausible for data of its size (K14; SIM-CONS-A iter-2 and iter-3). No theory is decided.



## Claims (ledger: `claims/claims.csv`)
- **TA-CONS-01** [E] In Whyte, Hohwy & Smith's active-inference model of masking, late P3b-like potentials and increased PFC activity were produced by the working-memory demands of self-report and vanished without report, yet simulated PFC activity on visible trials still crossed the reportability threshold. On this model, no-report results do not necessarily contradict cognitive (global-workspace or higher-order) theories. *Sources:* K13. *Limits:* One computational model; shows compatibility, not that the theories are right. *Deepens:* R5:C1-R5-02;R5:C2-R5-03.
- **TA-CONS-02** [E] In SIM-CONS-A's minimal threshold toy (gating + report demand), removing report cut the visible-minus-invisible PFC contrast by 60% while 84% of visible trials still exceeded the reportability threshold. K13's qualitative pattern follows from these two assumptions, so the toy shows the logic is coherent but adds no evidence about brains. *Sources:* SIM-CONS-A/iter-1#V1;SIM-CONS-A/iter-1#H1;SIM-CONS-A/iter-1#H2. *Limits:* Assumption-driven by construction. *Deepens:* R5:C1-R5-02.
- **TA-CONS-04** [E] The Minimal Phenomenal Experience questionnaire (92 items; 1,403 usable of 3,627 responses from meditators, mostly Vipassana 43.9% and Zen 34.9%) yielded 12 factors explaining 44% of variance, including 'Pure Awareness in Dream and Sleep', 'Luminosity', 'Wakeful Presence' and 'Witness Consciousness'. *Sources:* K14. *Limits:* Self-selected meditators; exploratory factor names are interpretive. *Deepens:* R5:C3-R5-07;R5:C0v2-R5-04.
- **TA-CONS-05** [E] In SIM-CONS-A, 92 structureless items (n = 1,403) gave about 43 'factors' by the eigenvalue-above-1 rule but about 0 by parallel analysis; with 12 true factors parallel analysis recovered exactly 12 at loadings of .4 to .75, and '12 components explain 44%' corresponded to loadings near .6. K14's dimensionality is statistically plausible for data of its size; what the factors are experiences of is a separate question. *Sources:* SIM-CONS-A/iter-2#V1;SIM-CONS-A/iter-2#H1;SIM-CONS-A/iter-3#V1;SIM-CONS-A/iter-3#H1;SIM-CONS-A/iter-3#H2. *Limits:* Principal components on simulated normal items; K14 used factor analysis on real data (not re-run). *Deepens:* R5:C3-R5-07.
- **TA-CONS-03** [P] Integrated information theory predicts that silencing all active neurons in the main complex leaves consciousness present (silent-brain prediction) and that disabling silent neurons can change experience (disabled-neuron prediction). Against the objection that these are untestable, Ponce de Leon & Yoshimi (2026) argue both can be tested, while noting why such theoretical disputes are hard to resolve (Lakatos). *Sources:* K12. *Limits:* Philosophical analysis; no experiment run. *Deepens:* R5:C0v2-R5-08;R5:C2-R5-03.
- **TA-CONS-06** [PS] 'Pure awareness' (interpretive): contemplative traditions describe consciousness without ordinary content (for example turiya in Advaita, S31), and meditators' reports of such states have a measurable structure (K14). Whether awareness without content exists as more than a reported state is a philosophical question the track does not settle. *Sources:* S31;K14;S32;G03. *Limits:* Interpretive. *Deepens:* R5:C0v2-R5-12;R5:C3-R5-07.
- **TA-CONS-07** [PS] Boundary: no theory has solved consciousness. Track Cycle A sharpened two methodological questions (report confounds, testability of IIT's silent-neuron predictions) but decided none of the theories. *Sources:* S16;S19;G03. *Limits:* Framework statement. *Deepens:* R5:C0v2-R5-12.

## Simulations (SIM-CONS-A; 3 iterations, spec-first; validation 3/3, hypotheses supported 5/5)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `c93bbde7` | K13 argues that no-report paradigms remove report-related late PFC activity but that PFC activity on visible trials may still cross a reportability threshold, so no-report data need not refute cognitive theories. Check the logic in a minimal threshold toy. | V1 Pass; H1 Supported; H2 Supported |
| 2 | `8b7dd3b3` | Context for K14's 12-factor solution (92 items, 1,403 respondents): how many factors would common retention rules return if the items had NO structure? | V1 Pass; H1 Supported; R1 Reported |
| 3 | `feea3c7a` | With 12 true factors in 92 items and n = 1,403, how strong must loadings be for parallel analysis to recover 12, and what loading makes '12 components explain 44%' consistent? | V1 Pass; H1 Supported; H2 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: Report-confound model (K13).
- Pass 2: IIT testability (K12). The 2023 'pseudoscience' open letter itself was not found in Europe PMC (not read; not cited).
- Pass 3: Pure-awareness questionnaire structure (K14). Josipovic & Miskovic 2020 kept for Cycle B.

## Unresolved
- K13's model is one model; no empirical no-report dataset was read this cycle.
- No experiment testing IIT's silent-neuron predictions exists in the sources read.
- Whether 'pure awareness' factors replicate in an independent sample (K14 is one survey).
