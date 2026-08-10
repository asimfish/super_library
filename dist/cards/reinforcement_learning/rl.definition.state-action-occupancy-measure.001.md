# Super Library card: rl.definition.state-action-occupancy-measure.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### state–action occupancy measure

`rl.definition.state-action-occupancy-measure.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A measure of how frequently a policy visits each state–action pair under the environment dynamics, with the precise weighting determined by a discounted, finite-horizon, or stationary formulation.

**Use:** State the horizon or discounting convention, normalization, initial-state distribution, and whether the measure is stationary. Use it to make a policy objective or coverage assumption explicit.

**Avoid:** Do not confuse a policy occupancy measure with a spatial occupancy map or an occupancy-prediction world model.

**Patterns:**

- We express the objective as a utility of the discounted state–action occupancy measure induced by $\pi$.
- The constraint is defined over the stationary occupancy measure under {ergodicity assumptions}.

**Verify in primary sources:**

- `barakat2025-global-optimality-policy-gradient` — [On the Global Optimality of Policy Gradient Methods in General Utility Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/72411ab2fd50c0d1f1a4489896d96489-Abstract-Conference.html) (NeurIPS 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
