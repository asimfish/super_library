# Super Library card: rl.definition.offline-distribution-shift.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### distribution shift in offline RL

`rl.definition.offline-distribution-shift.001` · definition · reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A mismatch between state–action distributions represented in a fixed dataset and those induced by the learned policy, which makes value estimates for unsupported actions unreliable.

**Use:** Specify whether the shift concerns states, actions, transitions, tasks, or observations. Connect the failure mode to bootstrapping or policy optimization when applicable.

**Avoid:** Do not use 'distribution shift' without naming the two distributions being compared.

**Patterns:**

- Offline policy optimization can induce distribution shift by assigning probability to actions poorly covered by the dataset.
- We regularize {policy or value estimate} toward the support of the behavior data.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
