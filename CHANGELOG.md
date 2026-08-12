# Changelog

All notable changes to the Super Library corpus and tooling are documented
here. Versions correspond to immutable git tags; generated artifacts inside a
tag pin their own raw links to that tag.

## v0.4.0 — 2026-08-12

The evidence-protocols release: every core paper now carries an explicit,
audited review disposition.

- 274 reviewed gold records backed by 336 primary sources with canonical URLs;
  all 300 core-collection URLs verified reachable.
- Explicit review dispositions for all 300 core papers: 296 directly linked to
  normalized records and 4 recorded no-promotion outcomes, tracked in a
  236-decision promotion ledger with per-paper evidence locators and
  deduplication rationales.
- Full-text structural sampling extended from 40 to 80 papers (twenty per
  domain) with the ten document-level move detectors stated explicitly in the
  study method; all 12 TPAMI papers reviewed through primary text or official
  abstracts.
- Roughly forty new normalized records closing recurring concept gaps,
  including state abstraction, POMDP, hierarchical policy, differentiable
  physics simulation, self-supervised representation learning, AI feedback,
  RLHF, human-in-the-loop RL, risk-sensitive RL, meta-RL, multi-task RL,
  continual RL, reset-free RL, value factorization, reward shaping, self-play,
  multi-objective RL, regret, mobile manipulation, object rearrangement,
  social navigation, tactile sensing, vision-language reward, embodied
  reasoning, synthetic data generation, task-irrelevant distractors, and
  objective mismatch.
- A same-model blind paired professionalism benchmark: condition-neutral
  prompts, six anchored rubric dimensions, critical-error flags, paired
  bootstrap intervals, rater-agreement reporting, and a private A/B key
  written with owner-only permissions.
- A peer-review section protocol with six review-writing records and
  review-transfer retrieval evals.
- Slimmer generated catalogs (largest selective-context file well under the
  20 KB budget) and a per-paper analysis ledger separating metadata coverage,
  abstract analysis, structural sampling, and direct links.
- 74 unit and integration tests and 31 deterministic retrieval evals; builds
  remain deterministic with zero generated-artifact drift.

## v0.3.0 — 2026-07-31

- 300 audited papers from 2021–2025 across CVPR, ECCV, ICCV, NeurIPS, ICLR,
  ICML, and TPAMI; 228 gold records backed by 331 primary sources.
- 23 topic families; 10 selective section protocols; 18 one-file task routes
  (largest 17.3 KB); domain-specific experiment reporting overlays.
- Five auditable LaTeX table assets with replacement-token linting.
- 28 deterministic English/Chinese retrieval cases and 43 passing tests.

## v0.2.0 — 2026-07-29

- Bounded progressive retrieval: agent index, universal core, thin catalogs,
  and 3–8 entry cards per task with a hard context budget.
- Local route and bundle commands separating rhetorical and technical
  retrieval passes.
- 153 gold entries and 41 verified primary sources; machine router, schemas,
  checksums, and a deterministic standalone skill lookup script.

## v0.1.0 — 2026-07-29

- Initial reviewed release: 106 gold records and 32 primary sources across the
  11 target venues.
- World models, reinforcement learning, embodied AI, and robot learning
  coverage with CLI retrieval and source-aware definitions.
- Deterministic artifacts with schema validation and a SHA-256 manifest.
