# ADR-007: Positive lexical matching and explicit reporting domains

## Status

Accepted for reversible feature implementation, 2026-10-12. Based on `9890df2`;
no merge, release, model launch or paid endpoint use is implied.

## Evidence and constraints

Eight technical-query probes found that `matched interaction budget` ranked its
sample-efficiency record fourth, and `model query latency` ranked a generic
3D-VLA definition above the latency note. Positive collocations stored in the
new lexical profiles were not part of matching. A confidence-interval query had
no domain technical candidate, and percentage-change queries had no dedicated
absolute-versus-relative reporting note.

Keep the existing two-pass workflow, one selected protocol and serialized
character budgets. Metadata and test counts are not effectiveness evidence.
General rhetoric must not consume the technical pass merely because a domain
query shares frequent words with it. Negative dictionary examples must not
become positive aliases. Corpus facts remain outside model evidence.

## Candidates

### A: Include all general records and increase keyword weights

Would recover some reporting language, but also admits generic style guidance
and arbitrary word-repetition effects. Separate fixes in repository and portable
lookup can drift. Requires numerical weight tuning without relevance evidence.

### B: Prefer complete positive matches; explicitly scope reporting notes

Exact expression or positive-collocation matches precede keyword-only matches;
existing scoring breaks ties. Use existing controlled `domains` metadata for
reporting terms that genuinely apply across AI domains. Correct the topic gate
so an explicitly applicable multidomain general record is not later discarded.
Keep unscoped general rhetoric excluded from the technical pass.

## Decision and interface

Choose B. `scripts/retrieval.py` exposes a pure
`exact_positive_match(entry, query) -> bool`. It normalizes harmless hyphen/space
differences, reads only `expression` and positive `lexical_profile.collocations`,
and never reads contrasts, `avoid`, or `not_equivalent_to`. It performs no I/O,
model calls, network, caching, or learned reranking. It is shared verbatim with
the portable skill; root and portable consumers apply the same match precedence.

Keep existing keyword scoring and controlled filters. No new numeric tuning knob,
embedding index, vocabulary whitelist or required context tier is introduced.
Domain assignments are maintainer decisions validated against taxonomy, not an
automatic claim that every term has identical semantics in every field.

## Content and validation boundary

Add only nonredundant confidence-interval and percentage-point usage notes;
enrich existing latency, generalization, return, objective-mismatch and metric
records rather than multiplying synonyms. Independently verify primary sources
for scientific concepts. A published classical evaluation source may be added
outside the frozen 300-paper collection; do not inflate its coverage count.

Tests must reproduce the old retrieval defects, reject negative-alias leakage,
retain domain/topic exclusion, prove root/portable parity, and keep current
budget and old retrieval/writing contracts. New diagnostic queries are not
gold paragraphs or independent evidence of better prose. Actual generation and
blind rating remain separate and require an available authorized consumer.

Revisit if exact collocations overshadow the task's real concept or new profiles
crowd out technical records. Record before/after probe outcomes and adverse cases.
