# Super Library card: emb.definition.visuomotor-policy.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### visuomotor policy

`emb.definition.visuomotor-policy.001` · definition · robot_learning, embodied_ai · abstract, introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy that maps visual observations, often together with proprioception or goals, to motor actions or action sequences.

**Use:** Specify visual inputs, auxiliary conditioning, action representation, control frequency, and whether perception and control are trained end to end.

**Avoid:** Do not call a pipeline visuomotor if vision only labels a dataset and is unavailable to the deployed controller.

**Patterns:**

- The visuomotor policy maps {image history and proprioception} to {action chunk}.
- We train the policy end to end from {visual input} to {robot command}.

**Verify in primary sources:**

- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)
- `gu2017asynchronous` — [Deep Reinforcement Learning for Robotic Manipulation with Asynchronous Off-Policy Updates](https://ieeexplore.ieee.org/document/7989385) (ICRA 2017)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/embodied_reasoning_agents.md)
