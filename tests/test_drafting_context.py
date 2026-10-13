"""The drafting view is a projection, never a second authoritative dictionary."""

import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import superlib
import writing_context as context


def bundle(view, fmt="json", budget=24000):
    return subprocess.run([sys.executable, str(ROOT / "scripts/superlib.py"), "bundle",
        "--rhetoric-query", "finding led experimental narrative",
        "--technical-query", "model query latency", "--domain", "vision_language_action",
        "--section", "experiments", "--guide", "experiments.analysis", "--limit", "1",
        "--max-chars", str(budget), "--format", fmt, "--view", view],
        capture_output=True, text=True)


class DraftingContextTests(unittest.TestCase):
    def test_projection_preserves_meaning_constraints_sources_without_mutating_owner(self):
        _, _, entries = superlib.load_corpus()
        entry = next(e for e in entries if e["id"] == "vla.usage-note.control-latency.001")
        original = copy.deepcopy(entry)
        projected = context.project_entry(entry)
        for key in ("meaning", "guidance", "avoid", "source_ids"):
            self.assertEqual(projected[key], entry[key])
        self.assertEqual(projected["examples"], entry["examples"][:1])
        self.assertNotIn("contrasts", projected["lexical_profile"])
        projected["source_ids"].append("not-real")
        self.assertEqual(entry, original)

    def test_guide_projection_retains_all_checks_and_only_requested_overlays(self):
        guide = superlib.writing_guides_by_id()["experiments"]
        original = copy.deepcopy(guide)
        projected = context.project_guide(guide, ["robot_learning"])
        for key in ("inputs", "moves", "verification", "avoid"):
            self.assertEqual(projected[key], guide[key])
        self.assertEqual([o["id"] for o in projected["domain_overlays"]], ["embodied_ai"])
        self.assertNotIn("templates", projected)
        self.assertEqual(guide, original)

    def test_matched_ids_reduce_context_and_complete_default_stays_available(self):
        full = bundle("reference")
        draft = bundle("drafting")
        self.assertEqual(full.returncode, 0, full.stderr)
        self.assertEqual(draft.returncode, 0, draft.stderr)
        a, b = json.loads(full.stdout), json.loads(draft.stdout)
        self.assertEqual(a["retrieved_ids"], b["retrieved_ids"])
        self.assertLess(len(draft.stdout), len(full.stdout))
        self.assertEqual(b["context_view"], "drafting")
        self.assertIn("not a complete", b["projection_notice"])
        self.assertIn("templates", a["guide"])
        self.assertNotIn("templates", b["guide"])
        self.assertTrue(any("quality" in e for e in a["entries"]))
        self.assertEqual({e["retrieval_pass"] for e in b["entries"]}, {"rhetoric", "technical"})

    def test_both_formats_fail_closed_if_selected_view_cannot_fit(self):
        for fmt in ("markdown", "json"):
            large = bundle("drafting", fmt)
            self.assertEqual(large.returncode, 0, large.stderr)
            self.assertLessEqual(len(large.stdout), 24000)
            small = bundle("drafting", fmt, 100)
            self.assertEqual(small.returncode, 2)
            self.assertEqual(small.stdout, "")

    def test_portable_projection_matches_repository_and_retains_reference_show(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/superlib.py"), "build"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((ROOT / "scripts/writing_context.py").read_bytes(),
                         (ROOT / "skills/super-library/scripts/writing_context.py").read_bytes())
        _, sources, entries = superlib.load_corpus()
        entry = next(e for e in entries if e["id"] == "vla.usage-note.control-latency.001")
        result = subprocess.run([sys.executable, str(ROOT / "skills/super-library/scripts/lookup.py"),
            "--id", entry["id"], "--view", "drafting", "--format", "json"],
            capture_output=True, text=True, cwd="/tmp")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["entries"][0], context.project_entry(entry))
        shown = subprocess.run([sys.executable, str(ROOT / "scripts/superlib.py"), "show", entry["id"]],
                               capture_output=True, text=True)
        self.assertIn("Original conditional contrast", shown.stdout)

    def test_drafting_notice_preserves_facts_and_does_not_certify_correctness(self):
        self.assertIn("Facts come only from the task", context.NOTICE)
        self.assertIn("required values", context.NOTICE)
        self.assertIn("material adverse outcomes", context.NOTICE)
        self.assertIn("uncertainty", context.NOTICE)


if __name__ == "__main__":
    unittest.main()
