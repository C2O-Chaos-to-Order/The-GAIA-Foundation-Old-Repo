# Verification — Cycle 2 (x6)

Date: 2026-10-24. **Gate: INDETERMINATE** — every internal check passes or is reported; no independent review; R3 inter-rater reliability still lacks an independent coder; 2 passages and 1 URL Indeterminate (HTTP 429/403); ethics review not performed.

## 1. Reproducibility
All 42 iterations re-executed from a fresh copy by `gaia_tools.rerun` (Cycles 0–1 present for Report 7): **42/42** byte-identical `results.json`, identical check results and params. Raw: `verification_raw.json` → reproducibility.

## 2. Claim–source phrase checks (live re-fetch)
166 verification passages across all claims: **164 Pass**, 2 Indeterminate, 0 Fail. Established literature claims fully verified: **68/70**.
- Indeterminate: C0v2-R4-12 / S14 (HTTP 429; single retry also 429); passage present in the stored snapshot. Not counted as Pass.
- Indeterminate: C0v2-R6-12 / S26 (HTTP 403); passage present in the stored snapshot. Not counted as Pass.
- First run: C2-R2-01 / W06 failed because its phrase contained unescaped regex parentheses; the phrase was escaped in `claims.csv` and re-checked live: Pass (recorded in the raw file).
- Offline (`gaia_tools.claimsource` with local snapshots): K-phrase 118/118 Pass for Cycle 2 (and 0 Fail for Cycles 0–1).
Raw: `claim_source_checks.json`.

## 3. Links
130 register entries: 76 public URLs HTTP 200; 50 blocked URLs (mostly PubMed bot walls) resolved through the Europe PMC REST API with title match; 1 Indeterminate (S26, HTTP 403); G01/G02 checked via the GitHub connector; G03 is a repository path.
- G01 `Research/README.md` blob 141824b and G02 `Research/RESEARCH_PLAN_EXTENSION.md` blob d895748 on `main` @ 1f1681c — unchanged; G03 `Research/Cycles/Cycle-0-Baseline/FRAMEWORK.md` blob b4ec6c3 (GitHub connector, 2026-10-24).

## 4. Consistency (SIM-R7-C2 and gaia_tools)
- SIM-R7-C2 iteration 4 (register audit RC1–RC3) and 6 (whole-ledger audit AU1–AU4): all Pass. Iteration 5: T0 Pass; T1 0/142 carried claims changed label or status.
- `gaia_tools.validate` (data model 1.1.0): 0 errors over Cycles 0–2; Cycle-2 warnings: one Q3 (L24 placeholder rejection criterion, PS link).
- `gaia_tools.claimsource` C2: K-resolve 177/177, K-access 0 Fail, K-sim 0 Fail.

## 5. Gate
| Criterion | Result |
|---|---|
| Scope coverage (7 reports, 6 passes, 6 iterations each) | Pass |
| Labels applied and mapped | Pass |
| Sourcing (full-text rule) | Pass (K-access) |
| Metaphor kept separate from science | Pass (internal review) |
| Reproducibility | Pass (42/42) |
| Claim wording fully supported | Indeterminate (2 passages blocked; independent check pending) |
| R3 inter-rater reliability | **Indeterminate** (same-agent re-coding only) |
| Independent review | **Indeterminate** (not performed) |
| Ethics review | **Indeterminate** (not performed) |

Overall: **INDETERMINATE**. Indeterminate is never Pass.
