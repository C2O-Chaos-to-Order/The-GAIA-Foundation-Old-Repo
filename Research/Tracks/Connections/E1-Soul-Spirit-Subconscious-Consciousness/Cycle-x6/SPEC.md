# Connection x6: specification

Written and pushed **before** the x6 run, together with `config.json`, the x6 additions to `../tools/conn.py` (behind the config key `x6`, so the Baseline and x3 records still reproduce byte-identically; checked before this push) and `../judgments/*_x6.csv`.

## Reading added in x6 (in full)
- Main Reports 3 (Soul), 4 (Spirit) and 5 (Consciousness), Cycle-4-x12: `REPORT.md` and `claims/claims.csv` (all columns).
- The main link register `Report-7-Unified/maps/link_register.csv` (all 28 rows).
- The SSSC source register `Cycle-D-x12/Provenance/SOURCE_REGISTER.csv` (71 rows). One entry is abstract-only (K37, a CMAJ note on near-death experiences); none of this report's claims rests on it alone.
- The main source register (`Cycles/Cycle-4-x12/Provenance/SOURCE_REGISTER.csv`) is used as a lookup for source IDs, not listed as read in full. Its 9 IDs shared with the SSSC register carry identical citations (checked by C6-10).
- Hashes are in `inputs.read_in_full`. No new external source.

## Pass 1 (agent judgment)
- `phase_audit_x6.csv`: one verdict per topic-term match from the x3 phase census (25 rows): `genuine`, `related_sense` (for example Schwartz self-transcendence *values*, not experience), `false_positive` ('semi-implicit Euler', 'cost-aware') or `instrument_name` ('Mystical Consciousness Typology').
- `factors_x6.csv`: F01–F11 unchanged; two new tradition factors with main-report bases: F12 breath and life vocabulary (Soul, Spirit) and F13 the self as consciousness or as no self (Soul, Consciousness).
- `claims_x6.csv`: 34 claims (23 carried unchanged, 11 new), with a new `tradition` column (yes for claims that describe or interpret traditions):
  - CN6-01 [E, descriptive] breath vocabulary (main link L10).
  - CN6-02 [PS] no single soul/spirit boundary (L11; C4-R3-01 typology instability).
  - CN6-03 [E, descriptive] Jain and Advaita identify the self with consciousness; Buddhist anatman denies an abiding self.
  - CN6-04 [PS] soul, brain process or neither (L12, L27).
  - CN6-05 [H] shared neural signatures of altered states (L18), with Report 5's non-stationarity caution (C4-R5-05).
  - CN6-06 [P] constructs bleed into measures (spirituality scales; report-based markers).
  - CN6-07 [E] deep sleep: PCI falls in NREM sleep; Advaita reads deep sleep as nearer pure consciousness (descriptive).
  - CN6-08 [P] higher-order theories define the unconscious/conscious difference relationally.
  - CN6-09 [PS] Christian, African and Indigenous readings of soul and spirit (Reports 3 and 4).
  - CN6-10 [P] access versus phenomenal: Subconscious findings bear on access (L08).
  - CN6-11 [E census] eight main-report links join two of Reports 2–5.
- `links_x6.csv`: 28 links (20 carried, 8 new: CL-21 to CL-28), each carried from a main-report link or a pair of main-report claims.

## Pass 2 (tool), x6 additions
- Basis IDs may name main-report claims and links (Cycle-4-x12); their sources resolve through the main register, and a main link's sources are those of its basis claims.
- Factor bases may come from the topic's own main report (R3 Soul, R4 Spirit, R5 Consciousness, R2 Mind for the Subconscious); another report's claim is a problem.
- Source-ID conflict check between registers.
- Phase audit: every match must have a verdict, and genuine matches are counted per topic.
- Tradition rule: a tradition claim may be Established only as a marked description, and never Plausible or Hypothetical (a tradition's teaching is described, not shown or made likely).
- Balance: per topic, tradition and science claims among shared, difference and unity claims.
- Tradition families named (ten pre-registered regexes over tradition-claim wording).
- Main-report links among Reports 2–5 (self-links excluded): which are used here, which topic pairs have none.
- **Six iterations:** 1 `as_judged`; 2 `strict`; 3 `established_only`; 4 `no_method` (method factors removed); 5 `no_tradition` (tradition factors removed); 6 `as_judged` with duplicate source registrations merged.

## Pre-registered checks
| ID | Hypothesis | Metric | Test |
|---|---|---|---|
| C6-1 to C6-9 | As C3-1 to C3-9 (inputs, resolution, sources, label rule, owner rule, census, rows, anchors) | | = 0 |
| C6-10 | No source-ID conflict between registers | source_id_conflicts | = 0 |
| C6-11 | Tradition rule | tradition_rule_violations | = 0 |
| C6-12 | Every phase match audited | phase_audit_missing | = 0 |
| C6-13 | Every topic has a genuine phase match | topics_without_genuine_phase_match | = 0 |
| C6-14 | Every topic has tradition and science claims | topics_lacking_tradition_or_science | = 0 |
| C6-15 | Every tradition family named | tradition_families_absent | = 0 |
| C6-16 | Every pair joined by a main-report link | main_pairs_without_link | = 0 |
| C6-17 | Every main-report link among Reports 2–5 carried | main_links_among_topics_not_used | = 0 |
| C6-18 | ≥ 1 factor in all four topics | unity_factors | ≥ 1 |
| C6-19 | ≥ 1 substantive or tradition factor in all four topics | unity_factors_substantive | ≥ 1 |
| C6-20 | Every pair has a Connection link | pairs_without_connection_link | = 0 |
| C6-21 | No 80-character overlap with the Totality Suite | boundary_overlaps | = 0 |

The x3 checks on unchanged existing records (C3-10 to C3-13) are not repeated: their inputs did not change.

**Disclosure of prior knowledge.** Almost every x6 outcome is foreseeable, which is itself a diminishing-returns signal.
- **Integrity dry run.** C6-1 to C6-12 were dry-run. It found one bug: the report-to-topic map was inverted, so the main-link count was 0. That was fixed, and self-links (L16, L28) are now excluded. The census value of CN6-11 (8) was read from that dry run.
- **C6-13.** FAIL is foreseeable: the audit file gives Consciousness no genuine match. Its three matches are an instrument name and a numerical 'cost-aware' rule.
- **C6-14.** PASS is foreseeable from the claims file.
- **C6-15.** Not independent. The family list was written after a search of the main and track ledgers showed Christian, African and Indigenous material. CN6-09 was added because that material existed and the Connection had not cited it. The check records coverage; it does not test it.
- **C6-16 and C6-17.** FAIL is known from listing the main register. No main link joins Report 2 and Report 4 (Spirit–Subconscious). L07 (predictive processing) and L09 (personal identity) concern Mind, not specifically the Subconscious, so they are not carried.
- **C6-18 and C6-19.** Foreseeable from the factor file. C6-18 is expected to PASS in all six iterations. C6-19 is expected to PASS in 1, 4 and 6 (F07) and FAIL in 2, 3 and 5. F12 and F13 span two topics, so they cannot change unity.

No threshold was set after seeing a result.

## Maps & Matrix
v41 (`v41-cycles-0-4-mr-track-abcd-phases-x12-conn0ab`), built from the unchanged `phases maps` base plus the x6 overlay (iteration 3 record for `validation/`). v1–v40 are not modified.

## Gate
- PASS needs C6-1 to C6-12, C6-18, C6-20 and C6-21 in every iteration. It also needs identical reruns of the Baseline, x3 and x6 (worktree and fresh clone), the Maps rebuild, manifests, the validator and tests.
- C6-13 to C6-17 and C6-19 are reported as they fall.
- Content stays Proposed, gate INDETERMINATE.

## Amendment before the run (pushed separately, still before any x6 run)
The change census compared whole rows, so the new `tradition` column would have marked all 23 carried claims as changed. It now ignores `tradition`, like `anchor` and `change_vs_prev`. This affects no check, and the Baseline and x3 records still reproduce identically. Only C6-1 to C6-12 have been dry-run.
