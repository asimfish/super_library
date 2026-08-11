# Super Library card: rl.term.regret.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### regret

`rl.term.regret.001` · term · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The cumulative performance gap between a learning agent and a comparator, typically the best fixed or optimal policy in hindsight, accumulated over the learning process; sublinear regret means average performance approaches the comparator's.

**Use:** State the comparator class, the horizon or episode count regret is measured over, and whether the environment is stochastic, adversarial, or nonstationary. Report dependence on problem quantities such as horizon, dimension, or risk level rather than the rate alone.

**Avoid:** Do not call a performance shortfall regret without a comparator and accumulation window, and do not compare regret bounds across different comparator classes or feedback models as if equivalent.

**Patterns:**

- The algorithm attains {rate} regret over {episodes} episodes against {comparator class}.
- Regret scales with {problem quantity}, matching the lower bound up to {factor}.

**Verify in primary sources:**

- `shi2023-near-optimal-adversarial-reinforcement` — [Near-Optimal Adversarial Reinforcement Learning with Switching Costs](https://iclr.cc/virtual/2023/poster/11984) (ICLR 2023)
- `bastani2022-regret-bounds-risk-sensitive` — [Regret Bounds for Risk-Sensitive Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2022/hash/eb4898d622e9a48b5f9713ea1fcff2bf-Abstract-Conference.html) (NeurIPS 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
