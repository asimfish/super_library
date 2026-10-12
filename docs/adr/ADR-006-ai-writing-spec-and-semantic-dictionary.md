# ADR-006: AI writing specification and semantic usage profiles

## Status

Accepted for the reversible feature implementation, 2026-10-12. No merge or
release is authorized by this decision. Based on narrative revision `f8503cf`.

## Context

The user wants STE's writing-rules / dictionary distinction adapted to AI
research, with explained contrast examples and a diagram that exposes the design.
Karpathy's 2026-10-02 post motivates legible, inspectable outputs, not evidence
that STE improves conference-paper writing. The official STE rules govern
technical documentation. Neither their dictionary nor sentence ceilings are
appropriate as a universal AI-paper whitelist.

Existing owners are canonical entries, section protocols, bounded retrieval,
generated views, limited wording lint, and isolated paired evaluation. Another
writing skill, a vector database, or an independent terminology catalog would
duplicate those owners. The original workspace has unrelated pending changes;
implementation is isolated in a feature worktree.

## Candidates

### A: Expand every guide and add a second dictionary

Simple initially, but repeated rules drift across 17 guides; duplicate term IDs
break the single-source contract and large protocols displace useful records.

### B: One small rule registry plus optional profiles on existing entries

One canonical owner per term. Stable rule IDs are selected by section, summaries
are included in bounded bundles, and complete explanations are explicit reads.
Adds a small schema/module boundary and requires compatibility tests.

## Decision

Choose B. `library/writing_spec.json` owns general language/evidence rules, not
section narration. `library/writing_guides.json` still owns section protocols.
Existing `library/entries/*.jsonl` own terminology and optional `lexical_profile`
fields. Profiles express sense, part of speech, collocations, non-equivalence,
and original, fact-conditioned contrast examples; they do not certify a global
approved vocabulary. Existing records remain valid without this optional field.

Pure selection/rendering functions in `scripts/writing_spec.py` have no network,
model, secret, installation, or publication effects. `spec --list` and
`spec <section>` reveal one profile. Normal bundles receive only compact rule
summaries for their section; examples and research notes are not default context.
The complete selected spec and guide count against the existing serialized
character budget and cannot be silently truncated. Fast paths and the fallback
core carry the same relevant compact summaries; there is no extra required read.

## Impact and boundaries

- Hard constraints preserve supplied facts and evidence scope; preferences guide
  clarity. Neither class is automatically verified by a wording checker.
- No fixed sentence/paragraph ceiling, tense blacklist, synonym substitution, or
  mandatory narrative slots. Domain terms and author notation are preserved.
- Primary papers support scientific claims; the language context never does.
- Generated Markdown, JSON indexes, skill views and the diagram describe the
  same owners. SVG is the repository-native diagram; a Canvas is an interactive
  companion, not a second source of corpus data.
- Rules/profiles need schema, reference, budget, mirror and adversarial tests.
  Effectiveness still requires fresh isolated baseline/library generations and
  independent blind ratings; attractive figures and passing tests are not proof.
- Revisit if rule summaries crowd out technical records, profiles drift from
  paper terminology, or blind evaluation finds omission/template contamination.

## Sources and rights

- https://x.com/karpathy/status/2105819303471976479 (read in full through the
  public read-only FxTwitter relay; primary X page returned 403).
- https://www.asd-ste100.org/about_STE.html
- https://www.asd-ste100.org/STE_faq.html
- https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf

Independent design synthesis. ASD owns its standard; no STE dictionary, rule
text, full post, or paper text is copied into the distributable corpus.
