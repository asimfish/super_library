# Blind Agent diagnostic and design revision — 2026-10-13

## Outcome, not certification

The compact drafting view is implemented as an opt-in. Default reference
behavior is unchanged. Eight synthetic tasks were generated and anonymously
reviewed in two stages. Four discovery tasks did **not** show consistent
library benefit; four verification tasks provide a limited reason to keep the
compact view available. This is not a top-conference acceptance claim, a human
evaluation, or a replacement for the pinned formal effectiveness benchmark.

Full task packets, all 20 drafts, unchanged score values and rationales, decoded
assignments, exact retrieval commands, bundle sizes and identities are in
[`agent_pilot_2026-10.json`](../library/studies/agent_pilot_2026-10.json).
This maintainer study is excluded from default writing retrieval.

## Design and isolation

The user explicitly authorized blind testing. All writers and raters used fresh
`fork_turns=none` contexts and the same inherited model without overrides.
Each writer saw one condition and four tasks; each rater saw only anonymous
texts, common task packets and the existing six anchored dimensions.
Mappings remained in owner-only files until both ratings were frozen.

Discovery used the frozen `1c2f4a80823a9b65ea663854f84243ae96bff5ce` library:
VLA deployment trade-off, world-model prediction/control mismatch, introduction
bridge and missing experimental protocol. Independent LLM ratings were frozen
before any code change.

The six projection tests first failed on missing CLI support/mirrors, then passed.
The candidate was frozen at `b386b41ddebace383cc776f30c9ffbd27d7f44e9`.
Verification used four disjoint tasks: standalone analysis, efficiency caption,
mixed/null Abstract results, and translation with numeric/negation fidelity.
The three arms were no library, candidate reference, and candidate drafting.
Reference/drafting use the same code/data revision and retrieval parameters
apart from `--view`. Four saved old reference bundles were byte-identical to the
candidate reference output. Both paper-evaluation files were left unchanged.

Initial manual dispatches were cancelled before output inspection because their
repeated task wording was not identical. Fresh replacements read the same
frozen task file. Those cancelled outputs were excluded for setup integrity,
not quality selection. The third verification arm was added before any
verification generation, not after seeing its outcomes.

## Findings

Discovery, across eight rater decisions: library 2 wins, control 3 wins, 3 ties.
Equal-weight means across six dimensions, four tasks and two raters were
4.7708 for library and 4.7917 for control. Both raters identified redundant
closing conclusions in result analysis. One identified an ambiguous attachment
of aggregate latency to a seen-object subset. The same drafts passed the wording
lint and declared machine checks: those passes did not diagnose narrative quality.

The runtime prompt also contained multiple template menus, source metadata and
teaching contrasts. These observations motivate
[ADR-008](adr/ADR-008-reference-versus-drafting-context.md); they do **not** prove
that those prompt components caused the prose defects.

On the four verification tasks, both raters preferred drafting for the Abstract;
the other three tasks tied drafting with reference. Means were control 4.8125,
reference 4.9375 and drafting 5.0000. No critical error was flagged in these
ratings. All 20 drafts passed the unchanged declared machine checks.
These ceiling-heavy, subjective LLM scores on four cases do not establish
statistical efficacy or cross-model robustness. Do not compare discovery and
verification means as a before/after improvement: their task sets differ.

Actual verification bundle sizes, reference → drafting, in characters:

- Standalone analysis: 17,118 → 11,575.
- Efficiency caption: 17,533 → 13,755.
- Abstract: 19,591 → 14,952.
- Translation: 18,377 → 13,919.

The record IDs match between views on these tasks; the original 24,000-character
gate is unchanged. Counts exclude user facts, host instructions and tool wrappers.
Tool-reported token estimates are not treated as model input token counts.

## Limitations and next frontier

- Provider immutable model revision, temperature, top-p, generation seed and
  output-token limit are not exposed. A random seed governs blinding only.
- Instruction isolation was enforced through task contracts, not filesystem
  sandboxing. Shared host instructions and available tools remain possible
  influences; the orchestrator inspected writer boundary reports.
- One reference verification writer additionally read the mandatory automatic
  context-manager Skill and taxonomy/topics. This access/context difference is
  disclosed rather than hidden or regenerated away.
- Two independent rater **contexts** per stage are same-family LLM judges,
  not credentialed humans or cross-model raters. Agreement may reflect shared
  biases. Four tasks per writer share a within-arm context.
- Verification tasks were excluded from this iteration's design editing, but
  they are existing synthetic repository cases, not a novel external dataset.
- No repeated generations, user-owned full manuscripts, source-overlap detector,
  venue-specific acceptance or actual reviewer outcomes were evaluated.

Keep drafting optional. The formal benchmark still rejects unexposed controls
outside its harness smoke suite; no gate, case or rubric was relaxed to publish
this pilot. Prior negative Qwen evaluations remain historical evidence.

The next useful test is a pinned external model and human/cross-model review of
retained-table analysis, including whether each sentence adds a comparison,
explanation or material boundary. Also test return/latency/statistical units under
ambiguous source notes. Do not tune against the eight frozen pilot texts or
turn them into preferred answers in the language corpus.

Engineering handoff remains conditional on real-world writing efficacy, not on
the subjective perfect scores here. This iteration adds no papers or synonyms:
278 records, 337 sources, 300 frozen core papers and 14 enriched profiles remain.

## Engineering acceptance

`make check` passed 112 tests and 42/42 unchanged retrieval cases, with no
generated drift. Six new tests cover projections, complete-reference compatibility,
matching IDs, selected overlays, preservation and budget failures; two audit tests
verify response identity, rating coverage, arithmetic and adverse-result retention.
Python compilation, `git diff --check` and targeted Canvas strict TypeScript
passed. The versioned SVG was rendered in a complete 1800×1120 WebKit viewport
and inspected; actual IDE-host Canvas interaction was not automatically tested.

Capability/provenance records were updated for the same skill owner. The native
governance contracts passed, but no global Forge registry audit/installation or
new model activation-recognition evaluation is claimed. No credentials, new
dependencies, services, private manuscript uploads or publication/submission
capabilities were added. The raw synthetic diagnostic is maintainer-only evidence,
not a default prompt resource. Remote CI must be checked against the delivered
commit separately; scheduled source-health checks are not implied by push CI.
