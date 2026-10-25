# N-A Baseline: specification

This specification was written and pushed **before** the Baseline run. The method is in `../PLAN.md`, and the pre-registered checks are in `config.json`.

## Sources read in full for the Baseline
All were checked against their blob SHAs in `../ledger/ledger_c0.csv` (`read_c0 = full`):
- the Five-Level taxonomy (5L)
- the Phase A inventory
- the Synergy v3.0 ch. 28 editorial synthesis
- Original-Human-Consciousness (H-04)
- Integrity Courts
- the Documentation Control Standard
- `Tablets/INDEX.md` and the three `Tablets/MATRIX-*.md` files
- on the Foundation side: `Research/README.md` §2 and §9 and Work Queue §B, §C and §N

The 22 tablet files and the other 31 core reports are read as a **census only** in this cycle: status lines, seal lines and phase labels, extracted by the tool. They are read in full in x3 and x6. This is a limitation of the Baseline.

## Pass 1 (agent judgment)
- `schemes_c0.csv`: 16 vocabularies, 6 from the Foundation and 10 from GD. Each one names the extractor that re-derives it from its source.
- `crosswalk_c0.csv`: term-to-term rows.
  - Relations: same-name-same-sense, same-name-different-sense, partial-overlap, broader, narrower, different-kind, no-counterpart, internal-variant.
  - `(none)` is allowed only with no-counterpart or different-kind.
- `conflicts_c0.csv`: K1–K6 (the Work Queue's six bullets), each with a verdict of confirmed, refined or corrected.
- `options_c0.csv`: at least 2 options per conflict, always including one of type `defer`. The decision is always `open (Kyle)`.

## Pass 2 (tool)
See PLAN step 3. There is one iteration, rule `as_judged`.

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C0-1 | Mirror matches blob SHAs | ledger_mismatches | = 0 |
| C0-2 | Ledger ⊆ listing | ledger_not_in_listing | = 0 |
| C0-3 | Judged schemes equal extracted | scheme_extraction_mismatches | = 0 |
| C0-4 | Every scheme term crosswalked | crosswalk_unmapped_terms | = 0 |
| C0-5 | Judgment rows well-formed and labelled | problems | = 0 |
| C0-6 | Options rule (≥2, a defer, no decision) | options_violations | = 0 |
| C0-7 | Work Queue records six conflicts | wq_conflict_bullets | = 6 |
| C0-8 | WQ "Phase 1–7" holds | phase_max | = 7 |
| C0-9 | Reports' next-phase statements consistent | phase_next_mislabels | = 0 |
| C0-10 | WQ "8 flagged" reproduced from INDEX | index_flagged_discrepancies | = 8 |
| C0-11 | Foundation's two ladders agree | foundation_ladder_symdiff | = 0 |
| C0-12 | No 80-char overlap with suite or GD | boundary_overlaps | = 0 |

**Boundary scan (C0-12).** This is the PC-4 scan against the suite. Against GD, exact repository paths and basenames from `../ledger/listing.csv` are masked on both sides first, because a filename is a locator and not copied content. `../ledger/` is excluded, since it holds only paths, SHAs and sizes. Every other file in this folder is scanned, including this cycle's outputs.

C0-8 to C0-11 test **earlier claims**: the Work Queue's wording, the internal consistency of GD and the internal consistency of the Foundation. If one of them fails, that is a finding, not a method failure.

**Disclosure.** While the tool was being developed, its extractors were dry-run against the mirror. That dry run already indicated that C0-8, C0-9 and C0-11 would fail: the highest phase is 8, there are 2 mislabels, and the ladders differ by Power, Base and Quantum. The checks keep the thresholds the claims imply and are not re-thresholded.

## Gate
- PASS needs C0-1 to C0-7 and C0-12 to pass, plus identical reruns.
- C0-8 to C0-11 are reported as they fall.
- The crosswalk itself stays **Proposed**. Every resolution is Kyle's.
