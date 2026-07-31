# Super Library one-file route: Evidence-bounded reviewer rebuttal

`rebuttal.general` · domain `general` · section `rebuttal` · intent `respond`

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

### Yes. {direct answer}; the supporting evidence is {evidence pointer}.

`general.sentence-pattern.rebuttal-answer.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Answers a reviewer question immediately and then points to evidence.

**Use:** Use when the answer is genuinely yes. Replace the first token with 'No' or a qualified answer when appropriate; never force agreement.

**Avoid:** Do not begin with a long thank-you paragraph that delays the answer.

**Patterns:**

- Yes. {claim bounded to the question}; the supporting evidence is reported in {table, figure, section, or verified result}.

### The requested comparison is already included in {location}, where {verified result}.

`general.sentence-pattern.rebuttal-evidence.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Points a reviewer to existing evidence and summarizes only the relevant result.

**Use:** Give an exact manuscript location and reproduce numbers faithfully. If absent, use a revision or limitation frame instead.

**Avoid:** Do not invent a table location or imply that an indirect analysis answers the request.

**Patterns:**

- The requested comparison is already included in {Table or Appendix}, where {method} achieves {verified metric} under {protocol}.

### We will revise {location} to make {point} explicit.

`general.sentence-pattern.rebuttal-revision.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Commits to a concrete presentation change in response to feedback.

**Use:** Name the section, statement, figure, caption, or experimental detail and the information to add. Do not promise a new result unless it exists.

**Avoid:** Avoid vague promises such as 'we will improve the paper.'

**Patterns:**

- We will revise {Section or caption} to make {assumption, protocol, or limitation} explicit.

### We do not currently have evidence for {broader claim}; we will restrict the manuscript to {supported claim}.

`general.sentence-pattern.rebuttal-no-evidence.001` · sentence_pattern · general · rebuttal

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Responds to a request that cannot be supported with existing results by narrowing the claim instead of inventing evidence.

**Use:** Use when the requested experiment was not run or the available analysis is insufficient. Explain what existing evidence still supports.

**Avoid:** Do not imply that an unrun experiment produced a favorable result or promise a result whose outcome is unknown.

**Patterns:**

- We do not currently have evidence for robustness under {shift}; we will restrict the manuscript to the evaluated {scope}.
- The requested comparison is not available in the current submission, so we will remove the corresponding general claim.

### statistically significant versus substantial improvement

`general.usage-note.significant.001` · usage_note · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Statistical significance refers to an inferential test or interval criterion, whereas substantial, marked, or large describes effect magnitude and requires a stated scale.

**Use:** Translate 显著 according to evidence: use 'statistically significant' only when a specified statistical analysis supports it; otherwise report the effect size or use a magnitude term justified by context.

**Avoid:** Do not infer statistical significance from a visibly larger mean, non-overlapping point estimates, or the Chinese adjective 显著 alone.

**Patterns:**

- {method} yields a {value}-point improvement, but the difference is not statistically significant under {test}.
- The improvement is substantial relative to {reference scale}, with an effect size of {value}.

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/routes/index.md) only for a different task.
