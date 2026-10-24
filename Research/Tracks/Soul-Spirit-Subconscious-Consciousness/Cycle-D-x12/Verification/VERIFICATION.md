# Verification — Track Cycle D (x12)

Date: 2026-10-24 · Tooling: `Research/tools` gaia_tools 0.5.1 (`python -m gaia_tools.tracks ...`), data model 1.4.0.

| Check | Result | File |
|---|---|---|
| Schema/structure validation of all track cycles | 0 errors, 0 warnings | `schema_validation_track.json` |
| Claim-source check (offline: resolve, full-text access rule, simulation-result rule, snapshot phrases) | 0 claims with a Fail; {"K-resolve": {"Pass": 139}, "K-access": {"Pass": 50, "n/a": 89}, "K-sim": {"n/a": 82, "Pass": 57}, "K-phrase": {"Pass": 73, "n/a": 66}} | `claim_source_TD.json` |
| Re-run of every simulation from a fresh copy (results, checks, params and SPEC hashes) | ALL IDENTICAL (48 runs) | `rerun_TD.json` |
| Live phrase re-fetch (single retry; unreachable = Indeterminate, never Pass) | {"Pass": 134} | `live_phrase_checks.json` |

## Gate
**INDETERMINATE.** Every internal check passed, but no independent (human) reviewer has checked the claims, codings or simulation designs, the same open condition as the main cycles (`Research/Cycles/Cycle-4-x12/INDEPENDENT_REVIEW_CHECKLIST.md`). Indeterminate is never Pass.

## Disclosed issues
- Smoke tests of all 20 new simulation kinds were run on seed 99 with reduced repetitions (build14/smoke.py) before the official runs. The hypothesis thresholds were written in the smoke harness at the same time and copied unchanged into specs_D.py, so several official outcomes were foreseeable from the smoke results. No threshold was changed after the smoke tests.
- SIM-CONS-D iteration 5, V1 Fail (0.054 vs <= 0.05): the 'validation' check was in fact a design-property expectation (misleading-evidence rate under a BF >= 3 bound), mislabelled as validation. Recorded as Fail and not re-run; TD-CONS-28 is labelled Plausible.
- K49: the first fetch (Europe PMC full-text XML) returned HTTP 500 and is logged; the PMC HTML of the author manuscript was then read (build13/fetch_pmc_html.py).
- K61 is the PsyArXiv preprint (file AfterlifeBeliefsReligionV2.pdf) fetched from OSF and converted with pdftotext; the published version was not read.
- Four Europe PMC title/author queries (K49, K61, K55 and AWARE-II searches) were first run without logging at about 06:56Z; they were re-run through a logging wrapper so that SEARCH_LOG holds them (marked with a note).
- Reporting inconsistencies found and recorded, not attributed as errors: K49's d' (3.464) vs 2.75 from its Table 2; K55's 'B mattering = 0.20' printed with t = -5.62 (sign).
- Illustrative parameters (not from the sources): SIM-SOUL-D iterations 2, 5, 6, 8, 10, 11, 12; SIM-SPIRIT-D 2, 5, 7, 9, 10, 11, 12; SIM-SUBC-D 2, 3, 5-9, 11, 12 (and the JZS prior in 1, 4, 10); SIM-CONS-D 1, 2, 3, 5-8, 12. The claims say so.
- Robustness/sensitivity re-runs that ask no new source-based question: SOUL 7-12; SPIRIT 8-12; SUBC 4-12; CONS 5-10, 12 (27 of 48 runs). SUBC had only three new sources, so 9 of its 12 runs are robustness runs.
- Carried from earlier track cycles: SIM-CONS-B iter-4 V1 Fail; SIM-SUBC-A iter-2 design flaw fixed in SIM-SUBC-B iter-1; Track A b001/b002 issued in one parallel call (both landed, hashes verified).
