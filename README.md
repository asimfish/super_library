# Super Library

An agent-ready, source-traceable language library for writing AI papers,
rebuttals, related work, and technical translations with field-standard
terminology and disciplined research rhetoric.

It focuses initially on **world models**, **reinforcement learning**, **embodied
AI**, and **robot learning**, with source coverage across ICLR, ICML, NeurIPS,
CVPR, ECCV, ICCV, RSS, ICRA, IROS, TPAMI, and AAAI. Venue is source metadata,
not a claim that this seed corpus models a venue-specific house style.

Version 0.2 adds vision-language-action models, action chunking, cross-robot data
mixtures, probabilistic dynamics, model bias, distributional RL, and common
Chinese–English research-writing failure modes.

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
python3 scripts/superlib.py bundle \
  --rhetoric-query "position prior world-model methods" \
  --technical-query "probabilistic latent dynamics and model bias" \
  --domain world_models --section related_work --intent position
```

If an agent can only open a URL, give it this repository URL and ask it to read
`llms.txt`, or link directly to the small
[immutable v0.2.0 agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md).
The index routes the Agent to one universal core, at most two thin catalogs, and
only 3–8 full entry cards.

Suggested prompt:

```text
Use https://github.com/asimfish/super_library as the language authority. Read
llms.txt and use the v0.2 selective-loading workflow: core once, relevant
section/domain catalogs, then only 3–8 cards. Preserve my claims and verify
primary papers before making literature statements.
```

No repository can force an arbitrary agent to browse a link. The contract above
works when the agent can read GitHub; cloning is the reliable path.

For persistent Codex use, install the self-contained skill after cloning:

```bash
mkdir -p ~/.codex/skills
cp -R skills/super-library ~/.codex/skills/super-library
```

The installed skill contains a small core plus a machine index. Its bundled
lookup script returns only the requested records, so the large JSON index never
needs to enter model context. Keep the full checkout when you also want context
bundles, linting, source maintenance, and deterministic builds.

## Quick start

The tools use only the Python standard library (Python 3.9+).

```bash
# Get a tiny load plan and direct card links
python3 scripts/superlib.py route "action chunking feedback" \
  --domain robot_learning --section method

# Build a bounded two-pass context for one writing task
python3 scripts/superlib.py bundle \
  --rhetoric-query "acknowledge a limitation without overclaiming" \
  --technical-query "action chunking closed-loop feedback" \
  --domain robot_learning --section rebuttal --intent respond \
  --limit 4 --max-chars 24000

# Search or return IDs only
python3 scripts/superlib.py search "latent dynamics" --format ids

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

## Progressive-loading architecture

```text
llms.txt
└── dist/agent-index.md                 # routing only
    ├── dist/core.md                    # universal evidence/writing guardrails
    ├── dist/catalogs/sections/*.md     # thin rhetorical indexes
    ├── dist/catalogs/domains/*.md      # thin technical indexes
    └── dist/cards/<domain>/<id>.md     # one complete entry at a time

library/                                # canonical hand-reviewed source data
scripts/superlib.py                     # route/search/bundle/build/lint
skills/super-library/                   # standalone selective-lookup skill
dist/packs/ and legacy compact          # exhaustive compatibility artifacts
```

The generated `router.json` records byte budgets and every route. `catalog.jsonl`
is a thin machine catalog; `index.json` is the complete offline index and should
be queried by a script, not pasted into an Agent.

## What is stored

- `library/entries/`: curated JSONL records. Definitions are paraphrases; example
  sentences are original templates.
- `library/sources.jsonl`: primary-paper metadata and stable links.
- `library/taxonomy.json`: controlled domains, sections, intents, venues, and kinds.
- `library/core_ids.json`: the deliberately small universal-core selection.
- `schemas/`: machine-readable data contracts.
- `dist/agent-index.md`, `core.md`, `catalogs/`, and `cards/`: progressive Agent
  retrieval layers.
- `skills/super-library/`: a self-contained skill with a bounded lookup script.
- `scripts/superlib.py`: routing, bundle generation, search, validation, build,
  statistics, and wording lint.
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

The v0.2 reviewed snapshot contains **153 gold entries** and **41 verified primary
sources**. It is designed to grow through reviewed contributions rather than
automatic PDF scraping.

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
[docs/DATA_MODEL.md](docs/DATA_MODEL.md) for the schema. The complete loading
design and context invariants are in
[docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## Licensing

Code and documentation are released under the MIT License. Original library
records are dedicated under CC0 1.0 so they can be reused in prose without
attribution; see [`DATA_LICENSE`](DATA_LICENSE). Linked papers retain their
respective rights and are not redistributed; see
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).
