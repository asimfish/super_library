# Super Library card: wm.term.controllable-generation.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### action-controllable generation

`wm.term.controllable-generation.001` · term · world_models · method, related_work, experiments

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Generation whose predicted future changes in response to an explicit action or control sequence supplied to the model.

**Use:** Demonstrate controllability by varying actions while holding context fixed and evaluate action-consistent consequences, not appearance alone.

**Avoid:** Do not call text- or context-conditioned generation action-controllable when no agent control enters the dynamics.

**Patterns:**

- Holding the initial context fixed, we vary {action sequence} to evaluate whether the generated futures reflect the commanded behavior.

**Verify in primary sources:**

- `zhu2025-irasim-fine-grained-world` — [IRASim: A Fine-Grained World Model for Robot Manipulation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhu_IRASim_A_Fine-Grained_World_Model_for_Robot_Manipulation_ICCV_2025_paper.html) (ICCV 2025)
- `bar2025-navigation-world-models` — [Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html) (CVPR 2025)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/world_models.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [topic: video_occupancy_world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/video_occupancy_world_models.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/planning_imagination.md)
