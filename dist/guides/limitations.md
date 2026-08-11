# Super Library protocol: Limitations: evidence boundary and consequential failure modes

`limitations` · `section_protocol` · section `limitations` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

State where the evidence, assumptions, resources, and deployment conditions stop supporting the paper's claims, and identify concrete failure modes without generic disclaimers.

**Use when:** Drafting a Limitations section, failure-boundary discussion, broader-impact caveat, or scoped response to an untested setting.

## Required inputs

- The paper's claims and the exact evidence supporting each claim.
- Untested datasets, tasks, shifts, embodiments, populations, or deployment conditions that a reader might otherwise infer.
- Observed failures, null results, sensitivity, safety concerns, and resource requirements.
- Assumptions in the formulation, data, annotations, simulator, metrics, or evaluation protocol.

## Functional protocol

### 1. Bound each claim (required)

- Name the evaluated axis and the nearest unsupported extrapolation.
- Distinguish not evaluated, evaluated with a null result, and observed failure.
- Use calibrated modality so uncertainty is not converted into a negative result.

### 2. Describe mechanism and consequence (required)

- State the condition under which the failure occurs and the observable consequence.
- Connect the boundary to a data, model, objective, protocol, or deployment mechanism when evidence permits.
- Identify who or what is affected when the limitation has safety, fairness, or operational consequences.

### 3. Separate current mitigation from future work (required)

- Describe existing safeguards or diagnostics as implemented facts.
- Label proposed mitigations as future work and do not imply they are validated.
- Prioritize limitations that materially change interpretation over generic statements that all methods could make.

## Choose one internal template

### Empirical boundary

Use when: The main limitation is incomplete evaluation or a measured failure region.

1. Supported claim and evaluated scope.
2. Nearest untested or failed condition.
3. Observed evidence or reason for uncertainty.
4. Effect on interpretation or deployment.
5. Current mitigation and clearly labeled future validation.

### Assumption or resource boundary

Use when: Performance relies on information, data, compute, hardware, or a formal assumption.

1. Required assumption or resource.
2. Where it enters the method or evaluation.
3. What changes when it is violated or unavailable.
4. Scope of claims that remain valid.

## Verification

- Every limitation is specific enough to suggest a test, affected claim, or deployment decision.
- Observed failures, null results, and untested settings are linguistically distinct.
- The section does not introduce evidence or causal explanations absent from the paper.
- Resource and data limitations include units, scale, provenance, or access conditions where relevant.
- Safety-relevant limitations are not hidden behind vague future-work language.

## Avoid

- Generic statements that more data, compute, or future research may help.
- Presenting a missing experiment as evidence of likely success or failure.
- Minimizing a consequential failure because it occurs outside the average benchmark case.
- Adding a limitation that contradicts the paper's main claim without reconciling the scope.

## Retrieve related sentence cards only as needed

- [Our evaluation is limited to {scope}; performance under {unseen condition} remains to be established.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.limitation.001.md) — `general.sentence-pattern.limitation.001`
- [Performance degrades under {condition}, which limits the claim to {scope}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.result-boundary.001.md) — `general.sentence-pattern.result-boundary.001`
- [We observe no consistent advantage on {scope}; the difference remains within {uncertainty}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.result-null.001.md) — `general.sentence-pattern.result-null.001`
- [This gain comes with {cost}, revealing a trade-off between {axes}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.result-tradeoff.001.md) — `general.sentence-pattern.result-tradeoff.001`
- [An important next step is to evaluate {capability} under {condition}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.future.001.md) — `general.sentence-pattern.future.001`
- [name the generalization axis and held-out unit](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.generalization-axis.001.md) — `general.usage-note.generalization-axis.001`
- [Distinguish possibility, interpretation, empirical evidence, and formal proof.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.modality.001.md) — `general.usage-note.modality.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
