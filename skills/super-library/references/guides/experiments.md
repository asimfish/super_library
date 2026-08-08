# Super Library protocol: Experiments: claim-to-evidence protocol

`experiments` · `section_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Design and write an experimental section in which each major empirical claim is tested under an explicit protocol and bounded interpretation.

**Use when:** Planning or writing the complete empirical evaluation, before selecting a specialized table or analysis guide.

## Required inputs

- Empirical claim list and one research question per claim.
- Datasets, tasks, splits, environments, embodiments, populations, and held-out units.
- Metrics with direction, units, denominator, aggregation unit, and decision relevance.
- Baseline implementations, training data, pretraining, tuning, parameter, compute, and interaction budgets.
- Seeds or trials, checkpoint and hyperparameter selection protocol, uncertainty statistic, and statistical tests when used.
- Hardware, software versions, training and evaluation compute, real-system safety constraints, and failure records.

## Functional protocol

### 1. Create the claim–evidence matrix (required)

- For every claim, record research question, comparison axis, protocol, metric, display, and allowed interpretation.
- Place claim-critical evidence in the main paper when the venue warns that reviewers may not consult appendices.
- Remove experiments that do not test a stated claim or label them exploratory.

### 2. Define evaluation scope (required)

- Describe task, data provenance, split construction, held-out unit, and evaluation population.
- For embodied work, distinguish simulation from real-system trials and name the control loop, intervention, reset, and success denominator.
- For RL, distinguish environment steps, gradient steps, episodes, wall-clock time, and offline data size.

### 3. Define metrics and statistical unit (required)

- State whether higher or lower is better, the unit, and the averaging unit.
- Report the number of independent seeds, runs, scenes, tasks, episodes, or trials and avoid treating correlated samples as independent.
- Name mean, median, standard deviation, standard error, confidence interval, or percentile explicitly.

### 4. Establish baseline fairness (required)

- Record implementation source, version, reproduction changes, and tuning protocol for each baseline.
- Disclose material differences in pretraining data, model scale, supervision, compute, and interaction budget.
- Do not bold a result as best when protocols are not comparable.

### 5. Answer the primary research questions (required)

- Lead each result paragraph with the question or comparison axis.
- Point to the display, quantify the relevant difference, state consistency or exceptions, then give a calibrated interpretation.
- Report null, negative, unstable, or adverse results when they bear on the claim.

### 6. Add only claim-relevant analyses (conditional)

- Use ablation for component or mechanism claims, generalization for named shifts, robustness for named perturbations, and efficiency for named resources.
- Add sensitivity or scaling analysis when a conclusion depends on a chosen hyperparameter or scale.
- Include qualitative examples and failure cases when metrics conceal behavior relevant to deployment.

### 7. Close reproducibility gaps (required)

- Provide enough implementation and evaluation detail to reconstruct the reported protocol.
- State code, data, simulator, benchmark, and model availability only as actually provided.
- Use the target venue's current reproducibility checklist or statement and point to manuscript locations.

## Choose one internal template

### Standard empirical evaluation

Use when: The paper has benchmarked quantitative claims.

1. Research questions or evaluation goals.
2. Tasks, datasets, splits, and metrics.
3. Baselines and fairness controls.
4. Implementation, selection, and statistical protocol.
5. Main results organized by research question.
6. Ablation or mechanism analysis.
7. Generalization, robustness, efficiency, qualitative behavior, or failures only as claim-relevant.
8. Scope summary and appendix pointers.

### Real-robot or real-system evaluation

Use when: Physical deployment or human intervention is part of the evidence.

1. Platform, sensing, control frequency, workspace, safety protocol, and task definitions.
2. Trial independence, reset procedure, intervention policy, denominator, and success criteria.
3. Training data and sim-to-real or cross-embodiment conditions.
4. Matched baselines and deployment latency.
5. Per-task result counts with uncertainty.
6. Representative failures and safety-relevant limitations.

### Theory with supporting experiments

Use when: Experiments illustrate or stress-test a formal result.

1. Question tied to the theorem or assumption.
2. Synthetic setting that isolates the predicted behavior.
3. Metric and parameter regime.
4. Comparison with the predicted trend or bound.
5. Realistic setting, if used, clearly separated from proof.
6. Conditions where empirical behavior departs from the theory.

## Select one domain reporting overlay

Apply only the overlay matching the empirical domain; do not load a second protocol for these checks.

### Reinforcement learning

- Separate environment interactions, gradient updates, episodes, wall-clock time, replay ratio, and offline transition count; never report them as one generic sample budget.
- Name the environment version, observation and action interfaces, horizon or termination rule, reward convention, and any score normalization reference.
- Report evaluation episodes per seed, independent training seeds, aggregation across tasks, uncertainty, and the checkpoint-selection protocol.
- For offline RL, describe dataset provenance, behavior-policy mixture, support or coverage diagnostics, and whether any online interaction or evaluation data informed tuning.

### World models

- Separate one-step prediction, multi-step open-loop rollout, closed-loop planning, and downstream policy evidence; none is a substitute for another.
- Report prediction target, latent or observation space, action conditioning, context length, rollout horizon, replanning interval, and stochastic sampling procedure.
- State whether planning uses ground-truth observations between decisions and whether reward, value, termination, or uncertainty heads are learned.
- Evaluate compounding error across horizons and connect control claims to return, success, constraint, or planning metrics under a named interaction budget.

### Embodied AI and robot learning

- Name simulator and real-system conditions separately, including platform, sensing, workspace, control loop, safety constraints, and sim-to-real differences.
- Define a trial, reset, intervention, timeout, partial completion, and success denominator; report per-task counts and uncertainty rather than only a pooled percentage.
- Describe demonstrations by task, trajectory, timestep, operator, embodiment, and collection policy when these affect data comparability.
- Make held-out objects, scenes, tasks, instructions, users, and embodiments distinct generalization axes and disclose selection on any held-out condition.

### Vision-language-action models

- Report pretraining and robot data mixtures, embodiment-specific heads, action representation, prediction horizon, execution horizon, and feedback or replanning interval.
- Separate model-query latency, action-chunk generation time, effective control frequency, end-to-end task time, and hardware or precision conditions.
- State whether evaluation is open-loop prediction, closed-loop control, simulation, or physical deployment and avoid transferring conclusions across those regimes.
- Name instruction, object, scene, task, and embodiment splits separately; report adaptation, prompting, fine-tuning, or calibration used at evaluation time.

## Verification

- Every main empirical claim has a visible row in the claim–evidence matrix.
- Numbers and method labels agree across Abstract, Experiments, captions, tables, figures, and appendix.
- Absolute changes, relative changes, and percentage-point changes are labeled correctly.
- Comparison conclusions name the matched and unmatched resources.
- Metric direction, units, denominator, number of runs, and uncertainty are recoverable without guessing.
- Supplement placement follows current venue rules; critical evidence is not hidden behind an optional review path.

## Avoid

- Calling a study comprehensive because it contains many datasets without covering the paper's actual claim axes.
- Reporting only favorable seeds, tasks, checkpoints, qualitative examples, or hyperparameter ranges.
- Attributing a gain to one component from a tiny or noisy ablation difference.
- Treating simulation success, offline metrics, open-loop prediction, and closed-loop deployment as interchangeable evidence.
- Using an appendix pointer to replace the minimum protocol information needed to interpret a main result.

## Retrieve related sentence cards only as needed

- [For a controlled comparison, we hold {factor} fixed and vary only {factor}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.fair-comparison.001.md) — `general.sentence-pattern.fair-comparison.001`
- [Unless otherwise specified, we use {default configuration} in all experiments.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.reproducibility-default.001.md) — `general.sentence-pattern.reproducibility-default.001`
- [Removing {component} reduces {metric}, indicating that {bounded interpretation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.ablation.001.md) — `general.sentence-pattern.ablation.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [At a matched {budget}, {method} yields {verified comparison}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-matched-budget.001.md) — `general.sentence-pattern.rebuttal-matched-budget.001`
- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [statistically significant versus substantial improvement](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.significant.001.md) — `general.usage-note.significant.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
