# Super Library card: rl.definition.return-conditioned-sequence.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### return-conditioned sequence modeling

`rl.definition.return-conditioned-sequence.001` · definition · reinforcement_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Modeling actions as a sequence prediction problem conditioned on a desired return together with past states and actions.

**Use:** Specify tokenization, context, conditioning signal, and how desired returns are chosen at inference. Do not assume conditioning guarantees achievement of the requested return.

**Avoid:** Do not describe a return-conditioned model as optimizing return through online RL unless it actually performs such updates.

**Patterns:**

- The policy predicts the next action conditioned on {return-to-go} and {trajectory context}.
- At inference, we condition the sequence model on {target return}.

**Verify in primary sources:**

- `chen2021decisiontransformer` — [Decision Transformer: Reinforcement Learning via Sequence Modeling](https://papers.nips.cc/paper_files/paper/2021/hash/7f489f642a0ddb10272b5c31057f0663-Abstract.html) (NeurIPS 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/offline_rl.md)
- [topic: imitation_sequence](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/imitation_sequence.md)
