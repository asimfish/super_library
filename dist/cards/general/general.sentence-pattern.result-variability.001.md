# Super Library card: general.sentence-pattern.result-variability.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Variation across {seeds or trials} is {statistic}, indicating {bounded inference}.

`general.sentence-pattern.result-variability.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Uses a named variability statistic to qualify the stability of an empirical result.

**Use:** Name standard deviation, interquartile range, confidence interval, or another appropriate statistic and keep the inference modest.

**Avoid:** Do not call a method stable from one run or from low variation over correlated evaluation episodes.

**Patterns:**

- Variation across seeds is {standard deviation}, indicating that the ranking is {stable or uncertain} under this protocol.
- The interval across trials is {range}, so the observed difference should be interpreted as {bounded conclusion}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
