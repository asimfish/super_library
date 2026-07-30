# Super Library card: wm.definition.task-oriented-model.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### task-oriented latent dynamics model

`wm.definition.task-oriented-model.001` · definition · world_models, reinforcement_learning · introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A latent dynamics model trained to preserve decision-relevant predictive structure without necessarily reconstructing raw observations.

**Use:** Name the task signals, such as reward, value, or latent consistency, that shape the representation. Use 'implicit world model' only when a cited paper defines that label for its own model.

**Avoid:** Do not treat 'task-oriented' and 'implicit' as general synonyms, or claim that reconstruction is unnecessary for every task family.

**Patterns:**

- We learn a task-oriented latent dynamics model using {reward, value, and consistency objectives} rather than pixel reconstruction.
- The model predicts {decision-relevant quantities} in latent space.

**Verify in primary sources:**

- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `hansen2024tdmpc2` — [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) (ICLR 2024)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/dynamics_representation.md)
