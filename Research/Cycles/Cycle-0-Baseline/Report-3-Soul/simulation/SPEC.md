# SIM-R3-C0 — Inter-tradition soul-concept overlap analysis (specification, written before execution)

**Status:** Specified before execution. Class: **Interpretive coding + computation.** This is NOT a simulation of a soul and says nothing about whether a soul exists. It measures how similar *documented conceptions* are, given an explicit, single-coder interpretive coding.

## Question
Given 9 documented conceptions of soul/self and 10 attributes, which conceptions cluster together, and how robust is that clustering to the cells the coder marked uncertain?

## Inputs
`coding.csv` — 9 conceptions × 10 attributes, values 1/0, with a parallel `uncertain` flag and the source ID for each conception (S07 Plato/Aristotle/Epicurus/Stoics; S08 Cartesian & hylomorphic dualism, physicalism; S31 Advaita Vedānta; S32 Indian Buddhist anātman). Coder: Grok Bot (single, unvalidated, no inter-rater reliability).
Gap recorded: Hebrew Bible *nephesh* was planned but no fetchable source was obtained in this pass; excluded rather than coded from memory.

## Algorithm
Jaccard similarity on attribute presence; average-linkage hierarchical clustering; cut at 3 clusters. Robustness: enumerate all 2^u combinations of the u uncertain cells, recompute the 3-cluster partition, and report (i) the fraction of combinations reproducing the base partition, (ii) pairwise co-clustering frequency.

## Expected outputs / failure criteria
- E1: coding matrix complete (no blanks) and every conception has a source ID.
- E2: robustness is reported, whatever it is. If base partition reproduced in < 50% of combinations, the clustering result is classified **Indeterminate (coding-sensitive)**; otherwise **Interpretive (robust to flagged uncertainty only)**.
- Not tested: validity of the attribute set, coder bias, translation issues.
