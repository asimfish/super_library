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

**Contextual usage profile (not a universal word whitelist):**

- Part of speech: sentence pattern
- Scope: Declare metric direction, scale and aggregation unit; distinguish the experimental unit from repeated observations.
- Collocations: metric direction, aggregation unit, independent training runs
- Not interchangeable with: number of evaluation episodes, uncertainty estimate
- Rule references: sentences.attachment, experiments.scope

Original conditional contrast; do not import its facts into a draft:
- Given: Each of {runs} independent training runs is evaluated for {episodes} episodes; a statistic is computed across runs.
- Misuse: Results are averaged over {episodes} independent runs.
- Preferred: Each of {runs} independent training runs is evaluated for {episodes} episodes; {statistic} is computed across runs.
- Why: Does not relabel episodes from one trained policy as independent training runs.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
