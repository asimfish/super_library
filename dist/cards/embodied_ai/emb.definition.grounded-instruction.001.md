# Super Library card: emb.definition.grounded-instruction.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### grounded instruction following

`emb.definition.grounded-instruction.001` · definition · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Mapping linguistic instructions to actions by relating language to perceived entities, spatial relations, state changes, and interaction possibilities in the environment.

**Use:** State the grounding modalities and whether supervision includes demonstrations, symbolic plans, object annotations, or only task success.

**Avoid:** Do not claim grounding when language is used only as an opaque class label.

**Patterns:**

- The agent grounds {instruction phrase} in {visual entities and state changes} before selecting actions.
- We learn grounded instruction following from {demonstrations or interaction feedback}.

**Verify in primary sources:**

- `anderson2018vln` — [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) (CVPR 2018)
- `shridhar2020alfred` — [ALFRED: A Benchmark for Interpreting Grounded Instructions for Everyday Tasks](https://openaccess.thecvf.com/content_CVPR_2020/html/Shridhar_ALFRED_A_Benchmark_for_Interpreting_Grounded_Instructions_for_Everyday_Tasks_CVPR_2020_paper.html) (CVPR 2020)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: egocentric_3d_grounding](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/egocentric_3d_grounding.md)
- [topic: language_conditioned_control](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/language_conditioned_control.md)
