# Super Library card: rl.definition.reset-free-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### reset-free (autonomous) reinforcement learning

`rl.definition.reset-free-rl.001` · definition · reinforcement_learning, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Learning in a continual, non-episodic interaction stream in which the environment is not reset between trials, so the agent must recover from failures, return to useful states, and manage its own data collection as part of learning.

**Use:** State how the agent retries without external resets (learned reset or recovery policies, backward controllers, or curricula), how evaluation is separated from the nonepisodic training stream, and how many human interventions occurred.

**Avoid:** Do not present episodic benchmark results as autonomous learning, and do not omit manual resets or interventions when claiming reset-free operation.

**Patterns:**

- After {failure mode}, {recovery mechanism} returns the agent to {useful state distribution} without an external reset.
- We report {intervention count} human interventions over {training duration}.

**Verify in primary sources:**

- `sharma2022-autonomous-reinforcement-learning-formalism` — [Autonomous Reinforcement Learning: Formalism and Benchmarking](https://iclr.cc/virtual/2022/poster/7153) (ICLR 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: sim_to_real_robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/sim_to_real_robot_learning.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
