# Super Library protocol: Tables: common construction and reporting standard

`experiments.table.common` · `table_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Make each table answer one research question with enough protocol information to interpret every comparison.

**Use when:** Designing or auditing any quantitative experimental table.

## Required inputs

- Research question and comparison axis.
- Source data, analysis script, and exact mapping from cells to outputs.
- Metric direction, units, denominator, aggregation, uncertainty, and number of independent runs.
- Protocol differences in data, pretraining, compute, interaction, tuning, hardware, or evaluation.

## Functional protocol

### 1. Assign one primary question (required)

- A reader should be able to state what comparison the table answers in one sentence.
- Split unrelated settings or metrics when grouping obscures the decision.

### 2. Write a self-contained caption (required)

- Open by naming the compared systems or methods; the first clause states what entities the table compares, not which metrics it lists.
- Name task, dataset or environment, split, and evaluation setting.
- Define metric direction, units, aggregation, uncertainty, number of runs, abbreviations, and emphasis rules; column arrows or one collective direction note suffice.
- State consequential protocol differences or point to a precise footnote.

### 3. Structure rows and columns (required)

- Group baselines by method family or protocol and keep row labels stable across tables.
- Order columns by task, shift, or metric logic rather than by favorable outcome.
- Use consistent precision justified by measurement uncertainty.

### 4. Use accessible, unambiguous encoding (required)

- Do not use color as the only cue; define bold, underline, symbols, and arrows.
- Distinguish zero, missing, not reported, and not applicable.
- Prefer restrained horizontal rules and avoid vertical-rule clutter.

### 5. Reconcile table and prose (required)

- Every cited value and ranking in prose matches the table.
- Cells trace to source data and transformations.
- Emphasis compares only rows under a defensible common protocol.

## Choose one internal template

### General quantitative caption

Use when: The table reports comparable numeric results.

1. Which systems or methods are compared, and on what task or setting.
2. Protocol or split.
3. Metric names with arrows and units.
4. Statistic, uncertainty, and number of independent runs.
5. Meaning of emphasis and missing-value symbols.
6. Material protocol exceptions.

## Verification

- The table remains interpretable when separated from the surrounding paragraph.
- Bold or underline never implies a fair ranking across incomparable protocols.
- Missing values use a documented symbol and are not encoded as zero.
- The table is legible in grayscale and at final publication size.
- No significance marker appears without a verified test, comparison, and correction policy when applicable.

## Avoid

- Using decorative color or mandatory best/second-best colors.
- Mixing percentages and fractions in one metric without explicit units.
- Averaging metrics with incompatible scales into an unexplained overall score.
- Packing setup details into tiny cells that reviewers cannot read.
- Opening the caption with metric names instead of the compared systems, or repeating a per-metric higher-or-lower-is-better gloss when arrows or one collective note already define direction.

## Retrieve related sentence cards only as needed

- [For a controlled comparison, we hold {factor} fixed and vary only {factor}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.fair-comparison.001.md) — `general.sentence-pattern.fair-comparison.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [respectively requires an unambiguous one-to-one ordering](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.respectively.001.md) — `general.usage-note.respectively.001`
- [statistically significant versus substantial improvement](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.significant.001.md) — `general.usage-note.significant.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
