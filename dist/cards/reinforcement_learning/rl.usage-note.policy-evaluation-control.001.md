# Super Library card: rl.usage-note.policy-evaluation-control.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### policy evaluation versus control

`rl.usage-note.policy-evaluation-control.001` · usage_note · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Policy evaluation estimates returns for a fixed policy, whereas control additionally seeks or improves a policy to obtain higher return.

**Use:** State whether a theoretical property or operator applies only under a fixed policy or also under policy improvement and maximization.

**Avoid:** Do not transfer a convergence or contraction statement from policy evaluation to control without checking the additional assumptions.

**Patterns:**

- The distributional operator is analyzed separately for fixed-policy evaluation and control.
- Our theorem concerns policy evaluation; the control variant is assessed empirically.

**Verify in primary sources:**

- `bellemare2017distributional` — [A Distributional Perspective on Reinforcement Learning](https://proceedings.mlr.press/v70/bellemare17a.html) (ICML 2017)
- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
