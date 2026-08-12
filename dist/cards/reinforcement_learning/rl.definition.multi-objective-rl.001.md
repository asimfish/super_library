# Super Library card: rl.definition.multi-objective-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### multi-objective reinforcement learning

`rl.definition.multi-objective-rl.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A setting with a vector of reward signals whose trade-offs are resolved by preferences or scalarization, so the target is a policy or set of policies covering the preference space rather than a single scalar-optimal policy.

**Use:** State the objectives and the scalarization or preference model, whether preferences are known, adversarial, or revealed at test time, and report performance across the preference space rather than at one weighting.

**Avoid:** Do not collapse multiple objectives into one fixed weighting without stating it, and do not claim coverage of the preference space from performance at a single preference.

**Patterns:**

- The reward is {vector of objectives}; the policy conditions on {preference representation}.
- We evaluate across {preference distribution}, reporting {coverage metric} rather than one weighted return.

**Verify in primary sources:**

- `wu2021-accommodating-picky-customers-regret` — [Accommodating Picky Customers: Regret Bound and Exploration Complexity for Multi-Objective Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2021/hash/6d7d394c9d0c886e9247542e06ebb705-Abstract.html) (NeurIPS 2021)
- `wiltzer2024-foundations-multivariate-distributional-reinforcement` — [Foundations of Multivariate Distributional Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b76bec34ef5e0c0ceedff6edfbefc9f5-Abstract-Conference.html) (NeurIPS 2024)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
- [topic: safe_robust_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/safe_robust_rl.md)
