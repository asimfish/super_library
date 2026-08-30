# Super Library protocol: Ablation table

`experiments.table.ablation` · `table_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Test component, loss, data, or design claims with matched variants and conclusions no stronger than the intervention supports.

**Use when:** A table compares the full method with controlled variants.

## Required inputs

- Full model and the claim attached to each component or design choice.
- Matched training data, initialization, optimization, compute, evaluation, and seeds.
- Known or plausible component interactions.
- Per-variant statistics and uncertainty.

## Functional protocol

### 1. Design interpretable variants (required)

- Use the full method as an explicit anchor.
- Change one factor at a time unless the table explicitly tests an interaction.
- Retune only under a declared common policy; disabling a component may change the best optimization settings.

### 2. Expose interactions (conditional)

- Add factorial or paired variants when components are theoretically coupled.
- Do not add single-component drops as if effects were additive when interactions are expected.

### 3. Bound the conclusion (required)

- Compare the effect magnitude with run-to-run uncertainty.
- Conclude contribution under the tested configuration, not universal necessity.
- Report removals that improve a metric and discuss the trade-off.

## Choose one internal template

### Component presence matrix

Use when: Several discrete modules are toggled.

1. Rows: base, incremental or factorial variants, and full method.
2. Columns: explicit component indicators followed by claim-relevant metrics.
3. Caption: opens by naming the ablated system, then matched resources, seeds, uncertainty, and full-model definition.
4. Analysis: largest supported effect, interaction, uncertainty, and exception.

## Verification

- All variants use the declared matched protocol.
- The table includes the actual full method used for the main result.
- Component names are identical in Method, table, caption, and prose.
- Ablation claims do not rely on differences smaller than the reported uncertainty without further analysis.

## Avoid

- Calling a hyperparameter sweep an ablation without defining the design claim.
- Removing multiple coupled components in one row and attributing the change to one of them.
- Reporting only the best seed or one favorable task.

## Reusable LaTeX asset

- [Ablation table](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/templates/tables/ablation.tex) — `ablation.tex`; requires booktabs.
- Replace every `SL_*` token. Run the wording audit afterward;
  unresolved table tokens are reported as errors for manual repair.

## Retrieve related sentence cards only as needed

- [Removing {component} reduces {metric}, indicating that {bounded interpretation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.ablation.001.md) — `general.sentence-pattern.ablation.001`
- [These results are consistent with the hypothesis that {mechanism}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.causal-caution.001.md) — `general.sentence-pattern.causal-caution.001`
- [Unless otherwise specified, we use {default configuration} in all experiments.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.reproducibility-default.001.md) — `general.sentence-pattern.reproducibility-default.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
