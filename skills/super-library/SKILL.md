---
name: super-library
description: Retrieve source-traceable terminology, definitions, sentence patterns, rebuttal moves, and translation guidance for professional AI/ML research writing. Use for drafting or revising papers, abstracts, related work, methods, experiments, limitations, reviewer rebuttals, and Chinese–English technical translations, especially in world models, reinforcement learning, embodied AI, robot learning, and vision-language-action models.
---

# Super Library

Use the corpus to constrain terminology and rhetorical choices while producing
original prose. Treat it as a language and paper-discovery aid, never as evidence.

## Select the lowest-cost retrieval path

First classify mode (`paper`, `rebuttal`, or `translation`), technical domain,
topic family when applicable, target section, communicative intent, and evidence
boundary.

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

Use `route "<query>" --domain <domain> --section <section>` when card URLs or
catalog routes are needed. Use `show <entry-id>` for one complete record.

### Installed standalone skill

Read `references/core.md` once. Do not read `references/index.json`; query it with
the bundled script so only a few records enter context. Run these commands from
the installed skill directory:

```bash
python3 scripts/lookup.py "<rhetorical need>" \
  --domain <domain> --section <section> --intent <intent> --limit 4
python3 scripts/lookup.py "<technical concept or Chinese term>" \
  --domain <domain> [--topic <topic>] --kind term --limit 4
```

Omit `--kind` for a mix of terms and definitions. Use `--id <entry-id>` to load
one known record.

### Link-only access

Open the immutable
[`agent-index.md`](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md).
Follow its order: universal core, one section catalog, one domain hub, at most one
topic catalog, then 3–8 cards.
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

- Read [paper.md](references/paper.md) for paper sections and Related Work.
- Read [rebuttal.md](references/rebuttal.md) for reviewer responses.
- Read [translation.md](references/translation.md) for Chinese–English translation.
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
- Do not present corpus definitions as quotations or copy paper sentences.
- Treat the 300-paper evidence maps as citation-navigation aids, not default
  writing context; open one only when a literature claim requires verification.
- Prefer an exact, modest claim over impressive but unsupported wording.
