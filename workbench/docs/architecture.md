# Architecture (M0/M1)

Local FastAPI app + SQLite.

- Content-addressed byte store planned (currently in-memory during inventory).
- Domain logic in app/domain.py (grid generator).
- Importer safety checks in app/importer.py (no execution of content).
- UI is server-rendered Jinja; API is JSON.

Threat model (trusted local host):
- Loopback binding.
- No remote credentials required.
- Imported content treated as untrusted; no eval/exec.
- CSRF protection deferred to later milestone; currently single-user trusted device.

See GAIA-BUILD-001 for full requirements.
