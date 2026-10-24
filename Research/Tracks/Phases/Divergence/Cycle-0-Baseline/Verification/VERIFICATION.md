# Verification — Divergence Cycle-0-Baseline (DV0)

Checked 2026-10-24T07:55:27+00:00 by the producing agent (Grok Bot). This is internal consistency and reproducibility only; **independent challenge has not happened**, so the gate is **INDETERMINATE** (Indeterminate is never Pass; GOVERNANCE/UNIVERSAL_REGULATION.md §2).

| check | tool | result |
|---|---|---|
| Schema and cross-file rules (E1-E10) over all phase cycles | `python -m gaia_tools.phases validate ..` | 0 errors, 0 warnings (`schema_validation_phases.json`) |
| Claim-source (resolve, full-text rule for Established, SIM outcome wording, phrases vs local snapshots) | `phases claimsource .. DV0 --snapshots` | 22 claims, 0 with a Fail; {"K-resolve": {"Pass": 22}, "K-access": {"Pass": 10, "n/a": 12}, "K-sim": {"n/a": 16, "Pass": 6}, "K-phrase": {"Pass": 15, "n/a": 7}} |
| Re-execution in a temporary copy (spec, params, results hashes and check outcomes) | `phases rerun .. DV0` | 6 runs, all identical: True |
| Live re-fetch of each verification phrase from the source URL | `build15/verify.py` | {"Pass": 20} |
| Simulation validation checks | EXECUTION_RECORD.json | 7/8 Pass; failures: SIM-DV-PHI-0 iter-1 V1 |
| Simulation hypotheses | EXECUTION_RECORD.json | 7/8 Supported (the rest Not supported; findings, not errors) |
| Manifest | `MANIFEST.sha256` | sha256 of every file in this cycle folder |

## Gate record (UNIVERSAL_REGULATION.md §3)
- **Scope:** Divergence Cycle-0-Baseline — 22 claims, 9 sources in the register, 6 simulation runs, 5 links.
- **Criteria:** 0 validation errors; 0 claim-source Fail; reruns identical; live phrases Pass; validation checks Pass or disclosed; independent review recorded.
- **Decision:** INDETERMINATE. **Authority:** the owner (Kyle Alexander Steen) or a reviewer he names; the agent cannot pass its own gate. **Blockers:** independent review; validation failures disclosed: SIM-DV-PHI-0 iter-1 V1.

## Disclosures
- SIM-DV-PHI-0 iter-1 V1 Fail (7.877 vs analytic 7.485; tolerance 5% without Monte Carlo allowance). Recorded, not re-run. Out-of-record diagnostic: 3,000 replicates gave 7.524 (SE 0.044), so the Fail is attributed to the tolerance, not the code. DV0-PHI-04 is labelled Hypothetical.
- SIM-DV-NAT-0 H1 threshold set to 0.25 after a pre-spec smoke test showed the first draft (0.5) mis-specified the two-deme statistic; disclosed in the SPEC.
- SIM-DV-APP-0 H1 Not supported (R^2 0.958 < 0.98); kept as a finding.
- arXiv API queries timed out (logged with n = 0); Europe PMC search returned HTTP 503 at 07:4xZ, so NCBI E-utilities were used for search and full text (reference lists stripped from the stored text).
- 'Read in full' means the full text was retrieved and stored (hash in the register) and the passages cited were read; the agent did not read every paragraph of every source line by line.
