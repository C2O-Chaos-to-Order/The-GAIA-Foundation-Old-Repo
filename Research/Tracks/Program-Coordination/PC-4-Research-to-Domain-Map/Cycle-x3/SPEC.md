# PC-4 Cycle x3: Specification

Written and pushed **before** any x3 change to the judgments and before the x3 run. Stacked on `research/pc4-c0` @ 40530e40. Method: `../PLAN.md`. Pre-registered checks: `config.json`.

## Passes (3)
1. **Charter-scope review.** Read section 2 (Scope) of every domain used as a primary, and of the domains named in the Baseline basis column, and test each primary against the scope text. Change a primary only when a scope line names the item's subject better than the current home; record every change with the scope line that justified it.
2. **Established by reference.** Where a Work Queue item other than the report itself names the domain (the PC-4 examples; the b7 cluster lines), set `named_in` to that item and label the mapping Established. The tool checks the reference mechanically. Record every place where the queue's naming and the judged primary disagree ("tensions"), and keep the judgment if the charter supports it.
3. **Matcher-disagreement review.** For every Baseline report where the matcher's top 3 contains no judged domain, decide keep or change, with a reason (`../judgments/review_x3.csv`). Compare the result with the gap check's b8 list of ten domains with no existing material.

## Iterations (3)
1. `charter` matcher, stemming, k = 3. 2. `title_purpose`. 3. `title`.

## New mechanical checks (enabled by `queue_named_checks`)
- `queue_named_missing`: items whose own text names a domain not in their judged set, plus b7 cluster members that carry none of the domains their cluster names (must be 0).
- `queue_named_not_primary`: items whose queue-named domains do not include the judged primary (reported as tensions, not failures).

## Pre-registered checks
| ID | Hypothesis | Metric | Test | Iterations |
|---|---|---|---|---|
| X3-1 | Inventory still complete | inventory_gap | = 0 | all |
| X3-2 | Every row passes integrity, including named_in references | problems | = 0 | all |
| X3-3 | No queue-named domain is missing | queue_named_missing | = 0 | all |
| X3-4 | Charter matcher agrees at least as well as Baseline | topk_primary_rate | ≥ 0.427 | 1 |
| X3-5 | Title and purpose alone still agree | topk_primary_rate | ≥ 0.35 | 2 |
| X3-6 | Titles alone agree | topk_primary_rate | ≥ 0.25 | 3 |
| X3-7 | At least 15 reports are Established | report_label_counts.Established | ≥ 15 | all |
| X3-8 | Reports with no domain do not increase | reports_no_domain | ≤ 2 | all |
| X3-9 | All 9 b7 proposals pass | clusters_ok | = 9 | all |

X3-7 is close to mechanical once pass 2 is done; it is a check that the references validate, not a discovery. X3-4 to X3-6 are genuine predictions. Changing primaries toward the charter scope could lower lexical agreement, so X3-4 may fail.

## Verification
As Baseline, plus `verify` of Baseline with the x3 tool (earlier cycles must still reproduce).
