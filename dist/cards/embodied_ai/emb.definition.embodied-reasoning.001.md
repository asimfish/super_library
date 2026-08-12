# Super Library card: emb.definition.embodied-reasoning.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### embodied reasoning

`emb.definition.embodied-reasoning.001` · definition · embodied_ai, vision_language_action · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Intermediate inference grounded in an agent's observations and task, such as spatial relations, action consequences, or subgoal structure, produced between perception and control so that decisions follow from stated premises rather than direct pattern matching.

**Use:** State the reasoning format (language, keypoints, or plans), what grounds it (images, scene metadata, demonstrations), and how it is supervised or rewarded. Evaluate reasoning quality separately from downstream control success when the benchmark allows it.

**Avoid:** Do not call generic chain-of-thought embodied reasoning when it never conditions on the agent's observations or task state, and do not report reasoning-benchmark gains as control gains without a control evaluation.

**Patterns:**

- The model produces {reasoning form} conditioned on {observation and task context} before predicting {action or keypoint}.
- We evaluate embodied reasoning on {reasoning benchmark} and report control success separately on {control tasks}.

**Verify in primary sources:**

- `kim2025-robot-r1-reinforcement-learning` — [Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics](https://proceedings.neurips.cc/paper_files/paper/2025/hash/ec46d737282bb408e642ed883a145c40-Abstract-Conference.html) (NeurIPS 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_reasoning_agents.md)
