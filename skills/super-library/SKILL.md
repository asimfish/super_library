---
name: super-library
description: Retrieve source-traceable terminology, definitions, sentence patterns, rebuttal moves, and translation guidance for professional AI/ML research writing. Use for drafting or revising papers, abstracts, related work, methods, experiments, limitations, reviewer rebuttals, and Chinese–English technical translations, especially in world models, reinforcement learning, embodied AI, and robot learning.
---

# Super Library

Use the corpus to constrain terminology and rhetorical choices while producing
original prose. Treat it as a language and paper-discovery aid, never as evidence.

## Workflow

1. Determine:
   - mode: `paper`, `rebuttal`, or `translation`;
   - domain from `library/taxonomy.json` when the full checkout is available,
     otherwise from the focused domains described in the bundled compact context;
   - target section and communicative intent;
   - evidence boundary: facts, citations, numbers, and claims supplied or verified.
2. From the repository root, retrieve before drafting. Run separate rhetorical
   and technical queries when both are needed:

   ```bash
   python3 scripts/superlib.py search "<rhetorical need>" \
     --domain <domain> --section <section> --intent <intent> --limit 6
   python3 scripts/superlib.py search "<technical concept or Chinese term>" \
     --domain <domain> --kind term --limit 6
   ```

   Omit `--kind` for a mix of terms and definitions. Run multiple focused queries
   when the task contains distinct concepts. Use
   `show <entry-id>` to inspect one record and its sources.
3. Draft from the user's scientific propositions. Prefer relevant
   `attested_collocation` records; use `original_pattern` records as structural
   guardrails. Adapt slot-based examples; never concatenate examples into a
   paragraph.
4. For definitions, method descriptions, historical statements, comparisons, or
   Related Work, open the primary links returned by the CLI and verify each claim.
   Insert `[CITATION NEEDED: <source-id>]` rather than inventing a citation.
5. Run the limited wording lint:

   ```bash
   python3 scripts/superlib.py audit --text-file <draft>
   ```

   It checks risky wording, corpus anti-patterns, unresolved placeholders, and
   optional BibTeX keys. Manually check terminology consistency, scientific claim
   scope, source overlap, numbers, negation, modality, comparison fairness,
   citation coverage, and translation fidelity.

If repository scripts are unavailable, first read the bundled
`references/compact.md`. If it is absent, read the immutable raw compact pack at
`https://raw.githubusercontent.com/asimfish/super_library/v0.1.0/dist/super-library-compact.md`.
If neither the CLI nor compact pack can be loaded, say that the library was not
loaded; do not claim to have used it.

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
- Prefer an exact, modest claim over impressive but unsupported wording.
