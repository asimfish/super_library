# Super Library card: vla.term.action-expert.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### action expert

`vla.term.action-expert.001` · term · vision_language_action, robot_learning · abstract, introduction, method, related_work

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A specialized policy component that converts multimodal representations into robot actions, often alongside a pretrained vision-language backbone.

**Use:** Describe which parameters are specialized, how information is exchanged with the backbone, and whether the expert is autoregressive, diffusion-based, or otherwise structured.

**Avoid:** Do not imply a standardized architecture; action expert is an architectural role whose realization varies by paper.

**Patterns:**

- An action expert conditions on {backbone features} and predicts {action representation} for {robot embodiment}.

**Verify in primary sources:**

- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)
- `hou2025-dita-scaling-diffusion-transformer` — [Dita: Scaling Diffusion Transformer for Generalist Vision-Language-Action Policy](https://openaccess.thecvf.com/content/ICCV2025/html/Hou_Dita_Scaling_Diffusion_Transformer_for_Generalist_Vision-Language-Action_Policy_ICCV_2025_paper.html) (ICCV 2025)

Catalog routes:
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/vla_models.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/action_representation.md)
