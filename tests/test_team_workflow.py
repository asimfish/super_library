"""Contract tests for the file-based, fail-closed writing-team coordinator.

These are synthetic author-supplied facts, not a writing-quality evaluation.
Oracles are public API results, rejected transitions, and durable file contents;
no test calls a private coordinator helper or emulates its validation algorithm.
"""

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Barrier
from unittest.mock import patch

from scripts import team_workflow as team


ROOT = Path(__file__).resolve().parents[1]
LANGUAGE = "LANGUAGE-CONTEXT-ONLY: retain the comparison axis and uncertainty."
ARGUMENTS = {
    "schema_version": "1.0",
    "notice": "Original structural synthesis, not scientific evidence.",
    "frames": [],
}
NARRATIVE_TARGETS = (
    "question", "evidence_selection", "flow", "scope", "no_meta_prose",
)


def task_fixture():
    return {
        "task_id": "synthetic-results",
        "request": "Write a short standalone comparison from only supplied facts.",
        "domain": "general",
        "section": "experiments",
        "intent": "compare",
        "guide": "experiments.analysis",
        "rhetoric_query": "Report a finding and its measured cost.",
        "technical_query": "Success rate and inference latency",
        "relation": "",
        "experiment_type": "",
        "evidence": [
            {
                "id": "fact-success",
                "text": "Under the same protocol, A succeeds in 8/10 trials and B in 6/10.",
                "locator": "Synthetic fixture, table 1, success row",
                "kind": "author_fact",
                "required": True,
            },
            {
                "id": "fact-latency",
                "text": "Median inference latency is 20 ms for A and 10 ms for B.",
                "locator": "Synthetic fixture, table 1, latency row",
                "kind": "author_fact",
                "required": True,
            },
        ],
        "constraints": ["No claims of statistical significance or causal mechanism."],
    }


def evidence_output(task=None):
    task = task or task_fixture()
    return {
        "checks": [
            {"evidence_id": item["id"], "status": "supported", "note": "Author fact."}
            for item in task["evidence"]
        ],
        "unresolved": [],
    }


def plan_output():
    return {
        "claims": [
            {
                "id": "claim-success",
                "statement": "A records more successes than B under the same protocol.",
                "evidence_ids": ["fact-success"],
                "qualification": "Descriptive counts only; ten trials per method.",
            },
            {
                "id": "claim-cost",
                "statement": "A has higher median inference latency than B.",
                "evidence_ids": ["fact-latency"],
                "qualification": "This measured setting only.",
            },
        ],
        "moves": [
            {"purpose": "Compare success counts", "claim_ids": ["claim-success"]},
            {"purpose": "Report the latency trade-off", "claim_ids": ["claim-cost"]},
        ],
    }


def writer_output(prefix=""):
    success = "A succeeds in 8/10 trials, compared with 6/10 for B under the same protocol."
    cost = "Median inference latency is 20 ms for A and 10 ms for B."
    return {
        "text": prefix + success + " " + cost,
        "claim_map": [
            {"claim_id": "claim-success", "quote": success, "evidence_ids": ["fact-success"]},
            {"claim_id": "claim-cost", "quote": cost, "evidence_ids": ["fact-latency"]},
        ],
    }


def review_output(role, verdict="pass", issue=""):
    targets = (
        ("fact-success", "fact-latency", "claim-success", "claim-cost")
        if role == "evidence_reviewer" else NARRATIVE_TARGETS
    )
    checks = [{"target_id": target, "status": "pass", "reason": "Checked."}
              for target in targets]
    if verdict == "revise":
        checks[0].update(status="fail", reason=issue or "Revision needed.")
    return {"verdict": verdict, "checks": checks,
            "issues": [issue or "Revision needed."] if verdict == "revise" else []}


class TeamWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory(prefix="superlib-team-test-")
        self.addCleanup(self.directory.cleanup)
        self.base = Path(self.directory.name)
        self.run = self.base / "run"

    def initialize(self, task=None, language=LANGUAGE, arguments=None):
        return team.initialize(
            ROOT, self.run, task or task_fixture(), language,
            copy.deepcopy(ARGUMENTS if arguments is None else arguments),
        )

    def artifact(self, role, output, actor=None, packet=None):
        packet = packet or team.packet(self.run, role)
        return {"role": role, "actor_id": actor or "actor-" + role,
                "input_sha256": packet["input_sha256"], "output": output}

    def submit(self, role, output, actor=None):
        return team.submit(self.run, self.artifact(role, output, actor))

    def advance_to_writer(self):
        self.initialize()
        self.submit("evidence_reader", evidence_output())
        self.submit("argument_planner", plan_output())

    def advance_to_reviews(self):
        self.advance_to_writer()
        self.submit("writer", writer_output())

    def passing_reviews(self):
        for role in ("evidence_reviewer", "narrative_reviewer"):
            self.submit(role, review_output(role))

    def assert_export_denied(self):
        with self.assertRaises(ValueError):
            team.export(self.run)

    def snapshot(self, directory=None):
        directory = directory or self.run
        return {str(path.relative_to(directory)): path.read_bytes()
                for path in directory.rglob("*") if path.is_file()}

    def isolated_catalog(self):
        root = self.base / "catalog"
        (root / "library").mkdir(parents=True)
        for name in ("taxonomy", "topics", "writing_guides", "argument_frames", "team_workflow"):
            shutil.copyfile(ROOT / "library" / (name + ".json"),
                            root / "library" / (name + ".json"))
        return root

    def test_exports_exact_manuscript_only_after_both_reviews(self):
        self.initialize()
        self.assert_export_denied()
        self.submit("evidence_reader", evidence_output())
        self.assert_export_denied()
        self.submit("argument_planner", plan_output())
        self.assert_export_denied()
        self.submit("writer", writer_output())
        self.assert_export_denied()
        self.submit("evidence_reviewer", review_output("evidence_reviewer"))
        self.assert_export_denied()
        self.submit("narrative_reviewer", review_output("narrative_reviewer"))
        self.assertEqual(team.export(self.run).rstrip("\n"), writer_output()["text"])
        self.assertNotIn("claim-success", team.export(self.run))
        self.assertNotIn("actor-", team.export(self.run))

    def test_dependency_order_and_unknown_roles_fail_closed(self):
        self.initialize()
        self.assertEqual(team.status(self.run)["ready_roles"], ["evidence_reader"])
        for role in ("argument_planner", "writer", "evidence_reviewer", "narrative_reviewer",
                     "../../escaped-artifact", "not-a-role"):
            with self.subTest(role=role), self.assertRaises(ValueError):
                team.packet(self.run, role)
        self.assertFalse((self.base / "escaped-artifact").exists())
        self.assert_export_denied()

    def test_original_task_is_frozen_without_mutating_callers(self):
        task = task_fixture()
        arguments = copy.deepcopy(ARGUMENTS)
        original = copy.deepcopy(task)
        self.initialize(task=task, arguments=arguments)
        self.assertEqual(task, original)
        task["evidence"][0]["text"] = "Caller mutation must not replace frozen evidence."
        arguments["notice"] = "Caller mutation."
        self.assertEqual(team.packet(self.run, "evidence_reader")["task"], original)
        self.submit("evidence_reader", evidence_output())
        self.submit("argument_planner", plan_output())
        packet = team.packet(self.run, "writer")
        self.assertEqual(packet["task"], original)
        self.assertIn(LANGUAGE, json.dumps(packet))
        self.assertNotIn("Caller mutation", json.dumps(packet))

    def test_unknown_or_mismatched_task_selectors_are_rejected_before_creation(self):
        invalid = {
            "domain": "unknown-domain", "section": "unknown-section", "intent": "unknown-intent",
            "topic": "unknown-topic", "guide": "unknown-guide", "relation": "unknown-relation",
            "experiment_type": "unknown-experiment", "task_id": "../../escaped-task",
        }
        for key, value in invalid.items():
            with self.subTest(key=key):
                task = task_fixture()
                task[key] = value
                self.run = self.base / ("invalid-" + key)
                with self.assertRaises(ValueError):
                    self.initialize(task)
                self.assertFalse(self.run.exists())
        self.run = self.base / "guide-mismatch"
        task = task_fixture()
        task["guide"] = "abstract"
        with self.assertRaises(ValueError):
            self.initialize(task)
        self.assertFalse(self.run.exists())

    def test_empty_duplicate_and_unknown_evidence_fields_are_rejected(self):
        variants = []
        task = task_fixture()
        task["evidence"] = []
        variants.append(task)
        task = task_fixture()
        task["evidence"][1]["id"] = task["evidence"][0]["id"]
        variants.append(task)
        task = task_fixture()
        task["evidence"][0]["kind"] = "assumed_true"
        variants.append(task)
        task = task_fixture()
        task["output_path"] = "../../escape"
        variants.append(task)
        task = task_fixture()
        task["evidence"][0]["required"] = "yes"
        variants.append(task)
        task = task_fixture()
        task["evidence"][0]["locator"] = ""
        variants.append(task)
        task = task_fixture()
        task["evidence"][0]["id"] = "../../escaped-evidence"
        variants.append(task)
        task = task_fixture()
        task["constraints"] = "A list is required."
        variants.append(task)
        for index, task in enumerate(variants):
            with self.subTest(index=index):
                self.run = self.base / ("malformed-" + str(index))
                with self.assertRaises(ValueError):
                    self.initialize(task)
                self.assertFalse(self.run.exists())

    def test_evidence_reader_must_cover_each_fact_exactly_once(self):
        self.initialize()
        for mutation in ("missing", "duplicate", "unknown"):
            with self.subTest(mutation=mutation):
                output = evidence_output()
                if mutation == "missing":
                    output["checks"].pop()
                elif mutation == "duplicate":
                    output["checks"].append(copy.deepcopy(output["checks"][0]))
                else:
                    output["checks"][0]["evidence_id"] = "invented-fact"
                before = team.status(self.run)
                with self.assertRaises(ValueError):
                    self.submit("evidence_reader", output)
                self.assertEqual(team.status(self.run), before)
        self.submit("evidence_reader", evidence_output())
        self.assertEqual(team.status(self.run)["ready_roles"], ["argument_planner"])

    def test_unverified_source_cannot_be_promoted_or_used_for_a_claim(self):
        task = task_fixture()
        task["evidence"][1]["kind"] = "unverified_source"
        self.initialize(task)
        with self.assertRaises(ValueError):
            self.submit("evidence_reader", evidence_output(task))
        output = evidence_output(task)
        output["checks"][1].update(status="unverified", note="Primary source not checked.")
        output["unresolved"] = ["Primary source not checked."]
        self.submit("evidence_reader", output)
        with self.assertRaises(ValueError):
            self.submit("argument_planner", plan_output())
        self.assert_export_denied()

    def test_planner_requires_supported_evidence_and_complete_claim_moves(self):
        self.initialize()
        self.submit("evidence_reader", evidence_output())
        for mutation in ("unknown-evidence", "unused-required-fact", "unused-claim",
                         "unknown-claim", "empty-evidence", "duplicate-claim"):
            with self.subTest(mutation=mutation):
                output = plan_output()
                if mutation == "unknown-evidence":
                    output["claims"][0]["evidence_ids"] = ["invented-fact"]
                elif mutation == "unused-required-fact":
                    output["claims"][1]["evidence_ids"] = ["fact-success"]
                elif mutation == "unused-claim":
                    output["moves"].pop()
                elif mutation == "unknown-claim":
                    output["moves"][0]["claim_ids"] = ["invented-claim"]
                elif mutation == "empty-evidence":
                    output["claims"][0]["evidence_ids"] = []
                else:
                    output["claims"].append(copy.deepcopy(output["claims"][0]))
                with self.assertRaises(ValueError):
                    self.submit("argument_planner", output)
        self.submit("argument_planner", plan_output())
        self.assertEqual(team.status(self.run)["ready_roles"], ["writer"])

    def test_writer_map_requires_real_quotes_all_claims_and_correct_fact_links(self):
        self.advance_to_writer()
        for mutation in ("missing-claim", "invented-quote", "wrong-evidence", "unknown-claim",
                         "missing-evidence", "empty-text"):
            with self.subTest(mutation=mutation):
                output = writer_output()
                if mutation == "missing-claim":
                    output["claim_map"].pop()
                elif mutation == "invented-quote":
                    output["claim_map"][0]["quote"] = "A result that is absent from the draft."
                elif mutation == "wrong-evidence":
                    output["claim_map"][0]["evidence_ids"] = ["fact-latency"]
                elif mutation == "unknown-claim":
                    output["claim_map"][0]["claim_id"] = "invented-claim"
                elif mutation == "missing-evidence":
                    output["claim_map"][0]["evidence_ids"] = []
                else:
                    output["text"] = ""
                with self.assertRaises(ValueError):
                    self.submit("writer", output)
        self.submit("writer", writer_output())
        self.assertEqual(set(team.status(self.run)["ready_roles"]),
                         {"evidence_reviewer", "narrative_reviewer"})

    def test_packet_language_separation_and_peer_review_isolation(self):
        self.initialize()
        self.assertNotIn(LANGUAGE, json.dumps(team.packet(self.run, "evidence_reader")))
        self.submit("evidence_reader", evidence_output())
        self.assertNotIn(LANGUAGE, json.dumps(team.packet(self.run, "argument_planner")))
        self.submit("argument_planner", plan_output())
        self.assertEqual(team.packet(self.run, "writer")["inputs"]["language_context"], LANGUAGE)
        self.submit("writer", writer_output())
        for role in ("evidence_reviewer", "narrative_reviewer"):
            packet = team.packet(self.run, role)
            self.assertEqual(packet["task"], task_fixture())
            self.assertIn(writer_output()["text"], json.dumps(packet))
            self.assertNotIn(LANGUAGE, json.dumps(packet))
        before = team.packet(self.run, "narrative_reviewer")
        feedback = review_output("evidence_reviewer", "revise", "PEER-REVIEW-SECRET-314159")
        self.submit("evidence_reviewer", feedback)
        after = team.packet(self.run, "narrative_reviewer")
        self.assertEqual(after, before)
        self.assertNotIn("PEER-REVIEW-SECRET-314159", json.dumps(after))

    def test_reviews_require_all_targets_once_and_coherent_pass_verdict(self):
        self.advance_to_reviews()
        for role in ("evidence_reviewer", "narrative_reviewer"):
            for mutation in ("missing", "duplicate", "unknown", "failed-check", "issues"):
                with self.subTest(role=role, mutation=mutation):
                    output = review_output(role)
                    if mutation == "missing":
                        output["checks"].pop()
                    elif mutation == "duplicate":
                        output["checks"].append(copy.deepcopy(output["checks"][0]))
                    elif mutation == "unknown":
                        output["checks"][0]["target_id"] = "invented-target"
                    elif mutation == "failed-check":
                        output["checks"][0]["status"] = "fail"
                    else:
                        output["issues"] = ["An unresolved material issue."]
                    with self.assertRaises(ValueError):
                        self.submit(role, output)
                    self.assert_export_denied()
        self.passing_reviews()
        self.assertTrue(team.status(self.run)["can_export"])

    def test_reviewers_must_be_distinct_from_writer_and_each_other(self):
        self.advance_to_reviews()
        for role in ("evidence_reviewer", "narrative_reviewer"):
            with self.subTest(role=role), self.assertRaises(ValueError):
                self.submit(role, review_output(role), actor="actor-writer")
        self.submit("evidence_reviewer", review_output("evidence_reviewer"), actor="review-actor")
        with self.assertRaises(ValueError):
            self.submit("narrative_reviewer", review_output("narrative_reviewer"), actor="review-actor")
        self.assert_export_denied()
        self.submit("narrative_reviewer", review_output("narrative_reviewer"), actor="other-review-actor")
        self.assertTrue(team.status(self.run)["can_export"])

    def test_tampered_dependency_hash_is_rejected_without_advancing_state(self):
        self.initialize()
        artifact = self.artifact("evidence_reader", evidence_output())
        artifact["input_sha256"] = "0" * 64
        before = team.status(self.run)
        with self.assertRaises(ValueError):
            team.submit(self.run, artifact)
        self.assertEqual(team.status(self.run), before)
        self.submit("evidence_reader", evidence_output())

    def test_worker_proposals_cannot_supply_paths_commands_or_unknown_fields(self):
        self.initialize()
        for key, value in (("output_path", "../../escape"), ("command", "echo unsafe"),
                           ("round", 99)):
            with self.subTest(key=key):
                artifact = self.artifact("evidence_reader", evidence_output())
                artifact[key] = value
                with self.assertRaises(ValueError):
                    team.submit(self.run, artifact)
        self.assertEqual(team.status(self.run)["ready_roles"], ["evidence_reader"])
        self.assertFalse((self.base / "escape").exists())

    def test_duplicate_submission_does_not_overwrite_accepted_artifact(self):
        self.initialize()
        artifact = self.artifact("evidence_reader", evidence_output())
        team.submit(self.run, artifact)
        before = self.snapshot()
        artifact["output"]["checks"][0]["note"] = "Attempted overwrite."
        with self.assertRaises(ValueError):
            team.submit(self.run, artifact)
        self.assertEqual(self.snapshot(), before)

    def test_revision_requires_both_reviews_and_an_explicit_revision_verdict(self):
        self.advance_to_reviews()
        with self.assertRaises(ValueError):
            team.revise(self.run)
        self.submit("evidence_reviewer", review_output("evidence_reviewer", "revise"))
        with self.assertRaises(ValueError):
            team.revise(self.run)
        self.submit("narrative_reviewer", review_output("narrative_reviewer"))
        self.assertTrue(team.status(self.run)["can_revise"])
        self.assert_export_denied()

    def test_passing_reviews_cannot_be_revised(self):
        self.advance_to_reviews()
        self.passing_reviews()
        before = team.status(self.run)
        with self.assertRaises(ValueError):
            team.revise(self.run)
        self.assertEqual(team.status(self.run), before)

    def test_revision_invalidates_old_writer_and_reviews_and_keeps_feedback(self):
        self.advance_to_writer()
        old_writer = self.artifact("writer", writer_output())
        team.submit(self.run, old_writer)
        old_evidence = self.artifact("evidence_reviewer", review_output("evidence_reviewer"))
        old_narrative = self.artifact("narrative_reviewer", review_output("narrative_reviewer"))
        self.submit("evidence_reviewer", review_output("evidence_reviewer", "revise", "REVISION-FEEDBACK-42"))
        self.submit("narrative_reviewer", review_output("narrative_reviewer"))
        team.revise(self.run)
        status = team.status(self.run)
        self.assertEqual(status["round"], 2)
        self.assertEqual(status["ready_roles"], ["writer"])
        self.assertEqual(set(status["completed_roles"]), {"evidence_reader", "argument_planner"})
        packet = team.packet(self.run, "writer")
        self.assertNotEqual(packet["input_sha256"], old_writer["input_sha256"])
        self.assertIn("REVISION-FEEDBACK-42", json.dumps(packet))
        self.assertEqual(packet["task"], task_fixture())
        with self.assertRaises(ValueError):
            team.submit(self.run, old_writer)
        self.submit("writer", writer_output(prefix="In this setting, "))
        for artifact in (old_evidence, old_narrative):
            with self.assertRaises(ValueError):
                team.submit(self.run, artifact)
        self.assert_export_denied()
        self.passing_reviews()
        self.assertEqual(team.export(self.run).rstrip("\n"), writer_output(prefix="In this setting, ")["text"])

    def test_revision_round_limit_cannot_be_bypassed(self):
        self.advance_to_reviews()
        maximum = team.status(self.run)["max_revision_rounds"]
        self.assertGreaterEqual(maximum, 1)
        for _ in range(maximum):
            self.submit("evidence_reviewer", review_output("evidence_reviewer", "revise"))
            self.submit("narrative_reviewer", review_output("narrative_reviewer"))
            team.revise(self.run)
            self.submit("writer", writer_output())
        self.submit("evidence_reviewer", review_output("evidence_reviewer", "revise"))
        self.submit("narrative_reviewer", review_output("narrative_reviewer"))
        before = team.status(self.run)
        with self.assertRaises(ValueError):
            team.revise(self.run)
        self.assertEqual(team.status(self.run), before)
        self.assert_export_denied()

    def test_resume_in_new_process_preserves_status_and_exact_export(self):
        self.advance_to_reviews()
        self.passing_reviews()
        program = (
            "import json,sys; from pathlib import Path; "
            "from scripts import team_workflow as team; "
            "run=Path(sys.argv[1]); "
            "print(json.dumps({'status':team.status(run),'text':team.export(run)}))"
        )
        result = subprocess.run([sys.executable, "-c", program, str(self.run)],
                                cwd=ROOT, text=True, capture_output=True, check=False)
        self.assertEqual(result.returncode, 0, result.stderr)
        resumed = json.loads(result.stdout)
        self.assertEqual(resumed["status"], team.status(self.run))
        self.assertEqual(resumed["text"].rstrip("\n"), writer_output()["text"])

    def test_existing_run_or_unrelated_directory_is_never_overwritten(self):
        self.initialize()
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.initialize()
        self.assertEqual(self.snapshot(), before)
        self.run = self.base / "unrelated"
        self.run.mkdir()
        sentinel = self.run / "keep.txt"
        sentinel.write_text("User content.", encoding="utf-8")
        with self.assertRaises(ValueError):
            self.initialize()
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "User content.")
        self.assertEqual(set(self.run.iterdir()), {sentinel})

    def test_symlink_run_directory_is_rejected_without_touching_target(self):
        target = self.base / "real-user-directory"
        target.mkdir()
        sentinel = target / "keep.txt"
        sentinel.write_text("User content.", encoding="utf-8")
        self.run.symlink_to(target, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.initialize()
        with self.assertRaises(ValueError):
            team.status(self.run)
        self.assertEqual(set(target.iterdir()), {sentinel})
        self.assertEqual(sentinel.read_text(encoding="utf-8"), "User content.")

    def test_complete_serialized_packets_respect_each_role_budget(self):
        config = json.loads((ROOT / "library/team_workflow.json").read_text(encoding="utf-8"))
        self.initialize()
        outputs = {"evidence_reader": evidence_output(), "argument_planner": plan_output(),
                   "writer": writer_output(), "evidence_reviewer": review_output("evidence_reviewer"),
                   "narrative_reviewer": review_output("narrative_reviewer")}
        for role, output in outputs.items():
            packet = team.packet(self.run, role)
            serialized = json.dumps(packet, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
            self.assertLessEqual(len(serialized), config["packet_max_chars"][role])
            self.submit(role, output)

    def test_oversized_context_fails_without_silent_truncation_or_partial_run(self):
        with self.assertRaises(ValueError):
            self.initialize(language="Complete original context. " * 10000)
        self.assertFalse(self.run.exists())

    def test_excessive_task_facts_are_not_silently_truncated(self):
        task = task_fixture()
        task["evidence"][0]["text"] = "Required fact. " * 10000 + "DO-NOT-DROP-THIS-TAIL"
        before = copy.deepcopy(task)
        with self.assertRaises(ValueError):
            self.initialize(task)
        self.assertEqual(task, before)
        self.assertFalse(self.run.exists())

    def test_packet_budget_counts_task_and_envelope_not_only_retrieved_context(self):
        root = self.isolated_catalog()
        config_path = root / "library/team_workflow.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["packet_max_chars"]["evidence_reader"] = 1000
        config_path.write_text(json.dumps(config), encoding="utf-8")
        self.assertEqual(team.load_config(root)["packet_max_chars"]["evidence_reader"], 1000)
        with self.assertRaises(ValueError):
            team.initialize(root, self.run, task_fixture(), "Short.", copy.deepcopy(ARGUMENTS))
        self.assertFalse(self.run.exists())

    def test_oversized_output_is_rejected_without_mutating_workflow(self):
        self.advance_to_writer()
        output = writer_output(prefix="Out of scope text. " * 10000)
        before = team.status(self.run)
        with self.assertRaises(ValueError):
            self.submit("writer", output)
        self.assertEqual(team.status(self.run), before)
        self.assert_export_denied()

    def test_catalog_changes_do_not_change_an_existing_run(self):
        root = self.isolated_catalog()
        team.initialize(root, self.run, task_fixture(), LANGUAGE, copy.deepcopy(ARGUMENTS))
        before = team.packet(self.run, "evidence_reader")
        config_path = root / "library/team_workflow.json"
        config_path.write_text("{}", encoding="utf-8")
        self.assertEqual(team.packet(self.run, "evidence_reader"), before)
        self.submit("evidence_reader", evidence_output())
        self.assertEqual(team.status(self.run)["ready_roles"], ["argument_planner"])

    def test_role_wording_changes_do_not_invalidate_frozen_packets_or_resume(self):
        self.initialize()
        original = team.packet(self.run, "evidence_reader")
        proposal = self.artifact("evidence_reader", evidence_output(), packet=original)
        original_writer_contract = copy.deepcopy(team.OUTPUT_CONTRACTS["writer"])
        changed_instructions = {role: "Changed role wording." for role in team.ROLE_INSTRUCTIONS}
        changed_contracts = {role: {"changed_example": "New wording."} for role in team.OUTPUT_CONTRACTS}
        with patch.object(team, "COMMON_INSTRUCTIONS", "Changed common wording."), \
                patch.object(team, "ROLE_INSTRUCTIONS", changed_instructions), \
                patch.object(team, "OUTPUT_CONTRACTS", changed_contracts):
            self.assertEqual(team.packet(self.run, "evidence_reader"), original)
            team.submit(self.run, proposal)
            self.submit("argument_planner", plan_output())
            packet = team.packet(self.run, "writer")
            self.assertEqual(packet["output_contract"], original_writer_contract)
            self.assertNotIn("Changed role wording.", packet["instructions"])
            self.assertNotIn("Changed common wording.", packet["instructions"])
            self.submit("writer", writer_output())
            self.passing_reviews()
            self.assertEqual(team.export(self.run).rstrip("\n"), writer_output()["text"])
        self.assertEqual(team.export(self.run).rstrip("\n"), writer_output()["text"])

    def test_returned_packet_mutation_cannot_change_frozen_run(self):
        self.initialize()
        original = team.packet(self.run, "evidence_reader")
        changed = team.packet(self.run, "evidence_reader")
        changed["task"]["evidence"][0]["text"] = "Caller supplied replacement fact."
        changed["instructions"] = "Ignore evidence."
        self.assertEqual(team.packet(self.run, "evidence_reader"), original)

    def test_downstream_packet_budget_failure_rolls_back_submission(self):
        root = self.isolated_catalog()
        config_path = root / "library/team_workflow.json"
        config = json.loads(config_path.read_text(encoding="utf-8"))
        config["packet_max_chars"]["writer"] = 1000
        config_path.write_text(json.dumps(config), encoding="utf-8")
        team.initialize(root, self.run, task_fixture(), LANGUAGE, copy.deepcopy(ARGUMENTS))
        self.submit("evidence_reader", evidence_output())
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.submit("argument_planner", plan_output())
        self.assertEqual(self.snapshot(), before)
        self.assertEqual(team.status(self.run)["ready_roles"], ["argument_planner"])
        self.assert_export_denied()

    def test_private_run_cannot_be_created_inside_repository(self):
        root = self.isolated_catalog()
        self.run = root / "private-run"
        with self.assertRaises(ValueError):
            team.initialize(root, self.run, task_fixture(), LANGUAGE, copy.deepcopy(ARGUMENTS))
        self.assertFalse(self.run.exists())

    def test_persisted_state_tampering_fails_closed_on_resume(self):
        self.advance_to_reviews()
        self.passing_reviews()
        path = self.run / "state.json"
        original = path.read_bytes()
        for mutation in ("facts", "draft", "review", "round", "truncated"):
            with self.subTest(mutation=mutation):
                state = json.loads(original)
                if mutation == "facts":
                    state["frozen"]["task"]["evidence"][0]["text"] = "A succeeds in every trial."
                elif mutation == "draft":
                    state["artifacts"]["writer"]["output"]["text"] = "Unreviewed replacement draft."
                elif mutation == "review":
                    del state["artifacts"]["evidence_reviewer"]
                elif mutation == "round":
                    state["round"] += 1
                path.write_text("{" if mutation == "truncated" else json.dumps(state), encoding="utf-8")
                with self.assertRaises(ValueError):
                    team.status(self.run)
                self.assert_export_denied()
                path.write_bytes(original)
        self.assertEqual(team.export(self.run).rstrip("\n"), writer_output()["text"])

    def test_symlink_artifact_or_state_is_rejected_without_touching_target(self):
        self.advance_to_reviews()
        self.passing_reviews()
        external = self.base / "external.json"
        external.write_text('{"preserve":"user content"}', encoding="utf-8")
        injected = self.run / "proposal.json"
        injected.symlink_to(external)
        with self.assertRaises(ValueError):
            team.status(self.run)
        self.assert_export_denied()
        self.assertEqual(external.read_text(encoding="utf-8"), '{"preserve":"user content"}')
        injected.unlink()
        state = self.run / "state.json"
        saved = self.base / "saved-state.json"
        state.rename(saved)
        before = saved.read_bytes()
        state.symlink_to(saved)
        with self.assertRaises(ValueError):
            team.status(self.run)
        self.assert_export_denied()
        self.assertEqual(saved.read_bytes(), before)

    def test_concurrent_independent_reviews_preserve_both_accepted_results(self):
        self.advance_to_reviews()
        proposals = [self.artifact(role, review_output(role))
                     for role in ("evidence_reviewer", "narrative_reviewer")]
        barrier = Barrier(2)

        def submit_at_once(proposal):
            barrier.wait(timeout=5)
            return team.submit(self.run, proposal)

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(submit_at_once, proposal) for proposal in proposals]
            for future in futures:
                future.result(timeout=10)
        self.assertTrue(team.status(self.run)["reviews_complete"])
        self.assertEqual(team.export(self.run).rstrip("\n"), writer_output()["text"])

    def test_concurrent_reuse_of_one_review_actor_never_exports(self):
        self.advance_to_reviews()
        proposals = [self.artifact(role, review_output(role), actor="same-actor")
                     for role in ("evidence_reviewer", "narrative_reviewer")]
        barrier = Barrier(2)

        def submit_at_once(proposal):
            barrier.wait(timeout=5)
            try:
                team.submit(self.run, proposal)
            except ValueError:
                return "rejected"
            return "accepted"

        with ThreadPoolExecutor(max_workers=2) as pool:
            futures = [pool.submit(submit_at_once, proposal) for proposal in proposals]
            results = [future.result(timeout=10) for future in futures]
        self.assertCountEqual(results, ["accepted", "rejected"])
        self.assert_export_denied()

    def test_external_json_rejects_duplicate_keys_and_nonfinite_numbers(self):
        path = self.base / "proposal.json"
        for text in ('{"actor_id":"first","actor_id":"second"}',
                     '{"value":NaN}', '{"value":Infinity}', '{"value":-Infinity}'):
            with self.subTest(text=text):
                path.write_text(text, encoding="utf-8")
                with self.assertRaises(ValueError):
                    team.read_input(path)

    def test_external_json_rejects_links_nonregular_files_and_invalid_utf8(self):
        target = self.base / "target.json"
        target.write_text('{"valid":true}', encoding="utf-8")
        link = self.base / "linked.json"
        link.symlink_to(target)
        with self.assertRaises(ValueError):
            team.read_input(link)
        with self.assertRaises(ValueError):
            team.read_input(self.base)
        target.write_bytes(b"\xff\xfe\x00")
        with self.assertRaises(ValueError):
            team.read_input(target)
        fifo = self.base / "proposal.fifo"
        os.mkfifo(fifo)
        # A subprocess deadline makes a blocking special-file read a visible test failure.
        program = (
            "import sys; from pathlib import Path; from scripts import team_workflow as team; "
            "team.read_input(Path(sys.argv[1]))"
        )
        result = subprocess.run([sys.executable, "-c", program, str(fifo)], cwd=ROOT,
                                text=True, capture_output=True, check=False, timeout=5)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("TeamWorkflowError", result.stderr)
        self.assertIn("regular file", result.stderr)


if __name__ == "__main__":
    unittest.main()
