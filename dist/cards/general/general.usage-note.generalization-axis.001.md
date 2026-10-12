# Super Library card: general.usage-note.generalization-axis.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### name the generalization axis and held-out unit

`general.usage-note.generalization-axis.001` · usage_note · general, world_models, reinforcement_learning, embodied_ai, robot_learning, vision_language_action · abstract, introduction, experiments, limitations, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Generalization is always relative to a specified shift, such as unseen objects, tasks, environments, users, embodiments, or combinations.

**Use:** State what was held out during training and what unit is averaged at evaluation. Prefer 'generalization to unseen objects' over an unqualified 'generalization ability.'

**Avoid:** Do not infer broad out-of-distribution generalization from a random train–test split over nearly identical samples.

**Patterns:**

- We evaluate generalization to unseen {objects or tasks} by holding out {unit} during training.
- The current study does not establish transfer across unseen {embodiments or environments}.

**Contextual usage profile (not a universal word whitelist):**

- Part of speech: reporting instruction
- Scope: A reporting framework for named held-out units, not a claim of transfer across untested shifts.
- Collocations: generalization axis, held-out evaluation, generalization to unseen environments
- Not interchangeable with: random train-test split, cross-embodiment transfer
- Rule references: claims.calibration, experiments.scope

Original conditional contrast; do not import its facts into a draft:
- Given: Only objects were held out; environments and embodiments were unchanged.
- Misuse: The policy generalizes across environments and embodiments.
- Preferred: We evaluate generalization to held-out objects in the same environment and embodiment.
- Why: Binds the conclusion to the tested shift and avoids adding untested transfer axes.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: conclusion](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/conclusion.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
