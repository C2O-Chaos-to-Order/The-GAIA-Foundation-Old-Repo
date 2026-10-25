# Connection x12: specification

Written and pushed **before** the x12 run. The push includes:
- `config.json`;
- `../CONNECTION.md` (the consolidated report);
- the x12 additions to `../tools/conn.py`, behind the config key `x12` and the iteration flag `drop_reviewed`. The Baseline, x3, x6 and x9 records still reproduce byte-identically; this was checked before the push;
- `../judgments/*_x12.csv`.

## Reading
None added. x12 consolidates; the inputs are those of x9.

## Pass 1 (agent judgment)
- **`claims_x12.csv` and `links_x12.csv`:** the x9 rows carried unchanged (35 claims, 28 links), with `change_vs_prev` set to `carried`.
- **`factors_x12.csv`:** identical to x9.
- **`review_x12.csv`:** every x9 item is kept. The challenge is consolidation: is the item stated in `CONNECTION.md` as in the ledger? The x9 factor-row drops (F03/CONS, F09/SPIRIT) are carried. This is not a second adversarial review.
- **`../CONNECTION.md`:**
  - the answer in brief, the topics' objects, shared factors, differences, unity by the README §9.5 criterion, the six pairs, traditions and science, the phases, the owner's claims, the cycle record with disclosures and diminishing returns, and options for the owner;
  - a register row for every claim and link.

## Pass 2 (tool), x12 additions
- **Document check.** Every claim and link ID appears in `CONNECTION.md`, and the document names no unknown ID. Its label totals (`Claims by label: …`, `Links by label: …`) and every register row's label match the judgments. Every item has a register row.
- **Yield census across all five cycles.** Per cycle: new, changed and removed claims, links and factor rows, and new evidence claims (census, framing and owner claims excluded). The census reports whether evidence yield (new evidence claims plus new links) is non-increasing from x6 on, and whether x12 itself added or changed anything.
- **Twelve iterations.** The six x6 rules, `reviewed`, the four rules combined with the x9 factor-row drops (`drop_reviewed`), and `reviewed` with duplicate registrations merged:

  | # | Rule | Drops | Merge |
  |---|---|---|---|
  | 1 | as_judged | | |
  | 2 | strict | | |
  | 3 | established_only | | |
  | 4 | no_method | | |
  | 5 | no_tradition | | |
  | 6 | as_judged | | yes |
  | 7 | reviewed | yes | |
  | 8 | strict | yes | |
  | 9 | established_only | yes | |
  | 10 | no_method | yes | |
  | 11 | no_tradition | yes | |
  | 12 | reviewed | yes | yes |

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C12-1 to C12-17 | As C9-1 to C9-17 | | = 0 |
| C12-18 | Every ID in the document | document_missing_ids | = 0 |
| C12-19 | No unknown ID in the document | document_unknown_ids | = 0 |
| C12-20 | Document labels match | document_label_mismatches | = 0 |
| C12-21 | Every item has a register row | document_items_without_register_row | = 0 |
| C12-22 | Evidence yield non-increasing from x6 | yield_nonincreasing_from | = 1 |
| C12-23 | x12 adds or changes nothing | this_cycle_new_or_changed | = 0 |
| C12-24 | ≥ 1 factor in all four topics | unity_factors | ≥ 1 |
| C12-25 | ≥ 1 substantive or tradition factor in all four topics | unity_factors_substantive | ≥ 1 |
| C12-26 | Every pair has a Connection link | pairs_without_connection_link | = 0 |
| C12-27 | No 80-character overlap with the Totality Suite | boundary_overlaps | = 0 |

**Disclosure of prior knowledge.** Almost nothing here is open. That is the expected state of a consolidation cycle, and it is the diminishing-returns finding.
- **Integrity dry run.** C12-1 to C12-13 and C12-18 to C12-21 were dry-run, and all were 0.
- **C12-14 to C12-16.** PASS is foreseeable; x9's items are unchanged.
- **C12-17.** FAIL is foreseen (L07, L09).
- **C12-22 and C12-23.** Foreseeable from the judgment files (x6: 10 new evidence claims and 8 links; x9: 0 and 0; x12: nothing). They record the yield; they do not test it.
- **C12-24.** PASS expected in all 12 iterations.
- **C12-25.** Expected to PASS where F07 counts (1, 4, 6, 7, 10, 12) and FAIL in 2, 3, 5, 8, 9 and 11.
- **Expected factors in all four topics** under the review-adjusted rules 7–12: F01, F02, F04, plus F07 where PS bases count. Iteration 10 (no_method with drops) is expected to leave only F07.
- **Open.** C12-27 covers the new `CONNECTION.md`.

No threshold was set after seeing a result.

## Maps & Matrix
v43 (`v43-cycles-0-4-mr-track-abcd-phases-x12-conn0abcd`), built from the unchanged `phases maps` base plus the x12 overlay (iteration 7 record for `validation/`). v1–v42 are not modified.

## Gate
- PASS needs C12-1 to C12-16, C12-18 to C12-21, C12-24, C12-26 and C12-27 in every iteration. It also needs identical reruns of all five cycles (worktree and fresh clone), the Maps rebuild, manifests, the validator and tests.
- C12-17, C12-22, C12-23 and C12-25 are reported as they fall.
- Content stays Proposed, gate INDETERMINATE.
