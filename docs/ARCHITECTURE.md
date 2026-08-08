# Retrieval architecture

Super Library separates canonical records from generated Agent views. The design
goal is bounded context: adding corpus entries must not force every Agent to read
more text.

## Canonical layer

```text
library/
├── entries/*.jsonl       reviewed language and concept records
├── sources.jsonl         primary-source metadata
├── topics.json           controlled technical topic families
├── collections.json      audited paper-collection contracts
├── corpus_report.json    explicit abstract-analysis exceptions and audit policy
├── taxonomy.json         versions and controlled vocabularies
├── aliases.json          Chinese/common query expansion
├── core_ids.json         universal high-risk records
├── compact_ids.json      legacy single-file selection
├── writing_guides.json   bounded section and table protocols
├── task_routes.json      bounded task/domain fast-path bundles
├── table_templates.json  reviewed LaTeX table-asset registry
├── studies/*.json        aggregate calibration audits; no paper prose
└── watchlist.json        wording-lint rules
```

Schemas and business rules validate the canonical layer. Generated files are
never authoritative. `schemas/catalog.schema.json` and `schemas/router.schema.json`
also validate the selective indexes during every build.

## Progressive disclosure

| Level | Artifact | Purpose | Default quantity |
|---|---|---|---|
| 0 | `llms.txt` | Find the pinned entrypoint | one tiny file |
| 1 | `dist/agent-index.md` | Choose routes | one file |
| fast path | `dist/routes/<task>.md` | Load one precomposed task/domain bundle | exactly one, when matched |
| 2 | `dist/core.md` | Load universal evidence and wording constraints | once |
| protocol | `dist/guides/index.md` | Select a section/table protocol | one tiny index |
| protocol | `dist/guides/<guide-id>.md` | Structure one paper section/rebuttal/translation/table | at most one |
| 3 | `dist/catalogs/sections/*.md` | Select rhetorical moves | at most one |
| 3 | `dist/catalogs/domains/*.md` | Choose a technical topic | at most one small hub |
| 4 | `dist/catalogs/topics/*.md` | Select technical concepts | at most one |
| 5 | `dist/cards/**/*.md` | Load complete records | 3–8 cards |
| evidence | `dist/evidence/topics/*.md` | Verify a literature claim in primary papers | only on demand |
| audit | `dist/evidence/source-analysis.*` | Inspect per-paper analysis depth | never by default |
| asset | `dist/templates/tables/*.tex` | Start a standards-aware experiment table | one copied asset |

Catalogs contain labels and routing metadata, not complete guidance. Domain
catalogs are small hubs whose size does not grow with every entry. Cards contain
meaning, usage constraints, anti-patterns, examples, provenance, and sources.
`dist/router.json` records paths and measured byte sizes for automated clients.
Section protocols are separate from sentence cards: a protocol defines required
inputs, functional moves, internal templates, and verification, while cards
supply a few reusable expressions. This prevents all structural guides from
entering every writing context.

The generated task routes are a bounded one-file alternative to levels 2–5 for
common combinations of domain and section. Each route contains only the relevant
core constraints, one protocol when required, and a small reviewed entry set.
Every route is measured during the build and must remain below 24,000 characters.
An Agent should stop after loading a matching task route unless it needs primary
evidence or a concept that the route does not cover.

The complete `dist/index.json`, legacy compact file, and full domain packs are
compatibility or offline-machine artifacts. They are explicitly excluded from the
default Agent route.

The 300-paper recent collection is also excluded from default writing context.
Each paper maps to one controlled topic family, and each topic has a separate
evidence map. Multiple papers can support one normalized expression card; source
coverage therefore grows without forcing the number of near-duplicate cards to
grow linearly. A generated per-paper ledger makes four states explicit: metadata
membership, bounded abstract analysis, full-paper structural sampling, and direct
links from normalized records. See
[`ADR-001`](adr/ADR-001-curated-cards-and-analysis-ledger.md).

## Local retrieval

Local Agents should avoid Markdown traversal:

```bash
python3 scripts/superlib.py bundle \
  --rhetoric-query "<rhetorical move>" \
  --technical-query "<concept>" \
  --domain <domain> [--topic <topic>] --section <section> --intent <intent>
```

Append `--guide <guide-id>` when the task needs one section, rebuttal, translation,
analysis, or table protocol.
The two searches are intentionally different. Rhetorical filtering uses section
and intent; technical filtering omits them so a rebuttal can still retrieve a
method definition. `--max-chars` bounds the emitted Markdown.

`route` returns URLs and recommended card IDs without loading the card bodies.
For structured paper sections, rebuttals, and translations it also recommends one guide;
experiment-table queries route to the matching specialized protocol. `guide`
lists or renders one protocol without traversing all guide files.
For a supported task/domain pair, `route` also returns one `task_pack` path that
can replace manual catalog traversal. `template --list` identifies reviewed
LaTeX experiment-table assets, and `template <id> --output <path>` copies exactly
one source asset without rendering or rewriting it.
`search --format ids` is the smallest direct retrieval mode.

## Standalone skill

The skill bundles `core.md`, the one-file routes, section protocols, LaTeX table
assets, `router.json`, and the complete JSON index on disk. Its
`scripts/lookup.py` reads the machine index and emits only a limited result set.
The JSON index is a tool input, not a reference that the Agent should read.

## Build invariants

Tests enforce:

- deterministic generated artifacts;
- a small Agent index and universal core;
- one bounded task route for every declared fast-path combination;
- exactly one bounded protocol route and a separately bounded protocol index;
- validated, byte-identical LaTeX table assets in the distribution and skill;
- bounded catalog and card sizes;
- exactly controlled collection membership, venue/year boundaries, and topic maps;
- one deterministic analysis-depth record for every core paper;
- duplicate source titles, source URLs, and normalized expressions are rejected;
- one card for every published entry;
- valid card links and manifest hashes;
- two-pass retrieval even when the target section is `rebuttal`;
- deterministic retrieval cases covering domain, topic, section, intent, guide,
  and task-route selection;
- identical machine snapshots in the root distribution and standalone skill.
