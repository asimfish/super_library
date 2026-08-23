# Super Library protocol: Generalization and robustness table

`experiments.table.generalization` · `table_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Make the training–evaluation shift or perturbation explicit and report performance across both reference and shifted conditions.

**Use when:** Claims concern unseen tasks, objects, environments, embodiments, distributions, corruptions, or perturbations.

## Required inputs

- Training distribution and exact held-out unit.
- Reference, shifted, and severity conditions.
- Metric, denominator, seeds or trials, and uncertainty.
- Whether model selection used any shifted-condition information.

## Functional protocol

### 1. Define the shift axis (required)

- Name what is unseen and how it was withheld.
- Separate interpolation, compositional recombination, domain shift, and open-set evaluation.

### 2. Retain a reference condition (required)

- Report in-distribution or seen-condition performance beside shifted performance.
- Make accuracy–robustness trade-offs visible.

### 3. Audit selection leakage (required)

- State which data selected hyperparameters and checkpoints.
- Do not call a condition held out if it influenced tuning or prompt selection.

## Choose one internal template

### Training versus shifted evaluation

Use when: Methods are compared across seen and one or more unseen conditions.

1. Rows: methods under comparable training data.
2. Columns: seen reference, each named shift or severity, and a defined gap metric if useful.
3. Caption: opens by naming the compared systems, then held-out unit, selection protocol, metric, runs, uncertainty, and arrows.
4. Analysis: shifted-condition difference, reference trade-off, consistency, and residual failure.

## Verification

- The held-out definition can be reconstructed from the caption or referenced setup.
- The term out-of-distribution is tied to a specific changed variable.
- Any robustness average states the perturbation set and weighting.
- The conclusion does not generalize beyond the sampled shift.

## Avoid

- Labeling a random example split as novel-task or novel-environment generalization.
- Reporting only shifted results and hiding degradation in the reference condition.
- Tuning on the test shift while describing it as unseen.

## Reusable LaTeX asset

- [Generalization and robustness table](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/templates/tables/generalization.tex) — `generalization.tex`; requires booktabs.
- Replace every `SL_*` token. Run the wording audit afterward;
  unresolved table tokens are reported as errors for manual repair.

## Retrieve related sentence cards only as needed

- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [Under {evaluated setting}, {method} consistently {measured outcome}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.scope.001.md) — `general.sentence-pattern.scope.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
