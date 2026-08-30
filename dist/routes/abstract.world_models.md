# Super Library one-file route: World-model empirical abstract

`abstract.world_models` · domain `world_models` · section `abstract` · intent `evidence`

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

`abstract` · `section_protocol` · section `abstract` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

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

##### 5. Anti-defensive final pass (required)

- Polish tone only, never content: every task, setting, protocol, mechanism, and comparison named in the final pass must already appear in the supplied material in those terms; if a claim-forward rewrite would add, upgrade, or rename one, keep the original wording instead.
- Open with the contribution the supplied results support, never with a disclaimer, apology, or list of things the work does not do.
- State scope positively: name what the work covers, keep at most the exclusions a reader needs, and fold stacked 'we do not claim' disclaimers into one boundary sentence.
- Use plain declaratives for measured results and reserve 'may', 'might', or 'potentially' for claims the material marks as untested; never remove a hedge if doing so widens a claim beyond the supplied evidence.
- Keep every evidential qualifier such as the sample size, split, or evaluated setting: those bind the claim to its evidence and are not defensive tone.

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
- Hedging a measured result with 'may', 'might', or 'potentially', or spending the opening on disclaimers instead of the supported contribution.

#### Retrieve related sentence cards only as needed

- [A central challenge is to {objective} while {constraint}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.motivate.001.md) — `general.sentence-pattern.motivate.001`
- [Despite progress in {area}, existing methods remain limited by {specific limitation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.gap.001.md) — `general.sentence-pattern.gap.001`
- [Our main contribution is {artifact or insight} that {verified capability}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.contribution.001.md) — `general.sentence-pattern.contribution.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [state-of-the-art performance on {benchmark} under {protocol}](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.state-of-the-art.001.md) — `general.usage-note.state-of-the-art.001`
- [We present {method}, which {capability the supplied results state} on {evaluated setting}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.claim-forward-opening.001.md) — `general.sentence-pattern.claim-forward-opening.001`
- [{Method} targets {setting the material states}; {one adjacent setting} is outside the scope of this work.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.positive-scope.001.md) — `general.sentence-pattern.positive-scope.001`
- [Across {units the material states}, {method} improves {metric} by {stated amount}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.calibrated-strength.001.md) — `general.sentence-pattern.calibrated-strength.001`
- [defensive hedging versus calibrated claiming](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.anti-defensive-tone.001.md) — `general.usage-note.anti-defensive-tone.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
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

### We present {method}, which {capability the supplied results state} on {evaluated setting}.

`general.sentence-pattern.claim-forward-opening.001` · sentence_pattern · general · abstract, introduction

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Opens with the contribution itself instead of a disclaimer about what the work does not do or does not claim.

**Use:** Open with the supported contribution stated in the material's own terms, then bound it. Reuse the material's nouns for tasks, settings, protocols, and mechanisms; never substitute a broader term for a narrower one the material uses. Strength comes from claiming exactly what the evidence supports, not from claiming more.

**Avoid:** Do not open with 'does not attempt', 'is not intended to', or an apology before the contribution is stated; never widen a claim beyond the supplied evidence, upgrade a scope term, or name a mechanism, protocol, or comparison the material does not state.

**Patterns:**

- We present {method}, which improves {metric} by {stated amount} across {evaluated benchmarks}.
- We show that {supported finding}, based on {evidence the material states}.

### Across {units the material states}, {method} improves {metric} by {stated amount}.

`general.sentence-pattern.calibrated-strength.001` · sentence_pattern · general · abstract, experiments, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Matches verb strength to evidential status: plain declaratives for measured results, hedges only for claims the material marks as unmeasured.

**Use:** When the material states a measured result, report it with a direct verb and its stated scope. Reserve 'may', 'might', and 'potentially' for statements the material itself marks as untested. Never delete a hedge if doing so widens the claim beyond the stated evidence.

**Avoid:** Do not write 'may potentially improve' for a gain the material measures, and do not promote an untested setting to a direct claim by dropping its hedge.

**Patterns:**

- Across {stated number} tasks, {method} improves {metric} from {stated baseline value} to {stated value}.
- On the {stated split}, {method} reduces {failure mode} by {stated amount}; settings beyond this split were not evaluated.

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
