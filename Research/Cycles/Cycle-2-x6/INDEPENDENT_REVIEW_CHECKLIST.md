# Independent review checklist (Cycle 2)

For a reviewer who did not produce this work. Record disagreements in a review file rather than editing the ledgers.

## Sources and claims
- [ ] Pick at least 10 Established claims at random; confirm the wording is supported by the cited source in context, not only by the verification phrase.
- [ ] Check that W02/W03 (abstract only) support only what C2-R6-01/02 say, and that C2-R6-01 rests on W01's full text.
- [ ] Check the Q1 fills (limits fields of 37 carried claims) for accuracy.
- [ ] Review `Provenance/SEARCH_LOG.jsonl`: are important studies missing (e.g. failures to replicate latent inhibition; Gaia critiques after 2001)?

## R3 inter-rater reliability
- [ ] Complete `Report-3-Soul/research/pass-5/blank_form_for_independent_coder.csv` using `CODEBOOK.md`, without looking at either coding; compute kappa against both.

## Labels and links
- [ ] Philosophical/Spiritual claims are phrased as interpretation; GAIA framing never substitutes for evidence.
- [ ] Decide whether the strict reading of the link rule (L04, L08, L16 downgraded) is right, or define 'essential' basis claims.

## Simulations
- [ ] Re-run all 42 iterations (`python -m gaia_tools.rerun .. C2`).
- [ ] Read each SPEC.md: were the pre-registered thresholds sensible? Note the disclosed R5 pilot and R7 re-runs.
- [ ] Confirm every 'not supported' outcome is reported as a finding (17 in Cycle 2).

## Process
- [ ] Ethics: no human-subject data used; check Report 4's health framing.

Until this checklist is completed by someone independent, the gate stays **Indeterminate**.
