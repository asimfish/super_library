# Super Library one-file route: Grounded peer-review assessment

`review.general` · domain `general` · section `review` · intent `evidence`

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

### Super Library protocol: Peer review: grounded assessment with actionable requests

`review` · `section_protocol` · section `review` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Assess a submission by anchoring every judgment in its reported content, separating evidential statuses, making each weakness actionable, and calibrating the overall assessment to the listed evidence.

**Use when:** Writing reviewer comments, a weaknesses section, clarifying questions, an overall assessment, or a post-rebuttal update for a paper submission.

#### Required inputs

- The submission content available to the reviewer: claims, methods, reported results, disclosed limitations.
- The venue's requested review structure and any scoring or formatting rules.
- For post-rebuttal updates, the original concerns and the author response point by point.

#### Functional protocol

##### 1. Ground every statement in the submission (required)

- Anchor each strength, weakness, and question to a specific claim, section, table, or omission.
- Classify each criticism as absent, contradicted, or unverifiable before phrasing it.
- Never assert unverifiable properties or misconduct; describe the claim-evidence gap instead.

##### 2. Separate summary, strengths, weaknesses, and questions (required)

- Summarize the contribution neutrally before evaluating it.
- Keep disclosed limitations credited to the authors and probe their boundary instead of rediscovering them.
- Keep each weakness distinct; do not bundle unrelated concerns.

##### 3. Make weaknesses actionable (required)

- Pair each substantive weakness with a concrete, answerable request or question.
- When more than one remedy would resolve the concern, enumerate the acceptable options explicitly as a short numbered or (i)/(ii) list so the authors can satisfy any one of them; do not bury alternatives in a run-on sentence.
- Request only what the authors can deliver within the venue's process.
- Keep requests inside the review's scope; do not escalate to demands the concern does not justify.

##### 4. Present the comment for the author's working eye (required)

- Open the comment by naming the specific concern in one sentence; do not open with background or a restatement of the paper's numbers.
- State each fact or number from the submission exactly once; a repeated fact reads as filler in a review.
- When a criticism could be read more broadly than intended, close by scoping it explicitly: name what is not being claimed or demanded.

##### 5. Calibrate the overall assessment (required)

- Trace the overall judgment to the listed strengths and weaknesses and nothing else.
- Match hedging to evidence; avoid verdict language the review body does not support.
- After a rebuttal, concede addressed points explicitly and keep unresolved ones with reasons.

#### Choose one internal template

##### Grounded weaknesses section

Use when: Writing the weaknesses portion of a review.

1. Specific claim or reporting gap with its location.
2. Evidential status: absent, contradicted, or unverifiable.
3. Why it matters for the paper's main claim.
4. Concrete, answerable request.

##### Post-rebuttal update

Use when: Updating the assessment after the author response.

1. Concern-by-concern mapping to the response.
2. Explicit concession of addressed points.
3. Remaining concerns with stated reasons.
4. Updated overall assessment traceable to the above.

#### Verification

- Every criticism names its anchor in the submission and its evidential status.
- No unverifiable property or misconduct implication is asserted as fact.
- Disclosed limitations are credited, not rediscovered.
- Each substantive weakness carries an answerable request.
- Alternative acceptable remedies appear as an explicit enumerated list rather than buried in prose.
- No fact or number from the submission is restated more than once.
- The overall assessment introduces no claim absent from the review body.

#### Avoid

- Asserting non-reproducibility, hidden results, or misconduct without packet evidence.
- Presenting a disclosed limitation as an undisclosed flaw.
- Rhetorical or hostile questions in place of answerable requests.
- Repeating the same submission fact or number in consecutive sentences.
- A single dense paragraph that mixes the concern, its consequences, and several remedies without visible structure.
- Dismissing an evidence base wholesale when it validly supports a narrower claim.
- Verdicts or scores that exceed the venue's requested format or the listed evidence.

#### Retrieve related sentence cards only as needed

- [The {claim} rests on {reported evidence}, which supports {narrower statement} but not {claimed scope}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.review-grounded-weakness.001.md) — `general.sentence-pattern.review-grounded-weakness.001`
- [Could the authors report {specific quantity or protocol detail}? This would clarify {stated concern}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.review-actionable-question.001.md) — `general.sentence-pattern.review-actionable-question.001`
- [Given {listed strengths} and {unresolved weaknesses}, the current evidence supports {bounded judgment}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.review-calibrated-assessment.001.md) — `general.sentence-pattern.review-calibrated-assessment.001`
- [The authors already acknowledge {limitation} in {location}; the open question is {boundary probe}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.review-credit-disclosure.001.md) — `general.sentence-pattern.review-credit-disclosure.001`
- [The added {evidence} addresses {original concern}; {remaining concern} stands because {reason}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.review-post-rebuttal.001.md) — `general.sentence-pattern.review-post-rebuttal.001`
- [absent from the manuscript versus contradicted by the manuscript versus unverifiable from the manuscript](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.review-evidence-scope.001.md) — `general.usage-note.review-evidence-scope.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.

## Selected language records

### The {claim} rests on {reported evidence}, which supports {narrower statement} but not {claimed scope}.

`general.sentence-pattern.review-grounded-weakness.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

States a review weakness by anchoring it to what the submission actually reports, separating the claim from the evidence behind it.

**Use:** Quote or locate the specific claim and the specific evidence before judging the gap. Keep the weakness about the submission's content, not about unverifiable properties.

**Avoid:** Do not assert properties the review packet cannot verify, such as reproducibility or hidden results, and do not restate a disagreement as a factual error.

**Patterns:**

- The generalization claim rests on results from {evaluated conditions}, which support robustness within that range but not the broader statement in the abstract.
- The comparison covers {included baselines}, which establishes progress over those methods but not the field-wide claim.

### Could the authors report {specific quantity or protocol detail}? This would clarify {stated concern}.

`general.sentence-pattern.review-actionable-question.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Asks the authors for one concrete, answerable item and states what the answer would resolve.

**Use:** Target quantities recoverable from a standard experimental log or manuscript revision. One question per missing item, phrased neutrally.

**Avoid:** Avoid rhetorical or accusatory questions and compound questions that bundle several requests into one.

**Patterns:**

- Could the authors report the number of random seeds and the dispersion statistic used in Table {n}? This would clarify how stable the reported gains are.
- Could the authors state the training budget per method? This would clarify whether the comparison is matched.

### Given {listed strengths} and {unresolved weaknesses}, the current evidence supports {bounded judgment}.

`general.sentence-pattern.review-calibrated-assessment.001` · sentence_pattern · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Closes a review with an overall judgment that traces explicitly to the listed strengths and weaknesses and no further.

**Use:** Weigh only items already established in the review body. Match the hedging strength to the evidence: firm where results are clear, open where reporting is incomplete.

**Avoid:** Do not introduce comparisons, claims, or scores absent from the review body, and do not let polish or novelty language substitute for the listed evidence.

**Patterns:**

- Given the clear formulation and strong results on {covered settings}, balanced against the missing {analysis}, the current evidence supports a cautiously positive assessment.
- The contribution is well motivated, but until {unresolved item} is addressed the empirical claim remains partially supported.

### absent from the manuscript versus contradicted by the manuscript versus unverifiable from the manuscript

`general.usage-note.review-evidence-scope.001` · usage_note · general · review

**Provenance:** `original_pattern` · **Quality:** `gold+reviewed`

Reviewer statements about a submission carry three distinct evidential statuses: the manuscript omits something, the manuscript contradicts something, or the review packet cannot establish something either way.

**Use:** Choose the status explicitly before writing the criticism: request what is absent, correct what is contradicted, and mark what is unverifiable as outside the review's evidence rather than asserting it.

**Avoid:** Do not convert an omission into an accusation, and do not state unverifiable properties, such as reproducibility or hidden failures, as established facts.

**Patterns:**

- No episode counts are reported (absent), so we request them; we cannot judge reproducibility from the packet (unverifiable), so we do not assert it.
- The abstract claims real-world generalization while all experiments are simulated (contradicted), which is a claim-evidence mismatch rather than misconduct.

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
