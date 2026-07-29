# Writing workflows

## Paper or related work

1. Extract propositions, entities, comparison axes, and uncertainty from the notes.
2. Retrieve rhetorical moves by section and intent, then retrieve technical terms
   and definitions by domain without a section filter.
3. Use definitions as semantic atoms; synthesize a new sentence for the local
   argument.
4. Verify every literature relationship in the linked primary papers.
5. Audit claim scope, comparison scope, terminology consistency, and transitions.

With a checkout, `superlib.py bundle` performs both retrieval passes and enforces
a context-character budget. With link-only access, use `agent-index.md`, the
universal core, the `related_work` section catalog, one domain catalog, and only
the selected cards.

## Rebuttal

1. Split each review into answerable concerns.
2. Classify each as misunderstanding, missing evidence, limitation, presentation,
   or requested experiment.
3. Retrieve `section=rebuttal` entries with `respond`, `clarify`, `acknowledge`,
   or `scope`, then run a separate domain-only query for the technical concept.
4. Lead with the direct answer, then evidence, then the concrete manuscript change.
5. Do not claim a new experiment was run unless results are available.

## Chinese-to-English technical translation

1. Recover the scientific proposition rather than Chinese word order.
2. Lock terminology with `kind=term` records.
3. Retrieve patterns for the target section and intent.
4. Reconstruct concise English, preserving modality (`may`, `can`, `is`) and
   comparison scope.
5. Back-translate the proposition mentally and audit for inflated claims.
