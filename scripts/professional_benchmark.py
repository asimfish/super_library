#!/usr/bin/env python3
"""Blind A/B preparation and scoring for the Super Library benchmark."""

from __future__ import annotations

import hashlib
import itertools
import json
import random
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence, Tuple

if __package__:
    from .writing_eval import evaluate_response
else:
    from writing_eval import evaluate_response


class ProfessionalBenchmarkError(ValueError):
    """Raised when benchmark inputs violate the public evaluation contract."""


def canonical_sha256(value: Any) -> str:
    """Hash JSON-compatible data with a stable serialization."""

    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def neutral_prompt_packet(case: Mapping[str, Any]) -> Dict[str, Any]:
    """Return the condition-neutral task shown to both generation arms."""

    classification = {
        "domain": case["domain"],
        "section": case["section"],
        "intent": case["intent"],
    }
    if case.get("topic"):
        classification["topic"] = case["topic"]
    return {
        "case_id": case["id"],
        "mode": case["mode"],
        "classification": classification,
        "request": case["request"],
        "facts": case["facts"],
        "evidence_boundary": case["evidence_boundary"],
        "instructions": [
            "Return only the requested manuscript prose.",
            "Preserve every supplied fact, number, negation, and uncertainty qualifier.",
            "Do not invent citations, experiments, results, or implementation details.",
        ],
    }


def suite_case_ids(config: Mapping[str, Any], suite_id: str) -> List[str]:
    for suite in config["suites"]:
        if suite["id"] == suite_id:
            return list(suite["case_ids"])
    raise ProfessionalBenchmarkError(f"unknown benchmark suite {suite_id!r}")


def prepare_blind_pairs(
    config: Mapping[str, Any],
    cases_by_id: Mapping[str, Mapping[str, Any]],
    response_root: Path,
    run_manifest: Mapping[str, Any],
    suite_id: str,
    seed: int,
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Create a condition-blind response bundle and a separate private key."""

    case_ids = suite_case_ids(config, suite_id)
    condition_ids = [condition["id"] for condition in config["conditions"]]
    if set(condition_ids) != {"baseline", "super_library"}:
        raise ProfessionalBenchmarkError(
            "benchmark requires baseline and super_library conditions"
        )
    missing: List[str] = []
    responses: Dict[Tuple[str, str], str] = {}
    for condition_id in condition_ids:
        for case_id in case_ids:
            path = response_root / condition_id / f"{case_id}.md"
            if not path.is_file():
                missing.append(str(path))
                continue
            text = path.read_text(encoding="utf-8").strip()
            if not text:
                missing.append(f"{path} (empty)")
                continue
            responses[(condition_id, case_id)] = text
    if missing:
        preview = ", ".join(missing[:5])
        suffix = f" (+{len(missing) - 5} more)" if len(missing) > 5 else ""
        raise ProfessionalBenchmarkError(
            f"missing or empty benchmark responses: {preview}{suffix}"
        )

    manifest_hash = canonical_sha256(run_manifest)
    rng = random.Random(seed)
    shuffled = list(case_ids)
    rng.shuffle(shuffled)
    blind_pairs: List[Dict[str, Any]] = []
    key_pairs: List[Dict[str, Any]] = []
    for index, case_id in enumerate(shuffled, 1):
        case = cases_by_id[case_id]
        pair_digest = hashlib.sha256(
            f"{config['benchmark_id']}:{suite_id}:{seed}:{case_id}".encode("utf-8")
        ).hexdigest()[:8]
        pair_id = f"pair-{index:03d}-{pair_digest}"
        a_condition, b_condition = condition_ids
        if rng.randrange(2):
            a_condition, b_condition = b_condition, a_condition
        blind_pairs.append(
            {
                "pair_id": pair_id,
                "prompt": neutral_prompt_packet(case),
                "response_a": responses[(a_condition, case_id)],
                "response_b": responses[(b_condition, case_id)],
            }
        )
        key_pairs.append(
            {
                "pair_id": pair_id,
                "case_id": case_id,
                "assignment": {"a": a_condition, "b": b_condition},
            }
        )
    blind = {
        "schema_version": "1.0",
        "benchmark_id": config["benchmark_id"],
        "suite_id": suite_id,
        "run_id": run_manifest["run_id"],
        "run_manifest_sha256": manifest_hash,
        "seed": seed,
        "rating_instructions": [
            "Score response A and response B independently before choosing a preference.",
            "Use integer scores from 1 to 5 and the declared 1/3/5 anchors.",
            "Flag every applicable critical error; polished style cannot offset one.",
            "Do not infer or discuss which generation condition produced either side.",
        ],
        "rubric_dimensions": config["rubric_dimensions"],
        "critical_errors": config["critical_errors"],
        "pairs": blind_pairs,
    }
    key = {
        "schema_version": "1.0",
        "benchmark_id": config["benchmark_id"],
        "suite_id": suite_id,
        "run_id": run_manifest["run_id"],
        "run_manifest_sha256": manifest_hash,
        "blind_bundle_sha256": canonical_sha256(blind),
        "pairs": key_pairs,
    }
    return blind, key


def validate_blind_key(
    config: Mapping[str, Any],
    cases_by_id: Mapping[str, Mapping[str, Any]],
    blind: Mapping[str, Any],
    key: Mapping[str, Any],
) -> List[str]:
    """Validate bundle/key binding before revealing condition labels."""

    errors: List[str] = []
    for field in ("benchmark_id", "suite_id", "run_id", "run_manifest_sha256"):
        if blind.get(field) != key.get(field):
            errors.append(f"blind/key mismatch for {field}")
    if blind.get("benchmark_id") != config.get("benchmark_id"):
        errors.append("blind bundle targets a different benchmark")
    if key.get("blind_bundle_sha256") != canonical_sha256(blind):
        errors.append("blind bundle checksum does not match the private key")
    blind_pairs = {
        pair.get("pair_id"): pair
        for pair in blind.get("pairs", [])
        if isinstance(pair, dict)
    }
    key_pairs = {
        pair.get("pair_id"): pair
        for pair in key.get("pairs", [])
        if isinstance(pair, dict)
    }
    if len(blind_pairs) != len(blind.get("pairs", [])):
        errors.append("blind bundle contains duplicate or invalid pair IDs")
    if len(key_pairs) != len(key.get("pairs", [])):
        errors.append("private key contains duplicate or invalid pair IDs")
    if set(blind_pairs) != set(key_pairs):
        errors.append("blind bundle and private key contain different pairs")
    expected_cases = set(suite_case_ids(config, str(blind.get("suite_id", ""))))
    if len(key_pairs) != len(expected_cases):
        errors.append("private key pair count does not match the selected suite")
    observed_cases = set()
    for pair_id, record in key_pairs.items():
        case_id = record.get("case_id")
        if case_id not in cases_by_id:
            errors.append(f"{pair_id}: unknown case {case_id!r}")
        observed_cases.add(case_id)
        assignment = record.get("assignment", {})
        if set(assignment) != {"a", "b"} or set(assignment.values()) != {
            "baseline",
            "super_library",
        }:
            errors.append(f"{pair_id}: invalid condition assignment")
        blind_record = blind_pairs.get(pair_id, {})
        prompt_case_id = blind_record.get("prompt", {}).get("case_id")
        if prompt_case_id != case_id:
            errors.append(f"{pair_id}: prompt and private key case IDs differ")
        if not str(blind_record.get("response_a", "")).strip():
            errors.append(f"{pair_id}: response_a is empty")
        if not str(blind_record.get("response_b", "")).strip():
            errors.append(f"{pair_id}: response_b is empty")
    if observed_cases != expected_cases:
        errors.append("private key does not contain exactly the selected suite cases")
    return errors


def validate_ratings(
    config: Mapping[str, Any],
    blind: Mapping[str, Any],
    ratings: Mapping[str, Any],
) -> List[str]:
    """Validate rubric IDs and rating coverage references."""

    errors: List[str] = []
    if ratings.get("benchmark_id") != config.get("benchmark_id"):
        errors.append("ratings target a different benchmark")
    pair_ids = {pair["pair_id"] for pair in blind.get("pairs", [])}
    dimension_ids = {item["id"] for item in config["rubric_dimensions"]}
    critical_ids = {item["id"] for item in config["critical_errors"]}
    raters = ratings.get("raters", [])
    rater_ids = [item.get("id") for item in raters if isinstance(item, dict)]
    if len(rater_ids) != len(set(rater_ids)):
        errors.append("ratings contain duplicate rater IDs")
    known_raters = set(rater_ids)
    for rater in raters:
        if isinstance(rater, dict) and rater.get("independent") is not True:
            errors.append(
                f"rater {rater.get('id')!r} must attest independent=true"
            )
    seen = set()
    for index, rating in enumerate(ratings.get("ratings", []), 1):
        origin = f"rating[{index}]"
        pair_id = rating.get("pair_id")
        rater_id = rating.get("rater_id")
        if pair_id not in pair_ids:
            errors.append(f"{origin}: unknown pair_id {pair_id!r}")
        if rater_id not in known_raters:
            errors.append(f"{origin}: unknown rater_id {rater_id!r}")
        identity = (pair_id, rater_id)
        if identity in seen:
            errors.append(f"{origin}: duplicate pair/rater rating")
        seen.add(identity)
        for side in ("a", "b"):
            side_rating = rating.get(side, {})
            scores = side_rating.get("scores", {})
            if set(scores) != dimension_ids:
                errors.append(
                    f"{origin}.{side}: scores must contain exactly "
                    f"{sorted(dimension_ids)}"
                )
            for dimension_id, score in scores.items():
                if not isinstance(score, int) or isinstance(score, bool) or not 1 <= score <= 5:
                    errors.append(
                        f"{origin}.{side}.{dimension_id}: score must be an integer 1-5"
                    )
            flags = side_rating.get("critical_errors", [])
            if len(flags) != len(set(flags)):
                errors.append(f"{origin}.{side}: duplicate critical-error IDs")
            unknown = set(flags) - critical_ids
            if unknown:
                errors.append(
                    f"{origin}.{side}: unknown critical-error IDs {sorted(unknown)}"
                )
    return errors


def _mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def _rounded(value: float) -> float:
    return round(value, 4)


def _percentile(sorted_values: Sequence[float], fraction: float) -> float:
    if not sorted_values:
        return 0.0
    position = (len(sorted_values) - 1) * fraction
    lower = int(position)
    upper = min(lower + 1, len(sorted_values) - 1)
    weight = position - lower
    return sorted_values[lower] * (1 - weight) + sorted_values[upper] * weight


def bootstrap_mean_interval(
    values: Sequence[float], resamples: int, confidence_level: float, seed: int
) -> List[float]:
    """Return a deterministic percentile bootstrap interval over paired cases."""

    if not values:
        return [0.0, 0.0]
    rng = random.Random(seed)
    means = []
    for _ in range(resamples):
        sample = [values[rng.randrange(len(values))] for _ in values]
        means.append(_mean(sample))
    means.sort()
    alpha = (1.0 - confidence_level) / 2.0
    return [
        _rounded(_percentile(means, alpha)),
        _rounded(_percentile(means, 1.0 - alpha)),
    ]


def score_benchmark(
    config: Mapping[str, Any],
    cases_by_id: Mapping[str, Mapping[str, Any]],
    blind: Mapping[str, Any],
    key: Mapping[str, Any],
    ratings: Mapping[str, Any],
) -> Dict[str, Any]:
    """Aggregate machine invariants, blind ratings, paired effect, and agreement."""

    errors = validate_blind_key(config, cases_by_id, blind, key)
    errors.extend(validate_ratings(config, blind, ratings))
    if errors:
        raise ProfessionalBenchmarkError("; ".join(errors))

    blind_by_id = {pair["pair_id"]: pair for pair in blind["pairs"]}
    key_by_id = {pair["pair_id"]: pair for pair in key["pairs"]}
    dimension_ids = [item["id"] for item in config["rubric_dimensions"]]
    conditions = ["baseline", "super_library"]
    response_machine: Dict[Tuple[str, str], Dict[str, Any]] = {}
    for pair_id, key_record in key_by_id.items():
        case_id = key_record["case_id"]
        pair = blind_by_id[pair_id]
        for side in ("a", "b"):
            condition = key_record["assignment"][side]
            response_machine[(condition, case_id)] = evaluate_response(
                dict(cases_by_id[case_id]), pair[f"response_{side}"]
            )

    response_scores: Dict[Tuple[str, str], List[float]] = {}
    dimension_scores: Dict[Tuple[str, str, str], List[int]] = {}
    critical_observations = {condition: [] for condition in conditions}
    preference_votes = {"super_library": 0, "baseline": 0, "tie": 0}
    preferences_by_pair: Dict[str, List[str]] = {}
    for rating in ratings["ratings"]:
        pair_id = rating["pair_id"]
        key_record = key_by_id[pair_id]
        case_id = key_record["case_id"]
        preferences_by_pair.setdefault(pair_id, []).append(rating["preference"])
        preferred = rating["preference"]
        if preferred == "tie":
            preference_votes["tie"] += 1
        else:
            preference_votes[key_record["assignment"][preferred]] += 1
        for side in ("a", "b"):
            condition = key_record["assignment"][side]
            side_rating = rating[side]
            scores = side_rating["scores"]
            composite = _mean([scores[item] for item in dimension_ids])
            response_scores.setdefault((condition, case_id), []).append(composite)
            for dimension_id in dimension_ids:
                dimension_scores.setdefault(
                    (condition, case_id, dimension_id), []
                ).append(scores[dimension_id])
            critical_observations[condition].append(
                bool(side_rating["critical_errors"])
            )

    minimum_raters = config["quality_gates"]["min_raters_per_response"]
    suite_cases = suite_case_ids(config, blind["suite_id"])
    total_responses = len(suite_cases) * len(conditions)
    sufficiently_rated = sum(
        len(response_scores.get((condition, case_id), [])) >= minimum_raters
        for condition in conditions
        for case_id in suite_cases
    )
    coverage = sufficiently_rated / total_responses if total_responses else 0.0

    condition_reports: Dict[str, Any] = {}
    for condition in conditions:
        machine_results = [
            response_machine[(condition, case_id)] for case_id in suite_cases
        ]
        response_composites = [
            _mean(response_scores[(condition, case_id)])
            for case_id in suite_cases
            if response_scores.get((condition, case_id))
        ]
        dimensions = {}
        for dimension_id in dimension_ids:
            per_response = [
                _mean(dimension_scores[(condition, case_id, dimension_id)])
                for case_id in suite_cases
                if dimension_scores.get((condition, case_id, dimension_id))
            ]
            dimensions[dimension_id] = _rounded(_mean(per_response))
        observations = critical_observations[condition]
        condition_reports[condition] = {
            "responses": len(suite_cases),
            "machine_pass_rate": _rounded(
                _mean([float(result["passed"]) for result in machine_results])
            ),
            "machine_check_pass_rate": _rounded(
                sum(result["machine_checks_passed"] for result in machine_results)
                / sum(result["machine_checks"] for result in machine_results)
            ),
            "mean_professionalism": _rounded(_mean(response_composites)),
            "dimension_means": dimensions,
            "critical_error_rate": _rounded(
                _mean([float(flagged) for flagged in observations])
            ),
        }

    paired_differences = []
    for case_id in suite_cases:
        baseline_scores = response_scores.get(("baseline", case_id), [])
        library_scores = response_scores.get(("super_library", case_id), [])
        if len(baseline_scores) < minimum_raters or len(library_scores) < minimum_raters:
            continue
        paired_differences.append(_mean(library_scores) - _mean(baseline_scores))
    non_tie_votes = preference_votes["super_library"] + preference_votes["baseline"]
    win_rate = (
        preference_votes["super_library"] / non_tie_votes if non_tie_votes else 0.0
    )
    bootstrap = config["bootstrap"]
    comparison = {
        "paired_cases": len(paired_differences),
        "paired_mean_delta": _rounded(_mean(paired_differences)),
        "bootstrap_confidence_level": bootstrap["confidence_level"],
        "paired_delta_bootstrap_interval": bootstrap_mean_interval(
            paired_differences,
            bootstrap["resamples"],
            bootstrap["confidence_level"],
            bootstrap["seed"],
        ),
        "preference_votes": preference_votes,
        "super_library_win_rate_excluding_ties": _rounded(win_rate),
    }

    score_comparisons = []
    grouped_values: Dict[Tuple[str, str, str], List[int]] = {}
    for rating in ratings["ratings"]:
        for side in ("a", "b"):
            for dimension_id, value in rating[side]["scores"].items():
                grouped_values.setdefault(
                    (rating["pair_id"], side, dimension_id), []
                ).append(value)
    for values in grouped_values.values():
        score_comparisons.extend(itertools.combinations(values, 2))
    exact_rate = _mean([float(left == right) for left, right in score_comparisons])
    within_one_rate = _mean(
        [float(abs(left - right) <= 1) for left, right in score_comparisons]
    )
    preference_groups = [
        values for values in preferences_by_pair.values() if len(values) >= 2
    ]
    agreement = {
        "score_pair_comparisons": len(score_comparisons),
        "exact_score_agreement": _rounded(exact_rate),
        "within_one_score_agreement": _rounded(within_one_rate),
        "preference_pairs_with_multiple_raters": len(preference_groups),
        "unanimous_preference_rate": _rounded(
            _mean([float(len(set(values)) == 1) for values in preference_groups])
        ),
    }

    gates_config = config["quality_gates"]
    gate_values = [
        (
            "case_rating_coverage",
            coverage,
            ">=",
            gates_config["min_case_coverage"],
        ),
        (
            "super_library_machine_pass_rate",
            condition_reports["super_library"]["machine_pass_rate"],
            ">=",
            gates_config["library_machine_pass_rate_min"],
        ),
        (
            "super_library_mean_professionalism",
            condition_reports["super_library"]["mean_professionalism"],
            ">=",
            gates_config["library_mean_professionalism_min"],
        ),
        (
            "super_library_critical_error_rate",
            condition_reports["super_library"]["critical_error_rate"],
            "<=",
            gates_config["library_critical_error_rate_max"],
        ),
        (
            "paired_mean_delta",
            comparison["paired_mean_delta"],
            ">=",
            gates_config["paired_mean_delta_min"],
        ),
        (
            "super_library_pairwise_win_rate",
            comparison["super_library_win_rate_excluding_ties"],
            ">=",
            gates_config["library_pairwise_win_rate_min"],
        ),
        (
            "inter_rater_within_one",
            agreement["within_one_score_agreement"],
            ">=",
            gates_config["inter_rater_within_one_min"],
        ),
    ]
    gates = []
    for gate_id, value, operator, threshold in gate_values:
        passed = value >= threshold if operator == ">=" else value <= threshold
        gates.append(
            {
                "id": gate_id,
                "value": _rounded(value),
                "operator": operator,
                "threshold": threshold,
                "passed": passed,
            }
        )
    return {
        "schema_version": "1.0",
        "benchmark_id": config["benchmark_id"],
        "suite_id": blind["suite_id"],
        "run_id": blind["run_id"],
        "cases": len(suite_cases),
        "raters": len(ratings["raters"]),
        "rating_coverage": _rounded(coverage),
        "conditions": condition_reports,
        "comparison": comparison,
        "agreement": agreement,
        "quality_gates": gates,
        "passed": all(gate["passed"] for gate in gates),
        "interpretation_boundary": (
            "This report measures the declared prompts, generator, raters, and "
            "library commit only; it does not certify scientific correctness or "
            "generalize to other models, domains, or venues."
        ),
    }
