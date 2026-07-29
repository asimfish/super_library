# Rebuttal workflow

Split the review into atomic concerns and classify each as misunderstanding,
missing evidence, requested comparison, presentation, limitation, or scope.

For each concern:

1. Give the answer in the first sentence: yes, no, a qualification, or the exact
   point of disagreement.
2. Give existing evidence with a real table, figure, section, equation, or result.
3. Explain the implication for the paper's claim.
4. State a concrete revision or a bounded limitation.

Retrieve `section=rebuttal` with one of `respond`, `clarify`, `acknowledge`,
`concede`, `evidence`, or `scope`. Retrieve the technical concept in a second
domain-only pass without `section=rebuttal`.

Constraints:

- Be respectful and direct; do not spend scarce words on ceremonial thanks.
- Acknowledge a valid concern without conceding a stronger claim than necessary.
- Never fabricate a new experiment, number, baseline, or manuscript location.
- If a requested experiment is unavailable, state what current evidence can and
  cannot establish.
- Preserve the reviewer's terminology where it avoids ambiguity.
- Check the final word or character limit exactly.
