# Super Library card: rl.term.policy.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### policy

`rl.term.policy.001` · term · reinforcement_learning, robot_learning · method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A rule or conditional distribution that maps an agent's information state, such as an observation or history, to actions.

**Use:** Use π(a|s) for a stochastic policy and state whether conditioning is on state, observation, goal, language, or history.

**Avoid:** Do not call a value function or open-loop action sequence a policy.

**Patterns:**

- The stochastic policy {symbol} maps {observation or state} to a distribution over {actions}.
- We condition the policy on {goal specification} in addition to {observation}.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `brohan2023rt1` — [RT-1: Robotics Transformer for Real-World Control at Scale](https://roboticsproceedings.org/rss19/p025.html) (RSS 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
