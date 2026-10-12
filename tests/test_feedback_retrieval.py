"""Probe-driven retrieval contracts; these do not rate generated prose."""

import copy
import json
import re
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import superlib


class FeedbackRetrievalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.taxonomy, cls.sources, cls.entries = superlib.load_corpus()
        cls.sources_by_id = {s["id"]: s for s in cls.sources}

    def technical(self, query, domain, topic=()):
        return superlib.rank_entries(self.entries, self.sources_by_id, query, [domain],
                                     kinds=("term", "definition", "usage_note"),
                                     include_general=False, topics=topic)

    def test_positive_collocations_beat_incidental_keyword_overlap(self):
        for query, domain, expected in (
            ("matched interaction budget", "reinforcement_learning", "rl.term.sample-efficiency.001"),
            ("model-query latency", "vision_language_action", "vla.usage-note.control-latency.001"),
            ("model query latency", "vision_language_action", "vla.usage-note.control-latency.001"),
            ("MODEL QUERY LATENCY", "vision_language_action", "vla.usage-note.control-latency.001"),
        ):
            with self.subTest(query=query):
                self.assertEqual(self.technical(query, domain)[0][1]["id"], expected)

    def test_reporting_terms_survive_domain_and_topic_filters(self):
        for query, domain, topic, expected in (
            ("confidence interval", "embodied_ai", "robot_manipulation", "general.usage-note.confidence-interval.001"),
            ("percentage points", "vision_language_action", "vla_models", "general.usage-note.percentage-points.001"),
        ):
            matches = self.technical(query, domain, [topic])
            self.assertTrue(matches, query)
            self.assertEqual(matches[0][1]["id"], expected)
        unrelated = {e["id"] for _, e in self.technical("effectiveness", "world_models")}
        self.assertNotIn("general.usage-note.effectiveness.001", unrelated)

    def test_chinese_reporting_aliases_reach_the_same_root_and_portable_records(self):
        built = subprocess.run([sys.executable, str(ROOT / "scripts/superlib.py"), "build"],
                               capture_output=True, text=True)
        self.assertEqual(built.returncode, 0, built.stderr)
        for query, domain, expected in (
            ("置信区间", "embodied_ai", "general.usage-note.confidence-interval.001"),
            ("百分点", "vision_language_action", "general.usage-note.percentage-points.001"),
            ("相对百分比变化", "reinforcement_learning", "general.usage-note.percentage-points.001"),
        ):
            with self.subTest(query=query):
                matches = self.technical(query, domain)
                self.assertTrue(matches, query)
                self.assertEqual(matches[0][1]["id"], expected)
                result = subprocess.run([sys.executable, str(ROOT / "skills/super-library/scripts/lookup.py"),
                                         query, "--domain", domain, "--limit", "1", "--format", "ids"],
                                        cwd="/tmp", capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertEqual(result.stdout.strip(), expected)

    def test_negative_examples_are_not_positive_query_aliases(self):
        from retrieval import exact_positive_match
        entry = next(e for e in self.entries if e["id"] == "rl.term.sample-efficiency.001")
        self.assertTrue(exact_positive_match(entry, "matched interaction budget"))
        self.assertFalse(exact_positive_match(entry, "inference latency"))
        changed = copy.deepcopy(entry)
        changed["lexical_profile"]["contrasts"][0]["before"] = "misleading invented collocation"
        changed["lexical_profile"]["not_equivalent_to"].append("misleading invented collocation")
        self.assertFalse(exact_positive_match(changed, "misleading invented collocation"))
        self.assertFalse(exact_positive_match(entry, ""))

    def test_exact_match_does_not_bypass_domain_or_topic_restrictions(self):
        wrong_domain = self.technical("model query latency", "world_models")
        self.assertNotIn("vla.usage-note.control-latency.001", {e["id"] for _, e in wrong_domain})
        wrong_topic = self.technical("model query latency", "vision_language_action", ["robot_manipulation"])
        self.assertNotIn("vla.usage-note.control-latency.001", {e["id"] for _, e in wrong_topic})

    def test_recorded_development_probes_are_reproducible(self):
        snapshot = json.loads((ROOT / "library/studies/feedback_retrieval_2026-10.json").read_text())
        self.assertEqual(len(snapshot["cases"]), 8)
        self.assertIn("not a held-out", snapshot["limitations"])
        for case in snapshot["cases"]:
            matches = self.technical(case["query"], case["domain"])
            ids = [e["id"] for _, e in matches[:4]]
            self.assertEqual(ids, case["after_top4"])
            self.assertEqual(ids[0], case["expected_id"])

    def test_readme_paper_identifiers_remain_canonical_during_count_updates(self):
        links = re.findall(r"https://proceedings\.neurips\.cc/[^)\s]+", (ROOT / "README.md").read_text())
        self.assertTrue(links)
        canonical = {s["url"] for s in self.sources}
        for link in links:
            self.assertIn(link, canonical)

    def test_portable_and_root_positive_matching_agree(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/superlib.py"), "build"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((ROOT / "scripts/retrieval.py").read_bytes(),
                         (ROOT / "skills/super-library/scripts/retrieval.py").read_bytes())
        for query, domain, expected in (
            ("matched interaction budget", "reinforcement_learning", "rl.term.sample-efficiency.001"),
            ("model query latency", "vision_language_action", "vla.usage-note.control-latency.001"),
        ):
            result = subprocess.run([sys.executable, str(ROOT / "skills/super-library/scripts/lookup.py"),
                                     query, "--domain", domain, "--limit", "1", "--format", "ids"],
                                    cwd="/tmp", capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(result.stdout.strip(), expected)

    def test_bundle_preserves_both_passes_with_new_reporting_content(self):
        for fmt in ("markdown", "json"):
            result = subprocess.run([sys.executable, str(ROOT / "scripts/superlib.py"), "bundle",
                                     "--rhetoric-query", "finding led experimental narrative",
                                     "--technical-query", "confidence interval", "--domain", "embodied_ai",
                                     "--topic", "robot_manipulation", "--section", "experiments",
                                     "--guide", "experiments.analysis", "--limit", "2",
                                     "--max-chars", "24000", "--format", fmt],
                                    capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertLessEqual(len(result.stdout), 24000)
            self.assertIn("general.usage-note.confidence-interval.001", result.stdout)
            if fmt == "json":
                self.assertEqual({e["retrieval_pass"] for e in json.loads(result.stdout)["entries"]},
                                 {"rhetoric", "technical"})


if __name__ == "__main__":
    unittest.main()
