# Cycle 0 — Baseline v2 (framework-aligned) — Verification

**Date:** 2026-10-24 · **Performed by:** Grok Bot, the same agent that produced the reports.
**This is an internal check, NOT independent human or specialist review.** Checks repeated by the producer are not independent (Research/README.md §4).

## Scope
All 7 reports in `Cycles/Cycle-0-Baseline/` (Baseline v2): 100 claims (Established 65, Plausible 14, Philosophical/Spiritual 19, Hypothetical 2), 78 register entries (75 external sources plus 3 governing documents G01–G03), 7 executed simulations and the 24-link GAIA-motherthread register.

## Methods
1. **Reproducibility.** Every simulation was re-executed from a fresh copy of the staged tree. Output SHA-256 values were compared with the execution record (`verification_raw.json` → `reproducibility`).
2. **Claim–source re-verification (live).** Every claim carrying a verification phrase was checked: all 55 Established claims that rest on literature, plus 26 others. Each source was re-fetched live from its retrieval URL (PDFs via `pdftotext`; PubMed abstracts via NCBI E-utilities) and searched for the supporting passage. A stored-snapshot check was run alongside (`claim_source_spotchecks.json`). The 10 Established claims that rest only on simulation checks are verified by method 1 and by SIM-R7-C0 E7.
3. **Link check.** HTTP status of every public source URL (`verification_raw.json` → `links`).
4. **Ledger and link-register consistency.** SIM-R7-C0 checks E5–E10 (`Report-7-Unified/simulation/outputs/consistency.json`).
5. **QC checklist.** RESEARCH_PLAN_EXTENSION §9, item by item, plus framework rules.

## Results

### 1. Reproducibility — Pass
| Simulation | Rerun exit | Outputs byte-identical | Checks (original → rerun) |
|---|---|---|---|
| SIM-R1-C0 | 0 | Yes | 7/7 → 7/7 pass |
| SIM-R2-C0 | 0 | Yes | 4/4 → 4/4 pass |
| SIM-R3-C0 | 0 | Yes | 3/3 → 3/3 pass |
| SIM-R4-C0 | 0 | Yes | 5/5 → 5/5 pass (corrected model; v1 E2 Fail archived) |
| SIM-R5-C0 | 0 | Yes | 3/3 → 3/3 pass |
| SIM-R6-C0 | 0 | Yes | 4/4 → 4/4 pass |
| SIM-R7-C0 | 0 | Yes | 10/10 → 10/10 pass |

The R2, R5 and R6 numerical outputs are identical to v1 (unchanged models and seeds; R6 CSVs differ only in line endings, CRLF → LF). Reproducibility is not validity.

### 2. Claim–source re-verification — 92/92 passages found live (81 claims, 69 sources)
- **Established literature claims:** 55/55 re-verified live → **Pass**.
- Plausible 14/14, Philosophical/Spiritual 11/11 and Hypothetical 1/1 phrase checks also passed.
- Access caveats: PMC sometimes served a reCAPTCHA page during runs, so the verifier falls back to Europe PMC or NCBI E-utilities and records the route used; in the final run every check succeeded via its primary route. Harvard DASH (S14) returned HTTP 429 on the first attempt and 200 on retry. That is logged.
- **What this checks:** that the cited passage exists in the source. Whether the passage fully supports the claim's wording was judged by the producer when writing it and is not independently checked → see QC 11.

### 3. Link check — 59/78 HTTP 200
- 16 PubMed landing pages (S13, S20, S23, S28, T01, T08, T10–T13, U10, U11, U20, U21, U30, U31) returned HTTP 203 with a cookie/bot wall. Their content was retrieved through NCBI E-utilities, and every claim check on them passed. The landing pages are **Indeterminate**, not broken.
- G01 and G02 (private-repository blob URLs) return 404 when unauthenticated; they were read through the authenticated connector → **Indeterminate**.
- G03 (`FRAMEWORK.md`) is an in-repository path → n/a.

### 4. Consistency (SIM-R7-C0) — Pass
E5: required fields, vocabularies and label↔status mapping all valid. E6: all 100 claims' sources and `SIM#check` citations resolve. E7: no Established claim cites a failed or unspecified simulation check (this refined rule replaces v1's E7, which failed and needed manual review). E9: all 24 links are complete, all 7 link types occur, and R1–R6 are all linked. E10: no Established claim rests only on the framework or motherthread document.
**Warning (E8, not a failure):** 11 Established claims rest only on abstract or excerpt access: C0v2-R1-09, R2-04, R2-12, R4-10, R5-02, R5-06, R6-01, R6-02, R6-04, R6-05, R6-13. Each states only what the abstract states; each is flagged for full-text checking in Cycle 1.

## QC checklist (Plan §9 + framework rules)
| # | Item | Result | Evidence |
|---|---|---|---|
| 1 | Exactly seven reports | **Pass** | Report-1 … Report-7, each with REPORT.md |
| 2 | Each report covers the framework's full scope | **Pass** (self-assessed) | "Framework scope coverage" table in every REPORT.md; every listed scope item has ≥1 claim |
| 3 | Every conclusion carries a framework label | **Pass** | `framework_label` on 100/100 claims and 24/24 links (E5, E9) |
| 4 | Factual claims sourced and traceable | **Pass** | E6; locators on every row |
| 4b | Claim–source support re-verified | **Pass** for passage presence (55/55 Established literature claims, 92/92 checks) · **Indeterminate** for full support of wording (not independent) | §2 |
| 5 | Metaphor kept separate from mechanism | **Pass** | R6 Part A/B science vs metaphor sections; GAIA motherthread labelled Philosophical/Spiritual; E10 |
| 6 | Research and speculation separated | **Pass** | Framework label + repository class/status |
| 7 | Consistent category names / indexing | **Pass** | SIM-R7-C0 E1 |
| 8 | 625 intersections unique and correctly enumerated | **Pass** | E1 |
| 9 | Arithmetic checked independently of semantics | **Pass** | E3, E4 |
| 10 | Simulation results come from documented execution | **Pass** | 7 EXECUTION_RECORDs; reruns identical |
| 11 | No conclusion asserted beyond evidence | **Indeterminate** | Self-assessed only; needs independent review |
| 12 | Failed tests, contrary evidence, unresolved questions preserved | **Pass** | v1 R4 E2 failure archived in `Report-4-Spirit/simulation/archive_v1/` and in change histories; R1 E1 deviation note; R2 withdrawn rationale; counterevidence column; L24 and Open-questions sections |
| 13 | Ethics: dignity, rights, non-harm, fairness, accountability | **Indeterminate** | Ethics section per report; no dedicated ethical review |
| 14 | Singularity and Origin remain open | **Pass** | C0v2-R7-07, L24 |
| 15 | Manifest and digests agree with delivered files | **Pass** | `sha256sum -c Provenance/MANIFEST.sha256` (cycle README); ZIP not produced |
| — | Independent review | **Not performed → Indeterminate** | — |

## Coverage now closed (vs v1 gaps)
R1: nervous system, sensory perception, environment. R2: thought/reasoning, emotion, perception, identity, learning, mind–body. R3: Hebrew Bible/nefesh, Christian, Islamic, Hindu, Buddhist, Chinese, African, Indigenous, Greek; identity, moral character, purpose, independence. R4: vitality, transcendence, connection, inspiration, plus well-being evidence. R5: attention, self-awareness, perception, altered states, origin/nature. R6: biodiversity, interdependence, philosophy of the whole, heat transfer, planetary dynamics, heart symbol. R7: all seven link types, with tests and rejection criteria.

## Remaining gaps (carried to Cycle 1)
Full-text checks for the 11 abstract-only Established claims. Multi-coder coding for SIM-R3. Traditions not yet covered: prāṇa (Hindu spirit), Jain, Sikh, Daoist, further Indigenous self-descriptions. Language, social cognition and development (R2). Gaia proponents' replies to Kirchner (R6). Phase semantics of the 625 grid (R7).

## Gate decision
**Cycle 0 (Baseline v2) gate: INDETERMINATE.** All automated checks pass and passage-level re-verification of Established claims is complete. Passing still requires independent review, independent judgement that the wording is supported, and an ethics review, and none of these are met. Indeterminate is not Pass. The Global Research Completion Gate is unchanged, and implementation is not authorized.
