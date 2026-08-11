# Super Library card: wm.term.dynamics-ensemble.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### ensemble dynamics model / probabilistic ensemble

`wm.term.dynamics-ensemble.001` · term · world_models, reinforcement_learning · related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A collection of separately fitted dynamics predictors whose aggregate predictions can improve robustness and provide a practical disagreement signal.

**Use:** Describe initialization, data resampling, ensemble size, and how predictions are combined or sampled. Call disagreement a heuristic for epistemic uncertainty unless a stronger interpretation is justified.

**Avoid:** Do not present an ensemble as an exact Bayesian posterior or treat members trained identically as independent evidence.

**Patterns:**

- We fit an ensemble of {number} dynamics models and sample a member when propagating each particle.
- Planning penalizes action sequences with high ensemble disagreement.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)
- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/dynamics_representation.md)
