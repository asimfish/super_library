"""Explicit runtime projections; canonical cards remain the reference owner."""

from __future__ import annotations

import copy
from typing import Any, Mapping, Sequence

NOTICE = (
    "Drafting projection, not a complete reference card. Facts come only from the "
    "task. Avoid notes constrain wording; do not turn every warning into a sentence. "
    "Each sentence should advance the supplied argument rather than repeat its "
    "opening finding. Preserve required values, material adverse outcomes and "
    "uncertainty; a missing input is not a slot to invent."
)


def project_entry(entry: Mapping[str, Any]) -> dict:
    keys = ("id", "kind", "expression", "meaning", "guidance", "avoid", "source_ids")
    out = {key: copy.deepcopy(entry[key]) for key in keys}
    out["provenance_type"] = entry["provenance"]["type"]
    # One optional structural illustration, not a required sentence to emit.
    out["examples"] = copy.deepcopy(entry["examples"][:1])
    if entry.get("attestations"):
        out["attestations"] = copy.deepcopy(entry["attestations"])
    if entry.get("lexical_profile"):
        out["lexical_profile"] = {
            key: copy.deepcopy(value) for key, value in entry["lexical_profile"].items()
            if key != "contrasts"
        }
    return out


def project_source(source: Mapping[str, Any]) -> dict:
    return {key: source[key] for key in ("id", "title", "venue", "year", "url")}


def project_guide(guide: Mapping[str, Any], domains: Sequence[str] = ()) -> dict:
    keys = ("id", "guide_type", "section", "label", "purpose", "inputs",
            "moves", "verification", "avoid")
    out = {key: copy.deepcopy(guide[key]) for key in keys}
    requested = {"embodied_ai" if d == "robot_learning" else d for d in domains}
    overlays = guide.get("domain_overlays", [])
    if overlays:
        out["domain_overlays"] = copy.deepcopy([
            item for item in overlays if not requested or item["id"] in requested
        ])
    return out


def render_guide(guide: Mapping[str, Any]) -> str:
    lines = [f"## Task-specific protocol: {guide['label']}", "",
             f"`{guide['id']}` · drafting projection", "", guide["purpose"], "",
             "### Inputs, only when supplied", ""]
    lines.extend(f"- {text}" for text in guide["inputs"])
    for move in guide["moves"]:
        mode = "required if its material exists" if move["required"] else "conditional"
        lines.extend(["", f"### {move['label']} ({mode})", ""])
        lines.extend(f"- {text}" for text in move["checks"])
    for overlay in guide.get("domain_overlays", []):
        lines.extend(["", f"### {overlay['label']}", ""])
        lines.extend(f"- {text}" for text in overlay["checks"])
    for key in ("verification", "avoid"):
        lines.extend(["", f"### {key.title()}", ""])
        lines.extend(f"- {text}" for text in guide[key])
    return "\n".join(lines) + "\n"


def render_entry(entry: Mapping[str, Any], sources: Sequence[Mapping[str, Any]]) -> str:
    lines = [f"### {entry['expression']} · `{entry['id']}`", "",
             f"Provenance: `{entry['provenance_type']}`; source links are navigation.",
             "", entry["meaning"], "", f"Use: {entry['guidance']}",
             "", f"Avoid: {entry['avoid']}"]
    if entry["examples"]:
        lines.extend(["", "Optional pattern; use only facts supplied by the task:",
                      entry["examples"][0]])
    profile = entry.get("lexical_profile")
    if profile:
        lines.extend(["", f"Sense / part of speech: {profile['part_of_speech']}; {profile['scope']}",
                      f"Collocations: {', '.join(profile['collocations'])}",
                      f"Not interchangeable with: {', '.join(profile['not_equivalent_to'])}",
                      f"Rule references: {', '.join(profile['rule_ids'])}"])
    for item in entry.get("attestations", []):
        lines.append(f"Attested: `{item['source_id']}` at {item['locator']}")
    if sources:
        lines.extend(["", "Verify primary sources before a literature claim:"])
        lines.extend(f"- [{s['title']}]({s['url']}) · `{s['id']}` ({s['venue']} {s['year']})"
                     for s in sources)
    return "\n".join(lines)
