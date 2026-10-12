# Super Library protocol: Experimental analysis: evidence before interpretation

`experiments.analysis` · `analysis_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Build a finding-led argument from verified comparisons, selective numerical anchors and material exceptions; no table recitation or invented explanation.

**Use when:** Writing main-result, ablation, robustness, efficiency, or failure-analysis paragraphs after displays are finalized.

## Required inputs

- The research question and comparison axis.
- Verified values and display locations; identify which tables, captions, and setup remain available to the reader.
- Aggregation, uncertainty, statistical unit, and whether the requested passage is standalone or must preserve every supplied quantity.
- Supported comparisons, claim-changing exceptions, failure cases, and any supplied mechanism evidence. Missing evidence is not a slot to fill.

## Functional protocol

### 1. Plan evidence placement internally (required)

- Keep an internal ledger of claims, values, uncertainty, comparability, exceptions and final locations; print it only if requested.
- Setup defines protocols; captions interpret displays; tables retain results; analysis develops findings. Never cite an absent table to justify omission.
- For standalone passages, translations, all-value requests or missing displays, retain all required quantities and qualifiers; split dense prose without dropping facts.

### 2. State one supported finding and select its evidence (required)

- Start with the supported finding or brief research question, naming the comparison axis and display. A question heading is optional.
- Anchor magnitude, regimes, uncertainty, costs or exceptions in natural units. Distinguish absolute from relative change; avoid redundant endpoints, row recitation and numeric quotas.
- Keep each number attached to its exact scope and denominator; never assign an aggregate figure to a task subset or a subset figure to the aggregate.
- Compare the strongest relevant matched baseline. Describe the cross-setting extent, not only the largest gain; retain reversals and null outcomes.

### 3. Calibrate interpretation (conditional)

- Explain only with supplied supporting analysis. A bounded empirical conclusion is enough; no generic mechanism sentence is required.
- Use 'suggests' or 'is consistent with' only for a supported, unidentified mechanism. Hedging does not license an invented explanation.
- Name uncontrolled alternatives: scale, data, tuning or compute.
- Do not equate lack of statistical significance with equivalence.

### 4. Report boundary and trade-off (required)

- Identify settings where the advantage diminishes, reverses, or becomes unstable.
- State quality–efficiency, robustness–accuracy, or data–compute trade-offs explicitly.
- Connect a failure case to the claim it limits.

### 5. Connect the argument without exposing the scaffold (required)

- Order paragraphs by the empirical question: outcome, changed regime, then an existing diagnostic or trade-off. Each advances the argument.
- Retain the technical subject and comparison axis. Use contrast words for actual contrasts, not decorative transitions or repeated summaries.
- Templates are choices, not a sentence quota. Merge compatible moves; omit unsupported bridges, tests, mechanisms and revisions.

## Choose one internal template

### Main result paragraph

Use when: A table or figure answers one primary research question.

1. Supported finding or brief question, comparison axis and display pointer.
2. Decisive contrast or trend; full coverage stays in the retained display.
3. Material exception, uncertainty or cost beside the claim it qualifies.
4. Bounded answer; mechanism only if separately supported.

### Ablation paragraph

Use when: Variants test components, losses, data sources, or design choices.

1. Component question, matched contrast and recoverable full-model reference.
2. Contrast that distinguishes alternatives, not a sentence for each variant.
3. Effect against reported uncertainty, including adverse or null outcomes.
4. Interactions or non-additivity if components are coupled.
5. Contribution in this setting, not universal necessity.

### Regime-dependent or null result

Use when: A favorable aggregate conceals a reversal, saturation, or no detectable advantage.

1. Where the advantage holds and fails, with a shared display pointer.
2. Contrast or uncertainty that establishes the boundary.
3. Tested-regime conclusion; no detectable difference is not equivalence.

### Outcome followed by a diagnostic

Use when: Separate experiments actually investigate a question raised by the main result.

1. Outcome and the empirical question it leaves unresolved.
2. Existing diagnostic and its changed or measured variable.
3. Evidence that refines the earlier conclusion, with remaining alternatives.

### Failure analysis paragraph

Use when: Failures are categorized qualitatively or quantitatively.

1. Failure taxonomy and denominator.
2. Most frequent or consequential category.
3. Condition associated with the failure.
4. Plausible explanation separated from observed fact.
5. Implication for scope, deployment, or future evaluation.

## Verification

- Every adjective such as consistent, substantial, stable, or efficient is tied to a visible statistic or named condition.
- Each paragraph has one empirical point. Numerical anchors support magnitude, regimes, uncertainty, costs or exceptions; required standalone values still remain.
- Full required values remain at their promised locations. Omitted display cells cannot reverse or materially weaken the prose claim.
- Shared protocol details are recoverable in setup or captions; no standalone excerpt silently depends on them.
- Interpretations preserve uncertainty and do not exceed the intervention or control structure.
- Negative and anomalous results are not silently omitted from the described trend.

## Avoid

- Beginning every sentence with 'Table X shows' and paraphrasing the full table.
- Turning reporting checklists into one overloaded sentence, or repeating 'These results demonstrate the effectiveness' after every comparison.
- Using a favorable average to conceal a reversal, or deleting required numbers merely to reduce numeric density.
- Using 'because' or 'due to' when an ablation only establishes association.
- Describing a one-benchmark gain as general improvement.
- Calling overlapping error bars a significance test or non-overlapping bars proof of a mechanism.

## Retrieve related sentence cards only as needed

- [finding-led experimental narrative](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.result-narrative.001.md) — `general.usage-note.result-narrative.001`
- [preserve evidence without repeating every table cell](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.result-display-allocation.001.md) — `general.usage-note.result-display-allocation.001`
- [Our results suggest that {bounded interpretation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.phrase.results-suggest.001.md) — `general.phrase.results-suggest.001`
- [These results are consistent with the hypothesis that {mechanism}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.causal-caution.001.md) — `general.sentence-pattern.causal-caution.001`
- [{method} improves {metric} by {value} relative to {baseline} under {protocol}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.quantify.001.md) — `general.sentence-pattern.quantify.001`
- [statistically significant versus substantial improvement](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.significant.001.md) — `general.usage-note.significant.001`
- [replace vague effectiveness claims with the observed outcome](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.effectiveness.001.md) — `general.usage-note.effectiveness.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
