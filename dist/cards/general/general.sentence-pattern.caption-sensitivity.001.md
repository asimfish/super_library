# Super Library card: general.sentence-pattern.caption-sensitivity.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Sensitivity to {parameter}; {default marker} denotes the selected configuration.

`general.sentence-pattern.caption-sensitivity.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Introduces a sensitivity caption and identifies the configuration used elsewhere in the paper.

**Use:** State the full range, selection data and objective, fixed factors, runs, uncertainty, and changed resource when scale varies.

**Avoid:** Do not show only values near the chosen optimum or imply a scaling law from a narrow sweep.

**Patterns:**

- Sensitivity to {parameter}; the dagger denotes the validation-selected configuration. All other settings and seeds are fixed.
- Scaling with {data or model size}; bold identifies the configuration used for the main experiments, not an oracle test optimum.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
