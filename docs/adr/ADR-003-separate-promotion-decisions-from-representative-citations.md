# ADR-003: Separate promotion decisions from representative citations

Status: Accepted
Date: 2026-08-11

## Context

The 300-paper core needs auditable paper-by-paper review, but normalized language
records are deliberately many-to-many and compact. A reviewed paper may confirm
that an existing definition is sufficient without being a representative source
for every statement on that card. A review may also validly find no reusable,
nonredundant language.

## Driving factors

- Record a primary-source locator and explicit outcome for every completed review.
- Keep coverage claims distinguishable from representative definition evidence.
- Remove completed no-promotion reviews from the work queue.
- Avoid increasing default card size in proportion to papers reviewed.
- Preserve deterministic, schema-validated maintenance artifacts.

## Considered options

### A. A canonical promotion-decision ledger outside Agent writing context

Store review provenance, dedup comparisons, and outcome-specific links separately.
Combine those links with representative citations only in generated coverage views.

### B. Add every reviewed paper to an existing entry's `source_ids`

This is simpler, but it makes cards and primary-source lists grow with maintenance
coverage and implies that every paper is representative evidence for the card.

### C. Create one language card for every reviewed paper

This maximizes paper-level traceability but duplicates definitions and writing
patterns, weakens retrieval precision, and makes context size grow linearly.

## Decision

Adopt option A. `library/promotion_decisions.jsonl` is canonical and uses three
outcomes: `promote_normalized_record`, `link_existing_record`, and
`record_no_promotion`. Outcome validators are registered behind a small protocol.
A promoted record must cite the reviewed source. An existing-record link is an
audit relationship only. A no-promotion decision has no linked entry, but records
which existing entries were checked for duplication.

The generated source-analysis ledger exposes representative links, promotion
links, and their union separately. The promotion queue excludes any paper with a
completed decision, including no-promotion outcomes.

## Impact

- Coverage can increase while default Agent cards remain concise.
- Maintainers can audit why a paper did or did not add a new language record.
- A direct coverage link no longer necessarily means the paper appears in a card's
  `source_ids`; generated views label both link types.
- Literature claims still require opening the primary paper. The decision ledger
  is navigation metadata, not citable evidence.
