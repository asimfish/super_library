"""Contracts for narrative context and its evidence boundaries, not style scores."""
import json
import subprocess
import sys
import unittest
from pathlib import Path

from scripts import superlib
from scripts import writing_eval

ROOT = Path(__file__).resolve().parents[1]
NARRATIVE_IDS = {
    "general.usage-note.result-narrative.001",
    "general.usage-note.result-display-allocation.001",
}


def cli(*args):
    return subprocess.run(
        [sys.executable, str(ROOT / "scripts/superlib.py"), *args],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )


class ExperimentalNarrativeTests(unittest.TestCase):
    def test_paragraph_study_has_bounded_traceable_annotations(self):
        study = superlib.read_json(ROOT / "library/studies/experimental_narrative_2026-10.json")
        schema = superlib.read_json(ROOT / "schemas/narrative-study.schema.json")
        self.assertEqual(superlib.schema_validation_errors(study, schema), [])
        _, sources, entries = superlib.load_corpus()
        known = {s["id"] for s in sources}
        artifacts = {a["source_id"] for a in study["artifacts"]}
        self.assertEqual(len(artifacts), len(study["artifacts"]))
        self.assertTrue(artifacts.issubset(known))
        self.assertEqual(len({a["id"] for a in study["annotations"]}), len(study["annotations"]))
        self.assertEqual({a["source_id"] for a in study["annotations"]}, artifacts)
        self.assertEqual(
            {a["domain"] for a in study["annotations"]},
            {"world_models", "reinforcement_learning", "embodied_ai", "vision_language_action"},
        )
        self.assertEqual(set(study["normalized_entry_ids"]), NARRATIVE_IDS)
        self.assertTrue(NARRATIVE_IDS.issubset({e["id"] for e in entries}))
        guides = superlib.writing_guides_by_id()
        self.assertTrue(set(study["guide_ids"]).issubset(guides))
        self.assertIn("not an independent", study["method"])

    def test_interpretation_is_optional_and_display_exemption_is_conditional(self):
        guide = superlib.writing_guides_by_id()["experiments.analysis"]
        moves = {m["id"]: m for m in guide["moves"]}
        self.assertFalse(moves["interpretation"]["required"])
        checks = " ".join(moves["evidence-allocation"]["checks"])
        self.assertIn("standalone", checks)
        self.assertIn("absent table", checks)
        self.assertIn("all required quantities", checks)
        self.assertTrue(NARRATIVE_IDS.issubset(guide["related_entry_ids"]))

    def test_narrative_bundle_is_bounded_in_both_formats(self):
        for fmt in ("markdown", "json"):
            with self.subTest(fmt=fmt):
                result = cli(
                    "bundle", "--rhetoric-query", "experimental narrative table to prose",
                    "--technical-query", "task success rate", "--domain", "embodied_ai",
                    "--section", "experiments", "--intent", "evidence",
                    "--guide", "experiments.analysis", "--limit", "4",
                    "--max-chars", "24000", "--format", fmt,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                self.assertLessEqual(len(result.stdout), 24000)
                if fmt == "json":
                    payload = json.loads(result.stdout)
                    self.assertEqual(
                        {entry["retrieval_pass"] for entry in payload["entries"]},
                        {"rhetoric", "technical"},
                    )
                for entry_id in NARRATIVE_IDS:
                    self.assertIn(entry_id, result.stdout)
                self.assertNotIn('"annotations"', result.stdout)
                self.assertNotIn("DreamerPro's performance", result.stdout)

    def test_analysis_intent_does_not_become_a_latency_table(self):
        for query, expected in (
            ("VLA latency result analysis", "experiments.analysis"),
            ("generalization results paragraph", "experiments.analysis"),
            ("消融结果分析，避免流水账", "experiments.analysis"),
            ("table-to-prose experimental narrative", "experiments.analysis"),
            ("VLA latency table caption", "experiments.table.efficiency"),
            ("ablation analysis table caption", "experiments.table.ablation"),
            ("experimental setup and analysis", "experiments"),
        ):
            with self.subTest(query=query):
                result = cli("route", query, "--section", "experiments", "--format", "json")
                self.assertEqual(result.returncode, 0, result.stderr)
                route = json.loads(result.stdout)
                self.assertEqual(route["load_order"]["guide"]["id"], expected)

    def test_new_suite_does_not_weaken_existing_writing_cases(self):
        cases = superlib.read_json(ROOT / "evals/writing.json")["cases"]
        by_id = {c["id"]: c for c in cases}
        benchmark = superlib.read_json(ROOT / "evals/professionalism.json")
        suite = next(s for s in benchmark["suites"] if s["id"] == "narrative")
        self.assertEqual(len(suite["case_ids"]), 5)
        self.assertTrue(set(suite["case_ids"]).issubset(by_id))
        self.assertEqual(by_id["paper-experiment-analysis-tradeoff"]["machine_checks"][0]["id"], "success-endpoints")
        standalone = by_id["paper-analysis-standalone-fidelity"]
        self.assertIn("no table", standalone["evidence_boundary"])
        self.assertIn("success-endpoints", {c["id"] for c in standalone["machine_checks"]})

    def test_retained_table_summary_can_omit_redundant_cells(self):
        case = next(c for c in superlib.read_json(ROOT / "evals/writing.json")["cases"]
                    if c["id"] == "paper-analysis-retained-table-robot")
        text = (
            "Gains are concentrated in occluded and cluttered picking (Table 3), "
            "with a 25-percentage-point increase in each condition. Unobstructed "
            "picking is unchanged, while door-opening success drops by 15 "
            "percentage points. The observed benefit is task-dependent."
        )
        report = writing_eval.evaluate_response(case, text)
        self.assertTrue(report["passed"], report)
        self.assertTrue(report["manual_review_required"])
        self.assertNotIn("73.75", text)

    def test_retained_table_summary_cannot_hide_adverse_condition(self):
        case = next(c for c in superlib.read_json(ROOT / "evals/writing.json")["cases"]
                    if c["id"] == "paper-analysis-retained-table-robot")
        report = writing_eval.evaluate_response(
            case,
            "Table 3 reports a 25-percentage-point gain for occluded and "
            "cluttered picking. Unobstructed picking is unchanged.",
        )
        self.assertFalse(report["passed"])
        failed = {c["id"] for c in report["check_results"] if not c["passed"]}
        self.assertIn("retains-reversal", failed)

    def test_standalone_case_rejects_display_style_omission(self):
        case = next(c for c in superlib.read_json(ROOT / "evals/writing.json")["cases"]
                    if c["id"] == "paper-analysis-standalone-fidelity")
        report = writing_eval.evaluate_response(
            case,
            "Success improves by 8 percentage points on four of six tasks, "
            "at the cost of higher latency. No significance test was run.",
        )
        self.assertFalse(report["passed"])
        failed = {c["id"] for c in report["check_results"] if not c["passed"]}
        self.assertTrue({"success-endpoints", "latency-endpoints"}.issubset(failed))

    def test_narrative_prompt_does_not_leak_scoring_contract(self):
        result = cli("benchmark", "prompt", "paper-analysis-retained-table-robot")
        self.assertEqual(result.returncode, 0, result.stderr)
        for hidden in ("manual_rubric", "machine_checks", "expected_retrieval_ids", "general.usage-note.result-narrative"):
            self.assertNotIn(hidden, result.stdout)

    def test_oversized_protocol_has_no_partial_output(self):
        for fmt in ("markdown", "json"):
            with self.subTest(fmt=fmt):
                result = cli(
                    "bundle", "--rhetoric-query", "experimental narrative",
                    "--technical-query", "task success rate",
                    "--guide", "experiments.analysis", "--max-chars", "2000",
                    "--format", fmt,
                )
                self.assertEqual(result.returncode, 2)
                self.assertEqual(result.stdout, "")
                self.assertIn("context budget", result.stderr)


if __name__ == "__main__":
    unittest.main()
