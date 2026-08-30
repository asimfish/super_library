# Super Library one-file route: Vision-language-action limitation-to-design introduction

`introduction.vision_language_action` · domain `vision_language_action` · section `introduction` · intent `motivate`

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

### Super Library protocol: Introduction: limitation–insight–evidence alignment

`introduction` · `section_protocol` · section `introduction` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Build an argument that moves from a scoped problem to a verified gap, design insight, contribution, and evidence without relying on a fixed paragraph count.

**Use when:** Planning, drafting, or restructuring an AI-paper Introduction.

#### Required inputs

- Paper type: method, new problem or setting, resource, empirical study, or theory.
- Task definition, relevant application stakes, and intended reader prerequisites.
- Closest approach families and the verified axes on which they differ.
- The exact limitation addressed, including its assumptions and practical consequence.
- Core insight, design elements, contribution claims, and the experiment or theorem supporting each claim.

#### Functional protocol

##### 1. Establish scope and problem (required)

- Define the operational task before expanding to broader motivation.
- Use a concrete running scenario only when it is real and technically representative.
- Avoid claiming that all prior work shares one weakness.

##### 2. Map closest approaches (required)

- Group work by representation, supervision, data, decision mechanism, interaction regime, or deployment assumption.
- Use only verified literature relationships and reserve detailed chronology for Related Work.
- Make the comparison axis explicit before stating the limitation.

##### 3. State gap and consequence (required)

- Name the condition under which the limitation matters.
- Separate lack of evaluation from evidence of failure.
- Do not turn a design difference into a defect without evidence.

##### 4. Bridge insight to design (required)

- State the key insight before the component list.
- Map each emphasized challenge to a design choice.
- Explain the causal claim only as strongly as the design and analysis allow.

##### 5. Pair contributions with evidence (required)

- Write parallel contributions at the same abstraction level.
- Pair each empirical contribution with a named evaluation question or display.
- Replace 'extensive experiments' with the evaluated axes and principal finding.
- Preview only outcomes the supplied results state: never add a comparison, superiority claim, or guarantee word such as 'consistently' or 'ensures' that the material does not contain.

##### 6. Close with scope (conditional)

- State assumptions or non-goals that prevent an overbroad reading.
- Keep the boundary consistent with the Limitations and Experiments sections.

##### 7. Anti-defensive final pass (required)

- Polish tone only, never content: every task, setting, protocol, mechanism, and comparison named in the final pass must already appear in the supplied material in those terms; if a claim-forward rewrite would add, upgrade, or rename one, keep the original wording instead.
- Open with the contribution the supplied results support, never with a disclaimer, apology, or list of things the work does not do.
- State scope positively: name what the work covers, keep at most the exclusions a reader needs, and fold stacked 'we do not claim' disclaimers into one boundary sentence.
- Use plain declaratives for measured results and reserve 'may', 'might', or 'potentially' for claims the material marks as untested; never remove a hedge if doing so widens a claim beyond the supplied evidence.
- Keep every evidential qualifier such as the sample size, split, or evaluated setting: those bind the claim to its evidence and are not defensive tone.

#### Choose one internal template

##### Technique paper

Use when: A new method addresses a known task.

1. Operational task and stakes.
2. Closest method families and relevant comparison axes.
3. Limitation under a named condition.
4. Key insight and method overview.
5. Contribution–evidence pairs.
6. Supported scope or non-goal.

##### New setting or resource

Use when: The paper primarily introduces a task, dataset, benchmark, or problem formulation.

1. Missing capability or evaluation need.
2. Why existing settings fail to measure it.
3. Definition and design principles of the new setting.
4. Coverage, validity, and diagnostic axes.
5. Baseline findings and remaining gap.
6. Availability and boundary.

##### Theory or analysis paper

Use when: The main contribution is explanatory or formal rather than architectural.

1. Formal problem and why it matters.
2. Known results and the unresolved regime.
3. Main insight or analytical device.
4. Principal result and assumptions.
5. Consequences and evidence.
6. Limits of the analysis.

#### Verification

- Construct a matrix from limitation to challenge, design choice, contribution, and supporting experiment or theorem.
- Check every literature statement against primary papers rather than the library or another paper's Related Work.
- Ensure contribution wording matches the Abstract and does not exceed the evidence summarized later.
- Read the Introduction once without citations: the logical bridge should remain clear.

#### Avoid

- A universal six-paragraph requirement; use functional moves and merge them when the argument benefits.
- A straw-man progression from a deliberately weak 'naive' solution to the proposed method.
- Chronological paper listing, unverified 'first' claims, and generic importance claims.
- Contribution bullets that mix a task definition, one module, and a result at incompatible levels.
- Hedging a measured result with 'may', 'might', or 'potentially', or spending the opening on disclaimers instead of the supported contribution.

#### Retrieve related sentence cards only as needed

- [A central challenge is to {objective} while {constraint}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.motivate.001.md) — `general.sentence-pattern.motivate.001`
- [Despite progress in {area}, existing methods remain limited by {specific limitation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.gap.001.md) — `general.sentence-pattern.gap.001`
- [Our main contribution is {artifact or insight} that {verified capability}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.contribution.001.md) — `general.sentence-pattern.contribution.001`
- [Under {evaluated setting}, {method} consistently {measured outcome}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.scope.001.md) — `general.sentence-pattern.scope.001`
- [A complementary line of work studies {adjacent problem}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-family.001.md) — `general.sentence-pattern.related-family.001`
- [These approaches share {common objective}, but differ in {technical axes}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-synthesis.001.md) — `general.sentence-pattern.related-synthesis.001`
- [We present {method}, which {capability the supplied results state} on {evaluated setting}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.claim-forward-opening.001.md) — `general.sentence-pattern.claim-forward-opening.001`
- [{Method} targets {setting the material states}; {one adjacent setting} is outside the scope of this work.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.positive-scope.001.md) — `general.sentence-pattern.positive-scope.001`
- [Across {units the material states}, {method} improves {metric} by {stated amount}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.calibrated-strength.001.md) — `general.sentence-pattern.calibrated-strength.001`
- [defensive hedging versus calibrated claiming](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.anti-defensive-tone.001.md) — `general.usage-note.anti-defensive-tone.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.

## Selected language records

### This assumption becomes restrictive when {condition}, because {consequence}.

`general.sentence-pattern.intro-restrictive-assumption.001` · sentence_pattern · general · introduction, related_work, limitations

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Connects a verified method assumption to the condition under which it limits the target capability.

**Use:** State the assumption, triggering condition, and consequence explicitly. Support literature and empirical claims with primary evidence.

**Avoid:** Do not describe a design difference as restrictive without showing why it matters for the task.

**Patterns:**

- This assumption becomes restrictive when {shift}, because {technical consequence}.
- The requirement for {resource} limits deployment in {setting}, where {constraint}.

### Motivated by this observation, we design {mechanism} to {goal}.

`general.sentence-pattern.intro-observation-design.001` · sentence_pattern · general · introduction, method

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Bridges a stated insight or empirical observation to the paper's design response.

**Use:** Ensure the antecedent observation directly motivates the mechanism. Name the technical goal rather than 'better performance.'

**Avoid:** Avoid using the transition when the design choice is unrelated to the preceding limitation.

**Patterns:**

- Motivated by this observation, we design {mechanism} to preserve {property}.
- This analysis motivates {design choice}, which targets {failure mode}.

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

### vision-language-action (VLA) model

`emb.definition.vla.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A model or policy that conditions on visual observations and language and produces robot actions or an action representation for embodied control.

**Use:** Specify all inputs, the action space, control frequency, training data, and whether actions are generated directly, discretized as tokens, or decoded by a separate head.

**Avoid:** Do not call a vision-language model a VLA merely because its textual output can be interpreted by an external planner.

**Patterns:**

- The VLA policy maps camera observations and a language instruction to a sequence of robot actions.
- We fine-tune the pretrained VLA on {number} demonstrations from {target embodiment}.

**Verify in primary sources:**

- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `zhen2024vla` — [3D-VLA: A 3D Vision-Language-Action Generative World Model](https://proceedings.mlr.press/v235/zhen24a.html) (ICML 2024)

### separate multimodal pretraining from robot-policy fine-tuning

`vla.usage-note.pretrain-finetune.001` · usage_note · vision_language_action, robot_learning · method, experiments, related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Multimodal representation learning and action-policy optimization use different data, objectives, and sometimes different parameter subsets.

**Use:** Report each stage's data sources, objective, trainable parameters, robot supervision, and evaluation role.

**Avoid:** Do not describe all prior training as robot pretraining when much of it contains no robot actions.

**Patterns:**

- We first pretrain {modules} on {data and objective}, then fine-tune {parameters} on {robot demonstrations} for action prediction.

**Verify in primary sources:**

- `li2024-mastering-robot-manipulation-multimodal` — [Mastering Robot Manipulation with Multimodal Prompts through Pretraining and Multi-task Fine-tuning](https://proceedings.mlr.press/v235/li24x.html) (ICML 2024)
- `li2025-llara-supercharging-robot-learning` — [LLaRA: Supercharging Robot Learning Data for Vision-Language Policy](https://iclr.cc/virtual/2025/poster/28695) (ICLR 2025)

### We present {method}, which {capability the supplied results state} on {evaluated setting}.

`general.sentence-pattern.claim-forward-opening.001` · sentence_pattern · general · abstract, introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Opens with the contribution itself instead of a disclaimer about what the work does not do or does not claim.

**Use:** Open with the supported contribution stated in the material's own terms, then bound it. Reuse the material's nouns for tasks, settings, protocols, and mechanisms; never substitute a broader term for a narrower one the material uses. Strength comes from claiming exactly what the evidence supports, not from claiming more.

**Avoid:** Do not open with 'does not attempt', 'is not intended to', or an apology before the contribution is stated; never widen a claim beyond the supplied evidence, upgrade a scope term, or name a mechanism, protocol, or comparison the material does not state.

**Patterns:**

- We present {method}, which improves {metric} by {stated amount} across {evaluated benchmarks}.
- We show that {supported finding}, based on {evidence the material states}.

### {Method} targets {setting the material states}; {one adjacent setting} is outside the scope of this work.

`general.sentence-pattern.positive-scope.001` · sentence_pattern · general · abstract, introduction, method, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States scope by what the work covers, with at most one deliberate exclusion, instead of a chain of defensive disclaimers.

**Use:** Name the covered scope positively from the supplied material. Keep only the exclusions a reader needs to avoid misusing the result; an exclusion is a boundary statement, not an apology.

**Avoid:** Do not stack multiple 'we do not claim' clauses when one positive scope sentence carries the same boundary; do not restate the covered scope as a list of things the work is not.

**Patterns:**

- {Method} addresses {stated problem class}; extending it to {adjacent class} is left to future work.
- Our evaluation covers {stated benchmarks and budget}; deployment-scale settings are outside the scope of this study.

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
