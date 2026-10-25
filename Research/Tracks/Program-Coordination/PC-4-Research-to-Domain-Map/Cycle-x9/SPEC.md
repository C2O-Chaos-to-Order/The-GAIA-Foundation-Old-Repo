# PC-4 Cycle x9: Specification

Written and pushed **before** any x9 change and before the x9 run. Stacked on `research/pc4-x6` @ 5fef31b6. Pre-registered checks: `config.json`. Expectation stated in advance: **x9 should add little.** The map's primaries did not change in x6.

## Passes (9)
1. **ToG §6 item 3 re-read** (carried from x6). Decide, with a reason, whether epistemic governance ("claim classes … forbidden overstatement") reaches TOT-038 and TOT-023.
2. **Candidate effect.** Which no-primary domains would candidate reports fill if the owner approved them (`candidate_fills_primary`)?
3. **Chance baseline for the matcher.** 500 label permutations per iteration (fixed seed). Is agreement above chance?
4. **Per-section agreement.** Matcher agreement by Work Queue section, to show where the lexical check is blind.
5. **Source check of finished reports.** Read the README or opening of each finished report (§A, §B) in the repository and confirm or change its domain.
6. **Coverage by priority.** Domains with no primary report, by register priority P0 to P3 (`no_primary_by_priority`).
7. **Cluster home robustness.** For each proposed home, record whether it is approved, open, and whether it waits on an owner decision.
8. **Similarity scan for unlisted duplicates.** TF-IDF cosine between all pairs of reports (with "Sources:" lists stripped). Pairs at ≥ 0.5 that no cluster groups are candidate duplicates. Any confirmed overlap is proposed as a NEW-n cluster with a single home.
9. **Drift since Baseline.** Count the report primaries that differ from `map_c0.csv` and list them.

## Iterations (9)
Matcher variants `charter`, `title_purpose` and `title`, each at k = 1, 3 and 5. Stemming on. Every iteration reports a permutation baseline.

## Pre-registered checks
| ID | Hypothesis | Metric | Test | Iterations |
|---|---|---|---|---|
| X9-1 | Inventory complete | inventory_gap | = 0 | all |
| X9-2 | Integrity | problems | = 0 | all |
| X9-3 | No queue-named domain missing | queue_named_missing | = 0 | all |
| X9-4 | Every cluster proposal passes | clusters_failed | = 0 | all |
| X9-5 | Matcher beats chance at k = 3 | perm_p | ≤ 0.01 | 2, 5, 8 |
| X9-6 | At least 1 unclustered similar pair | similar_pairs_unclustered | ≥ 1 | all |
| X9-7 | At most 25 primaries changed since Baseline | primaries_changed_since_baseline | ≤ 25 | all |
| X9-8 | Reports with no domain ≤ 1 | reports_no_domain | ≤ 1 | all |
