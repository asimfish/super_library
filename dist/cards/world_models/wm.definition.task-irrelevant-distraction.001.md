# Super Library card: wm.definition.task-irrelevant-distraction.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### task-irrelevant distractors

`wm.definition.task-irrelevant-distraction.001` · definition · world_models, reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Observation content that is predictable or salient but has no bearing on reward or action selection, so models or encoders that spend capacity on it degrade downstream control even when prediction metrics look good.

**Use:** Name the distractor source (backgrounds, textures, or dynamics), state whether the training objective is reconstruction-based, and report control performance alongside prediction quality under distraction. Say how capacity is steered toward task-relevant content, for example task-aware losses, prototypes, or reconstruction-free objectives.

**Avoid:** Do not equate low reconstruction error with a useful world model under distraction, and do not call every hard visual scene a distractor setting without separating task-relevant from irrelevant content.

**Patterns:**

- In {environment}, {distractor content} is predictable but irrelevant to {task}, degrading {reconstruction-based method}.
- We steer model capacity toward task-relevant dynamics with {mechanism}, improving {control metric} under distraction.

**Verify in primary sources:**

- `hutson2024-policy-shaped-prediction-avoiding` — [Policy-shaped prediction: avoiding distractions in model-based reinforcement learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/17af43527227c5c96db0f8d4c6aadc4e-Abstract-Conference.html) (NeurIPS 2024)
- `deng2022-dreamerpro-reconstruction-free-model` — [DreamerPro: Reconstruction-Free Model-Based Reinforcement Learning with Prototypical Representations](https://proceedings.mlr.press/v162/deng22a.html) (ICML 2022)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: model_based_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/model_based_rl.md)
