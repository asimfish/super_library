# Super Library card: emb.definition.active-perception.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### active perception

`emb.definition.active-perception.001` · definition · embodied_ai, robot_learning · introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Perception in which an agent's actions influence which observations become available, coupling information acquisition with control.

**Use:** Describe the action-dependent sensing process and whether actions are chosen explicitly for information gain or jointly for task reward.

**Avoid:** Do not call ordinary data augmentation active perception.

**Patterns:**

- The task requires active perception because the agent must move to reveal {occluded or unobserved information}.
- Actions affect both {task progress} and the observations available for future decisions.

**Verify in primary sources:**

- `xia2018gibson` — [Gibson Env: Real-World Perception for Embodied Agents](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) (CVPR 2018)
- `savva2019habitat` — [Habitat: A Platform for Embodied AI Research](https://openaccess.thecvf.com/content_ICCV_2019/html/Savva_Habitat_A_Platform_for_Embodied_AI_Research_ICCV_2019_paper.html) (ICCV 2019)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
