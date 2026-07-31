# Super Library card: general.usage-note.missing-zero-na.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### A dash denotes an unreported value, not a measured zero.

`general.usage-note.missing-zero-na.001` · usage_note · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Separates missing or unreported results from numeric zero and from conditions that are not applicable.

**Use:** Define every symbol in the caption or footnote. Use 0 or 0.0 only for a measured zero and N/A only when the metric or condition does not apply.

**Avoid:** Do not encode unavailable, failed, and zero-valued results with the same blank cell or dash.

**Patterns:**

- A dash denotes a result that was not reported; N/A indicates that the metric is not applicable.
- Zero is reported numerically, while failed runs are counted under {failure policy}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
