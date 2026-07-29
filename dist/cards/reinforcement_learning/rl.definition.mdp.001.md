# Super Library card: rl.definition.mdp.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Markov decision process (MDP)

`rl.definition.mdp.001` · definition · reinforcement_learning · method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A formal sequential decision process defined by states, actions, transition dynamics, and rewards, together with a discount factor or finite horizon when required by the formulation; the next-state distribution depends on the current state and action.

**Use:** List the tuple used in the paper and define any departure, such as partial observability, finite horizon, goal conditioning, or multiple agents.

**Avoid:** Do not assert the Markov property for raw observations when the agent only has partial information.

**Patterns:**

- We model the task as an MDP {tuple}, where {symbol definitions}.
- Because observations are partial, the policy conditions on {history or belief representation}.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
