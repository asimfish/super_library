# ADR-008: Separate complete reference records from drafting context

## Status and evidence

Accepted for an opt-in, reversible implementation, 2026-10-13. Base:
`1c2f4a80823a9b65ea663854f84243ae96bff5ce`. Four discovery tasks, fresh
instruction-isolated writers and two fresh anonymous LLM raters yielded two
library preferences, three control preferences and three ties. No universal
writing benefit was established. Both raters observed repeated conclusions;
one observed an ambiguous aggregate-latency attachment. Context inspection
also found teaching contrasts, multiple templates and source metadata occupying
the runtime budget. These are correlated observations, not a proved causal link.

## Requirements and candidates

Keep one canonical owner for each rule, term and guide; preserve evidence
checks, provenance type, source navigation, filters and serialized budgets.
Do not alter historical writing tasks, rubrics or explicit-control requirements.

A: Shorten canonical guides and records globally. Fewer bytes, but inspection,
teaching and definition evidence lose their detail; hard to reverse selectively.

B: Explicit reference/drafting views derived from the same records. Reference
is the unchanged default. Drafting omits index metadata, extra template menus,
negative teaching contrasts and repeated example alternatives. It preserves
all selected guide inputs, moves/checks, verification and avoid constraints;
only matching domain overlays are included. Scientific evidence still lives
in primary sources. The view is identified as a projection, not a complete card.

Choose B. Adding an embedding service or another authoritative phrase book is
not justified by these failures.

## Interface and ownership

`scripts/writing_context.py` exposes pure
`project_entry(entry)`, `project_source(source)`,
`project_guide(guide, domains)` and Markdown renderers for those projections.
No I/O, facts inference, model call, new dependency, learned weights or cache.
The portable skill receives the same module; only presentation changes, not
retrieval scoring. `bundle --view drafting` and
`lookup.py --view drafting` explicitly request the projection.
`show`, `guide`, generated complete cards and reference views remain unchanged.
Table assets still use the existing one-template workflow.

The drafting preamble states that avoid notes constrain the draft rather than
require a defensive sentence, and that each sentence should advance the supplied
argument. It never authorizes removal of required standalone values, material
adverse findings, missing-evidence disclosures or task-requested quantities.

## Verification and reconsideration

Tests prove no canonical mutation, exact check/avoid preservation, overlay
selection, root/portable parity, complete default compatibility and hard-budget
failure semantics. Measure size on matched record IDs; do not infer token count
from characters or conflate more admitted records with less per-record overhead.

Freeze the candidate before four verification tasks. Add an immutable old
reference arm alongside the no-library and candidate drafting arms; fresh
writers and raters see no discovery texts. Model revision and decoding controls
remain unexposed: this is a diagnostic LLM study, not a formal release gate or
independent human review. Keep all adverse cases. Do not set a new default solely
from this pilot; revisit on preservation failures or later pinned cross-model
and human evidence.

Execution clarification, 2026-10-14: the recorded verification used reference
and drafting from the same frozen candidate `b386b41`, not different runtime
commits. Four saved old reference bundles matched the candidate reference output
byte-for-byte. The diagnostic report records this implementation of the original
three-arm plan; the default reference contract remained unchanged.
