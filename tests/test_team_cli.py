"""Public command wiring, once-only retrieval, and the published fixture boundary."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts/superlib.py"
sys.path.insert(0, str(ROOT / "scripts"))
import team_workflow


def cli(*args):
    return subprocess.run([sys.executable, str(CLI), *args], cwd=ROOT,
                          capture_output=True, text=True)


class TeamCliTests(unittest.TestCase):
    def test_unavailable_posix_lock_does_not_break_config_reads(self):
        with patch.object(team_workflow, "fcntl", None), tempfile.TemporaryDirectory() as directory:
            self.assertEqual(team_workflow.load_config(ROOT)["schema_version"], "1.0")
            destination = Path(directory) / "run"
            with self.assertRaisesRegex(ValueError, "POSIX"):
                team_workflow.initialize(ROOT, destination, {}, "unused", {})
            self.assertFalse(destination.exists())

    def test_real_task_initializes_once_and_reader_gets_no_language_bundle(self):
        with tempfile.TemporaryDirectory() as directory:
            run = str(Path(directory) / "run")
            task = str(ROOT / "examples/team/experiment-task.json")
            initialized = cli("team", "init", "--task", task, "--run-dir", run)
            self.assertEqual(initialized.returncode, 0, initialized.stderr)
            self.assertEqual(json.loads(initialized.stdout)["ready_roles"], ["evidence_reader"])
            packet = cli("team", "next", "--run-dir", run, "--role", "evidence_reader")
            self.assertEqual(packet.returncode, 0, packet.stderr)
            body = json.loads(packet.stdout)
            self.assertEqual(body["task"], json.loads(Path(task).read_text()))
            self.assertNotIn("language_context", body["inputs"])
            state = json.loads((Path(run) / "state.json").read_text())
            self.assertLessEqual(len(state["frozen"]["language_context"]), 16000)
            self.assertEqual(len(state["frozen"]["argument_context"]["frames"]), 1)
            original = (Path(run) / "state.json").read_bytes()
            duplicate = cli("team", "init", "--task", task, "--run-dir", run)
            self.assertEqual(duplicate.returncode, 2)
            self.assertEqual(duplicate.stdout, "")
            self.assertEqual((Path(run) / "state.json").read_bytes(), original)
            denied = cli("team", "export", "--run-dir", run)
            self.assertEqual(denied.returncode, 2)
            self.assertEqual(denied.stdout, "")

    def test_retrieved_frame_matches_function_and_complete_output_budget(self):
        args = ("frames", "--section", "experiments", "--intent", "contrast",
                "--relation", "tradeoff", "--experiment-type", "efficiency")
        result = cli(*args)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLessEqual(len(result.stdout), 6000)
        records = json.loads(result.stdout)["frames"]
        self.assertEqual(len(records), 1)
        self.assertIn("tradeoff", records[0]["relations"])
        unknown = cli(*args[:-1], "not-a-type")
        self.assertEqual(unknown.returncode, 2)
        self.assertEqual(unknown.stdout, "")
        small = cli(*args, "--max-chars", "2000")
        self.assertEqual(small.returncode, 2)
        self.assertEqual(small.stdout, "")

    def test_invalid_guide_alignment_creates_no_run(self):
        with tempfile.TemporaryDirectory() as directory:
            task = json.loads((ROOT / "examples/team/experiment-task.json").read_text())
            task["guide"] = "abstract"
            source = Path(directory) / "task.json"
            source.write_text(json.dumps(task))
            run = Path(directory) / "run"
            result = cli("team", "init", "--task", str(source), "--run-dir", str(run))
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")
            self.assertFalse(run.exists())

    def test_public_example_preserves_previously_audited_values_and_table_locator(self):
        example = json.loads((ROOT / "examples/team/experiment-task.json").read_text())
        study = json.loads((ROOT / "library/studies/public_table_transfer_2026-10.json").read_text())
        original = json.loads(study["task_file_content"])["tasks"][0]
        for fact, row in zip(example["evidence"][:4], original["rows"]):
            for value in row[2:]:
                self.assertIn(str(value), fact["text"])
            self.assertIn("Table II", fact["locator"])
            self.assertTrue(fact["required"])
        self.assertIn("not a new blinded efficacy test", example["constraints"][0])


if __name__ == "__main__":
    unittest.main()
