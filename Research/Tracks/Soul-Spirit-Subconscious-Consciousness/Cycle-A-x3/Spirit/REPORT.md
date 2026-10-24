# Spirit — Track Cycle A (x3)

Track: Soul, Spirit, Subconscious and Consciousness (`../../README.md`). Scope and boundary: `../../FRAMEWORK.md` § Spirit. Labels: **E** Established · **P** Plausible · **PS** Philosophical/Spiritual · **H** Hypothetical. GAIA is the motherthread (PS framing) and is kept separate from the science.

## Reading of this cycle
Cycle A added self-transcendent experience. Mystical-type experience can be measured with acceptable psychometric fit (K04), but widely cited experimental effects of awe were not reproduced in six studies (K05). SIM-SPIRIT-A shows that three failed replications argue against medium effects more than small ones (H1 not supported), and that binary 'complete experience' classifications are noisy (H1 not supported). The hypothesis that awe links spirituality to well-being stays Hypothetical.



## Claims (ledger: `claims/claims.csv`)
- **TA-SPIRIT-01** [E] In English validation data (280 measurements, 145 healthy participants, four placebo-controlled psilocybin studies), the four-factor Mystical Experience Questionnaire (MEQ30) and the six-factor MEQ40 showed acceptable to good confirmatory fit, and six of the eight Psychedelic Experience Scale subscales showed high internal consistency. *Sources:* K04. *Limits:* Drug-context sample; psychometric fit says the questionnaire measures reports consistently, not what the experiences are of. *Deepens:* R4:C0v2-R4-06;R4:C0v2-R4-11.
- **TA-SPIRIT-02** [E] Graziosi et al. (2026) did not reproduce reported effects of experimentally induced awe on agency detection, prosocial behaviour or well-being across online, laboratory and virtual-reality inductions, including three online direct replications with 2.5 times the original sample sizes. *Sources:* K05. *Limits:* Mostly online (MTurk) samples; induction strength can differ from originals. *Deepens:* R4:C0v2-R4-08.
- **TA-SPIRIT-03** [E] In SIM-SPIRIT-A (illustrative originals of 50 per group, published only if p < .05), published effects averaged d = 0.48 when the true effect was zero; a replication at 2.5x n has power .35 for a true d = 0.2, so three failed replications still have probability .27 (pre-registered H1 of < .10: not supported). A run of failures like K05's argues against medium effects (d = 0.3: .04) more than against small ones. *Sources:* SIM-SPIRIT-A/iter-1#V1;SIM-SPIRIT-A/iter-1#H1;SIM-SPIRIT-A/iter-1#H2. *Limits:* Illustrative n0; equal-variance normal model. *Deepens:* R4:C0v2-R4-08.
- **TA-SPIRIT-05** [E] In SIM-SPIRIT-A, a binary 'all four subscales above a cut' classification was unstable even with subscale reliability .90: only 72% of people classified at test were classified again at retest (kappa .67; pre-registered H1 of at least 80%: not supported). Binary 'complete experience' counts carry more measurement noise than the subscale reliabilities suggest. *Sources:* SIM-SPIRIT-A/iter-2#V1;SIM-SPIRIT-A/iter-2#H1. *Limits:* Illustrative cut (60th percentile on each subscale), not the published criterion, which was not read. *Deepens:* R4:C0v2-R4-11.
- **TA-SPIRIT-06** [E] In SIM-SPIRIT-A, with no true effect, testing four outcome families without correction yields at least one significant result in 18% (uncorrelated) to 14% (r = .6) of simulated two-group studies. *Sources:* SIM-SPIRIT-A/iter-3#V1;SIM-SPIRIT-A/iter-3#H1. *Limits:* Generic; not an audit of any original study. *Deepens:* R4:C0v2-R4-08.
- **TA-SPIRIT-04** [P] Keltner & Monroy (2026) review evidence that awe is a distinct emotion expressed in mouth and gaze activity, vocal bursts and upward head orientation with 'some degree of universality' (in one paradigm, five cultures overlapped in 63% of awe-expression elements) and elaborated culturally in choral music, dance and art of the sublime. *Sources:* K06. *Limits:* Narrative review by proponents of the basic-emotion approach. *Deepens:* R4:C0v2-R4-06.
- **TA-SPIRIT-07** [PS] Transcendence (descriptive): traditions describe mystical experience as contact with or realisation of a reality beyond ordinary experience (S15, which excludes paranormal experiences). Questionnaires such as the MEQ measure how people report such experiences; whether the experienced reality exists is a philosophical and spiritual question the measurements do not settle. *Sources:* S15;K04;G03. *Limits:* Interpretive. *Deepens:* R4:C0v2-R4-06;R4:C0v2-R4-15.
- **TA-SPIRIT-08** [H] Hypothesis: self-transcendent emotions such as awe are one pathway linking spirituality to well-being (Report 4). After K05's failed replications, this remains a hypothesis without robust experimental support; it would be tested by preregistered, adequately powered induction studies with manipulation checks. *Sources:* K05;K06;S11. *Limits:* Not tested here. *Deepens:* R4:C0v2-R4-08;R4:C0v2-R4-14.

## Simulations (SIM-SPIRIT-A; 3 iterations, spec-first; validation 3/3, hypotheses supported 2/4)

| iter | params | purpose | checks |
|---|---|---|---|
| 1 | `ee1d2cf3` | K05 failed to reproduce several awe effects, including three direct replications at 2.5x the original samples. How strong is a run of three failures as evidence against a small true effect, and how inflated would published originals be under selection? | V1 Pass; H1 Not supported; H2 Supported; R1 Reported |
| 2 | `e146bdbc` | Mystical-experience research often turns four MEQ30 subscales into a binary 'complete' experience by a cut on every subscale. With the high internal consistency K04 reports, how stable is such a binary across two measurements? | V1 Pass; H1 Not supported; R1 Reported |
| 3 | `eea6e5bf` | Original awe experiments reported effects on several outcome families (agency detection, prosociality, well-being, supernatural belief: K05). Under no true effect, how often is at least one of four outcomes significant? | V1 Pass; H1 Supported; R1 Reported |

Each `simulation/iter-k/SPEC.md` was written before execution and holds the parameters; `EXECUTION_RECORD.json` holds results, checks and hashes. 'Not supported' is a finding, not an error.

## Research passes (3; details `research/PASSES.md`)
- Pass 1: K04: MEQ30/MEQ40 English validation.
- Pass 2: K05: failed replications of awe effects (counter-evidence); K06: awe expression review. The 'self-transcendent experience varieties' query returned nothing usable (psychedelic-therapy and nature-relatedness papers outside scope).
- Pass 3: Nothing new: S15 already carried in Report 4 (C0v2-R4-06); reused for the boundary claim TA-SPIRIT-07.

## Unresolved
- The standard MEQ30 'complete mystical experience' criterion was not read in a source; SIM-SPIRIT-A used an illustrative cut.
- Original sample sizes and effects of the awe studies K05 replicated (would sharpen SIM-SPIRIT-A).
- Expectancy and blinding in psychedelic studies that use the MEQ (not yet searched).
