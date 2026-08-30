# Super Library pack: general

Corpus `0.4.0` · snapshot `2026-08-09`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [selective agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) and [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md) before using this exhaustive pack.

### generalization ability / robustness ability

`general.anti-pattern.ability-noun.001` · anti_pattern · general · abstract, introduction, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

These noun stacks often conceal the evaluated shift or perturbation and can sound like literal translations rather than operational claims.

**Use:** Prefer 'generalization to {held-out condition}', 'robustness to {perturbation}', or the exact measured outcome. 'Capability' is acceptable only when its scope is stated.

**Avoid:** Do not replace the phrase with an equally vague adjective such as 'strong generalizability.'

**Patterns:**

- We evaluate generalization to unseen {objects} and robustness to {perturbation}.
- The policy succeeds under {specified shift} in {fraction} of trials.

### more superior / more optimal

`general.anti-pattern.more-superior.001` · anti_pattern · general · abstract, introduction, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Redundant comparative forms that obscure the actual comparison dimension.

**Use:** Use 'outperforms' for a verified metric comparison, 'is more effective' with a criterion, or simply report the numbers.

**Avoid:** Do not intensify inherently comparative or absolute adjectives.

**Patterns:**

- {method} outperforms {baseline} on {metric} in {setting}.

### perform good / get better performance

`general.anti-pattern.perform-good.001` · anti_pattern · general · abstract, introduction, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Non-idiomatic or underspecified performance wording often produced by literal translation.

**Use:** Use 'performs well' only for an informal summary; in papers, prefer 'achieves higher {metric}' or a quantified comparison.

**Avoid:** Avoid 'perform good', 'gets a good result', and comparison without a metric or baseline.

**Patterns:**

- {method} achieves higher {metric} than {baseline} under {protocol}.

### We compare {method} to {baselines}.

`general.phrase.compare-to.001` · phrase · general · experiments, related_work, rebuttal, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Introduces a direct comparison set.

**Use:** Name baselines and disclose protocol mismatches. 'Compare with' is also grammatical, but use one form consistently.

**Avoid:** Do not use a direct comparison frame when data, compute, split, or evaluation protocol is materially incompatible without a caveat.

**Patterns:**

- We compare {method} to {baseline set} at a matched {data or interaction budget}.

**Usage attestations:**

- `kumar2020cql` — Section 6, experiments
- `haarnoja2018sac` — Section 6, experiments
- `hansen2022tdmpc` — Section 5 and appendix

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### We demonstrate that {empirical finding}.

`general.phrase.demonstrate.001` · phrase · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

States a finding supported by the paper's experiments or analysis.

**Use:** Use only for evidence actually reported in the paper, and bind the statement to its setting. Prefer 'show' or 'find' if 'demonstrate' would overstate the design.

**Avoid:** Do not use this phrase for an aspiration, untested mechanism, or causal conclusion unsupported by the experiment.

**Patterns:**

- We demonstrate that {method} {measured behavior} across {evaluated scope}.

**Usage attestations:**

- `haarnoja2018sac` — Abstract
- `khazatsky2024droid` — Abstract

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)

### a range of downstream tasks

`general.phrase.downstream-range.001` · phrase · general · abstract, introduction, experiments, conclusion, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Refers to several named applications used to test whether a learned representation, model, or policy transfers beyond its training objective.

**Use:** Name the downstream tasks and state whether evaluation uses frozen features, prompting, fine-tuning, planning, or policy learning.

**Avoid:** Do not use range to conceal a small or homogeneous evaluation set, and do not imply zero-shot transfer when adaptation is used.

**Patterns:**

- We assess {representation or model} on a range of downstream tasks under {adaptation protocol}: {named tasks}.

**Usage attestations:**

- `wu2024-ivideogpt-interactive-videogpts-scalable` — Official abstract
- `hao2025-neural-motion-simulator-pushing` — Official abstract
- `wang2025-vq-vla-improving-vision` — Official abstract

**Verify in primary sources:**

- `wu2024-ivideogpt-interactive-videogpts-scalable` — [iVideoGPT: Interactive VideoGPTs are Scalable World Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html) (NeurIPS 2024)
- `hao2025-neural-motion-simulator-pushing` — [Neural Motion Simulator Pushing the Limit of World Models in Reinforcement Learning](https://openaccess.thecvf.com/content/CVPR2025/html/Hao_Neural_Motion_Simulator_Pushing_the_Limit_of_World_Models_in_CVPR_2025_paper.html) (CVPR 2025)
- `wang2025-vq-vla-improving-vision` — [VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers](https://openaccess.thecvf.com/content/ICCV2025/html/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.html) (ICCV 2025)

### We evaluate {method} on {benchmarks or tasks}.

`general.phrase.evaluate-on.001` · phrase · general · experiments, rebuttal, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Introduces the empirical evaluation scope.

**Use:** Name representative benchmarks, tasks, environments, or datasets and then state metrics and protocols. Use 'across' when emphasizing coverage over multiple groups.

**Avoid:** Do not imply broad evaluation with an unspecified 'various datasets.'

**Patterns:**

- We evaluate {method} on {number} {tasks or benchmarks} spanning {scope}.

**Usage attestations:**

- `hafner2019planet` — Section 5, experiments
- `hansen2022tdmpc` — Introduction and Section 5
- `kumar2020cql` — Section 6, experiments

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)

### We find that {observed pattern}.

`general.phrase.find-that.001` · phrase · general · experiments, conclusion, rebuttal, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Reports an observed empirical pattern in a measured, comparatively neutral voice.

**Use:** Use for a result discovered through analysis or experiments. Follow with the measurement and avoid implying a mechanism that was not isolated.

**Avoid:** Do not substitute 'we find that' for the actual result or omit exceptions.

**Patterns:**

- Across {evaluation units}, we find that {observed pattern}.

**Usage attestations:**

- `khazatsky2024droid` — Introduction and Section V
- `savva2019habitat` — Section 4, experiments
- `haarnoja2018sac` — Introduction and conclusion

**Verify in primary sources:**

- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)
- `savva2019habitat` — [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) (ICCV 2019)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

### In contrast to {comparison class}, {difference}.

`general.phrase.in-contrast.001` · phrase · general · introduction, related_work, method, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Marks a technically relevant contrast with a named method family, assumption, or setting.

**Use:** Keep the comparison axis parallel and support the characterization of the cited class. Use 'whereas' when contrasting two clauses is more concise.

**Avoid:** Do not contrast one method's best property with another method's unrelated weakness.

**Patterns:**

- In contrast to {method family}, our approach {difference on the same technical axis}.

**Usage attestations:**

- `haarnoja2018sac` — Abstract
- `hansen2022tdmpc` — Introduction

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

### We introduce {concept or resource}.

`general.phrase.introduce.001` · phrase · general · abstract, introduction, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Announces a newly defined task, concept, dataset, or resource.

**Use:** Follow with an appositive definition or operational description. Prefer this over decorative novelty claims.

**Avoid:** Do not use 'introduce' when merely reviewing an existing concept.

**Patterns:**

- We introduce {name}, a {resource type} designed to {purpose}.

**Usage attestations:**

- `chen2020soundspaces` — Abstract
- `khazatsky2024droid` — Abstract
- `shridhar2020alfred` — Introduction, first paragraph

**Verify in primary sources:**

- `chen2020soundspaces` — [SoundSpaces: Audio-Visual Navigation in 3D Environments](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123510018.pdf) (ECCV 2020)
- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)
- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)

### We present {artifact or framework}.

`general.phrase.present.001` · phrase · general · abstract, introduction, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Introduces a method, platform, dataset, benchmark, or analysis without asserting novelty through an adjective.

**Use:** Name the artifact and its role. This concise opening is useful when 'propose' would be unnatural for a benchmark or platform.

**Avoid:** Do not leave the object vague, as in 'we present a new solution,' without specifying what it is.

**Patterns:**

- We present {artifact}, a {type} for {purpose}.

**Usage attestations:**

- `shridhar2020alfred` — Abstract
- `savva2019habitat` — Abstract

**Verify in primary sources:**

- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)
- `savva2019habitat` — [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) (ICCV 2019)

### In this paper, we propose {method}.

`general.phrase.propose.001` · phrase · general · abstract, introduction, method, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Introduces the paper's proposed method or formulation directly.

**Use:** Use once near the first precise method statement. Replace 'paper' with 'work' only for local style consistency; explain the method immediately after naming it.

**Avoid:** Do not repeat this stock opening for every contribution or use 'propose' for an analysis that has already been established elsewhere.

**Patterns:**

- In this paper, we propose {method}, which {core mechanism or capability}.

**Usage attestations:**

- `hafner2019planet` — Abstract
- `haarnoja2018sac` — Abstract
- `kumar2020cql` — Abstract

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)

### Our results suggest that {bounded interpretation}.

`general.phrase.results-suggest.001` · phrase · general · experiments, conclusion, limitations, rebuttal, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Offers a cautious interpretation supported by results without claiming definitive proof.

**Use:** Use when evidence supports an interpretation but does not fully establish it. State the evaluated regime and relevant uncertainty.

**Avoid:** Do not use 'suggest' to hide a result that is null, inconsistent, or unsupported.

**Patterns:**

- Our results suggest that {mechanism or design choice} may improve {measured capability} in {setting}.

**Usage attestations:**

- `haarnoja2018sac` — Conclusion
- `zhu2025unifiedworld` — Abstract

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `zhu2025unifiedworld` — [Unified World Models: Coupling Video and Action Diffusion for Pretraining on Large Robotic Datasets](https://www.roboticsproceedings.org/rss21/p015.html) (RSS 2025)

### We show that {result}.

`general.phrase.show.001` · phrase · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Reports a result established within the stated theoretical or empirical scope.

**Use:** State the evidence boundary in the same sentence or nearby. For empirical work, include the task, benchmark, or protocol; for theory, name the assumptions.

**Avoid:** Do not let 'show' silently upgrade correlation to causation or a finite benchmark result to universal validity.

**Patterns:**

- We show that {method} improves {metric} on {benchmark} under {protocol}.

**Usage attestations:**

- `kumar2020cql` — Abstract
- `shridhar2020alfred` — Abstract

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)

### in both simulated and real-world {environments or experiments}

`general.phrase.simulated-real-world.001` · phrase · general · abstract, experiments, conclusion, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

States that a method or finding was evaluated in simulation and on a physical or otherwise genuinely deployed real-world system.

**Use:** Name the simulator, real platform, number of trials, and any protocol differences; report the two result groups separately when they are not directly comparable.

**Avoid:** Do not call a recorded real-world dataset a real-world deployment or merge simulated and physical results into one unsupported claim.

**Patterns:**

- We evaluate {method} in both simulated and real-world {environments}, using {matched or separately described protocols}.

**Usage attestations:**

- `zhu2024-retrieval-augmented-embodied-agents` — Official abstract
- `li2025-object-centric-prompt-driven` — Official abstract
- `lu2025-gwm-scalable-gaussian-world` — Official abstract
- `zhu2025-move-understand-3d-scene` — Official abstract

**Verify in primary sources:**

- `zhu2024-retrieval-augmented-embodied-agents` — [Retrieval-Augmented Embodied Agents](https://openaccess.thecvf.com/content/CVPR2024/html/Zhu_Retrieval-Augmented_Embodied_Agents_CVPR_2024_paper.html) (CVPR 2024)
- `li2025-object-centric-prompt-driven` — [Object-Centric Prompt-Driven Vision-Language-Action Model for Robotic Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Li_Object-Centric_Prompt-Driven_Vision-Language-Action_Model_for_Robotic_Manipulation_CVPR_2025_paper.html) (CVPR 2025)
- `lu2025-gwm-scalable-gaussian-world` — [GWM: Towards Scalable Gaussian World Models for Robotic Manipulation](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_GWM_Towards_Scalable_Gaussian_World_Models_for_Robotic_Manipulation_ICCV_2025_paper.html) (ICCV 2025)
- `zhu2025-move-understand-3d-scene` — [Move to Understand a 3D Scene: Bridging Visual Grounding and Exploration for Efficient and Versatile Embodied Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_Move_to_Understand_a_3D_Scene_Bridging_Visual_Grounding_and_ICCV_2025_paper.html) (ICCV 2025)

### {unit} not seen during training

`general.phrase.unseen-during-training.001` · phrase · general · abstract, experiments, limitations, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Identifies a held-out evaluation unit relative to the training data or task distribution.

**Use:** Replace unit with the exact held-out axis—environment, task, object, embodiment, instruction, or combination—and describe how the split was constructed.

**Avoid:** Do not imply broad out-of-distribution generalization when only one named axis was held out.

**Patterns:**

- We evaluate on {unit} not seen during training while holding {other factors} fixed.

**Usage attestations:**

- `koh2021pathdreamer` — Official abstract
- `mazoure2022-improving-zero-shot-generalization` — Official abstract
- `wen2025-diffusionvla-scaling-robot-foundation` — Official abstract

**Verify in primary sources:**

- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)
- `mazoure2022-improving-zero-shot-generalization` — [Improving Zero-Shot Generalization in Offline Reinforcement Learning using Generalized Similarity Functions](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9fbdfded5c4d2969d889efc72f85c644-Abstract-Conference.html) (NeurIPS 2022)
- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)

### across a wide spectrum of {tasks or settings}

`general.phrase.wide-spectrum.001` · phrase · general · abstract, introduction, experiments, conclusion, translation

**Provenance:** `attested_collocation` · **Quality:** `gold+reviewed`

Signals deliberately broad coverage across named tasks, settings, or conditions.

**Use:** Use only when the evaluation spans substantively different cases, and name the covered spectrum in the same sentence or immediately after it.

**Avoid:** Do not use wide spectrum as decorative emphasis for several variants of one narrow task.

**Patterns:**

- We evaluate {method} across a wide spectrum of {named tasks or settings}, including {representative cases}.

**Usage attestations:**

- `fan2022-minedojo-building-open-ended` — Official abstract
- `jiang2024-reinforcement-learning-friendly-vision` — Official abstract
- `huang2024-embodied-generalist-agent-3d` — Official abstract

**Verify in primary sources:**

- `fan2022-minedojo-building-open-ended` — [MineDojo: Building Open-Ended Embodied Agents with Internet-Scale Knowledge](https://proceedings.neurips.cc/paper_files/paper/2022/hash/74a67268c5cc5910f64938cac4526a90-Abstract-Datasets_and_Benchmarks.html) (NeurIPS 2022)
- `jiang2024-reinforcement-learning-friendly-vision` — [Reinforcement Learning Friendly Vision-Language Model for Minecraft](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/8467_ECCV_2024_paper.php) (ECCV 2024)
- `huang2024-embodied-generalist-agent-3d` — [An Embodied Generalist Agent in 3D World](https://proceedings.mlr.press/v235/huang24ae.html) (ICML 2024)

### The joint variant differs from the sum of individual changes, suggesting an interaction between {components}.

`general.sentence-pattern.ablation-interaction.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Describes non-additive ablation behavior as evidence consistent with a component interaction.

**Use:** Use only when the factorial variants and common reference permit the comparison. Quantify the observed non-additivity and uncertainty.

**Avoid:** Do not infer interaction from unrelated single-drop variants or unmatched optimization settings.

**Patterns:**

- The joint variant changes {metric} by {value}, compared with {individual effects}, suggesting an interaction between {components}.
- The benefit of {component A} appears only with {component B}, consistent with their intended coupling.

### Removing {component} reduces {metric}, indicating that {bounded interpretation}.

`general.sentence-pattern.ablation.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Connects an ablation result to a component-level interpretation.

**Use:** Report the size and uncertainty where possible. 'Indicating' should introduce a bounded interpretation rather than a causal universal.

**Avoid:** Do not conclude that a component is necessary in every setting from one ablation.

**Patterns:**

- Removing {component} reduces {metric} from {a} to {b}, indicating that it contributes to {capability} in {setting}.

### For {task}, existing methods remain limited by {specific constraint}.

`general.sentence-pattern.abstract-gap.001` · sentence_pattern · general · abstract, introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces a concrete research gap tied to a task and a named constraint.

**Use:** Use only after verifying that the closest relevant methods share the stated constraint. Name the setting in which it matters.

**Avoid:** Avoid replacing the constraint with 'limited performance' or implying that every prior method has the same weakness.

**Patterns:**

- For {task}, existing methods remain limited by {assumption} when {condition}.
- In {setting}, current approaches require {resource or supervision}, which restricts {capability}.

### Our key insight is that {insight}, which enables {capability}.

`general.sentence-pattern.abstract-insight.001` · sentence_pattern · general · abstract, introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States the conceptual observation that motivates the method and connects it to a scoped capability.

**Use:** Express a technical relationship that the paper actually establishes or uses. Follow with the mechanism that realizes it.

**Avoid:** Do not use 'key insight' for a restatement of the method name or an unsupported causal story.

**Patterns:**

- Our key insight is that {representation property} permits {operation}, which enables {capability}.
- The central observation is that {condition}; this motivates {design choice}.

### We introduce {method}, which {mechanism} to {objective}.

`general.sentence-pattern.abstract-method.001` · sentence_pattern · general · abstract, introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Names the contribution and summarizes its operative mechanism and objective in one sentence.

**Use:** Replace the slots with the paper-level mechanism, not a list of low-level implementation details. Use the exact method name from the manuscript.

**Avoid:** Avoid chaining several modules with 'novel' adjectives without explaining their function.

**Patterns:**

- We introduce {method}, which combines {mechanisms} to {objective}.
- We develop {method}, a {method class} that {mechanism} for {task}.

### Across {evaluation scope}, {method} changes {metric} by {value} relative to {comparator}.

`general.sentence-pattern.abstract-result.001` · sentence_pattern · general · abstract, experiments, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports one principal verified result with its evaluation scope, metric, magnitude, and comparator.

**Use:** Specify whether the value is absolute, relative, or in percentage points. Use the same aggregation and comparison set as the referenced display.

**Avoid:** Do not average incompatible tasks or select the largest favorable result while implying it summarizes the full study.

**Patterns:**

- Across {number} {tasks}, {method} improves {metric} by {value} percentage points over {comparator}.
- Under {shift}, {method} reduces {error metric} from {baseline value} to {method value}.

### These results support {scoped conclusion} under {evaluated conditions}.

`general.sentence-pattern.abstract-scope.001` · sentence_pattern · general · abstract, conclusion, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Closes an empirical summary with a conclusion bounded by the actual evaluation.

**Use:** Name the datasets, tasks, shifts, assumptions, or system conditions that bound the conclusion when they are material.

**Avoid:** Avoid turning benchmark evidence into an unrestricted claim about real-world deployment or general intelligence.

**Patterns:**

- These results support {conclusion} for {task family} under {protocol}.
- The evidence supports transfer across {held-out axis}, but does not establish {broader scope}.

### Baseline results are {rerun or sourced} using {implementation and version}.

`general.sentence-pattern.baseline-provenance.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Records whether baseline numbers were reproduced or taken from a source and identifies the implementation.

**Use:** State code commit or release, consequential changes, tuning policy, and whether the reported protocol matches the present evaluation.

**Avoid:** Do not mix rerun and copied numbers without labeling their provenance and compatibility.

**Patterns:**

- Baseline results are reproduced using the authors' {release} with {documented changes}.
- Results marked with {symbol} are taken from {verified source}; all others are rerun under our protocol.

### Across {units the material states}, {method} improves {metric} by {stated amount}.

`general.sentence-pattern.calibrated-strength.001` · sentence_pattern · general · abstract, experiments, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Matches verb strength to evidential status: plain declaratives for measured results, hedges only for claims the material marks as unmeasured.

**Use:** When the material states a measured result, report it with a direct verb and its stated scope. Reserve 'may', 'might', and 'potentially' for statements the material itself marks as untested. Never delete a hedge if doing so widens the claim beyond the stated evidence.

**Avoid:** Do not write 'may potentially improve' for a gain the material measures, and do not promote an untested setting to a direct claim by dropping its hedge.

**Patterns:**

- Across {stated number} tasks, {method} improves {metric} from {stated baseline value} to {stated value}.
- On the {stated split}, {method} reduces {failure mode} by {stated amount}; settings beyond this split were not evaluated.

### Ablation of {components} with all variants trained under {matched protocol}.

`general.sentence-pattern.caption-ablation.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces an ablation caption and states the matched condition needed to compare variants.

**Use:** Define component indicators, full-model row, metric, runs, uncertainty, and any retuning policy in the remaining caption.

**Avoid:** Do not claim a matched ablation when variants use different data, budgets, selection, or evaluation.

**Patterns:**

- Ablation of {components} with all variants trained under the same {data and compute budget}. Values report {statistic} over {seeds}.
- Component analysis on {task}; the full model is {row}, and each variant changes {factor}.

### Quality and deployment cost measured under {hardware and timing protocol}.

`general.sentence-pattern.caption-efficiency.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Frames an efficiency caption around both outcome quality and a reproducibly measured deployment resource.

**Use:** Name hardware, precision, batch, input, warm-up, timing boundary, repeats, resource units, and metric directions.

**Avoid:** Do not label a table efficiency when it reports only parameter count or latency without task quality.

**Patterns:**

- Quality and deployment cost measured on {hardware} at {precision} and batch size {value}. Latency includes {boundary}.
- Task success and control latency under {deployment protocol}; values report {statistic} over {repeats}.

### Generalization from {training condition} to {held-out condition}.

`general.sentence-pattern.caption-generalization.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Names the training and held-out conditions at the start of a generalization-table caption.

**Use:** Continue with the held-out unit, selection protocol, metrics, runs, uncertainty, and reference condition.

**Avoid:** Do not use 'unseen' without specifying what was withheld and whether it influenced model selection.

**Patterns:**

- Generalization from {training environments} to held-out {environments}. Test environments are excluded from training and validation.
- Transfer from {embodiments} to unseen {embodiments}; success rates are averaged over {trials}.

### Results on {dataset or task} under {protocol}. {Metric direction and units}.

`general.sentence-pattern.caption-main-results.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Provides the first two functional sentences of a self-contained main-results caption.

**Use:** Continue with aggregation, uncertainty, runs, emphasis, and protocol exceptions. Use the exact split and evaluation setting.

**Avoid:** Do not use a one-phrase caption that forces readers to reconstruct the protocol from the prose.

**Patterns:**

- Results on {tasks} under the {split} protocol. Higher {metric} is better; values are {units} and report {statistic} over {runs}.
- Evaluation on {environment} with {budget}. Lower {metric} is better, and bold marks the best comparable result.

### Sensitivity to {parameter}; {default marker} denotes the selected configuration.

`general.sentence-pattern.caption-sensitivity.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces a sensitivity caption and identifies the configuration used elsewhere in the paper.

**Use:** State the full range, selection data and objective, fixed factors, runs, uncertainty, and changed resource when scale varies.

**Avoid:** Do not show only values near the chosen optimum or imply a scaling law from a narrow sweep.

**Patterns:**

- Sensitivity to {parameter}; the dagger denotes the validation-selected configuration. All other settings and seeds are fixed.
- Scaling with {data or model size}; bold identifies the configuration used for the main experiments, not an oracle test optimum.

### These results are consistent with the hypothesis that {mechanism}.

`general.sentence-pattern.causal-caution.001` · sentence_pattern · general · experiments, limitations, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Links observations to a mechanism without claiming that the experiment identifies causality.

**Use:** Use when evidence supports but does not isolate the proposed explanation. Follow with an ablation or limitation if available.

**Avoid:** Do not write 'the gains are due to' without an identifying intervention.

**Patterns:**

- These results are consistent with the hypothesis that {component or inductive bias} improves {measured behavior}.

### We present {method}, which {capability the supplied results state} on {evaluated setting}.

`general.sentence-pattern.claim-forward-opening.001` · sentence_pattern · general · abstract, introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Opens with the contribution itself instead of a disclaimer about what the work does not do or does not claim.

**Use:** Lead with the strongest claim the supplied evidence states, then bound it; every capability named must appear in the material's stated results. Strength comes from claiming exactly what the evidence supports, not from claiming more.

**Avoid:** Do not open with 'does not attempt', 'is not intended to', or an apology before the contribution is stated; never widen a claim beyond the supplied evidence to sound more confident.

**Patterns:**

- We present {method}, which improves {metric} by {stated amount} across {evaluated benchmarks}.
- We show that {supported finding}, based on {evidence the material states}.

### Unlike {comparison class}, which {defining behavior}, our approach {distinct behavior}.

`general.sentence-pattern.contrast.001` · sentence_pattern · general · introduction, related_work, method

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Contrasts two methods on one explicit mechanism or assumption.

**Use:** Keep the grammatical comparison parallel and verify that the characterization holds for the cited comparison class.

**Avoid:** Do not compare your full method with one isolated weakness of a baseline.

**Patterns:**

- Unlike {method family}, which relies on {assumption}, our approach {mechanism without that assumption}.

### Our main contribution is {artifact or insight} that {verified capability}.

`general.sentence-pattern.contribution.001` · sentence_pattern · general · abstract, introduction, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States the central contribution and its demonstrated capability in one sentence.

**Use:** Name a method, analysis, dataset, benchmark, or finding. Bind the capability to the evaluated scope.

**Avoid:** Do not use 'novel' as a substitute for explaining what is contributed.

**Patterns:**

- Our main contribution is {method or analysis} that {capability} under {evaluated conditions}.

### We use {term} to denote {operational meaning}.

`general.sentence-pattern.define.001` · sentence_pattern · general · introduction, related_work, method, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces a local, operational meaning for a term.

**Use:** Use when the paper needs a definition whose scope is specific to the present formulation. State the defining property, not a circular synonym.

**Avoid:** Do not imply that a local convention is the field's only accepted definition.

**Patterns:**

- We use {term} to denote {entity or process satisfying explicit conditions}.

### In this work, {term} refers to {scope-bounded definition}.

`general.sentence-pattern.define.002` · sentence_pattern · general · introduction, related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines a term while making the scope of the definition explicit.

**Use:** Use when community usage is broader than the aspect studied in the paper. Follow with inclusions or exclusions if ambiguity remains.

**Avoid:** Do not use this frame to silently redefine a standard term for rhetorical convenience.

**Patterns:**

- In this work, {term} refers specifically to {property within the studied setting}.

### We evaluate {method} on {tasks} using {metrics} under {protocol}.

`general.sentence-pattern.experiment-overview.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces the evaluation scope, outcome measures, and protocol in one compact sentence.

**Use:** Name the actual tasks, principal metrics, split or evaluation regime, and any material simulation or deployment condition.

**Avoid:** Avoid 'we conduct extensive experiments' without stating what questions or settings are evaluated.

**Patterns:**

- We evaluate {method} on {benchmarks} using {metrics} under a matched {budget}.
- We evaluate in {simulation or real system} on {tasks}, reporting {metrics} under {protocol}.

### Failure cases are dominated by {category}, accounting for {fraction} of {denominator}.

`general.sentence-pattern.failure-denominator.001` · sentence_pattern · general · experiments, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports a failure category with its frequency and explicit denominator.

**Use:** Define a mutually interpretable failure taxonomy, label multi-cause cases, and state whether categories were assigned manually or automatically.

**Avoid:** Do not select illustrative failures without reporting how frequently they occur in the evaluated population.

**Patterns:**

- Failure cases are dominated by {category}, accounting for {count} of {total} unsuccessful trials.
- Among {denominator}, {fraction} involve {condition}; category labels were assigned using {procedure}.

### For a controlled comparison, we hold {factor} fixed and vary only {factor}.

`general.sentence-pattern.fair-comparison.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Explains how an experiment isolates a comparison dimension.

**Use:** Use only when the protocol truly controls the named factor; list remaining mismatches if they affect interpretation.

**Avoid:** Do not call a comparison controlled when data, compute, architecture, or tuning differs materially.

**Patterns:**

- For a controlled comparison, we hold {data and compute budget} fixed and vary only {model component}.

### Our formulation builds on {foundation} and extends it to {new setting or capability}.

`general.sentence-pattern.foundation.001` · sentence_pattern · general · related_work, method

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States intellectual continuity and the precise extension contributed by the paper.

**Use:** Cite the foundation and explain what changes in the new formulation. Use 'extends' only when the technical relationship is real.

**Avoid:** Do not erase the contribution of the foundational method.

**Patterns:**

- Our formulation builds on {named framework} and extends it to {setting} by {technical modification}.

### An important next step is to evaluate {capability} under {condition}.

`general.sentence-pattern.future.001` · sentence_pattern · general · limitations, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Identifies a concrete unresolved evaluation or research direction.

**Use:** Use for work not completed in the current paper. Prefer a falsifiable next step over generic aspirations.

**Avoid:** Do not write as though the proposed future experiment has already succeeded.

**Patterns:**

- An important next step is to evaluate {capability} under {distribution shift or deployment condition}.

### Despite progress in {area}, existing methods remain limited by {specific limitation}.

`general.sentence-pattern.gap.001` · sentence_pattern · general · introduction, related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Identifies a research gap without dismissing prior progress.

**Use:** The limitation must be supported and relevant to the proposed contribution. Specify the affected regime, assumption, or metric.

**Avoid:** Do not claim that all existing methods fail when only a subset was examined.

**Patterns:**

- Despite progress in {capability}, existing methods remain limited by {assumption or failure mode} in {setting}.

### The {split} holds out {unit} from all training and selection data.

`general.sentence-pattern.heldout-split.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines a held-out unit and excludes it from both model fitting and selection.

**Use:** Name whether the unit is subject, scene, object, task, environment, embodiment, or temporal block. Disclose any preprocessing learned globally.

**Avoid:** Do not call a test condition unseen if it influenced prompts, hyperparameters, checkpoint selection, or data curation.

**Patterns:**

- The test split holds out {objects} from all training and validation trajectories.
- For cross-environment evaluation, {environments} are excluded from both training and model selection.

### We report {statistic} over {number} independent {runs or seeds}.

`general.sentence-pattern.independent-runs.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States the aggregation statistic and number of independent repetitions.

**Use:** Replace the statistical unit precisely and explain nested averaging when episodes or scenes occur within seeds. Name uncertainty separately.

**Avoid:** Avoid 'averaged over multiple runs' when the count, independence, and dispersion are not given.

**Patterns:**

- We report the mean and standard deviation over {number} independent seeds.
- Values are medians over {number} runs, with {interval} percentiles in parentheses.

### Within {scope}, the closest approaches can be compared along {axis one} and {axis two}.

`general.sentence-pattern.intro-approach-axes.001` · sentence_pattern · general · introduction, related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Organizes related approach families by explicit technical dimensions relevant to the present argument.

**Use:** Choose verified axes such as representation, supervision, data, decision rule, interaction regime, or deployment assumption.

**Avoid:** Do not manufacture a taxonomy that collapses technically heterogeneous work or omits the closest method.

**Patterns:**

- Within {task}, the closest approaches can be compared by how they represent {entity} and obtain {supervision}.
- Existing methods can be distinguished by {decision mechanism} and {interaction regime}.

### The design addresses {challenge} by {technical choice}.

`general.sentence-pattern.intro-challenge-design.001` · sentence_pattern · general · introduction, method

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Maps one emphasized challenge to the corresponding design mechanism.

**Use:** Use the same challenge and component names throughout the Introduction, Method, and experiments. Avoid implying causal sufficiency without evidence.

**Avoid:** Do not introduce a challenge that no design element or experiment addresses.

**Patterns:**

- The design addresses {challenge} by conditioning {mechanism} on {signal}.
- To handle {challenge}, the model uses {technical choice}.

### Our contributions are evaluated through {research questions}.

`general.sentence-pattern.intro-contribution-evidence.001` · sentence_pattern · general · introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Frames empirical contributions as questions that the Experiments section is designed to answer.

**Use:** Replace the slot with two or three concrete questions or evaluation axes. Pair non-empirical contributions with theorems, resources, or analyses instead.

**Avoid:** Avoid treating the mere number of experiments as a contribution.

**Patterns:**

- We evaluate whether {method} improves {outcome}, transfers across {shift}, and reduces {resource}.
- The experiments test {main comparison}, {mechanism claim}, and {deployment boundary}.

### We focus on {scope}; {non-goal} remains outside the present study.

`general.sentence-pattern.intro-nongoal.001` · sentence_pattern · general · introduction, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States an explicit boundary that prevents an overbroad reading of the contribution.

**Use:** Use for a material assumption or non-goal, especially when motivation is broader than evaluation. Keep it consistent with Limitations.

**Avoid:** Do not use a non-goal to dismiss a comparison or safety issue that is essential to the central claim.

**Patterns:**

- We focus on {evaluated setting}; transfer to {unseen setting} remains outside the present study.
- Our analysis concerns {formal regime} and does not establish {broader guarantee}.

### Motivated by this observation, we design {mechanism} to {goal}.

`general.sentence-pattern.intro-observation-design.001` · sentence_pattern · general · introduction, method

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Bridges a stated insight or empirical observation to the paper's design response.

**Use:** Ensure the antecedent observation directly motivates the mechanism. Name the technical goal rather than 'better performance.'

**Avoid:** Avoid using the transition when the design choice is unrelated to the preceding limitation.

**Patterns:**

- Motivated by this observation, we design {mechanism} to preserve {property}.
- This analysis motivates {design choice}, which targets {failure mode}.

### This work studies {task} under {operational setting}.

`general.sentence-pattern.intro-operational-scope.001` · sentence_pattern · general · introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the paper's task and setting before broader motivation or method details.

**Use:** Specify the decision, observation, data, interaction, or deployment regime that makes the task operationally distinct.

**Avoid:** Avoid beginning from an expansive societal claim when the paper evaluates a narrower technical setting.

**Patterns:**

- This work studies {task} under {observation and action constraints}.
- We consider {task} in the {offline, online, simulated, or real-system} setting.

### This assumption becomes restrictive when {condition}, because {consequence}.

`general.sentence-pattern.intro-restrictive-assumption.001` · sentence_pattern · general · introduction, related_work, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Connects a verified method assumption to the condition under which it limits the target capability.

**Use:** State the assumption, triggering condition, and consequence explicitly. Support literature and empirical claims with primary evidence.

**Avoid:** Do not describe a design difference as restrictive without showing why it matters for the task.

**Patterns:**

- This assumption becomes restrictive when {shift}, because {technical consequence}.
- The requirement for {resource} limits deployment in {setting}, where {constraint}.

### Latency is measured on {hardware} with {precision, batch, and timing boundary}.

`general.sentence-pattern.latency-protocol.001` · sentence_pattern · general, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the hardware and measurement boundary required to interpret latency.

**Use:** State warm-up, synchronization, repeats, input shape, preprocessing, action decoding, and whether the value is model-only or end to end.

**Avoid:** Do not compare latency across hardware or confuse batched throughput with single-sample latency.

**Patterns:**

- Latency is measured on {hardware} at {precision} and batch size {value}, including {timing boundary}.
- End-to-end control latency includes {components} and is averaged over {repetitions} after {warm-up}.

### {Method} assumes {stated condition}; the supplied evidence does not evaluate {setting beyond that condition}.

`general.sentence-pattern.limitation-boundary.001` · sentence_pattern · general · limitations, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States a limitation as a concrete boundary plus its evidential status, rather than as an apology or a speculative failure claim.

**Use:** Bind the boundary to conditions the material states. Mark unevaluated settings as unevaluated instead of predicting degradation or failure in them; a limitation names what the evidence does not cover, not a defect the evidence does not establish.

**Avoid:** Do not apologize for a limitation, and do not assert that performance degrades or fails in settings the evidence never tested.

**Patterns:**

- Our experiments assume {stated condition}; behavior under {other condition} was not evaluated.
- {Method} relies on {stated resource}; settings without it are untested rather than known failure cases.

### Our evaluation is limited to {scope}; performance under {unseen condition} remains to be established.

`general.sentence-pattern.limitation.001` · sentence_pattern · general · limitations, conclusion, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States an evaluation boundary and separates tested from untested conditions.

**Use:** Name the missing population, environment, scale, horizon, embodiment, or distribution. Do not bury a material limitation.

**Avoid:** Do not turn a limitation into an unsupported claim that future work will certainly solve it.

**Patterns:**

- Our evaluation is limited to {tasks or environments}; robustness to {shift} remains to be established.

### Higher values of {metric} indicate {meaning}; results are averaged over {unit}.

`general.sentence-pattern.metric-direction-unit.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines metric direction, interpretation, and the statistical unit used for aggregation.

**Use:** Use 'lower' where appropriate and name whether the unit is task, scene, episode, trial, seed, or example.

**Avoid:** Do not let readers infer whether a metric is a percentage, fraction, count, error, or normalized score.

**Patterns:**

- Higher values of {metric} indicate {capability}; results are averaged over {tasks} and then over {seeds}.
- Lower {metric} indicates {meaning}; each value is averaged over {evaluation unit}.

### A central challenge is to {objective} while {constraint}.

`general.sentence-pattern.motivate.001` · sentence_pattern · general · abstract, introduction, related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Motivates a problem through a concrete objective–constraint tension.

**Use:** Name both the desired capability and the condition that makes it difficult. Prefer measurable constraints over adjectives such as challenging or complex.

**Avoid:** Avoid an empty claim such as 'This is a very challenging problem.'

**Patterns:**

- A central challenge is to {achieve capability} while {respecting data, compute, safety, or deployment constraint}.

### Prior approaches differ primarily in {axis one} and {axis two}.

`general.sentence-pattern.position.001` · sentence_pattern · general · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Organizes related work by technical comparison axes instead of paper-by-paper chronology.

**Use:** Choose axes that expose meaningful assumptions or design choices, then place representative methods along them with citations.

**Avoid:** Do not invent a taxonomy whose categories overlap without explanation.

**Patterns:**

- Prior approaches differ primarily in how they {technical axis one} and whether they {technical axis two}.

### Our setting is most closely related to {family}, but differs in {assumption or objective}.

`general.sentence-pattern.position.002` · sentence_pattern · general · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Positions the present work relative to the nearest literature family.

**Use:** Name the closest family before the distinction. The difference should be technically consequential, not cosmetic.

**Avoid:** Avoid claiming complete novelty merely because the exact combination has not appeared.

**Patterns:**

- Our setting is most closely related to {method family}, but differs in its assumption of {assumption} and its objective of {objective}.

### {Method} targets {setting the material states}; {one adjacent setting} is outside the scope of this work.

`general.sentence-pattern.positive-scope.001` · sentence_pattern · general · abstract, introduction, method, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States scope by what the work covers, with at most one deliberate exclusion, instead of a chain of defensive disclaimers.

**Use:** Name the covered scope positively from the supplied material. Keep only the exclusions a reader needs to avoid misusing the result; an exclusion is a boundary statement, not an apology.

**Avoid:** Do not stack multiple 'we do not claim' clauses when one positive scope sentence carries the same boundary; do not restate the covered scope as a list of things the work is not.

**Patterns:**

- {Method} addresses {stated problem class}; extending it to {adjacent class} is left to future work.
- Our evaluation covers {stated benchmarks and budget}; deployment-scale settings are outside the scope of this study.

### {method} improves {metric} by {value} relative to {baseline} under {protocol}.

`general.sentence-pattern.quantify.001` · sentence_pattern · general · abstract, experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports a quantified comparison with its baseline and protocol.

**Use:** State whether the value is absolute or relative, and match the aggregation and uncertainty used in the table.

**Avoid:** Avoid 'significant' unless statistical significance was actually tested.

**Patterns:**

- {method} improves mean {metric} by {absolute or relative value} over {baseline} under the {protocol} protocol.

### Each real-system condition is evaluated in {trials} trials, with success defined as {criterion}.

`general.sentence-pattern.real-system-trials.001` · sentence_pattern · general, embodied_ai, robot_learning, vision_language_action · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines the trial count and success criterion for a physical or deployed-system evaluation.

**Use:** Also state reset procedure, intervention policy, trial independence, task allocation, and the denominator used for success rate.

**Avoid:** Do not report a success percentage without the number and composition of physical trials.

**Patterns:**

- Each real-robot task is evaluated in {trials} trials, with success defined as {terminal condition}.
- We conduct {number} trials per {task and object} pair and count an intervention as {outcome}.

### We agree that {concern} is important; our current evidence addresses {covered scope}.

`general.sentence-pattern.rebuttal-acknowledge.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Acknowledges a valid concern while delimiting what the current paper can support.

**Use:** Use when the concern is valid but broader than the submitted evidence. State the uncovered portion explicitly if space permits.

**Avoid:** Do not say 'we agree' and then dismiss the concern without engaging it.

**Patterns:**

- We agree that {evaluation dimension} is important; our current evidence addresses {specific subset}, while {uncovered condition} remains outside scope.

### Yes. {direct answer}; the supporting evidence is {evidence pointer}.

`general.sentence-pattern.rebuttal-answer.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Answers a reviewer question immediately and then points to evidence.

**Use:** Use when the answer is genuinely yes. Replace the first token with 'No' or a qualified answer when appropriate; never force agreement.

**Avoid:** Do not begin with a long thank-you paragraph that delays the answer.

**Patterns:**

- Yes. {claim bounded to the question}; the supporting evidence is reported in {table, figure, section, or verified result}.

### We apologize for the ambiguity: {precise clarification}.

`general.sentence-pattern.rebuttal-clarify.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Acknowledges unclear presentation and states the intended meaning directly.

**Use:** Use only when the manuscript wording could reasonably cause the misunderstanding. Follow with the exact revision.

**Avoid:** Do not blame the reviewer for a misunderstanding caused by unclear writing.

**Patterns:**

- We apologize for the ambiguity: {term or claim} refers to {precise scope}, not {plausible alternative reading}.

### This is a limitation of the current study, but it does not affect {narrower conclusion}.

`general.sentence-pattern.rebuttal-concede.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Makes a bounded concession while preserving a conclusion supported by existing evidence.

**Use:** Use only when the narrower conclusion truly survives the limitation. Explain why with evidence or logic.

**Avoid:** Do not minimize a limitation that invalidates the main claim.

**Patterns:**

- This is a limitation of the current study, but it does not affect our conclusion about {claim within tested scope} because {reason}.

### The reviewer is correct that {specific statement}; we will correct {location} accordingly.

`general.sentence-pattern.rebuttal-correct.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Accepts a concrete factual or presentation error without conceding claims that are unaffected by it.

**Use:** Name the exact error, give the corrected statement, and reassess any downstream conclusion that depends on it.

**Avoid:** Do not use a cosmetic correction frame when the issue invalidates the main analysis.

**Patterns:**

- The reviewer is correct that {quantity or label} was stated incorrectly; we will replace it with {correct value} in {location}.
- The reviewer is correct that our wording implied {overbroad claim}; we will narrow it to {supported scope}.

### The requested comparison is already included in {location}, where {verified result}.

`general.sentence-pattern.rebuttal-evidence.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Points a reviewer to existing evidence and summarizes only the relevant result.

**Use:** Give an exact manuscript location and reproduce numbers faithfully. If absent, use a revision or limitation frame instead.

**Avoid:** Do not invent a table location or imply that an indirect analysis answers the request.

**Patterns:**

- The requested comparison is already included in {Table or Appendix}, where {method} achieves {verified metric} under {protocol}.

### At a matched {budget}, {method} yields {verified comparison}.

`general.sentence-pattern.rebuttal-matched-budget.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Frames a comparison under an explicitly controlled data, interaction, parameter, compute, or tuning budget.

**Use:** Name the matched resource and disclose other material differences. Report the exact statistic and uncertainty used in the manuscript.

**Avoid:** Do not call a comparison budget-matched when only one of several dominant resources is controlled.

**Patterns:**

- At a matched interaction budget of {value}, {method} obtains {metric}, compared with {baseline result}.
- When parameter count is matched, the difference in {metric} is {value}.

### We do not currently have evidence for {broader claim}; we will restrict the manuscript to {supported claim}.

`general.sentence-pattern.rebuttal-no-evidence.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Responds to a request that cannot be supported with existing results by narrowing the claim instead of inventing evidence.

**Use:** Use when the requested experiment was not run or the available analysis is insufficient. Explain what existing evidence still supports.

**Avoid:** Do not imply that an unrun experiment produced a favorable result or promise a result whose outcome is unknown.

**Patterns:**

- We do not currently have evidence for robustness under {shift}; we will restrict the manuscript to the evaluated {scope}.
- The requested comparison is not available in the current submission, so we will remove the corresponding general claim.

### We will revise {location} to make {point} explicit.

`general.sentence-pattern.rebuttal-revision.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Commits to a concrete presentation change in response to feedback.

**Use:** Name the section, statement, figure, caption, or experimental detail and the information to add. Do not promise a new result unless it exists.

**Avoid:** Avoid vague promises such as 'we will improve the paper.'

**Patterns:**

- We will revise {Section or caption} to make {assumption, protocol, or limitation} explicit.

### A complementary line of work studies {adjacent problem}.

`general.sentence-pattern.related-family.001` · sentence_pattern · general · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces adjacent literature that informs but does not directly solve the same problem.

**Use:** Explain the relationship after the topic sentence: shared tool, assumption, representation, or evaluation setting.

**Avoid:** Do not label directly competing methods as merely complementary to evade comparison.

**Patterns:**

- A complementary line of work studies {adjacent problem}, sharing our interest in {common element} but targeting {different objective}.

### These approaches share {common objective}, but differ in {technical axes}.

`general.sentence-pattern.related-synthesis.001` · sentence_pattern · general · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Synthesizes a family of papers through one commonality and one or more technically relevant differences.

**Use:** Support the shared property and each difference with verified citations. Select axes that connect directly to the present method.

**Avoid:** Do not force heterogeneous work into one family merely because papers use similar architectures.

**Patterns:**

- These approaches share the objective of {objective}, but differ in their assumptions about {axis one} and {axis two}.
- While both families address {problem}, they obtain supervision from {different sources}.

### Unless otherwise specified, we use {default configuration} in all experiments.

`general.sentence-pattern.reproducibility-default.001` · sentence_pattern · general · method, experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Declares a shared experimental default while allowing explicitly identified exceptions.

**Use:** State the actual default and enumerate consequential exceptions where they occur. Do not use the frame to hide benchmark-specific tuning.

**Avoid:** Avoid a global default statement when several experiments use materially different protocols.

**Patterns:**

- Unless otherwise specified, we report the mean over {number} seeds and use {aggregation rule}.
- Unless otherwise specified, all methods use the same {data, compute, or interaction budget}.

### All methods use the same {resource budget}; remaining differences are {differences}.

`general.sentence-pattern.resource-parity.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States one controlled comparison resource while disclosing consequential factors that remain unmatched.

**Use:** Name data, environment interaction, parameters, training compute, tuning, or evaluation budgets precisely. Do not imply full fairness from one matched resource.

**Avoid:** Avoid the blanket phrase 'under fair settings' without listing matched and unmatched factors.

**Patterns:**

- All methods use the same {interaction budget}; model size and pretraining data differ as noted in {location}.
- Training data are matched across methods, while {baseline} uses {additional resource}.

### On {metric}, {method} changes {baseline value} to {method value}, an {absolute or relative} difference of {value}.

`general.sentence-pattern.result-absolute-relative.001` · sentence_pattern · general · abstract, experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports both endpoint values and labels the comparison as absolute or relative.

**Use:** For percentages, distinguish percentage-point differences from relative percent changes. Retain the metric unit and aggregation.

**Avoid:** Avoid 'improves by 10%' when readers cannot tell whether this means ten percentage points or ten percent relative.

**Patterns:**

- On {metric}, {method} increases the score from {value} to {value}, a gain of {points} percentage points.
- The error decreases from {value} to {value}, corresponding to a {relative value}% relative reduction.

### Performance degrades under {condition}, which limits the claim to {scope}.

`general.sentence-pattern.result-boundary.001` · sentence_pattern · general · experiments, limitations, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Connects an observed failure condition to the boundary it imposes on the paper's claim.

**Use:** Quantify the degradation, state the denominator, and distinguish a sampled failure condition from a universal boundary.

**Avoid:** Do not bury a condition that directly contradicts an Abstract or Introduction claim.

**Patterns:**

- Performance degrades under {shift}, which limits the claim to {evaluated range}.
- Success falls from {value} to {value} for {condition}; we therefore restrict the conclusion to {scope}.

### The improvement is concentrated in {conditions}, whereas {other conditions} show {outcome}.

`general.sentence-pattern.result-concentration.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Identifies where an aggregate gain arises and contrasts it with conditions showing a different pattern.

**Use:** Use subgroup or condition-level results that were defined or transparently labeled exploratory. Report denominators and uncertainty.

**Avoid:** Do not select favorable subgroups post hoc without disclosure or ignore degradation elsewhere.

**Patterns:**

- The improvement is concentrated in {long-horizon tasks}, whereas {short-horizon tasks} show comparable performance.
- Gains occur primarily under {shift}; in the reference condition, the methods differ by {value}.

### The advantage is consistent across {settings}, with {exceptions}.

`general.sentence-pattern.result-consistency.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Summarizes the breadth of an observed comparison while explicitly retaining exceptions.

**Use:** Name the settings and define consistency using the direction, effect range, uncertainty, or success frequency. Fill the exception slot even if the answer is none observed.

**Avoid:** Do not call a result consistent when only an average is positive or when important settings reverse the ranking.

**Patterns:**

- The advantage is consistent across {tasks}, except on {task}, where {outcome}.
- The direction is stable over {seeds or scales}, although the magnitude varies from {range}.

### This pattern is consistent with {hypothesis}, although {alternative} is not controlled.

`general.sentence-pattern.result-hypothesis-caution.001` · sentence_pattern · general · experiments, limitations, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Offers a mechanism interpretation while acknowledging a plausible uncontrolled explanation.

**Use:** Use after stating the observed result. Replace the slots with a testable hypothesis and a concrete confounder or alternative mechanism.

**Avoid:** Avoid 'this proves that the gain is due to' when the experiment does not identify the mechanism.

**Patterns:**

- This pattern is consistent with {mechanism}, although differences in {data or scale} are not controlled.
- The result suggests {explanation}; however, {alternative} could also account for the change.

### We observe no consistent advantage on {scope}; the difference remains within {uncertainty}.

`general.sentence-pattern.result-null.001` · sentence_pattern · general · experiments, rebuttal, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports a null or unstable comparison without converting it into evidence of equivalence.

**Use:** Name the uncertainty statistic and comparison scope. If equivalence matters, use an appropriate equivalence or non-inferiority design.

**Avoid:** Do not interpret a non-significant or noisy difference as proof that methods are identical.

**Patterns:**

- We observe no consistent advantage on {tasks}; differences vary in sign across {seeds}.
- The estimate differs by {value}, with a {confidence interval} that includes {reference}.

### This gain comes with {cost}, revealing a trade-off between {axes}.

`general.sentence-pattern.result-tradeoff.001` · sentence_pattern · general · experiments, limitations, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports a measured benefit together with the resource, quality, safety, or robustness cost that accompanies it.

**Use:** Quantify both axes under the same protocol and avoid causal language if the trade-off is only observational.

**Avoid:** Do not hide the cost in a footnote while presenting the gain as unqualified superiority.

**Patterns:**

- This gain comes with {latency increase}, revealing a trade-off between {accuracy} and {deployment speed}.
- Improved robustness is accompanied by {reference-condition change}, indicating a trade-off across {axes}.

### Variation across {seeds or trials} is {statistic}, indicating {bounded inference}.

`general.sentence-pattern.result-variability.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Uses a named variability statistic to qualify the stability of an empirical result.

**Use:** Name standard deviation, interquartile range, confidence interval, or another appropriate statistic and keep the inference modest.

**Avoid:** Do not call a method stable from one run or from low variation over correlated evaluation episodes.

**Patterns:**

- Variation across seeds is {standard deviation}, indicating that the ranking is {stable or uncertain} under this protocol.
- The interval across trials is {range}, so the observed difference should be interpreted as {bounded conclusion}.

### Could the authors report {specific quantity or protocol detail}? This would clarify {stated concern}.

`general.sentence-pattern.review-actionable-question.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Asks the authors for one concrete, answerable item and states what the answer would resolve.

**Use:** Target quantities recoverable from a standard experimental log or manuscript revision. One question per missing item, phrased neutrally.

**Avoid:** Avoid rhetorical or accusatory questions and compound questions that bundle several requests into one.

**Patterns:**

- Could the authors report the number of random seeds and the dispersion statistic used in Table {n}? This would clarify how stable the reported gains are.
- Could the authors state the training budget per method? This would clarify whether the comparison is matched.

### Given {listed strengths} and {unresolved weaknesses}, the current evidence supports {bounded judgment}.

`general.sentence-pattern.review-calibrated-assessment.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Closes a review with an overall judgment that traces explicitly to the listed strengths and weaknesses and no further.

**Use:** Weigh only items already established in the review body. Match the hedging strength to the evidence: firm where results are clear, open where reporting is incomplete.

**Avoid:** Do not introduce comparisons, claims, or scores absent from the review body, and do not let polish or novelty language substitute for the listed evidence.

**Patterns:**

- Given the clear formulation and strong results on {covered settings}, balanced against the missing {analysis}, the current evidence supports a cautiously positive assessment.
- The contribution is well motivated, but until {unresolved item} is addressed the empirical claim remains partially supported.

### The authors already acknowledge {limitation} in {location}; the open question is {boundary probe}.

`general.sentence-pattern.review-credit-disclosure.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Credits a limitation the submission itself discloses before probing its boundary, keeping the review fair to the authors' own reporting.

**Use:** Check the limitations section and experimental caveats before writing a weakness. If the point is disclosed, engage with its measured extent instead of presenting it as a discovery.

**Avoid:** Do not present a disclosed limitation as hidden, and do not imply concealment when the manuscript states the assumption.

**Patterns:**

- The authors already acknowledge the fixed-viewpoint assumption and quantify its cost; the open question is how the degradation scales with viewpoint change.
- The single-embodiment scope is disclosed in the limitations section; the remaining concern is whether the claimed mechanism depends on it.

### The {claim} rests on {reported evidence}, which supports {narrower statement} but not {claimed scope}.

`general.sentence-pattern.review-grounded-weakness.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States a review weakness by anchoring it to what the submission actually reports, separating the claim from the evidence behind it.

**Use:** Quote or locate the specific claim and the specific evidence before judging the gap. Keep the weakness about the submission's content, not about unverifiable properties.

**Avoid:** Do not assert properties the review packet cannot verify, such as reproducibility or hidden results, and do not restate a disagreement as a factual error.

**Patterns:**

- The generalization claim rests on results from {evaluated conditions}, which support robustness within that range but not the broader statement in the abstract.
- The comparison covers {included baselines}, which establishes progress over those methods but not the field-wide claim.

### The added {evidence} addresses {original concern}; {remaining concern} stands because {reason}.

`general.sentence-pattern.review-post-rebuttal.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Updates a review after the author response by explicitly closing concerns the new evidence resolves and restating the ones it does not.

**Use:** Concede addressed points plainly and separately from unresolved ones. Accept or keep open each remaining concern with a stated reason; do not add demands absent from the original review.

**Avoid:** Do not hold a resolved concern open without a reason, and do not flip the overall stance on points the response never addressed.

**Patterns:**

- The added multi-seed run addresses the stability concern; the missing baseline comparison stands, although the stated incompatibility is a reasonable ground.
- The clarified protocol resolves the comparability question; the scope concern stands because the new results remain within the original benchmark.

### Under {evaluated setting}, {method} consistently {measured outcome}.

`general.sentence-pattern.scope.001` · sentence_pattern · general · abstract, introduction, experiments, conclusion, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports a recurring empirical pattern with an explicit evaluation boundary.

**Use:** Use 'consistently' only when the pattern holds across the stated units. Name seeds, tasks, datasets, or metrics as appropriate.

**Avoid:** Do not generalize beyond the evaluated settings or omit exceptions.

**Patterns:**

- Across {tasks or datasets}, {method} consistently improves {metric} over {named comparison set}.

### This distinction matters because {consequence}.

`general.sentence-pattern.transition.001` · sentence_pattern · general · introduction, related_work, method, experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Connects a technical distinction to its consequence for the argument or evaluation.

**Use:** Use after defining two concepts or settings. The consequence should be explicit and locally relevant.

**Avoid:** Avoid a transition that merely repeats the distinction.

**Patterns:**

- This distinction matters because it determines whether {downstream consequence}.

### Although {qualified premise}, {bounded conclusion}.

`general.sentence-pattern.translation-preserve.001` · sentence_pattern · general · translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Preserves a concession and its qualification during Chinese-to-English reconstruction.

**Use:** Keep negation, modality, comparison direction, quantities, and citations attached to the same propositions as in the source.

**Avoid:** Do not upgrade a qualified Chinese claim into an unconditional English conclusion.

**Patterns:**

- Although {method} improves {metric} on {subset}, the difference is not statistically significant across {units}.

### Hyperparameters are selected on {validation set} using {criterion}.

`general.sentence-pattern.validation-selection.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Declares which data and objective selected hyperparameters or checkpoints.

**Use:** State whether one configuration is shared across tasks and whether test or shifted conditions influenced selection.

**Avoid:** Do not report test-optimal settings as if they were selected without access to test results.

**Patterns:**

- Hyperparameters are selected on {validation tasks} using {metric}, and the selected configuration is fixed for all test tasks.
- We select the checkpoint with the highest {validation metric} before evaluating it once on {test set}.

### inductive bias

`general.term.inductive-bias.001` · term · general · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A structural assumption built into an architecture, objective, or algorithm that restricts or prefers certain solutions before observing data, shaping what is learned and how much experience is required.

**Use:** Name the bias concretely (architecture, symmetry, prior connectivity, or objective structure), state the assumption it encodes about the task, and support claimed benefits with sample-efficiency, transfer, or ablation evidence rather than intuition.

**Avoid:** Do not credit an unspecified inductive bias for empirical gains, and do not present a bias as universally helpful without noting the tasks where its assumption fails.

**Patterns:**

- {Architecture choice} encodes an inductive bias toward {assumed structure}, improving {metric} in {regime}.
- Ablating {bias source} isolates its contribution to {sample-efficiency or transfer result}.

**Verify in primary sources:**

- `bhattasali2022-neural-circuit-architectural-priors` — [Neural Circuit Architectural Priors for Embodied Control](https://proceedings.neurips.cc/paper_files/paper/2022/hash/52e431bd7689d98426300cb103bb0ee3-Abstract-Conference.html) (NeurIPS 2022)

### defensive hedging versus calibrated claiming

`general.usage-note.anti-defensive-tone.001` · usage_note · general · abstract, introduction, conclusion, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Distinguishes protective hedges added to preempt criticism, such as preemptive apologies, stacked disclaimers, and unprompted concessions, from calibrated hedges that mark genuinely unmeasured claims.

**Use:** Remove hedges that guard against imagined objections when the material states the result plainly; keep hedges the evidence requires. Removing a hedge must never widen the claim beyond the supplied material: when in doubt, restate the scope positively instead of weakening the verb.

**Avoid:** Do not delete evidential qualifiers such as the sample size, split, or evaluated setting as if they were defensive tone; those qualifiers bind the claim to its evidence and must stay.

**Patterns:**

- Defensive: 'While our method may not generalize, it might potentially improve results.' Calibrated: 'Across {stated tasks}, our method improves {metric} by {stated amount}; other settings were not evaluated.'
- Defensive: 'We do not claim novelty, completeness, or optimality.' Calibrated: '{Method} targets {stated problem}; {one adjacent problem} is outside this work's scope.'

### replace vague effectiveness claims with the observed outcome

`general.usage-note.effectiveness.001` · usage_note · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

An effectiveness claim is informative only when it names the intervention, comparison, metric, and evaluated setting.

**Use:** Write the measured change directly. Use 'supports the effectiveness of' only when several results jointly justify the scoped judgment; use 'proves' only for a formal result.

**Avoid:** Avoid 'the experiments prove the effectiveness and superiority of our method.'

**Patterns:**

- Across {tasks}, {method} improves {metric} over {baselines} under a matched {budget}.
- The ablation supports the contribution of {component} to {measured outcome} in {setting}.

### name the generalization axis and held-out unit

`general.usage-note.generalization-axis.001` · usage_note · general, embodied_ai, robot_learning · abstract, introduction, experiments, limitations, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Generalization is always relative to a specified shift, such as unseen objects, tasks, environments, users, embodiments, or combinations.

**Use:** State what was held out during training and what unit is averaged at evaluation. Prefer 'generalization to unseen objects' over an unqualified 'generalization ability.'

**Avoid:** Do not infer broad out-of-distribution generalization from a random train–test split over nearly identical samples.

**Patterns:**

- We evaluate generalization to unseen {objects or tasks} by holding out {unit} during training.
- The current study does not establish transfer across unseen {embodiments or environments}.

### A dash denotes an unreported value, not a measured zero.

`general.usage-note.missing-zero-na.001` · usage_note · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Separates missing or unreported results from numeric zero and from conditions that are not applicable.

**Use:** Define every symbol in the caption or footnote. Use 0 or 0.0 only for a measured zero and N/A only when the metric or condition does not apply.

**Avoid:** Do not encode unavailable, failed, and zero-valued results with the same blank cell or dash.

**Patterns:**

- A dash denotes a result that was not reported; N/A indicates that the metric is not applicable.
- Zero is reported numerically, while failed runs are counted under {failure policy}.

### Distinguish possibility, interpretation, empirical evidence, and formal proof.

`general.usage-note.modality.001` · usage_note · general · abstract, introduction, related_work, experiments, limitations, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Modal verbs and evidential verbs serve different functions rather than forming one universal strength ordering.

**Use:** Use 'may/might' for possibility, 'suggests/supports' for a tentative interpretation or evidence relation, 'shows/demonstrates' for a result established within the study design, and 'proves' only for a formal proof under stated assumptions.

**Avoid:** Do not translate 可能 or 表明 into an unqualified 'proves', or assume that any two evidential verbs have a context-free ordering.

**Patterns:**

- The results suggest that {hypothesis}, but do not establish {stronger causal claim}.

### performance is usually a mass noun when reporting an aggregate result

`general.usage-note.performance.001` · usage_note · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

In empirical writing, 'performance' usually denotes aggregate measured behavior, whereas plural 'performances' is reserved for genuinely distinct acts or types of performance.

**Use:** Prefer 'improves performance,' 'achieves higher task success,' or the exact metric. Use a plural only when the sentence explicitly distinguishes multiple kinds of performance.

**Avoid:** Avoid mechanically translating 性能 into 'performances' or writing 'achieve better performances' without a metric.

**Patterns:**

- {method} improves performance on {benchmark}, as measured by {metric}.
- The methods exhibit different performance profiles across {task groups}.

### respectively requires an unambiguous one-to-one ordering

`general.usage-note.respectively.001` · usage_note · general · method, experiments, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Respectively maps two or more ordered lists element by element and should be used only when both lists have matching cardinality and a clear order.

**Use:** Place 'respectively' close to the second list. If the mapping could be misread, split the sentence or state each pairing explicitly.

**Avoid:** Avoid using 'respectively' when one item maps to several values or when the antecedent order is unclear.

**Patterns:**

- The {first method} and {second method} obtain {first value} and {second value}, respectively.
- We use {value one} for {setting one} and {value two} for {setting two}.

### absent from the manuscript versus contradicted by the manuscript versus unverifiable from the manuscript

`general.usage-note.review-evidence-scope.001` · usage_note · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reviewer statements about a submission carry three distinct evidential statuses: the manuscript omits something, the manuscript contradicts something, or the review packet cannot establish something either way.

**Use:** Choose the status explicitly before writing the criticism: request what is absent, correct what is contradicted, and mark what is unverifiable as outside the review's evidence rather than asserting it.

**Avoid:** Do not convert an omission into an accusation, and do not state unverifiable properties, such as reproducibility or hidden failures, as established facts.

**Patterns:**

- No episode counts are reported (absent), so we request them; we cannot judge reproducibility from the packet (unverifiable), so we do not assert it.
- The abstract claims real-world generalization while all experiments are simulated (contradicted), which is a claim-evidence mismatch rather than misconduct.

### statistically significant versus substantial improvement

`general.usage-note.significant.001` · usage_note · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Statistical significance refers to an inferential test or interval criterion, whereas substantial, marked, or large describes effect magnitude and requires a stated scale.

**Use:** Translate 显著 according to evidence: use 'statistically significant' only when a specified statistical analysis supports it; otherwise report the effect size or use a magnitude term justified by context.

**Avoid:** Do not infer statistical significance from a visibly larger mean, non-overlapping point estimates, or the Chinese adjective 显著 alone.

**Patterns:**

- {method} yields a {value}-point improvement, but the difference is not statistically significant under {test}.
- The improvement is substantial relative to {reference scale}, with an effect size of {value}.

### state-of-the-art performance on {benchmark} under {protocol}

`general.usage-note.state-of-the-art.001` · usage_note · general · abstract, introduction, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

A scoped claim that a verified result is best within a defined comparison set.

**Use:** Use only after checking the benchmark, metric, split, protocol, contemporaneous comparison set, and direction of improvement. Prefer the exact result when the scope is narrow.

**Avoid:** Never use 'state-of-the-art' as a general adjective for the method or as a synonym for strong.

**Patterns:**

- Under the {protocol} protocol, {method} achieves the best reported {metric} among {comparison set}.
