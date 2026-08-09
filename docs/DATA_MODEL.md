# Data model

`library/entries/*.jsonl` is the canonical corpus. One physical line is one JSON
record, which keeps diffs reviewable and permits streaming.

## Entry

Required fields:

| Field | Meaning |
|---|---|
| `id` | Stable lowercase identifier |
| `kind` | `term`, `definition`, `phrase`, `sentence_pattern`, `usage_note`, or `anti_pattern` |
| `domains` | One or more controlled technical domains |
| `sections` | Paper/rebuttal contexts where the entry is useful |
| `intents` | Communicative functions such as `define`, `contrast`, or `respond` |
| `expression` | Preferred surface form or reusable pattern |
| `meaning` | The semantic content the expression is safe to carry |
| `guidance` | Scope, grammar, evidence, and placement constraints |
| `avoid` | A concrete misuse or weaker alternative |
| `examples` | Original templates; braces denote slots |
| `source_ids` | Primary sources for terminology or concepts |
| `tags` | Search aliases |
| `topic_families` | Controlled technical clusters used for bounded routing |
| `provenance` | Authorship/transformation classification |
| `quality` | Review tier, status, and date |

`source_ids` are mandatory for definitions and technical terminology. A source
does not license a claim automatically: reopen the paper and verify the exact
claim in context.

## Provenance

- `original_pattern`: sentence pattern written for this project.
- `attested_collocation`: short research collocation observed in at least two
  independent primary papers, with a locator for each attestation.
- `terminology`: field-standard term indexed from primary literature.
- `paraphrased_synthesis`: independently written semantic synthesis across the
  listed sources.

The repository intentionally has no `quote` provenance type.

## Quality

- `gold + reviewed`: language and technical meaning reviewed; the only default
  search and generated-pack tier.
- `silver + source_checked`: useful and source-checked, available only with an
  explicit CLI flag.
- `bronze + candidate`: unreviewed candidate, available only with an explicit
  CLI flag and always excluded from generated packs.

## Generated artifacts

`python3 scripts/superlib.py build` deterministically creates:

- `dist/agent-index.md`: smallest link-only route table and loading contract.
- `dist/core.md`: universal high-risk writing and evidence rules.
- `dist/guides/index.md`: thin route table for section and table protocols.
- `dist/guides/<guide-id>.md`: one bounded section, rebuttal, translation,
  results-analysis, or table-construction protocol.
- `dist/catalogs/sections/*.md`: thin rhetoric catalogs.
- `dist/catalogs/domains/*.md`: small technical-domain hubs.
- `dist/catalogs/topics/*.md`: bounded technical-concept catalogs.
- `dist/evidence/topics/*.md`: on-demand maps from a topic to recent primary papers.
- `dist/evidence/source-analysis.{md,jsonl}`: aggregate and per-paper analysis-depth
  audit, excluded from default writing context.
- `dist/evidence/promotion-queue.{md,jsonl}`: bounded, scored maintainer queue for
  normalization and deduplication review; never writing evidence.
- `dist/cards/<domain>/<entry-id>.md`: one complete record per loadable card.
- `dist/router.json` and `dist/catalog.jsonl`: machine-readable routing metadata.
- `dist/index.json`: complete machine index for scripts; do not paste it into an
  Agent context.
- `dist/super-library-compact.md` and `dist/packs/<domain>.md`: exhaustive
  compatibility artifacts, not default Agent entrypoints.
- `dist/stats.json`: coverage counts.
- `dist/manifest.json`: release metadata, immutable URLs, source-of-truth files,
  and SHA-256 hashes for generated artifacts.
- `skills/super-library/references/{agent-index.md,core.md,index.json,router.json}`:
  the standalone skill snapshot. Its lookup script queries `index.json` without
  loading that file into model context.
- `skills/super-library/references/guides/*.md`: identical generated protocol
  snapshots; an Agent reads at most one for the current task.

Selection for the universal core is controlled by `library/core_ids.json`;
`library/compact_ids.json` controls only the legacy compatibility pack. Never edit
`dist/` or generated skill snapshots by hand.

## Source collections

`library/sources.jsonl` stores paper metadata once. Optional `domains`,
`topic_families`, and `collections` fields provide controlled indexing.
`library/collections.json` defines auditable boundaries such as allowed years,
venues, domains, and minimum paper counts. For `recent-five-year-core`, validation
requires published papers from 2021–2025, one of seven target venues, and at least
one topic family.

Paper records and expression records are intentionally many-to-many. A topic may
contain dozens of papers but only a few normalized terminology, definition, usage,
or Related Work cards. This prevents repeated phrasing from bloating Agent context.

`library/corpus_report.json` records collection verification and aggregate phrase
analysis without retaining source abstracts. It makes partial analysis explicit
instead of implying that every linked paper was text-mined.

## Writing guides and section study

`library/writing_guides.json` stores protocols separately from expression cards.
Every guide has a stable ID, type, target section, required inputs, functional
moves, internal template variants, verification checks, avoid rules, and links to
related card IDs. Guides never supply scientific facts.

`library/studies/section_writing_2026-07.json` records the source IDs and aggregate
document-level observations for the 40-paper full-text calibration sample.
Validation checks its source membership and domain, venue, and year counts. Raw
PDF text and extracted sentences are not stored.

## Writing evaluation and coverage policy

`evals/writing.json` stores blind requests, supplied facts, an evidence boundary,
routing expectations, deterministic regular-expression checks, and a separate
manual rubric. `eval-writing --case <id>` does not expose the checks or rubric.
A machine pass establishes only the declared objective invariants.

`library/coverage_policy.json` stores roadmap goals, ranking weights, the generated
queue bound, and allowed review outcomes. Goals do not make validation fail merely
because they have not yet been reached. Queue generation consumes the per-paper
analysis ledger and never changes canonical entries automatically.
