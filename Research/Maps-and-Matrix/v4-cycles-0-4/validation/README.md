# Validation outputs (v4)

| File | Tool | What it shows |
|---|---|---|
| `schema_validation.json` | `python -m gaia_tools.validate ..` | schema + cross-file errors and warnings |
| `claim_source_C0..C4.json` | `python -m gaia_tools.claimsource .. C<n> --snapshots DIR` | K-resolve / K-access / K-sim / K-phrase per claim |
| `rerun_C0..C3.json` | copied from v3 (trees unchanged) | re-execution identity |
| `rerun_C4.json` | `python -m gaia_tools.rerun .. C4` | 84 Cycle-4 runs re-executed from a fresh copy |
