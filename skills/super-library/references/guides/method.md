# Super Library protocol: Method: executable specification and design rationale

`method` · `section_protocol` · section `method` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Describe the problem formulation, components, objective, training procedure, and inference behavior precisely enough that a technically competent reader can reconstruct the method and test each claimed mechanism.

**Use when:** Planning, drafting, or auditing an AI-paper Method section, algorithm description, or implementation-facing formulation.

## Required inputs

- Operational task definition, notation, inputs, outputs, supervision, and assumptions.
- Component graph with tensor or state interfaces and the purpose of each component.
- Objectives with signs, weights, estimators, gradient boundaries, and optimization schedule.
- Training-data flow and deployment-time procedure, including what information is available at each stage.
- Claim-to-mechanism map and material compute, latency, memory, or sampling requirements.

## Functional protocol

### 1. Define the problem and information boundary (required)

- Define every symbol before or at first use and state tensor, sequence, or state semantics when ambiguity matters.
- Separate training-only supervision or privileged information from inference-time inputs.
- State assumptions and non-goals that limit what the formulation represents.

### 2. Specify components through interfaces (required)

- For each component, state its input, output, transformation, and downstream consumer.
- Explain why the component addresses a named failure mode or claim rather than only naming its architecture.
- Keep notation and component names identical across text, equations, figures, pseudocode, and appendices.

### 3. Make the learning objective auditable (required)

- Define each loss or reward term, coefficient, estimator, normalization, mask, and reduction.
- State where gradients flow or stop and which parameters each term updates.
- Distinguish the optimized surrogate from the scientific quantity it is intended to improve.

### 4. Separate training and inference procedures (required)

- Give an ordered training procedure with data sampling, update ratios, target updates, and selection protocol where relevant.
- Give an ordered inference or control procedure with state, decoding, replanning, stopping, and timing boundaries.
- Surface stochastic choices, seeds, search budgets, or external modules that affect reproducibility.

## Choose one internal template

### Model–objective–procedure

Use when: A learned architecture is the main contribution.

1. Problem formulation and notation.
2. System overview and component interfaces.
3. Representation or prediction modules.
4. Training objectives and optimization.
5. Inference or control procedure.
6. Complexity, assumptions, and implementation-critical details.

### Algorithmic procedure

Use when: The contribution is primarily an update rule, planner, optimizer, or decision procedure.

1. Formal setting and objective.
2. Core update or search rule.
3. Estimator, approximation, and stopping conditions.
4. Pseudocode with all externally chosen quantities defined.
5. Computational requirements and applicable guarantees.

## Verification

- A reader can trace every input to every output without guessing an unstated module or data source.
- Equations, pseudocode, diagrams, and prose use consistent notation and ordering.
- Train-time and test-time information, computation, and model variants are explicitly separated.
- Every mechanism claim has a corresponding experiment, theorem, diagnostic, or explicitly limited interpretation.
- Implementation details that materially affect the comparison are in the main text or clearly routed appendix.

## Avoid

- Using intuitive prose in place of an operational definition.
- Introducing modules as a list without interfaces or design rationale.
- Hiding optimization, selection, or inference details behind 'we follow standard practice'.
- Claiming a component causes an improvement when the design only establishes correlation.

## Retrieve related sentence cards only as needed

- [We use {term} to denote {operational meaning}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.define.001.md) — `general.sentence-pattern.define.001`
- [The design addresses {challenge} by {technical choice}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.intro-challenge-design.001.md) — `general.sentence-pattern.intro-challenge-design.001`
- [Unless otherwise specified, we use {default configuration} in all experiments.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.reproducibility-default.001.md) — `general.sentence-pattern.reproducibility-default.001`
- [This distinction matters because {consequence}.](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.sentence-pattern.transition.001.md) — `general.sentence-pattern.transition.001`
- [respectively requires an unambiguous one-to-one ordering](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/cards/general/general.usage-note.respectively.001.md) — `general.usage-note.respectively.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
