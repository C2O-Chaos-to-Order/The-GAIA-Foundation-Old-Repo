# Report 2 — The Mind: the cognitive and psychological foundation

| Field | Value |
|---|---|
| Stable ID | GAIA-CYCLE-0-BASELINE-R2 |
| Version | Baseline v2 (Cycle 0, framework-aligned) |
| Status | Researched (1 bounded pass, framework-aligned); simulated (executed, see §Simulation); internally verified; **not independently reviewed** |
| Date | 2026-10-24 |
| Owner | Kyle Alexander Steen (repository owner); prepared by Grok Bot |
| Governing scope | `../FRAMEWORK.md` (Seven-Report Foundational Framework; organizing principle: GAIA Is the Motherthread) |
| Integrity rules | Research/README.md, Research/RESEARCH_PLAN_EXTENSION.md (@7875b4e) |
| Conclusion labels | Established / Plausible / Philosophical/Spiritual / Hypothetical (mapping to repository statuses: `../FRAMEWORK.md` appendix) |

## Abstract
The leading accounts of thought, memory, reasoning, emotion, perception, identity and learning, where they compete, and what remains open. Established: forgetting curves replicate; prediction-error learning explains blocking; spacing benefits retention with an optimal gap that grows with the retention interval; judgement relies on heuristics that produce systematic errors. Competing: predictive processing as a unified account of perception and action; three traditions in emotion theory; several theories of perception; psychological vs animalist accounts of identity; identity theory vs dualism on the mind–body relation. The evidence base itself is partly unreliable (36% replication). The simulation (executed, all checks passed) reproduces blocking and compares forgetting-curve forms.

## Contents
Purpose & exclusions · Research questions & definitions · Framework scope coverage · Methods · Evidence & findings · Competing theories · Simulation · Claim-to-source ledger · Relationships to other reports · Ethical implications · Limitations & counterevidence · Open questions & falsification · Conclusion · References · Change history

## Purpose and exclusions
Scope (framework, Report 2): thought, memory, reasoning, emotion, perception, identity, learning, and how mental processes relate to the body; domains cognitive science, psychology, neuroscience. Excluded: clinical psychology and therapy guidance; soul-based accounts of the self (Report 3).

## Research questions and definitions
1. What is established about memory and learning? 2. How do people reason under uncertainty? 3. What are the leading accounts of perception and of emotion, and where do they compete? 4. What makes a person the same over time? 5. How do mental processes relate to the body? 6. How reliable is the evidence base?

## Framework scope coverage
Every scope item the framework lists for this report, with the claims that address it.

| Framework scope item | Claims | Labels |
|---|---|---|
| Thought & reasoning | C0v2-R2-04; C0v2-R2-05 | Established, Plausible |
| Memory | C0v2-R2-01; C0v2-R2-13 | Established |
| Learning | C0v2-R2-02; C0v2-R2-03; C0v2-R2-13 | Established |
| Emotion | C0v2-R2-07 | Plausible |
| Perception | C0v2-R2-05; C0v2-R2-06 | Philosophical/Spiritual, Plausible |
| Identity | C0v2-R2-08 | Philosophical/Spiritual |
| Mind–body relation | C0v2-R2-09; C0v2-R2-10 | Philosophical/Spiritual, Plausible |
| Reliability of evidence | C0v2-R2-11; C0v2-R2-12 | Established |

## Methods
One bounded, framework-aligned research pass (2026-10-23/24) that reuses valid v1 sources and adds new ones. Sources were primary texts, primary studies, systematic reviews, specialist encyclopaedias (SEP, IEP), open textbooks and official assessments, found by targeted search and fetched directly. Each fetched page was snapshotted and its SHA-256 recorded; third-party text is not redistributed. Each claim is tied to the passage that supports it (locator) and labelled with a framework label plus a repository class/status. Where only an abstract or excerpt was accessible, the access mode says so. Every Established literature claim carries a verification phrase that was re-checked against a fresh fetch of its source (see `../Verification/VERIFICATION.md`). Simulations were specified in `simulation/SPEC.md` before execution and re-run fresh for v2.

## Evidence and findings
Label counts in this report's ledger: Established: 7, Plausible: 3, Philosophical/Spiritual: 3, Hypothetical: 0.

**Memory and learning.** Ebbinghaus' forgetting curve replicated (C0v2-R2-01); Rescorla–Wagner explains blocking via shared prediction error (02); spaced practice beats massed, with the best gap increasing with retention interval (03) — Established.

**Reasoning.** Judgement under uncertainty uses representativeness, availability and anchoring — economical, usually effective, but systematically biased (04, Established).

**Perception.** Predictive processing treats the brain as a hierarchical prediction machine (05, Plausible / contested); philosophically, illusion and hallucination generate the problem of perception with four competing theory families (06, Philosophical).

**Emotion.** Feeling, evaluative and motivational traditions still compete (07, Plausible / contested).

**Identity.** Psychological-continuity views vs animalism (08, Philosophical).

**Mind–body.** Identity theory vs dualism (09, Philosophical); interoception links bodily state to feeling and cognition (10, Plausible).

**Reliability.** 36% replication in the OSC project; in Many Labs 2 variation tracked the effect more than the sample (11–12, Established).

## Competing theories and alternatives
Learning: associative (RW) vs attention-based extensions (S06). Perception: predictive processing vs more modular views (U11 commentaries); philosophically sense-datum / adverbial / intentionalist / naive-realist (U15). Emotion: feeling vs evaluative/appraisal vs motivational/basic-emotion vs constructionist (U12). Identity: psychological continuity vs animalism vs constitution views (U13). Mind–body: identity theory/physicalism vs dualism (U14, T06, S08).

## Simulation
**SIM-R2-C0** — status: executed; run finished 2026-10-24T00:24:40Z; Python 3.13.5, NumPy 2.5.4, SciPy 1.18.1; all pre-registered checks passed: **True**.

| Check | Expectation | Observed | Result |
|---|---|---|---|
| E1 | V_X blocking < 0.1*V_X control | `[0.00039896132710136594, 0.49999999450244187]` | **Pass** |
| E2 | sum V on AX -> lambda | `[0.9999999999912268, 0.9999999890048837]` | **Pass** |
| E3 | Ebbinghaus: power or log AIC < exponential AIC | `{"exponential": -29.552, "power": -50.659, "log": -45.073}` | **Pass** |
| E4 | Dros: report only | `{"exponential": -37.279, "power": -38.441, "log": -43.385}` | **Pass** |

Specification (written before execution, incl. v2 changes and recorded deviations): `simulation/SPEC.md`; parameters: `simulation/params.json`; raw outputs: `simulation/outputs/` (SHA-256 in `simulation/EXECUTION_RECORD.json`). Simulation results are labelled Established only for the model itself, never for the real-world system.

## Claim-to-source ledger
Machine-readable: `claims/claims.csv` (includes verification phrases); sources: `sources/sources.csv`.

| ID | Claim | Framework label | Repo class / status | Sources | Locator | Confidence | Counterevidence / limits |
|---|---|---|---|---|---|---|---|
| C0v2-R2-01 | Memory: Ebbinghaus' savings-based forgetting curve was replicated in a single-subject study (about 70 h of learning; retention intervals 20 min to 31 days). | **Established** | Empirical / Supported | S04 | Abstract; Table 3 | High | n = 1; 31-day savings anomalously low. |
| C0v2-R2-02 | Learning: the Rescorla–Wagner model explains Kamin blocking through a shared prediction error; attention-related phenomena require extensions beyond RW. | **Established** | Empirical / Supported | S06 | RW and blocking section; attention discussion | High | RW is one of several learning models. |
| C0v2-R2-03 | Learning: a meta-analysis of 839 assessments of distributed practice (317 experiments, 184 articles) found that the inter-study interval producing maximal retention increases as the retention interval increases. | **Established** | Empirical / Supported | T03 | Abstract | High | Verbal recall tasks only. |
| C0v2-R2-04 | Reasoning/thought: judgments under uncertainty rely on heuristics (representativeness, availability, anchoring and adjustment) that are economical and usually effective but produce systematic, predictable errors. | **Established** | Empirical / Supported | U10 | Abstract | High | Later debate on 'ecological rationality' of heuristics not read in this pass. |
| C0v2-R2-05 | Perception/thought: predictive-processing accounts treat brains as hierarchical prediction machines minimizing prediction error; Clark judges this the best clue yet to a unified science of mind and action while setting out evidential and conceptual challenges. | **Plausible** | Empirical / Contested | U11 | Abstract | Medium | Open peer commentary (dozens of replies) contests scope and testability. |
| C0v2-R2-06 | Perception (philosophy): illusion and hallucination generate the 'problem of perception'; sense-datum, adverbial, intentionalist and naive-realist/disjunctivist theories compete. | **Philosophical/Spiritual** | Interpretive/philosophical / Contested | U15 | Opening; §3 contents | High (as description) |  |
| C0v2-R2-07 | Emotion: theories fall into feeling, evaluative (incl. appraisal) and motivational traditions (incl. basic-emotion and constructionist views) that still compete; no single definition is settled. | **Plausible** | Interpretive/philosophical / Contested | U12 | §2 'Three Traditions'; §§3–9 | High (as description) |  |
| C0v2-R2-08 | Identity: there is no single problem of personal identity; psychological-continuity views and animalism (we are biological organisms) are leading competing answers to the persistence question. | **Philosophical/Spiritual** | Interpretive/philosophical / Contested | U13 | §1; §§4, 7 | High (as description) |  |
| C0v2-R2-09 | Mind–body: the identity theory holds that mental states and processes are identical to brain states and processes; physicalism and dualism remain competing positions. | **Philosophical/Spiritual** | Interpretive/philosophical / Contested | U14;T06;S08 | U14 opening; T06; S08 | High (as description) |  |
| C0v2-R2-10 | Mind–body: interoceptive signalling links bodily state to feelings, drives and cognitive/emotional experience; its causal role in specific mental-health conditions is plausible but not settled. | **Plausible** | Empirical / Mixed | T02 | Abstract | Medium | Associational evidence; measurement challenges acknowledged by authors. |
| C0v2-R2-11 | Reliability of the evidence base: in 100 replications of psychology studies, 36% had significant results and effects were about half the original size. | **Established** | Empirical / Supported | S05 | Abstract/summary | High | Replication metrics are debated. |
| C0v2-R2-12 | Across Many Labs 2, variability in observed effect sizes was attributable more to the effect studied than to the sample or setting. | **Established** | Empirical / Supported | T04 | Abstract (APS page) | High | Abstract-level access only. |
| C0v2-R2-13 | In SIM-R2-C0, Rescorla–Wagner reproduced blocking (V_X 0.0004 vs 0.50 control); on Ebbinghaus' data power (AIC −50.7) and log (−45.1) fit better than exponential (−29.6); on the replication data log fit best (−43.4). | **Established** | Mathematical/computational / Supported | SIM-R2-C0#E1;SIM-R2-C0#E3;SIM-R2-C0#E4 | Report-2-Mind/simulation/outputs/results.json | High (computation) | Seven data points; two-parameter forms only. |

## Relationships to other reports
R1: nervous system and interoception (L04, L05). R5: prediction-error theories bridge learning, perception and consciousness (L07); access vs phenomenal distinction (L08). R3: personal identity vs soul (L09). GAIA motherthread: mind develops in a body embedded in an environment — framing only.

## Ethical implications
Replication rates (36%) caution against building policy or personal advice on single psychology findings, including in later Love-lens work.

## Limitations and counterevidence
Several sources are abstract-only (U10, U11, T04). Emotion, perception and identity are covered through specialist encyclopaedias, not primary experiments. Language, social cognition and development were not researched in this pass. Not independently reviewed.

## Open questions and falsification criteria
- Is predictive processing a unified theory or a framework? *Test:* distinct, risky predictions vs rivals. *Reject* if its predictions are matched by models without hierarchical prediction error.
- Which emotion theory best predicts cross-cultural data? Open.
- Personal identity and the mind–body relation: no empirical test decides; recorded as open.

## Conclusion with evidence classification
Established: memory/forgetting, prediction-error learning, spacing, heuristics and biases, replication rates. Plausible: predictive processing; interoception's causal role; emotion theories (competing). Philosophical/Spiritual: problem of perception, personal identity, mind–body relation. Unresolved: which accounts of perception, emotion and identity are right.

## References
- **G02** — KyleAlexanderSteen/The-GAIA-Foundation, Research/RESEARCH_PLAN_EXTENSION.md @ 7875b4e (blob d895748) <https://github.com/KyleAlexanderSteen/The-GAIA-Foundation/blob/7875b4e19061dc8ad0e7d9d5fbfecd34d4e459d8/Research/RESEARCH_PLAN_EXTENSION.md> (accessed 2026-10-23; full text (GitHub connector))
- **G03** — Steen KA. The Seven-Report Foundational Framework (for Grok), incl. 'GAIA Is the Motherthread' (owner instruction 2026-10-24). Copy at Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md. <Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md> (accessed 2026-10-24; full text (owner-supplied file); snapshot SHA-256 `2bad2984fe2109de…`)
- **S04** — Murre JMJ, Dros J (2015). Replication and Analysis of Ebbinghaus' Forgetting Curve. PLoS ONE 10(7):e0120644. doi:10.1371/journal.pone.0120644 <https://pmc.ncbi.nlm.nih.gov/articles/PMC4492928/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `4d690164934877ea…`)
- **S05** — Open Science Collaboration (2015). Estimating the reproducibility of psychological science. Science 349:aac4716. doi:10.1126/science.aac4716 <https://www.reed.edu/psychology/scalp/assets/journal-articles/OSC_RP_2015_Science.pdf> (accessed 2026-10-23; full text (PDF hosted by Reed College); snapshot SHA-256 `4387db34aa0a2633…`)
- **S06** — Holland PC, Schiffino FL (2016). Mini-Review: Prediction errors, attention and associative learning. Neurobiol Learn Mem (PMC4862921). <https://pmc.ncbi.nlm.nih.gov/articles/PMC4862921/> (accessed 2026-10-23; full text (PMC); snapshot SHA-256 `8596bd21fea7f671…`)
- **S08** — Robinson H, Weir R. Dualism. Stanford Encyclopedia of Philosophy (substantive revision 2025). <https://plato.stanford.edu/entries/dualism/> (accessed 2026-10-23; full text; snapshot SHA-256 `ab916c4bcb92e362…`)
- **T02** — Khalsa SS, Adolphs R, Cameron OG, et al. (2018). Interoception and Mental Health: A Roadmap. Biol Psychiatry Cogn Neurosci Neuroimaging 3(6):501-513. doi:10.1016/j.bpsc.2017.12.004 <https://pmc.ncbi.nlm.nih.gov/articles/PMC6054486/> (accessed 2026-10-23; full text (PMC6054486); snapshot SHA-256 `59856fef067f6301…`)
- **T03** — Cepeda NJ, Pashler H, Vul E, Wixted JT, Rohrer D (2006). Distributed practice in verbal recall tasks: a review and quantitative synthesis. Psychol Bull 132(3):354-380. doi:10.1037/0033-2909.132.3.354 <https://www.yorku.ca/ncepeda/publications/CPVWR2006.pdf> (accessed 2026-10-23; full text (author-hosted PDF); snapshot SHA-256 `c92a8df87942c804…`)
- **T04** — Klein RA, Vianello M, Hasselman F, et al. (2018). Many Labs 2: Investigating Variation in Replicability Across Samples and Settings. Adv Methods Pract Psychol Sci 1(4):443-490. doi:10.1177/2515245918810225 <https://www.psychologicalscience.org/journals/ampps/2515245918810225/> (accessed 2026-10-23; abstract only (APS journal page); snapshot SHA-256 `531de3c4db0ef9f5…`)
- **T06** — Stoljar D. Physicalism. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/physicalism/> (accessed 2026-10-24; full text; snapshot SHA-256 `830d9f12b87829ff…`)
- **U10** — Tversky A, Kahneman D (1974). Judgment under Uncertainty: Heuristics and Biases. Science 185(4157):1124-1131. doi:10.1126/science.185.4157.1124 <https://pubmed.ncbi.nlm.nih.gov/17835457/> (accessed 2026-10-24; abstract only (NCBI E-utilities PMID 17835457); snapshot SHA-256 `73175cef421acd96…`)
- **U11** — Clark A (2013). Whatever next? Predictive brains, situated agents, and the future of cognitive science. Behav Brain Sci 36(3):181-204. doi:10.1017/S0140525X12000477 <https://pubmed.ncbi.nlm.nih.gov/23663408/> (accessed 2026-10-24; abstract only (NCBI E-utilities PMID 23663408); snapshot SHA-256 `8035997068144673…`)
- **U12** — Scarantino A, de Sousa R. Emotion. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/emotion/> (accessed 2026-10-24; full text; snapshot SHA-256 `1496ec30482a5caa…`)
- **U13** — Olson ET. Personal Identity. Stanford Encyclopedia of Philosophy. <https://plato.stanford.edu/entries/identity-personal/> (accessed 2026-10-24; full text; snapshot SHA-256 `bed25f23b2d08844…`)
- **U14** — Smart JJC. The Mind/Brain Identity Theory. Stanford Encyclopedia of Philosophy (rev. 2007). <https://plato.stanford.edu/entries/mind-identity/> (accessed 2026-10-24; full text; snapshot SHA-256 `8d0e9b9e0810b272…`)
- **U15** — Crane T, French C. The Problem of Perception. Stanford Encyclopedia of Philosophy (rev. 2021). <https://plato.stanford.edu/entries/perception-problem/> (accessed 2026-10-24; full text; snapshot SHA-256 `eac31009e7ab3ed0…`)

## Change history
- **2026-10-24 — Baseline v2 (Cycle 0, framework-aligned).** Rewritten against FRAMEWORK.md. Added reasoning (C0v2-R2-04), perception (05, 06), emotion (07), identity (08), mind–body (09, 10), spacing (03), Many Labs 2 (12). v1 C0-R2-05 ('scope not researched') is closed. v1 claims C0-R2-01…04 map to C0v2-R2-01, 02, 11, 13. Sources added: U10–U15, T03, T04.
- 2026-10-23 — Baseline (Cycle 0) v1: first version, built mainly on Research/README.md and RESEARCH_PLAN_EXTENSION.md (v1 files are superseded in place; the full v1 text remains in this branch's git history, commits before the v2 push). The earlier GAIA-PRELIM v0.1.0 package was deleted from `main` by the owner (commits 802e17a, df9a561) and never contained committed per-report files; nothing from it is reused.
