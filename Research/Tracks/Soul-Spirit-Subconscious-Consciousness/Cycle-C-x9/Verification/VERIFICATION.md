# Verification — Track Cycle C (x9)

Date: 2026-10-24 · Tooling: `Research/tools` gaia_tools 0.5.1 (`python -m gaia_tools.tracks ...`), data model 1.4.0.

| Check | Result | File |
|---|---|---|
| Schema/structure validation of all track cycles | 0 errors, 0 warnings | `schema_validation_track.json` |
| Claim-source check (offline: resolve, full-text access rule, simulation-result rule, snapshot phrases) | 0 claims with a Fail; {"K-resolve": {"Pass": 105}, "K-access": {"n/a": 68, "Pass": 37}, "K-sim": {"n/a": 64, "Pass": 41}, "K-phrase": {"Pass": 57, "n/a": 48}} | `claim_source_TC.json` |
| Re-run of every simulation from a fresh copy (results, checks, params and SPEC hashes) | ALL IDENTICAL (36 runs) | `rerun_TC.json` |
| Live phrase re-fetch (single retry; unreachable = Indeterminate, never Pass) | {"Pass": 96, "Indeterminate": 1} | `live_phrase_checks.json` |

## Gate
**INDETERMINATE.** Every internal check passed, but no independent (human) reviewer has checked the claims, codings or simulation designs, the same open condition as the main cycles (`Research/Cycles/Cycle-4-x12/INDEPENDENT_REVIEW_CHECKLIST.md`). Indeterminate is never Pass.

## Disclosed issues
- Before the official runs, every new simulation kind was smoke-tested on a different seed with reduced repetitions to check that the code ran and the validation checks worked. Hypothesis thresholds had been written into specs_C.py first and were not changed afterwards. Two changes were made after smoke tests, both before any official run: (1) the rare-association validation V1 was given a Monte Carlo tolerance (0.05 + 3 SE) and its repetitions were raised (lesson from SIM-CONS-B iter-4); (2) exp() overflow in the conditioning toy was clipped.
- K44 (van Elk 2022) was fetched and turned out to be the same paper as K01. It is logged in FETCH_LOG and not cited.
- K37 is a complete short article (about 700 words). The source register's word-count rule labels it 'abstract only'. Its claims are labelled Plausible and Hypothetical, not Established.
- SIM-CONS-C iterations 4 and 7 found that K47's reported percentages and chi-square (5.93, p = .052) do not fit a simple 'never limit vs other' test at the stated group sizes. This is recorded as an unresolved reporting question, not as an error by the authors.
- Illustrative parameters (not taken from the sources): SIM-SUBC-C iterations 1, 2, 3, 6, 7, 9; SIM-SOUL-C iterations 1, 2, 4, 5, 6, 8, 9; SIM-SPIRIT-C iterations 1-9 (path values, reliabilities, curve); SIM-CONS-C iterations 1, 2, 4-8. The claims say so.
- Robustness/sensitivity re-runs that ask no new source-based question: SUBC 8, 9; SOUL 6, 7, 8, 9; SPIRIT 6, 7, 8, 9; CONS 6, 7, 8, 9 (14 of 36 runs).
- Carried from earlier track cycles: SIM-CONS-B iter-4 V1 Fail (recorded, not re-run; TB/TC-CONS-14 Plausible); SIM-SUBC-A iter-2 design flaw fixed in SIM-SUBC-B iter-1; Track A b001/b002 issued in one parallel call (both landed, hashes verified).
