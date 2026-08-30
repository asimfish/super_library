# Super Library one-file route: Paper title and scope statement

`title.general` · domain `general` · section `title` · intent `scope`

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

### {Method} targets {setting the material states}; {one adjacent setting} is outside the scope of this work.

`general.sentence-pattern.positive-scope.001` · sentence_pattern · general · abstract, introduction, method, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States scope by what the work covers, with at most one deliberate exclusion, instead of a chain of defensive disclaimers.

**Use:** Name the covered scope positively from the supplied material. Keep only the exclusions a reader needs to avoid misusing the result; an exclusion is a boundary statement, not an apology.

**Avoid:** Do not stack multiple 'we do not claim' clauses when one positive scope sentence carries the same boundary; do not restate the covered scope as a list of things the work is not.

**Patterns:**

- {Method} addresses {stated problem class}; extending it to {adjacent class} is left to future work.
- Our evaluation covers {stated benchmarks and budget}; deployment-scale settings are outside the scope of this study.

### Across {units the material states}, {method} improves {metric} by {stated amount}.

`general.sentence-pattern.calibrated-strength.001` · sentence_pattern · general · abstract, experiments, conclusion

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Matches verb strength to evidential status: plain declaratives for measured results, hedges only for claims the material marks as unmeasured.

**Use:** When the material states a measured result, report it with a direct verb and its stated scope. Reserve 'may', 'might', and 'potentially' for statements the material itself marks as untested. Never delete a hedge if doing so widens the claim beyond the stated evidence.

**Avoid:** Do not write 'may potentially improve' for a gain the material measures, and do not promote an untested setting to a direct claim by dropping its hedge.

**Patterns:**

- Across {stated number} tasks, {method} improves {metric} from {stated baseline value} to {stated value}.
- On the {stated split}, {method} reduces {failure mode} by {stated amount}; settings beyond this split were not evaluated.

### replace vague effectiveness claims with the observed outcome

`general.usage-note.effectiveness.001` · usage_note · general · abstract, experiments, conclusion, rebuttal, translation

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

An effectiveness claim is informative only when it names the intervention, comparison, metric, and evaluated setting.

**Use:** Write the measured change directly. Use 'supports the effectiveness of' only when several results jointly justify the scoped judgment; use 'proves' only for a formal result.

**Avoid:** Avoid 'the experiments prove the effectiveness and superiority of our method.'

**Patterns:**

- Across {tasks}, {method} improves {metric} over {baselines} under a matched {budget}.
- The ablation supports the contribution of {component} to {measured outcome} in {setting}.

### A dash denotes an unreported value, not a measured zero.

`general.usage-note.missing-zero-na.001` · usage_note · general · experiments

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Separates missing or unreported results from numeric zero and from conditions that are not applicable.

**Use:** Define every symbol in the caption or footnote. Use 0 or 0.0 only for a measured zero and N/A only when the metric or condition does not apply.

**Avoid:** Do not encode unavailable, failed, and zero-valued results with the same blank cell or dash.

**Patterns:**

- A dash denotes a result that was not reported; N/A indicates that the metric is not applicable.
- Zero is reported numerically, while failed runs are counted under {failure policy}.

## Exit check

Audit scientific claims, citations, terminology consistency, source
overlap, unresolved placeholders, and any statement that exceeds the
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
