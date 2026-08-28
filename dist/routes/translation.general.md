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

## Task protocol

### Super Library protocol: Translation: proposition-first scientific English

`translation` · `section_protocol` · section `translation` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Translate Chinese AI-paper prose by preserving the scientific proposition, terminology, notation, evidence strength, and discourse function before realizing it in field-standard English.

**Use when:** Translating or bilingual-editing AI-paper text, captions, rebuttals, definitions, or technical explanations from Chinese into English.

#### Required inputs

- Source text plus its section, domain, intended readers, and neighboring sentences.
- A terminology lock for method names, benchmark names, symbols, metrics, and repeated concepts.
- The proposition structure: actor, action or relation, object, condition, comparison, evidence, negation, and modality.
- Any primary source that must be checked for a technical definition or literature claim.

#### Functional protocol

##### 1. Recover the scientific proposition (required)

- Identify who or what performs each action and what condition limits the statement.
- Preserve negation, causal direction, quantifiers, uncertainty, comparison direction, and temporal order.
- Resolve omitted Chinese subjects only from context; surface ambiguity instead of guessing.

##### 2. Lock technical terminology (required)

- Retrieve the canonical term by domain without relying on literal dictionary equivalence.
- Use one English form for each concept unless a distinction is intended.
- Preserve symbols, method names, citation keys, metric units, dataset names, and capitalization.

##### 3. Realize the section-specific discourse move (required)

- Choose sentence structure for the section and intent rather than mirroring Chinese word order.
- Use attested collocations only when they match the proposition and rewrite original patterns around the facts.
- Make comparison axes and antecedents explicit where English readers would otherwise misread them.

##### 4. Back-check fidelity (required)

- Compare the translation against the source for omissions, additions, stronger modality, and reversed relations.
- Check all numbers, units, parentheses, citations, equations, and respectively mappings.
- Do not add explanations, praise, novelty, or evidence absent from the source.

#### Choose one internal template

##### Technical proposition

Use when: Translating method, experiment, or analysis prose.

1. Recover proposition and condition.
2. Lock terms and notation.
3. Select section-appropriate subject and verb.
4. Realize modifiers near the quantity or noun they constrain.
5. Back-check evidence strength and factual completeness.

##### Definition or literature claim

Use when: The source defines a concept or characterizes prior work.

1. Identify the exact definitional or literature proposition.
2. Verify the primary source and canonical term.
3. Paraphrase rather than present source-derived wording as a quotation.
4. Preserve citation scope and distinguish synthesis from source claims.

#### Verification

- Back-translation preserves the same technical proposition, negation, comparison, and uncertainty.
- Terminology is consistent with the paper and the target research community.
- Every number, unit, symbol, citation, benchmark, and method name is unchanged unless correction was explicitly requested.
- English syntax is natural for the target section and does not retain avoidable Chinese topic-comment structure.
- No factual content, novelty claim, causal claim, or citation was added.

#### Avoid

- Translating words in source order before identifying the proposition.
- Replacing technical terms with stylistically varied near-synonyms.
- Strengthening may, can, suggests, or is associated with into proves or demonstrates.
- Adding an explanatory clause that is plausible but absent from the source.

#### Retrieve related sentence cards only as needed

- [Although {qualified premise}, {bounded conclusion}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.translation-preserve.001.md) — `general.sentence-pattern.translation-preserve.001`
- [Distinguish possibility, interpretation, empirical evidence, and formal proof.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.modality.001.md) — `general.usage-note.modality.001`
- [respectively requires an unambiguous one-to-one ordering](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.respectively.001.md) — `general.usage-note.respectively.001`
- [statistically significant versus substantial improvement](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.significant.001.md) — `general.usage-note.significant.001`
- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [generalization ability / robustness ability](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.anti-pattern.ability-noun.001.md) — `general.anti-pattern.ability-noun.001`
- [perform good / get better performance](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.anti-pattern.perform-good.001.md) — `general.anti-pattern.perform-good.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.

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
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
