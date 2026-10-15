"""Argument-frame routing and provenance contracts, not writing-quality claims."""

import copy
import json
import shutil
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

from scripts import argument_frames


ROOT = Path(__file__).resolve().parents[1]


@contextmanager
def fixture_root():
    with tempfile.TemporaryDirectory(prefix="superlib-frames-test-") as directory:
        root = Path(directory)
        (root / "schemas").mkdir()
        (root / "library").mkdir()
        for relative in (
            "library/argument_frames.json", "library/taxonomy.json",
            "library/writing_guides.json", "schemas/argument-frames.schema.json",
        ):
            shutil.copyfile(ROOT / relative, root / relative)
        for relative in ("library/entries", "library/studies"):
            shutil.copytree(ROOT / relative, root / relative)
        yield root


def mutate_registry(root, change):
    path = root / "library/argument_frames.json"
    config = json.loads(path.read_text(encoding="utf-8"))
    change(config)
    path.write_text(json.dumps(config, ensure_ascii=False), encoding="utf-8")


class ArgumentFrameTests(unittest.TestCase):
    def test_registry_has_seven_original_navigation_only_frames(self):
        self.assertEqual(argument_frames.validate_frames(ROOT), [])
        registry = argument_frames.load_frames(ROOT)
        self.assertEqual(len(registry["frames"]), 7)
        self.assertEqual(registry["audit"]["status"], "existing_library_navigation_only")
        self.assertIs(registry["audit"]["new_primary_paper_audit"], False)
        for frame in registry["frames"]:
            self.assertEqual(frame["provenance"], "original_synthesis")
            self.assertNotIn("expression", frame)
            self.assertNotIn("examples", frame)
            self.assertTrue(frame["entry_ids"] and frame["guide_refs"] and frame["study_refs"])

    def test_indexes_are_derived_and_scoped_by_section_and_function(self):
        config = argument_frames.load_frames(ROOT)
        self.assertNotIn("indexes", json.loads((ROOT / argument_frames.REGISTRY_PATH).read_text()))
        index = config["indexes"]["evidence_relation"]
        self.assertEqual(index["experiments"]["compare"]["tradeoff"], ["argument.tradeoff"])
        self.assertNotIn("tradeoff", index["related_work"]["compare"])
        self.assertNotIn("argument.tradeoff", config["indexes"]["function"]["abstract"]["compare"])

    def test_each_relation_selects_its_exact_frame(self):
        registry = argument_frames.load_frames(ROOT)
        for frame in registry["frames"]:
            with self.subTest(frame=frame["id"]):
                envelope = argument_frames.select_frames(
                    ROOT, section=frame["sections"][0], intent=frame["intents"][0],
                    relation=frame["relations"][0], experiment_type=frame["experiment_types"][0],
                )
                self.assertEqual([f["id"] for f in envelope["frames"]], [frame["id"]])
                self.assertEqual(envelope["frames"][0], frame)

    def test_selection_is_deterministic_whole_and_deduplicated(self):
        arguments = {"section": "experiments", "intent": "evidence", "limit": 8, "max_chars": 24000}
        first = argument_frames.select_frames(ROOT, **arguments)
        self.assertEqual(first, argument_frames.select_frames(ROOT, **arguments))
        ids = [frame["id"] for frame in first["frames"]]
        self.assertEqual(ids, sorted(set(ids)))
        original = {frame["id"]: frame for frame in argument_frames.load_frames(ROOT)["frames"]}
        for frame in first["frames"]:
            self.assertEqual(frame, original[frame["id"]])

    def test_known_incompatible_selectors_return_explicit_empty(self):
        for selectors in (
            {"section": "related_work", "intent": "compare", "relation": "tradeoff"},
            {"section": "experiments", "intent": "evidence", "relation": "tradeoff", "experiment_type": "ablation"},
            {"section": "method", "intent": "describe"},
        ):
            with self.subTest(selectors=selectors):
                envelope = argument_frames.select_frames(ROOT, **selectors)
                self.assertEqual(envelope["frames"], [])
                self.assertIn("No matching frame", envelope["notice"])

    def test_unknown_and_non_string_selectors_fail(self):
        defaults = {"section": "experiments", "intent": "evidence"}
        for key in ("section", "intent", "relation", "experiment_type"):
            for value in ("unknown", "EXPERIMENTS", [], None):
                with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                    argument_frames.select_frames(ROOT, **{**defaults, key: value})
        for key in ("section", "intent"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                argument_frames.select_frames(ROOT, **{**defaults, key: ""})

    def test_invalid_budgets_and_limits_fail(self):
        for key, values in (("limit", (0, -1, 9, True, 1.5)), ("max_chars", (0, -1, False, 1.5))):
            for value in values:
                with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                    argument_frames.select_frames(ROOT, section="experiments", intent="evidence", **{key: value})

    def test_budget_includes_complete_json_envelope_and_newline(self):
        arguments = {"section": "experiments", "intent": "evidence", "relation": "tradeoff"}
        result = argument_frames.select_frames(ROOT, **arguments)
        size = len(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
        self.assertEqual(result, argument_frames.select_frames(ROOT, **arguments, max_chars=size))
        with self.assertRaisesRegex(ValueError, "complete envelope"):
            argument_frames.select_frames(ROOT, **arguments, max_chars=size - 1)

    def test_budget_does_not_silently_discard_selected_frames(self):
        arguments = {"section": "experiments", "intent": "evidence"}
        one = argument_frames.select_frames(ROOT, **arguments, limit=1)
        one_size = len(json.dumps(one, ensure_ascii=False, indent=2) + "\n")
        with self.assertRaisesRegex(ValueError, "complete envelope"):
            argument_frames.select_frames(ROOT, **arguments, limit=2, max_chars=one_size)
        with self.assertRaisesRegex(ValueError, "complete envelope"):
            argument_frames.select_frames(ROOT, section="method", intent="describe", max_chars=1)

    def test_unknown_reference_and_selector_validation(self):
        cases = (
            (lambda c: c["frames"][0]["entry_ids"].append("unknown.entry"), "unknown entry"),
            (lambda c: c["frames"][0]["guide_refs"][0].update(id="unknown.guide"), "unknown guide"),
            (lambda c: c["frames"][0]["sections"].append("unknown"), "unknown sections"),
            (lambda c: c["frames"][0]["intents"].append("unknown"), "unknown intents"),
            (lambda c: c["frames"][0]["relations"].append("unknown"), "unknown relations"),
            (lambda c: c["frames"][0]["experiment_types"].append("unknown"), "unknown experiment_types"),
            (lambda c: c["relations"].append("unused"), "unused relations"),
        )
        for mutate, expected in cases:
            with self.subTest(expected=expected), fixture_root() as root:
                mutate_registry(root, mutate)
                self.assertIn(expected, "\n".join(argument_frames.validate_frames(root)))
                with self.assertRaises(ValueError):
                    argument_frames.load_frames(root)

    def test_reference_locators_are_resolved_not_merely_stored(self):
        for key in ("guide_refs", "study_refs"):
            with self.subTest(key=key), fixture_root() as root:
                prefix = "/moves/" if key == "guide_refs" else "/observations/"
                mutate_registry(root, lambda c: c["frames"][0][key][0].update(locator=prefix + "99999"))
                self.assertTrue(argument_frames.validate_frames(root))
        with fixture_root() as root:
            mutate_registry(root, lambda c: c["frames"][0]["guide_refs"][0].update(id="abstract"))
            self.assertIn("no matching section", "\n".join(argument_frames.validate_frames(root)))

    def test_study_traversal_and_symlink_fail(self):
        with fixture_root() as root:
            mutate_registry(root, lambda c: c["frames"][0]["study_refs"][0].update(path="../secret.json"))
            self.assertTrue(argument_frames.validate_frames(root))
        with fixture_root() as root:
            path = root / "library/studies/experimental_narrative_2026-10.json"
            path.unlink()
            path.symlink_to(ROOT / "library/studies/experimental_narrative_2026-10.json")
            self.assertIn("unsafe study path", "\n".join(argument_frames.validate_frames(root)))

    def test_duplicate_id_and_duplicate_argument_content_fail(self):
        with fixture_root() as root:
            mutate_registry(root, lambda c: c["frames"][1].update(id=c["frames"][0]["id"]))
            self.assertIn("duplicate frame ID", "\n".join(argument_frames.validate_frames(root)))
        with fixture_root() as root:
            def duplicate(config):
                frame = copy.deepcopy(config["frames"][0])
                frame["id"] = "argument.relabeled-duplicate"
                config["frames"].append(frame)
            mutate_registry(root, duplicate)
            self.assertIn("duplicate argument content", "\n".join(argument_frames.validate_frames(root)))

    def test_new_audit_claim_or_copied_language_field_fails(self):
        for mutate in (
            lambda c: c["audit"].update(new_primary_paper_audit=True),
            lambda c: c["frames"][0].update(provenance="attested_collocation"),
            lambda c: c["frames"][0].update(expression="A second canonical language owner."),
        ):
            with fixture_root() as root:
                mutate_registry(root, mutate)
                self.assertTrue(argument_frames.validate_frames(root))

    def test_malformed_missing_and_wrong_shape_registry_fail_closed(self):
        for contents in ("{", "[]", '{"schema_version":"1.0"}'):
            with self.subTest(contents=contents), fixture_root() as root:
                (root / argument_frames.REGISTRY_PATH).write_text(contents, encoding="utf-8")
                self.assertTrue(argument_frames.validate_frames(root))
                with self.assertRaises(ValueError):
                    argument_frames.load_frames(root)
        with fixture_root() as root:
            (root / argument_frames.REGISTRY_PATH).unlink()
            self.assertTrue(argument_frames.validate_frames(root))


if __name__ == "__main__":
    unittest.main()
