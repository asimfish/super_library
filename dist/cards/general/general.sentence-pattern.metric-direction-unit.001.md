# Super Library card: general.sentence-pattern.metric-direction-unit.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### Higher values of {metric} indicate {meaning}; results are averaged over {unit}.

`general.sentence-pattern.metric-direction-unit.001` · sentence_pattern · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Defines metric direction, interpretation, and the statistical unit used for aggregation.

**Use:** Use 'lower' where appropriate and name whether the unit is task, scene, episode, trial, seed, or example.

**Avoid:** Do not let readers infer whether a metric is a percentage, fraction, count, error, or normalized score.

**Patterns:**

- Higher values of {metric} indicate {capability}; results are averaged over {tasks} and then over {seeds}.
- Lower {metric} indicates {meaning}; each value is averaged over {evaluation unit}.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
