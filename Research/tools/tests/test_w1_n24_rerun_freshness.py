"""Wave 1 N24: re-run paths are retired (2026-11-09).

History (kept; not silently rewritten):
- Audit finding N24 (2026-11-07, High): ``gaia_tools.rerun`` copied stored
  EXECUTION_RECORD.json files into a temporary tree, ran each script, and
  compared the stored record with whatever remained in the copy. A script
  replaced by ``pass`` wrote nothing, so the cached record was compared with
  itself and the CLI reported "ALL IDENTICAL (7 runs)" with exit 0.
- 2026-11-08 repair on this branch (commit 2b263e61): delete the copied
  record (and listed outputs) before execution so a no-op can no longer pass.
  Those freshness tests lived in this file and remain in git history.
- 2026-11-09 owner decision (Kyle Steen, card t44s607): RETIRE the re-run
  paths instead of keeping the repair. This file now proves the retired
  paths refuse with a clear 'retired' error.

Standard-library unittest only (no pytest). Run from the repository root:

    python3 -m unittest discover -s Research/tools/tests -p "test_w1_n24*.py" -v

The 8 pre-existing import errors in the rest of Research/tools/tests
(jsonschema / pytest / gaia_tools path issues on this box) are unchanged
and are not addressed here.
"""

import os
import subprocess
import sys
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS))

from gaia_tools.retirement import RerunRetired  # noqa: E402
from gaia_tools import rerun, tracks, phases  # noqa: E402


class W1N24RerunRetiredTest(unittest.TestCase):
    def test_rerun_run_cycle_refuses(self):
        with self.assertRaises(RerunRetired) as ctx:
            rerun.run_cycle("/no/such/research", "C0")
        self.assertIn("retired", str(ctx.exception).lower())
        self.assertIn("t44s607", str(ctx.exception))

    def test_rerun_cli_refuses(self):
        env = dict(os.environ, PYTHONPATH=str(TOOLS), PYTHONDONTWRITEBYTECODE="1")
        proc = subprocess.run(
            [sys.executable, "-m", "gaia_tools.rerun", "/no/such/research", "C0"],
            cwd=str(TOOLS), env=env, capture_output=True, text=True,
        )
        self.assertNotEqual(proc.returncode, 0, proc.stdout)
        combined = proc.stdout + proc.stderr
        self.assertIn("retired", combined.lower())
        self.assertNotIn("ALL IDENTICAL", combined)

    def test_tracks_rerun_refuses(self):
        with self.assertRaises(RerunRetired) as ctx:
            tracks.rerun("/no/such/research", "TA")
        self.assertIn("retired", str(ctx.exception).lower())

    def test_phases_rerun_refuses(self):
        with self.assertRaises(RerunRetired) as ctx:
            phases.rerun("/no/such/research", "DV0")
        self.assertIn("retired", str(ctx.exception).lower())

    def test_tracks_and_phases_cli_rerun_refuse(self):
        env = dict(os.environ, PYTHONPATH=str(TOOLS), PYTHONDONTWRITEBYTECODE="1")
        cases = (
            ["-m", "gaia_tools.tracks", "rerun", "/no/such/research", "TA"],
            ["-m", "gaia_tools.phases", "rerun", "/no/such/research", "DV0"],
        )
        for args in cases:
            with self.subTest(args=args[1]):
                proc = subprocess.run(
                    [sys.executable, *args],
                    cwd=str(TOOLS), env=env, capture_output=True, text=True,
                )
                self.assertNotEqual(proc.returncode, 0, proc.stdout)
                combined = proc.stdout + proc.stderr
                self.assertIn("retired", combined.lower())
                self.assertNotIn("ALL IDENTICAL", combined)

    def test_checked_in_tree_is_not_modified(self):
        research = TOOLS.parent
        cycle0 = research / "Cycles" / "Cycle-0-Baseline"
        before = {p: p.stat().st_mtime_ns for p in cycle0.rglob("*") if p.is_file()}
        with self.assertRaises(RerunRetired):
            rerun.run_cycle(str(research), "C0")
        after = {p: p.stat().st_mtime_ns for p in cycle0.rglob("*") if p.is_file()}
        self.assertEqual(before, after)


if __name__ == "__main__":
    unittest.main()
