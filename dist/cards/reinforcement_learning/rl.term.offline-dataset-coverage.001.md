# Super Library card: rl.term.offline-dataset-coverage.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### state–action coverage of the offline dataset

`rl.term.offline-dataset-coverage.001` · term · reinforcement_learning, robot_learning · introduction, related_work, method, experiments, limitations, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The range and frequency of states and actions represented by a fixed dataset relative to those needed by a candidate policy or evaluation task.

**Use:** Operationalize coverage with dataset statistics, support assumptions, distances, or task-specific diagnostics; it is not captured by dataset size alone.

**Avoid:** Do not describe a dataset as diverse or well-covered solely because it contains many transitions.

**Patterns:**

- Performance degrades when the learned policy selects actions poorly represented in the offline dataset.
- We report coverage across {tasks, states, actions, or embodiments} in addition to trajectory count.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
