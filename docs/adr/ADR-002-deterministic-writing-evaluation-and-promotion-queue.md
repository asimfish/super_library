# ADR-002: Separate deterministic writing checks from scientific review

Status: Accepted
Date: 2026-08-09

## Context

Retrieval tests show that an Agent receives the intended records, but they do not
show whether the final prose preserves numbers, uncertainty, scope, and negative
evidence. At the same time, 240 papers in the 300-paper core are not directly
linked from a normalized language record. Expanding them in source-ID order would
waste review effort and create redundant cards.

## Driving factors

- Evaluate final writing without rewarding imitation of one reference paragraph.
- Keep CI deterministic, local, inexpensive, and independent of a model vendor.
- Preserve a human decision boundary for scientific correctness and prose quality.
- Prioritize already reviewed evidence gaps before collecting more papers.
- Allow a reviewer to conclude that a paper adds no nonredundant library record.

## Considered options

### A. Rule checks plus a separate manual rubric and policy-driven review queue

Declare blind prompts, evidence boundaries, machine-checkable regular-expression
invariants, and a manual rubric. Generate a ranked queue from analysis depth,
current domain/venue gaps, and recency. Store only configuration and facts as the
canonical data; derive reports deterministically.

### B. Gold prose plus semantic similarity

This makes one wording appear canonical even though many strong paragraphs are
valid. It rewards surface imitation and can penalize clearer, fact-equivalent prose.

### C. An LLM judge in continuous integration

This may help exploratory review, but scores vary across model versions and prompts,
add external cost, and do not provide a stable regression oracle.

## Decision

Adopt option A. `evals/writing.json` is the canonical behavior suite.
`scripts/writing_eval.py` exposes a registry of deterministic check evaluators;
new check types can be added without modifying CLI orchestration. The CLI exposes
blind case packets separately from hidden checks and manual rubrics. A machine
pass never implies scientific correctness or professional prose quality.

`library/coverage_policy.json` defines roadmap goals and scoring weights.
`coverage-gaps` and generated promotion-queue artifacts rank unlinked core papers.
Full-text structural samples without normalized links come first. A queue item is
review work, not language evidence, and `record_no_promotion` is a valid deduplication
outcome.

## Impact

- Maintainers can regression-test numbers, uncertainty, evidence scope, and forbidden
  claims in actual Agent output.
- Human reviewers still judge argument quality, terminology fit, citation validity,
  source overlap, and scientific truth.
- Coverage goals are explicit targets, not release assertions or hard corpus minima.
- The queue remains outside default Agent writing context and cannot be cited as
  evidence.
