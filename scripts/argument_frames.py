"""Select compact argument plans; canonical entries/guides remain language owners.

No paper text, scientific claims, or agent-generated prose is fetched here. Study
references identify prior library navigation only, not a fresh evidence audit.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REGISTRY_PATH = "library/argument_frames.json"
SCHEMA_PATH = "schemas/argument-frames.schema.json"


def _read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"argument frames: cannot read {path.name}: {exc}") from exc


def _pointer(document: Any, locator: str) -> Any:
    """Resolve a nonempty JSON Pointer without interpreting paths or commands."""
    if not isinstance(locator, str) or not locator.startswith("/"):
        raise ValueError("invalid JSON Pointer")
    current = document
    for component in locator[1:].split("/"):
        component = component.replace("~1", "/").replace("~0", "~")
        if isinstance(current, list):
            if not component.isdecimal():
                raise ValueError("invalid array index")
            current = current[int(component)]
        elif isinstance(current, dict):
            current = current[component]
        else:
            raise ValueError("JSON Pointer traverses a scalar")
    if current is None or current == "" or current == [] or current == {}:
        raise ValueError("JSON Pointer resolves to empty content")
    return current


def _indexes(frames: list[dict]) -> dict:
    functions: dict = {}
    relations: dict = {}
    for frame in sorted(frames, key=lambda item: item["id"]):
        for section in frame["sections"]:
            for intent in frame["intents"]:
                functions.setdefault(section, {}).setdefault(intent, []).append(frame["id"])
                scoped = relations.setdefault(section, {}).setdefault(intent, {})
                for relation in frame["relations"]:
                    scoped.setdefault(relation, []).append(frame["id"])
    return {"function": functions, "evidence_relation": relations}


def _validated_registry(root: Path) -> tuple[dict, list[str]]:
    # Reuse only the schema-subset checker, never validate_corpus (which calls us).
    if __package__:
        from .superlib import schema_validation_errors
    else:
        from superlib import schema_validation_errors

    config = _read_json(root / REGISTRY_PATH)
    schema = _read_json(root / SCHEMA_PATH)
    errors = schema_validation_errors(config, schema)
    if errors:
        return {}, [f"argument frames: {error}" for error in errors]
    taxonomy = _read_json(root / "library/taxonomy.json")
    guides = _read_json(root / "library/writing_guides.json")
    guides_by_id = {guide["id"]: guide for guide in guides["guides"]}
    entries_by_id = {}
    for path in sorted((root / "library/entries").glob("*.jsonl")):
        try:
            for line in path.read_text(encoding="utf-8").splitlines():
                if line.strip():
                    entry = json.loads(line)
                    entries_by_id[entry["id"]] = entry
        except (OSError, UnicodeError, json.JSONDecodeError, KeyError, TypeError) as exc:
            raise ValueError(f"argument frames: cannot read entries in {path.name}: {exc}") from exc
    seen_ids: set[str] = set()
    seen_arguments: set[str] = set()
    used_relations: set[str] = set()
    used_experiments: set[str] = set()
    studies: dict[str, Any] = {}
    for frame in config["frames"]:
        label = f"argument frames: {frame['id']}"
        if frame["id"] in seen_ids:
            errors.append(f"{label}: duplicate frame ID")
        seen_ids.add(frame["id"])
        # IDs, selectors and reference labels do not make duplicated prose novel.
        fingerprint = json.dumps(
            {key: frame[key] for key in ("question", "evidence_requirements", "moves", "boundary")},
            sort_keys=True, ensure_ascii=False,
        )
        if fingerprint in seen_arguments:
            errors.append(f"{label}: duplicate argument content")
        seen_arguments.add(fingerprint)
        for field, allowed in (
            ("sections", taxonomy["sections"]), ("intents", taxonomy["intents"]),
            ("relations", config["relations"]), ("experiment_types", config["experiment_types"]),
        ):
            unknown = sorted(set(frame[field]) - set(allowed))
            if unknown:
                errors.append(f"{label}: unknown {field}: {unknown}")
        used_relations.update(frame["relations"])
        used_experiments.update(frame["experiment_types"])
        for entry_id in frame["entry_ids"]:
            entry = entries_by_id.get(entry_id)
            if entry is None:
                errors.append(f"{label}: unknown entry ID {entry_id}")
            elif not set(frame["sections"]).intersection(entry.get("sections", [])):
                errors.append(f"{label}: entry {entry_id} has no matching section")
        for reference in frame["guide_refs"]:
            guide = guides_by_id.get(reference["id"])
            if guide is None:
                errors.append(f"{label}: unknown guide ID {reference['id']}")
                continue
            if guide["section"] not in frame["sections"]:
                errors.append(f"{label}: guide {reference['id']} has no matching section")
            try:
                _pointer(guide, reference["locator"])
            except (KeyError, IndexError, ValueError) as exc:
                errors.append(f"{label}: invalid guide locator {reference['locator']}: {exc}")
        for reference in frame["study_refs"]:
            relative = reference["path"]
            path = root / relative
            # Schema restricts the spelling; resolution also rejects symlink escape.
            study_root = root.resolve() / "library/studies"
            if (any(part.is_symlink() for part in (root / "library", root / "library/studies", path))
                    or not path.resolve().is_relative_to(study_root)):
                errors.append(f"{label}: unsafe study path {relative}")
                continue
            try:
                if relative not in studies:
                    studies[relative] = _read_json(path)
                _pointer(studies[relative], reference["locator"])
            except (KeyError, IndexError, ValueError) as exc:
                errors.append(f"{label}: invalid study reference {relative}{reference['locator']}: {exc}")
    for field, used in (("relations", used_relations), ("experiment_types", used_experiments)):
        unused = sorted(set(config[field]) - used)
        if unused:
            errors.append(f"argument frames: unused {field}: {unused}")
    return config, errors


def validate_frames(root: Path) -> list[str]:
    """Return schema, reference, scope and deduplication errors, without writes."""
    try:
        _, errors = _validated_registry(Path(root))
        return errors
    except (ValueError, KeyError, TypeError) as exc:
        return [f"argument frames: invalid registry dependency: {exc}"]


def load_frames(root: Path) -> dict:
    """Load validated originals plus derived section-scoped retrieval indexes.

    ``indexes.function[section][intent]`` and
    ``indexes.evidence_relation[section][intent][relation]`` contain frame IDs.
    These are computed from canonical frame selectors, never separately edited.
    """
    try:
        config, errors = _validated_registry(Path(root))
    except (KeyError, TypeError) as exc:
        raise ValueError(f"argument frames: invalid registry dependency: {exc}") from exc
    if errors:
        raise ValueError("\n".join(errors))
    config["indexes"] = _indexes(config["frames"])
    return config


def select_frames(
    root: Path, *, section: str, intent: str, relation: str = "",
    experiment_type: str = "", limit: int = 2, max_chars: int = 6000,
) -> dict:
    """Return whole frames, measured as UTF-8-friendly indented JSON + newline.

    All selectors are exact controlled IDs. Unknown values fail; known values
    with no joint match produce an explicit empty envelope. A requested matching
    set that exceeds the cap fails rather than silently omitting any frame.
    """
    root = Path(root)
    if not isinstance(limit, int) or isinstance(limit, bool) or not 1 <= limit <= 8:
        raise ValueError("argument frames: limit must be an integer from 1 to 8")
    if not isinstance(max_chars, int) or isinstance(max_chars, bool) or max_chars < 1:
        raise ValueError("argument frames: max_chars must be a positive integer")
    config = load_frames(root)
    taxonomy = _read_json(root / "library/taxonomy.json")
    for field, value, allowed, optional in (
        ("section", section, taxonomy["sections"], False),
        ("intent", intent, taxonomy["intents"], False),
        ("relation", relation, config["relations"], True),
        ("experiment_type", experiment_type, config["experiment_types"], True),
    ):
        if not isinstance(value, str) or (value not in allowed and not (optional and value == "")):
            raise ValueError(f"argument frames: unknown {field}: {value!r}")
    if relation:
        selected_ids = config["indexes"]["evidence_relation"].get(section, {}).get(intent, {}).get(relation, [])
    else:
        selected_ids = config["indexes"]["function"].get(section, {}).get(intent, [])
    by_id = {frame["id"]: frame for frame in config["frames"]}
    frames = [by_id[frame_id] for frame_id in selected_ids
              if not experiment_type or experiment_type in by_id[frame_id]["experiment_types"]][:limit]
    notice = config["notice"]
    if not frames:
        notice += " No matching frame for these known selectors; do not substitute an unrelated frame."
    envelope = {"schema_version": config["schema_version"], "notice": notice, "frames": frames}
    size = len(json.dumps(envelope, ensure_ascii=False, indent=2) + "\n")
    if size > max_chars:
        raise ValueError(f"argument frames: complete envelope requires {size} characters; max_chars is {max_chars}")
    return envelope
