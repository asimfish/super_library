## AI writing specification

AI-paper adaptation, not STE compliance. Rules do not supply facts. Hard constraints need semantic review; preferences allow technically justified exceptions. No universal word whitelist or sentence-length ceiling.

- `facts.preserve` [must]: Preserve facts, numbers, notation, negation, uncertainty and citation scope; never fill an unsupported template slot.
  Why: Clearer wording is not permission to strengthen or invent the scientific proposition.
  Check: Manual comparison with the supplied facts; wording lint cannot establish fidelity.
- `terms.consistency` [must]: Use a stable term for each defined concept; retain domain terminology and distinguish related but non-equivalent metrics or components.
  Why: Stylistic synonym variation can silently change the measured quantity or model component. A term may have multiple field senses; define the manuscript's scope rather than imposing one globally.
  Check: Manual terminology and symbol ledger; resolve legitimate aliases explicitly.
- `claims.calibration` [must]: Bind significance, causality, generalization and ranking to their required evidence; hedging does not license an unsupported mechanism.
  Why: A polished sentence can still inflate what the evaluation establishes.
  Check: Manual evidence audit; a lexical warning alone cannot determine claim validity.
  Original conditional example; not evidence or an answer to copy:
  Facts: {method} has a larger reported mean on {metric}; no inferential test was supplied.
  Misuse under those facts: {method} achieves a statistically significant improvement on {metric}.
  Preferred under those facts: {method} has a higher reported mean on {metric}; statistical significance was not assessed.
  Reason: Retains the comparison without inventing statistical evidence. Original placeholders are not measurements.
- `sentences.direct` [prefer]: Give each sentence a clear main claim. Prefer direct verbs; retain passive voice, tense and technical noun phrases when they preserve the intended focus.
  Why: The goal is readable dependency structure, not minimum word count. Formal terms are not automatically wrong.
  Check: Manual reading for subject, predicate and information load; do not auto-rewrite long sentences.
- `sentences.attachment` [must]: Place each condition, unit, denominator and uncertainty next to the quantity or claim it qualifies; make pronouns and list mappings unambiguous.
  Why: Numbers and descriptions can share a sentence when their relation is explicit. Splitting must not detach a qualification.
  Check: Manual quantity-to-condition mapping, including absolute versus relative change.
- `paragraphs.focus` [prefer]: Organize a paragraph around one question or finding. Connect sentences through the same subject or a real comparison, not decorative transitions.
  Why: Short correct sentences still form a laundry list if they do not advance an argument. No fixed sentence count is prescribed.
  Check: Manual identification of the paragraph's point and the contribution of each sentence.
- `rebuttal.answer` [must]: Answer the concern directly; acknowledge only established problems and promise only supplied revisions, supported analyses or authorized commitments.
  Why: A polite response must not invent a manuscript defect, completed experiment or author commitment.
  Check: Manual concern-to-answer and change-to-evidence mapping.
