# Super Library protocol: Abstract: claim-aligned empirical summary

`abstract` · `section_protocol` · section `abstract` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Produce a compact summary whose problem, contribution, evidence, and scope exactly match the completed paper.

**Use when:** Drafting or revising an AI-paper abstract after the methods and principal results are known.

## Required inputs

- One-sentence problem and evaluated scope.
- The specific unresolved limitation or challenge addressed by this paper.
- The paper's core insight and the mechanism that realizes it.
- Verified principal evidence, including benchmark, metric, comparison, statistic, and uncertainty when available.
- Assumptions, deployment boundary, or evaluated generalization axis that materially limits the claim.

## Functional protocol

### 1. Build an abstract claim ledger (required)

- Map every proposed abstract claim to a section, theorem, table, or figure in the paper.
- Remove a claim if the mapped evidence does not support its comparison set or generalization scope.
- Keep aspirational motivation grammatically distinct from achieved results.

### 2. State the problem and precise gap (required)

- Name the task or setting before the broad application motivation.
- Describe a concrete assumption, failure mode, resource bottleneck, or missing capability rather than calling prior work insufficient.
- Do not claim priority or novelty unless independently verified.

### 3. Connect insight to mechanism (required)

- State what makes the approach work conceptually, then name the mechanism.
- Do not enumerate low-level modules that do not affect the paper-level contribution.

### 4. Report evidence with scope (required)

- Prefer one decision-relevant verified result over 'extensive experiments demonstrate'.
- Distinguish absolute change from relative change and percentage points.
- End with the supported implication or boundary, not a universal superiority claim.

## Choose one internal template

### Empirical method paper

Use when: The main contribution is a method evaluated on benchmarks, simulation, or real systems.

1. Task and operational context.
2. Specific limitation under a named setting or assumption.
3. Core insight.
4. Method and mechanism.
5. Verified principal comparison with evaluation scope.
6. Supported implication or explicit boundary.

### Resource or benchmark paper

Use when: The main contribution is a dataset, environment, benchmark, or evaluation protocol.

1. Capability that cannot currently be measured well.
2. Coverage or validity gap in existing resources.
3. What the new resource contains and how it is constructed.
4. What diagnostic dimensions or tasks it enables.
5. Verified baseline findings and what they reveal.
6. Access, scope, or limitation statement.

### Theory-led paper

Use when: The main contribution is a theorem, guarantee, bound, or analysis.

1. Problem and formal setting.
2. Limitation of existing guarantees.
3. Main result with its assumptions.
4. Key proof or algorithmic idea at a high level.
5. Implication relative to the prior bound or setting.
6. Empirical evidence only if it is actually part of the contribution.

## Verification

- The abstract uses the same task, method name, metric names, and comparison direction as the body.
- Every number matches the final table or theorem, including units, denominator, and aggregation.
- No conclusion extends beyond the evaluated datasets, tasks, embodiments, shifts, or assumptions.
- The target venue's current length, paragraph, citation, and formatting rules were checked separately.

## Avoid

- Opening with an unverifiable claim that the broad field is fundamentally important.
- Using 'novel', 'effective', 'superior', or 'state-of-the-art' as substitutes for a technical contribution and verified result.
- Listing modules without explaining the insight that connects them.
- Adding citations, results, or deployment claims not present in the completed paper.

## Retrieve related sentence cards only as needed

- [A central challenge is to {objective} while {constraint}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.motivate.001.md) — `general.sentence-pattern.motivate.001`
- [Despite progress in {area}, existing methods remain limited by {specific limitation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.gap.001.md) — `general.sentence-pattern.gap.001`
- [Our main contribution is {artifact or insight} that {verified capability}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.contribution.001.md) — `general.sentence-pattern.contribution.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [state-of-the-art performance on {benchmark} under {protocol}](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.usage-note.state-of-the-art.001.md) — `general.usage-note.state-of-the-art.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
