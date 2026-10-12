# Super Library card: general.usage-note.percentage-points.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### percentage-point difference versus relative percent change

`general.usage-note.percentage-points.001` · usage_note · general, world_models, reinforcement_learning, embodied_ai, robot_learning, vision_language_action · abstract, experiments, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

For a metric expressed in percent, subtracting two percentage values gives a percentage-point difference; relative percent change divides the difference by the stated nonzero reference value.

**Use:** State the metric, comparator and endpoints or a traceable display. Label absolute differences as percentage points and relative changes as percent relative to the reference. Respect metric direction and aggregation; a relative change from a zero reference is undefined.

**Avoid:** Do not silently turn relative improvement into percentage points, assign an aggregate difference to every task, or call points on a normalized score percentage points without a percentage scale.

**Patterns:**

- Success rate rises from {baseline}% to {method}%, a gain of {difference} percentage points.
- Relative to {baseline value}, {error metric} decreases by {relative change}%; lower values indicate better performance.

**Contextual usage profile (not a universal word whitelist):**

- Part of speech: measurement phrases
- Scope: Percentage-point differences apply only to percent-scale metrics; relative percent changes require a named nonzero reference.
- Collocations: percentage points, percentage-point difference, percentage change, relative percent change
- Not interchangeable with: relative percentage improvement, normalized-score points
- Rule references: sentences.attachment, experiments.scope

Original conditional contrast; do not import its facts into a draft:
- Given: On the same protocol, success rate changes from {baseline}% to {method}%; the subtraction is {difference} percentage points.
- Misuse: Success rate improves by {difference}%.
- Preferred: Success rate increases from {baseline}% to {method}%, a gain of {difference} percentage points.
- Why: Makes the absolute unit and reference explicit; do not compute new quantities unless the task permits it and the endpoints are available.

Catalog routes:
- [domain: general](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/general.md)
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/robot_learning.md)
- [domain: vision_language_action](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/vision_language_action.md)
- [section: abstract](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/abstract.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
