# Super Library one-file route: Embodied-AI Related Work positioning

`related_work.embodied_ai` · domain `embodied_ai` · section `related_work` · intent `position`

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
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/routes/index.md) only for a different task.
