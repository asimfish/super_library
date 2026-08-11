# Super Library card: rl.definition.curriculum-reinforcement-learning.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### curriculum reinforcement learning (CRL)

`rl.definition.curriculum-reinforcement-learning.001` · definition · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A reinforcement-learning training paradigm that selects or adapts a sequence of tasks or task distributions so that an agent learns on intermediate conditions before or while progressing toward a target task distribution.

**Use:** Specify the task or context space, what the curriculum changes, how tasks are selected or ordered, the pacing or adaptation signal, the target distribution, and whether evaluation uses a fixed held-out distribution. Difficulty need not be a single scalar or increase monotonically.

**Avoid:** Do not label ordinary shuffling, a fixed benchmark suite, or goal conditioning alone as curriculum reinforcement learning; identify the mechanism that changes the training-task distribution over learning.

**Patterns:**

- The curriculum updates the training-task distribution from {initial distribution} toward {target distribution} according to {progress signal}.
- At iteration {i}, the agent trains on tasks sampled from {p_i(c)}, while evaluation remains fixed on {target distribution}.

**Verify in primary sources:**

- `klink2024-benefit-optimal-transport-curriculum` — [On the Benefit of Optimal Transport for Curriculum Reinforcement Learning](https://doi.org/10.1109/tpami.2024.3390051) (TPAMI 2024)
- `cho2023-outcome-directed-reinforcement-learning` — [Outcome-directed Reinforcement Learning by Uncertainty \& Temporal Distance-Aware Curriculum Goal Generation](https://iclr.cc/virtual/2023/poster/11888) (ICLR 2023)
- `ao2021-co-pilot-collaborative-planning` — [CO-PILOT: COllaborative Planning and reInforcement Learning On sub-Task curriculum](https://proceedings.neurips.cc/paper_files/paper/2021/hash/56577889b3c1cd083b6d7b32d32f99d5-Abstract.html) (NeurIPS 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: exploration_skills_goals](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/exploration_skills_goals.md)
