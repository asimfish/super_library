# Super Library card: wm.definition.latent-action-representation.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### latent action representation

`wm.definition.latent-action-representation.001` · definition · world_models, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A learned variable inferred from observation transitions or videos to encode action-like changes when the corresponding low-level action labels are absent, often for conditioning a predictive model or later alignment with executable controls.

**Use:** State the inference inputs, temporal granularity, discrete or continuous parameterization, training objective, and how the latent variable is aligned with or decoded into the target robot action space.

**Avoid:** Do not call a motion code an executable robot action before validating its alignment or decoder, and do not assume that a latent action is identifiable, causal, or embodiment-invariant by construction.

**Patterns:**

- An inverse model infers a latent action from adjacent observations, and the world model predicts the next observation conditioned on that code.
- During robot fine-tuning, latent actions are aligned with {target control representation} using {paired supervision}.

**Verify in primary sources:**

- `zhang2024-prelar-world-model-pre` — [PreLAR: World Model Pre-training with Learnable Action Representation](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/3363_ECCV_2024_paper.php) (ECCV 2024)
- `schmidt2024-learning-act-without-actions` — [Learning to Act without Actions](https://openreview.net/forum?id=rvUq3cxpDF) (ICLR 2024)
- `gao2025-adaworld-learning-adaptable-world-models` — [AdaWorld: Learning Adaptable World Models with Latent Actions](https://proceedings.mlr.press/v267/gao25u.html) (ICML 2025)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/dynamics_representation.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/action_representation.md)
