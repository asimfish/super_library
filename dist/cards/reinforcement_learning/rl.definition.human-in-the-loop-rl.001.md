# Super Library card: rl.definition.human-in-the-loop-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### human-in-the-loop reinforcement learning

`rl.definition.human-in-the-loop-rl.001` · definition · reinforcement_learning, embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training regime in which humans participate during learning, for example by intervening in control, providing demonstrations on demand, or shaping rewards, so the policy is optimized from both autonomous interaction and human guidance.

**Use:** Specify when and how humans intervene, how their input enters the objective (auxiliary loss, replay prioritization, or reward shaping), the amount of human effort required, and how performance behaves once guidance is withdrawn.

**Avoid:** Do not conflate human-in-the-loop training with offline imitation from fixed demonstrations or with preference-based reward learning from post-hoc comparisons; state the interaction protocol explicitly.

**Patterns:**

- A human supervisor intervenes when {trigger condition}, and the intervention is incorporated through {mechanism}.
- We report performance as a function of {human effort measure} to quantify the cost of guidance.

**Verify in primary sources:**

- `wu2023-human-guided-reinforcement-learning` — [Human-Guided Reinforcement Learning With Sim-to-Real Transfer for Autonomous Navigation](https://doi.org/10.1109/tpami.2023.3314762) (TPAMI 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: safe_robust_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/safe_robust_rl.md)
