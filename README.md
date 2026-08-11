# Super Library

An agent-ready, source-traceable language library for writing AI papers,
rebuttals, related work, and technical translations with field-standard
terminology and disciplined research rhetoric.

It focuses on **world models**, **reinforcement learning**, **embodied AI**,
**robot learning**, and **vision-language-action (VLA) models**, with source
coverage across ICLR, ICML, NeurIPS,
CVPR, ECCV, ICCV, RSS, ICRA, IROS, TPAMI, and AAAI. Venue is source metadata,
not a claim that this seed corpus models a venue-specific house style.

Version 0.4 maintains an audited 300-paper 2021–2025 core from CVPR, ECCV, ICCV,
NeurIPS, ICLR, ICML, and TPAMI. Papers are indexed into 23 topic families; their
recurring terminology and writing moves are deduplicated into compact reusable
records rather than copied once per paper. Sixteen selectively loaded protocols
now cover Abstract, Introduction, Related Work, Method, complete Experiments,
result analysis, Limitations, Conclusion, Rebuttal, Translation, and five table
types. Eighteen precomposed one-file routes keep common link-only
tasks below 24,000 characters; five LaTeX assets turn the table protocols into
editable reporting skeletons. A generated per-paper ledger separates metadata
coverage, abstract analysis, full-paper structural sampling, and direct links to
normalized records. A 20-case blind writing suite checks final-output facts and
evidence boundaries. A separate paired professionalism benchmark now compares
the same model with and without the library through randomized A/B review, six
anchored quality dimensions, critical-error flags, paired bootstrap uncertainty,
and rater-agreement reporting. A policy-driven promotion queue prioritizes the
next nonredundant paper reviews without entering normal Agent context. A separate
decision ledger records whether each reviewed paper promoted a new record, reused
an existing record, or warranted no promotion.

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
[immutable v0.4.0 agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md).
The index first offers one-file task routes for the four core domains. A matching
route already contains the compact contract, one protocol when needed, and its
selected records, so the Agent reads that file and stops. Unmatched tasks fall
back to one universal core, one section catalog, one small domain hub, at most
one topic catalog, and only 3–8 full entry cards.

Suggested prompt:

```text
Use https://github.com/asimfish/super_library as the language authority. Read
llms.txt and use the v0.4 selective-loading workflow. Prefer one matching
one-file task route and stop. If none matches, use core once, one relevant
section protocol when needed, one section catalog and domain hub, at most one
topic catalog, then only 3–8 cards. Preserve my claims and verify primary papers
before making literature statements.
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
# Get a tiny load plan and one protocol recommendation
python3 scripts/superlib.py route "ablation table for coupled components" \
  --domain world_models --section experiments

# Inspect one experiment/table protocol without loading all sixteen
python3 scripts/superlib.py guide --list
python3 scripts/superlib.py guide experiments.table.ablation

# Copy one auditable LaTeX table skeleton
python3 scripts/superlib.py template --list
python3 scripts/superlib.py template main_results --output tables/main_results.tex

# Build a bounded two-pass context for one writing task
python3 scripts/superlib.py bundle \
  --guide experiments.analysis \
  --rhetoric-query "quantify the main comparison and retain exceptions" \
  --technical-query "action chunking closed-loop feedback" \
  --domain robot_learning --section experiments --intent evidence \
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

# Audit aggregate or per-paper analysis depth
python3 scripts/superlib.py analysis-status
python3 scripts/superlib.py analysis-status <source-id> --format json

# Inspect completed promotion/deduplication decisions
python3 scripts/superlib.py promotion-status
python3 scripts/superlib.py promotion-status <source-id> --format json

# Perform a current, bounded network check of canonical paper URLs
python3 scripts/superlib.py verify-sources --limit 20

# Execute deterministic top-k, guide, and task-pack routing cases
python3 scripts/superlib.py eval-retrieval

# List blind writing cases, then score one response (manual review still required)
python3 scripts/superlib.py eval-writing --list
python3 scripts/superlib.py eval-writing --case rebuttal-existing-evidence \
  --response-file response.md --strict

# Inspect the professional A/B benchmark and emit a condition-neutral prompt
python3 scripts/superlib.py benchmark list
python3 scripts/superlib.py benchmark prompt rebuttal-existing-evidence

# Rank the next papers for normalization/deduplication review
python3 scripts/superlib.py coverage-gaps --limit 20
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
    ├── dist/routes/<task>.md           # one-file fast path; stop when matched
    ├── dist/core.md                    # fallback evidence/writing guardrails
    ├── dist/guides/index.md            # choose exactly one section protocol
    │   └── dist/guides/<guide-id>.md   # one section/rebuttal/translation/table protocol
    ├── dist/catalogs/sections/*.md     # thin rhetorical indexes
    ├── dist/catalogs/domains/*.md      # small technical routing hubs
    ├── dist/catalogs/topics/*.md       # bounded technical indexes
    └── dist/cards/<domain>/<id>.md     # one complete entry at a time

dist/evidence/topics/*.md               # paper maps; verify claims only
dist/evidence/source-analysis.*         # per-paper analysis-depth audit; not writing context
dist/evidence/promotion-decisions.*     # completed review decisions; not writing context
dist/evidence/promotion-queue.*         # maintainer review queue; not writing context
dist/templates/tables/*.tex             # copy one experiment-table skeleton

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
- `library/topics.json`: 23 controlled topic families and query aliases.
- `library/collections.json`: auditable paper-selection policies and minimums.
- `library/writing_guides.json`: functional protocols for principal paper
  sections, rebuttal, translation, result analysis, and experiment table types.
- `library/task_routes.json`: 18 precomposed routes for common domain/section
  combinations; each rendered task pack is capped at 24,000 characters.
- `library/table_templates.json` and `templates/tables/`: five source-controlled
  LaTeX table assets with explicit `SL_*` replacement tokens.
- `library/studies/section_writing_2026-08.json`: source IDs and aggregate
  structural observations from the bounded full-paper calibration study.
- `library/coverage_policy.json`: review goals and deterministic scoring weights;
  goals are roadmap targets, not release assertions.
- `library/promotion_decisions.jsonl`: primary-source locators, deduplication
  comparisons, and explicit outcomes for completed evidence reviews.
- `library/taxonomy.json`: controlled domains, sections, intents, venues, and kinds.
- `library/core_ids.json`: the deliberately small universal-core selection.
- `schemas/`: machine-readable data contracts.
- `dist/agent-index.md`, `core.md`, `catalogs/`, and `cards/`: progressive Agent
  retrieval layers.
- `skills/super-library/`: a self-contained skill with a bounded lookup script.
- `scripts/superlib.py`: routing, bundle generation, search, analysis-depth audit,
  validation, build, statistics, source-health checks, and wording lint.
- `evals/`: deterministic retrieval cases, 20 blind writing cases, and the paired
  professionalism design for paper, rebuttal, and translation. Machine checks
  cover objective invariants; randomized same-model A/B evaluation adds anchored
  human ratings, critical-error flags, paired effect estimates, and agreement.

Each entry distinguishes:

- `expression`: recommended term or pattern;
- `meaning`: the semantic content it is safe to convey;
- `guidance` and `avoid`: usage boundary and common failure mode;
- `examples`: original templates with `{placeholders}`;
- `source_ids`: primary sources to verify for scientific claims;
- `provenance`: whether the entry is an original pattern, a terminology record,
  an independently paraphrased synthesis, or a short multi-source attested
  collocation.

The v0.4 reviewed snapshot contains **260 gold entries** and **336 primary-source
records with canonical URLs**. Exactly 300 sources form the recent five-year core: 125
reinforcement-learning, 90 embodied-AI, 55 world-model, and 30 VLA papers.
The collection contains 32 CVPR, 21 ECCV, 33 ICCV, 71 NeurIPS, 64 ICLR, 67 ICML,
and 12 TPAMI papers. It is designed to grow through reviewed contributions rather
than automatic PDF scraping.

For recurring wording, 288 official conference abstracts were analyzed locally
by document frequency; abstract text is not stored. Four cross-paper collocations
survived manual screening and were promoted with source-level attestations. All
12 TPAMI papers remain excluded from this abstract-level phrase-frequency study;
all twelve were subsequently reviewed—eight through their primary paper text
and four through their official abstracts—for normalized definitions or explicit
deduplication decisions. One hundred four core papers are representative sources
cited directly by normalized records. Completed promotion reviews add
eighty-three unique paper-level links, bringing explicit normalized-record coverage
to 187 without inserting every reviewed paper into default cards. One hundred
twenty-six promotion decisions are recorded: thirty-two new normalized records,
ninety-one existing-record links, and three explicit no-promotion outcomes. Inspect
`dist/evidence/source-analysis.jsonl`, run `analysis-status`, or use
`promotion-status` instead of inferring analysis depth from the 300-paper count.
See `library/corpus_report.json` and `library/promotion_decisions.jsonl`.

The current roadmap targets 100 directly linked core papers, 80 full-text
structural samples, and 20 writing-behavior cases. Current progress is 187, 80,
and 20 respectively, so every roadmap target is met, and all 80 sampled papers
now carry reviewed normalized-record links. Meeting the targets is not
a claim that the corpus is complete: newly sampled papers without normalized
links re-enter the review queue at the highest priority. `coverage-gaps` ranks
the next review candidates; reviewers may record `record_no_promotion` when a
paper adds only redundant wording.

To calibrate section organization rather than collect prose, 80 official
full-paper PDFs were analyzed locally: twenty each from reinforcement learning,
embodied AI, world models, and VLA, across CVPR, ECCV, ICCV, ICML, and NeurIPS,
with the move detectors stated explicitly in the study's method field.
Only source IDs and aggregate document-level observations are retained. This
sample informs the functional protocols but is not presented as a statistical
model of venue style. See `library/studies/section_writing_2026-08.json` and
`docs/WRITING_GUIDE_RESEARCH.md`.

Fourteen short collocations carry locators to at least two independent papers.
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
7. Keep paper coverage separate from expression count: many papers may support
   one normalized term or comparison pattern. Reject near-duplicate cards and
   route full paper lists through per-topic evidence maps outside default context.

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
