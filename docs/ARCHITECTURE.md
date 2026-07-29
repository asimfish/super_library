# Retrieval architecture

Super Library separates canonical records from generated Agent views. The design
goal is bounded context: adding corpus entries must not force every Agent to read
more text.

## Canonical layer

```text
library/
├── entries/*.jsonl       reviewed language and concept records
├── sources.jsonl         primary-source metadata
├── taxonomy.json         versions and controlled vocabularies
├── aliases.json          Chinese/common query expansion
├── core_ids.json         universal high-risk records
├── compact_ids.json      legacy single-file selection
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
| 2 | `dist/core.md` | Load universal evidence and wording constraints | once |
| 3 | `dist/catalogs/sections/*.md` | Select rhetorical moves | at most one |
| 3 | `dist/catalogs/domains/*.md` | Select technical concepts | at most one |
| 4 | `dist/cards/**/*.md` | Load complete records | 3–8 cards |

Catalogs contain labels and routing metadata, not complete guidance. Cards contain
meaning, usage constraints, anti-patterns, examples, provenance, and sources.
`dist/router.json` records paths and measured byte sizes for automated clients.

The complete `dist/index.json`, legacy compact file, and full domain packs are
compatibility or offline-machine artifacts. They are explicitly excluded from the
default Agent route.

## Local retrieval

Local Agents should avoid Markdown traversal:

```bash
python3 scripts/superlib.py bundle \
  --rhetoric-query "<rhetorical move>" \
  --technical-query "<concept>" \
  --domain <domain> --section <section> --intent <intent>
```

The two searches are intentionally different. Rhetorical filtering uses section
and intent; technical filtering omits them so a rebuttal can still retrieve a
method definition. `--max-chars` bounds the emitted Markdown.

`route` returns URLs and recommended card IDs without loading the card bodies.
`search --format ids` is the smallest direct retrieval mode.

## Standalone skill

The skill bundles `core.md`, `router.json`, and the complete JSON index on disk.
Its `scripts/lookup.py` reads the machine index and emits only a limited result
set. The JSON index is a tool input, not a reference that the Agent should read.

## Build invariants

Tests enforce:

- deterministic generated artifacts;
- a small Agent index and universal core;
- bounded catalog and card sizes;
- one card for every published entry;
- valid card links and manifest hashes;
- two-pass retrieval even when the target section is `rebuttal`;
- identical machine snapshots in the root distribution and standalone skill.
