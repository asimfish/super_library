# Super Library card: emb.definition.cross-robot-data-mixture.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### cross-robot data mixture

`emb.definition.cross-robot-data-mixture.001` · definition · embodied_ai, robot_learning, vision_language_action · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A training collection that combines trajectories from multiple robot platforms, embodiments, institutions, tasks, or data-generation pipelines.

**Use:** Report contributing datasets, sampling weights, action and observation normalization, license or availability constraints, and the target platforms used for evaluation.

**Avoid:** Do not equate a large aggregate trajectory count with balanced coverage across robots or tasks.

**Patterns:**

- We pretrain on a cross-robot mixture and fine-tune on demonstrations from the target embodiment.
- The mixture sampling weights are chosen by {rule} rather than in proportion to raw dataset size.

**Verify in primary sources:**

- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)
- `ghosh2024octo` — [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) (RSS 2024)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_reasoning_agents.md)
