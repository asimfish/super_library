"""Audit the frozen diagnostic evidence, not its subjective quality scores."""

import hashlib
import json
import statistics
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class DiagnosticPilotTests(unittest.TestCase):
    def setUp(self):
        self.study = json.loads((ROOT / "library/studies/agent_pilot_2026-10.json").read_text())

    def test_frozen_responses_and_ratings_have_complete_nonoverlapping_coverage(self):
        self.assertTrue(self.study["not_formal_release_evidence"])
        self.assertEqual(self.study["generation_controls"]["immutable_model_revision"], "unexposed")
        dimensions = {d["id"] for d in json.loads((ROOT / "evals/professionalism.json").read_text())["rubric_dimensions"]}
        seen = set()
        for phase in self.study["phases"]:
            self.assertEqual(len(phase["cases"]), 4)
            for case in phase["cases"]:
                self.assertNotIn(case["case_id"], seen)
                seen.add(case["case_id"])
                conditions = set(case["responses"])
                self.assertEqual(len(case["ratings"]), 2)
                self.assertEqual(len({r["rater_id"] for r in case["ratings"]}), 2)
                for response in case["responses"].values():
                    self.assertEqual(hashlib.sha256(response["text"].encode()).hexdigest(), response["sha256"])
                for rating in case["ratings"]:
                    self.assertEqual(set(rating["scores_by_condition"]), conditions)
                    self.assertLessEqual(set(rating["preferred_conditions"]), conditions)
                    for score in rating["scores_by_condition"].values():
                        self.assertEqual(set(score["scores"]), dimensions)
                        self.assertTrue(all(type(n) is int and 1 <= n <= 5 for n in score["scores"].values()))

    def test_summary_arithmetic_and_adverse_discovery_evidence_are_preserved(self):
        for phase in self.study["phases"]:
            for condition, mean in phase["mean_six_dimension_score"].items():
                observed = statistics.mean(statistics.mean(r["scores_by_condition"][condition]["scores"].values())
                    for c in phase["cases"] for r in c["ratings"])
                self.assertAlmostEqual(observed, mean)
        discovery = next(p for p in self.study["phases"] if p["id"] == "discovery")
        self.assertTrue(any("control" in r["preferred_conditions"]
                            for c in discovery["cases"] for r in c["ratings"]))


if __name__ == "__main__":
    unittest.main()
