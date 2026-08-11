# Super Library card: rl.definition.hierarchical-policy.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### hierarchical policy

`rl.definition.hierarchical-policy.001` · definition · reinforcement_learning, vision_language_action · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A control architecture that decomposes decision making across levels, where a high-level policy selects subgoals, skills, or intermediate commands at a coarser timescale and one or more low-level policies execute them as primitive actions.

**Use:** Specify what the high level outputs (subgoals, skills, or language commands), the timescales of the levels, how each level is trained (jointly, separately, or with frozen components), and how the interface between levels is constrained or grounded so low-level execution stays feasible.

**Avoid:** Do not call a pipeline hierarchical merely because it contains multiple modules; the levels must operate at different decision timescales or abstraction levels with a defined interface.

**Patterns:**

- The high-level policy proposes {subgoal or command} every {decision interval}, and the low-level policy executes {primitive actions} conditioned on it.
- We restrict the high-level action space to {reachable or grounded set} so that low-level execution remains feasible.

**Verify in primary sources:**

- `shi2025-hi-robot-open-ended` — [Hi Robot: Open-Ended Instruction Following with Hierarchical Vision-Language-Action Models](https://proceedings.mlr.press/v267/shi25d.html) (ICML 2025)
- `zhang2023-adjacency-constraint-efficient-hierarchical` — [Adjacency Constraint for Efficient Hierarchical Reinforcement Learning](https://doi.org/10.1109/tpami.2022.3192418) (TPAMI 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/exploration_skills_goals.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/vla_models.md)
