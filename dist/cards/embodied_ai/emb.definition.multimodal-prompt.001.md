# Super Library card: emb.definition.multimodal-prompt.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### multimodal task prompt

`emb.definition.multimodal-prompt.001` · definition · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A task specification composed of more than one modality, such as interleaved text, images, object crops, goals, or demonstrations.

**Use:** List the modalities, tokenization, temporal order, and information available at test time. Distinguish a prompt that specifies a task from observations generated while executing it.

**Avoid:** Do not call ordinary multimodal observations a task prompt unless they communicate the intended task or goal.

**Patterns:**

- The prompt interleaves a language instruction with images of the target objects.
- We evaluate novel compositions of visual and textual prompt elements.

**Verify in primary sources:**

- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
