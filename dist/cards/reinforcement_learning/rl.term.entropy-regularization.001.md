# Super Library card: rl.term.entropy-regularization.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### entropy regularization / entropy-augmented objective

`rl.term.entropy-regularization.001` · term · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

An objective term that rewards policy entropy in addition to task return, encouraging stochasticity according to a specified temperature or coefficient.

**Use:** State the entropy convention, coefficient or temperature, and whether it is fixed or adapted. Distinguish action entropy from state-distribution diversity.

**Avoid:** Do not claim that entropy regularization necessarily improves exploration or robustness in every environment.

**Patterns:**

- The actor maximizes expected return and policy entropy with temperature $\alpha$.
- We adapt the entropy temperature toward a target entropy of {value}.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/exploration_skills_goals.md)
