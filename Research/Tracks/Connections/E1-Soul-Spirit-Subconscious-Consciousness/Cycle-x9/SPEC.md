# Connection x9: specification

Written and pushed **before** the x9 run. The push includes:
- `config.json`;
- the x9 additions to `../tools/conn.py`, behind the config key `x9`. The Baseline, x3 and x6 records still reproduce byte-identically; this was checked before the push;
- `../judgments/*_x9.csv`.

## Reading added in x9 (in full)
- Master Report (Report 7, Cycle-4-x12): `REPORT.md` and `claims/claims.csv`. The rules adopted from it:
  - its strict Established-link rule (C2-R7-01: an Established link needs every basis claim Established);
  - its GAIA separability test (C3-R7-02, C4-R7-01: no Established link rests on a Philosophical/Spiritual or Hypothetical claim).
- The Phases `SYNTHESIS.md` was read in full in x3 and is listed there.
- No new external source.

## Pass 1 (agent judgment): adversarial review
`review_x9.csv` gives every x6 claim (34) and link (28) a verdict, with the challenge and the response. Two factor rows are also challenged.

| Verdict | Items |
|---|---|
| keep | 52 |
| revise (label kept) | CN0-04 (simulations "can" misclassify), CN0-07 (Advaita part marked descriptive), CN0-11 (limits cited Yogacara for a no-self view; x6 cites Indian Buddhist anatman), CN3-05 (Soul topic removed; the Soul reading would be PS), CN6-03 (kind unity → difference: one tradition denies what others teach), CN6-07 (the agent's gloss "nearer to pure consciousness" replaced by the source's "partial experience of its bliss"), CL-07 (type interaction → shared factor) |
| downgrade | CN0-18 P → H (an ethics factor this broad fits almost any four topics), CL-14 E → PS (the dependence holds only within the teachings), CL-15 P → H (one feasibility study, 9 usable EEGs) |
| drop (factor rows, `reviewed` rule only) | F03/CONS (theory predictions, not failed replication), F09/SPIRIT (six focus groups and a PS claim) |
| withdraw | none |

- New claim CN9-01 [PS, framing]: Report 7 lists the nature of consciousness and the existence of a soul as unresolved (C0v2-R7-07). Nothing here resolves them.
- Totals: 35 claims, 28 links.
- `factors_x9.csv` is unchanged from x6. The phase audit is reused from x6.

## Pass 2 (tool), x9 additions
- **Review coverage and consistency.** Every previous item needs a verdict, and the verdict must match the change. A kept row must be unchanged except `change_vs_prev`. A revised row must change and keep its label. A downgraded row must have a lower label (E/P → PS counts as lower). A withdrawn row must be absent. New rows must be marked new.
- **Report 7's strict rule.** Lists Established items with any basis below Established.
- **Separability.** Lists Established items on a PS or H basis, or citing the framing source G03.
- **Tradition sources.** Lists tradition claims, framing aside, whose only sources are G03 or none.
- **Main links carried.** C6-17 without census claims: main links among Reports 2–5 used by no non-census claim or link.
- **Four iterations:**
  1. `as_judged`
  2. `strict`
  3. `established_only`
  4. `reviewed` (as judged, minus the dropped factor rows)

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C9-1 to C9-11 | As C6-1 to C6-11 | | = 0 |
| C9-12 | Every previous item reviewed | review_missing | = 0 |
| C9-13 | Verdicts match changes | review_inconsistencies | = 0 |
| C9-14 | Tradition claims cite a non-framing source | tradition_claims_without_source | = 0 |
| C9-15 | Report 7's strict rule | strict_e_violations | = 0 |
| C9-16 | GAIA separability | gaia_separability_violations | = 0 |
| C9-17 | Every main link among Reports 2–5 carried by a non-census item | main_links_not_used_substantive | = 0 |
| C9-18 | ≥ 1 factor in all four topics | unity_factors | ≥ 1 |
| C9-19 | ≥ 1 substantive or tradition factor in all four topics | unity_factors_substantive | ≥ 1 |
| C9-20 | Every pair has a Connection link | pairs_without_connection_link | = 0 |
| C9-21 | No 80-character overlap with the Totality Suite | boundary_overlaps | = 0 |

**Disclosure of prior knowledge.**
- **Integrity dry run.** C9-1 to C9-13 were dry-run, and all were 0.
- **C9-14 to C9-16.** The review began from a listing of every item's basis labels, so these outcomes are foreseeable. Every Established item seen there had only Established bases, so PASS is expected. They are kept as standing guards that later cycles must keep passing.
- **C9-17.** FAIL is foreseen. L07 and L09 are not carried (x6 §6).
- **C9-18 and C9-19.** Foreseeable from the factor and review files:
  - Under `reviewed`, the factors in all four topics are expected to be F01, F02, F04 and F07. F03 loses Consciousness and F09 loses Spirit.
  - C9-19 is expected to PASS in iterations 1 and 4 and FAIL in 2 and 3.

No threshold was set after seeing a result.

## Maps & Matrix
v42 (`v42-cycles-0-4-mr-track-abcd-phases-x12-conn0abc`), built from the unchanged `phases maps` base plus the x9 overlay (iteration 4 record for `validation/`). v1–v41 are not modified.

## Gate
- PASS needs C9-1 to C9-16, C9-18, C9-20 and C9-21 in every iteration. It also needs identical reruns of all four cycles (worktree and fresh clone), the Maps rebuild, manifests, the validator and tests.
- C9-17 and C9-19 are reported as they fall.
- Content stays Proposed, gate INDETERMINATE.
