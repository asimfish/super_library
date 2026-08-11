# Super Library card: wm.definition.video-world-model.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### video world model

`wm.definition.video-world-model.001` · definition · world_models · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A predictive model that represents environment evolution in image or video space, usually conditioned on context and optionally on agent actions.

**Use:** Specify conditioning variables, prediction horizon, stochasticity, controllability, and whether generated video is used for planning or only forecasting.

**Avoid:** Do not assume that visually plausible predictions are dynamically faithful or useful for control.

**Patterns:**

- We use a video world model to predict {horizon} future frames conditioned on {context and actions}.

**Verify in primary sources:**

- `po2025-long-context-state-space` — [Long-Context State-Space Video World Models](https://openaccess.thecvf.com/content/ICCV2025/html/Po_Long-Context_State-Space_Video_World_Models_ICCV_2025_paper.html) (ICCV 2025)
- `wang2024-drivedreamer-real-world-driven` — [DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6416_ECCV_2024_paper.php) (ECCV 2024)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: video_occupancy_world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/video_occupancy_world_models.md)
