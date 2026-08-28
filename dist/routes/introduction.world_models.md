# Super Library one-file route: World-model limitation-to-design introduction

`introduction.world_models` · domain `world_models` · section `introduction` · intent `motivate`

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

##### 6. Close with scope (conditional)

- State assumptions or non-goals that prevent an overbroad reading.
- Keep the boundary consistent with the Limitations and Experiments sections.

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

#### Retrieve related sentence cards only as needed

- [A central challenge is to {objective} while {constraint}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.motivate.001.md) — `general.sentence-pattern.motivate.001`
- [Despite progress in {area}, existing methods remain limited by {specific limitation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.gap.001.md) — `general.sentence-pattern.gap.001`
- [Our main contribution is {artifact or insight} that {verified capability}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.contribution.001.md) — `general.sentence-pattern.contribution.001`
- [Under {evaluated setting}, {method} consistently {measured outcome}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.scope.001.md) — `general.sentence-pattern.scope.001`
- [A complementary line of work studies {adjacent problem}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-family.001.md) — `general.sentence-pattern.related-family.001`
- [These approaches share {common objective}, but differ in {technical axes}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-synthesis.001.md) — `general.sentence-pattern.related-synthesis.001`

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

### world model

`wm.definition.world-model.001` · definition · world_models, reinforcement_learning · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learned predictive model of how an environment evolves, typically conditioned on the agent's actions and used to support prediction, planning, or policy learning.

**Use:** State what variables the model predicts, whether prediction occurs in observation or latent space, and how the model is used downstream. Community usage is broad, so define the paper's operational scope.

**Avoid:** Do not treat every video generator or static scene representation as a world model without an action, temporal, or decision-making connection.

**Patterns:**

- We use a world model to predict {future latent states or observations} conditioned on {current state and action sequence}.
- Here, world model refers to {learned transition components} used for {planning or policy optimization}.

**Verify in primary sources:**

- `ha2018worldmodels` — [Recurrent World Models Facilitate Policy Evolution](https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html) (NeurIPS 2018)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)

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
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
