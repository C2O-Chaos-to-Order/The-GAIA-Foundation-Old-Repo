# Validation outputs (v2)

| File | Tool | What it shows |
|---|---|---|
| `schema_validation.json` | `python -m gaia_tools.validate ..` | schema + cross-file errors (0) and warnings |
| `claim_source_C0/C1/C2.json` | `python -m gaia_tools.claimsource .. C<n> --snapshots DIR` | K-resolve / K-access / K-sim / K-phrase per claim |
| `rerun_C0.json`, `rerun_C1.json` | copied from v1 (C0/C1 unchanged) | re-execution identity |
| `rerun_C2.json` | `python -m gaia_tools.rerun .. C2` | 42 Cycle-2 runs re-executed from a fresh copy |
