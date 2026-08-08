# Super Library card: rl.definition.conservative-q.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### conservative Q-function learning

`rl.definition.conservative-q.001` · definition · reinforcement_learning · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Learning value estimates with an objective that penalizes overly high Q-values, especially for actions not supported by the offline dataset.

**Use:** Describe the exact regularizer and theoretical or empirical property established by the cited method; conservative bias can trade off underestimation and robustness.

**Avoid:** Do not claim that every pessimistic penalty provides a valid lower bound.

**Patterns:**

- The objective regularizes Q-values for out-of-distribution actions while fitting Bellman targets on dataset transitions.
- Conservative value estimation mitigates {specified offline optimization failure}.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/offline_rl.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/value_learning.md)
