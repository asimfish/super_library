# Super Library card: rl.definition.parameter-sharing.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### parameter sharing (multi-agent RL)

`rl.definition.parameter-sharing.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training multiple agents' policies or critics with one shared set of network parameters, so experience aggregates across agents and the trainable-parameter count stays constant as the number of agents grows.

**Use:** State which components are shared, how agents are distinguished (identifiers, observations, or roles), and whether sharing is full, selective, or partitioned by ability and goal. Report effects on both training efficiency and converged returns, since indiscriminate sharing can hurt heterogeneous agents.

**Avoid:** Do not assume shared parameters imply identical behavior, and do not generalize sharing benefits across environments without checking agent heterogeneity.

**Patterns:**

- All {agent group} policies share parameters and condition on {distinguishing input}.
- We partition agents into {groups} by {criterion} and share parameters within each group.

**Verify in primary sources:**

- `christianos2021-scaling-multi-agent-reinforcement` — [Scaling Multi-Agent Reinforcement Learning with Selective Parameter Sharing](https://proceedings.mlr.press/v139/christianos21a.html) (ICML 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: multi_agent_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/multi_agent_rl.md)
