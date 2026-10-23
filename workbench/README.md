# GAIA Research Workbench

Local-first research workbench implementing GAIA-BUILD-001 (M0/M1 vertical slice).

## Status
- Proposed engineering specification implemented as a runnable offline Python application.
- Uses synthetic fixtures. Original full package is incomplete in the repository; missing files are reported as such.
- Does not claim to be a Super-OS, Universe Digital Twin, or validated metaphysical system.

## Run
```bash
cd workbench
pip install -r requirements.txt
uvicorn app.main:app --host 127.0.0.1 --port 8000
```
Then open http://127.0.0.1:8000

## Features (this slice)
- Package ZIP inventory (missing/changed/extra/unsafe)
- 625-cell canonical grid generation (stable IDs, default NOT_ASSESSED)
- Simple dashboard UI
- Synthetic numeric fixtures (GAIA-SIM-002)
- SQLite persistence
- Unknowns endpoint

## Limitations
- Full original reports/PDF/grid CSV not present; importer demonstrates with fixtures.
- No authentication beyond loopback + trusted-device assumption.
- No full claim graph UI, ethics workflow engine, or export ZIP yet (planned for later milestones).
- Independent review pending.

See docs/ for architecture notes.
