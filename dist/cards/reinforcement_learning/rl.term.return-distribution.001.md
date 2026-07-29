# Super Library card: rl.term.return-distribution.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### return distribution / value distribution

`rl.term.return-distribution.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The probability distribution of cumulative discounted reward induced by environment randomness and policy actions from a specified state or state–action pair.

**Use:** Condition the distribution explicitly and distinguish its expectation from the full random-return law.

**Avoid:** Do not call a collection of value-network predictions a return distribution unless the learning formulation models random returns.

**Patterns:**

- We approximate the state–action return distribution $Z^\pi(s,a)$ with {representation}.
- The expected value is recovered by taking the mean of the learned return distribution.

**Verify in primary sources:**

- `bellemare2017distributional` — [A Distributional Perspective on Reinforcement Learning](https://proceedings.mlr.press/v70/bellemare17a.html) (ICML 2017)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
