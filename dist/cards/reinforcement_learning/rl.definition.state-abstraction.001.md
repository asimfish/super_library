# Super Library card: rl.definition.state-abstraction.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### state abstraction

`rl.definition.state-abstraction.001` · definition · reinforcement_learning, world_models · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A mapping from raw states or observations to a more compact representation that groups states carrying equivalent decision-relevant information, so that policies, values, or models can be learned over the abstract space.

**Use:** State what information the abstraction preserves (for example values, dynamics, or temporal distances), how it is learned or constructed, and which downstream component consumes it. Report whether the abstraction is fixed or trained jointly, and support transfer or sample-efficiency claims with a no-abstraction baseline.

**Avoid:** Do not call every learned encoder a state abstraction without stating the equivalence or information criterion it enforces, and do not equate abstraction quality with task return alone.

**Patterns:**

- The state abstraction maps {raw observations} to {compact representation} while preserving {decision-relevant quantity}.
- We learn the abstraction with {objective} and reuse it across {downstream tasks}, improving sample efficiency over {no-abstraction baseline}.

**Verify in primary sources:**

- `lee2025-temporal-distance-aware-transition` — [Temporal Distance-aware Transition Augmentation for Offline Model-based Reinforcement Learning](https://proceedings.mlr.press/v267/lee25p.html) (ICML 2025)
- `gomez2022-information-optimization-transferable-state` — [Information Optimization and Transferable State Abstractions in Deep Reinforcement Learning](https://doi.org/10.1109/tpami.2022.3200726) (TPAMI 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/dynamics_representation.md)
