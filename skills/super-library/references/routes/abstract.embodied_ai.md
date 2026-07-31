# Super Library one-file route: Embodied-AI empirical abstract

`abstract.embodied_ai` · domain `embodied_ai` · section `abstract` · intent `evidence`

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

### Super Library protocol: Abstract: claim-aligned empirical summary

`abstract` · `section_protocol` · section `abstract` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Produce a compact summary whose problem, contribution, evidence, and scope exactly match the completed paper.

**Use when:** Drafting or revising an AI-paper abstract after the methods and principal results are known.

#### Required inputs

- One-sentence problem and evaluated scope.
- The specific unresolved limitation or challenge addressed by this paper.
- The paper's core insight and the mechanism that realizes it.
- Verified principal evidence, including benchmark, metric, comparison, statistic, and uncertainty when available.
- Assumptions, deployment boundary, or evaluated generalization axis that materially limits the claim.

#### Functional protocol

##### 1. Build an abstract claim ledger (required)

- Map every proposed abstract claim to a section, theorem, table, or figure in the paper.
- Remove a claim if the mapped evidence does not support its comparison set or generalization scope.
- Keep aspirational motivation grammatically distinct from achieved results.

##### 2. State the problem and precise gap (required)

- Name the task or setting before the broad application motivation.
- Describe a concrete assumption, failure mode, resource bottleneck, or missing capability rather than calling prior work insufficient.
- Do not claim priority or novelty unless independently verified.

##### 3. Connect insight to mechanism (required)

- State what makes the approach work conceptually, then name the mechanism.
- Do not enumerate low-level modules that do not affect the paper-level contribution.

##### 4. Report evidence with scope (required)

- Prefer one decision-relevant verified result over 'extensive experiments demonstrate'.
- Distinguish absolute change from relative change and percentage points.
- End with the supported implication or boundary, not a universal superiority claim.

#### Choose one internal template

##### Empirical method paper

Use when: The main contribution is a method evaluated on benchmarks, simulation, or real systems.

1. Task and operational context.
2. Specific limitation under a named setting or assumption.
3. Core insight.
4. Method and mechanism.
5. Verified principal comparison with evaluation scope.
6. Supported implication or explicit boundary.

##### Resource or benchmark paper

Use when: The main contribution is a dataset, environment, benchmark, or evaluation protocol.

1. Capability that cannot currently be measured well.
2. Coverage or validity gap in existing resources.
3. What the new resource contains and how it is constructed.
4. What diagnostic dimensions or tasks it enables.
5. Verified baseline findings and what they reveal.
6. Access, scope, or limitation statement.

##### Theory-led paper

Use when: The main contribution is a theorem, guarantee, bound, or analysis.

1. Problem and formal setting.
2. Limitation of existing guarantees.
3. Main result with its assumptions.
4. Key proof or algorithmic idea at a high level.
5. Implication relative to the prior bound or setting.
6. Empirical evidence only if it is actually part of the contribution.

#### Verification

- The abstract uses the same task, method name, metric names, and comparison direction as the body.
- Every number matches the final table or theorem, including units, denominator, and aggregation.
- No conclusion extends beyond the evaluated datasets, tasks, embodiments, shifts, or assumptions.
- The target venue's current length, paragraph, citation, and formatting rules were checked separately.

#### Avoid

- Opening with an unverifiable claim that the broad field is fundamentally important.
- Using 'novel', 'effective', 'superior', or 'state-of-the-art' as substitutes for a technical contribution and verified result.
- Listing modules without explaining the insight that connects them.
- Adding citations, results, or deployment claims not present in the completed paper.

#### Retrieve related sentence cards only as needed

- [A central challenge is to {objective} while {constraint}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.motivate.001.md) — `general.sentence-pattern.motivate.001`
- [Despite progress in {area}, existing methods remain limited by {specific limitation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.gap.001.md) — `general.sentence-pattern.gap.001`
- [Our main contribution is {artifact or insight} that {verified capability}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.contribution.001.md) — `general.sentence-pattern.contribution.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [state-of-the-art performance on {benchmark} under {protocol}](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.usage-note.state-of-the-art.001.md) — `general.usage-note.state-of-the-art.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.

## Selected language records

### For {task}, existing methods remain limited by {specific constraint}.

`general.sentence-pattern.abstract-gap.001` · sentence_pattern · general · abstract, introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces a concrete research gap tied to a task and a named constraint.

**Use:** Use only after verifying that the closest relevant methods share the stated constraint. Name the setting in which it matters.

**Avoid:** Avoid replacing the constraint with 'limited performance' or implying that every prior method has the same weakness.

**Patterns:**

- For {task}, existing methods remain limited by {assumption} when {condition}.
- In {setting}, current approaches require {resource or supervision}, which restricts {capability}.

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

### embodied AI

`emb.definition.embodied-ai.001` · definition · embodied_ai, robot_learning · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The study of agents that perceive and act within an environment, where their observations, actions, and learning are shaped by embodiment and closed-loop interaction.

**Use:** Specify the body, sensors, action space, environment, and task. For simulated agents, state which physical or interaction constraints are modeled.

**Avoid:** Do not use 'embodied' for a passive model that only processes a fixed image or text dataset without an interaction formulation.

**Patterns:**

- We study embodied AI agents that perceive {sensory inputs} and act through {action space} in {environment}.
- The agent's observations depend on its previous actions, creating a closed perception–action loop.

**Verify in primary sources:**

- `xia2018gibson` — [Gibson Env: Real-World Perception for Embodied Agents](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) (CVPR 2018)
- `savva2019habitat` — [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) (ICCV 2019)

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
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/routes/index.md) only for a different task.
