"""Pure selection/rendering for an AI-paper adaptation, not STE compliance."""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Mapping, Sequence


def select_rules(config: Mapping[str, Any], sections: Iterable[str] = ()) -> List[Dict[str, Any]]:
    selected = {"core", *sections}
    return [rule for rule in config["rules"] if selected.intersection(rule["sections"])]


def compact_spec(config: Mapping[str, Any], sections: Iterable[str] = ()) -> Dict[str, Any]:
    """No examples, rationales, external text or unseen section protocols."""
    return {
        "id": config["id"],
        "notice": config["notice"],
        "rules": [
            {key: rule[key] for key in ("id", "level", "summary")}
            for rule in select_rules(config, sections)
        ],
    }


def render_spec(config: Mapping[str, Any], sections: Iterable[str] = (), *, full: bool = False) -> str:
    lines = ["## AI writing specification", "", config["notice"], ""]
    for rule in select_rules(config, sections):
        lines.append(f"- `{rule['id']}` [{rule['level']}]: {rule['summary']}")
        if full:
            lines.extend([f"  Why: {rule['rationale']}", f"  Check: {rule['check']}"])
            if rule.get("contrast"):
                pair = rule["contrast"]
                lines.extend([
                    "  Original conditional example; not evidence or an answer to copy:",
                    f"  Facts: {pair['facts']}", f"  Misuse under those facts: {pair['before']}",
                    f"  Preferred under those facts: {pair['after']}", f"  Reason: {pair['reason']}",
                ])
    return "\n".join(lines) + "\n"


def render_lexical_profile(profile: Mapping[str, Any]) -> str:
    lines = [
        "", "**Contextual usage profile (not a universal word whitelist):**", "",
        f"- Part of speech: {profile['part_of_speech']}",
        f"- Scope: {profile['scope']}",
        f"- Collocations: {', '.join(profile['collocations'])}",
        f"- Not interchangeable with: {', '.join(profile['not_equivalent_to'])}",
        f"- Rule references: {', '.join(profile['rule_ids'])}",
    ]
    for pair in profile["contrasts"]:
        lines.extend([
            "", "Original conditional contrast; do not import its facts into a draft:",
            f"- Given: {pair['facts']}", f"- Misuse: {pair['before']}",
            f"- Preferred: {pair['after']}", f"- Why: {pair['reason']}",
        ])
    return "\n".join(lines)


def reference_errors(config: Mapping[str, Any], entries: Sequence[Mapping[str, Any]], sections: Sequence[str]) -> List[str]:
    errors: List[str] = []
    ids = [rule["id"] for rule in config["rules"]]
    if len(ids) != len(set(ids)):
        errors.append("writing spec: duplicate rule IDs")
    allowed = {"core", *sections}
    for rule in config["rules"]:
        unknown = set(rule["sections"]) - allowed
        if unknown:
            errors.append(f"writing spec: {rule['id']}: unknown sections {sorted(unknown)}")
    for entry in entries:
        profile = entry.get("lexical_profile")
        if isinstance(profile, dict) and isinstance(profile.get("rule_ids"), list):
            unknown = set(profile["rule_ids"]) - set(ids)
            if unknown:
                errors.append(f"writing spec: {entry['id']}: unknown rule IDs {sorted(unknown)}")
    return errors
