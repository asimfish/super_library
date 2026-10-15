# ADR-010: Argument frames and artifact-based agent cooperation

## Status

Accepted for the feature branch. Writing effectiveness remains unproven.

## Context

Our language records constrain terminology and wording, but a professional
experimental paragraph also needs an argument: question, comparison, decisive
evidence, exception and scoped conclusion. Prior public-table diagnostics were
mixed; the baseline sometimes integrated efficiency and success more clearly.
User feedback asks for IdeaScientist-inspired structures and a multi-agent system.

## Driving factors

- Preserve original facts, adverse outcomes, uncertainty and required quantities.
- Keep one owner for terminology and section protocols.
- Retrieve a few structures by function and evidence relation, without full papers
  or the whole corpus entering every agent's context.
- Make independent roles executable with the host's available agents, without a
  new provider SDK, credential, model service or assumed external installation.
- Resume interrupted work and reject stale or incomplete reviews.

## Candidates

| Candidate | Benefit | Cost / limitation |
|---|---|---|
| One agent with a larger combined prompt | Simple invocation | Same context authors and reviews; no durable stage boundaries |
| Multi-agent graph tied to a provider SDK and vector service | Automatic provider-specific dispatch | New dependencies, keys and service cost; premature retrieval infrastructure |
| Local artifact coordinator plus host agent sessions | Explicit stages and bounded contexts; works with existing agents | Host must dispatch real workers and attest identities; local files are not sandbox isolation |

## Decision

Choose the artifact coordinator. A single coordinator owns a local run; stage
workers submit schema-constrained proposals. The runtime exposes initialization,
status, ready-role packets, artifact submission, revision and export. The host
owns model selection, invocation, worker identities and cancellation. It must
never replace separate reviews with role-play in the writing session while
claiming independence.

Use JSON for task, state, role outputs and frames; manuscript export is text.
The task, retrieval outputs, config and role contracts are frozen at initialization. Packet hashes
bind role, input facts, dependencies and round. Atomic persistence and a local lock
serialize coordinator updates. Existing output is never silently overwritten.

The dependency graph is evidence_reader → argument_planner → writer →
{evidence_reviewer, narrative_reviewer}. Both reviewers are required and cannot be
the writer or each other. These IDs detect accidental role reuse; they do not
authenticate a remote person/model. Reviewer packets omit the peer's judgment.
Revision retains history, replaces the current writing/review stage, and requires
fresh reviews. A bounded revision count prevents an unending retry loop.

`library/argument_frames.json` owns original argument structures. Terms remain in
entries, section instructions in guides, and audit evidence in studies. Frames
reference those owners and derive function/evidence-relation indexes. Selection
uses exact controlled tags, deterministic ordering, deduplication and a serialized
character budget. No third-party corpus, paper prose or numeric result becomes a
new language record. These summaries do not claim fresh source verification.

The writer receives original facts as well as the evidence checks and plan. The
plan cannot silently erase an adverse outcome. Evidence IDs and exact quote maps
make support traceable; reviewers still must judge entailment and narrative value.
Internal metadata belongs in artifacts, while export returns manuscript text only.

## Impact

Existing bundle/search/route behavior and the frozen release stay compatible.
Team initialization uses one existing bounded drafting bundle plus at most two
frames. Planners and evidence reviewers do not receive the language corpus.
The CLI does not execute model output, follow arbitrary URLs or invoke shell
commands. Private artifacts should live outside the repository; `.team-runs/`
is also ignored. Local host access remains the trust boundary.

Rollback means using ordinary retrieval and retaining any run directory as an
audit record. No migration or replacement of existing corpus records is required.
Portable and link-only skill installations retain their old retrieval path;
the new coordinator requires a full feature-branch checkout.

## Verification boundary

Tests establish state transitions, budgets, reference coverage, revision
invalidation, input validation and compatible retrieval. A live host-agent run
establishes that separate agents can consume and submit the contracts. Neither
establishes causal writing improvement. New counterbalanced blind comparisons,
with facts and criteria frozen before drafting, remain necessary for that claim.

The first live run exposed a review weakness: both reviewers passed a largely
comparison-by-comparison paragraph with a long caveat ending. Maintainer inspection
found it insufficiently finding-led. A subsequent independent contract revision
asks the planner for a governing finding, permits scope evidence to qualify an
existing claim, and requires narrative reviewers to assess whether contrasts
develop that finding. Both candidates are retained as development observations;
the second run is not a fresh holdout or causal evidence of improved writing.

## Inspiration and ownership

[IdeaScientist fields](https://github.com/jiarui-liu/IdeaScientist/blob/82a98a08772eab08d11fd097445afa4a8eaaa5b3/ideascientist/vault/fields.py)
and [role boundaries](https://github.com/jiarui-liu/IdeaScientist/blob/82a98a08772eab08d11fd097445afa4a8eaaa5b3/ideascientist/harness/roles.py)
informed the high-level design. This is an independent implementation, not a
port of its code/prompts or an import of its generated data. See the existing
skill's `UPSTREAM.md` for pinned provenance and license boundaries.
