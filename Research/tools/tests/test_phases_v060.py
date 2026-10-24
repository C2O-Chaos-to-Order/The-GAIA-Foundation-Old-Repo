import csv, glob, json, os, shutil
import jsonschema, pytest
import gaia_tools
from gaia_tools import phases as PH

RESEARCH = os.path.join(os.path.dirname(__file__), "..", "..")
SCHEMA = json.load(open(os.path.join(os.path.dirname(PH.__file__), "schemas", "phase_claim.schema.json")))


def test_version():
    assert tuple(int(x) for x in gaia_tools.__version__.split(".")) >= (0, 6, 0)


def test_sim_ref():
    assert PH.SIM_REF.match("SIM-DV-NAT-0/iter-1#V1")
    assert PH.SIM_REF.match("SIM-AS-PHI-D/iter-12#H2")
    assert not PH.SIM_REF.match("SIM-SOUL-A/iter-1#V1")


def test_schema_rejects_bad_id():
    row = dict(claim_id="DV0-XYZ-01", field="NAT", wording="x" * 30, claim_class="Empirical", framework_label="Established", conclusion_status="Supported",
               source_ids="P01", locator="", confidence="", counterevidence_limits="", operationalization="", being="", cross_links="", verification_phrases="", change_vs_prev_cycle="")
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.validate(row, SCHEMA)


def test_corpus_rows_conform():
    n = 0
    for cid, cp, _ in PH.phase_cycles(RESEARCH):
        for r in PH.claims(cp):
            r = {k: v for k, v in r.items() if not k.startswith("_")}; jsonschema.validate(r, SCHEMA); n += 1
    if not n: pytest.skip("no phase cycles present")


def test_validate_no_errors():
    assert PH.validate(RESEARCH)["n_errors"] == 0


def test_claimsource_no_fail():
    for cid, _, _ in PH.phase_cycles(RESEARCH):
        assert PH.claimsource(RESEARCH, cid)["n_fail"] == 0


def test_spec_tamper_detected(tmp_path):
    pcs = PH.phase_cycles(RESEARCH)
    if not pcs: pytest.skip("no phase cycles present")
    dst = tmp_path / "Research"; os.makedirs(dst / "Tracks" / "Phases")
    cid, cp, ph = pcs[0]; shutil.copytree(cp, dst / "Tracks" / "Phases" / ph / os.path.basename(cp))
    spec = glob.glob(str(dst / "Tracks" / "Phases" / ph / os.path.basename(cp) / "*" / "simulation" / "iter-1" / "SPEC.md"))[0]
    open(spec, "a").write("\ntampered\n")
    assert any(e[1] == "E8" for e in PH.validate(str(dst))["errors"])
