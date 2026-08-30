# Super Library protocol: Conclusion: contribution–evidence–scope closure

`conclusion` · `section_protocol` · section `conclusion` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results. Every
move binds only to material the task supplies: when a move's material is
absent, satisfy the move by omission or by stating the absence, and never
invent facts, defects, numbers, or commitments to complete a move.

Close the paper by restating the solved problem, core contribution, principal verified evidence, and remaining boundary without adding new claims or repeating the abstract verbatim.

**Use when:** Drafting or revising the final paper section after claims, results, and limitations are stable.

## Required inputs

- Final problem statement and contribution claims.
- Principal verified result or theoretical implication with its evaluation scope.
- The most consequential limitation or next research question.
- Any broader implication that follows directly from the paper rather than from aspiration.

## Functional protocol

### 1. Synthesize problem and contribution (required)

- Restate the addressed problem at the same scope as the Introduction.
- Name the core insight and contribution rather than listing every module.
- Avoid copying the Abstract sentence by sentence.

### 2. Close the claim with evidence (required)

- State the principal verified finding and the setting in which it holds.
- Retain exceptions, trade-offs, or uncertainty that materially affect the conclusion.
- Do not upgrade a trend or benchmark result into a causal or universal claim.

### 3. End with a bounded implication (required)

- Identify a specific remaining boundary or research direction grounded in the findings.
- State untested settings as untested: never assert that performance degrades, transfers, or persists in any setting the supplied evidence did not evaluate.
- Separate demonstrated capability from plausible broader impact.
- Introduce no new method detail, citation-dependent literature claim, or result.

### 4. Anti-defensive final pass (required)

- Polish tone only, never content: every task, setting, protocol, mechanism, and comparison named in the final pass must already appear in the supplied material in those terms; if a claim-forward rewrite would add, upgrade, or rename one, keep the original wording instead.
- Open with the contribution the supplied results support, never with a disclaimer, apology, or list of things the work does not do.
- State scope positively: name what the work covers, keep at most the exclusions a reader needs, and fold stacked 'we do not claim' disclaimers into one boundary sentence.
- Use plain declaratives for measured results and reserve 'may', 'might', or 'potentially' for claims the material marks as untested; never remove a hedge if doing so widens a claim beyond the supplied evidence.
- Keep every evidential qualifier such as the sample size, split, or evaluated setting: those bind the claim to its evidence and are not defensive tone.

## Choose one internal template

### Empirical paper closure

Use when: The main contribution is an empirically evaluated method or system.

1. Problem and core design insight.
2. Contribution at system or algorithm level.
3. Principal evidence with evaluation scope.
4. Trade-off or limitation that affects interpretation.
5. Specific next question or bounded implication.

### Theory or resource closure

Use when: The main contribution is a theorem, benchmark, dataset, or analysis.

1. Formal or measurement gap addressed.
2. Main result or resource contribution.
3. What the result enables or reveals under stated assumptions.
4. Boundary of validity or coverage.
5. Concrete follow-up enabled by the contribution.

## Verification

- Every conclusion claim appears earlier with supporting evidence or analysis.
- Numbers, comparisons, and scope match the final Results and Limitations sections.
- No state-of-the-art, generalization, deployment, or causal claim is strengthened during summarization.
- The final sentence communicates a specific implication or boundary rather than generic future work.

## Avoid

- Repeating the Abstract nearly verbatim.
- Introducing a new experiment, citation, comparison, or technical mechanism.
- Ending with an unbounded claim that the method opens broad new possibilities.
- Omitting a trade-off that is necessary to interpret the main result.
- Hedging a measured result with 'may', 'might', or 'potentially', or spending the opening on disclaimers instead of the supported contribution.

## Retrieve related sentence cards only as needed

- [Our main contribution is {artifact or insight} that {verified capability}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.contribution.001.md) — `general.sentence-pattern.contribution.001`
- [Across {evaluation scope}, {method} changes {metric} by {value} relative to {comparator}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.abstract-result.001.md) — `general.sentence-pattern.abstract-result.001`
- [Under {evaluated setting}, {method} consistently {measured outcome}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.scope.001.md) — `general.sentence-pattern.scope.001`
- [Performance degrades under {condition}, which limits the claim to {scope}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.result-boundary.001.md) — `general.sentence-pattern.result-boundary.001`
- [This gain comes with {cost}, revealing a trade-off between {axes}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.result-tradeoff.001.md) — `general.sentence-pattern.result-tradeoff.001`
- [An important next step is to evaluate {capability} under {condition}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.future.001.md) — `general.sentence-pattern.future.001`
- [We present {method}, which {capability the supplied results state} on {evaluated setting}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.claim-forward-opening.001.md) — `general.sentence-pattern.claim-forward-opening.001`
- [{Method} targets {setting the material states}; {one adjacent setting} is outside the scope of this work.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.positive-scope.001.md) — `general.sentence-pattern.positive-scope.001`
- [Across {units the material states}, {method} improves {metric} by {stated amount}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.calibrated-strength.001.md) — `general.sentence-pattern.calibrated-strength.001`
- [defensive hedging versus calibrated claiming](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.anti-defensive-tone.001.md) — `general.usage-note.anti-defensive-tone.001`
- [{Method} assumes {stated condition}; the supplied evidence does not evaluate {setting beyond that condition}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.limitation-boundary.001.md) — `general.sentence-pattern.limitation-boundary.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
