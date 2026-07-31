# Super Library card: rl.usage-note.marl-observability.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### separate centralized information during training from each agent's execution-time observations

`rl.usage-note.marl-observability.001` · usage_note · reinforcement_learning · related_work, method, experiments

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Multi-agent algorithms may use global state or joint information in training while each deployed agent acts from local observations and internal memory.

**Use:** Report information available to actor, critic, mixer, and replay data at both training and execution; state the partial-observability model.

**Avoid:** Do not call execution decentralized if an actor directly receives privileged global information.

**Patterns:**

- During training, {module} observes {centralized information}; at execution, agent {i} acts from {local history or observation}.

**Verify in primary sources:**

- `phan2023-attention-based-recurrence-multi` — [Attention-Based Recurrence for Multi-Agent Reinforcement Learning under Stochastic Partial Observability](https://proceedings.mlr.press/v202/phan23a.html) (ICML 2023)
- `kuba2022-trust-region-policy-optimisation` — [Trust Region Policy Optimisation in Multi-Agent Reinforcement Learning](https://iclr.cc/virtual/2022/poster/6244) (ICLR 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [topic: multi_agent_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/multi_agent_rl.md)
