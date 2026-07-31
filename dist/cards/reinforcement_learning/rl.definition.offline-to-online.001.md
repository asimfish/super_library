# Super Library card: rl.definition.offline-to-online.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### offline-to-online reinforcement learning

`rl.definition.offline-to-online.001` · definition · reinforcement_learning · introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learning protocol that initializes from a fixed offline dataset and subsequently improves the policy using additional online environment interaction.

**Use:** Report offline data provenance, initialization method, online interaction budget, replay mixture, and whether baselines receive the same data.

**Avoid:** Do not label online fine-tuning as an offline-RL result without separately reporting the online budget.

**Patterns:**

- We initialize from {offline dataset} and continue learning for {online budget} transitions using {data-mixture strategy}.

**Verify in primary sources:**

- `wagenmaker2023-leveraging-offline-data-online` — [Leveraging Offline Data in Online Reinforcement Learning](https://proceedings.mlr.press/v202/wagenmaker23a.html) (ICML 2023)
- `wang2024-making-offline-rl-online` — [Making Offline RL Online: Collaborative World Models for Offline Visual Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/b041cbfcc3f282a9b3c8eb9c16177529-Abstract-Conference.html) (NeurIPS 2024)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/offline_rl.md)
