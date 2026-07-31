# Super Library card: emb.definition.vla.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### vision-language-action (VLA) model

`emb.definition.vla.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A model or policy that conditions on visual observations and language and produces robot actions or an action representation for embodied control.

**Use:** Specify all inputs, the action space, control frequency, training data, and whether actions are generated directly, discretized as tokens, or decoded by a separate head.

**Avoid:** Do not call a vision-language model a VLA merely because its textual output can be interpreted by an external planner.

**Patterns:**

- The VLA policy maps camera observations and a language instruction to a sequence of robot actions.
- We fine-tune the pretrained VLA on {number} demonstrations from {target embodiment}.

**Verify in primary sources:**

- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `zhen2024vla` — [3D-VLA: A 3D Vision-Language-Action Generative World Model](https://proceedings.mlr.press/v235/zhen24a.html) (ICML 2024)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/vla_models.md)
- [topic: robot_foundation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/robot_foundation.md)
