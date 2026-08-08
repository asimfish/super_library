# Super Library card: emb.sentence-pattern.related-work.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Embodied methods should be positioned by supervision, interaction regime, and deployment assumptions.

`emb.sentence-pattern.related-work.001` · sentence_pattern · embodied_ai, robot_learning · related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Structures embodied-AI related work around how data is obtained, whether learning is interactive, and what information or hardware is available at deployment.

**Use:** Use concrete axes such as demonstrations versus rewards, simulation versus real data, online versus offline collection, and privileged versus deployable observations.

**Avoid:** Do not group methods only by architecture when their data and deployment assumptions dominate the comparison.

**Patterns:**

- We organize prior work by its supervision signal, whether training uses online interaction, and the sensory information available at deployment.
- Unlike methods trained on {data regime}, our approach assumes {different verified regime}.

**Verify in primary sources:**

- `xia2018gibson` — [Gibson Env: Real-World Perception for Embodied Agents](https://openaccess.thecvf.com/content_cvpr_2018/html/Xia_Gibson_Env_Real-World_CVPR_2018_paper.html) (CVPR 2018)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)
- `khazatsky2024droid` — [DROID: A Large-Scale In-The-Wild Robot Manipulation Dataset](https://roboticsproceedings.org/rss20/p120.html) (RSS 2024)
- `gu2017asynchronous` — [Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates](https://ieeexplore.ieee.org/document/7989385) (ICRA 2017)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_reasoning_agents.md)
