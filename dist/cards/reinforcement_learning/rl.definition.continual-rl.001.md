# Super Library card: rl.definition.continual-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### continual reinforcement learning

`rl.definition.continual-rl.001` · definition · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A setting in which an agent learns from a sequence of tasks or a nonstationary stream over its lifetime, aiming to retain previously acquired knowledge, avoid catastrophic forgetting, and transfer forward to new tasks under bounded capacity and compute.

**Use:** State the task sequence and what changes along it, the memory and compute constraints, and whether task boundaries and identities are observed. Report forgetting and forward transfer separately from single-task performance.

**Avoid:** Do not equate continual RL with multi-task RL trained jointly on a fixed task set, and do not report only final average performance, which hides forgetting.

**Patterns:**

- The agent learns {task sequence} under {capacity constraint}; we report forgetting and forward transfer on {benchmark}.
- Knowledge is retained through {mechanism} while {component} adapts to the current task.

**Verify in primary sources:**

- `mendez2022-modular-lifelong-reinforcement-learning` — [Modular Lifelong Reinforcement Learning via Neural Composition](https://iclr.cc/virtual/2022/poster/6937) (ICLR 2022)
- `fu2025-knowledge-retention-continual-model` — [Knowledge Retention in Continual Model-Based Reinforcement Learning](https://proceedings.mlr.press/v267/fu25f.html) (ICML 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
