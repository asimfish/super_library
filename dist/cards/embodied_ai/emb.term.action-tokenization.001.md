# Super Library card: emb.term.action-tokenization.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### robot-action tokenization

`emb.term.action-tokenization.001` · term · embodied_ai, robot_learning, vision_language_action · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A representation that maps continuous or structured robot controls into discrete tokens or token-like outputs for sequence-model prediction.

**Use:** Describe discretization bins, dimensions, control semantics, decoding, clipping, and any embodiment-specific normalization.

**Avoid:** Do not assume that language-token and action-token probabilities have the same semantics or that tokenization is lossless.

**Patterns:**

- Each action dimension is discretized into {number} bins and represented by a dedicated token range.
- The predicted action tokens are decoded into {control command} at {frequency} Hz.

**Verify in primary sources:**

- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/vla_models.md)
- [topic: action_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/action_representation.md)
