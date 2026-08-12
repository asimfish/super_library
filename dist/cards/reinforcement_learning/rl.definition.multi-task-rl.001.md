# Super Library card: rl.definition.multi-task-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### multi-task reinforcement learning (MTRL)

`rl.definition.multi-task-rl.001` · definition · reinforcement_learning, robot_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training one agent or shared components on a set of reinforcement-learning tasks so that experience, representations, or parameters transfer across tasks, instead of optimizing each task independently.

**Use:** State what is shared (policy, representation, or experts), how tasks are identified or weighted, the training order or curriculum when asymmetric, and how negative transfer between dissimilar tasks is detected or mitigated. Report per-task and aggregate returns, not aggregates alone.

**Avoid:** Do not equate multi-task RL with goal-conditioned RL over goals of one task family, and do not claim positive transfer from aggregate results while individual tasks regress.

**Patterns:**

- The agent shares {component} across {task set} and mitigates negative transfer with {mechanism}.
- We report per-task returns alongside the aggregate to expose transfer asymmetry across {benchmarks}.

**Verify in primary sources:**

- `huang2023-curriculum-based-asymmetric-multi` — [Curriculum-Based Asymmetric Multi-Task Reinforcement Learning](https://doi.org/10.1109/tpami.2022.3223872) (TPAMI 2023)
- `kong2025-mastering-massive-multi-task` — [Mastering Massive Multi-Task Reinforcement Learning via Mixture-of-Expert Decision Transformer](https://proceedings.mlr.press/v267/kong25a.html) (ICML 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
