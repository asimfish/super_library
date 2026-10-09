# Writing-guide research

The section protocols are an original synthesis. They were calibrated against
current official venue guidance, a local structural study of recent primary
papers, and several open-source research-writing skills. No third-party template
text is copied into the corpus.

## Official constraints

- [NeurIPS Paper Checklist](https://neurips.cc/public/guides/PaperChecklist):
  abstract and Introduction claims should match contributions, assumptions,
  limitations, and the generalization scope supported by results.
- [ICML 2026 Author Instructions](https://icml.cc/Conferences/2026/AuthorInstructions):
  material critical to evaluation belongs in the main paper because reviewers
  may choose not to consult supplementary material; reproducibility and code
  availability matter; accessibility is encouraged.
- [ICLR 2026 Author Guide](https://iclr.cc/Conferences/2026/AuthorGuide):
  the optional reproducibility statement should point to the paper, appendix,
  and supplemental locations that contain the actual reproduction details.
- [CVPR 2026 Author Guidelines](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines):
  compute reporting, formatting, self-contained submission, and policy remain
  external, versioned constraints and are not frozen into generic prose
  templates.

These rules are represented as verification boundaries rather than universal
venue style stereotypes.

## Open-source skills reviewed

- [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-writing):
  evidence IDs, consistency manifests, fail-closed placeholders, reconciliation
  of Methods/Results, and provenance-bound accessible tables.
- [sciwrite](https://github.com/labarba/sciwrite):
  separate revision passes for clutter, verbs, sentence architecture, keyword
  consistency, and numeric/citation consistency.
- [Paper-Polish-Workflow-skill](https://github.com/Lylll9436/Paper-Polish-Workflow-skill):
  extract measurable findings before prose and separate evidence statements from
  interpretation.
- [EvoSkills paper-writing](https://github.com/EvoScientist/EvoSkills/tree/main/skills/paper-writing):
  section-specific references, multiple Abstract and Introduction variants, and
  claim-to-experiment planning.
- [Supervisor-Skills intro-drafter](https://github.com/HKUSTDial/Supervisor-Skills/tree/main/skills/intro-drafter):
  align limitations, challenges, design elements, and contributions while keeping
  the scaffold internal.
- [AER-Skills](https://github.com/brycewang-stanford/AER-Skills):
  demonstrates why venue-specific paragraph counts and abstract lengths must stay
  conditional rather than become global rules.

Adopted ideas were rewritten as controlled functional moves. The project rejects
mandatory colored best/second-best cells, a universal paragraph count, forced
observation lists, and one venue's word limit as global defaults.

## Primary-paper section study

`library/studies/section_writing_2026-08.json` records an 80-paper full-text
calibration sample: twenty papers each for reinforcement learning, embodied AI,
world models, and VLA, across CVPR, ECCV, ICCV, ICML, and NeurIPS. The
document-level move detectors are stated explicitly in the study's method
field. Only aggregate counts and source IDs are retained.

The study is not used to claim that a phrase is statistically representative of
accepted papers. It supports three design decisions:

1. section templates are functional moves rather than fixed heading sequences;
2. result analysis must connect supported findings to comparisons, uncertainty,
   and boundaries, with full details recoverable from their manuscript locations;
3. protocol completeness and comparison fairness are explicit checks rather than
   inferred from fluent prose.

## Paragraph-level narrative calibration, 2026-10-09

[experimental_narrative_2026-10.json](../library/studies/experimental_narrative_2026-10.json)
adds twelve manually annotated passages from seven existing sources. Unlike the
80-paper document-level detector study, it examines paragraph ordering, numerical
roles, and the division of work between setup, displays, and analysis. Each
annotation carries a primary-PDF URL, checksum, locator, transferable structural
rule, and a boundary. This is one agent's purposive synthesis, not independent
expert review or a statistical survey of venue style. It adds no papers to the
300-paper coverage count.

The annotations distinguish recurring strategies: an aggregate result followed
by a diagnostic in [TD-MPC2](https://proceedings.iclr.cc/paper_files/paper/2024/file/cf73d57b6dcda32b293df7c2d5341f49-Paper-Conference.pdf),
a question followed by a changed reward condition in
[Decision Transformer](https://proceedings.neurips.cc/paper_files/paper/2021/file/7f489f642a0ddb10272b5c31057f0663-Paper.pdf),
and a favorable comparison qualified by harder-task degradation in
[VIMA](https://proceedings.mlr.press/v202/jiang23b/jiang23b.pdf).
These are structural observations, not quotations or claims that their source
interpretations are always scientifically justified.

The revision upgrades the existing `experiments` and `experiments.analysis`
protocols and adds two normalized usage records. It does not add a mandatory
study file to writing context. In a retained-display task, the display supplies
full coverage and the paragraph selects decisive evidence; standalone passages,
exact translations, and explicit all-value requests retain all required values.
No fixed numeric density, opening phrase, paragraph length, or five-sentence
template is imposed. Explanations are optional and evidence-bound.

Five new writing cases exercise four domain-specific comparisons and a
standalone-fidelity control. Their machine checks cover only observable facts;
manual review must judge selection, cohesion, omitted exceptions, and claim
scope. [EXPERIMENT_NARRATIVE.md](EXPERIMENT_NARRATIVE.md) contains an editorial
illustration and the proposed effectiveness protocol, not a measured win.
