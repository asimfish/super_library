#!/usr/bin/env python3
"""Deterministic checks for blind Super Library writing evaluations."""

from __future__ import annotations

import re
from typing import Any, Callable, Dict, List, Protocol


class CheckEvaluator(Protocol):
    """Evaluate one declared check against a candidate response."""

    def __call__(self, check: Dict[str, Any], text: str) -> bool: ...


CHECK_REGISTRY: Dict[str, CheckEvaluator] = {}


def register_check(name: str) -> Callable[[CheckEvaluator], CheckEvaluator]:
    """Register a deterministic writing check by stable schema identifier."""

    def decorator(evaluator: CheckEvaluator) -> CheckEvaluator:
        if name in CHECK_REGISTRY:
            raise ValueError(f"duplicate writing check evaluator: {name}")
        CHECK_REGISTRY[name] = evaluator
        return evaluator

    return decorator


@register_check("required_regex")
def required_regex(check: Dict[str, Any], text: str) -> bool:
    return re.search(check["pattern"], text, re.IGNORECASE | re.MULTILINE) is not None


@register_check("forbidden_regex")
def forbidden_regex(check: Dict[str, Any], text: str) -> bool:
    return re.search(check["pattern"], text, re.IGNORECASE | re.MULTILINE) is None


def evaluate_response(case: Dict[str, Any], text: str) -> Dict[str, Any]:
    """Score objective invariants and return the separate manual rubric."""

    results: List[Dict[str, Any]] = []
    for check in case["machine_checks"]:
        evaluator = CHECK_REGISTRY.get(check["type"])
        if evaluator is None:
            passed = False
            detail = f"unknown evaluator {check['type']!r}"
        else:
            try:
                passed = evaluator(check, text)
                detail = check["message"]
            except re.error as exc:
                passed = False
                detail = f"invalid regular expression: {exc}"
        results.append(
            {
                "id": check["id"],
                "type": check["type"],
                "passed": passed,
                "message": detail,
            }
        )
    passed_count = sum(result["passed"] for result in results)
    return {
        "id": case["id"],
        "passed": passed_count == len(results),
        "machine_checks": len(results),
        "machine_checks_passed": passed_count,
        "check_results": results,
        "manual_review_required": True,
        "manual_rubric": case["manual_rubric"],
    }
