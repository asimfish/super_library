# Super Library one-file route: Vision-language-action experimental protocol

`experiments.vision_language_action` · domain `vision_language_action` · section `experiments` · intent `evidence`

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

##### Vision-language-action models

- Report pretraining and robot data mixtures, embodiment-specific heads, action representation, prediction horizon, execution horizon, and feedback or replanning interval.
- Separate model-query latency, action-chunk generation time, effective control frequency, end-to-end task time, and hardware or precision conditions.
- State whether evaluation is open-loop prediction, closed-loop control, simulation, or physical deployment and avoid transferring conclusions across those regimes.
- Name instruction, object, scene, task, and embodiment splits separately; report adaptation, prompting, fine-tuning, or calibration used at evaluation time.

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

### All methods use the same {resource budget}; remaining differences are {differences}.

`general.sentence-pattern.resource-parity.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States one controlled comparison resource while disclosing consequential factors that remain unmatched.

**Use:** Name data, environment interaction, parameters, training compute, tuning, or evaluation budgets precisely. Do not imply full fairness from one matched resource.

**Avoid:** Avoid the blanket phrase 'under fair settings' without listing matched and unmatched factors.

**Patterns:**

- All methods use the same {interaction budget}; model size and pretraining data differ as noted in {location}.
- Training data are matched across methods, while {baseline} uses {additional resource}.

### Latency is measured on {hardware} with {precision, batch, and timing boundary}.

`general.sentence-pattern.latency-protocol.001` · sentence_pattern · general, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the hardware and measurement boundary required to interpret latency.

**Use:** State warm-up, synchronization, repeats, input shape, preprocessing, action decoding, and whether the value is model-only or end to end.

**Avoid:** Do not compare latency across hardware or confuse batched throughput with single-sample latency.

**Patterns:**

- Latency is measured on {hardware} at {precision} and batch size {value}, including {timing boundary}.
- End-to-end control latency includes {components} and is averaged over {repetitions} after {warm-up}.

### policy inference latency and control frequency

`vla.usage-note.control-latency.001` · usage_note · vision_language_action, robot_learning · experiments, limitations, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Inference latency measures computation time per policy update, while control frequency describes how often commands are issued; chunking and asynchronous execution can make them differ.

**Use:** Report hardware, batch size, observation resolution, action horizon, synchronization policy, latency statistic, and achieved control rate.

**Avoid:** Do not infer deployability from model size or nominal frequency alone.

**Patterns:**

- On {hardware}, the policy requires {latency statistic} per update and sustains {frequency} Hz with {execution scheme}.

**Verify in primary sources:**

- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)
- `zheng2025-tracevla-visual-trace-prompting` — [TraceVLA: Visual Trace Prompting Enhances Spatial-Temporal Awareness for Generalist Robotic Policies](https://iclr.cc/virtual/2025/poster/29130) (ICLR 2025)

### open-loop action prediction versus closed-loop execution

`vla.usage-note.open-closed-loop.001` · usage_note · vision_language_action, robot_learning · method, experiments, related_work, limitations

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Open-loop prediction generates an action sequence without incorporating intermediate observations, whereas closed-loop execution refreshes observations and may replan during the sequence.

**Use:** Report prediction horizon, executed chunk length, observation refresh rate, and replanning frequency separately.

**Avoid:** Do not call a chunked policy fully closed-loop merely because a new chunk is eventually predicted.

**Patterns:**

- The policy predicts {prediction horizon} actions, executes {execution horizon}, and replans after receiving a new observation.

**Verify in primary sources:**

- `li2025-reinforcement-learning-action-chunking` — [Reinforcement Learning with Action Chunking](https://proceedings.neurips.cc/paper_files/paper/2025/hash/50348e8f9aef984abe0ea1ec2a326f78-Abstract-Conference.html) (NeurIPS 2025)
- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)

### separate prediction horizon, execution horizon, and feedback frequency

`emb.usage-note.chunking-feedback.001` · usage_note · embodied_ai, robot_learning, vision_language_action · method, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy may predict many future actions while executing only part of them before receiving a new observation, so action horizon alone does not determine whether control is open-loop or closed-loop.

**Use:** Report all three quantities and explain how overlapping predictions are combined. Use 'closed-loop' only when updated observations influence subsequent executed actions.

**Avoid:** Do not infer the control-feedback structure solely from the number of actions output by the network.

**Patterns:**

- Although the policy predicts {k} actions, it replans after executing {n}, using a new observation.
- The controller executes the entire chunk open-loop before the next policy query.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
