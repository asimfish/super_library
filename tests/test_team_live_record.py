"""Replay real host-agent artifacts; never score prose quality from schema checks."""

import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import team_workflow as team


class LiveTeamRecordTests(unittest.TestCase):
    def test_public_live_records_resume_and_export_exact_reviewed_text(self):
        fixtures = sorted((ROOT / "evals/team-smoke-2026-10").glob("*.state.json"))
        self.assertEqual([path.name for path in fixtures], ["initial.state.json", "refined.state.json"])
        manifest = json.loads((ROOT / "evals/team-smoke-2026-10/manifest.json").read_text())
        self.assertFalse(manifest["held_out"])
        self.assertFalse(manifest["blind_comparison"])
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name), tempfile.TemporaryDirectory() as directory:
                run = Path(directory)
                shutil.copyfile(fixture, run / "state.json")
                (run / ".lock").touch()
                state = json.loads(fixture.read_text())
                metadata = next(item for item in manifest["runs"] if fixture.name == item["name"] + ".state.json")
                self.assertEqual(state["state_sha256"], metadata["state_sha256"])
                self.assertEqual(state["frozen_sha256"], metadata["frozen_sha256"])
                status = team.status(run)
                self.assertTrue(status["reviews_complete"])
                if status["can_export"]:
                    self.assertEqual(team.export(run), state["artifacts"]["writer"]["output"]["text"])
                else:
                    with self.assertRaises(ValueError):
                        team.export(run)
                actors = {record["actor_id"] for record in state["artifacts"].values()}
                self.assertEqual(len(actors), 5)
                self.assertEqual(state["frozen"]["task"], json.loads(
                    (ROOT / "examples/team/experiment-task.json").read_text()))


if __name__ == "__main__":
    unittest.main()
