# Super Library card: emb.term.task-success-rate.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### task success rate

`emb.term.task-success-rate.001` · term · embodied_ai, robot_learning · experiments, rebuttal, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The fraction or percentage of evaluation trials that satisfy a predefined task-completion criterion.

**Use:** Define the success criterion, trial unit, number of trials, aggregation level, and treatment of partial completion and timeouts. Provide uncertainty where appropriate.

**Avoid:** Do not compare success rates computed with different horizons, reset policies, human interventions, or success detectors without qualification.

**Patterns:**

- Task success rate is computed over {number} independent trials using {completion criterion}.
- The policy succeeds in {count}/{total} trials, corresponding to {percentage}%.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `kim2025openvla` — [OpenVLA: An Open-Source Vision-Language-Action Model](https://proceedings.mlr.press/v270/kim25c.html) (CoRL 2025)
- `jiang2023vima` — [VIMA: Robot Manipulation with Multimodal Prompts](https://proceedings.mlr.press/v202/jiang23b.html) (ICML 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/experiments.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
