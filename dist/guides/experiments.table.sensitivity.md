# Super Library protocol: Sensitivity, sweep, and scaling table

`experiments.table.sensitivity` · `table_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Show how conclusions change with a hyperparameter, data scale, model scale, horizon, or evaluation budget without cherry-picking.

**Use when:** A claim or design choice depends on a selected value, range, or scale.

## Required inputs

- Parameter or scale, unit, candidate range, and rationale.
- Selection set, selection objective, and whether the sweep was planned or exploratory.
- Matched factors held constant across values.
- Per-value metric, resource, runs, and uncertainty.

## Functional protocol

### 1. Define the range and default (required)

- Report the full evaluated range in a meaningful linear or logarithmic order.
- Mark the chosen default and state how it was selected.
- Include boundary values that can reveal collapse when feasible.

### 2. Hold other factors fixed (required)

- State data, optimization, compute, evaluation, and seeds held constant.
- When scale changes compute, report the changed resource rather than implying a one-factor intervention.

### 3. Describe sensitivity, not just optimum (required)

- Report stability range, monotonicity, saturation, reversal, or instability.
- Separate a tuning optimum from evidence for the proposed mechanism.

## Choose one internal template

### Parameter or scale sweep

Use when: One ordered variable is varied.

1. Rows: ordered parameter or scale values with the default marked.
2. Columns: claim-relevant metric, uncertainty, and changed resource.
3. Caption: range, selection protocol, controls, runs, and default marker.
4. Analysis: trend, stable region, chosen point, and exception.

## Verification

- All evaluated values are reported or omissions are explained.
- Test-set performance did not select the final value unless explicitly declared as exploratory.
- Scaling conclusions separate benefits of model size, data, and compute where the design permits.
- The prose discusses the trend and uncertainty rather than only the maximum cell.

## Avoid

- Showing a narrow range centered on the selected value without rationale.
- Choosing a different best hyperparameter for every test task without disclosing the oracle.
- Calling a three-point sweep a scaling law.
- Hiding unstable or failed settings.

## Retrieve related sentence cards only as needed

- [Unless otherwise specified, we use {default configuration} in all experiments.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.reproducibility-default.001.md) — `general.sentence-pattern.reproducibility-default.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [These results are consistent with the hypothesis that {mechanism}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.causal-caution.001.md) — `general.sentence-pattern.causal-caution.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
