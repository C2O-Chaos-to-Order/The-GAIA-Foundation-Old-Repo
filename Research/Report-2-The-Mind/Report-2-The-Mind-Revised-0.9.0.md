# Report 2 — The Mind
## Revised Version 0.9.0 — Embodied Learning and Interoceptive Arbitration

**Revision date:** 2026-10-23  
**Status:** Research-updated draft; independent review pending  
**Change type:** Computational specification and evidence calibration  
**Risk level:** Low  
**Repositories affected:** `KyleAlexanderSteen/The-GAIA-Foundation`  
**Supersedes:** Revised 0.8.0 (preserved)

## Scope
“Mind” refers to interacting capacities including perception, attention, memory, learning, affect, planning, language, metacognition, and action control. No single computational vocabulary should be treated as a complete explanation of all these capacities.

## Complementary learning families
- **Predictive processing / active inference:** generative models, uncertainty, precision, prediction errors, and action.
- **Reinforcement learning:** policy and action updating based on reward, cost, and prediction error.
- **Hebbian plasticity:** changes in connections or representations associated with coordinated activity.

These frameworks overlap but are not synonyms. Models should state which mechanism produces each prediction and compare against simpler rivals.

## Two routes to interoceptive prioritisation
The 2026 IWAI study distinguishes (1) **likelihood precision**, which weights sensory evidence about bodily state and can sharpen posterior estimates, and (2) **preference reweighting**, which changes the desirability of bodily outcomes and thus which states an agent visits during learning. In a foraging gridworld, precision sharpened interoceptive inference and improved survival; preference reweighting changed the state distribution learned. In 72 further layouts, the predicted preference benefit on difficult layouts was not established, while both interventions improved average survival and interacted positively. https://stjohngrimbly.com/iwai2026/

A formula such as `P_i = α γ_i + (1 − α) ρ_i` is only a proposed model form, not a validated physiological law. Similarly, an arbitration policy combining predictive, reward, and Hebbian error terms requires operational definitions, parameter-identifiability analysis, and preregistered outcomes before it is executable or falsifiable.

## Proposed test
Manipulate precision and preference independently in a factorial design. Measure interoceptive discrimination/calibration, preference-sensitive choice, action policy, regulation/survival, and coverage/accuracy of the learned bodily model separately. Include manipulation checks, channel ablations, matched controls, and out-of-distribution transfer. A null dissociation is informative only if the intended variables changed successfully.

## Biological grounding and boundaries
A whole-cell model of JCVI-syn3A integrates metabolism, genetic information processes, growth, and division across a complete cell cycle, with experimentally compared outputs and cell-to-cell heterogeneity. It illustrates bottom-up model integration, but it is not a model of a human mind. https://doi.org/10.1016/j.cell.2026.02.009

**Supported in bounded contexts:** bodily state affects adaptive behaviour; multiple computational mechanisms contribute to learning; precision and preference can be distinguished in a particular agent model. **Provisional:** IELF as a unified architecture and direct mapping to human neural circuits. **Not established:** computational self-modeling implies phenomenal consciousness, soul, or spirit.

## Readiness
Research update filed. No new numerical simulations were executed. Formal implementation, parameter sweeps, and independent replication remain pending.

---

# Addendum — Five-Phase Meta-Architecture Governance Integration (v0.9.0)

**Change type:** Cross-report governance integration  
**Risk level:** Moderate; conceptual update only  
**Evidence status:** Research-grounded design proposal; independent validation pending  
**Simulation status:** No simulations executed; no numerical output presented as evidence  
**Implementation:** Not authorized

## Purpose

This report contributes **Cognition, computation, memory, affect, and interoceptive arbitration** to the Transformative Intelligence governance architecture. The five phases now function as governance operations:

1. **Divergence — generation:** preserve relevant perspectives and record claim type, evidence, provenance, and uncertainty.
2. **Insurgence — contestation:** challenge core commitments using predeclared criteria; retain rival positions and document the outcome.
3. **Allegiance — stabilization:** adopt provisional working standards with review dates, anomaly triggers, and revision conditions.
4. **Convergence — integration:** connect compatible findings without silently erasing meaningful differences; record information lost or left unresolved.
5. **Ascendence — meta-evaluation:** evaluate the process and specify how conclusions reconnect to first-order evidence or accountable review.

## Report-specific governance rule

Type claims as computational model, behavioural observation, neural correlate, causal mechanism, or philosophical interpretation. Model fit alone does not establish identity between a computational description and a mental process.

## Minimum claim record

For consequential claims, record the exact claim; claim type; source and provenance; method and scope; uncertainty; counterevidence and rival explanations; decision relevance; and review or revision trigger. A source supporting one claim type does not automatically support a stronger causal, normative, or metaphysical conclusion.

## Controls

| Control | Requirement | Failure signal |
|---|---|---|
| Generation record | Each included perspective declares its evidential basis and limits | Inclusion or exclusion lacks a traceable rationale |
| Challenge protocol | Define success and potential disconfirmation before evaluation | Criteria shift after results to protect a preferred position |
| Commitment review | Record owner, scope, review date, and anomaly triggers | A commitment persists without review or is retired arbitrarily |
| Loss ledger | Document distinctions merged, omitted, or judged incomparable | Synthesis implies equivalence while concealing material differences |
| Re-entry condition | Meta-level recommendations connect to a checkable observation or review | Meta-level conclusions cannot be affected by first-order evidence |
| Dissent and appeal | Preserve minority reports and reasoned challenges | Governance suppresses disagreement instead of adjudicating it |

## Readiness

- **Document integration:** added to this report.
- **Source verification:** claim-by-claim audit remains pending; earlier citations are not automatically certified by this addendum.
- **Independent disciplinary review:** pending.
- **Simulation execution and numerical validation:** pending; none executed for this update.
- **Implementation:** not authorized.

The prior 0.8.0 report is preserved. This addendum does not claim the five-phase architecture is a universal law or empirically validated controller.


---

## Addendum — Hypergraph Architecture Integration (v4.0.0)

**Purpose:** connect cognition, computation, memory, and affect to the proposed hypergraph governance model.

- **Vertices and relations:** distinguish cognitive claims, task representations, memory traces, source records, inference rules, and uncertainty. Use typed hyperedges for dependencies that jointly involve context, prior information, task, and evaluator.
- **Divergence and insurgency:** keep alternative models and counterexamples available. Predeclare what would count as a discriminating result; an adversarial game reaching agreement does not establish truth.
- **Allegiance and recursive governance:** model reasoning policies as versioned, reviewable commitments. Changes to the inference framework must preserve old baselines and explain which conclusions change.
- **Convergence:** integrate psychological, computational, and physiological descriptions only with explicit mappings and a loss ledger; avoid treating analogy as mechanism.
- **Meta-wisdom invariant:** make the observer and the observation procedure auditable, including selection effects, blind spots, and changes to evaluation criteria.
- **Testable failure cases:** circular self-validation; unlogged changes to inference rules; hidden evidence selection; compression that erases dissent or uncertainty.

**Evidence status:** conceptual integration only. Source verification and independent disciplinary review remain pending; no simulation or numerical validation was executed for this addendum; implementation is not authorized. Prior report content is preserved.

## Addendum — v5.0.0 Engineered-Invariant Integration: The Mind

Map claims about cognition, learning, memory, reasoning, and agency as typed nodes linked to primary evidence, assumptions, competing explanations, and counterevidence. Distinguish empirical cognitive science from normative models, computational metaphors, and speculative claims. Recursive self-evaluation cannot be treated as complete access to the mind or as independent evidence for its own conclusions.

The invariant contract requires scope discipline, provenance, adversarial challenge, and exogenous review. A metric such as the proposed Measure Centrality Index must have a defined construct, formula, data requirements, and validity/sensitivity analysis before numerical results are reported. This addendum records design requirements only; no cognitive simulation, numerical result, proof, or implementation is claimed.


---

## Addendum — v7.0.0 Quantum Entanglement Upgrade: The Mind

**Change type:** Cross-report research integration; **risk:** high epistemic risk if quantum terminology is conflated with physical evidence; **execution:** no code or simulation executed; **implementation:** not authorized.

The v7.0.0 proposal allows context-sensitive and relational models of cognition and affect, including quantum-like formalisms where justified. The 2026 cognitive-affective CHSH article describes a proposed empirical design; do not report |S| = 2√2 as observed without completed data and reproducible analysis. A likelihood ratio compares explicit hypotheses and is not an entanglement-strength metric by definition. Compare classical dependence and common-cause alternatives.

Distinguish physical quantum entanglement, quantum-like formalism, empirical non-quantum coupling, and philosophical interpretation. Full specification: [v7.0.0](../Transformative-Intelligence-Five-Phase-Meta-Architecture/Transformative-Intelligence-Five-Phase-Meta-Architecture-Revised-7.0.0.md).

**Readiness:** documentation integration only; source audit, formal validation, simulation, empirical replication, and independent review remain pending. Prior content preserved.


---

## v8.0.0 Sentience as Recursive Relationality Addendum: The Mind

**Status:** conceptual/research integration; no code, simulation, or numerical validation performed for this addendum; implementation not authorized.

v8.0.0 distinguishes self-reference, metacognition, recurrence, agency, and phenomenal sentience. Quantum-like models of cognition or affect do not by themselves demonstrate physical quantum processing or subjective experience. Any CHSH claim requires a defined protocol, data, uncertainty, assumptions, classical alternatives, and replication; 2√2 is the standard theoretical maximum, not an observed result for this architecture.

**Cross-report control:** distinguish physical quantum entanglement, quantum-like formalisms, ordinary physiological or systems coupling, operational capacities, and claims about subjective experience. Preserve source provenance, uncertainty, counterevidence, and domain-specific definitions. See [the v8.0.0 specification](../Transformative-Intelligence-Five-Phase-Meta-Architecture/Transformative-Intelligence-Five-Phase-Meta-Architecture-Revised-8.0.0.md). Prior report content is preserved; full source audit and independent review remain pending.

---

## Source-Audit Addendum — Cognitive Models and Inference (2026-10-23)

### Findings and corrections

1. **Predictive processing, active inference, reinforcement learning, and Hebbian plasticity are not synonyms.** Predictive-processing accounts emphasize prediction and error minimization; active-inference formulations add a particular account of action and preferred outcomes; reinforcement learning studies value-guided policy updating; Hebbian rules describe activity-dependent changes in connections. A combined architecture must identify which formal mechanism generates each prediction rather than using the labels interchangeably.

2. **Distinguish model demonstration from human evidence.** The report's interoceptive-prioritisation gridworld results are evidence about the specified simulated agent, assumptions, reward structure, and layout distribution. They do not establish that the same intervention improves human survival, cognition, or health. Generalization requires preregistered human or animal tests and comparison against simpler baselines.

3. **Metacognition is not equivalent to consciousness.** Confidence judgments, error monitoring, self-models, reportability, and subjective experience overlap but are separable constructs. Measures should state whether they test behavioral calibration, access to information, or phenomenal experience.

4. **Causal alternatives matter.** Correlation among body state, neural activity, and behavior may reflect feedback, common inputs, learning history, or measurement artefacts. Causal claims require interventions, temporal predictions, controls, and robustness checks.

### Source anchors

- Seth & Bayne, “Theories of consciousness,” *Nature Reviews Neuroscience* 23 (2022), https://www.nature.com/articles/s41583-022-00587-4. This review emphasizes that prominent theories differ in their commitments and that empirical discriminability is a central requirement.
- Libretti & Puckett, *Physiology, Homeostasis* (StatPearls/NCBI Bookshelf), https://pubmed.ncbi.nlm.nih.gov/32644564/, for dynamic regulation as a physiological baseline.

**Evidence status:** general distinctions are supported by established research practice; this addendum does not independently validate the report's custom agent model. Formal replication, ablation studies, sensitivity analysis, and human generalization remain pending. No new simulation was run.


## Targeted source-audit checkpoint — 2026-10-23

**Scope of this pass:** interoception, embodied self-awareness, and active inference as theoretical framing.

- Wang & Chang, “The Coding Logic of Interoception,” *Annual Review of Physiology* 86 (2024), 301–327, DOI https://doi.org/10.1146/annurev-physiol-042222-023455, describes interoception as distributed sensing of internal bodily signals and emphasizes links with homeostasis, motivation, autonomic function, cognition, and behavior. The review also notes unresolved questions about system-level signal coding.
- “Interoception, network physiology and the emergence of bodily self-awareness,” *Neuroscience & Biobehavioral Reviews* 165 (2024), article 105864, DOI https://doi.org/10.1016/j.neubiorev.2024.105864, supports treating bodily self-awareness as involving interacting interoceptive and broader physiological networks, rather than a single isolated signal.
- Pezzulo, Parr & Friston, “Active inference as a theory of sentient behavior,” *Biological Psychology* (2024), DOI https://doi.org/10.1016/j.biopsycho.2023.108741, is a theoretical review of active inference. It supplies a modeling framework, not by itself proof that any particular system is sentient.

**Correction boundary:** distinguish measurable interoceptive physiology, cognitive/behavioral models, and phenomenal consciousness. A successful model of regulation or action does not establish subjective experience. Any custom agent or arbitration model in this report needs explicit variables, comparison baselines, ablations, sensitivity analysis, and replication before it can be treated as validated.

**Remaining:** full claim-by-claim source audit, model specification review, and independent neuroscience/cognitive-science review. No new simulation was run. Status remains OPEN.
