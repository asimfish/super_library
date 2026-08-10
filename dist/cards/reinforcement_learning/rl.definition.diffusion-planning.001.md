# Super Library card: rl.definition.diffusion-planning.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### diffusion-based trajectory planning / diffusion planning

`rl.definition.diffusion-planning.001` · definition · reinforcement_learning, world_models · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A decision-making approach that represents trajectories or related planning variables with a diffusion generative model and produces a plan through conditioned or guided iterative denoising.

**Use:** State which states and actions are denoised, the trajectory horizon, conditioning or guidance objective, number of denoising steps, how a plan is selected, and which portion is executed before replanning. Report inference cost separately from task quality.

**Avoid:** Do not conflate trajectory-level diffusion planning with a diffusion policy that predicts only actions conditioned on observations, and do not imply real-time execution without a measured latency protocol.

**Patterns:**

- The diffusion planner iteratively denoises length-{H} state–action trajectories conditioned on {return, goal, or constraint}.
- At each decision point, we sample {number} trajectories, execute {portion}, and replan after {feedback event}.

**Verify in primary sources:**

- `janner2022-planning-diffusion-flexible-behavior` — [Planning with Diffusion for Flexible Behavior Synthesis](https://proceedings.mlr.press/v162/janner22a.html) (ICML 2022)
- `huang2024-diffusion-models-optimizers-efficient` — [Diffusion Models as Optimizers for Efficient Planning in Offline RL](https://www.ecva.net/papers/eccv_2024/papers_ECCV/html/6735_ECCV_2024_paper.php) (ECCV 2024)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/offline_rl.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/planning_imagination.md)
