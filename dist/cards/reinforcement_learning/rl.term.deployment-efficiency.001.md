# Super Library card: rl.term.deployment-efficiency.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### deployment efficiency

`rl.term.deployment-efficiency.001` · term · reinforcement_learning · related_work, experiments, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The amount of distinct real-world or environment deployment rounds required to collect interaction data, separated from the total number of transitions.

**Use:** Define a deployment round, parallelism, batch size, adaptivity between rounds, and both round and sample complexity.

**Avoid:** Do not call a method deployment-efficient solely because it is sample-efficient.

**Patterns:**

- The algorithm uses {rounds} deployment rounds and {samples} transitions, with policy updates occurring {between or within rounds}.

**Verify in primary sources:**

- `qiao2023-near-optimal-deployment-efficiency` — [Near-Optimal Deployment Efficiency in Reward-Free Reinforcement Learning with Linear Function Approximation](https://iclr.cc/virtual/2023/poster/11300) (ICLR 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/exploration_skills_goals.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/rl_theory_evaluation.md)
