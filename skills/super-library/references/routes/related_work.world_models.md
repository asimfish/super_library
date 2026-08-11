# Super Library one-file route: World-model Related Work positioning

`related_work.world_models` · domain `world_models` · section `related_work` · intent `position`

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

### Super Library protocol: Related Work: evidence-verified synthesis and positioning

`related_work` · `section_protocol` · section `related_work` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Organize verified primary papers into problem-relevant families, compare them on explicit axes, and locate the present work without paper-by-paper narration or unsupported priority claims.

**Use when:** Planning, drafting, or revising an AI-paper Related Work section or a focused literature-positioning paragraph.

#### Required inputs

- The exact task, setting, and claim that the literature discussion must contextualize.
- Verified primary papers with bibliographic metadata and notes tied to specific passages.
- A small set of organizing families and explicit comparison axes such as objective, supervision, data regime, assumptions, compute, or deployment setting.
- The present paper's factual relationship to each relevant family, including shared assumptions and material differences.

#### Functional protocol

##### 1. Verify the literature evidence (required)

- Open every primary paper used for a definition, historical claim, method characterization, or comparison.
- Record what the cited passage supports and do not infer absent limitations from silence.
- Use the library's source IDs only as navigation; never treat a corpus summary as the citation evidence.

##### 2. Build a task-relevant taxonomy (required)

- Group papers by the technical choice that matters to this paper rather than by arbitrary chronology.
- State the comparison axis before naming examples from a family.
- Separate families that solve different problem settings instead of ranking them together.

##### 3. Synthesize similarities and differences (required)

- Describe a recurring approach, then identify a verified assumption, mechanism, or scope difference.
- Make the subject of every evaluative statement explicit: method, dataset, protocol, or result.
- Distinguish reported evidence from the authors' interpretation and from this paper's synthesis.

##### 4. Position the present work precisely (required)

- State what is shared with prior work before the differentiating axis.
- Name the changed assumption, supervision, data, mechanism, evaluation, or deployment constraint.
- Do not imply superiority unless a verified comparable experiment supports it.

#### Choose one internal template

##### Taxonomy-first synthesis

Use when: Several approach families address a common task under different assumptions.

1. Define the shared task and organizing axis.
2. Describe the first family and its operative assumption.
3. Contrast the next family on the same axis.
4. Synthesize the unresolved boundary across families.
5. Position the present work on that boundary.

##### Concept evolution

Use when: Chronology is scientifically meaningful because later work changes a specific assumption or capability.

1. State the original formulation or capability with a primary source.
2. Describe the verified change introduced by subsequent work.
3. Compare the resulting families on a stable axis rather than merely listing years.
4. Identify the remaining problem addressed here.

#### Verification

- Every citation exists, has been opened, and supports the adjacent proposition at the stated scope.
- Every comparison names a common axis and avoids ranking incompatible protocols.
- Definitions are paraphrases unless a short quotation is explicitly marked and permitted.
- The section represents close alternatives fairly, including assumptions that favor the present method.
- No claim uses latest, first, only, most, or state-of-the-art without a separately verified comparison set.

#### Avoid

- One sentence per paper with no cross-paper synthesis.
- Citation clusters whose individual sources do not support the whole sentence.
- Describing prior work only through limitations while omitting its intended setting or strength.
- Using temporal recency as a proxy for relevance, quality, or novelty.

#### Retrieve related sentence cards only as needed

- [A complementary line of work studies {adjacent problem}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-family.001.md) — `general.sentence-pattern.related-family.001`
- [These approaches share {common objective}, but differ in {technical axes}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.related-synthesis.001.md) — `general.sentence-pattern.related-synthesis.001`
- [Prior approaches differ primarily in {axis one} and {axis two}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.position.001.md) — `general.sentence-pattern.position.001`
- [Unlike {comparison class}, which {defining behavior}, our approach {distinct behavior}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.contrast.001.md) — `general.sentence-pattern.contrast.001`
- [Distinguish possibility, interpretation, empirical evidence, and formal proof.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.modality.001.md) — `general.usage-note.modality.001`
- [state-of-the-art performance on {benchmark} under {protocol}](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.state-of-the-art.001.md) — `general.usage-note.state-of-the-art.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.

## Selected language records

### Prior approaches differ primarily in {axis one} and {axis two}.

`general.sentence-pattern.position.001` · sentence_pattern · general · related_work

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Organizes related work by technical comparison axes instead of paper-by-paper chronology.

**Use:** Choose axes that expose meaningful assumptions or design choices, then place representative methods along them with citations.

**Avoid:** Do not invent a taxonomy whose categories overlap without explanation.

**Patterns:**

- Prior approaches differ primarily in how they {technical axis one} and whether they {technical axis two}.

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

### model-based reinforcement learning

`wm.definition.model-based-rl.001` · definition · world_models, reinforcement_learning · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Reinforcement learning that uses a model of environment dynamics, learned or known, to improve decision making through planning, synthetic experience, value estimation, or policy optimization.

**Use:** Explain the role of the model rather than applying the label solely because the architecture contains a predictor.

**Avoid:** Do not conflate model-based RL with supervised next-step prediction that never affects decisions.

**Patterns:**

- The method is model-based because the learned dynamics model is used to {plan actions or optimize the policy}.
- Model-based reinforcement learning can use predicted transitions for {downstream decision process}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

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
