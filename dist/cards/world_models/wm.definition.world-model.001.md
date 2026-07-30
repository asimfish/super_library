# Super Library card: wm.definition.world-model.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### world model

`wm.definition.world-model.001` · definition · world_models, reinforcement_learning · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learned predictive model of how an environment evolves, typically conditioned on the agent's actions and used to support prediction, planning, or policy learning.

**Use:** State what variables the model predicts, whether prediction occurs in observation or latent space, and how the model is used downstream. Community usage is broad, so define the paper's operational scope.

**Avoid:** Do not treat every video generator or static scene representation as a world model without an action, temporal, or decision-making connection.

**Patterns:**

- We use a world model to predict {future latent states or observations} conditioned on {current state and action sequence}.
- Here, world model refers to {learned transition components} used for {planning or policy optimization}.

**Verify in primary sources:**

- `ha2018worldmodels` — [Recurrent World Models Facilitate Policy Evolution](https://papers.nips.cc/paper/2018/hash/2de5d16682c3c35007e4e92982f1a2ba-Abstract.html) (NeurIPS 2018)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/dynamics_representation.md)
