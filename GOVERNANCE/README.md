# GOVERNANCE

Governance standards for The GAIA Foundation. **Owner and decision authority:** KyleAlexanderSteen (repository owner).

| File | What it is | Status |
|---|---|---|
| [`UNIVERSAL_REGULATION.md`](UNIVERSAL_REGULATION.md) | GAIA Universal Regulation Standard (GAIA-GOV-UR-001): the owner's principle, seven laws, five regulation domains and absolute boundary, with derived domain-standard stubs | **Proposed** (not adopted, not implemented) |
| [`AUDIT_UNIVERSAL_REGULATION_v1.md`](AUDIT_UNIVERSAL_REGULATION_v1.md) | First audit of the repository against the standard (20 PASS / 13 FAIL / 12 INDETERMINATE) | Gate **INDETERMINATE**; preserved unchanged |
| [`AUDIT_UNIVERSAL_REGULATION_v1.csv`](AUDIT_UNIVERSAL_REGULATION_v1.csv) | Audit v1 items | Data for v1 |
| [`AUDIT_UNIVERSAL_REGULATION_v2.md`](AUDIT_UNIVERSAL_REGULATION_v2.md) | Re-audit after remediation (29 PASS / 3 FAIL / 13 INDETERMINATE) | Gate **INDETERMINATE** (self-audit; independent review pending) |
| [`AUDIT_UNIVERSAL_REGULATION_v2.csv`](AUDIT_UNIVERSAL_REGULATION_v2.csv) | Audit v2 items, with v1 decision and change per item | Data for v2 |
| [`GATE_AUTHORITY.md`](GATE_AUTHORITY.md) | Who decides gates: the owner; agents never; INDETERMINATE is never PASS; merge is not a gate PASS; register of gate records | Proposed |
| [`RISK_LEVELS.md`](RISK_LEVELS.md) | Risk tiers (the responsibility ladder) and overlays, applied to every product | Proposed |
| [`PRODUCT_REGISTER.csv`](PRODUCT_REGISTER.csv) | 64 products: owner, decision authority, tier, overlays, effects, safeguards, gate | Generated |
| [`LAW2_CROSSWALK.md`](LAW2_CROSSWALK.md) | Four claim labels mapped onto Law 2's six distinctions, with limits | Proposed |
| [`LAW2_CROSSWALK_COUNTS.csv`](LAW2_CROSSWALK_COUNTS.csv) | Crosswalk per (label, claim_class) with row counts | Generated |
| [`AGENT_PUSH_LOG.md`](AGENT_PUSH_LOG.md) | Which branches an AI agent wrote; attribution rule | Self-report |
| [`CHANGELOG.md`](CHANGELOG.md) | Change history of this folder, incidents and remediation policy | — |
| [`tools/build_registers.py`](tools/build_registers.py) | Generator for the two generated CSV files (research tooling only) | — |
| `MANIFEST.sha256` | SHA-256 digests of the other files in this folder (paths relative to this folder) | — |

Related files at the repository root: [`../SECURITY.md`](../SECURITY.md), [`../.github/CODEOWNERS`](../.github/CODEOWNERS), [`../.github/workflows/verify.yml`](../.github/workflows/verify.yml).

This folder adds to `Research/README.md` and `Research/RESEARCH_PLAN_EXTENSION.md`; it does not modify or replace them. Nothing here authorizes implementation or deployment.
