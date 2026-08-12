# Super Library card: emb.definition.mobile-manipulation.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### mobile manipulation

`emb.definition.mobile-manipulation.001` · definition · embodied_ai, robot_learning, vision_language_action · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A robot task family in which a mobile base and a manipulator are controlled together, so task success depends on coordinating base placement or motion with arm trajectories rather than manipulating from a fixed base.

**Use:** State how base and arm are coordinated (a joint policy, decoupled planning, or bi-level optimization), what determines base placement, and which fixed-base assumptions still hold. Report navigation and manipulation outcomes separately when the evaluation allows it.

**Avoid:** Do not present fixed-base manipulation results as mobile manipulation, and do not silently reduce the problem to navigation followed by independent manipulation without stating that decoupling.

**Patterns:**

- The mobile manipulation policy coordinates {base motion} with {end-effector trajectory} to accomplish {task goal}.
- Base waypoints are selected to satisfy {feasibility criterion}, after which the arm executes {manipulation primitive}.

**Verify in primary sources:**

- `wu2025-momanipvla-transferring-vision-language` — [MoManipVLA: Transferring Vision-language-action Models for General Mobile Manipulation](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_MoManipVLA_Transferring_Vision-language-action_Models_for_General_Mobile_Manipulation_CVPR_2025_paper.html) (CVPR 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_manipulation.md)
- [topic: vla_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/vla_models.md)
