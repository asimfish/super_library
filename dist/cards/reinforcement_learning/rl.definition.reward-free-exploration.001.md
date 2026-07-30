# Super Library card: rl.definition.reward-free-exploration.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### reward-free exploration

`rl.definition.reward-free-exploration.001` · definition · reinforcement_learning · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An exploration setting in which an agent collects information without knowing the downstream reward and later uses the collected data to solve one or more reward-specified tasks.

**Use:** State whether rewards are entirely absent during exploration, which task class is considered, and how planning or learning proceeds after reward revelation.

**Avoid:** Do not use reward-free as a synonym for intrinsic-reward exploration when a designed exploration reward drives data collection.

**Patterns:**

- During reward-free exploration, the agent collects {data}; after receiving {reward specification}, it computes {policy or value function} without further interaction.

**Verify in primary sources:**

- `cheng2023-improved-sample-complexity-reward` — [Improved Sample Complexity for Reward-free Reinforcement Learning under Low-rank MDPs](https://iclr.cc/virtual/2023/poster/11380) (ICLR 2023)
- `qiao2023-near-optimal-deployment-efficiency` — [Near-Optimal Deployment Efficiency in Reward-Free Reinforcement Learning with Linear Function Approximation](https://iclr.cc/virtual/2023/poster/11300) (ICLR 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/exploration_skills_goals.md)
