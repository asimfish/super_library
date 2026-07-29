# Super Library card: emb.definition.sim-to-real.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### simulation-to-real (sim-to-real) transfer

`emb.definition.sim-to-real.001` · definition · embodied_ai, robot_learning · abstract, introduction, related_work, experiments, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training or developing a model in simulation and deploying or adapting it to a physical system whose observations or dynamics differ from the simulator.

**Use:** Name what transfers, what is randomized or adapted, the real-world evaluation, and whether real data is used before deployment.

**Avoid:** Do not claim zero-shot sim-to-real if any real-world fine-tuning or calibration materially updates the policy.

**Patterns:**

- We evaluate zero-shot sim-to-real transfer by deploying the simulation-trained policy without {real-world policy updates}.
- The transfer gap arises from mismatches in {appearance, dynamics, sensing, or actuation}.

**Verify in primary sources:**

- `tobin2017domainrandomization` — [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://ieeexplore.ieee.org/document/8202133/) (IROS 2017)
- `kumar2021rma` — [RMA: Rapid Motor Adaptation for Legged Robots](https://roboticsproceedings.org/rss17/p011.html) (RSS 2021)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/related_work.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
