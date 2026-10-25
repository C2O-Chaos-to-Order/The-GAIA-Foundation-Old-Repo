# PC-4 Research-to-Domain Map: Plan

Status: **Proposed (research output, not adopted).** Work Queue item PC-4 (Program Coordination) and gap check item b7.
Owner approval to start: Kyle, 2026-10-25 (relayed in the agent task). Author: Grok Bot, with the Kyle Steen trailer on every commit.

## 1. Question

Which of the 45 Totality domains (GAIA-TOT-001 to 045) does each Work Queue report belong to, so that nothing is researched twice?
Three outputs are required:

1. An **item → domain map** for every Work Queue report, every Totality of Governance report (ToG 1–10 and the ToG Synthesis) and every GAIA-Documentation item in §N (reports 1–8, N-A, N-B).
2. A **single-home proposal** for each of the 9 duplicate clusters in gap b7. These are proposals for the owner, not decisions.
3. **Coverage lists**: domains with no report, and reports with no domain.

## 2. Inputs and the adoption boundary

| Input | Where | How it is pinned |
|---|---|---|
| Work Queue | `Research/WORK_QUEUE.md` in this branch | SHA-256 recorded in every EXECUTION_RECORD |
| GAIA Totality Suite v0.1.0 | **Owner-provided, external.** Read at `/workspace/coord/zip/gaia_totality_suite_v0_1/` (override with `PC4_SUITE`) | `TOTALITY_REGISTER.csv` SHA-256 `057efb5489305f99280f9b350771058686e35fef753682449f2901b152fe8c72`; charters checked against the suite's `SHA256SUMS.txt` (pinned `2f18e3b36c89bc491d21c89438e4315474e13c22ae03476bafc3581839f6a5d7`) |

The suite is cited as **owner-provided v0.1.0, status Proposed, not adopted**. Its own boundary says it must not be copied to `main` and each file needs owner review before any repository action. This track therefore **files no suite file**. It stores only what it derives: stable IDs, titles and priorities (in the coverage tables) and the mappings. The register is read with `utf-8-sig` because it starts with a byte-order mark. Rerunning needs the owner's suite; the tool refuses to run if the hashes differ.

## 3. Inventory

`tools/pc4.py inventory` parses every checkbox in the Work Queue (outside the change log), gives it a stable ID (A-01, ToG-03, PC-4, N-1, M-b7.4 …) and a kind from its section:

| Kind | Sections | Mapped? | Counted as a report for coverage? |
|---|---|---|---|
| report | A, B, D–J, ToG 1–10 and Synthesis, PC-1–9, K, K "Added later", N 1–8, N-A, N-B | yes | **yes** |
| candidate | K "Recommended by Grok Bot", M(c) s1–s11 (awaiting owner approval) | yes | only in the "with candidates" sensitivity |
| governance | Governance (ToG draft, Roadmap Stages 0–8) | yes | no (process stages) |
| level | C (the seven level boxes) | yes | no (upgrade-ladder boxes) |
| tot-domain-report | Waves 0–5 | no: these are the domain reports themselves | no |
| update, setting, gap, cluster, recommendation, out-of-scope, afterwards | L, M, Afterwards | no (b7 clusters are handled in the cluster file) | no |

## 4. Mapping rules and labels

Each mapped item gets one **primary** domain (its single home), zero or more **secondary** domains, a label, and a basis.
`NONE` is allowed only with a reason (for example, the owner has not yet defined the subject).

The label applies to the mapping claim, "item X belongs to domain Y", not to the content of the report:

- **Established**: the Work Queue text itself names the primary domain (`named_in` gives the item whose text names it; the tool checks this mechanically).
- **Plausible**: agent judgment, supported by the domain's title, purpose or charter scope, and stated in the basis.
- **Hypothetical**: a weak or speculative fit, or a `NONE` that depends on an undefined subject.
- **Philosophical/Spiritual**: available but not expected for mapping claims; the *subjects* of many reports are Philosophical/Spiritual, which is why TOT-023 (Cultural, Philosophical, Spiritual and Theological Knowledge: "represent belief systems and interpretive traditions accurately without falsely converting them into empirical claims") is their natural domain.

Secondary assignments are agent judgment (Plausible) unless the item text names them.

## 5. Independent check: lexical matcher

A deterministic TF-IDF matcher (standard library, no model) ranks the 45 domains for each report from the domain text. It is a crude second rater: agreement means the judgment is lexically supported, disagreement means "look again", not "wrong". Variants: `title`, `title_purpose`, `charter` (title, purpose and charter sections 1–4 and 7). Metrics: top-1 and top-k hit rates for the judged primary, and top-k "any judged domain".

## 6. Cycles (standing pattern)

Baseline → x3 → x6 → x9 → x12. Each cycle folder holds `SPEC.md` (written and pushed before the run), `config.json` (the pre-registered checks), `PASSES.md`, `iter-N/EXECUTION_RECORD.json` and `iter-N/data/`, `REPORT.md`, `VERIFICATION.md` and `MANIFEST.sha256`. Each cycle is on its own branch `research/pc4-<cycle>`, stacked on the previous one, pushed in small chunks without force.

Gate results are PASS, FAIL or INDETERMINATE; INDETERMINATE is never PASS. A failed pre-registered check stays failed in the record and is reported; it is not re-thresholded after the fact.

Planned shape (each later SPEC fixes the details before its run):

| Cycle | Passes | Iterations |
|---|---|---|
| Baseline | 1: map every in-scope item; first b7 proposals | 1: `charter` matcher |
| x3 | 3: charter-scope review of every primary; Established-by-reference; review of matcher disagreements against the gap check | 3: `charter`, `title_purpose`, `title` |
| x6 | 6: coverage-gap search in non-report items; b7 membership update for §N; dependency check; ToG §6 24-domain alignment; sensitivity; label audit | 6: k and stemming grid |
| x9 | 9 (expected to add little) | 9: robustness, including a permutation (chance) baseline |
| x12 | 12 (expected to add little) | 12 |

Diminishing returns are reported per pass ("Added nothing" is recorded as such).
