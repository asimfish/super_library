"""Semantic validators for evidence-promotion review outcomes."""

from __future__ import annotations

from typing import Any, Dict, List, Mapping, Protocol, Sequence


class DecisionValidator(Protocol):
    """Validate the semantics specific to one promotion outcome."""

    def validate(
        self,
        decision: Mapping[str, Any],
        entries_by_id: Mapping[str, Mapping[str, Any]],
    ) -> List[str]:
        """Return human-readable validation errors."""


class LinkExistingRecordValidator:
    def validate(
        self,
        decision: Mapping[str, Any],
        entries_by_id: Mapping[str, Mapping[str, Any]],
    ) -> List[str]:
        if decision.get("linked_entry_ids"):
            return []
        return ["link_existing_record requires at least one linked entry"]


class PromoteNormalizedRecordValidator:
    def validate(
        self,
        decision: Mapping[str, Any],
        entries_by_id: Mapping[str, Mapping[str, Any]],
    ) -> List[str]:
        linked_ids = decision.get("linked_entry_ids", [])
        if not linked_ids:
            return ["promote_normalized_record requires at least one linked entry"]
        source_id = decision.get("source_id")
        promoted = [
            entry_id
            for entry_id in linked_ids
            if source_id in entries_by_id.get(entry_id, {}).get("source_ids", [])
        ]
        if promoted:
            return []
        return [
            "promote_normalized_record linked entries must cite the promoted source"
        ]


class RecordNoPromotionValidator:
    def validate(
        self,
        decision: Mapping[str, Any],
        entries_by_id: Mapping[str, Mapping[str, Any]],
    ) -> List[str]:
        if not decision.get("linked_entry_ids"):
            return []
        return ["record_no_promotion must not declare linked entries"]


DECISION_VALIDATORS: Dict[str, DecisionValidator] = {
    "link_existing_record": LinkExistingRecordValidator(),
    "promote_normalized_record": PromoteNormalizedRecordValidator(),
    "record_no_promotion": RecordNoPromotionValidator(),
}


def validate_decision_semantics(
    decision: Mapping[str, Any],
    entries_by_id: Mapping[str, Mapping[str, Any]],
) -> List[str]:
    validator = DECISION_VALIDATORS.get(str(decision.get("decision")))
    if validator is None:
        return [f"unknown promotion decision {decision.get('decision')!r}"]
    return validator.validate(decision, entries_by_id)


def decision_links_by_source(
    decisions: Sequence[Mapping[str, Any]],
) -> Dict[str, List[str]]:
    """Return deduplicated audit links without mutating representative citations."""
    return {
        str(decision["source_id"]): sorted(set(decision.get("linked_entry_ids", [])))
        for decision in decisions
        if decision.get("source_id")
    }
