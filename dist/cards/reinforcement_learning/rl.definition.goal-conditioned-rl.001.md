# Super Library card: rl.definition.goal-conditioned-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### goal-conditioned reinforcement learning

`rl.definition.goal-conditioned-rl.001` · definition · reinforcement_learning · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A reinforcement-learning formulation in which the policy or value function is conditioned on a goal representation and optimized to reach or satisfy that goal.

**Use:** Specify the goal space, reward or success definition, goal-sampling distribution, horizon, and generalization split.

**Avoid:** Do not conflate goal conditioning with language conditioning unless language is the defined goal representation.

**Patterns:**

- The policy conditions on goal {g} and maximizes {objective} under goals sampled from {distribution}.

**Verify in primary sources:**

- `cho2023-outcome-directed-reinforcement-learning` — [Outcome-directed Reinforcement Learning by Uncertainty \& Temporal Distance-Aware Curriculum Goal Generation](https://iclr.cc/virtual/2023/poster/11888) (ICLR 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/exploration_skills_goals.md)
