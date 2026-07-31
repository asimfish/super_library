# Super Library card: emb.term.multimodal-action.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### multimodal action distribution

`emb.term.multimodal-action.001` · term · robot_learning · introduction, related_work, method, experiments, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

An action distribution with multiple distinct high-probability behaviors, such as different valid trajectories for accomplishing the same task.

**Use:** Explain the source of multimodality and evaluate mode coverage or task success; multiple samples do not by themselves establish meaningful modes.

**Avoid:** Do not use multimodal to mean that the input has multiple sensor modalities.

**Patterns:**

- The policy must represent a multimodal action distribution because {multiple strategies} are valid for the same observation.
- We visualize samples corresponding to {distinct action modes}.

**Verify in primary sources:**

- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/embodied_reasoning_agents.md)
