# Super Library card: rl.definition.self-play.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### self-play

`rl.definition.self-play.001` · definition · reinforcement_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training scheme in which an agent improves by playing with or against copies or past versions of itself, or a population thereof, generating its own curriculum of increasingly strong counterparts without human gameplay data.

**Use:** State the opponent or partner pool (current copy, past checkpoints, or a population), how counterparts are sampled, and how nontransitivity or strategy cycling is handled. Evaluate against held-out strategies or humans, not only within the training population.

**Avoid:** Do not conflate self-play with imitation of human games, and do not claim general strength from within-population results alone.

**Patterns:**

- The agent trains via self-play against {opponent pool} sampled by {scheme}.
- We evaluate against {held-out opponents or human players} to test robustness beyond the training population.

**Verify in primary sources:**

- `zha2021-douzero-mastering-doudizhu-self` — [DouZero: Mastering DouDizhu with Self-Play Deep Reinforcement Learning](https://proceedings.mlr.press/v139/zha21a.html) (ICML 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: multi_agent_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/multi_agent_rl.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/policy_optimization.md)
