# Super Library card: wm.term.model-predictive-control.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### model predictive control (MPC)

`wm.term.model-predictive-control.001` · term · world_models, reinforcement_learning, robot_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A control strategy that repeatedly optimizes a finite-horizon action sequence using a model, executes an initial portion, and replans from the new state.

**Use:** State the planning horizon, optimizer, objective, terminal value, and how many actions are executed before replanning.

**Avoid:** Do not use MPC as a synonym for any policy that consumes model predictions.

**Patterns:**

- At each environment step, MPC optimizes {candidate action sequences} over a horizon of {H} and executes {first action or action chunk}.
- We augment the finite-horizon objective with {terminal value estimate}.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
