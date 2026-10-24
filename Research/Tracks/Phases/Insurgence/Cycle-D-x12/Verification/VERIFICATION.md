# Verification — Insurgence Cycle-D-x12 (IND)

Checked 2026-10-24T18:41:23+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. IND --snapshots` | 89 claims, 0 with a Fail; {"K-resolve": {"Pass": 89}, "K-access": {"Pass": 11, "n/a": 78}, "K-sim": {"n/a": 27, "Pass": 62}, "K-phrase": {"Pass": 33, "n/a": 56}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. IND` | 72 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 64} |
| Simulation validation checks | EXECUTION_RECORD.json | 72/72 Pass; failures: none |
| Simulation hypotheses | EXECUTION_RECORD.json | 83/96 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Insurgence Cycle-D-x12 — 89 claims, 21 sources in the register, 72 simulation runs, 11 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; none other.

## Disclosures
- Three new sources read in full: P40 (Wan, Riedl & Lazer 2025, CC BY-NC-ND; fetched in INC, read in IND; SI not read), P44 and P45 (Downey, Think Complexity 7.3 and 7.4, LibreTexts, CC BY-NC-SA 3.0). NAT, APP, HUM and PHI received no new source; P42 remains unread and uncited.
- Empty passes: 58 of 72. Diminishing returns are strong: only FOR and SOC added substantive claims, both from pass 1 sources; NAT, APP, HUM and PHI are replications and small variants.
- Source issues recorded: P45 writes p and q interchangeably for the same probability; P40 has two small text slips ('With higher p 2 but lower p 2', meaning lower p1; Fig. 2A caption names the orange region 'clustered networks outspread random networks').
- Smoke tests (seed 99) gave foreknowledge disclosed in SPECs: percolation 0.02/0.66/1.0 (100 arrays); complex contagion at (0.05, 0.9) 0.02 vs 0.003. A code bug (a name-scoping error in evaluating the hypothesis expression) stopped the run at SOC iter-4; it was fixed without changing any spec or threshold and the run resumed from iter-4 (iter-1 to 3 unaffected; reruns check reproducibility).
- Not supported: NAT iter-11 H1; SOC iter-5 H1, iter-9 H1, iter-10 H1, iter-11 H1 (flip from INC), iter-12 H1 and H2; APP iter-1 H1, iter-8 H1, iter-10 H1-H3, iter-12 H1. Two INC results flipped on new seeds (SOC q = 0.7 tail gap; APP AR1 trend): both marginal.
- Live phrase check: the first attempt gave 63 Pass and 1 Indeterminate (HTTP 500 from LibreTexts for P22, transient: three later fetches returned 200); the live check alone was re-run once and gave 64/64 Pass (first attempt kept in build15/verify_local_IND.json).
- Unsourced standard results used from the agent's knowledge (labelled): site-percolation threshold 0.5927 and finite-size sharpening; Kramers' law and the fold value carried from INC.
- Pushed to research/phase-insurgence-x12 with git over HTTPS (user token, never printed or stored); commits authored by Grok Bot with a Co-authored-by: Kyle Steen trailer. CI (GitHub Actions) is paused for cost; all checks run locally. Gate INDETERMINATE.
