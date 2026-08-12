# Super Library card: emb.definition.social-navigation.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### social navigation

`emb.definition.social-navigation.001` · definition · embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Embodied navigation among humans in which the agent must reach its goal while respecting human comfort and social conventions, so evaluation considers interaction quality, such as collisions, proximity, and yielding, in addition to goal success.

**Use:** State how humans are modeled or replayed, which social criteria are measured (collision rate, personal-space violations, encounter outcomes), and whether social behavior comes from auxiliary objectives, rewards, or demonstrations.

**Avoid:** Do not call navigation social merely because moving obstacles exist; the evaluation must measure human-aware behavior, not only goal success.

**Patterns:**

- The policy navigates to {goal} among {human models}, penalizing {social violation measure}.
- We evaluate encounters with {metric set} beyond success rate on {benchmark}.

**Verify in primary sources:**

- `cancelli2023-exploiting-proximity-aware-tasks` — [Exploiting Proximity-Aware Tasks for Embodied Social Navigation](https://openaccess.thecvf.com/content/ICCV2023/html/Cancelli_Exploiting_Proximity-Aware_Tasks_for_Embodied_Social_Navigation_ICCV_2023_paper.html) (ICCV 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: embodied_navigation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_navigation.md)
