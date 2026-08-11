# Super Library card: emb.term.tactile-sensing.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### tactile sensing

`emb.term.tactile-sensing.001` · term · embodied_ai, robot_learning · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Contact-based measurement at the robot's surfaces, such as forces, pressure, vibration, or binary contact events, that complements vision and proprioception by registering interactions those signals miss.

**Use:** State the tactile modality and resolution (dense arrays versus sparse binary contacts), sensor placement, latency and alignment with other modalities, and the failure the signal prevents, for example decoupled robot-object motion that proprioceptive error cannot register.

**Avoid:** Do not treat fingertip or skin tactile sensing as interchangeable with wrist force-torque sensing, and do not claim contact-rich competence from vision-only results.

**Patterns:**

- {Sparse binary or dense} tactile signals at {mounting locations} register {interaction event} that {other modality} misses.
- We fuse tactile, proprioceptive, and visual streams with {latency budget} alignment for {contact-rich task}.

**Verify in primary sources:**

- `miller2025-enhancing-tactile-based-reinforcement` — [Enhancing Tactile-based Reinforcement Learning for Robotic Control](https://proceedings.neurips.cc/paper_files/paper/2025/hash/bc09efb501c801ed92e181e26a885c2d-Abstract-Conference.html) (NeurIPS 2025)
- `wan2025-rapid-hand-robust-affordable` — [RAPID Hand: Robust, Affordable, Perception-Integrated, Dexterous Manipulation Platform for Embodied Intelligence](https://proceedings.neurips.cc/paper_files/paper/2025/hash/8bead340bb510de5c8356f60ca039efc-Abstract-Conference.html) (NeurIPS 2025)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: robot_manipulation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/robot_manipulation.md)
- [topic: locomotion_dexterity](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/locomotion_dexterity.md)
