# Super Library card: wm.sentence-pattern.related-work.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### World-model methods can be organized by {representation}, {training objective}, and {decision mechanism}.

`wm.sentence-pattern.related-work.001` · sentence_pattern · world_models · related_work

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Provides a technical-axis structure for a world-model related-work paragraph.

**Use:** Instantiate each axis with verified method families: observation-space versus latent prediction, reconstruction versus task-oriented objectives, and online planning versus imagined policy learning.

**Avoid:** Do not force methods into mutually exclusive categories when they combine mechanisms.

**Patterns:**

- World-model methods can be organized by the space in which they predict, the objectives used to learn the representation, and whether decisions arise from online planning or policy learning in imagination.

**Verify in primary sources:**

- `hafner2019planet` — [Learning Latent Dynamics for Planning from Pixels](https://proceedings.mlr.press/v97/hafner19a.html) (ICML 2019)
- `hafner2020dreamer` — [Dream to Control: Learning Behaviors by Latent Imagination](https://openreview.net/forum?id=S1lOTC4tDS) (ICLR 2020)
- `hansen2022tdmpc` — [Temporal Difference Learning for Model Predictive Control](https://proceedings.mlr.press/v162/hansen22a.html) (ICML 2022)
- `hansen2024tdmpc2` — [TD-MPC2: Scalable, Robust World Models for Continuous Control](https://proceedings.iclr.cc/paper_files/paper/2024/hash/cf73d57b6dcda32b293df7c2d5341f49-Abstract-Conference.html) (ICLR 2024)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [topic: world_model_general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/world_model_general.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/dynamics_representation.md)
