# Super Library card: emb.term.3d-scene-memory.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### 3D scene memory

`emb.term.3d-scene-memory.001` · term · embodied_ai, world_models · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A persistent spatial representation that aggregates observations into a three-dimensional memory for embodied exploration, grounding, or reasoning.

**Use:** Specify coordinate frame, stored features, update rule, memory lifetime, and how queries access the memory.

**Avoid:** Do not use the term for a single-frame 3D feature tensor that is not maintained across interaction.

**Patterns:**

- The agent updates a 3D scene memory with {features} in {coordinate frame} and queries it for {task}.

**Verify in primary sources:**

- `yang2025-3d-mem-3d-scene` — [3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-Mem_3D_Scene_Memory_for_Embodied_Exploration_and_Reasoning_CVPR_2025_paper.html) (CVPR 2025)
- `lin2025-bip3d-bridging-2d-images` — [BIP3D: Bridging 2D Images and 3D Perception for Embodied Intelligence](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_BIP3D_Bridging_2D_Images_and_3D_Perception_for_Embodied_Intelligence_CVPR_2025_paper.html) (CVPR 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: egocentric_3d_grounding](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/egocentric_3d_grounding.md)
