# Super Library pack: general

Corpus `0.1.0` · snapshot `2026-07-29`.

These are paraphrases, canonical terms, and original sentence patterns.
Verify technical claims in the linked primary sources before citing them.
Read the [self-contained mini contract](https://raw.githubusercontent.com/asimfish/super_library/v0.1.0/dist/super-library-compact.md) before using this pack directly.

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

### Removing {component} reduces {metric}, indicating that {bounded interpretation}.

`general.sentence-pattern.ablation.001` · sentence_pattern · general · experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Connects an ablation result to a component-level interpretation.

**Use:** Report the size and uncertainty where possible. 'Indicating' should introduce a bounded interpretation rather than a causal universal.

**Avoid:** Do not conclude that a component is necessary in every setting from one ablation.

**Patterns:**

- Removing {component} reduces {metric} from {a} to {b}, indicating that it contributes to {capability} in {setting}.

### These results are consistent with the hypothesis that {mechanism}.

`general.sentence-pattern.causal-caution.001` · sentence_pattern · general · experiments, limitations, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Links observations to a mechanism without claiming that the experiment identifies causality.

**Use:** Use when evidence supports but does not isolate the proposed explanation. Follow with an ablation or limitation if available.

**Avoid:** Do not write 'the gains are due to' without an identifying intervention.

**Patterns:**

- These results are consistent with the hypothesis that {component or inductive bias} improves {measured behavior}.

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

### Our evaluation is limited to {scope}; performance under {unseen condition} remains to be established.

`general.sentence-pattern.limitation.001` · sentence_pattern · general · limitations, conclusion, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States an evaluation boundary and separates tested from untested conditions.

**Use:** Name the missing population, environment, scale, horizon, embodiment, or distribution. Do not bury a material limitation.

**Avoid:** Do not turn a limitation into an unsupported claim that future work will certainly solve it.

**Patterns:**

- Our evaluation is limited to {tasks or environments}; robustness to {shift} remains to be established.

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

### {method} improves {metric} by {value} relative to {baseline} under {protocol}.

`general.sentence-pattern.quantify.001` · sentence_pattern · general · abstract, experiments, rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reports a quantified comparison with its baseline and protocol.

**Use:** State whether the value is absolute or relative, and match the aggregation and uncertainty used in the table.

**Avoid:** Avoid 'significant' unless statistical significance was actually tested.

**Patterns:**

- {method} improves mean {metric} by {absolute or relative value} over {baseline} under the {protocol} protocol.

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

### The requested comparison is already included in {location}, where {verified result}.

`general.sentence-pattern.rebuttal-evidence.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Points a reviewer to existing evidence and summarizes only the relevant result.

**Use:** Give an exact manuscript location and reproduce numbers faithfully. If absent, use a revision or limitation frame instead.

**Avoid:** Do not invent a table location or imply that an indirect analysis answers the request.

**Patterns:**

- The requested comparison is already included in {Table or Appendix}, where {method} achieves {verified metric} under {protocol}.

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

### Distinguish possibility, interpretation, empirical evidence, and formal proof.

`general.usage-note.modality.001` · usage_note · general · abstract, introduction, related_work, experiments, limitations, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Modal verbs and evidential verbs serve different functions rather than forming one universal strength ordering.

**Use:** Use 'may/might' for possibility, 'suggests/supports' for a tentative interpretation or evidence relation, 'shows/demonstrates' for a result established within the study design, and 'proves' only for a formal proof under stated assumptions.

**Avoid:** Do not translate 可能 or 表明 into an unqualified 'proves', or assume that any two evidential verbs have a context-free ordering.

**Patterns:**

- The results suggest that {hypothesis}, but do not establish {stronger causal claim}.

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
