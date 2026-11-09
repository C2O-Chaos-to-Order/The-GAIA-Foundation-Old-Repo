"""Wave 1 remediation N24: re-execution must produce fresh evidence.

Audit finding N24 (2026-11-07, High): ``gaia_tools.rerun`` copies the Cycles
tree -- including the stored EXECUTION_RECORD.json files and outputs -- into a
temporary directory, runs each script, and then compares the stored record with
whatever record is in the copy. A script replaced by ``pass`` writes nothing,
so the copied (cached) record is compared with itself and the CLI reported
"ALL IDENTICAL (7 runs)" with exit 0.

Standard-library unittest only (no pytest). Every test works on a scratch copy
of Cycle-0; the checked-in tree is never modified. Run from the repository root:

    python3 -m unittest discover -s Research/tools/tests -p "test_w1_n24*.py" -v

Limitation: the genuine C0 simulations need numpy/scipy, which are not part of
this stdlib-only test profile, so the positive control below uses a stand-in
script that freshly writes the stored bytes. It shows the checker accepts a run
that really regenerates its record and outputs; it is not a scientific rerun.
"""

import glob
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
RESEARCH = TOOLS.parent
CYCLE0 = RESEARCH / "Cycles" / "Cycle-0-Baseline"
sys.path.insert(0, str(TOOLS))

from gaia_tools import rerun  # noqa: E402

_REGENERATE = '''import json, os, shutil
here = os.path.dirname(os.path.abspath(__file__))
SOURCE = {source!r}
os.makedirs(os.path.join(here, "outputs"), exist_ok=True)
for rel in {outputs!r}:
    os.makedirs(os.path.dirname(os.path.join(here, rel)), exist_ok=True)
    shutil.copyfile(os.path.join(SOURCE, rel), os.path.join(here, rel))
{write_record}
'''


def _live_scripts(cycle_dir: Path):
    return [p for p in cycle_dir.rglob("sim_*.py") if "archive_v1" not in p.parts]


class W1N24RerunFreshnessTest(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="w1-n24-"))
        self.research = self.tmp / "Research"
        self.cycle = self.research / "Cycles" / "Cycle-0-Baseline"
        self.cycle.parent.mkdir(parents=True)
        shutil.copytree(CYCLE0, self.cycle, ignore=shutil.ignore_patterns("__pycache__"))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _cli(self):
        env = dict(os.environ, PYTHONPATH=str(TOOLS), PYTHONDONTWRITEBYTECODE="1")
        return subprocess.run(
            [sys.executable, "-m", "gaia_tools.rerun", str(self.research), "C0"],
            env=env, capture_output=True, text=True,
        )

    def _replace_scripts(self, write_record: bool, write_outputs: bool):
        for script in _live_scripts(self.cycle):
            simdir = script.parent
            record_path = simdir / "EXECUTION_RECORD.json"
            stored = json.loads((CYCLE0 / record_path.relative_to(self.cycle)).read_text())
            outputs = list(stored.get("outputs") or {}) if write_outputs else []
            record_line = (
                "open(os.path.join(here, 'EXECUTION_RECORD.json'), 'w').write("
                f"{json.dumps(json.dumps(stored))})" if write_record else "pass"
            )
            script.write_text(_REGENERATE.format(
                source=str(CYCLE0 / simdir.relative_to(self.cycle)),
                outputs=outputs, write_record=record_line,
            ))

    def test_noop_scripts_cannot_pass_reexecution(self):
        scripts = _live_scripts(self.cycle)
        self.assertEqual(len(scripts), 7)
        for script in scripts:
            script.write_text("pass\n")
        proc = self._cli()
        self.assertNotEqual(proc.returncode, 0, proc.stdout)
        self.assertNotIn("ALL IDENTICAL", proc.stdout)

    def test_noop_rows_report_missing_fresh_record(self):
        for script in _live_scripts(self.cycle):
            script.write_text("pass\n")
        report = rerun.run_cycle(str(self.research), "C0")
        self.assertFalse(report["all_identical"])
        self.assertEqual(report["n_runs"], 7)
        for row in report["runs"]:
            self.assertFalse(row["fresh_record"], row)
            self.assertFalse(row["outputs_identical"], row)

    def test_record_without_regenerated_outputs_is_rejected(self):
        self._replace_scripts(write_record=True, write_outputs=False)
        report = rerun.run_cycle(str(self.research), "C0")
        self.assertFalse(report["all_identical"])
        for row in report["runs"]:
            if row["expected_outputs"]:
                self.assertTrue(row["fresh_record"], row)
                self.assertFalse(row["outputs_present"], row)

    def test_run_that_regenerates_record_and_outputs_is_accepted(self):
        self._replace_scripts(write_record=True, write_outputs=True)
        report = rerun.run_cycle(str(self.research), "C0")
        for row in report["runs"]:
            self.assertEqual(row["exit"], 0, row)
            self.assertTrue(row["fresh_record"], row)
            self.assertTrue(row["outputs_present"], row)
        self.assertTrue(report["all_identical"], report)

    def test_checked_in_tree_is_not_modified(self):
        before = {p: p.stat().st_mtime_ns for p in CYCLE0.rglob("*") if p.is_file()}
        for script in _live_scripts(self.cycle):
            script.write_text("pass\n")
        rerun.run_cycle(str(self.research), "C0")
        after = {p: p.stat().st_mtime_ns for p in CYCLE0.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


class W1N24TrackAndPhaseRerunFreshnessTest(unittest.TestCase):
    """Same cached-record pattern in ``tracks.rerun`` and ``phases.rerun``.

    The audit only tamper-probed ``gaia_tools.rerun`` (C0). Both sibling runner
    families copy the cycle, including stored EXECUTION_RECORD.json files, and
    compare after execution in the same way; these tests probe them directly.
    """

    CASES = (
        ("tracks", "TA", Path("Tracks/Soul-Spirit-Subconscious-Consciousness/Cycle-A-x3")),
        ("phases", "DV0", Path("Tracks/Phases/Divergence/Cycle-0-Baseline")),
    )

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="w1-n24-tp-"))
        self.research = self.tmp / "Research"

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _copy(self, rel):
        target = self.research / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(RESEARCH / rel, target, ignore=shutil.ignore_patterns("__pycache__"))
        return target

    def test_noop_scripts_cannot_pass_track_or_phase_reexecution(self):
        import importlib

        for module_name, cycle_id, rel in self.CASES:
            with self.subTest(runner=module_name):
                target = self._copy(rel)
                scripts = list(target.rglob("sim_*.py"))
                self.assertTrue(scripts)
                for script in scripts:
                    script.write_text("pass\n")
                module = importlib.import_module(f"gaia_tools.{module_name}")
                report = module.rerun(str(self.research), cycle_id)
                self.assertGreater(report["n_runs"], 0)
                self.assertFalse(report["all_identical"], f"{module_name} accepted cached records")
                for row in report["runs"]:
                    self.assertFalse(row["fresh_record"], row)


if __name__ == "__main__":
    unittest.main()
