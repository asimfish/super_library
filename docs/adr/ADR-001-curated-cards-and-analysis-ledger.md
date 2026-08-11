# ADR-001: Keep curated cards and add an explicit analysis-depth ledger

Status: Accepted
Date: 2026-08-09

## Context

Super Library must cover hundreds of papers while giving a writing Agent a small,
high-signal context. A paper's presence in the source collection does not mean its
wording was promoted into a reusable record. Earlier aggregate counts made that
distinction difficult to audit paper by paper.

## Driving factors

- Keep default writing context bounded as the paper collection grows.
- Avoid redistributing copyrighted paper text or encouraging phrase copying.
- Make metadata coverage, abstract analysis, full-paper structural sampling, and
  direct library links independently auditable.
- Preserve deterministic, reviewable builds without an external vector service.
- Route literature verification to primary papers rather than treating retrieval
  output as evidence.

## Considered options

### A. Curated normalized cards plus a generated per-paper ledger

Keep terminology, definitions, usage notes, and original sentence patterns as the
canonical writing layer. Generate one analysis record per core paper from explicit
canonical exclusions, the full-paper study sample, and reverse `source_ids` links.
Keep this ledger outside the default writing route.

### B. Full-text chunk store with embedding or vector retrieval

Store or index full paper text and retrieve passages dynamically. This increases
phrase-copying and licensing risk, requires chunking and embedding infrastructure,
makes deterministic review harder, and can spend context on redundant prose.

### C. One prose pack per paper

Handwrite a summary and phrase list for every paper. This is transparent but grows
linearly, duplicates recurring expressions, and tempts Agents to load many files.

## Decision

Adopt option A. Canonical sources remain in `library/`; generated writing artifacts
remain in `dist/`. `dist/evidence/source-analysis.jsonl` records abstract status,
full-text structural-sample status, direct linked entry IDs, and an explicit outcome
for every paper in the 300-paper core. `analysis-status` exposes the same view
locally. The ledger is an audit artifact, not writing context or scientific evidence.

Use a separate network checker for current URL health. A historical collector count
does not establish present reachability; 404/410 responses are failures, while
access-control and transient statuses remain distinct.

## Impact

- Agents continue to retrieve one route or a small protocol/card bundle.
- Maintainers can now answer how deeply each paper was processed without opening
  every topic map or inferring from aggregate counts.
- Collection breadth and normalized-expression coverage remain different metrics.
- Adding a paper does not require a new card, but it does require a ledger outcome.
- Full-text or semantic retrieval can be reconsidered later only with a separate
  licensing, provenance, deduplication, and context-budget design.
