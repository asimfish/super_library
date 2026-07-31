# Super Library card: emb.definition.open-vocabulary-manipulation.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### open-vocabulary manipulation

`emb.definition.open-vocabulary-manipulation.001` · definition · embodied_ai, robot_learning · introduction, related_work, experiments

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Manipulation conditioned on object or task descriptions whose evaluation vocabulary is not restricted to a fixed closed set used during task-specific training.

**Use:** Define the held-out unit, language source, object and task splits, perception assumptions, and any foundation-model supervision.

**Avoid:** Do not claim open-vocabulary generalization when test names are new strings for training-seen objects or skills.

**Patterns:**

- We evaluate open-vocabulary manipulation on held-out {objects, concepts, or instructions} while holding {other axis} fixed.

**Verify in primary sources:**

- `wen2025-diffusionvla-scaling-robot-foundation` — [DiffusionVLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression](https://proceedings.mlr.press/v267/wen25g.html) (ICML 2025)
- `zhang2025-vlabench-large-scale-benchmark` — [VLABench: A Large-Scale Benchmark for Language-Conditioned Robotics Manipulation with Long-Horizon Reasoning Tasks](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_VLABench_A_Large-Scale_Benchmark_for_Language-Conditioned_Robotics_Manipulation_with_Long-Horizon_ICCV_2025_paper.html) (ICCV 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/robot_manipulation.md)
- [topic: language_conditioned_control](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/language_conditioned_control.md)
