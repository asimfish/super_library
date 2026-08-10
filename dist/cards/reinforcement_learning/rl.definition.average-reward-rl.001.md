# Super Library card: rl.definition.average-reward-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### average-reward reinforcement learning

`rl.definition.average-reward-rl.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A continuing-task reinforcement-learning formulation that evaluates a policy by its long-run reward per time step rather than by a finite-horizon or geometrically discounted return.

**Use:** State the limiting-average convention and assumptions such as ergodicity or unichain structure. Distinguish average reward from the differential value or bias function used for policy evaluation and optimization.

**Avoid:** Do not use average-reward RL to mean the arithmetic mean of episodic returns across evaluation runs.

**Patterns:**

- We optimize the long-run average reward under {ergodicity or unichain assumptions}.
- Unlike discounted RL, the average-reward objective evaluates continuing behavior without a geometric discount factor.

**Verify in primary sources:**

- `ganesh2025-sharper-global-convergence-analysis` — [A Sharper Global Convergence Analysis for Average Reward Reinforcement Learning via an Actor-Critic Approach](https://proceedings.mlr.press/v267/ganesh25b.html) (ICML 2025)
- `suttle2023-beyond-exponentially-fast-mixing` — [Beyond Exponentially Fast Mixing in Average-Reward Reinforcement Learning via Multi-Level Monte Carlo Actor-Critic](https://proceedings.mlr.press/v202/suttle23a.html) (ICML 2023)
- `hairi2022-finite-time-convergence-sample` — [Finite-Time Convergence and Sample Complexity of Multi-Agent Actor-Critic Reinforcement Learning with Average Reward](https://iclr.cc/virtual/2022/poster/6851) (ICLR 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
