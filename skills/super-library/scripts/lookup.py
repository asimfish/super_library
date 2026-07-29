#!/usr/bin/env python3
"""Bounded lookup for an installed, standalone Super Library skill."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Sequence, Tuple


SKILL_DIR = Path(__file__).resolve().parents[1]
INDEX_PATH = SKILL_DIR / "references" / "index.json"
TOKEN_RE = re.compile(r"[a-z0-9]+(?:[-'][a-z0-9]+)?")


def load_index() -> Dict[str, Any]:
    return json.loads(INDEX_PATH.read_text(encoding="utf-8"))


def normalize(text: str) -> str:
    return " ".join(TOKEN_RE.findall(text.lower()))


def expand_query(query: str, aliases: Dict[str, List[str]]) -> List[str]:
    variants = [query]
    for alias, expansions in aliases.items():
        if alias in query:
            variants.extend(query.replace(alias, expansion) for expansion in expansions)
    return list(dict.fromkeys(variants))


def score(entry: Dict[str, Any], query: str) -> int:
    if not query.strip():
        return 1
    query_norm = normalize(query)
    tokens = [
        token
        for token in TOKEN_RE.findall(query_norm)
        if token
        not in {
            "a",
            "an",
            "and",
            "are",
            "for",
            "from",
            "in",
            "is",
            "of",
            "on",
            "the",
            "to",
            "with",
        }
    ]
    expression = normalize(entry["expression"])
    meaning = normalize(entry["meaning"])
    guidance = normalize(entry["guidance"])
    examples = normalize(" ".join(entry["examples"]))
    metadata = normalize(
        " ".join(entry["domains"] + entry["sections"] + entry["intents"] + entry["tags"])
    )
    value = 0
    if query_norm == expression:
        value += 50
    elif query_norm and query_norm in expression:
        value += 24
    elif query_norm and query_norm in f"{expression} {meaning}":
        value += 12
    for token in tokens:
        value += 7 * expression.split().count(token)
        value += 4 * meaning.split().count(token)
        value += 2 * guidance.split().count(token)
        value += examples.split().count(token)
        value += 3 * metadata.split().count(token)
    if value and entry["provenance"]["type"] == "attested_collocation":
        value += 2
    return value


def filtered(
    entries: Iterable[Dict[str, Any]],
    domains: Sequence[str],
    sections: Sequence[str],
    intents: Sequence[str],
    kinds: Sequence[str],
) -> Iterable[Dict[str, Any]]:
    for entry in entries:
        if (
            domains
            and "general" not in entry["domains"]
            and not set(domains).intersection(entry["domains"])
        ):
            continue
        if sections and not set(sections).intersection(entry["sections"]):
            continue
        if intents and not set(intents).intersection(entry["intents"]):
            continue
        if kinds and entry["kind"] not in kinds:
            continue
        yield entry


def rank(
    index: Dict[str, Any],
    query: str,
    domains: Sequence[str],
    sections: Sequence[str],
    intents: Sequence[str],
    kinds: Sequence[str],
) -> List[Tuple[int, Dict[str, Any]]]:
    variants = expand_query(query, index["aliases"])
    ranked = [
        (max(score(entry, variant) for variant in variants), entry)
        for entry in filtered(index["entries"], domains, sections, intents, kinds)
    ]
    ranked = [item for item in ranked if item[0] > 0]
    ranked.sort(key=lambda item: (-item[0], item[1]["id"]))
    return ranked


def compact_entry(
    entry: Dict[str, Any], sources_by_id: Dict[str, Dict[str, Any]]
) -> str:
    lines = [
        f"### {entry['expression']}",
        f"`{entry['id']}` · {entry['kind']} · {', '.join(entry['domains'])}",
        "",
        entry["meaning"],
        "",
        f"**Use:** {entry['guidance']}",
        "",
        f"**Avoid:** {entry['avoid']}",
        "",
        f"**Pattern:** {entry['examples'][0]}",
    ]
    if entry["source_ids"]:
        links = ", ".join(
            f"[{source_id}]({sources_by_id[source_id]['url']})"
            for source_id in entry["source_ids"]
        )
        lines.extend(["", f"**Verify:** {links}"])
    return "\n".join(lines)


def normalize_values(
    values: Sequence[str], taxonomy: Dict[str, Any], field: str
) -> List[str]:
    aliases = taxonomy.get("filter_aliases", {}).get(field, {})
    taxonomy_key = {
        "domain": "domains",
        "section": "sections",
        "intent": "intents",
        "kind": "kinds",
    }[field]
    allowed = set(taxonomy[taxonomy_key])
    normalized = []
    for value in values:
        mapped = aliases.get(value, aliases.get(value.lower(), value))
        if mapped not in allowed:
            raise SystemExit(
                f"unknown --{field} value {value!r}; expected one of "
                f"{', '.join(sorted(allowed))}"
            )
        normalized.append(mapped)
    return normalized


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Retrieve a small number of records from the bundled corpus index."
    )
    parser.add_argument("query", nargs="?", default="")
    parser.add_argument("--id", dest="entry_id")
    parser.add_argument("--domain", action="append", default=[])
    parser.add_argument("--section", action="append", default=[])
    parser.add_argument("--intent", action="append", default=[])
    parser.add_argument("--kind", action="append", default=[])
    parser.add_argument("--limit", type=int, default=6)
    parser.add_argument(
        "--format", choices=["markdown", "ids", "json"], default="markdown"
    )
    args = parser.parse_args()
    if args.limit < 1 or args.limit > 20:
        parser.error("--limit must be between 1 and 20")

    index = load_index()
    taxonomy = index["taxonomy"]
    for field in ("domain", "section", "intent", "kind"):
        setattr(args, field, normalize_values(getattr(args, field), taxonomy, field))
    sources_by_id = {source["id"]: source for source in index["sources"]}

    if args.entry_id:
        selected = [
            entry for entry in index["entries"] if entry["id"] == args.entry_id
        ]
        if not selected:
            print(f"unknown entry id: {args.entry_id}")
            return 2
    else:
        ranked = rank(
            index,
            args.query,
            args.domain,
            args.section,
            args.intent,
            args.kind,
        )
        selected = [entry for _, entry in ranked[: args.limit]]
        if not selected:
            print("no matching entries")
            return 2

    if args.format == "ids":
        print("\n".join(entry["id"] for entry in selected))
    elif args.format == "json":
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    else:
        print(
            "\n\n".join(
                compact_entry(entry, sources_by_id) for entry in selected
            )
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
