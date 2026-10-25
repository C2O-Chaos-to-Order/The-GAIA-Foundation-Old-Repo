# Connection x3: specification

Written and pushed **before** the x3 run, together with `config.json`, the x3 additions to `../tools/conn.py` (behind the config key `x3`, so the Baseline record still reproduces byte-identically) and `../judgments/*_x3.csv`.

## Reading added in x3 (in full)
- The four SSSC Cycle-D-x12 claim ledgers, all columns (wording, sources, locators, limits, deepens, cross-links, verification phrases): 139 rows.
- Convergence Cycle-D-x12 Philosophy-Spirituality and Applied-Sciences reports; Transcendence Cycle-D-x12 Philosophy-Spirituality and Applied-Sciences reports.
  - Convergence Applied-Sciences (numerical quadrature) was read and adds **nothing** to the Connection. This is recorded as a null reading.
- Hashes are in `inputs.read_in_full`. No new external source.

## Pass 1 (agent judgment)
- `claims_x3.csv`: 23 claims.
  - 18 carried. CN0-12 is revised in its limits only, to point to CN3-03.
  - 5 new:
    - CN3-01 and CN3-02: census claims, promoted from the Baseline tables.
    - CN3-03: shared methods are shared error sources (Convergence toy, H).
    - CN3-04: common-core instruments can manufacture sameness (Convergence and Transcendence, H).
    - CN3-05: loss of self as a junction of Spirit, Consciousness and the Soul topic's self (P).
  - New column `anchor`: a phrase that must appear verbatim in a named basis item. It guards against misreading a basis claim.
- `links_x3.csv`: 20 links.
  - 17 carried.
  - 3 new: CL-18 (Spirit–Consciousness, ego dissolution, P); CL-19 and CL-20, which make explicit two dependencies the track itself filed (TD-SPIRIT-31 → TC-SOUL-01; TD-CONS-29 → TC-SOUL-21).
- `factors_x3.csv`: unchanged from the Baseline.

## Pass 2 (tool), x3 additions
- Basis IDs may now name SSSC Cycles A–C claims (TA-/TB-/TC-).
- **Anchor check.**
- **Cross-mention census:** for each topic, the claims whose wording or limits use another topic's terms. Terms are pre-registered in `config.json` `x3.topic_terms`.
- **Phase × topic census:** phase claims (all six phases, Cycle-D-x12) whose wording uses each topic's terms.
- **Limitation census:** six pre-registered limitation families in the `counterevidence_limits` column, by topic.
- **Change census** against the Baseline judgments.
- **Three iterations:**
  1. `as_judged`
  2. `strict`: a factor row counts only with an Established or Plausible basis claim
  3. `established_only`

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C3-1 | Sources read in full exist | missing_inputs | = 0 |
| C3-2 | Every basis ID resolves | dangling_basis | = 0 |
| C3-3 | Every source ID is in an existing register | unresolved_sources | = 0 |
| C3-4 | Every listed source is cited by a basis item | sources_not_in_basis | = 0 |
| C3-5 | No label above its weakest ranked basis | label_rule_violations | = 0 |
| C3-6 | Owner rule | owner_rule_violations | = 0 |
| C3-7 | Census claims match computed values | census_claim_mismatches | = 0 |
| C3-8 | Rows well-formed | problems | = 0 |
| C3-9 | Anchors found verbatim | anchor_mismatches | = 0 |
| C3-10 | Every pair has a cross-mention in the existing ledgers | pairs_without_cross_mention | = 0 |
| C3-11 | Every topic's terms match a phase claim | topics_without_phase_match | = 0 |
| C3-12 | Transcendence has the most topic-matching phase claims | transcendence_most_matches | = 1 |
| C3-13 | ≥ 3 limitation families occur in all four topics | limitation_families_in_all_four | ≥ 3 |
| C3-14 | ≥ 1 factor in all four topics under the iteration's rule | unity_factors | ≥ 1 |
| C3-15 | ≥ 1 substantive or tradition factor in all four topics under the iteration's rule | unity_factors_substantive | ≥ 1 |
| C3-16 | Every pair has a Connection link | pairs_without_connection_link | = 0 |
| C3-17 | No 80-character overlap with the Totality Suite | boundary_overlaps | = 0 |

**Disclosure of prior knowledge.**
- **Integrity dry run.** The tool was dry-run on the x3 inputs to check integrity metrics only (C3-2 to C3-9). That run found one ordering bug: census claims were compared before the x3 metrics existed. It was fixed. The open checks C3-10 to C3-15 were not printed.
- **C3-12.** During Baseline exploration, before this cycle, a single combined keyword search of the phase ledgers (not these per-topic terms) matched 16 Transcendence claims of 21 in all. C3-12 is therefore close to known and is confirmatory only.
- **C3-15.** Under `strict` and `established_only`, this check is foreseeable from the judgment file. The only substantive or tradition factor in all four topics under `as_judged` is F07, and its Soul row rests on Philosophical/Spiritual claims only. C3-15 is expected to PASS in iteration 1 and FAIL in iterations 2 and 3. It is kept because the contrast is the point: the tradition-level unity disappears once only E/P evidence counts.
No threshold was set after seeing a result.

## Maps & Matrix
v40 (`v40-cycles-0-4-mr-track-abcd-phases-x12-conn0a`), built from the unchanged `phases maps` base plus the x3 overlay (iteration 3 record for `validation/`). v1–v39 are not modified.

## Gate
- PASS needs C3-1 to C3-9, C3-14, C3-16 and C3-17 in every iteration, plus identical reruns of the Baseline and x3 (worktree and fresh clone), the Maps rebuild, manifests, the validator and tests.
- C3-10 to C3-13 and C3-15 are reported as they fall.
- Content stays Proposed, gate INDETERMINATE.
