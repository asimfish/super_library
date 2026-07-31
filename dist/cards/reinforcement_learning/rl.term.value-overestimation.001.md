# Super Library card: rl.term.value-overestimation.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### value overestimation

`rl.term.value-overestimation.001` · term · reinforcement_learning · introduction, related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Systematic upward bias in estimated values, often amplified when optimization selects actions whose estimates are erroneously high.

**Use:** Identify the estimator and distribution on which overestimation is measured. In offline RL, relate it to actions not well supported by data when justified.

**Avoid:** Do not infer overestimation solely because a policy performs poorly.

**Patterns:**

- The critic overestimates values for actions outside the dataset support.
- We measure value overestimation by comparing {predicted quantity} with {reference return}.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/value_learning.md)
