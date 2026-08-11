# Super Library card: wm.term.trajectory-sampling.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### trajectory sampling for uncertainty propagation

`wm.term.trajectory-sampling.001` · term · world_models, reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A sampling procedure that propagates multiple hypothetical trajectories through a probabilistic dynamics model to approximate distributions over future outcomes.

**Use:** Specify the particle count, how ensemble members are selected across time, and how predicted returns are aggregated for action selection.

**Avoid:** Do not use the term as a synonym for collecting real environment trajectories or for generic Monte Carlo evaluation without a learned model.

**Patterns:**

- We propagate {number} particles through the probabilistic ensemble and rank candidate action sequences by their predicted returns.
- Each particle samples {model or transition noise} according to {sampling rule}.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/planning_imagination.md)
