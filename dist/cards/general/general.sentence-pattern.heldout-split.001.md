# Super Library card: general.sentence-pattern.heldout-split.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### The {split} holds out {unit} from all training and selection data.

`general.sentence-pattern.heldout-split.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines a held-out unit and excludes it from both model fitting and selection.

**Use:** Name whether the unit is subject, scene, object, task, environment, embodiment, or temporal block. Disclose any preprocessing learned globally.

**Avoid:** Do not call a test condition unseen if it influenced prompts, hyperparameters, checkpoint selection, or data curation.

**Patterns:**

- The test split holds out {objects} from all training and validation trajectories.
- For cross-environment evaluation, {environments} are excluded from both training and model selection.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
