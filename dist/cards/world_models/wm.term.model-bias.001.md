# Super Library card: wm.term.model-bias.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### model bias in model-based reinforcement learning

`wm.term.model-bias.001` · term · world_models, reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Distortion in policy learning or planning caused by systematic discrepancies between learned model transitions and the environment transitions relevant to the evaluated policy.

**Use:** Identify the state–action distribution and downstream quantity affected. Separate model bias from finite-sample variance and generic policy-estimation error.

**Avoid:** Do not equate low average one-step validation loss with negligible policy-relevant model bias.

**Patterns:**

- Long synthetic rollouts can amplify model bias when the policy visits state–action pairs poorly covered by real data.
- We evaluate model error under the current policy distribution rather than only on the training split.

**Verify in primary sources:**

- `janner2019mbpo` — [When to Trust Your Model: Model-Based Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2019/hash/5faf461eff3099671ad63c6f3f094f7f-Abstract.html) (NeurIPS 2019)
- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: model_based_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/model_based_rl.md)
