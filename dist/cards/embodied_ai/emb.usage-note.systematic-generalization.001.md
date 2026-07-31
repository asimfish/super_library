# Super Library card: emb.usage-note.systematic-generalization.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### evaluate embodied generalization along separately controlled axes

`emb.usage-note.systematic-generalization.001` · usage_note · embodied_ai, robot_learning, vision_language_action · experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Systematic evaluation varies identified factors—such as objects, placements, task templates, prompt compositions, environments, or embodiments—while documenting which combinations were withheld.

**Use:** Define each split procedurally and report results by axis. Use 'zero-shot' only when the evaluated factor or combination was absent from training under the stated protocol.

**Avoid:** Do not collapse all held-out conditions into one generalization score that hides qualitatively different shifts.

**Patterns:**

- We report separate results for unseen objects, unseen task compositions, and unseen embodiments.
- The hardest split holds out both {factor one} and {factor two} during training.

**Verify in primary sources:**

- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `oneill2024openx` — [Open X-Embodiment: Robotic Learning Datasets and RT-X Models](https://doi.org/10.1109/ICRA57147.2024.10611477) (ICRA 2024)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/vision_language_action.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/limitations.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/embodied_reasoning_agents.md)
