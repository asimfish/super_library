# Super Library one-file route: Vision-language-action Related Work positioning

`related_work.vision_language_action` · domain `vision_language_action` · section `related_work` · intent `position`

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
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

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

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
