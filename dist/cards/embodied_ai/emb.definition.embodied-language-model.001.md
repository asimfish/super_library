# Super Library card: emb.definition.embodied-language-model.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### embodied multimodal language model

`emb.definition.embodied-language-model.001` · definition · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A language-model-based system that directly incorporates continuous or encoded sensor modalities to support reasoning or prediction grounded in an embodied environment.

**Use:** Specify the sensor encoders, how their outputs enter the language model, the training tasks, and whether the system predicts language, plans, values, or executable actions.

**Avoid:** Do not assume that multimodal grounding alone makes the model a closed-loop robot controller.

**Patterns:**

- The embodied language model interleaves visual and state-estimation embeddings with text tokens.
- The model supports {planning or question answering}, while a separate controller executes robot actions.

**Verify in primary sources:**

- `driess2023palme` — [PaLM-E: An Embodied Multimodal Language Model](https://proceedings.mlr.press/v202/driess23a.html) (ICML 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
