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
- `dist/catalogs/sections/*.md`: thin rhetoric catalogs.
- `dist/catalogs/domains/*.md`: thin technical-concept catalogs.
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

Selection for the universal core is controlled by `library/core_ids.json`;
`library/compact_ids.json` controls only the legacy compatibility pack. Never edit
`dist/` or generated skill snapshots by hand.
