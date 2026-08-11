# Super Library card: wm.definition.objective-mismatch.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### objective mismatch (model-based RL)

`wm.definition.objective-mismatch.001` · definition · world_models, reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The misalignment between the objective used to train a dynamics model, typically prediction accuracy on collected data, and the downstream objective of policy performance, so a model that predicts well can still induce a poor policy.

**Use:** State where the mismatch enters (training distribution, loss weighting, confounders, or value-irrelevant detail) and how the method aligns model learning with control, for example value-aware, policy-aware, or causal objectives. Evaluate with both model-quality and policy-return metrics.

**Avoid:** Do not report model accuracy alone as evidence of control quality, and do not use objective mismatch loosely for any underperformance unrelated to the model-policy interface.

**Patterns:**

- Although {model} attains low prediction error, {policy} underperforms because {mismatch source}.
- We mitigate objective mismatch by {alignment mechanism}, improving {return metric} at matched model accuracy.

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
