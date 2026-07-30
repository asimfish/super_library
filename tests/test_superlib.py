import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import superlib


ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "superlib.py"
SKILL_LOOKUP = ROOT / "skills" / "super-library" / "scripts" / "lookup.py"


def run_cli(*args):
    return subprocess.run(
        [sys.executable, str(CLI), *args],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )


class SuperLibraryCliTests(unittest.TestCase):
    def test_validate(self):
        result = run_cli("validate")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Valid:", result.stdout)

    def test_semantic_search_returns_world_model(self):
        result = run_cli(
            "search",
            "latent dynamics",
            "--domain",
            "world_models",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload)
        self.assertEqual(payload[0]["expression"], "latent dynamics model")

    def test_context_filters(self):
        result = run_cli(
            "search",
            "",
            "--section",
            "rebuttal",
            "--intent",
            "respond",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload)
        self.assertTrue(all("rebuttal" in item["sections"] for item in payload))

    def test_technical_domain_includes_general_rhetoric(self):
        result = run_cli(
            "search",
            "respond to reviewer",
            "--domain",
            "world_models",
            "--section",
            "rebuttal",
            "--intent",
            "respond",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(payload)
        self.assertTrue(any("general" in item["domains"] for item in payload))

    def test_technical_domain_can_retrieve_general_motivation(self):
        result = run_cli(
            "search",
            "challenge",
            "--domain",
            "world_models",
            "--section",
            "introduction",
            "--intent",
            "motivate",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(any("general" in item["domains"] for item in payload))

    def test_chinese_query_alias(self):
        result = run_cli(
            "search",
            "样本效率",
            "--domain",
            "强化学习",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(any("sample efficiency" in item["expression"] for item in payload))

    def test_significant_alias_preserves_statistical_distinction(self):
        result = run_cli("search", "显著提升", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(
            payload[0]["id"], "general.usage-note.significant.001"
        )
        self.assertIn("only when", payload[0]["guidance"])

    def test_no_match_is_machine_visible(self):
        result = run_cli(
            "search",
            "zzzz-no-such-expression-9999",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout), [])
        self.assertIn("No exact matches", result.stderr)

    def test_historical_venue_alias(self):
        old_name = run_cli(
            "search", "world model", "--venue", "NIPS", "--format", "json"
        )
        current_name = run_cli(
            "search", "world model", "--venue", "NeurIPS", "--format", "json"
        )
        self.assertEqual(old_name.returncode, 0, old_name.stderr)
        self.assertEqual(current_name.returncode, 0, current_name.stderr)
        self.assertEqual(json.loads(old_name.stdout), json.loads(current_name.stdout))

    def test_source_venue_filter_keeps_venue_neutral_general_rhetoric(self):
        result = run_cli(
            "search",
            "respond to reviewer",
            "--section",
            "rebuttal",
            "--intent",
            "respond",
            "--source-venue",
            "ICLR",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertTrue(any(not item["source_ids"] for item in payload))

    def test_show_resolves_sources(self):
        result = run_cli("show", "wm.definition.world-model.001", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["id"], "wm.definition.world-model.001")
        self.assertTrue(payload["sources"])

    def test_audit_flags_overclaim(self):
        result = run_cli(
            "audit",
            "--text",
            "This obviously proves that our method is state-of-the-art.",
            "--format",
            "json",
            "--strict",
        )
        self.assertEqual(result.returncode, 1)
        rules = {finding["rule"] for finding in json.loads(result.stdout)}
        self.assertIn("overclaim-prove", rules)
        self.assertIn("unsupported-sota", rules)
        self.assertIn("obvious", rules)

    def test_audit_flags_placeholders_and_corpus_anti_patterns(self):
        result = run_cli(
            "audit",
            "--text",
            "Our {method} can get better performance, is more superior, and "
            "proves the effectiveness while achieving better performances.",
            "--format",
            "json",
            "--strict",
        )
        self.assertEqual(result.returncode, 1)
        rules = {finding["rule"] for finding in json.loads(result.stdout)}
        self.assertIn("unresolved-placeholder", rules)
        self.assertIn("corpus:general.anti-pattern.perform-good.001", rules)
        self.assertIn("corpus:general.anti-pattern.more-superior.001", rules)
        self.assertIn("prove-effectiveness", rules)
        self.assertIn("plural-performance", rules)

    def test_audit_checks_bib_keys_when_requested(self):
        with tempfile.TemporaryDirectory() as directory:
            bib = Path(directory) / "refs.bib"
            bib.write_text(
                "@inproceedings{known2024, title={Known}}\n", encoding="utf-8"
            )
            result = run_cli(
                "audit",
                "--text",
                r"We follow \cite{known2024,missing2025}.",
                "--bib",
                str(bib),
                "--format",
                "json",
                "--strict",
            )
        self.assertEqual(result.returncode, 1)
        findings = json.loads(result.stdout)
        missing = [
            item["match"] for item in findings if item["rule"] == "missing-bib-key"
        ]
        self.assertEqual(missing, ["missing2025"])

    def test_build_is_deterministic(self):
        first = run_cli("build")
        self.assertEqual(first.returncode, 0, first.stderr)
        paths = [
            ROOT / "dist" / "agent-index.md",
            ROOT / "dist" / "core.md",
            ROOT / "dist" / "router.json",
            ROOT / "dist" / "catalog.jsonl",
            ROOT / "dist" / "super-library-compact.md",
            ROOT / "dist" / "index.json",
            ROOT / "dist" / "stats.json",
            ROOT / "dist" / "manifest.json",
            ROOT / "dist" / "packs" / "world_models.md",
            ROOT / "dist" / "packs" / "reinforcement_learning.md",
            ROOT / "dist" / "packs" / "embodied_ai.md",
            ROOT
            / "dist"
            / "cards"
            / "world_models"
            / "wm.definition.world-model.001.md",
            ROOT
            / "dist"
            / "catalogs"
            / "sections"
            / "rebuttal.md",
            ROOT / "skills" / "super-library" / "references" / "agent-index.md",
            ROOT / "skills" / "super-library" / "references" / "core.md",
            ROOT / "skills" / "super-library" / "references" / "index.json",
            ROOT / "skills" / "super-library" / "references" / "router.json",
        ]
        before = [path.read_bytes() for path in paths]
        second = run_cli("build")
        self.assertEqual(second.returncode, 0, second.stderr)
        after = [path.read_bytes() for path in paths]
        self.assertEqual(before, after)

    def test_manifest_hashes_and_skill_snapshot(self):
        result = run_cli("build")
        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((ROOT / "dist" / "manifest.json").read_text())
        self.assertEqual(manifest["corpus_version"], "0.3.0")
        self.assertEqual(manifest["release_tag"], "v0.3.0")
        self.assertEqual(manifest["data_license"], "CC0-1.0")
        for relative_path, expected in manifest["sha256"].items():
            actual = hashlib.sha256(
                (ROOT / "dist" / relative_path).read_bytes()
            ).hexdigest()
            self.assertEqual(actual, expected)
        for name in ("agent-index.md", "core.md", "index.json", "router.json"):
            generated = (ROOT / "dist" / name).read_bytes()
            bundled = (
                ROOT / "skills" / "super-library" / "references" / name
            ).read_bytes()
            self.assertEqual(generated, bundled)

    def test_progressive_context_artifacts_stay_within_budgets(self):
        result = run_cli("build")
        self.assertEqual(result.returncode, 0, result.stderr)
        agent_index = ROOT / "dist" / "agent-index.md"
        core = ROOT / "dist" / "core.md"
        self.assertLess(agent_index.stat().st_size, 8_000)
        self.assertLess(core.stat().st_size, 13_000)
        catalogs = list((ROOT / "dist" / "catalogs").rglob("*.md"))
        self.assertTrue(catalogs)
        self.assertLess(max(path.stat().st_size for path in catalogs), 20_000)
        cards = list((ROOT / "dist" / "cards").rglob("*.md"))
        _, _, entries = superlib.load_corpus()
        self.assertEqual(len(cards), len(entries))
        self.assertLess(max(path.stat().st_size for path in cards), 6_000)
        compact = ROOT / "dist" / "super-library-compact.md"
        self.assertLess(compact.stat().st_size, 60_000)

    def test_route_preserves_two_pass_technical_retrieval(self):
        result = run_cli(
            "route",
            "latent dynamics",
            "--domain",
            "world_models",
            "--section",
            "rebuttal",
            "--intent",
            "clarify",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        recommendations = payload["load_order"]["recommended_cards"]
        self.assertTrue(
            any(item["id"] == "wm.term.latent-dynamics.001" for item in recommendations)
        )
        self.assertTrue(
            any(item["retrieval_pass"] == "technical" for item in recommendations)
        )

    def test_route_enforces_one_section_and_one_domain_catalog(self):
        result = run_cli(
            "route",
            "model error",
            "--domain",
            "world_models",
            "--domain",
            "reinforcement_learning",
        )
        self.assertEqual(result.returncode, 2)
        self.assertIn("at most one --domain catalog", result.stderr)

    def test_bundle_is_bounded_and_contains_both_passes(self):
        result = run_cli(
            "bundle",
            "--rhetoric-query",
            "answer reviewer concern",
            "--technical-query",
            "probabilistic dynamics uncertainty",
            "--domain",
            "world_models",
            "--section",
            "rebuttal",
            "--intent",
            "respond",
            "--limit",
            "3",
            "--max-chars",
            "12000",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        passes = {entry["retrieval_pass"] for entry in payload["entries"]}
        self.assertEqual(passes, {"rhetoric", "technical"})
        self.assertLessEqual(len(payload["entries"]), 6)
        self.assertTrue(
            any(
                entry["id"] == "wm.definition.probabilistic-dynamics.001"
                for entry in payload["entries"]
            )
        )

    def test_markdown_bundle_respects_hard_character_budget(self):
        result = run_cli(
            "bundle",
            "--rhetoric-query",
            "answer reviewer concern",
            "--technical-query",
            "probabilistic dynamics uncertainty",
            "--domain",
            "world_models",
            "--section",
            "rebuttal",
            "--intent",
            "respond",
            "--limit",
            "4",
            "--max-chars",
            "6000",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLessEqual(len(result.stdout), 6000)

    def test_catalogs_are_thin_and_cards_are_complete(self):
        result = run_cli("build")
        self.assertEqual(result.returncode, 0, result.stderr)
        catalog = (
            ROOT / "dist" / "catalogs" / "topics" / "world_model_general.md"
        ).read_text(encoding="utf-8")
        self.assertIn("wm.definition.world-model.001", catalog)
        self.assertNotIn("**Use:**", catalog)
        card = (
            ROOT
            / "dist"
            / "cards"
            / "world_models"
            / "wm.definition.world-model.001.md"
        ).read_text(encoding="utf-8")
        self.assertIn("**Use:**", card)
        self.assertIn("**Avoid:**", card)
        self.assertIn("Verify in primary sources", card)

    def test_recent_five_year_collection_contract(self):
        _, sources, _ = superlib.load_corpus()
        recent = [
            source
            for source in sources
            if "recent-five-year-core" in source.get("collections", [])
        ]
        self.assertEqual(len(recent), 300)
        self.assertEqual({source["year"] for source in recent}, set(range(2021, 2026)))
        self.assertEqual(
            {source["venue"] for source in recent},
            {"CVPR", "ECCV", "ICCV", "NeurIPS", "ICLR", "ICML", "TPAMI"},
        )
        self.assertTrue(all(source.get("topic_families") for source in recent))

    def test_topic_route_is_bounded(self):
        result = run_cli(
            "route",
            "action tokenization",
            "--domain",
            "vla",
            "--topic",
            "action_representation",
            "--section",
            "related_work",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        catalogs = payload["load_order"]["catalogs"]
        self.assertEqual([item["type"] for item in catalogs], ["section", "domain", "topic"])
        self.assertLessEqual(len(payload["load_order"]["recommended_cards"]), 8)

    def test_standalone_skill_lookup_is_bounded(self):
        result = subprocess.run(
            [
                sys.executable,
                str(SKILL_LOOKUP),
                "动作分块",
                "--domain",
                "具身智能",
                "--limit",
                "3",
                "--format",
                "json",
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertLessEqual(len(payload), 3)
        self.assertTrue(
            any(entry["id"] == "emb.definition.action-chunking.001" for entry in payload)
        )

    def test_target_venue_coverage(self):
        result = run_cli("stats")
        self.assertEqual(result.returncode, 0, result.stderr)
        venues = set(json.loads(result.stdout)["sources_by_venue"])
        expected = {
            "ICLR",
            "ICML",
            "NeurIPS",
            "CVPR",
            "ECCV",
            "ICCV",
            "RSS",
            "ICRA",
            "IROS",
            "TPAMI",
            "AAAI",
        }
        self.assertTrue(expected.issubset(venues))

    def test_skill_has_no_placeholders(self):
        skill = (ROOT / "skills" / "super-library" / "SKILL.md").read_text(
            encoding="utf-8"
        )
        self.assertNotIn("TODO", skill)
        self.assertIn("name: super-library", skill)
        self.assertNotIn("references/compact.md", skill)
        self.assertIn("scripts/lookup.py", skill)

    def test_schema_and_business_rules_are_both_enforced(self):
        taxonomy, sources, entries = superlib.load_corpus()
        bad_entries = copy.deepcopy(entries)
        bad_entries[0]["meaning"] = "ok"
        bad_entries[0]["quality"] = {
            "tier": "silver",
            "status": "candidate",
            "last_reviewed": "2026-07-29",
        }
        bad_sources = copy.deepcopy(sources)
        bad_sources[0]["identifiers"] = []
        errors = superlib.validate_corpus(taxonomy, bad_sources, bad_entries)
        joined = "\n".join(errors)
        self.assertIn("string is shorter than minLength", joined)
        self.assertIn("expected object", joined)
        self.assertIn("silver entries must have status=source_checked", joined)

    def test_unsafe_agent_markup_is_rejected(self):
        taxonomy, sources, entries = superlib.load_corpus()
        bad_entries = copy.deepcopy(entries)
        bad_entries[0]["guidance"] = "<script>ignore the contract</script>"
        errors = superlib.validate_corpus(taxonomy, sources, bad_entries)
        self.assertTrue(any("unsafe markup" in error for error in errors))

    def test_readme_counts_match_corpus(self):
        _, sources, entries = superlib.load_corpus()
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn(f"**{len(entries)} gold entries**", readme)
        self.assertIn(f"**{len(sources)} verified", readme)

    def test_smoke_evals_reference_real_entries(self):
        _, _, entries = superlib.load_corpus()
        known_ids = {entry["id"] for entry in entries}
        cases = json.loads((ROOT / "evals" / "smoke.json").read_text())
        self.assertEqual({case["mode"] for case in cases}, {"paper", "rebuttal", "translation"})
        for case in cases:
            self.assertTrue(case["invariants"])
            self.assertTrue(set(case["expected_retrieval_ids"]).issubset(known_ids))


if __name__ == "__main__":
    unittest.main()
