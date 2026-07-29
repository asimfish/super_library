# Super Library card: rl.definition.temporal-difference.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### temporal-difference (TD) learning

`rl.definition.temporal-difference.001` · definition · reinforcement_learning, world_models · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Learning a value-related prediction by moving it toward a target that combines an observed reward with a bootstrapped estimate of subsequent value.

**Use:** State the exact target, discount, update horizon, target network or stop-gradient treatment, and whether the estimate is on-policy or off-policy.

**Avoid:** Do not describe every loss across adjacent time steps as temporal-difference learning.

**Patterns:**

- We minimize a temporal-difference error against $r_t+\gamma V_{\bar\theta}(s_{t+1})$.
- The latent value is trained with an $n$-step TD target.

**Verify in primary sources:**

- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `haarnoja2018sac` — [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html) (ICML 2018)
- `hessel2018rainbow` — [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/11796) (AAAI 2018)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/world_models.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
