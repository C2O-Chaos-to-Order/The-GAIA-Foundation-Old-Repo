"""Tests for gaia_tools 0.5.0 / data model 1.4.0: track support (tracks.py) and maps over all work (maps_all.py)."""
import csv, glob, json, os, shutil, tempfile
import jsonschema, pytest
from conftest import RESEARCH
from gaia_tools import tracks as T, maps_all as MA, __version__, DATA_MODEL_VERSION
SCH = os.path.join(os.path.dirname(T.__file__), "schemas")
HAS_TRACK = bool(T.track_cycles(RESEARCH))
need = pytest.mark.skipif(not HAS_TRACK, reason="no track cycles in this corpus")


def _schema(n):
    return jsonschema.Draft202012Validator(json.load(open(os.path.join(SCH, n))))


def test_versions():
    assert tuple(int(x) for x in __version__.split(".")) >= (0, 5, 0) and tuple(int(x) for x in DATA_MODEL_VERSION.split(".")) >= (1, 4, 0)


def test_track_sim_ref():
    m = T.TRACK_SIM_REF.match("SIM-SUBC-B/iter-12#H3")
    assert m and m.group("topic") == "SUBC" and m.group("cyc") == "B" and m.group("it") == "12"
    assert not T.TRACK_SIM_REF.match("SIM-R5-C4/iter-1#V1") and not T.TRACK_SIM_REF.match("SIM-SOUL-A#H1")


def test_claim_schema_rejects_bad_rows():
    v = _schema("track_claim.schema.json")
    good = {k: "x" * 25 for k in T.CLAIM_FIELDS}
    good.update(claim_id="TA-SOUL-01", topic="SOUL", claim_class="Empirical", framework_label="Established", conclusion_status="Supported", source_ids="K01;SIM-SOUL-A/iter-1#V1")
    assert not list(v.iter_errors(good))
    for k, bad in (("claim_id", "TA-SOUL-1"), ("framework_label", "Proven"), ("source_ids", "Q99"), ("topic", "BODY")):
        assert list(v.iter_errors(dict(good, **{k: bad}))), k


@need
def test_corpus_claims_and_records_match_schemas():
    vc, vr = _schema("track_claim.schema.json"), _schema("track_execution_record.schema.json")
    for tid, cp, _ in T.track_cycles(RESEARCH):
        for r in T.claims(cp):
            assert not list(vc.iter_errors({k: v for k, v in r.items() if not k.startswith("_")})), r["claim_id"]
        for s in T.runs(cp, tid):
            assert not list(vr.iter_errors(json.load(open(os.path.join(cp, s["execution_record"]))))), s["directory"]


@need
def test_validate_corpus_has_no_errors():
    assert T.validate(RESEARCH)["n_errors"] == 0


@need
def test_claimsource_offline_no_fail():
    for tid, _, _ in T.track_cycles(RESEARCH):
        assert T.claimsource(RESEARCH, tid)["n_fail"] == 0


@need
def test_spec_tamper_is_detected(tmp_path):
    dst = tmp_path / "Research"; shutil.copytree(os.path.join(RESEARCH, "Tracks"), dst / "Tracks")
    spec = sorted(glob.glob(str(dst / "Tracks" / "*" / "Cycle-A-x3" / "Soul" / "simulation" / "iter-1" / "SPEC.md")))[0]
    open(spec, "a").write("\nedited after execution\n")
    assert any(e[1] == "E8" for e in T.validate(str(dst))["errors"])


@need
def test_not_supported_must_be_stated(tmp_path):
    dst = tmp_path / "Research"; shutil.copytree(os.path.join(RESEARCH, "Tracks"), dst / "Tracks")
    f = sorted(glob.glob(str(dst / "Tracks" / "*" / "Cycle-A-x3" / "Soul" / "claims" / "claims.csv")))[0]
    rows = list(csv.DictReader(open(f, encoding="utf-8"))); r = next(x for x in rows if "SIM-SOUL-A/iter-2#H1" in x["source_ids"])
    r["wording"] = r["wording"].replace("not supported", "n.s.")
    with open(f, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=T.CLAIM_FIELDS, lineterminator="\n"); w.writeheader(); w.writerows(rows)
    assert any(e[1] == "E6" for e in T.validate(str(dst))["errors"])


@need
def test_maps_all_deterministic_and_complete(tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    MA.build(RESEARCH, str(a), "t"); MA.build(RESEARCH, str(b), "t")
    for p in glob.glob(str(a / "**" / "*.*"), recursive=True):
        assert open(p, "rb").read() == open(str(b / os.path.relpath(p, a)), "rb").read(), p
    g = json.load(open(a / "graph" / "link_graph.json"))
    ids = {n["id"] for n in g["nodes"]}
    assert {"GAIA", "MR", "SOUL", "SPIRIT", "SUBC", "CONS"} <= ids
    mt = {e["target"] for e in g["edges"] if e["type"] == "motherthread"}
    assert {"SOUL", "SPIRIT", "SUBC", "CONS", "MR", "R1", "R7"} <= mt
    assert all(e["label_code"] in ("E", "P", "PS", "H") for e in g["edges"])
    assert any(e["id"].startswith("TL-") for e in g["edges"])
    cells = list(csv.DictReader(open(a / "matrix" / "intersections_625.csv")))
    assert len(cells) == 625 and "track_claims_in_projection" in cells[0]
    cm = list(csv.DictReader(open(a / "claim_map" / "claim_map.csv")))
    assert any(r["cycle"] == "MR" for r in cm) and any(r["cycle"] == "TA" for r in cm)
