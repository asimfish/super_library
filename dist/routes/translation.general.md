# Super Library one-file route: Chinese-to-English scientific translation

`translation.general` · domain `general` · section `translation` · intent `clarify`

This file is a bounded language context, not scientific evidence. Draft
from the user's verified facts, adapt every pattern, and reopen linked
primary papers before definitions, comparisons, or literature claims.
Do not load the core, catalogs, guide, or cards again for this task.

## Compact contract

- Preserve numbers, notation, negation, uncertainty, comparison direction,
  evaluation scope, and citation placement.
- Prefer field-standard terminology; do not copy a paper sentence or retain
  an unresolved placeholder.
- Bind empirical language to the named protocol, metric, denominator,
  aggregation, uncertainty, and comparison set.
- State evidence before interpretation and retain exceptions, trade-offs,
  null results, and failure boundaries that affect the claim.

## Selected language records

### Although {qualified premise}, {bounded conclusion}.

`general.sentence-pattern.translation-preserve.001` · sentence_pattern · general · translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Preserves a concession and its qualification during Chinese-to-English reconstruction.

**Use:** Keep negation, modality, comparison direction, quantities, and citations attached to the same propositions as in the source.

**Avoid:** Do not upgrade a qualified Chinese claim into an unconditional English conclusion.

**Patterns:**

- Although {method} improves {metric} on {subset}, the difference is not statistically significant across {units}.

### Distinguish possibility, interpretation, empirical evidence, and formal proof.

`general.usage-note.modality.001` · usage_note · general · abstract, introduction, related_work, experiments, limitations, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Modal verbs and evidential verbs serve different functions rather than forming one universal strength ordering.

**Use:** Use 'may/might' for possibility, 'suggests/supports' for a tentative interpretation or evidence relation, 'shows/demonstrates' for a result established within the study design, and 'proves' only for a formal proof under stated assumptions.

**Avoid:** Do not translate 可能 or 表明 into an unqualified 'proves', or assume that any two evidential verbs have a context-free ordering.

**Patterns:**

- The results suggest that {hypothesis}, but do not establish {stronger causal claim}.

### statistically significant versus substantial improvement

`general.usage-note.significant.001` · usage_note · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Statistical significance refers to an inferential test or interval criterion, whereas substantial, marked, or large describes effect magnitude and requires a stated scale.

**Use:** Translate 显著 according to evidence: use 'statistically significant' only when a specified statistical analysis supports it; otherwise report the effect size or use a magnitude term justified by context.

**Avoid:** Do not infer statistical significance from a visibly larger mean, non-overlapping point estimates, or the Chinese adjective 显著 alone.

**Patterns:**

- {method} yields a {value}-point improvement, but the difference is not statistically significant under {test}.
- The improvement is substantial relative to {reference scale}, with an effect size of {value}.

### respectively requires an unambiguous one-to-one ordering

`general.usage-note.respectively.001` · usage_note · general · method, experiments, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Respectively maps two or more ordered lists element by element and should be used only when both lists have matching cardinality and a clear order.

**Use:** Place 'respectively' close to the second list. If the mapping could be misread, split the sentence or state each pairing explicitly.

**Avoid:** Avoid using 'respectively' when one item maps to several values or when the antecedent order is unclear.

**Patterns:**

- The {first method} and {second method} obtain {first value} and {second value}, respectively.
- We use {value one} for {setting one} and {value two} for {setting two}.

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/routes/index.md) only for a different task.
