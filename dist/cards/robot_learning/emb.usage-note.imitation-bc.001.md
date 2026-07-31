# Super Library card: emb.usage-note.imitation-bc.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### imitation learning versus behavioral cloning

`emb.usage-note.imitation-bc.001` · usage_note · robot_learning, embodied_ai · introduction, related_work, method, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Imitation learning is the broader problem of learning behavior from demonstrations, while behavioral cloning usually denotes direct supervised prediction of expert actions from observations.

**Use:** Use behavioral cloning for the supervised objective and imitation learning for the wider family, which may include interactive data collection, occupancy matching, or other objectives.

**Avoid:** Do not use the two terms as universally interchangeable when the algorithm is not direct supervised cloning.

**Patterns:**

- We use behavioral cloning to fit the policy to demonstration state–action pairs.
- The method belongs to imitation learning but differs from behavioral cloning in {interactive or distributional mechanism}.

**Verify in primary sources:**

- `ho2016gail` — [Generative Adversarial Imitation Learning](https://papers.nips.cc/paper/2016/hash/cc7e2b878868cbae992d1fb743995d8f-Abstract.html) (NeurIPS 2016)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/robot_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/embodied_ai.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: embodied_reasoning_agents](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/embodied_reasoning_agents.md)
