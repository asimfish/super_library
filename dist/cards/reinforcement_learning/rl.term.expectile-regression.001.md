# Super Library card: rl.term.expectile-regression.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### expectile value regression

`rl.term.expectile-regression.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

An asymmetric squared-loss regression objective whose expectile parameter emphasizes different portions of the target distribution; in IQL it is used to fit an upper expectile of in-dataset action values.

**Use:** Define the expectile parameter and targets. Do not describe expectiles as quantiles; they use asymmetric squared rather than absolute loss.

**Avoid:** Do not claim that an upper expectile is the maximum unless limiting conditions are established.

**Patterns:**

- The value function is fitted by expectile regression to emphasize high-valued actions present in the dataset.
- We set the expectile parameter to {tau}.

**Verify in primary sources:**

- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/offline_rl.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/value_learning.md)
