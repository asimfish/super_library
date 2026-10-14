# ADR-009: Separate source facts from language-effect validation

## Status and scope

Accepted for a maintainer-operated diagnostic workflow, 2026-10-14.
Library candidate: `6825f0b1320dcf38f4ce351dd34c4b514628cef0`.
This is not an automatic paper-ingestion service, a new default Agent prompt,
a private-manuscript upload capability or a formal effectiveness release.

The prior synthetic pilot did not establish a consistent library advantage.
Real published tables add protocol and numerical complexity, but public-table
transfer still cannot establish benefit on an author's own manuscript.

## Requirements and alternatives

Separate two questions: whether an extracted task correctly represents its
primary source, and whether a writing treatment improves the resulting prose.
Do not let an author's published analysis become a preferred answer, conceal
adverse output, or alter a frozen language candidate after inspecting holdouts.
Keep bulky validation records out of ordinary retrieval.

A: Give both writers the complete published paper. This is realistic for some
workflows, but author prose and source navigation confound table-to-argument
transfer. It also increases context cost and potential quotation overlap.

B: Extract selected cells and independently synthesize a condition-neutral fact
packet; verify against published tables, then freeze identical bytes for both
writers. Maintain source URLs, PDF hashes and exact locators separately.

Choose B for this diagnostic. It tests a defined subset of writing behavior,
not full-paper reading. Source-paper measurement validity remains unaudited.

## Owners and interfaces

- Primary papers own scientific evidence. A maintainer and one fresh verifier
  check selected cells, metric meanings, units, denominators and protocols.
- The frozen task packet owns this task's propositions and missing-information
  boundary. It specifies whether tables/setup remain or the text is standalone.
- Canonical entries and one selected protocol own language context; the opt-in
  drafting projection remains unchanged. Facts do not come from sentence cards.
- Fresh writers each own one generation condition and an unedited output file.
- A condition mapping is held separately while fresh raters see only anonymous
  texts, common facts and the existing anchored rubric. Reveal after both rate.
- A maintainer records numerical checks and sentence functions separately from
  subjective preferences. A statistical or scope error cannot be averaged away.

Source verification is manual/Agent-assisted, not a runtime guarantee. Instruction
isolation is not filesystem sandboxing. Hashes bind inspected files; they do not
prove correct measurement, blind behavior or model reproducibility.

The evidence record in `library/studies/public_table_transfer_2026-10.json`
preserves task bytes, source audit, all responses, anonymous pairs, raw ratings,
revealed assignments and arithmetic. Tests audit identity/coverage/arithmetic;
they do not require a favorable score or classify prose automatically. The record
is not an entry, source record, guide or default generated context resource.
Published PDFs and original author paragraphs are not distributed in the repo.

The primary random seed produced all drafting-A pairs. A separate, explicitly
post-hoc position-sensitivity stage therefore uses two complementary balanced
layouts and fresh raters, without regenerating prose or replacing primary scores.
Future primary evaluations must predeclare counterbalanced layouts rather than
rely on an unconstrained four-pair random placement. Neither this sensitivity
check nor primary ratings are a causal estimate of position or library effects.

## Acceptance and reconsideration

Before generation: source-check all selected cells and freeze the common packet,
library commit, blinding seed, task selection and scoring criteria. No manual
rewrite, selective regeneration, case deletion or rubric relaxation after output.

After generation: preserve ties, disagreements, critical-error flags and audit
limitations. Check context volume independently of quality. Fewer numbers,
perfect lint or elegant architecture are not quality targets or efficacy proof.

Unexposed model revisions/sampling controls, same-family LLM judges and selected
public tasks prohibit formal-effectiveness, human-review or generalization claims.
An author-owned table/original paragraph and human or cross-model assessment
remain a separate next stage. Private manuscript material must stay outside the
public repository and requires an explicit external-transmission scope.
