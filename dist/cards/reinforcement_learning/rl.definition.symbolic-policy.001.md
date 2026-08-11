# Super Library card: rl.definition.symbolic-policy.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### symbolic policy

`rl.definition.symbolic-policy.001` · definition · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A control policy represented by an explicit symbolic expression, program, or rule structure that maps a specified state or feature representation to actions.

**Use:** State the symbol vocabulary or grammar, input representation, search or optimization procedure, action-space support, expression complexity, and whether the policy is learned directly or distilled from a neural policy. Evaluate comprehensibility separately from task return.

**Avoid:** Do not claim that a policy is interpretable merely because it contains symbols, and do not call a neural policy symbolic when only an auxiliary explanation or latent representation is symbolic.

**Patterns:**

- The symbolic policy maps {structured state features} to {actions} through an expression drawn from {grammar or primitive set}.
- We report task return together with expression length and fidelity to {teacher policy, if applicable}.

**Verify in primary sources:**

- `landajuela2021-discovering-symbolic-policies` — [Discovering Symbolic Policies With Deep Reinforcement Learning](https://proceedings.mlr.press/v139/landajuela21a.html) (ICML 2021)
- `zheng2025-symbolic-visual-reinforcement-learning` — [Symbolic Visual Reinforcement Learning: A Scalable Framework With Object-Level Abstraction and Differentiable Expression Search](https://doi.org/10.1109/tpami.2024.3469053) (TPAMI 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
