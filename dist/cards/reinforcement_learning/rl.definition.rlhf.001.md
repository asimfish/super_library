# Super Library card: rl.definition.rlhf.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### reinforcement learning from human feedback (RLHF)

`rl.definition.rlhf.001` · definition · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training pipeline that learns a reward model from human judgments, typically preference comparisons between candidate outputs or behaviors, and then optimizes a policy against that learned reward when a programmatic reward is unavailable.

**Use:** State how human judgments are collected and aggregated, the reward-model class, the policy-optimization stage, and known failure modes such as reward hacking, reward-model misgeneralization, and evaluator disagreement. Keep RLHF distinct from AI feedback (model-generated judgments) and from human-in-the-loop intervention during training.

**Avoid:** Do not present RLHF as a guarantee of goal alignment, and do not use RLHF to describe direct human reward shaping without a learned reward model.

**Patterns:**

- We collect {judgment type} from {annotator pool}, fit {reward model}, and optimize the policy with {algorithm} against it.
- We audit the learned reward for {failure mode} before deploying the policy on {task}.

**Verify in primary sources:**

- `rando2025-open-problems-fundamental-limitations` — [Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback](https://iclr.cc/virtual/2025/poster/31506) (ICLR 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
- [topic: safe_robust_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/safe_robust_rl.md)
