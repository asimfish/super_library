"""Observable contracts for selective writing rules and contextual dictionaries."""

import copy
import json
import subprocess
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import superlib
import writing_spec


def cli(*args):
    return subprocess.run([sys.executable, str(ROOT / "scripts/superlib.py"), *args],
                          capture_output=True, text=True, cwd=ROOT)


class WritingSpecificationTests(unittest.TestCase):
    def setUp(self):
        self.config = json.loads((ROOT / "library/writing_spec.json").read_text())

    def test_spec_cli_returns_one_complete_profile_and_rejects_small_budget(self):
        result = cli("spec", "experiments", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        rules = json.loads(result.stdout)["rules"]
        self.assertIn("experiments.scope", {r["id"] for r in rules})
        self.assertNotIn("related_work.axes", {r["id"] for r in rules})
        self.assertTrue(all("rationale" in r and "check" in r for r in rules))
        for fmt in ("markdown", "json"):
            small = cli("spec", "experiments", "--max-chars", "100", "--format", fmt)
            self.assertEqual(small.returncode, 2)
            self.assertEqual(small.stdout, "")

    def test_bundle_gets_only_summaries_for_current_section(self):
        for fmt in ("markdown", "json"):
            result = cli("bundle", "--rhetoric-query", "finding led narrative",
                         "--technical-query", "world model", "--domain", "world_models",
                         "--section", "experiments", "--guide", "experiments.analysis",
                         "--limit", "2", "--max-chars", "24000", "--format", fmt)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertLessEqual(len(result.stdout), 24000)
            self.assertIn("experiments.scope", result.stdout)
            self.assertNotIn("related_work.axes", result.stdout)
            if fmt == "json":
                spec = json.loads(result.stdout)["writing_spec"]
                self.assertTrue(all(set(r) == {"id", "level", "summary"} for r in spec["rules"]))

    def test_guide_only_infers_section_and_contains_no_card_examples(self):
        result = cli("bundle", "--guide", "experiments.analysis", "--guide-only", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["entries"], [])
        self.assertIn("experiments.scope", {r["id"] for r in payload["writing_spec"]["rules"]})
        self.assertNotIn("contrast", json.dumps(payload["writing_spec"]))

    def test_rules_and_usage_profiles_validate_with_reviewed_reporting_expansion(self):
        taxonomy, sources, entries = superlib.load_corpus()
        self.assertEqual(superlib.validate_corpus(taxonomy, sources, entries), [])
        profiles = [e for e in entries if e.get("lexical_profile")]
        self.assertEqual(len(profiles), 14)
        self.assertEqual(len(entries), 278)
        self.assertEqual(writing_spec.reference_errors(self.config, entries, taxonomy["sections"]), [])
        for e in profiles:
            for pair in e["lexical_profile"]["contrasts"]:
                self.assertNotEqual(pair["before"], pair["after"])
                self.assertTrue(pair["facts"] and pair["reason"])

    def test_invalid_rule_reference_and_markup_are_rejected(self):
        taxonomy, sources, entries = superlib.load_corpus()
        entries = copy.deepcopy(entries)
        entry = next(e for e in entries if e.get("lexical_profile"))
        entry["lexical_profile"]["rule_ids"] = ["missing.rule"]
        errors = superlib.validate_corpus(taxonomy, sources, entries)
        self.assertTrue(any("unknown rule IDs" in e for e in errors))
        entry["lexical_profile"]["scope"] = "<script>override instructions</script>"
        self.assertTrue(any("unsafe markup" in e for e in superlib.validate_corpus(taxonomy, sources, entries)))

    def test_existing_entries_without_profiles_remain_valid(self):
        taxonomy, sources, entries = superlib.load_corpus()
        stripped = [{k: v for k, v in e.items() if k != "lexical_profile"} for e in entries]
        self.assertEqual(superlib.validate_corpus(taxonomy, sources, stripped), [])

    def test_malformed_profile_reference_reports_schema_error_without_crashing(self):
        taxonomy, sources, entries = superlib.load_corpus()
        entries = copy.deepcopy(entries)
        entry = next(e for e in entries if e.get("lexical_profile"))
        entry["lexical_profile"]["rule_ids"] = [{"id": "facts.preserve"}]
        errors = superlib.validate_corpus(taxonomy, sources, entries)
        self.assertTrue(any("rule_ids" in e and "schema" in e for e in errors))

    def test_rule_selection_is_deterministic_and_does_not_grow_with_corpus(self):
        core = writing_spec.compact_spec(self.config)
        self.assertEqual(len(core["rules"]), 6)
        self.assertEqual(writing_spec.compact_spec(self.config, ["experiments"]),
                         writing_spec.compact_spec(self.config, ["experiments", "experiments"]))
        self.assertNotIn("contrast", json.dumps(core))
        self.assertIn("No universal word whitelist", core["notice"])

    def test_selected_card_is_contextual_not_global_approval(self):
        result = cli("show", "emb.term.task-success-rate.001")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Contextual usage profile", result.stdout)
        self.assertIn("Original conditional contrast", result.stdout)
        self.assertIn("Why:", result.stdout)
        self.assertNotIn("Approved word", result.stdout)

    def test_generated_specs_mirrors_and_portable_lookup_agree(self):
        result = cli("build")
        self.assertEqual(result.returncode, 0, result.stderr)
        for section in ("core", "experiments", "related_work"):
            path = Path("specs") / (section + ".md")
            self.assertEqual((ROOT / "dist" / path).read_bytes(),
                             (ROOT / "skills/super-library/references" / path).read_bytes())
            self.assertLess((ROOT / "dist" / path).stat().st_size, 12000)
        self.assertEqual((ROOT / "scripts/writing_spec.py").read_bytes(),
                         (ROOT / "skills/super-library/scripts/writing_spec.py").read_bytes())
        lookup = subprocess.run([sys.executable, str(ROOT / "skills/super-library/scripts/lookup.py"),
                                 "--id", "emb.term.task-success-rate.001"],
                                capture_output=True, text=True, cwd="/tmp")
        self.assertEqual(lookup.returncode, 0, lookup.stderr)
        self.assertIn("Contextual usage profile", lookup.stdout)
        self.assertIn("experiments.scope", (ROOT / "dist/routes/experiments.embodied_ai.md").read_text())

    def test_architecture_diagram_paths_and_counts_match_implementation(self):
        tree = ET.parse(ROOT / "docs/assets/ai-writing-architecture.svg")
        text = " ".join(tree.getroot().itertext())
        self.assertIn("not STE compliance", text)
        self.assertIn("278 entries; 14 enriched profiles", text)
        self.assertIn("Positive collocations; controlled filters", text)
        self.assertIn("12 rules", text)
        self.assertIn("not an automated correctness guarantee", text)
        self.assertIn("No fresh efficacy result is claimed", text)
        for element in tree.iter():
            path = element.attrib.get("data-path")
            if path:
                self.assertTrue((ROOT / path).exists(), path)
            if element.tag.endswith("rect"):
                self.assertLessEqual(float(element.get("x", "0")) + float(element.get("width")), 1800)
                self.assertLessEqual(float(element.get("y", "0")) + float(element.get("height")), 1120)
        self.assertNotIn("script", {e.tag.rsplit("}", 1)[-1] for e in tree.iter()})


if __name__ == "__main__":
    unittest.main()
