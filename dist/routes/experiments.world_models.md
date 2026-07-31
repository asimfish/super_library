# Super Library one-file route: World-model experimental protocol

`experiments.world_models` · domain `world_models` · section `experiments` · intent `evidence`

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

`experiments` · `section_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

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

##### World models

- Separate one-step prediction, multi-step open-loop rollout, closed-loop planning, and downstream policy evidence; none is a substitute for another.
- Report prediction target, latent or observation space, action conditioning, context length, rollout horizon, replanning interval, and stochastic sampling procedure.
- State whether planning uses ground-truth observations between decisions and whether reward, value, termination, or uncertainty heads are learned.
- Evaluate compounding error across horizons and connect control claims to return, success, constraint, or planning metrics under a named interaction budget.

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

- [For a controlled comparison, we hold {factor} fixed and vary only {factor}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.fair-comparison.001.md) — `general.sentence-pattern.fair-comparison.001`
- [Unless otherwise specified, we use {default configuration} in all experiments.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.reproducibility-default.001.md) — `general.sentence-pattern.reproducibility-default.001`
- [Removing {component} reduces {metric}, indicating that {bounded interpretation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.ablation.001.md) — `general.sentence-pattern.ablation.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [At a matched {budget}, {method} yields {verified comparison}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.rebuttal-matched-budget.001.md) — `general.sentence-pattern.rebuttal-matched-budget.001`
- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [statistically significant versus substantial improvement](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.usage-note.significant.001.md) — `general.usage-note.significant.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.

## Selected language records

### Higher values of {metric} indicate {meaning}; results are averaged over {unit}.

`general.sentence-pattern.metric-direction-unit.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines metric direction, interpretation, and the statistical unit used for aggregation.

**Use:** Use 'lower' where appropriate and name whether the unit is task, scene, episode, trial, seed, or example.

**Avoid:** Do not let readers infer whether a metric is a percentage, fraction, count, error, or normalized score.

**Patterns:**

- Higher values of {metric} indicate {capability}; results are averaged over {tasks} and then over {seeds}.
- Lower {metric} indicates {meaning}; each value is averaged over {evaluation unit}.

### We report {statistic} over {number} independent {runs or seeds}.

`general.sentence-pattern.independent-runs.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States the aggregation statistic and number of independent repetitions.

**Use:** Replace the statistical unit precisely and explain nested averaging when episodes or scenes occur within seeds. Name uncertainty separately.

**Avoid:** Avoid 'averaged over multiple runs' when the count, independence, and dispersion are not given.

**Patterns:**

- We report the mean and standard deviation over {number} independent seeds.
- Values are medians over {number} runs, with {interval} percentiles in parentheses.

### All methods use the same {resource budget}; remaining differences are {differences}.

`general.sentence-pattern.resource-parity.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States one controlled comparison resource while disclosing consequential factors that remain unmatched.

**Use:** Name data, environment interaction, parameters, training compute, tuning, or evaluation budgets precisely. Do not imply full fairness from one matched resource.

**Avoid:** Avoid the blanket phrase 'under fair settings' without listing matched and unmatched factors.

**Patterns:**

- All methods use the same {interaction budget}; model size and pretraining data differ as noted in {location}.
- Training data are matched across methods, while {baseline} uses {additional resource}.

### model rollout horizon trades synthetic coverage against accumulated error

`wm.usage-note.rollout-horizon.001` · usage_note · world_models, reinforcement_learning · method, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Increasing the number of learned transitions can provide more synthetic experience but also exposes training or planning to errors that compound under the rollout distribution.

**Use:** Treat rollout length as an algorithmic choice tied to model accuracy and policy shift. Report its schedule and include a sensitivity study when central to the claim.

**Avoid:** Do not state that shorter or longer model rollouts are universally better across data regimes and tasks.

**Patterns:**

- We use a rollout horizon of {k}; longer rollouts degrade {metric} as prediction errors accumulate.
- The rollout horizon increases from {a} to {b} as the model is trained on more real data.

**Verify in primary sources:**

- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)

### one-step accuracy does not by itself establish long-horizon fidelity

`wm.usage-note.one-vs-multistep.001` · usage_note · world_models · method, experiments, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Accurate next-step prediction and stable recursive rollout are related but distinct evaluation properties.

**Use:** Report multi-step or task-level metrics when the downstream method unrolls the model. Specify open-loop versus closed-loop evaluation.

**Avoid:** Do not use low one-step loss as the sole evidence that a model supports long-horizon planning.

**Patterns:**

- Although the model achieves low one-step error, we separately evaluate rollout fidelity over {horizon}.
- One-step prediction accuracy does not by itself establish decision-relevant long-horizon fidelity.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)

### online planning versus policy learning in imagination

`wm.usage-note.planning-vs-policy.001` · usage_note · world_models, reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

World models may support decisions by optimizing actions at test time, by training an amortized policy on imagined experience, or by combining both.

**Use:** State when computation occurs and whether the deployed controller replans. This is a useful axis for organizing related work.

**Avoid:** Do not classify all world-model methods as planners.

**Patterns:**

- Whereas {method family} performs online planning in the learned model, {method family} trains a policy on imagined trajectories.
- Our method combines {online trajectory optimization} with {learned value or policy prior}.

**Verify in primary sources:**

- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/routes/index.md) only for a different task.
