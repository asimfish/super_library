---
name: super-library
description: Retrieve source-traceable terminology, definitions, sentence patterns, and bounded section protocols for professional AI/ML research writing. Use for drafting or revising abstracts, introductions, related work, methods, experiments, result analyses, tables, limitations, reviewer rebuttals, and Chinese–English technical translations, especially in world models, reinforcement learning, embodied AI, robot learning, and vision-language-action models.
---

# Super Library

Use the corpus to constrain terminology and rhetorical choices while producing
original prose. Treat it as a language and paper-discovery aid, never as evidence.

## Select the lowest-cost retrieval path

First classify mode (`paper`, `rebuttal`, or `translation`), technical domain,
topic family when applicable, target section, communicative intent, and evidence
boundary. For a structured section, rebuttal, translation, analysis, or table
task, also select exactly one protocol; do not load every protocol.
Never open `library/writing_guides.json` wholesale to make that choice; use
`route`, `guide --list`, or one known `guide <guide-id>` instead.

### Full repository checkout

Generate one bounded context bundle. Keep rhetoric and terminology as separate
queries:

```bash
python3 scripts/superlib.py bundle \
  --rhetoric-query "<communicative need>" \
  --technical-query "<technical concept or Chinese term>" \
  --domain <domain> [--topic <topic>] --section <section> --intent <intent> \
  --limit 4 --max-chars 24000
```

Add `--guide <guide-id>` whenever the task needs a section or table protocol.
Use `route "<query>" --domain <domain> --section <section>` when card URLs or
catalog routes are needed; it recommends one relevant protocol. Use
`guide --list`, `guide <guide-id>`, or `show <entry-id>` for a known record.
For an experimental table, run `template --list`, then
`template <template-id> --output <table.tex>` and replace every `SL_*` token.

### Installed standalone skill

First read `references/routes/index.md`. If one route matches the domain and
section, read that single route and stop. Otherwise read `references/core.md`
once. Do not read `references/index.json`; query it with the bundled script so
only a few records enter context. Run these commands from the installed skill
directory:

```bash
python3 scripts/lookup.py "<rhetorical need>" \
  --domain <domain> --section <section> --intent <intent> --limit 4
python3 scripts/lookup.py "<technical concept or Chinese term>" \
  --domain <domain> [--topic <topic>] --kind term --limit 4
```

Omit `--kind` for a mix of terms and definitions. Use `--id <entry-id>` to load
one known record. On the fallback path, for a structured section, rebuttal, or
translation task, read `references/guides/index.md`, then exactly one matching guide.
The guide contains links to sentence-card IDs; retrieve only the cards needed for
the current prose.
For a table task, copy exactly one matching file from `assets/tables/`; do not
load all table assets into context.

### Link-only access

Open the immutable
[`agent-index.md`](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md).
First check its one-file task-route index. If a route matches the domain and
section, read that single route and stop. Otherwise follow the fallback order:
universal core, one section catalog, one domain hub, at most one topic catalog,
then 3–8 cards. Insert one task-specific guide before the catalogs whenever a
matching protocol exists.
Do not load `index.json`, the legacy compact pack, or full domain packs by default.
If neither local retrieval nor the index can be loaded, state that Super Library
was not used.

## Draft and verify

1. Draft from the user's scientific propositions. Prefer attested collocations;
   use original patterns as structural guardrails. Adapt all placeholders.
2. For definitions, mechanisms, history, comparisons, or Related Work, reopen the
   primary links and verify each claim. Insert
   `[CITATION NEEDED: <source-id>]` rather than inventing a citation.
3. In a full checkout, run the limited wording lint:

   ```bash
   python3 scripts/superlib.py lint --text-file <draft> --bib <refs.bib>
   ```

   Manually check terminology, claim scope, source overlap, numbers, negation,
   modality, comparison fairness, citation coverage, and translation fidelity.

## Route by task

Use these files only on the fallback path when no one-file task route matches.

- Read [paper.md](references/paper.md) for paper sections and Related Work.
- Read [guides/abstract.md](references/guides/abstract.md) for an Abstract.
- Read [guides/introduction.md](references/guides/introduction.md) for an
  Introduction.
- Read [guides/related_work.md](references/guides/related_work.md),
  [guides/method.md](references/guides/method.md),
  [guides/limitations.md](references/guides/limitations.md), or
  [guides/conclusion.md](references/guides/conclusion.md) for the matching section.
- Read [guides/experiments.md](references/guides/experiments.md) for a complete
  experiment section, or select one specialized analysis/table guide through
  [guides/index.md](references/guides/index.md). In the complete experiment
  protocol, apply only the matching RL, world-model, embodied/robot, or VLA
  reporting overlay.
- Read [guides/rebuttal.md](references/guides/rebuttal.md) together with the
  compact [rebuttal workflow](references/rebuttal.md) for reviewer responses.
- Read [guides/translation.md](references/guides/translation.md) together with the
  compact [translation workflow](references/translation.md) for Chinese–English translation.
- Read [evidence.md](references/evidence.md) whenever definitions, literature
  claims, comparisons, or citations are involved.

For mixed tasks, combine the relevant workflows and apply the stricter constraint.
For example, a translated rebuttal must preserve source meaning and answer the
reviewer directly.

## Non-negotiable constraints

- Preserve technical meaning, equations, quantities, negation, uncertainty, and
  citation placement.
- Use `state-of-the-art` only after current external verification under a named
  benchmark, metric, protocol, and comparison set.
- Never invent experiments, results, baselines, author names, venues, years,
  BibTeX keys, or manuscript locations.
- In experiments, bind claims to research questions and evidence; disclose metric
  direction, units, denominator, aggregation, uncertainty, selection, baseline
  provenance, and material resource differences.
- Make tables interpretable without prose. Never encode missing as zero, use
  color as the only cue, or emphasize a best result across incomparable protocols.
- State observations before interpretations and preserve exceptions, trade-offs,
  null results, and failure boundaries.
- Do not present corpus definitions as quotations or copy paper sentences.
- Treat the 300-paper evidence maps as citation-navigation aids, not default
  writing context; open one only when a literature claim requires verification.
- Prefer an exact, modest claim over impressive but unsupported wording.
