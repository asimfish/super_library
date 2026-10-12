# Super Library card: wm.definition.objective-mismatch.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### objective mismatch (model-based RL)

`wm.definition.objective-mismatch.001` · definition · world_models, reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The misalignment between the objective used to train a dynamics model, typically prediction accuracy on collected data, and the downstream objective of policy performance, so a model that predicts well can still induce a poor policy.

**Use:** Distinguish the prediction objective from the downstream control objective. Name a mismatch source or alignment mechanism only when supported; report model-quality and control metrics separately and state the training and evaluation distributions.

**Avoid:** Do not report model accuracy alone as evidence of control quality, and do not use objective mismatch loosely for any underperformance unrelated to the model-policy interface.

**Patterns:**

- {model} has lower prediction error but does not improve {control metric} under {protocol}.
- We optimize {supplied alignment objective} and evaluate both {prediction metric} and {control metric}.

**Contextual usage profile (not a universal word whitelist):**

- Part of speech: noun phrase
- Scope: A prediction/control objective distinction, not an automatic diagnosis of why a particular controller fails.
- Collocations: objective mismatch, prediction accuracy versus control performance, model-policy alignment
- Not interchangeable with: compounding model error, distribution shift
- Rule references: claims.calibration, experiments.scope

Original conditional contrast; do not import its facts into a draft:
- Given: {model} has lower prediction error than {baseline}; control return is unchanged; no mechanism was isolated.
- Misuse: The lower error confirms that the world model improves planning.
- Preferred: Prediction error is lower, but control return is unchanged under {protocol}.
- Why: Separates the two measured outcomes without inventing a control gain or an identified causal mechanism.

**Verify in primary sources:**

- `lin2024-because-bilinear-causal-representation` — [BECAUSE: Bilinear Causal Representation for Generalizable Offline Model-based Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/cff98e0b76e05fd1df5c9256724b3af1-Abstract-Conference.html) (NeurIPS 2024)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: model_based_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/model_based_rl.md)
