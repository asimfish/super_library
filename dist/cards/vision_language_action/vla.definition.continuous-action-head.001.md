# Super Library card: vla.definition.continuous-action-head.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### continuous action head

`vla.definition.continuous-action-head.001` · definition · vision_language_action, robot_learning · method, related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy output module that directly parameterizes continuous robot controls rather than representing every action dimension as a discrete language token.

**Use:** Specify the distribution or regression objective, action parameterization, prediction horizon, and embodiment-specific output dimensions.

**Avoid:** Do not use this term as a synonym for the entire policy or assume that a continuous head eliminates temporal discretization.

**Patterns:**

- The continuous action head maps {fused representation} to {horizon} steps of {action parameterization}.

**Verify in primary sources:**

- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)
- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)

Catalog routes:
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/action_representation.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/vla_models.md)
