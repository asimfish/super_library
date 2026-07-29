# Super Library card: emb.term.proprioception.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### proprioceptive observation

`emb.term.proprioception.001` · term · robot_learning, embodied_ai · method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

Internal measurements of the agent's body state, such as joint positions, velocities, actuator states, or inertial readings.

**Use:** List the included signals, normalization, sampling rate, and temporal alignment with exteroceptive observations.

**Avoid:** Do not include external camera observations under proprioception.

**Patterns:**

- The policy conditions on visual features and proprioceptive observations comprising {signals}.
- We synchronize proprioception with {camera frames} at {rate}.

**Verify in primary sources:**

- `kumar2021rma` — [RMA: Rapid Motor Adaptation for Legged Robots](https://roboticsproceedings.org/rss17/p011.html) (RSS 2021)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
