# Super Library card: rl.sentence-pattern.related-work.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### RL methods should be compared at matched interaction, data, and evaluation budgets.

`rl.sentence-pattern.related-work.001` · sentence_pattern · reinforcement_learning · related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Frames a fair reinforcement-learning comparison around the budgets that determine efficiency and performance.

**Use:** Report environment steps, dataset size, number of seeds, evaluation episodes, compute where relevant, and tuning access. Separate final performance from sample efficiency.

**Avoid:** Do not compare results taken from incompatible protocols without a caveat.

**Patterns:**

- We compare methods at matched environment-interaction budgets and report performance over {number} seeds using {aggregation}.
- Because {prior result} uses a different data budget, we report it separately rather than treating it as a controlled baseline.

**Verify in primary sources:**

- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
