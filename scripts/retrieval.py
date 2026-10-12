"""Shared, I/O-free positive lexical matching for both retrieval clients."""

from __future__ import annotations

import re
from typing import Any, Mapping

WORDS = re.compile(r"[a-z0-9]+")


def exact_positive_match(entry: Mapping[str, Any], query: str) -> bool:
    """Prefer a complete concept name, never a warning or a negative example.

    Hyphen/space differences are harmless here; general query expansion remains
    the caller's responsibility. This is an ordering predicate, not a new
    numeric weight, embedding model, or semantic correctness claim.
    """
    normalized = " ".join(WORDS.findall(query.lower()))
    if not normalized:
        return False
    profile = entry.get("lexical_profile", {})
    collocations = profile.get("collocations", []) if isinstance(profile, dict) else []
    positive = [entry.get("expression", ""), *collocations]
    return any(isinstance(text, str)
               and normalized == " ".join(WORDS.findall(text.lower()))
               for text in positive)


def explicitly_scoped_general(entry: Mapping[str, Any]) -> bool:
    """A general record has reviewed technical applicability, not just rhetoric."""
    domains = set(entry.get("domains", []))
    return "general" in domains and bool(domains - {"general"})
