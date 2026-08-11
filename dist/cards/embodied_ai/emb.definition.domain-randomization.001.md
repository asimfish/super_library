# Super Library card: emb.definition.domain-randomization.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### domain randomization

`emb.definition.domain-randomization.001` · definition · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Training over deliberately varied simulation parameters to make a model robust across a distribution intended to cover or bracket variability encountered in the real system.

**Use:** List randomized parameters and distributions, and separate visual randomization from dynamics randomization. Whether the real domain lies within effective support is an empirical question.

**Avoid:** Do not use domain randomization as a generic label for ordinary image augmentation or claim coverage of the real domain without evaluation.

**Patterns:**

- During simulation training, we randomize {textures, lighting, camera, dynamics, or latency} over {specified ranges}.
- Domain randomization exposes the policy to {variation} before real-world deployment.

**Verify in primary sources:**

- `tobin2017domainrandomization` — [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://ieeexplore.ieee.org/document/8202133/) (IROS 2017)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: sim_to_real_robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/sim_to_real_robot_learning.md)
