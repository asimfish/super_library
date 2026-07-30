# Super Library card: wm.definition.model-based-rl.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### model-based reinforcement learning

`wm.definition.model-based-rl.001` · definition · world_models, reinforcement_learning · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Reinforcement learning that uses a model of environment dynamics, learned or known, to improve decision making through planning, synthetic experience, value estimation, or policy optimization.

**Use:** Explain the role of the model rather than applying the label solely because the architecture contains a predictor.

**Avoid:** Do not conflate model-based RL with supervised next-step prediction that never affects decisions.

**Patterns:**

- The method is model-based because the learned dynamics model is used to {plan actions or optimize the policy}.
- Model-based reinforcement learning can use predicted transitions for {downstream decision process}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/planning_imagination.md)
- [topic: model_based_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/model_based_rl.md)
