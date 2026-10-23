"""GAIA Research Workbench — FastAPI application (local-first)."""
from fastapi import FastAPI, UploadFile, File, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path
import json
import sqlite3
from datetime import datetime
from .domain import generate_canonical_grid, CellRecord
from .importer import inventory_zip, inventory_directory

app = FastAPI(title="GAIA Research Workbench", version="0.1.0")
BASE = Path(__file__).parent.parent
templates = Jinja2Templates(directory=str(BASE / "templates"))
app.mount("/static", StaticFiles(directory=str(BASE / "static")), name="static")

# Simple SQLite
DB = BASE / "workbench.db"
def init_db():
    conn = sqlite3.connect(DB)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS packages (
            id INTEGER PRIMARY KEY,
            name TEXT,
            imported_at TEXT,
            status TEXT,
            inventory_json TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS cells (
            cell_id TEXT PRIMARY KEY,
            data_json TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS runs (
            id INTEGER PRIMARY KEY,
            run_id TEXT,
            started_at TEXT,
            result_json TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Seed grid if empty
def ensure_grid():
    conn = sqlite3.connect(DB)
    cur = conn.execute("SELECT COUNT(*) FROM cells")
    if cur.fetchone()[0] == 0:
        for cell in generate_canonical_grid():
            conn.execute("INSERT INTO cells (cell_id, data_json) VALUES (?, ?)",
                         (cell.cell_id, cell.model_dump_json()))
        conn.commit()
    conn.close()

ensure_grid()

@app.get("/health")
def health():
    return {"status": "ok", "offline": True, "version": "0.1.0"}

@app.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    conn = sqlite3.connect(DB)
    pkgs = conn.execute("SELECT id, name, status, imported_at FROM packages").fetchall()
    cell_count = conn.execute("SELECT COUNT(*) FROM cells").fetchone()[0]
    conn.close()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "packages": pkgs,
        "cell_count": cell_count,
        "status_note": "Synthetic fixtures only; originals incomplete"
    })

@app.post("/imports/preview")
async def import_preview(file: UploadFile = File(...)):
    tmp = BASE / "tmp_upload.zip"
    content = await file.read()
    tmp.write_bytes(content)
    inv = inventory_zip(tmp)
    tmp.unlink(missing_ok=True)
    return JSONResponse(inv)

@app.post("/imports/commit")
async def import_commit(file: UploadFile = File(...), name: str = "imported"):
    tmp = BASE / "tmp_upload.zip"
    content = await file.read()
    tmp.write_bytes(content)
    inv = inventory_zip(tmp)
    tmp.unlink(missing_ok=True)
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO packages (name, imported_at, status, inventory_json) VALUES (?, ?, ?, ?)",
                 (name, datetime.utcnow().isoformat(), inv.get("status", "UNKNOWN"), json.dumps(inv)))
    conn.commit()
    conn.close()
    return {"committed": True, "status": inv.get("status")}

@app.get("/grid")
def get_grid(mode: str = None, domain: str = None, phase: str = None, lens: str = None):
    conn = sqlite3.connect(DB)
    rows = conn.execute("SELECT data_json FROM cells").fetchall()
    conn.close()
    cells = [json.loads(r[0]) for r in rows]
    if mode:
        cells = [c for c in cells if c["mode"] == mode]
    if domain:
        cells = [c for c in cells if c["domain"] == domain]
    if phase:
        cells = [c for c in cells if c["phase"] == phase]
    if lens:
        cells = [c for c in cells if c["lens"] == lens]
    return {"count": len(cells), "cells": cells[:50]}  # paginate in real UI

@app.post("/runs")
def run_simulation():
    """Bounded synthetic numeric fixtures. No network, no eval of imports."""
    # Fixture 1: 5x4 outer product +1
    a = [0, 1, 3, 5, 0]
    b = [3, 6, 9, 12]
    M = [[ai * bj + 1 for bj in b] for ai in a]
    # Fixture 2: elementwise then scalars
    A = [0, 1, 2, 3, 0]
    B = [1, 3, 5, 7, 0]
    C = [3, 6, 9, 12, 0]
    elem = [x*y*z for x,y,z in zip(A,B,C)]
    zeroed = [x * 1 * 0 for x in elem]
    result = {
        "run_id": f"GAIA-SIM-002-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}",
        "fixture1_shape": "5x4",
        "fixture1_matrix": M,
        "fixture2_elementwise": elem,
        "fixture2_literal_zero": zeroed,
        "fifth_coefficient": "UNDEFINED",
        "note": "Conditional arithmetic only; not empirical validation"
    }
    conn = sqlite3.connect(DB)
    conn.execute("INSERT INTO runs (run_id, started_at, result_json) VALUES (?, ?, ?)",
                 (result["run_id"], datetime.utcnow().isoformat(), json.dumps(result)))
    conn.commit()
    conn.close()
    return result

@app.get("/unknowns")
def unknowns():
    return {
        "unknowns": [
            "exact three-of-five component set",
            "Soul/Spirit interpretation",
            "phase order fixed or optional",
            "numeric operator meanings",
            "missing fifth original phase weight",
            "Origin scope",
            "utility benchmark"
        ]
    }
