# Super Library card: rl.term.update-to-data-ratio.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### update-to-data (UTD) ratio

`rl.term.update-to-data-ratio.001` · term · reinforcement_learning, world_models · method, experiments, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The number of gradient updates performed per collected environment step, a central knob for sample-efficient off-policy and model-based training that trades faster learning against overfitting to limited experience.

**Use:** Report the UTD ratio whenever sample-efficiency claims are made, state whether it is fixed or adapted during training, and say how overfitting from high ratios is detected or mitigated, for example validation on held-out experience or regularization.

**Avoid:** Do not compare sample efficiency across methods with different UTD ratios without disclosing them, and do not treat a higher ratio as free performance since it can overfit the replayed experience.

**Patterns:**

- We train with a UTD ratio of {value}, performing {updates} gradient updates per environment step.
- The ratio is adapted by {detection mechanism} to balance under- and overfitting of {model or critic}.

**Verify in primary sources:**

- `dorka2023-dynamic-update-data-ratio` — [Dynamic Update-to-Data Ratio: Minimizing World Model Overfitting](https://iclr.cc/virtual/2023/poster/11616) (ICLR 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/value_learning.md)
- [topic: model_based_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/model_based_rl.md)
