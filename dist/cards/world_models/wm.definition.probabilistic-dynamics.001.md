# Super Library card: wm.definition.probabilistic-dynamics.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### probabilistic dynamics model

`wm.definition.probabilistic-dynamics.001` · definition · world_models, reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A dynamics model that represents a conditional distribution over future states or latent states rather than returning only one point prediction.

**Use:** State what is random, how the distribution is parameterized, and whether it is intended to model environment stochasticity, model uncertainty, or both.

**Avoid:** Do not assume that any predicted variance is calibrated or that it cleanly separates aleatoric and epistemic uncertainty.

**Patterns:**

- We learn a probabilistic dynamics model $p_\theta(s_{t+1}\mid s_t,a_t)$ and propagate multiple particles during planning.
- The latent transition predicts a distribution over {next latent variable} conditioned on {state and action}.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/dynamics_representation.md)
