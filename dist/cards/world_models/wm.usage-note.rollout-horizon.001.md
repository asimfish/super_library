# Super Library card: wm.usage-note.rollout-horizon.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### model rollout horizon trades synthetic coverage against accumulated error

`wm.usage-note.rollout-horizon.001` · usage_note · world_models, reinforcement_learning · method, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Increasing the number of learned transitions can provide more synthetic experience but also exposes training or planning to errors that compound under the rollout distribution.

**Use:** Treat rollout length as an algorithmic choice tied to model accuracy and policy shift. Report its schedule and include a sensitivity study when central to the claim.

**Avoid:** Do not state that shorter or longer model rollouts are universally better across data regimes and tasks.

**Patterns:**

- We use a rollout horizon of {k}; longer rollouts degrade {metric} as prediction errors accumulate.
- The rollout horizon increases from {a} to {b} as the model is trained on more real data.

**Verify in primary sources:**

- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)
- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/planning_imagination.md)
