# Super Library protocol: Experimental analysis: evidence before interpretation

`experiments.analysis` · `analysis_protocol` · section `experiments` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Organize verified results into a finding-led argument: select quantitative evidence, connect comparisons, and preserve claim-changing exceptions without reciting a table or inventing an explanation.

**Use when:** Writing main-result, ablation, robustness, efficiency, or failure-analysis paragraphs after displays are finalized.

## Required inputs

- The research question and comparison axis.
- Verified values and display locations; identify which tables, captions, and setup remain available to the reader.
- Aggregation, uncertainty, statistical unit, and whether the requested passage is standalone or must preserve every supplied quantity.
- Supported comparisons, claim-changing exceptions, failure cases, and any supplied mechanism evidence. Missing evidence is not a slot to fill.

## Functional protocol

### 1. Plan evidence placement internally (required)

- Keep a compact internal ledger of claims, values, uncertainty, comparability, exceptions, and locations. Distinguish preservation across the deliverable from repetition in each paragraph; do not print the ledger unless asked.
- Setup defines the shared protocol; captions make displays interpretable; tables retain the full results; analysis explains the comparison that matters. Never refer to an absent table to justify omission.
- For standalone passages, translation, explicit all-value requests, or missing displays, retain all required quantities and qualifiers. Split dense material across sentences or paragraphs rather than dropping facts.

### 2. State one supported finding and select its evidence (required)

- Open with the finding that answers the research question, or briefly establish the question if needed. Name the comparison axis and attach the relevant display pointer; a question heading is optional.
- Select numerical anchors for magnitude, a regime change, uncertainty, a cost, or an exception. Use natural units and distinguish absolute from relative change; do not narrate every row, duplicate endpoints and derived gains without purpose, or impose a fixed number quota.
- Keep every number bound to the exact scope and denominator the material assigns it: never reattach an aggregate figure to a subset of tasks or a subset figure to the aggregate.
- Describe the supported pattern across settings, including its extent. Compare the strongest relevant matched baseline, not an easier comparator or only the largest gain. Preserve important reversals and null outcomes in the prose.

### 3. Calibrate interpretation (conditional)

- Add an explanation only when supplied analysis supports it. A result paragraph may end at a bounded empirical conclusion; do not append a generic mechanism sentence to sound persuasive.
- Use 'is consistent with' or 'suggests' for an explicitly supported but not identified mechanism. Hedging does not license an invented explanation.
- Name alternative explanations such as scale, data, tuning, or compute when they remain uncontrolled.
- Do not equate lack of statistical significance with equivalence.

### 4. Report boundary and trade-off (required)

- Identify settings where the advantage diminishes, reverses, or becomes unstable.
- State quality–efficiency, robustness–accuracy, or data–compute trade-offs explicitly.
- Connect a failure case to the claim it limits.

### 5. Connect the argument without exposing the scaffold (required)

- Order paragraphs by the empirical question: overall outcome, where it changes, then a diagnostic or trade-off when actually evaluated. Each paragraph advances the argument rather than re-announcing a display.
- Reuse the technical subject and comparison axis to connect sentences. Use however, whereas, or under only for a real contrast; avoid repeated result summaries and decorative transitions.
- Treat template sequences as choices, not a mandatory sentence count. Merge compatible moves, vary openings naturally, and omit unsupported moves rather than inventing a bridge, test, mechanism, or revision.

## Choose one internal template

### Main result paragraph

Use when: A table or figure answers one primary research question.

1. Supported finding or brief question, with the relevant comparison and display pointer.
2. Decisive quantitative contrast or cross-setting trend; use the retained display for full coverage.
3. Claim-changing exception, uncertainty, or cost placed beside the conclusion it qualifies.
4. Bounded empirical answer; add mechanism interpretation only if separately supported.

### Ablation paragraph

Use when: Variants test components, losses, data sources, or design choices.

1. Component question and matched comparison, with a full-model reference recoverable from prose or the retained display.
2. The contrast that distinguishes the design alternatives, not one sentence for every variant.
3. Magnitude relative to reported uncertainty; preserve an unfavorable or null effect.
4. Interaction or non-additivity if modules are coupled.
5. Narrow conclusion about contribution, not universal necessity.

### Regime-dependent or null result

Use when: A favorable aggregate conceals a reversal, saturation, or no detectable advantage.

1. Name where the advantage holds and where it does not, with the shared display pointer.
2. Select the contrast or uncertainty that makes this boundary visible.
3. Limit the conclusion to the tested regime; no detectable difference is not proof of equivalence.

### Outcome followed by a diagnostic

Use when: Separate experiments actually investigate a question raised by the main result.

1. Summarize the outcome and the unresolved empirical question it leaves.
2. Introduce the existing diagnostic and the variable it changes or measures.
3. Use its decisive evidence to refine, not merely repeat, the earlier conclusion; retain alternative explanations.

### Failure analysis paragraph

Use when: Failures are categorized qualitatively or quantitatively.

1. Failure taxonomy and denominator.
2. Most frequent or consequential category.
3. Condition associated with the failure.
4. Plausible explanation separated from observed fact.
5. Implication for scope, deployment, or future evaluation.

## Verification

- Every adjective such as consistent, substantial, stable, or efficient is tied to a visible statistic or named condition.
- Each paragraph has an identifiable empirical point; deleting a numerical anchor would remove evidence for magnitude, regime, uncertainty, cost, or a material exception. A necessary standalone value remains even when it is not an anchor.
- The prose does not repeat every cell of a retained display. All required quantities remain recoverable at their promised locations, and omitted cells cannot reverse or materially weaken the prose claim.
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
