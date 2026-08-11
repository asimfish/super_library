# Super Library protocol: Experimental analysis: evidence before interpretation

`experiments.analysis` · `analysis_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Turn verified results into precise analysis paragraphs without merely narrating a table or overstating a mechanism.

**Use when:** Writing main-result, ablation, robustness, efficiency, or failure-analysis paragraphs after displays are finalized.

## Required inputs

- The research question and comparison axis.
- Exact table or figure location and verified values.
- Aggregation, uncertainty, and statistical unit.
- Expected mechanism, plausible alternatives, exceptions, and failure cases.

## Functional protocol

### 1. State the evidence (required)

- Point to the display and identify the rows, columns, or trend relevant to the question.
- Quantify the difference in the metric's natural unit and distinguish relative from absolute change.
- State whether the pattern is consistent across tasks, datasets, seeds, scales, or shifts.

### 2. Calibrate interpretation (required)

- Use 'is consistent with' or 'suggests' for a mechanism not directly identified.
- Name alternative explanations such as scale, data, tuning, or compute when they remain uncontrolled.
- Do not equate lack of statistical significance with equivalence.

### 3. Report boundary and trade-off (required)

- Identify settings where the advantage diminishes, reverses, or becomes unstable.
- State quality–efficiency, robustness–accuracy, or data–compute trade-offs explicitly.
- Connect a failure case to the claim it limits.

## Choose one internal template

### Main result paragraph

Use when: A table or figure answers one primary research question.

1. Question and display pointer.
2. Quantified main comparison.
3. Consistency across relevant settings.
4. Calibrated explanation.
5. Exception, uncertainty, or trade-off.

### Ablation paragraph

Use when: Variants test components, losses, data sources, or design choices.

1. Component question and full-model anchor.
2. Matched variant comparison.
3. Magnitude relative to uncertainty.
4. Interaction or non-additivity if modules are coupled.
5. Narrow conclusion about contribution, not universal necessity.

### Failure analysis paragraph

Use when: Failures are categorized qualitatively or quantitatively.

1. Failure taxonomy and denominator.
2. Most frequent or consequential category.
3. Condition associated with the failure.
4. Plausible explanation separated from observed fact.
5. Implication for scope, deployment, or future evaluation.

## Verification

- Every adjective such as consistent, substantial, stable, or efficient is tied to a visible statistic or named condition.
- The prose does not repeat every cell; it selects the comparison that answers the stated question.
- Interpretations preserve uncertainty and do not exceed the intervention or control structure.
- Negative and anomalous results are not silently omitted from the described trend.

## Avoid

- Beginning every sentence with 'Table X shows' and paraphrasing the full table.
- Using 'because' or 'due to' when an ablation only establishes association.
- Describing a one-benchmark gain as general improvement.
- Calling overlapping error bars a significance test or non-overlapping bars proof of a mechanism.

## Retrieve related sentence cards only as needed

- [Our results suggest that {bounded interpretation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.phrase.results-suggest.001.md) — `general.phrase.results-suggest.001`
- [These results are consistent with the hypothesis that {mechanism}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.causal-caution.001.md) — `general.sentence-pattern.causal-caution.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [statistically significant versus substantial improvement](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.significant.001.md) — `general.usage-note.significant.001`
- [replace vague effectiveness claims with the observed outcome](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.effectiveness.001.md) — `general.usage-note.effectiveness.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
