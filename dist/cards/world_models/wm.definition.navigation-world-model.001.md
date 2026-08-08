# Super Library card: wm.definition.navigation-world-model.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### navigation world model

`wm.definition.navigation-world-model.001` · definition · world_models, embodied_ai · related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A predictive environment model specialized for forecasting navigation-relevant observations, states, or transitions under candidate agent motions.

**Use:** Specify its spatial representation, action interface, prediction target, and how a planner or policy consumes predictions.

**Avoid:** Do not use the label for a static map or localization model without a predictive transition component.

**Patterns:**

- The navigation world model predicts {navigation-relevant target} under {candidate motion} and supports {planning or policy update}.

**Verify in primary sources:**

- `bar2025-navigation-world-models` — [Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html) (CVPR 2025)
- `koh2021pathdreamer` — [Pathdreamer: A World Model for Indoor Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Koh_Pathdreamer_A_World_Model_for_Indoor_Navigation_ICCV_2021_paper.html) (ICCV 2021)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/planning_imagination.md)
- [topic: embodied_navigation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_navigation.md)
