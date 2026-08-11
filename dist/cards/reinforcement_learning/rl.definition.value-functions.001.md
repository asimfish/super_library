# Super Library card: rl.definition.value-functions.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### state-value and action-value functions

`rl.definition.value-functions.001` · definition · reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A state-value function estimates expected future return from a state under a policy, whereas an action-value function additionally conditions on the current action.

**Use:** Define the policy and return convention under which the expectation is taken. Use Q-function as the standard short form for an action-value function.

**Avoid:** Do not describe Q(s,a) as immediate reward or as a transition probability.

**Patterns:**

- The critic estimates the action-value function {Q symbol} under the current policy.
- The state-value function provides {bootstrap or baseline role}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/value_learning.md)
