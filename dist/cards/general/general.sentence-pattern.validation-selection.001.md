# Super Library card: general.sentence-pattern.validation-selection.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Hyperparameters are selected on {validation set} using {criterion}.

`general.sentence-pattern.validation-selection.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Declares which data and objective selected hyperparameters or checkpoints.

**Use:** State whether one configuration is shared across tasks and whether test or shifted conditions influenced selection.

**Avoid:** Do not report test-optimal settings as if they were selected without access to test results.

**Patterns:**

- Hyperparameters are selected on {validation tasks} using {metric}, and the selected configuration is fixed for all test tasks.
- We select the checkpoint with the highest {validation metric} before evaluating it once on {test set}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
