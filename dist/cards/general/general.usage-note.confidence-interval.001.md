# Super Library card: general.usage-note.confidence-interval.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### confidence interval

`general.usage-note.confidence-interval.001` · usage_note · general, world_models, reinforcement_learning, embodied_ai, robot_learning, vision_language_action · experiments, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

An interval estimate of a specified statistic using a method with stated nominal coverage; it is not the observed spread of individual trials.

**Use:** Name the statistic, confidence level, interval method, independent sampling unit, and aggregation. For a bootstrap, disclose the resampling unit and dependence structure. Report uncertainty for the difference when comparing methods; overlapping marginal intervals alone do not resolve the comparison.

**Avoid:** Do not label mean ± standard deviation as a confidence interval, treat episodes from one policy as independent training runs, or infer equivalence from an interval containing zero. Do not select bootstrap settings or fabricate an interval when only a mean was supplied.

**Patterns:**

- We report {statistic} with a {level}% confidence interval computed using {method} over {independent units}.
- The estimated difference in {metric} is {value}, with a {level}% {interval method} confidence interval of {bounds}.

**Contextual usage profile (not a universal word whitelist):**

- Part of speech: noun phrase
- Scope: Uncertainty about a named statistic under a stated sampling design. The interval method must be provided or justified, not inferred from a sentence template.
- Collocations: confidence interval, bootstrap confidence interval, interval estimate
- Not interchangeable with: standard deviation, standard error, credible interval
- Rule references: claims.calibration, sentences.attachment, experiments.scope

Original conditional contrast; do not import its facts into a draft:
- Given: Only {mean} and the standard deviation {sd} across {runs} training runs are supplied; no interval was computed.
- Misuse: The {level}% confidence interval is {mean} ± {sd}.
- Preferred: The mean is {mean}, with a standard deviation of {sd} across {runs} training runs.
- Why: Retains the supplied descriptive statistic without fabricating an interval or nominal coverage.

**Verify in primary sources:**

- `agarwal2021statisticalprecipice` — [Deep Reinforcement Learning at the Edge of the Statistical Precipice](https://proceedings.neurips.cc/paper/2021/hash/f514cec81cb148559cf475e7426eed5e-Abstract.html) (NeurIPS 2021)

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
