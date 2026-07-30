# Super Library card: general.sentence-pattern.caption-ablation.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Ablation of {components} with all variants trained under {matched protocol}.

`general.sentence-pattern.caption-ablation.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces an ablation caption and states the matched condition needed to compare variants.

**Use:** Define component indicators, full-model row, metric, runs, uncertainty, and any retuning policy in the remaining caption.

**Avoid:** Do not claim a matched ablation when variants use different data, budgets, selection, or evaluation.

**Patterns:**

- Ablation of {components} with all variants trained under the same {data and compute budget}. Values report {statistic} over {seeds}.
- Component analysis on {task}; the full model is {row}, and each variant changes {factor}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
