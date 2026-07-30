# Super Library card: emb.definition.vln.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### vision-and-language navigation (VLN)

`emb.definition.vln.001` · definition · embodied_ai · abstract, introduction, related_work, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A task in which an embodied agent follows a natural-language route instruction by grounding it in visual observations and selecting navigation actions.

**Use:** Specify environment type, action space, instruction source, navigation graph or continuous control, and generalization split.

**Avoid:** Do not conflate VLN with object-goal navigation that has no free-form instruction.

**Patterns:**

- In VLN, the agent maps a route instruction and a sequence of egocentric observations to navigation actions.
- We evaluate generalization to {unseen environments or instructions}.

**Verify in primary sources:**

- `anderson2018vln` — [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://openaccess.thecvf.com/content_cvpr_2018/html/Anderson_Vision-and-Language_Navigation_Interpreting_CVPR_2018_paper.html) (CVPR 2018)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: embodied_navigation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/embodied_navigation.md)
- [topic: egocentric_3d_grounding](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/egocentric_3d_grounding.md)
