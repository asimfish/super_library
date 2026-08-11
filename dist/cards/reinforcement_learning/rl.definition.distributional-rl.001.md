# Super Library card: rl.definition.distributional-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### distributional reinforcement learning

`rl.definition.distributional-rl.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A value-based perspective that models a probability distribution over random returns rather than only their expected value.

**Use:** Specify the distributional parameterization, projection or regression objective, and how action selection reduces the distribution to a decision criterion.

**Avoid:** Do not equate a return distribution with epistemic uncertainty about the value estimate.

**Patterns:**

- The critic approximates the distribution of discounted returns with {atoms or quantiles}.
- Actions are selected by the expectation of the learned return distribution.

**Verify in primary sources:**

- `bellemare2017distributional` — [A Distributional Perspective on Reinforcement Learning](https://proceedings.mlr.press/v70/bellemare17a.html) (ICML 2017)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/value_learning.md)
