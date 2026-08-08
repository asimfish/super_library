# Super Library card: wm.definition.occupancy-world-model.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### occupancy world model

`wm.definition.occupancy-world-model.001` · definition · world_models, embodied_ai · abstract, introduction, related_work, method

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A world model that predicts future spatial occupancy, often together with motion or semantic attributes, rather than synthesizing only RGB observations.

**Use:** Name the spatial representation, coordinate frame, temporal horizon, supervised targets, and use in planning or forecasting.

**Avoid:** Do not equate occupancy accuracy with collision-free or task-success performance without downstream evaluation.

**Patterns:**

- The occupancy world model forecasts {spatial representation} over {horizon} and provides {downstream module} with {predicted quantity}.

**Verify in primary sources:**

- `feng2025-gaussian-based-world-model` — [Gaussian-based World Model: Gaussian Priors for Voxel-Based Occupancy Prediction and Future Motion Prediction](https://openaccess.thecvf.com/content/ICCV2025/html/Feng_Gaussian-based_World_Model_Gaussian_Priors_for_Voxel-Based_Occupancy_Prediction_and_ICCV_2025_paper.html) (ICCV 2025)
- `huang2024-neural-volumetric-world-models` — [Neural Volumetric World Models for Autonomous Driving](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/2571_ECCV_2024_paper.php) (ECCV 2024)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: video_occupancy_world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/video_occupancy_world_models.md)
