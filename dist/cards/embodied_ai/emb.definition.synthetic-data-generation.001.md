# Super Library card: emb.definition.synthetic-data-generation.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### synthetic data generation

`emb.definition.synthetic-data-generation.001` · definition · embodied_ai, robot_learning · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Producing training scenes, trajectories, or annotations with generative or procedural models instead of collecting them from human operators or real environments, so dataset scale and diversity are limited by generation quality rather than collection effort.

**Use:** State what is generated (scenes, actions, or labels), the generative mechanism, how physical feasibility is enforced or filtered, and how much real data remains in the loop. Report downstream policy performance, not only generation fidelity or speed.

**Avoid:** Do not equate synthetic data generation with domain randomization, which varies parameters of an existing scene rather than generating new scenes or trajectories, and do not claim realism from visual quality alone.

**Patterns:**

- We generate {scenes or trajectories} from {conditioning input} with {generative model}, filtering samples that violate {feasibility check}.
- Policies trained on the generated data improve {metric} by {amount} over {human-collected baseline}.

**Verify in primary sources:**

- `lee2025-dynscene-scalable-generation-dynamic` — [DynScene: Scalable Generation of Dynamic Robotic Manipulation Scenes for Embodied AI](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.html) (CVPR 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_manipulation.md)
- [topic: sim_to_real_robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/sim_to_real_robot_learning.md)
