# Verification — Insurgence Cycle-0-Baseline (IN0)

Checked 2026-10-24T17:02:34+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. IN0 --snapshots` | 12 claims, 0 with a Fail; {"K-resolve": {"Pass": 12}, "K-access": {"Pass": 4, "n/a": 8}, "K-sim": {"n/a": 6, "Pass": 6}, "K-phrase": {"Pass": 8, "n/a": 4}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. IN0` | 6 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 15} |
| Simulation validation checks | EXECUTION_RECORD.json | 6/6 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 12/13 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Insurgence Cycle-0-Baseline — 12 claims, 6 sources in the register, 6 simulation runs, 3 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Three new sources (P25, P26 on PMC; P27 course notes, non-PMC) read in full; three fields (NAT, HUM, PHI) reuse sources read in full in earlier Divergence cycles (P22, P21, P08) without a new search. No empty passes (6/6 passes added a claim), but three added no new source.
- P27 is course lecture notes with no licence stated on the page; only short phrases are quoted. P27 contains a small typo ('Poisson(c-1) rather than Poisson(c-1)').
- New sim kinds (transcritical_onset, er_giant, moro_arith, branching_outbreak, insurgent_style, novelty_stream) were smoke-tested once (seed 99, reduced size) before SPECs were written; the smoke showed the SOC H2 outcome (not supported under the linear link) in advance; the 0.05 threshold was not changed.
- The 'Insurgence' operationalizations per field are this track's choices; none of the sources uses the word.
- Pushed to research/phase-insurgence-c0 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. Gate INDETERMINATE (independent review pending).
