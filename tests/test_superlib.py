import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from scripts import superlib
from scripts import source_health


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

    def test_chinese_introduction_query_routes_protocol_and_cards(self):
        result = run_cli(
            "route",
            "引言中把局限和设计贡献对齐",
            "--domain",
            "vla",
            "--section",
            "introduction",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["load_order"]["guide"]["id"], "introduction")
        ids = {
            item["id"] for item in payload["load_order"]["recommended_cards"]
        }
        self.assertIn("general.sentence-pattern.intro-challenge-design.001", ids)

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

    def test_audit_flags_ambiguous_experimental_reporting(self):
        result = run_cli(
            "audit",
            "--text",
            "Extensive experiments demonstrate that accuracy improves by 10%. "
            "Results are averaged over multiple seeds.",
            "--format",
            "json",
            "--strict",
        )
        self.assertEqual(result.returncode, 1)
        rules = {finding["rule"] for finding in json.loads(result.stdout)}
        self.assertIn("extensive-experiments", rules)
        self.assertIn("ambiguous-percent-improvement", rules)
        self.assertIn("unspecified-multiple-runs", rules)

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
            ROOT / "dist" / "guides" / "index.md",
            ROOT / "dist" / "guides" / "experiments.md",
            ROOT / "dist" / "guides" / "experiments.table.ablation.md",
            ROOT / "dist" / "routes" / "experiments.world_models.md",
            ROOT / "dist" / "routes" / "index.md",
            ROOT / "dist" / "templates" / "tables" / "main_results.tex",
            ROOT / "dist" / "catalog.jsonl",
            ROOT / "dist" / "super-library-compact.md",
            ROOT / "dist" / "index.json",
            ROOT / "dist" / "stats.json",
            ROOT / "dist" / "evidence" / "source-analysis.md",
            ROOT / "dist" / "evidence" / "source-analysis.jsonl",
            ROOT / "dist" / "evidence" / "promotion-queue.md",
            ROOT / "dist" / "evidence" / "promotion-queue.jsonl",
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
            ROOT
            / "skills"
            / "super-library"
            / "references"
            / "guides"
            / "experiments.md",
        ]
        before = [path.read_bytes() for path in paths]
        second = run_cli("build")
        self.assertEqual(second.returncode, 0, second.stderr)
        after = [path.read_bytes() for path in paths]
        self.assertEqual(before, after)

    def test_generated_tree_pruning_preserves_expected_files(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            generated = Path(temp_dir) / "generated"
            (generated / "child").mkdir(parents=True)
            expected = generated / "child" / "artifact.txt"
            stale = generated / "child" / "artifact 2.txt"
            expected.write_text("generated")
            stale.write_text("cloud conflict")
            superlib.prune_generated_tree(generated, {"child/artifact.txt"})
            self.assertEqual(expected.read_text(), "generated")
            self.assertFalse(stale.exists())
            self.assertTrue(generated.exists())

    def test_manifest_hashes_and_skill_snapshot(self):
        result = run_cli("build")
        self.assertEqual(result.returncode, 0, result.stderr)
        manifest = json.loads((ROOT / "dist" / "manifest.json").read_text())
        self.assertEqual(manifest["corpus_version"], "0.4.0")
        self.assertEqual(manifest["release_tag"], "v0.4.0")
        self.assertEqual(manifest["data_license"], "CC0-1.0")
        router = json.loads((ROOT / "dist" / "router.json").read_text())
        self.assertEqual(
            router["evidence"]["source_analysis_records"],
            "evidence/source-analysis.jsonl",
        )
        self.assertEqual(
            manifest["source_analysis"]["records"],
            "evidence/source-analysis.jsonl",
        )
        self.assertEqual(
            router["evidence"]["promotion_decisions_records"],
            "evidence/promotion-decisions.jsonl",
        )
        self.assertEqual(
            manifest["promotion_decisions"]["records"],
            "evidence/promotion-decisions.jsonl",
        )
        self.assertEqual(
            router["evidence"]["promotion_queue_records"],
            "evidence/promotion-queue.jsonl",
        )
        self.assertEqual(
            manifest["promotion_queue"]["records"],
            "evidence/promotion-queue.jsonl",
        )
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
        for generated_path in (ROOT / "dist" / "guides").glob("*.md"):
            bundled_path = (
                ROOT
                / "skills"
                / "super-library"
                / "references"
                / "guides"
                / generated_path.name
            )
            self.assertEqual(generated_path.read_bytes(), bundled_path.read_bytes())
        for generated_path in (ROOT / "dist" / "routes").glob("*.md"):
            bundled_path = (
                ROOT
                / "skills"
                / "super-library"
                / "references"
                / "routes"
                / generated_path.name
            )
            self.assertEqual(generated_path.read_bytes(), bundled_path.read_bytes())
        for source_path in (ROOT / "templates" / "tables").glob("*.tex"):
            bundled_path = (
                ROOT
                / "skills"
                / "super-library"
                / "assets"
                / "tables"
                / source_path.name
            )
            self.assertEqual(source_path.read_bytes(), bundled_path.read_bytes())

    def test_progressive_context_artifacts_stay_within_budgets(self):
        result = run_cli("build")
        self.assertEqual(result.returncode, 0, result.stderr)
        agent_index = ROOT / "dist" / "agent-index.md"
        core = ROOT / "dist" / "core.md"
        self.assertLess(agent_index.stat().st_size, 8_000)
        self.assertLess(core.stat().st_size, 13_000)
        guide_index = ROOT / "dist" / "guides" / "index.md"
        self.assertLess(guide_index.stat().st_size, 5_000)
        guides = [
            path
            for path in (ROOT / "dist" / "guides").glob("*.md")
            if path.name != "index.md"
        ]
        self.assertEqual(len(guides), 16)
        self.assertLess(max(path.stat().st_size for path in guides), 12_000)
        routes = [
            path
            for path in (ROOT / "dist" / "routes").glob("*.md")
            if path.name != "index.md"
        ]
        self.assertEqual(len(routes), 18)
        self.assertLess(max(path.stat().st_size for path in routes), 24_000)
        self.assertLess(
            (ROOT / "dist" / "routes" / "index.md").stat().st_size,
            6_000,
        )
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

    def test_route_recommends_one_specialized_experiment_guide(self):
        result = run_cli(
            "route",
            "ablation table for coupled components",
            "--domain",
            "world_models",
            "--section",
            "experiments",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(
            payload["load_order"]["guide"]["id"],
            "experiments.table.ablation",
        )
        self.assertIsNone(payload["load_order"]["task_pack"])

    def test_explicit_main_results_table_outranks_secondary_latency_signal(self):
        result = run_cli(
            "route",
            "main results table caption with success rate and A100 latency",
            "--domain",
            "world_models",
            "--section",
            "experiments",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(
            payload["load_order"]["guide"]["id"],
            "experiments.table.main_results",
        )

    def test_route_prefers_one_file_task_pack_for_common_task(self):
        result = run_cli(
            "route",
            "world model experiments",
            "--domain",
            "world_models",
            "--section",
            "experiments",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(
            payload["load_order"]["task_pack"]["id"],
            "experiments.world_models",
        )

    def test_mixed_real_robot_experiment_routes_to_complete_protocol(self):
        result = run_cli(
            "route",
            "真实机器人实验设置与结果分析",
            "--domain",
            "embodied_ai",
            "--section",
            "experiments",
            "--intent",
            "evidence",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["load_order"]["guide"]["id"], "experiments")
        self.assertEqual(
            payload["load_order"]["task_pack"]["id"],
            "experiments.embodied_ai",
        )

    def test_related_work_route_embeds_related_work_protocol(self):
        result = run_cli(
            "route",
            "world model related work",
            "--domain",
            "world_models",
            "--section",
            "related_work",
            "--format",
            "json",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["load_order"]["guide"]["id"], "related_work")
        self.assertEqual(
            payload["load_order"]["task_pack"]["id"],
            "related_work.world_models",
        )

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

    def test_bundle_can_embed_exactly_one_section_protocol(self):
        result = run_cli(
            "bundle",
            "--guide",
            "experiments.analysis",
            "--rhetoric-query",
            "quantify results and acknowledge exceptions",
            "--section",
            "experiments",
            "--intent",
            "evidence",
            "--limit",
            "2",
            "--max-chars",
            "12000",
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Task-specific protocol: Experimental analysis", result.stdout)
        self.assertIn("Retrieved IDs:", result.stdout)
        self.assertLessEqual(len(result.stdout), 12000)

    def test_guide_command_is_bounded_and_section_specific(self):
        listing = run_cli("guide", "--list", "--format", "json")
        self.assertEqual(listing.returncode, 0, listing.stderr)
        payload = json.loads(listing.stdout)
        self.assertEqual(len(payload), 16)
        guide = run_cli("guide", "experiments.table.efficiency")
        self.assertEqual(guide.returncode, 0, guide.stderr)
        self.assertIn("Define the resource", guide.stdout)
        self.assertIn("quality–resource trade-off", guide.stdout)
        self.assertLess(len(guide.stdout), 12_000)

    def test_main_results_guide_links_conditional_latency_reporting_card(self):
        guide = run_cli("guide", "experiments.table.main_results")
        self.assertEqual(guide.returncode, 0, guide.stderr)
        self.assertIn("general.sentence-pattern.latency-protocol.001", guide.stdout)

    def test_experiment_guide_has_four_domain_overlays(self):
        guide = run_cli("guide", "experiments")
        self.assertEqual(guide.returncode, 0, guide.stderr)
        self.assertIn("Select one domain reporting overlay", guide.stdout)
        for label in (
            "Reinforcement learning",
            "World models",
            "Embodied AI and robot learning",
            "Vision-language-action models",
        ):
            self.assertIn(label, guide.stdout)

    def test_experiment_task_route_embeds_only_matching_domain_overlay(self):
        build = run_cli("build")
        self.assertEqual(build.returncode, 0, build.stderr)
        text = (ROOT / "dist" / "routes" / "experiments.embodied_ai.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("### Embodied AI and robot learning", text)
        self.assertNotIn("### Reinforcement learning", text)
        self.assertNotIn("### World models", text)
        self.assertNotIn("### Vision-language-action models", text)
        bundle = run_cli(
            "bundle",
            "--rhetoric-query",
            "describe real-robot evaluation",
            "--technical-query",
            "task success rate",
            "--domain",
            "embodied_ai",
            "--section",
            "experiments",
            "--intent",
            "evidence",
            "--guide",
            "experiments",
        )
        self.assertEqual(bundle.returncode, 0, bundle.stderr)
        self.assertIn("### Embodied AI and robot learning", bundle.stdout)
        self.assertNotIn("### Reinforcement learning", bundle.stdout)

    def test_table_assets_are_copyable_and_auditable(self):
        listing = run_cli("template", "--list", "--format", "json")
        self.assertEqual(listing.returncode, 0, listing.stderr)
        self.assertEqual(len(json.loads(listing.stdout)), 5)
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary) / "efficiency.tex"
            copied = run_cli("template", "efficiency", "--output", str(output))
            self.assertEqual(copied.returncode, 0, copied.stderr)
            text = output.read_text(encoding="utf-8")
            self.assertIn("SL_HARDWARE", text)
            self.assertIn("\\toprule", text)
            refused = run_cli("template", "efficiency", "--output", str(output))
            self.assertEqual(refused.returncode, 2)
            audit = run_cli("audit", "--text-file", str(output), "--format", "json")
            rules = {finding["rule"] for finding in json.loads(audit.stdout)}
            self.assertEqual(rules, {"unresolved-table-token"})

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

    def test_section_writing_study_is_bounded_and_balanced(self):
        _, sources, _ = superlib.load_corpus()
        _, study = superlib.load_writing_guides()
        self.assertEqual(study["counts"]["full_papers"], 40)
        self.assertEqual(len(study["sample_source_ids"]), 40)
        self.assertEqual(
            study["counts"]["by_domain"],
            {
                "embodied_ai": 10,
                "reinforcement_learning": 10,
                "vision_language_action": 10,
                "world_models": 10,
            },
        )
        known = {source["id"] for source in sources}
        self.assertTrue(set(study["sample_source_ids"]).issubset(known))

    def test_source_analysis_ledger_is_complete_and_explicit(self):
        _, sources, entries = superlib.load_corpus()
        records = superlib.source_analysis_records(sources, entries)
        summary = superlib.source_analysis_summary(records)
        self.assertEqual(len(records), 300)
        self.assertEqual(summary["abstract_status"], {"analyzed": 288, "unavailable": 12})
        self.assertEqual(summary["full_text_status"], {"not_sampled": 260, "structural_sample": 40})
        self.assertEqual(summary["papers_with_direct_library_links"], 71)
        self.assertEqual(summary["papers_with_promotion_decisions"], 10)
        self.assertEqual(len({record["source_id"] for record in records}), 300)
        result = run_cli("analysis-status", records[0]["source_id"], "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["source_id"], records[0]["source_id"])

    def test_promotion_decisions_are_schema_valid_and_semantically_explicit(self):
        _, sources, entries = superlib.load_corpus()
        decisions = superlib.load_promotion_decisions()
        self.assertEqual(len(decisions), 10)
        self.assertEqual(
            {decision["decision"] for decision in decisions},
            {
                "link_existing_record",
                "promote_normalized_record",
                "record_no_promotion",
            },
        )
        self.assertEqual(
            superlib.validate_promotion_decisions(sources, entries, decisions), []
        )
        self.assertTrue(all(decision["dedup_entry_ids"] for decision in decisions))

        bad_decisions = copy.deepcopy(decisions)
        promoted = next(
            decision
            for decision in bad_decisions
            if decision["decision"] == "promote_normalized_record"
        )
        promoted["linked_entry_ids"] = ["rl.definition.actor-critic.001"]
        errors = superlib.validate_promotion_decisions(sources, entries, bad_decisions)
        self.assertTrue(
            any("must cite the promoted source" in error for error in errors), errors
        )

    def test_reviewed_papers_leave_queue_without_bloating_representative_sources(self):
        _, sources, entries = superlib.load_corpus()
        decisions = superlib.load_promotion_decisions()
        records = superlib.source_analysis_records(sources, entries, decisions)
        queue = superlib.promotion_queue_records(
            superlib.load_coverage_policy(), records
        )
        decided_ids = {decision["source_id"] for decision in decisions}
        self.assertTrue(decided_ids.isdisjoint(item["source_id"] for item in queue))
        reviewed = [record for record in records if record["promotion_decision"]]
        self.assertEqual(len(reviewed), 10)
        self.assertTrue(
            any(
                record["promotion_decision"]["decision"] == "link_existing_record"
                and not record["representative_entry_ids"]
                and record["promotion_entry_ids"]
                for record in reviewed
            )
        )

    def test_promotion_status_cli_exposes_auditable_summary_and_one_decision(self):
        summary_result = run_cli("promotion-status", "--format", "json")
        self.assertEqual(summary_result.returncode, 0, summary_result.stderr)
        summary = json.loads(summary_result.stdout)
        self.assertEqual(summary["reviewed_papers"], 10)
        self.assertEqual(sum(summary["by_decision"].values()), 10)

        decision = superlib.load_promotion_decisions()[0]
        detail_result = run_cli(
            "promotion-status", decision["source_id"], "--format", "json"
        )
        self.assertEqual(detail_result.returncode, 0, detail_result.stderr)
        detail = json.loads(detail_result.stdout)
        self.assertEqual(detail["source_id"], decision["source_id"])
        self.assertIn("primary_paper", detail)

    def test_source_health_classification_and_concurrency_are_deterministic(self):
        self.assertEqual(source_health.classify_http_status(200), "reachable")
        self.assertEqual(source_health.classify_http_status(403), "blocked")
        self.assertEqual(source_health.classify_http_status(404), "broken")
        self.assertEqual(source_health.classify_http_status(503), "transient")
        sources = [
            {"id": "paper-b", "url": "https://example.org/b"},
            {"id": "paper-a", "url": "https://example.org/a"},
        ]

        def fake_checker(source, timeout):
            self.assertEqual(timeout, 2.0)
            return {
                "source_id": source["id"],
                "url": source["url"],
                "final_url": source["url"],
                "http_status": 200,
                "status": "reachable",
                "detail": "",
            }

        results = source_health.verify_sources(
            sources, timeout=2.0, workers=2, checker=fake_checker
        )
        self.assertEqual([item["source_id"] for item in results], ["paper-a", "paper-b"])

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

    def test_skill_governance_artifacts_define_activation_boundaries(self):
        skill_dir = ROOT / "skills" / "super-library"
        card = (skill_dir / "skill-card.md").read_text(encoding="utf-8")
        activation = json.loads(
            (skill_dir / "evals" / "activation.json").read_text(encoding="utf-8")
        )
        cases = activation["activation_cases"]
        self.assertEqual(activation["skill"], "super-library")
        self.assertGreaterEqual(sum(case["should_activate"] for case in cases), 2)
        self.assertGreaterEqual(sum(not case["should_activate"] for case in cases), 2)
        self.assertIn("Capability manifest", card)
        self.assertIn("Credentials", card)
        self.assertIn("External effects", card)
        openai_yaml = (skill_dir / "agents" / "openai.yaml").read_text(
            encoding="utf-8"
        )
        self.assertIn("allow_implicit_invocation: true", openai_yaml)
        self.assertIn("$super-library", openai_yaml)

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

    def test_writing_guide_business_rules_are_enforced(self):
        taxonomy, sources, entries = superlib.load_corpus()
        guide_config, study = superlib.load_writing_guides()
        bad_guides = copy.deepcopy(guide_config)
        bad_guides["guides"][0]["related_entry_ids"].append("missing.entry.001")
        original_loader = superlib.load_writing_guides
        try:
            superlib.load_writing_guides = lambda: (bad_guides, study)
            errors = superlib.validate_writing_guides(taxonomy, sources, entries)
        finally:
            superlib.load_writing_guides = original_loader
        self.assertTrue(any("unknown related_entry_ids" in item for item in errors))

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
        self.assertIn(f"**{len(sources)} primary-source", readme)

    def test_writing_evals_reference_real_entries_and_valid_checks(self):
        _, _, entries = superlib.load_corpus()
        guide_config, _ = superlib.load_writing_guides()
        known_ids = {entry["id"] for entry in entries}
        known_guides = {guide["id"] for guide in guide_config["guides"]}
        cases = json.loads((ROOT / "evals" / "writing.json").read_text())["cases"]
        self.assertGreaterEqual(len(cases), 12)
        self.assertEqual({case["mode"] for case in cases}, {"paper", "rebuttal", "translation"})
        for case in cases:
            self.assertTrue(case["manual_rubric"])
            self.assertTrue(case["machine_checks"])
            self.assertTrue(set(case["expected_retrieval_ids"]).issubset(known_ids))
            self.assertIn(case["expected_guide_id"], known_guides)

    def test_writing_eval_lists_machine_checkable_cases(self):
        result = run_cli("eval-writing", "--list", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertGreaterEqual(payload["cases"], 12)
        self.assertTrue(all(item["machine_checks"] for item in payload["records"]))

    def test_writing_eval_blinds_checks_and_scores_pass_and_failure(self):
        case_id = "rebuttal-existing-evidence"
        blind = run_cli("eval-writing", "--case", case_id, "--format", "json")
        self.assertEqual(blind.returncode, 0, blind.stderr)
        packet = json.loads(blind.stdout)
        self.assertNotIn("machine_checks", packet)
        self.assertNotIn("manual_rubric", packet)
        self.assertNotIn("expected_retrieval_ids", packet)
        with tempfile.TemporaryDirectory() as temp_dir:
            response = Path(temp_dir) / "response.md"
            response.write_text(
                "Yes. Table 4 averages five seeds and shows a mean improvement "
                "of 3.2 points. No statistical significance test was run, so "
                "this evidence supports consistency across the reported runs "
                "but not a significance claim.",
                encoding="utf-8",
            )
            passed = run_cli(
                "eval-writing", "--case", case_id,
                "--response-file", str(response), "--format", "json", "--strict",
            )
            self.assertEqual(passed.returncode, 0, passed.stderr)
            self.assertTrue(json.loads(passed.stdout)["results"][0]["passed"])
            response.write_text("The result is robust.", encoding="utf-8")
            failed = run_cli(
                "eval-writing", "--case", case_id,
                "--response-file", str(response), "--format", "json", "--strict",
            )
            self.assertEqual(failed.returncode, 1, failed.stderr)
            self.assertFalse(json.loads(failed.stdout)["results"][0]["passed"])

    def test_writing_eval_accepts_equivalent_caption_protocol_wording(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            response = Path(temp_dir) / "response.md"
            response.write_text(
                "43 images/s and 21 ms on a single NVIDIA A100, using batch "
                "size 1 and FP16. Timing excludes model loading and includes "
                "preprocessing and action decoding. Values use 1,000 measured "
                "iterations following 100 warm-up iterations; they do not imply "
                "a hardware-independent ranking.",
                encoding="utf-8",
            )
            result = run_cli(
                "eval-writing", "--case", "paper-efficiency-table-caption",
                "--response-file", str(response), "--format", "json", "--strict",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)["results"][0]["passed"])

    def test_writing_eval_rejects_invalid_regex_contract(self):
        taxonomy, _, entries = superlib.load_corpus()
        bad_config = copy.deepcopy(superlib.load_writing_evals())
        bad_config["cases"][0]["machine_checks"][0]["pattern"] = "["
        original_loader = superlib.load_writing_evals
        try:
            superlib.load_writing_evals = lambda: bad_config
            errors = superlib.validate_writing_evals(taxonomy, entries)
        finally:
            superlib.load_writing_evals = original_loader
        self.assertTrue(any("invalid regex" in error for error in errors))

    def test_coverage_gaps_prioritize_reviewed_unlinked_papers(self):
        result = run_cli("coverage-gaps", "--limit", "10", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["summary"]["core_papers"], 300)
        self.assertEqual(payload["summary"]["directly_linked_papers"], 71)
        self.assertEqual(len(payload["records"]), 10)
        self.assertTrue(
            all(
                record["outcome"] == "structural_sample_without_library_links"
                for record in payload["records"]
            )
        )

    def test_promotion_queue_is_deterministic_and_keeps_dedup_outcome(self):
        _, sources, entries = superlib.load_corpus()
        policy = superlib.load_coverage_policy()
        records = superlib.source_analysis_records(sources, entries)
        first = superlib.promotion_queue_records(policy, records)
        second = superlib.promotion_queue_records(policy, records)
        self.assertEqual(first, second)
        p0_count = sum(record["priority"] == "P0" for record in first)
        self.assertEqual(p0_count, 21)
        self.assertTrue(all(record["priority"] == "P0" for record in first[:p0_count]))
        self.assertTrue(all(not record.get("linked_entry_ids") for record in first))
        self.assertTrue(
            all("record_no_promotion" in record["allowed_review_outcomes"] for record in first)
        )

    def test_retrieval_eval_executes_top_k_routes(self):
        cases = json.loads((ROOT / "evals" / "retrieval.json").read_text())
        self.assertGreaterEqual(len(cases), 28)
        result = run_cli("eval-retrieval")
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        self.assertEqual(payload["cases"], len(cases))
        self.assertEqual(payload["failed"], 0)
        self.assertEqual(payload["pass_rate"], 1.0)


if __name__ == "__main__":
    unittest.main()
