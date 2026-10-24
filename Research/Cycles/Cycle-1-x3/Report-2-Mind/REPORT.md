# Report 2 — The Mind: perception, memory, learning, reasoning, emotion, identity

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-1-X3-R2 |
| Version | Cycle 1 (x3) |
| Status | Researched (3 passes), simulated (3 chained iterations, all executed), internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Builds on | `../../Cycle-0-Baseline/Report-2-Mind/REPORT.md` (Baseline v2) |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; GAIA Is the Motherthread) |
| Labels | Established / Plausible / Philosophical/Spiritual / Hypothetical |
| Cycle-1 access rule | Established literature claims need at least one full-text (or textbook) source; abstract-only claims are capped at Plausible |

## GAIA thread (Philosophical/Spiritual)
The motherthread frames this report as one aspect of Earth's living whole. That framing is a philosophical choice, labelled as such; every scientific claim below stands or falls on its own sources.

## Abstract
Cycle 1 upgrades the heuristics-and-biases and Many Labs 2 claims to full text, widens the replication picture (13 of 21 Nature/Science social-science experiments replicated, at about half the original effect size; abstract only), and adds three challenges: ecological rationality (heuristics can be accurate; less-is-more), the claim that constructed-emotion and basic-emotion theories are irreconcilable, and a critique of predictive processing as a premature unification. Simulations show where Rescorla–Wagner blocking holds (only 20% of the grid) and fails, reproduce RW's known failure on latent inhibition (ratio exactly 1, while a Pearce–Hall variant gives 0.89), and confirm with cross-validation that forgetting is better fit by power (Ebbinghaus) and log (replication) curves than by an exponential.

## What changed in Cycle 1
Pass 1: C0v2-R2-04 → V04 and C0v2-R2-12 → V05 (full text). Pass 2: V37 (replication), V11 (emotion). Pass 3: V34 (ecological rationality) and V35 (predictive-processing critique) as counter-evidence to Established and Plausible claims.

Ledger: 20 claims (10 E, 7 P, 3 PS, 0 H); 7 new, 2 revised; the rest carried forward unchanged from Cycle 0 (each row's `c1_change` says which).

## Methods
Three successive research passes (consolidate → widen → challenge; notes in `research/pass-1..3/NOTES.md`) and three chained simulation iterations (`simulation/iter-1..3`, each with `SPEC.md` and `params.json` written before execution, `outputs/results.json` and `EXECUTION_RECORD.json`; iterations 2 and 3 read the previous iteration's results). Sources were fetched directly, snapshotted, hashed (`../Provenance/SOURCE_REGISTER.csv`) and phrase-checked (`../Verification/`). Check kinds: *validation* (code correctness; must pass), *hypothesis* (substantive; Supported / Not supported — a 'not supported' result is a finding), *reporting* (value recorded).

## Evidence and findings
**Memory and learning.** The Ebbinghaus forgetting curve replicated (C0v2-R2-01); prediction-error learning explains blocking (C0v2-R2-02); spacing improves retention (C0v2-R2-03) — all Established, carried forward. Cross-validated refits agree with Cycle 0 (C1-R2-07).

**Reasoning.** Heuristics are economical and usually effective but produce systematic and predictable errors (C0v2-R2-04, Established, full text), while the ecological-rationality programme argues they can be accurate where cues are valid (C1-R2-02, Plausible/Contested).

**Reliability.** 36% of 100 psychology replications were significant (C0v2-R2-11); Many Labs 2 attributes variation more to the effect than to the sample (C0v2-R2-12, full text); 62% of 21 Nature/Science social-science studies replicated at about 50% of the original effect (C1-R2-01, Plausible — abstract only).

**Emotion, perception, identity, mind–body** remain Plausible or Philosophical/Spiritual (C0v2-R2-05..10), now with explicit counter-positions (C1-R2-03, C1-R2-04).

## Competing views and counter-evidence
Heuristics as bias vs as ecological rationality; constructed vs basic emotion; predictive processing as unifying theory vs a framework that unifies only 'by fiat'. None is resolved by the sources read.

## Simulation (3 iterations)
| Iteration | Purpose | Checks (id: result) | Validation | Hypotheses supported |
|---|---|---|---|---|
| 1 | Rescorla-Wagner blocking over learning rate x pretraining amount: where does blocking (ratio < 0.1) fail? | W1: Pass, W2: Supported | 1/1 | 1/1 |
| 2 | Challenge pass: a known failure of Rescorla-Wagner is latent inhibition (pre-exposure slows later learning). Compare RW with a Pearce-Hall-type associability model. | L1: Pass, L2: Supported | 1/1 | 1/1 |
| 3 | Refit the forgetting curves (S04 Table 3: Ebbinghaus 1885 and Murre & Dros 2015 savings) with leave-one-out CV and bootstrap, not AIC alone (C0 used AIC only). | F1: Supported, F3: Reported | 0/0 | 1/1 |

Iteration 1 (RW grid) → iteration 2 (latent inhibition challenge) → iteration 3 (forgetting-curve model selection with LOOCV and bootstrap instead of AIC alone). All pre-registered hypotheses were supported; this is reported as such and not taken as evidence beyond the toy models.

## Claim-to-source ledger (`claims/claims.csv`)
| ID | Label | Status | Claim | Sources | Cycle-1 change |
|---|---|---|---|---|---|
| C0v2-R2-01 | E | Supported | Memory: Ebbinghaus' savings-based forgetting curve was replicated in a single-subject study (about 70 h of learning; retention intervals 20 min to 31 days). | S04 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-02 | E | Supported | Learning: the Rescorla–Wagner model explains Kamin blocking through a shared prediction error; attention-related phenomena require extensions beyond RW. | S06 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-03 | E | Supported | Learning: a meta-analysis of 839 assessments of distributed practice (317 experiments, 184 articles) found that the inter-study interval producing maximal retention increases as the retention interval increases. | T03 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-04 | E | Supported | Reasoning/thought: judgments under uncertainty rely on heuristics (representativeness, availability, anchoring and adjustment) that are economical and usually effective but produce systematic, predictable errors. | V04;U10 | Upgraded to full text V04; counter-view C1-R2-02 linked. |
| C0v2-R2-05 | P | Contested | Perception/thought: predictive-processing accounts treat brains as hierarchical prediction machines minimizing prediction error; Clark judges this the best clue yet to a unified science of mind and action while setting out evidential and conceptual challenges. | U11 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-06 | PS | Contested | Perception (philosophy): illusion and hallucination generate the 'problem of perception'; sense-datum, adverbial, intentionalist and naive-realist/disjunctivist theories compete. | U15 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-07 | P | Contested | Emotion: theories fall into feeling, evaluative (incl. appraisal) and motivational traditions (incl. basic-emotion and constructionist views) that still compete; no single definition is settled. | U12 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-08 | PS | Contested | Identity: there is no single problem of personal identity; psychological-continuity views and animalism (we are biological organisms) are leading competing answers to the persistence question. | U13 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-09 | PS | Contested | Mind–body: the identity theory holds that mental states and processes are identical to brain states and processes; physicalism and dualism remain competing positions. | U14;T06;S08 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-10 | P | Mixed | Mind–body: interoceptive signalling links bodily state to feelings, drives and cognitive/emotional experience; its causal role in specific mental-health conditions is plausible but not settled. | T02 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-11 | E | Supported | Reliability of the evidence base: in 100 replications of psychology studies, 36% had significant results and effects were about half the original size. | S05 | Carried forward unchanged from Cycle 0 (v2). |
| C0v2-R2-12 | E | Supported | Across Many Labs 2, variability in observed effect sizes was attributable more to the effect studied than to the sample or setting. | V05;T04 | Upgraded to full text V05. |
| C0v2-R2-13 | E | Supported | In SIM-R2-C0, Rescorla–Wagner reproduced blocking (V_X 0.0004 vs 0.50 control); on Ebbinghaus' data power (AIC −50.7) and log (−45.1) fit better than exponential (−29.6); on the replication data log fit best (−43.4). | C0:SIM-R2-C0#E1;C0:SIM-R2-C0#E3;C0:SIM-R2-C0#E4 | Carried forward; cites the Cycle-0 run. Re-tested with LOOCV/bootstrap in C1-R2-07. |
| C1-R2-01 | P | Mixed | A replication of 21 social-science experiments published in Nature and Science (2010-2015) found a significant effect in the same direction for 13 (62%), with replication effect sizes on average about 50% of the originals. | V37 | New in Cycle 1. |
| C1-R2-02 | P | Contested | Counter-view to heuristics-as-error: the recognition-heuristic programme argues that recognition is often an ecologically valid cue and can produce a less-is-more effect, in which less recognition knowledge yields more accurate inferences; the extent of its use is debated. | V34 | New in Cycle 1. |
| C1-R2-03 | P | Contested | Emotion: proponents of the theory of constructed emotion argue that it and basic emotion theory are intrinsically irreconcilable because they rest on incommensurate assumptions. | V11 | New in Cycle 1. |
| C1-R2-04 | P | Contested | Challenge to predictive processing: Litwin & Miłkowski argue that presenting predictive processing as a unifying account of perception, action and cognition is premature, because it fails to deliver general, simple, homogeneous and systematic explanations. | V35 | New in Cycle 1. |
| C1-R2-05 | E | Supported | In SIM-R2-C1, Rescorla–Wagner blocking (blocked-cue strength < 0.1 of control) occurred in only 20% of the learning-rate x pretraining grid; it failed whenever pretraining was weak (e.g. learning rate 0.1 with 10 pretraining trials gave ratio 0.35). | SIM-R2-C1/iter-1#W1;SIM-R2-C1/iter-1#W2 | New in Cycle 1. |
| C1-R2-06 | E | Supported | In SIM-R2-C1, Rescorla–Wagner predicted no latent inhibition (acquisition ratio exactly 1), reproducing a known limitation, while a Pearce–Hall-type associability model gave ratio 0.89. | SIM-R2-C1/iter-2#L1;SIM-R2-C1/iter-2#L2 | New in Cycle 1. |
| C1-R2-07 | E | Supported | In SIM-R2-C1, refitting the S04 forgetting data with leave-one-out cross-validation agreed with AIC: power fit best for Ebbinghaus (LOOCV MSE 0.0014 vs exponential 0.022) and logarithmic for the Murre & Dros replication; power won 220 and log 171 of 271 usable bootstrap resamples for the respective datasets. | SIM-R2-C1/iter-3#F1;SIM-R2-C1/iter-3#F3;S04 | New in Cycle 1. |

## Relationships to other reports (link register)
| Link | From → To | Type | Label | Cycle-1 status |
|---|---|---|---|---|
| L04 | R1 Body → R2 Mind | dependency | E | Unchanged. |
| L05 | R1 Body → R2 Mind | feedback loop | P | Under pressure in the toy: the anticipatory benefit was not robust to parameter perturbation (T3 not supported). |
| L06 | R1 Body → R2 Mind | competing interpretation | PS | Unchanged. |
| L07 | R2 Mind → R5 Consciousness | relationship | P | Basis now contested by V35; label Plausible retained. |
| L08 | R2 Mind → R5 Consciousness | distinction | E | The conceptual distinction is retained as Established; whether phenomenal consciousness exists without access is the contested question (C1-R5-02). |
| L09 | R2 Mind → R3 Soul | competing interpretation | PS | Unchanged label; widened. |

## Limitations
Seven data points per forgetting dataset; our Pearce–Hall variant is simplified; replication rates come from specific literatures.

## Open questions and falsification
Which environments make heuristics accurate (testable: cue-validity manipulations)? Can predictive processing make a risky prediction that competing accounts do not?

## Conclusion and gate
Core cognitive findings are Established with full-text support; theoretical frameworks remain contested. Gate: **Indeterminate**.

## References
Sources cited by this report's ledger (`sources/sources.csv`; full register in `../Provenance/SOURCE_REGISTER.csv`):

- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) [full text (GitHub connector)] <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md>
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. [full text (owner-supplied file)] <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md>
- **S04** — Murre JMJ, Dros J (2015). Replication and Analysis of Ebbinghaus' Forgetting Curve. PLoS ONE 10(7):e0120644. doi:10.1371/journal.pone.0120644 [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/>
- **S05** — Open Science Collaboration (2015). Estimating the reproducibility of psychological science. Science 349:aac4716. doi:10.1126/science.aac4716 [full text (PDF hosted by Reed College)] <https://www.reed.edu/psychology/scalp/assets/journal-articles/OSC_RP_2015_Science.pdf>
- **S06** — Holland PC, Schiffino FL (2016). Mini-Review: Prediction errors, attention and associative learning. Neurobiol Learn Mem (PMC4862921). [full text (PMC)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC4862921/>
- **S08** — Robinson H, Weir R. Dualism. Stanford Encyclopedia of Philosophy (substantive revision 2025). [full text] <https://plato.stanford.edu/entries/dualism/>
- **T02** — Khalsa SS, Adolphs R, Cameron OG, et al. (2018). Interoception and Mental Health: A Roadmap. Biol Psychiatry Cogn Neurosci Neuroimaging 3(6):501-513. doi:10.1016/j.bpsc.2017.12.004 [full text (PMC6054486)] <https://pmc.ncbi.nlm.nih.gov/articles/PMC6054486/>
- **T03** — Cepeda NJ, Pashler H, Vul E, Wixted JT, Rohrer D (2006). Distributed practice in verbal recall tasks: a review and quantitative synthesis. Psychol Bull 132(3):354-380. doi:10.1037/0033-2909.132.3.354 [full text (author-hosted PDF)] <https://www.yorku.ca/ncepeda/publications/CPVWR2006.pdf>
- **T04** — Klein RA, Vianello M, Hasselman F, et al. (2018). Many Labs 2: Investigating Variation in Replicability Across Samples and Settings. Adv Methods Pract Psychol Sci 1(4):443-490. doi:10.1177/2515245918810225 [abstract only (APS journal page)] <https://www.psychologicalscience.org/journals/ampps/2515245918810225/>
- **T06** — Stoljar D. Physicalism. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/physicalism/>
- **U10** — Tversky A, Kahneman D (1974). Judgment under Uncertainty: Heuristics and Biases. Science 185(4157):1124-1131. doi:10.1126/science.185.4157.1124 [abstract only (NCBI E-utilities PMID 17835457)] <https://pubmed.ncbi.nlm.nih.gov/17835457/>
- **U11** — Clark A (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. Behav Brain Sci 36(3):181-204. doi:10.1017/S0140525X12000477 [abstract only (NCBI E-utilities PMID 23663408)] <https://pubmed.ncbi.nlm.nih.gov/23663408/>
- **U12** — Scarantino A, de Sousa R. Emotion. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/emotion/>
- **U13** — Olson ET. Personal Identity. Stanford Encyclopedia of Philosophy. [full text] <https://plato.stanford.edu/entries/identity-personal/>
- **U14** — Smart JJC. The Mind/Brain Identity Theory. Stanford Encyclopedia of Philosophy (rev. 2007). [full text] <https://plato.stanford.edu/entries/mind-identity/>
- **U15** — Crane T, French C. The Problem of Perception. Stanford Encyclopedia of Philosophy (rev. 2021). [full text] <https://plato.stanford.edu/entries/perception-problem/>
- **V04** — Tversky A, Kahneman D (1974). Judgment under uncertainty: heuristics and biases. Science 185(4157):1124-1131 (JSTOR scan hosted on a UC Irvine course page) [full text (PDF, third-party course host)] <https://sites.socsci.uci.edu/~bskyrms/bio/readings/tversky_k_heuristics_biases.pdf>
- **V05** — Klein RA, et al. (2018). Many Labs 2: Investigating variation in replicability across samples and settings. Adv Methods Pract Psychol Sci 1(4):443-490. doi:10.1177/2515245918810225 [full text (PDF, UvA-DARE repository)] <https://pure.uva.nl/ws/files/32817291/2515245918810225.pdf>
- **V11** — Barrett LF, et al. (2025). The theory of constructed emotion: more than a feeling. Perspect Psychol Sci. doi:10.1177/17456916251319045 [full text (Europe PMC PMC12164598)] <https://europepmc.org/article/PMC/PMC12164598>
- **V34** — Pachur T, Todd PM, Gigerenzer G, Schooler LJ, Goldstein DG (2011). The recognition heuristic: a review of theory and tests. Front Psychol 2:147. doi:10.3389/fpsyg.2011.00147 [full text (Europe PMC PMC3132682)] <https://europepmc.org/article/PMC/PMC3132682>
- **V35** — Litwin P, Miłkowski M (2020). Unification by fiat: arrested development of predictive processing. Cogn Sci 44(7):e12867. doi:10.1111/cogs.12867 [full text (Europe PMC PMC7378938)] <https://europepmc.org/article/PMC/PMC7378938>
- **V37** — Camerer CF, et al. (2018). Evaluating the replicability of social science experiments in Nature and Science between 2010 and 2015. Nat Hum Behav 2(9):637-644. doi:10.1038/s41562-018-0399-z [abstract only (NCBI E-utilities)] <https://doi.org/10.1038/s41562-018-0399-z>

## Change history
- Cycle 0 Baseline v2 (2026-10-24): see `../../Cycle-0-Baseline/`.
- Cycle 1 (x3) (2026-10-24): this version; details in `CHANGELOG.md`.
