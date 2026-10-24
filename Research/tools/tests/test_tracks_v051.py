import csv, os
import gaia_tools
from gaia_tools import maps_all

RESEARCH = os.path.join(os.path.dirname(__file__), "..", "..")


def test_version():
    assert tuple(int(x) for x in gaia_tools.__version__.split(".")) >= (0, 5, 1)


def test_stem():
    assert maps_all._stem("TA-SOUL-01") == "SOUL-01"
    assert maps_all._stem("TB-SUBC-12") == "SUBC-12"
    assert maps_all._stem("C4-R3-01") == "C4-R3-01"


def test_carried_track_claims_not_dropped(tmp_path):
    tb = os.path.join(RESEARCH, "Tracks", "Soul-Spirit-Subconscious-Consciousness", "Cycle-B-x6")
    if not os.path.isdir(tb):
        import pytest; pytest.skip("Track Cycle B not present")
    maps_all.build(RESEARCH, str(tmp_path), "test")
    rows = list(csv.DictReader(open(tmp_path / "claim_map" / "claim_map.csv", encoding="utf-8")))
    tb_rows = [r for r in rows if r["cycle"] == "TB"]
    assert not any(r["change_vs_prev_cycle"] == "dropped" for r in tb_rows)
    assert sum(r["change_vs_prev_cycle"] == "new" for r in tb_rows) < len(tb_rows)
