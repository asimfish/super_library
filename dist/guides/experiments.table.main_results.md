# Super Library protocol: Main-results table

`experiments.table.main_results` · `table_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Compare the proposed method with relevant baselines while making protocol equivalence and principal metrics visible.

**Use when:** The central table supports the paper's primary empirical comparison.

## Required inputs

- Proposed variants and verified baseline set.
- Task or dataset groups and principal decision-relevant metrics.
- Pretraining, data, model-scale, compute, interaction, and tuning differences.
- Per-run values or verified aggregate statistics.

## Functional protocol

### 1. Group comparable baselines (required)

- Separate methods that use extra data, pretraining, privileged inputs, larger models, or different interaction budgets.
- Include the strongest relevant baseline that can be evaluated fairly; explain omissions.

### 2. Prioritize claim-relevant metrics (required)

- Lead with the metric that answers the research question.
- Add resource or safety metrics when the main claim depends on them.
- Use an overall average only when component metrics are commensurate and the weighting is defined.

### 3. Define ranking scope (required)

- Apply best-result emphasis only within comparable row groups.
- Do not hide uncertainty to make a small ranking difference appear decisive.

## Choose one internal template

### Methods by tasks or datasets

Use when: The same methods are evaluated under a common protocol across multiple tasks.

1. Rows: method families, then the proposed method and named variants.
2. Columns: protocol flags, task–metric groups, then a justified aggregate.
3. Caption: opens by naming the compared systems, then setting, split, metric directions, aggregation, runs, emphasis, and extra-resource flags.
4. Footnotes: implementation or protocol exceptions.

## Verification

- Every baseline row identifies whether results are reproduced, taken from a source, or rerun.
- The same checkpoint-selection and evaluation budget are used or differences are disclosed.
- The prose quantifies the primary comparison instead of only claiming the best rank.

## Avoid

- Ranking a larger pretrained model against a from-scratch baseline as if architecture were the only difference.
- Selecting baseline numbers from incompatible papers or evaluation protocols without a clear separator.
- Using average rank or an overall score to conceal regressions on important tasks.

## Reusable LaTeX asset

- [Main-results table](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/templates/tables/main_results.tex) — `main_results.tex`; requires booktabs.
- Replace every `SL_*` token. Run the wording audit afterward;
  unresolved table tokens are reported as errors for manual repair.

## Retrieve related sentence cards only as needed

- [Results on {dataset or task} under {protocol}. {Metric direction and units}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.caption-main-results.001.md) — `general.sentence-pattern.caption-main-results.001`
- [For a controlled comparison, we hold {factor} fixed and vary only {factor}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.fair-comparison.001.md) — `general.sentence-pattern.fair-comparison.001`
- [Latency is measured on {hardware} with {precision, batch, and timing boundary}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.latency-protocol.001.md) — `general.sentence-pattern.latency-protocol.001`
- [At a matched {budget}, {method} yields {verified comparison}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-matched-budget.001.md) — `general.sentence-pattern.rebuttal-matched-budget.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
