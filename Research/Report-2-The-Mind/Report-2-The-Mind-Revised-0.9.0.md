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