"""Basic tests for grid generation and importer safety."""
import pytest
from pathlib import Path
import zipfile
import tempfile
from app.domain import generate_canonical_grid
from app.importer import inventory_zip, is_unsafe_path

def test_grid_size():
    cells = generate_canonical_grid()
    assert len(cells) == 625
    assert cells[0].cell_id == "GAIA-A1-B1-P1-E1"
    assert cells[-1].cell_id == "GAIA-A5-B5-P5-E5"
    assert all(c.evidence_status.value == "NOT_ASSESSED" for c in cells)

def test_unsafe_path():
    assert is_unsafe_path("../evil")
    assert is_unsafe_path("/absolute")
    assert not is_unsafe_path("safe/file.md")

def test_inventory_rejects_traversal():
    with tempfile.TemporaryDirectory() as td:
        zpath = Path(td) / "bad.zip"
        with zipfile.ZipFile(zpath, "w") as zf:
            zf.writestr("../escape.txt", b"bad")
        inv = inventory_zip(zpath)
        assert "unsafe" in inv or any(e.get("status") == "unsafe_entry" for e in inv.get("entries", []))
