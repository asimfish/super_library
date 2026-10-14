"""Check diagnostic evidence identity and arithmetic, not writing efficacy."""

import hashlib
import json
import statistics
import unittest
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PublicTableTransferTests(unittest.TestCase):
    def setUp(self):
        self.study = json.loads(
            (ROOT / "library/studies/public_table_transfer_2026-10.json").read_text()
        )
        self.packet = json.loads(self.study["task_file_content"])

    def test_frozen_packet_sources_and_responses_have_complete_identity(self):
        study = self.study
        self.assertTrue(study["not_formal_release_evidence"])
        self.assertEqual(study["generation_controls"]["immutable_model_revision"], "unexposed")
        packet_hash = hashlib.sha256(study["task_file_content"].encode()).hexdigest()
        self.assertEqual(packet_hash, study["task_file_sha256"])
        self.assertEqual(hashlib.sha256(study["frozen_plan_content"].encode()).hexdigest(), study["frozen_plan_sha256"])
        self.assertEqual(hashlib.sha256(study["source_verification_file_content"].encode()).hexdigest(), study["source_verification_file_sha256"])
        self.assertEqual(json.loads(study["source_verification_file_content"]), study["source_verification"])
        tasks = {t["task_id"] for t in self.packet["tasks"]}
        self.assertEqual(tasks, {"T01", "T02", "T03", "T04"})
        self.assertEqual(len(study["sources"]), 3)
        self.assertEqual({t for s in study["sources"] for t in s["task_ids"]}, tasks)
        self.assertTrue(all(s["sha256"] and s["locator"] for s in study["sources"]))
        self.assertEqual({t["task_id"] for t in study["source_verification"]["tasks"]}, tasks)
        self.assertTrue(all(t["status"] == "verified" for t in study["source_verification"]["tasks"]))
        self.assertEqual(set(study["writers"]), {"baseline", "drafting"})
        for writer in study["writers"].values():
            self.assertEqual(writer["task_file_sha256"], packet_hash)
            self.assertEqual(hashlib.sha256(writer["raw_content"].encode()).hexdigest(), writer["raw_sha256"])
            responses = json.loads(writer["raw_content"])["responses"]
            self.assertEqual({r["task_id"] for r in responses}, tasks)
            self.assertEqual(len(responses), len(tasks))
            self.assertTrue(all(r["text"].strip() for r in responses))

    def test_blind_ratings_and_summary_cover_both_arms_without_quality_gate(self):
        study = self.study
        dimensions = {d["id"] for d in json.loads(
            (ROOT / "evals/professionalism.json").read_text()
        )["rubric_dimensions"]}
        critical_ids = {c["id"] for c in json.loads(
            (ROOT / "evals/professionalism.json").read_text()
        )["critical_errors"]}
        anonymous = json.loads(study["anonymous_file_content"])
        self.assertEqual(hashlib.sha256(study["anonymous_file_content"].encode()).hexdigest(), study["anonymous_file_sha256"])
        self.assertEqual(anonymous["task_file_sha256"], study["task_file_sha256"])
        pairs = {p["pair_id"]: p for p in anonymous["pairs"]}
        assignments = {a["pair_id"]: a for a in study["revealed_assignments"]}
        self.assertEqual(set(pairs), set(assignments))
        self.assertEqual(len(pairs), 4)
        tasks = {t["task_id"]: t for t in self.packet["tasks"]}
        responses = {c: {r["task_id"]: r["text"] for r in json.loads(w["raw_content"])["responses"]}
                     for c, w in study["writers"].items()}
        for pair_id, pair in pairs.items():
            task_id = assignments[pair_id]["task_id"]
            self.assertEqual(pair["task"], tasks[task_id])
            for side in ["a", "b"]:
                self.assertEqual(pair["response_" + side], responses[assignments[pair_id]["assignment"][side]][task_id])
        votes = {"baseline": 0, "drafting": 0, "tie": 0}
        means = {"baseline": [], "drafting": []}
        flagged = {"baseline": [], "drafting": []}
        self.assertEqual(len(study["raters"]), 2)
        for rater in study["raters"]:
            self.assertEqual(hashlib.sha256(rater["raw_content"].encode()).hexdigest(), rater["raw_sha256"])
            raw_rating = json.loads(rater["raw_content"])
            self.assertEqual(raw_rating["anonymous_file_sha256"], study["anonymous_file_sha256"])
            ratings = raw_rating["ratings"]
            self.assertEqual({r["pair_id"] for r in ratings}, set(pairs))
            self.assertEqual(len(ratings), len(pairs))
            for rating in ratings:
                assignment = assignments[rating["pair_id"]]["assignment"]
                self.assertEqual(set(assignment.values()), {"baseline", "drafting"})
                self.assertIn(rating["preferred"], {"a", "b", "tie"})
                votes["tie" if rating["preferred"] == "tie" else assignment[rating["preferred"]]] += 1
                for side in ["a", "b"]:
                    result = rating["scores_by_side"][side]
                    self.assertEqual(set(result["scores"]), dimensions)
                    self.assertTrue(all(type(n) is int and 1 <= n <= 5 for n in result["scores"].values()))
                    self.assertLessEqual(set(result["critical_errors"]), critical_ids)
                    means[assignment[side]].append(statistics.mean(result["scores"].values()))
                    if result["critical_errors"]:
                        flagged[assignment[side]].append([rater["rater_id"], rating["pair_id"], result["critical_errors"]])
        self.assertEqual(votes, study["summary"]["preference_votes"])
        for condition in means:
            self.assertAlmostEqual(statistics.mean(means[condition]), study["summary"]["mean_six_dimension_score"][condition])
            self.assertEqual(flagged[condition], study["summary"]["flagged_responses"][condition])

    def test_post_hoc_layouts_are_complementary_and_keep_frozen_outputs(self):
        stage = self.study["position_check"]
        self.assertFalse(stage["new_generation"])
        self.assertTrue(stage["outputs_unchanged"])
        self.assertEqual(hashlib.sha256(stage["plan_file_content"].encode()).hexdigest(), stage["plan_file_sha256"])
        responses = {c: {r["task_id"]: r["text"] for r in json.loads(w["raw_content"])["responses"]}
                     for c, w in self.study["writers"].items()}
        layouts = stage["layouts"]
        self.assertEqual(len(layouts), 2)
        maps = []
        votes = {"baseline": 0, "drafting": 0, "tie": 0}
        scores = {"baseline": [], "drafting": []}
        flags = {"baseline": [], "drafting": []}
        for layout in layouts:
            raw = layout["anonymous_file_content"]
            self.assertEqual(hashlib.sha256(raw.encode()).hexdigest(), layout["anonymous_file_sha256"])
            pairs = {p["pair_id"]: p for p in json.loads(raw)["pairs"]}
            mapping = {a["pair_id"]: a for a in layout["revealed_assignments"]}
            maps.append(mapping)
            self.assertEqual(sum(a["assignment"]["a"] == "drafting" for a in mapping.values()), 2)
            self.assertEqual(set(pairs), set(mapping))
            for pair_id, pair in pairs.items():
                for side in ["a", "b"]:
                    self.assertEqual(pair["response_" + side], responses[mapping[pair_id]["assignment"][side]][mapping[pair_id]["task_id"]])
            rater = layout["rater"]
            self.assertEqual(hashlib.sha256(rater["raw_content"].encode()).hexdigest(), rater["raw_sha256"])
            data = json.loads(rater["raw_content"])
            self.assertEqual(data["anonymous_file_sha256"], layout["anonymous_file_sha256"])
            self.assertEqual({r["pair_id"] for r in data["ratings"]}, set(pairs))
            self.assertEqual(len(data["ratings"]), 4)
            for rating in data["ratings"]:
                assignment = mapping[rating["pair_id"]]["assignment"]
                votes["tie" if rating["preferred"] == "tie" else assignment[rating["preferred"]]] += 1
                for side in ["a", "b"]:
                    result = rating["scores_by_side"][side]
                    scores[assignment[side]].append(statistics.mean(result["scores"].values()))
                    if result["critical_errors"]:
                        flags[assignment[side]].append([data["rater_id"], rating["pair_id"], result["critical_errors"]])
        for pair_id in maps[0]:
            self.assertEqual(maps[0][pair_id]["assignment"]["a"], maps[1][pair_id]["assignment"]["b"])
        self.assertEqual(votes, stage["summary"]["preference_votes"])
        for condition in scores:
            self.assertAlmostEqual(statistics.mean(scores[condition]), stage["summary"]["mean_six_dimension_score"][condition])
            self.assertEqual(flags[condition], stage["summary"]["flagged_responses"][condition])

    def test_real_numeric_constraints_are_preserved_without_gold_prose(self):
        tasks = {t["task_id"]: t for t in self.packet["tasks"]}
        diffusion_one = next(r for r in tasks["T01"]["rows"] if r[0] == "diffusion" and r[1] == 1)
        self.assertEqual(diffusion_one[-1], 0.0)
        self.assertIsNone(tasks["T02"]["rows"][0][-1])
        oa, memory, _ = tasks["T03"]["rows"]
        self.assertLess(oa[1], memory[1])
        self.assertLess(oa[2], memory[2])
        baseline, candidate = tasks["T04"]["rows"]
        margins = [Decimal(str(y)) - Decimal(str(x)) for x, y in zip(baseline[1:], candidate[1:])]
        self.assertEqual(margins, list(map(Decimal, ["1.55", "2.03", "1.66", "1.38"])))
        self.assertNotEqual(margins, sorted(margins))
        self.assertTrue(all(x > y for x, y in zip(candidate[1:-1], candidate[2:])))


if __name__ == "__main__":
    unittest.main()
