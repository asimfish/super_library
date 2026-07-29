# Super Library card: rl.definition.actor-critic.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### actor–critic method

`rl.definition.actor-critic.001` · definition · reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A reinforcement-learning method with an actor that represents or updates the policy and a critic that estimates a value-related signal used to guide the actor.

**Use:** State which value quantity the critic estimates, how the actor uses it, and whether updates are on-policy, off-policy, stochastic, or deterministic.

**Avoid:** Do not call every two-network method actor–critic; the functional roles matter.

**Patterns:**

- The actor parameterizes {policy}, while the critic estimates {value quantity} for policy improvement.
- We train the actor and critic from {real or imagined transitions}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
