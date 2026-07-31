# Super Library card: general.sentence-pattern.caption-efficiency.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Quality and deployment cost measured under {hardware and timing protocol}.

`general.sentence-pattern.caption-efficiency.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Frames an efficiency caption around both outcome quality and a reproducibly measured deployment resource.

**Use:** Name hardware, precision, batch, input, warm-up, timing boundary, repeats, resource units, and metric directions.

**Avoid:** Do not label a table efficiency when it reports only parameter count or latency without task quality.

**Patterns:**

- Quality and deployment cost measured on {hardware} at {precision} and batch size {value}. Latency includes {boundary}.
- Task success and control latency under {deployment protocol}; values report {statistic} over {repeats}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/experiments.md)
