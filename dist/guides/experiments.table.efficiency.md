# Super Library protocol: Efficiency and deployment table

`experiments.table.efficiency` · `table_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Report quality jointly with the resource that defines efficiency under a reproducible measurement protocol.

**Use when:** Claims concern sample, compute, memory, parameter, latency, throughput, energy, or deployment efficiency.

## Required inputs

- Quality metric and the exact resource axis.
- Hardware, software, precision, batch size, sequence length, input resolution, and concurrency.
- Training data or interaction budget and stopping rule.
- Warm-up, synchronization, preprocessing, and measurement window.

## Functional protocol

### 1. Define the resource (required)

- Distinguish parameters, FLOPs, accelerator-hours, wall-clock time, peak memory, latency, throughput, energy, environment steps, and demonstrations.
- Do not use sample efficiency when only optimization steps are reduced.

### 2. Fix the measurement protocol (required)

- State hardware, precision, batch, input shape, warm-up, synchronization, and included preprocessing.
- For robot policies, distinguish model inference latency from end-to-end control-loop frequency.

### 3. Show the quality–resource trade-off (required)

- Report quality and resource in the same table or linked display.
- Compare at matched quality, matched resource, or present the Pareto frontier.

## Choose one internal template

### Deployment profile

Use when: Methods are compared for inference or control deployment.

1. Rows: methods and deployment variants.
2. Columns: quality, parameters, peak memory, latency and/or throughput, and control rate when relevant.
3. Caption: opens by naming the compared systems, then hardware, precision, batch, input, timing boundary, repeats, and uncertainty; use column arrows or one collective direction note instead of per-metric higher-or-lower glosses.
4. Analysis: matched-quality or matched-resource comparison and trade-off.

## Verification

- Resource units and measurement boundaries are explicit.
- Training and inference resources are not mixed in one undefined efficiency claim.
- Reported throughput and latency use compatible batch and concurrency assumptions.
- Any deployment claim is checked against the actual real-time requirement.

## Avoid

- Calling a method efficient solely because it has fewer parameters.
- Comparing latency measured on different hardware without separation.
- Reporting throughput at a large batch as single-sample latency.
- Ignoring preprocessing, communication, simulator, or action-decoding time when it dominates deployment.

## Reusable LaTeX asset

- [Efficiency and deployment table](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/templates/tables/efficiency.tex) — `efficiency.tex`; requires booktabs.
- Replace every `SL_*` token. Run the wording audit afterward;
  unresolved table tokens are reported as errors for manual repair.

## Retrieve related sentence cards only as needed

- [At a matched {budget}, {method} yields {verified comparison}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-matched-budget.001.md) — `general.sentence-pattern.rebuttal-matched-budget.001`
- [For a controlled comparison, we hold {factor} fixed and vary only {factor}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.fair-comparison.001.md) — `general.sentence-pattern.fair-comparison.001`
- [policy inference latency and control frequency](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/vision_language_action/vla.usage-note.control-latency.001.md) — `vla.usage-note.control-latency.001`
- [sample efficiency / data efficiency](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/reinforcement_learning/rl.term.sample-efficiency.001.md) — `rl.term.sample-efficiency.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
