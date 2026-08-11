# Super Library card: rl.usage-note.support-generalization.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### distinguish interpolation within dataset support from extrapolation beyond it

`rl.usage-note.support-generalization.001` · usage_note · reinforcement_learning, robot_learning · related_work, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Good performance on held-out samples drawn from familiar coverage does not by itself establish reliable action selection in unsupported regions.

**Use:** Describe how evaluation differs from the behavior-data distribution and whether the policy is constrained or regularized near dataset support.

**Avoid:** Do not call a random trajectory split out-of-distribution evaluation without demonstrating a meaningful shift.

**Patterns:**

- The test tasks use held-out trajectories but remain within the dataset's object and action coverage.
- Generalization beyond the behavior-policy support remains to be established.

**Verify in primary sources:**

- `kumar2020cql` — [Conservative Q-Learning for Offline Reinforcement Learning](https://proceedings.neurips.cc/paper/2020/hash/0d2b2061826a5df3221116a5085a6052-Abstract.html) (NeurIPS 2020)
- `kostrikov2022iql` — [Offline Reinforcement Learning with Implicit Q-Learning](https://openreview.net/forum?id=68n2s9ZJWF8) (ICLR 2022)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: offline_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/offline_rl.md)
