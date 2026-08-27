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

## Task protocol

### Super Library protocol: Rebuttal: answer–evidence–revision with fixed evidence

`rebuttal` · `section_protocol` · section `rebuttal` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Respond directly to reviewer concerns using existing evidence, precise scope, and concrete manuscript changes while distinguishing correction, clarification, concession, and new work.

**Use when:** Drafting a conference rebuttal, response-to-reviewers document, or concise answer to a technical concern.

#### Required inputs

- The reviewer's concern decomposed into factual questions or requested actions.
- Existing manuscript evidence, table or figure locations, analyses, and exact results available before the response deadline.
- The valid scope of the current claim and any aspect that should be conceded.
- Specific text, figure, table, appendix, or experiment changes that are actually authorized and feasible.

#### Functional protocol

##### 1. Classify the concern (required)

- Separate misunderstanding, missing explanation, valid limitation, factual error, and request for new evidence.
- Answer each atomic concern once and preserve the reviewer's strongest interpretation.
- Do not frame disagreement as reviewer confusion when the manuscript was ambiguous.

##### 2. Lead with the answer (required)

- Begin with yes, no, agreement, correction, or a one-sentence scoped answer; one opening clause that names the reviewer's concern, with or without brief thanks, is acceptable only when the same or the next sentence delivers that answer.
- State the claim boundary before explanatory background when scope is disputed.
- Acknowledge a valid concern without conceding unrelated claims.

##### 3. Point to existing evidence (required)

- Give the exact table, figure, equation, appendix, or result and state what it supports.
- Report metric, denominator, comparison, runs, and uncertainty when the response relies on a number.
- If evidence is absent, say so and narrow the claim instead of inventing a result.

##### 4. Commit to a concrete revision (required)

- Describe the exact manuscript change and where it will appear.
- Distinguish completed analysis from a promised revision or future experiment.
- Ensure the revision resolves the stated concern rather than only adding volume.

##### 5. Shape the response as an answer-then-limits arc (required)

- When both the supporting evidence and its limits are substantive, give the direct answer with its evidence in one paragraph and the evidence boundary with the committed revision in a following paragraph.
- State each supplied fact or number exactly once; do not restate a result as a transition between points.
- Prefer plain verb phrases over stacked nominalizations so the response reads as an author addressing a colleague.

#### Choose one internal template

##### Clarification with existing evidence

Use when: The concern is addressed by evidence already in the submission but presentation is unclear.

1. Direct scoped answer.
2. Exact existing evidence and what it establishes.
3. Source of ambiguity in the current manuscript.
4. Concrete clarification and location.

##### Valid limitation or missing evidence

Use when: The reviewer identifies an unsupported scope, untested condition, or real weakness.

1. Explicit agreement on the valid concern.
2. What the current evidence does and does not establish.
3. Narrowed claim or limitation statement.
4. Feasible revision, with new experiments labeled only if actually run.

#### Verification

- The scoped answer arrives within the first two sentences; any opening acknowledgment names the concern and never substitutes for the answer.
- Answer-plus-evidence and limits-plus-revision occupy separate paragraphs when each is substantive.
- No supplied fact or number is restated more than once.
- Every numeric or comparative statement matches the submission or a clearly identified completed addition.
- Promises correspond to concrete edits that can be delivered under the venue rules.
- Tone is factual and respectful without exaggerating agreement or certainty.
- No citation, experiment, result, or venue policy is invented.

#### Avoid

- Thanking the reviewer without answering the question.
- Compressing answer, evidence, limits, and revision into one unbroken paragraph.
- Restating the same number or claim in successive sentences as connective filler.
- Claiming that the reviewer misunderstood when the manuscript omitted the needed distinction.
- Promising broad experiments without completed results, resources, or permission.
- Using significance, fairness, or state-of-the-art language without the required evidence.

#### Retrieve related sentence cards only as needed

- [Yes. {direct answer}; the supporting evidence is {evidence pointer}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-answer.001.md) — `general.sentence-pattern.rebuttal-answer.001`
- [We agree that {concern} is important; our current evidence addresses {covered scope}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-acknowledge.001.md) — `general.sentence-pattern.rebuttal-acknowledge.001`
- [The requested comparison is already included in {location}, where {verified result}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-evidence.001.md) — `general.sentence-pattern.rebuttal-evidence.001`
- [We do not currently have evidence for {broader claim}; we will restrict the manuscript to {supported claim}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-no-evidence.001.md) — `general.sentence-pattern.rebuttal-no-evidence.001`
- [We will revise {location} to make {point} explicit.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-revision.001.md) — `general.sentence-pattern.rebuttal-revision.001`
- [This is a limitation of the current study, but it does not affect {narrower conclusion}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.rebuttal-concede.001.md) — `general.sentence-pattern.rebuttal-concede.001`
- [For a controlled comparison, we hold {factor} fixed and vary only {factor}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.fair-comparison.001.md) — `general.sentence-pattern.fair-comparison.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.

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
verified evidence. Return to the [route index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/routes/index.md) only for a different task.
