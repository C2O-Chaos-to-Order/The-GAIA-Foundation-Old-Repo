# Verification — Track Cycle A (x3)

Date: 2026-10-24 · Tooling: `Research/tools` gaia_tools 0.5.0 (`python -m gaia_tools.tracks ...`), data model 1.4.0.

| Check | Result | File |
|---|---|---|
| Schema/structure validation of all track cycles | 0 errors, 0 warnings | `schema_validation_track.json` |
| Claim-source check (offline: resolve, full-text access rule, simulation-result rule, snapshot phrases) | 0 claims with a Fail; {"K-resolve": {"Pass": 37}, "K-access": {"n/a": 23, "Pass": 14}, "K-sim": {"n/a": 26, "Pass": 11}, "K-phrase": {"Pass": 23, "n/a": 14}} | `claim_source_TA.json` |
| Re-run of every simulation from a fresh copy (results, checks, params and SPEC hashes) | ALL IDENTICAL (12 runs) | `rerun_TA.json` |
| Live phrase re-fetch (single retry; unreachable = Indeterminate, never Pass) | {"Pass": 32} | `live_phrase_checks.json` |

## Gate
**INDETERMINATE.** Every internal check passed, but no independent (human) reviewer has checked the claims, codings or simulation designs, the same open condition as the main cycles (`Research/Cycles/Cycle-4-x12/INDEPENDENT_REVIEW_CHECKLIST.md`). Indeterminate is never Pass.

## Disclosed issues
- SIM-SUBC-A iteration 2 had a design flaw: latent knowledge was unbounded below, so 'below-chance' selection picked below-average knowledge. Its H1 'not supported' is a design artefact and is labelled as such in TA-SUBC-04; it is redone in Track Cycle B.
- SIM-SOUL-A iteration 1 and SIM-SPIRIT-A iterations 1-2 use illustrative parameters (K01 gives no numbers; original awe-study Ns and the published MEQ30 criterion were not read). The claims say so.
- SIM-CONS-A iteration 3 compares principal-component variance with K14's factor-analytic 44%; the two are not identical quantities.
