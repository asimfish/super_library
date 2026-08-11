# Super Library card: wm.definition.visual-world-model.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### visual world model for embodied agents

`wm.definition.visual-world-model.001` · definition · world_models, embodied_ai · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A predictive model that represents how an embodied agent's visual environment may evolve, often conditioned on motion or actions and used for navigation, planning, or policy learning.

**Use:** Specify predicted modalities, spatial frame, action or path conditioning, and whether the output is used by the agent. Separate plausible generation from geometrically accurate prediction.

**Avoid:** Do not infer physical consistency or control utility from visual realism alone.

**Patterns:**

- The visual world model predicts {RGB, depth, or semantics} at {future viewpoints} conditioned on {agent path or actions}.
- We evaluate whether predicted observations support {navigation or manipulation decision}.

**Verify in primary sources:**

- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)
- `zhen2025embodiedworld` — [Learning 4D Embodied World Models](https://openaccess.thecvf.com/content/ICCV2025/html/Zhen_Learning_4D_Embodied_World_Models_ICCV_2025_paper.html) (ICCV 2025)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: video_occupancy_world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/video_occupancy_world_models.md)
- [topic: embodied_navigation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_navigation.md)
