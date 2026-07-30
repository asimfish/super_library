# Super Library card: emb.usage-note.vla-vs-elm.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### distinguish VLA policies from embodied language models

`emb.usage-note.vla-vs-elm.001` · usage_note · embodied_ai, robot_learning, vision_language_action · related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A VLA label emphasizes action generation for control, whereas an embodied language model may use sensor inputs for reasoning or prediction without directly producing executable actions.

**Use:** Classify a method by its actual output and control interface rather than model backbone. Some systems may satisfy both descriptions, but the overlap should be stated.

**Avoid:** Do not use VLA, vision-language model, and embodied language model interchangeably.

**Patterns:**

- Unlike embodied language models evaluated on reasoning tasks, our VLA directly predicts {robot control representation}.
- The model supplies high-level plans to a separate low-level policy and is therefore not evaluated as an end-to-end VLA controller.

**Verify in primary sources:**

- `driess2023palme` — [PaLM-E: An Embodied Multimodal Language Model](https://proceedings.mlr.press/v202/driess23a.html) (ICML 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/vla_models.md)
- [topic: robot_foundation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/robot_foundation.md)
