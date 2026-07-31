# Super Library card: general.sentence-pattern.caption-main-results.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Results on {dataset or task} under {protocol}. {Metric direction and units}.

`general.sentence-pattern.caption-main-results.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Provides the first two functional sentences of a self-contained main-results caption.

**Use:** Continue with aggregation, uncertainty, runs, emphasis, and protocol exceptions. Use the exact split and evaluation setting.

**Avoid:** Do not use a one-phrase caption that forces readers to reconstruct the protocol from the prose.

**Patterns:**

- Results on {tasks} under the {split} protocol. Higher {metric} is better; values are {units} and report {statistic} over {runs}.
- Evaluation on {environment} with {budget}. Lower {metric} is better, and bold marks the best comparable result.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
