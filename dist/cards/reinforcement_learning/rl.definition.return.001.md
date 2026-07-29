# Super Library card: rl.definition.return.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### discounted return

`rl.definition.return.001` · definition · reinforcement_learning · method, experiments, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The cumulative sum of future rewards, commonly weighting a reward received k steps later by a discount factor raised to k.

**Use:** Define horizon, discount convention, termination handling, and whether reported return is undiscounted even if training uses discounting.

**Avoid:** Do not use reward and return interchangeably: reward is typically per transition, whereas return aggregates rewards over time.

**Patterns:**

- The objective maximizes the expected discounted return {equation}.
- We report undiscounted episode return while using {discount} for training.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
