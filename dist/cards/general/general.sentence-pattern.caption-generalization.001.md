# Super Library card: general.sentence-pattern.caption-generalization.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Generalization from {training condition} to {held-out condition}.

`general.sentence-pattern.caption-generalization.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Names the training and held-out conditions at the start of a generalization-table caption.

**Use:** Continue with the held-out unit, selection protocol, metrics, runs, uncertainty, and reference condition.

**Avoid:** Do not use 'unseen' without specifying what was withheld and whether it influenced model selection.

**Patterns:**

- Generalization from {training environments} to held-out {environments}. Test environments are excluded from training and validation.
- Transfer from {embodiments} to unseen {embodiments}; success rates are averaged over {trials}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
