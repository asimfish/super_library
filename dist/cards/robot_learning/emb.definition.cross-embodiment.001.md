# Super Library card: emb.definition.cross-embodiment.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### cross-embodiment transfer

`emb.definition.cross-embodiment.001` · definition · robot_learning, embodied_ai · abstract, introduction, related_work, experiments, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

The application or adaptation of learned knowledge across robots or agents with different morphologies, sensors, action spaces, or control interfaces.

**Use:** State whether transfer is zero-shot, requires fine-tuning, or only shares pretraining. Reserve 'generalization' for a held-out evaluation that directly supports it.

**Avoid:** Do not claim cross-embodiment generalization when every evaluated robot appears in training under the same interface.

**Patterns:**

- We evaluate cross-embodiment transfer by adapting the pretrained policy to {held-out robot} with {amount of data}.
- The embodiments differ in {morphology, camera setup, and action space}.

**Verify in primary sources:**

- `ghosh2024octo` — [Octo: An Open-Source Generalist Robot Policy](https://www.roboticsproceedings.org/rss20/p090.html) (RSS 2024)

Catalog routes:
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: sim_to_real_robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/sim_to_real_robot_learning.md)
