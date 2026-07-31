# Super Library protocol: Introduction: limitation–insight–evidence alignment

`introduction` · `section_protocol` · section `introduction` · [protocol index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/guides/index.md)

Load this protocol only for the matching task. It constrains structure and
evidence reporting; it does not supply scientific facts or results.

Build an argument that moves from a scoped problem to a verified gap, design insight, contribution, and evidence without relying on a fixed paragraph count.

**Use when:** Planning, drafting, or restructuring an AI-paper Introduction.

## Required inputs

- Paper type: method, new problem or setting, resource, empirical study, or theory.
- Task definition, relevant application stakes, and intended reader prerequisites.
- Closest approach families and the verified axes on which they differ.
- The exact limitation addressed, including its assumptions and practical consequence.
- Core insight, design elements, contribution claims, and the experiment or theorem supporting each claim.

## Functional protocol

### 1. Establish scope and problem (required)

- Define the operational task before expanding to broader motivation.
- Use a concrete running scenario only when it is real and technically representative.
- Avoid claiming that all prior work shares one weakness.

### 2. Map closest approaches (required)

- Group work by representation, supervision, data, decision mechanism, interaction regime, or deployment assumption.
- Use only verified literature relationships and reserve detailed chronology for Related Work.
- Make the comparison axis explicit before stating the limitation.

### 3. State gap and consequence (required)

- Name the condition under which the limitation matters.
- Separate lack of evaluation from evidence of failure.
- Do not turn a design difference into a defect without evidence.

### 4. Bridge insight to design (required)

- State the key insight before the component list.
- Map each emphasized challenge to a design choice.
- Explain the causal claim only as strongly as the design and analysis allow.

### 5. Pair contributions with evidence (required)

- Write parallel contributions at the same abstraction level.
- Pair each empirical contribution with a named evaluation question or display.
- Replace 'extensive experiments' with the evaluated axes and principal finding.

### 6. Close with scope (conditional)

- State assumptions or non-goals that prevent an overbroad reading.
- Keep the boundary consistent with the Limitations and Experiments sections.

## Choose one internal template

### Technique paper

Use when: A new method addresses a known task.

1. Operational task and stakes.
2. Closest method families and relevant comparison axes.
3. Limitation under a named condition.
4. Key insight and method overview.
5. Contribution–evidence pairs.
6. Supported scope or non-goal.

### New setting or resource

Use when: The paper primarily introduces a task, dataset, benchmark, or problem formulation.

1. Missing capability or evaluation need.
2. Why existing settings fail to measure it.
3. Definition and design principles of the new setting.
4. Coverage, validity, and diagnostic axes.
5. Baseline findings and remaining gap.
6. Availability and boundary.

### Theory or analysis paper

Use when: The main contribution is explanatory or formal rather than architectural.

1. Formal problem and why it matters.
2. Known results and the unresolved regime.
3. Main insight or analytical device.
4. Principal result and assumptions.
5. Consequences and evidence.
6. Limits of the analysis.

## Verification

- Construct a matrix from limitation to challenge, design choice, contribution, and supporting experiment or theorem.
- Check every literature statement against primary papers rather than the library or another paper's Related Work.
- Ensure contribution wording matches the Abstract and does not exceed the evidence summarized later.
- Read the Introduction once without citations: the logical bridge should remain clear.

## Avoid

- A universal six-paragraph requirement; use functional moves and merge them when the argument benefits.
- A straw-man progression from a deliberately weak 'naive' solution to the proposed method.
- Chronological paper listing, unverified 'first' claims, and generic importance claims.
- Contribution bullets that mix a task definition, one module, and a result at incompatible levels.

## Retrieve related sentence cards only as needed

- [A central challenge is to {objective} while {constraint}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.motivate.001.md) — `general.sentence-pattern.motivate.001`
- [Despite progress in {area}, existing methods remain limited by {specific limitation}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.gap.001.md) — `general.sentence-pattern.gap.001`
- [Our main contribution is {artifact or insight} that {verified capability}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.contribution.001.md) — `general.sentence-pattern.contribution.001`
- [Under {evaluated setting}, {method} consistently {measured outcome}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.scope.001.md) — `general.sentence-pattern.scope.001`
- [A complementary line of work studies {adjacent problem}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.related-family.001.md) — `general.sentence-pattern.related-family.001`
- [These approaches share {common objective}, but differ in {technical axes}.](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/cards/general/general.sentence-pattern.related-synthesis.001.md) — `general.sentence-pattern.related-synthesis.001`

Calibration and external-skill research are documented in the
[writing-guide research note](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/docs/WRITING_GUIDE_RESEARCH.md); extracted paper prose is
not stored.
