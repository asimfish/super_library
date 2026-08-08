# Super Library card: rl.definition.reinforcement-learning.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### reinforcement learning (RL)

`rl.definition.reinforcement-learning.001` · definition · reinforcement_learning · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A decision-making framework in which an agent interacts with an environment and learns behavior to maximize expected cumulative reward.

**Use:** Specify observation/state, action, reward, horizon or discount, and whether training is online or offline when these choices matter.

**Avoid:** Do not describe supervised imitation from a fixed dataset as reinforcement learning unless a reward-based objective or RL update is used.

**Patterns:**

- We formulate {task} as reinforcement learning, where the agent observes {observation}, selects {action}, and receives {reward}.
- The objective is to maximize the expected discounted return under {environment distribution}.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
