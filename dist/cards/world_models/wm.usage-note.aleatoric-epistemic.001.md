# Super Library card: wm.usage-note.aleatoric-epistemic.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### aleatoric versus epistemic uncertainty in learned dynamics

`wm.usage-note.aleatoric-epistemic.001` · usage_note · world_models, reinforcement_learning · related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Aleatoric uncertainty describes conditional variability that remains even with complete knowledge, whereas epistemic uncertainty reflects limited knowledge about the predictive model and may shrink with informative data.

**Use:** Explain which modeling component is intended to represent each uncertainty and validate the interpretation when it matters to planning or risk.

**Avoid:** Do not claim perfect decomposition merely because a network predicts a variance and an ensemble produces disagreement.

**Patterns:**

- The output distribution represents conditional stochasticity, while ensemble disagreement serves as a practical proxy for model uncertainty.
- We do not assume that the two uncertainty sources are perfectly identifiable from the available transitions.

**Verify in primary sources:**

- `chua2018pets` — [Deep Reinforcement Learning in a Handful of Trials using Probabilistic Dynamics Models](https://proceedings.neurips.cc/paper_files/paper/2018/hash/3de568f8597b94bda53149c7d7f5958c-Abstract.html) (NeurIPS 2018)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/dynamics_representation.md)
