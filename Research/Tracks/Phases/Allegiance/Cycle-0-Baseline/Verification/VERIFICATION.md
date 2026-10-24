# Verification — Allegiance Cycle-0-Baseline (AL0)

Checked 2026-10-24T18:54:52+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. AL0 --snapshots` | 12 claims, 0 with a Fail; {"K-resolve": {"Pass": 12}, "K-access": {"Pass": 3, "n/a": 9}, "K-sim": {"n/a": 6, "Pass": 6}, "K-phrase": {"Pass": 6, "n/a": 6}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. AL0` | 6 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 16} |
| Simulation validation checks | EXECUTION_RECORD.json | 7/7 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 11/12 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Allegiance Cycle-0-Baseline — 12 claims, 6 sources in the register, 6 simulation runs, 3 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Six new sources (P46-P51) read in full; no source reused from Divergence or Insurgence (P30 cited only as a comparator form in HUM, read in full in INA). No empty passes (6/6 added claims and a new source).
- The 'Allegiance' operationalizations per field (cooperative binding, cooperation rules, identity fusion, researcher allegiance, language loyalty, loyalty as virtue) are this track's choices; no repository document defines Allegiance (Research/README.md only lists the phase) and only P49 and P51 use the word.
- New sim kinds (hill_binding, coop_rules, fusion_loop, meta_power, language_markov, exit_voice) were smoke-tested once (seed 99, reduced size) before SPECs were written. Foreknowledge: FOR H2 was expected to be not supported (crossing 4.23 vs 4); HUM V1 failed in the smoke at T = 500 (slow Scotland rates) and T was raised to 3000, a numerical setting; a first NAT smoke with steeper Adair constants gave slope 3.88 and milder constants were used. No threshold was changed.
- SOC-02 and PHI-02 are Hypothetical toys formalizing verbal arguments (P48's labelling loop; Hirschman as reported in P51); parameters are arbitrary.
- P47 is an NIH author manuscript (publisher copyright): NCBI efetch returned only the abstract, so the PMC HTML page was fetched and read; P51 (SEP) was fetched directly after the Europe PMC search found nothing relevant; both are quoted in short phrases only.
- Source slips recorded: P46 'log 1 = log 100 = 0' and typos; P47 'There are a repeated encounters'; P50 cites figure 1a for results shown in figure 2 and writes 'minority Catalonia'; P48 calls fusion irrevocable yet reports cases where fusion decreased.
- Owner context (does not change methods): the owner maps phases to upgrade levels (Base = Divergence, Meta = Insurgence, Super = Allegiance, Hyper = Convergence, Ultra = Ascendence, Magic = Transcendence, a new sixth phase); 'Allegiance corresponds to Super/Superphysical' is recorded in the phase README as the owner's Hypothetical claim.
- Pushed to research/phase-allegiance-c0 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. Gate INDETERMINATE (independent review pending).
