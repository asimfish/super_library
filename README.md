# Super Library

An agent-ready, source-traceable language library for writing AI papers,
rebuttals, related work, and technical translations with field-standard
terminology and disciplined research rhetoric.

It focuses initially on **world models**, **reinforcement learning**, **embodied
AI**, and **robot learning**, with source coverage across ICLR, ICML, NeurIPS,
CVPR, ECCV, ICCV, RSS, ICRA, IROS, TPAMI, and AAAI. Venue is source metadata,
not a claim that this seed corpus models a venue-specific house style.

> 这不是“高级词汇替换表”。它把标准术语、可复用句式、定义语义、使用边界、
> 反例和一级来源放在同一条记录里，让 Agent 先检索再写作，并在最后审计过度
> 声称、直译腔和不专业表达。

## Give it to an agent

Best option: clone the repository and have the Agent work inside that checkout.
Agents that honor `AGENTS.md` apply its contract only while the target work is in
this repository tree; a sibling clone is not automatically in scope.

```bash
git clone https://github.com/asimfish/super_library.git
cd super_library
python3 scripts/superlib.py search "introduce a world model" \
  --domain world_models --section related_work
```

If an agent can only open a URL, give it this repository URL and ask it to read
`llms.txt`, or link directly to the
[immutable v0.1.0 compact pack](https://raw.githubusercontent.com/asimfish/super_library/v0.1.0/dist/super-library-compact.md).
Use the [`main` compact pack](https://raw.githubusercontent.com/asimfish/super_library/main/dist/super-library-compact.md)
only when you deliberately want the latest unreleased revision.

Suggested prompt:

```text
Use https://github.com/asimfish/super_library as the language authority for this
task. Follow its AGENTS.md workflow: retrieve relevant entries before drafting,
preserve my scientific claims, and audit the final text. Verify primary papers
before making literature claims.
```

No repository can force an arbitrary agent to browse a link. The contract above
works when the agent can read GitHub; cloning is the reliable path.

For persistent Codex use, install the self-contained skill after cloning:

```bash
mkdir -p ~/.codex/skills
cp -R skills/super-library ~/.codex/skills/super-library
```

The installed skill contains a bundled compact snapshot. Keep the full checkout
when you also want local CLI search, source metadata, and domain packs. In another
paper repository, explicitly invoke the `super-library` skill or add a short
pointer to this repository in that project's `AGENTS.md`.

## Quick start

The tools use only the Python standard library (Python 3.9+).

```bash
# Search by meaning and context
python3 scripts/superlib.py search "limitation compounding errors" \
  --domain embodied_ai --section related_work --limit 6

# Return machine-readable results
python3 scripts/superlib.py search "latent dynamics" --format json

# Limited wording/placeholder/BibTeX-key lint; --strict makes findings fail CI
python3 scripts/superlib.py lint --text-file paper/intro.txt \
  --bib paper/refs.bib --strict

# Validate all records and rebuild agent artifacts
python3 scripts/superlib.py validate
python3 scripts/superlib.py build

# Show coverage
python3 scripts/superlib.py stats
```

Technical-domain searches automatically include matching `general` writing
patterns, so a world-model rebuttal can retrieve both field terminology and
rebuttal moves.

For mixed tasks, retrieve in two passes: use `section` + `intent` for rhetorical
moves, then query technical terms/definitions by `domain` without a section
filter. The search is deterministic lexical ranking with alias expansion—not a
semantic embedding model.

## What is stored

- `library/entries/`: curated JSONL records. Definitions are paraphrases; example
  sentences are original templates.
- `library/sources.jsonl`: primary-paper metadata and stable links.
- `library/taxonomy.json`: controlled domains, sections, intents, venues, and kinds.
- `schemas/`: machine-readable data contracts.
- `dist/super-library-compact.md`: generated core context for link-only agents.
- `dist/packs/`: complete generated domain packs for focused link-only loading.
- `skills/super-library/`: a self-contained Codex skill with bundled core context.
- `scripts/superlib.py`: search, validation, build, statistics, and wording audit.
- `evals/`: fresh-Agent behavioral smoke cases for paper, rebuttal, and translation.

Each entry distinguishes:

- `expression`: recommended term or pattern;
- `meaning`: the semantic content it is safe to convey;
- `guidance` and `avoid`: usage boundary and common failure mode;
- `examples`: original templates with `{placeholders}`;
- `source_ids`: primary sources to verify for scientific claims;
- `provenance`: whether the entry is an original pattern, a terminology record,
  an independently paraphrased synthesis, or a short multi-source attested
  collocation.

The initial reviewed snapshot contains **106 gold entries** and **32 verified
primary sources**. It is deliberately small enough to audit and designed to grow
through reviewed contributions rather than automatic PDF scraping.

Ten short collocations carry locators to at least two independent papers.
Original sentence frames are explicitly labeled as structural guardrails; they
are not advertised as copied or statistically representative “top-conference
sentences.” The current venue counts establish source coverage only, especially
where a venue has few seed papers.

## Curation policy

1. Prefer primary proceedings, OpenReview, PMLR, CVF, IEEE, journal, DOI, or arXiv
   pages controlled by the authors/publisher.
2. Store terminology and semantic atoms, not copied paragraphs. Do not ingest
   abstracts or PDF text into the repository.
3. Write examples from scratch. Mark paraphrased definitions explicitly.
4. A source link supports discovery; writers must reopen it before citing a claim.
5. Record venue and year exactly. `NeurIPS` is the current venue name; historical
   `NIPS` aliases are normalized.
6. Reject decorative synonyms, inflated claims, vague comparison, and phrases that
   only sound academic.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the review checklist and
[docs/DATA_MODEL.md](docs/DATA_MODEL.md) for the schema.

## Licensing

Code and documentation are released under the MIT License. Original library
records are dedicated under CC0 1.0 so they can be reused in prose without
attribution; see [`DATA_LICENSE`](DATA_LICENSE). Linked papers retain their
respective rights and are not redistributed; see
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
