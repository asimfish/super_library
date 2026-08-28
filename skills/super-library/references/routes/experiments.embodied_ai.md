# Super Library one-file route: Embodied-AI and real-robot experimental protocol

`experiments.embodied_ai` · domain `embodied_ai` · section `experiments` · intent `evidence`

This file is a bounded language context, not scientific evidence. Draft
from the user's verified facts, adapt every pattern, and reopen linked
primary papers before definitions, comparisons, or literature claims.
Do not load the core, catalogs, guide, or cards again for this task.

## Compact contract

- Preserve numbers, notation, negation, uncertainty, comparison direction,
  evaluation scope, and citation placement.
- Prefer field-standard terminology; do not copy a paper sentence or retain
  an unresolved placeholder.
- Bind empirical language to the named protocol, metric, denominator,
  aggregation, uncertainty, and comparison set.
- State evidence before interpretation and retain exceptions, trade-offs,
  null results, and failure boundaries that affect the claim.

## Task protocol

### Super Library protocol: Experiments: claim-to-evidence protocol

`experiments` · `section_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Design and write an experimental section in which each major empirical claim is tested under an explicit protocol and bounded interpretation.

**Use when:** Planning or writing the complete empirical evaluation, before selecting a specialized table or analysis guide.

#### Required inputs

- Empirical claim list and one research question per claim.
- Datasets, tasks, splits, environments, embodiments, populations, and held-out units.
- Metrics with direction, units, denominator, aggregation unit, and decision relevance.
- Baseline implementations, training data, pretraining, tuning, parameter, compute, and interaction budgets.
- Seeds or trials, checkpoint and hyperparameter selection protocol, uncertainty statistic, and statistical tests when used.
- Hardware, software versions, training and evaluation compute, real-system safety constraints, and failure records.

#### Functional protocol

##### 1. Create the claim–evidence matrix (required)

- For every claim, record research question, comparison axis, protocol, metric, display, and allowed interpretation.
- Place claim-critical evidence in the main paper when the venue warns that reviewers may not consult appendices.
- Remove experiments that do not test a stated claim or label them exploratory.

##### 2. Define evaluation scope (required)

- Describe task, data provenance, split construction, held-out unit, and evaluation population.
- For embodied work, distinguish simulation from real-system trials and name the control loop, intervention, reset, and success denominator.
- For RL, distinguish environment steps, gradient steps, episodes, wall-clock time, and offline data size.

##### 3. Define metrics and statistical unit (required)

- State whether higher or lower is better, the unit, and the averaging unit.
- Report the number of independent seeds, runs, scenes, tasks, episodes, or trials and avoid treating correlated samples as independent.
- Name mean, median, standard deviation, standard error, confidence interval, or percentile explicitly.

##### 4. Establish baseline fairness (required)

- Record implementation source, version, reproduction changes, and tuning protocol for each baseline.
- Disclose material differences in pretraining data, model scale, supervision, compute, and interaction budget.
- Do not bold a result as best when protocols are not comparable.

##### 5. Answer the primary research questions (required)

- Lead each result paragraph with the question or comparison axis.
- Point to the display, quantify the relevant difference, state consistency or exceptions, then give a calibrated interpretation.
- Report null, negative, unstable, or adverse results when they bear on the claim.

##### 6. Add only claim-relevant analyses (conditional)

- Use ablation for component or mechanism claims, generalization for named shifts, robustness for named perturbations, and efficiency for named resources.
- Add sensitivity or scaling analysis when a conclusion depends on a chosen hyperparameter or scale.
- Include qualitative examples and failure cases when metrics conceal behavior relevant to deployment.

##### 7. Close reproducibility gaps (required)

- Provide enough implementation and evaluation detail to reconstruct the reported protocol.
- State code, data, simulator, benchmark, and model availability only as actually provided.
- Use the target venue's current reproducibility checklist or statement and point to manuscript locations.

#### Choose one internal template

##### Standard empirical evaluation

Use when: The paper has benchmarked quantitative claims.

1. Research questions or evaluation goals.
2. Tasks, datasets, splits, and metrics.
3. Baselines and fairness controls.
4. Implementation, selection, and statistical protocol.
5. Main results organized by research question.
6. Ablation or mechanism analysis.
7. Generalization, robustness, efficiency, qualitative behavior, or failures only as claim-relevant.
8. Scope summary and appendix pointers.

##### Real-robot or real-system evaluation

Use when: Physical deployment or human intervention is part of the evidence.

1. Platform, sensing, control frequency, workspace, safety protocol, and task definitions.
2. Trial independence, reset procedure, intervention policy, denominator, and success criteria.
3. Training data and sim-to-real or cross-embodiment conditions.
4. Matched baselines and deployment latency.
5. Per-task result counts with uncertainty.
6. Representative failures and safety-relevant limitations.

##### Theory with supporting experiments

Use when: Experiments illustrate or stress-test a formal result.

1. Question tied to the theorem or assumption.
2. Synthetic setting that isolates the predicted behavior.
3. Metric and parameter regime.
4. Comparison with the predicted trend or bound.
5. Realistic setting, if used, clearly separated from proof.
6. Conditions where empirical behavior departs from the theory.

#### Domain reporting overlay

Apply this domain-specific reporting layer together with the general protocol.

##### Embodied AI and robot learning

- Name simulator and real-system conditions separately, including platform, sensing, workspace, control loop, safety constraints, and sim-to-real differences.
- Define a trial, reset, intervention, timeout, partial completion, and success denominator; report per-task counts and uncertainty rather than only a pooled percentage.
- Describe demonstrations by task, trajectory, timestep, operator, embodiment, and collection policy when these affect data comparability.
- Make held-out objects, scenes, tasks, instructions, users, and embodiments distinct generalization axes and disclose selection on any held-out condition.

#### Verification

- Every main empirical claim has a visible row in the claim–evidence matrix.
- Numbers and method labels agree across Abstract, Experiments, captions, tables, figures, and appendix.
- Absolute changes, relative changes, and percentage-point changes are labeled correctly.
- Comparison conclusions name the matched and unmatched resources.
- Metric direction, units, denominator, number of runs, and uncertainty are recoverable without guessing.
- Supplement placement follows current venue rules; critical evidence is not hidden behind an optional review path.

#### Avoid

- Calling a study comprehensive because it contains many datasets without covering the paper's actual claim axes.
- Reporting only favorable seeds, tasks, checkpoints, qualitative examples, or hyperparameter ranges.
- Attributing a gain to one component from a tiny or noisy ablation difference.
- Treating simulation success, offline metrics, open-loop prediction, and closed-loop deployment as interchangeable evidence.
- Using an appendix pointer to replace the minimum protocol information needed to interpret a main result.

#### Retrieve related sentence cards only as needed

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

## Selected language records

### Each real-system condition is evaluated in {trials} trials, with success defined as {criterion}.

`general.sentence-pattern.real-system-trials.001` · sentence_pattern · general, embodied_ai, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the trial count and success criterion for a physical or deployed-system evaluation.

**Use:** Also state reset procedure, intervention policy, trial independence, task allocation, and the denominator used for success rate.

**Avoid:** Do not report a success percentage without the number and composition of physical trials.

**Patterns:**

- Each real-robot task is evaluated in {trials} trials, with success defined as {terminal condition}.
- We conduct {number} trials per {task and object} pair and count an intervention as {outcome}.

### Failure cases are dominated by {category}, accounting for {fraction} of {denominator}.

`general.sentence-pattern.failure-denominator.001` · sentence_pattern · general · experiments, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports a failure category with its frequency and explicit denominator.

**Use:** Define a mutually interpretable failure taxonomy, label multi-cause cases, and state whether categories were assigned manually or automatically.

**Avoid:** Do not select illustrative failures without reporting how frequently they occur in the evaluated population.

**Patterns:**

- Failure cases are dominated by {category}, accounting for {count} of {total} unsuccessful trials.
- Among {denominator}, {fraction} involve {condition}; category labels were assigned using {procedure}.

### All methods use the same {resource budget}; remaining differences are {differences}.

`general.sentence-pattern.resource-parity.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States one controlled comparison resource while disclosing consequential factors that remain unmatched.

**Use:** Name data, environment interaction, parameters, training compute, tuning, or evaluation budgets precisely. Do not imply full fairness from one matched resource.

**Avoid:** Avoid the blanket phrase 'under fair settings' without listing matched and unmatched factors.

**Patterns:**

- All methods use the same {interaction budget}; model size and pretraining data differ as noted in {location}.
- Training data are matched across methods, while {baseline} uses {additional resource}.

### Higher values of {metric} indicate {meaning}; results are averaged over {unit}.

`general.sentence-pattern.metric-direction-unit.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines metric direction, interpretation, and the statistical unit used for aggregation.

**Use:** Use 'lower' where appropriate and name whether the unit is task, scene, episode, trial, seed, or example.

**Avoid:** Do not let readers infer whether a metric is a percentage, fraction, count, error, or normalized score.

**Patterns:**

- Higher values of {metric} indicate {capability}; results are averaged over {tasks} and then over {seeds}.
- Lower {metric} indicates {meaning}; each value is averaged over {evaluation unit}.

### task success rate

`emb.term.task-success-rate.001` · term · embodied_ai, robot_learning, vision_language_action · experiments, rebuttal, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The fraction or percentage of evaluation trials that satisfy a predefined task-completion criterion.

**Use:** Define the success criterion, trial unit, number of trials, aggregation level, and treatment of partial completion and timeouts. Provide uncertainty where appropriate.

**Avoid:** Do not compare success rates computed with different horizons, reset policies, human interventions, or success detectors without qualification.

**Patterns:**

- Task success rate is computed over {number} independent trials using {completion criterion}.
- The policy succeeds in {count}/{total} trials, corresponding to {percentage}%.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)

### evaluate embodied generalization along separately controlled axes

`emb.usage-note.systematic-generalization.001` · usage_note · embodied_ai, robot_learning, vision_language_action · experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Systematic evaluation varies identified factors—such as objects, placements, task templates, prompt compositions, environments, or embodiments—while documenting which combinations were withheld.

**Use:** Define each split procedurally and report results by axis. Use 'zero-shot' only when the evaluated factor or combination was absent from training under the stated protocol.

**Avoid:** Do not collapse all held-out conditions into one generalization score that hides qualitatively different shifts.

**Patterns:**

- We report separate results for unseen objects, unseen task compositions, and unseen embodiments.
- The hardest split holds out both {factor one} and {factor two} during training.

**Verify in primary sources:**

- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
