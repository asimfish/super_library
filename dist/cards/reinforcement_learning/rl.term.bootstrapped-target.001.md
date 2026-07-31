# Super Library card: rl.term.bootstrapped-target.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### bootstrapped target

`rl.term.bootstrapped-target.001` · term · reinforcement_learning, world_models · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A learning target that contains a prediction produced by the current model or a target model for a later state, rather than relying entirely on observed outcomes.

**Use:** Name the prediction being reused and where gradients are stopped. Distinguish RL bootstrapping from statistical bootstrap resampling.

**Avoid:** Do not imply that a bootstrapped target is unbiased or independent of the network being trained.

**Patterns:**

- The critic is updated toward a bootstrapped target computed with the target value network.
- We stop gradients through the $n$-step return target.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/value_learning.md)
