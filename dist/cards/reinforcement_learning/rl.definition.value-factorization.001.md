# Super Library card: rl.definition.value-factorization.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### value factorization (multi-agent RL)

`rl.definition.value-factorization.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Decomposing a centralized joint action-value function or joint policy into per-agent components combined by a mixing structure, so agents act decentrally while training uses centralized information, as in centralized training with decentralized execution.

**Use:** State the factorization class and its representational restriction (monotonic mixing, entity-wise, or policy factorization), what centralized information training uses, and which coordination structures the restriction cannot express.

**Avoid:** Do not assume a factorized value function represents all coordination optima; restricted mixing can be unable to express tasks requiring tightly coupled simultaneous actions.

**Patterns:**

- The joint value factorizes as {mixing structure} over per-agent utilities trained with {centralized information}.
- We characterize tasks where {factorization class} cannot represent the optimal joint policy.

**Verify in primary sources:**

- `gupta2021-uneven-universal-value-exploration` — [UneVEn: Universal Value Exploration for Multi-Agent Reinforcement Learning](https://proceedings.mlr.press/v139/gupta21a.html) (ICML 2021)
- `zhang2021-fop-factorizing-optimal-joint` — [FOP: Factorizing Optimal Joint Policy of Maximum-Entropy Multi-Agent Reinforcement Learning](https://proceedings.mlr.press/v139/zhang21m.html) (ICML 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: multi_agent_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/multi_agent_rl.md)
