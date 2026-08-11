# Super Library card: rl.term.advantage-weighted-bc.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### advantage-weighted behavioral cloning

`rl.term.advantage-weighted-bc.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A policy-learning objective that imitates dataset actions with weights increasing with an estimated advantage, favoring actions judged better than the state-dependent baseline.

**Use:** State the weighting function, temperature or clipping, and the source of advantage estimates. It remains constrained to observed actions at training time.

**Avoid:** Do not describe it as ordinary behavior cloning when weights materially change the data contribution.

**Patterns:**

- The policy is trained by advantage-weighted behavioral cloning over actions in the offline dataset.
- Weights are computed from {advantage estimate} with temperature {beta}.

**Verify in primary sources:**

- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/offline_rl.md)
- [topic: imitation_sequence](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/imitation_sequence.md)
