# Super Library card: rl.definition.meta-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### meta-reinforcement learning

`rl.definition.meta-rl.001` · definition · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training on a distribution of related tasks so an agent adapts rapidly to a new task from limited experience, typically by inferring a task representation or belief from recent interaction, or by optimizing explicitly for post-adaptation performance.

**Use:** Specify the task distribution and what varies across tasks, the adaptation mechanism (context inference, belief states, or gradient adaptation) and its interaction budget, and report post-adaptation performance on held-out tasks rather than training-task returns.

**Avoid:** Do not conflate meta-RL with multi-task RL that optimizes fixed training tasks without an adaptation phase, and do not report adaptation speed without stating the interaction budget it consumed.

**Patterns:**

- The agent meta-trains on {task distribution} and adapts to held-out tasks within {budget} using {adaptation mechanism}.
- We report post-adaptation {metric} on {held-out tasks}, separated from training-task performance.

**Verify in primary sources:**

- `zhang2025-learning-task-belief-similarity` — [Learning Task Belief Similarity with Latent Dynamics for Meta-Reinforcement Learning](https://iclr.cc/virtual/2025/poster/30938) (ICLR 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/exploration_skills_goals.md)
