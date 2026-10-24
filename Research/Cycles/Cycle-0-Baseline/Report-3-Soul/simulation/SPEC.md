# SIM-R3-C0 — Inter-tradition soul-concept overlap (Baseline v2 specification, written before the v2 run)

**Status:** Specified 2026-10-24 before execution. Class: Mathematical/computational applied to an *interpretive* single-coder coding. It measures similarity between descriptions of doctrines as coded here; it says nothing about whether any soul exists.

## Question
Across 14 conceptions from the traditions the framework names (Greek ×4, Hebrew Bible, Christian, Islamic, Hindu ×2, Buddhist, Chinese, African, Indigenous, contemporary physicalism), which share attribute profiles on the framework's soul topics (identity, moral character, purpose, independence from body), and is any grouping robust to the coder's own flagged uncertainty?

## Inputs
`coding.csv`: 14 conceptions × 12 binary attributes (A1 immaterial … A12 extends to non-human beings), each row with the source(s) read; `uncertain_cells` lists cells the coder judged uncertain (36 cells). Coding by one coder (Grok Bot) from the cited passages only; several rows rest on one or two verses (C05, C07, C08) and therefore under-describe the tradition.

## Algorithm
Jaccard distance; average-linkage hierarchical clustering; cut at k = 4. Robustness: 20,000 Monte Carlo draws, each uncertain cell flipped independently with p = 0.5 (seed 20261024); record how often the base partition recurs and pairwise co-clustering frequency. (v1 enumerated all 2^12 combinations; with 36 uncertain cells enumeration is infeasible, hence Monte Carlo.)

## Pre-registered checks
- E1: matrix complete (14×12) and every row sourced.
- E2: robustness fraction and stable pairs (co-clustering ≥ 0.8) reported (reporting check; always Pass if produced).
- E3: no single attribute is shared by all 14 conceptions.

## Interpretation rule (fixed before running)
Base partition reproduced in ≥ 50% of draws → "robust to flagged uncertainty"; otherwise "coding-sensitive (Indeterminate)". Either way the result is labelled Philosophical/Spiritual: it is a structured comparison of beliefs, not evidence about the soul.

## Failure criteria
E1 or E3 fail → recorded as Fail; no re-coding after seeing results without a recorded deviation.

## v1 specification (superseded, kept for the record)
## SIM-R3-C0 — Inter-tradition soul-concept overlap analysis (specification, written before execution)

**Status:** Specified before execution. Class: **Interpretive coding + computation.** This is NOT a simulation of a soul and says nothing about whether a soul exists. It measures how similar *documented conceptions* are, given an explicit, single-coder interpretive coding.

### Question
Given 9 documented conceptions of soul/self and 10 attributes, which conceptions cluster together, and how robust is that clustering to the cells the coder marked uncertain?

### Inputs
`coding.csv` — 9 conceptions × 10 attributes, values 1/0, with a parallel `uncertain` flag and the source ID for each conception (S07 Plato/Aristotle/Epicurus/Stoics; S08 Cartesian & hylomorphic dualism, physicalism; S31 Advaita Vedānta; S32 Indian Buddhist anātman). Coder: Grok Bot (single, unvalidated, no inter-rater reliability).
Gap recorded: Hebrew Bible *nephesh* was planned but no fetchable source was obtained in this pass; excluded rather than coded from memory.

### Algorithm
Jaccard similarity on attribute presence; average-linkage hierarchical clustering; cut at 3 clusters. Robustness: enumerate all 2^u combinations of the u uncertain cells, recompute the 3-cluster partition, and report (i) the fraction of combinations reproducing the base partition, (ii) pairwise co-clustering frequency.

### Expected outputs / failure criteria
- E1: coding matrix complete (no blanks) and every conception has a source ID.
- E2: robustness is reported, whatever it is. If base partition reproduced in < 50% of combinations, the clustering result is classified **Indeterminate (coding-sensitive)**; otherwise **Interpretive (robust to flagged uncertainty only)**.
- Not tested: validity of the attribute set, coder bias, translation issues.
