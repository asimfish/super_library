# Super Library card: wm.definition.uncertainty-aware-planning.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### uncertainty-aware model-based planning

`wm.definition.uncertainty-aware-planning.001` · definition · world_models, reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Planning that represents or uses uncertainty in learned dynamics when evaluating candidate action sequences, rather than optimizing only a single deterministic forecast.

**Use:** State whether uncertainty is marginalized, sampled, penalized, or used as a constraint. Distinguish predictive uncertainty from risk preference.

**Avoid:** Do not imply safety or robustness solely because the planner propagates a distribution.

**Patterns:**

- The planner samples predictive dynamics and optimizes expected return under the resulting trajectory distribution.
- We penalize candidate plans with high {validated uncertainty statistic}.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/world_model_general.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/planning_imagination.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/dynamics_representation.md)
- [topic: model_based_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/model_based_rl.md)
