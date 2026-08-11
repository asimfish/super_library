# Super Library card: rl.definition.constrained-mdp.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### constrained Markov decision process (CMDP)

`rl.definition.constrained-mdp.001` · definition · reinforcement_learning · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An MDP augmented with one or more cumulative cost constraints, so the policy objective optimizes return while satisfying specified cost limits.

**Use:** Define reward, every cost signal, discounting or horizon, thresholds, feasibility assumptions, and whether constraints apply in expectation or with another risk criterion.

**Avoid:** Do not describe an unconstrained penalty objective as a CMDP without stating the corresponding constraints and thresholds.

**Patterns:**

- We formulate the task as a CMDP that maximizes {return} subject to {expected cumulative cost} not exceeding {threshold}.

**Verify in primary sources:**

- `khattar2023-cmdp-within-online-framework` — [A CMDP-within-online framework for Meta-Safe Reinforcement Learning](https://iclr.cc/virtual/2023/poster/11412) (ICLR 2023)
- `zhou2025-chpo-constrained-hybrid-action` — [CHPO: Constrained Hybrid-action Policy Optimization for Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2025/hash/5eca2e4fe7858cbbfef4e08573cfcb25-Abstract-Conference.html) (NeurIPS 2025)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: safe_robust_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/safe_robust_rl.md)
