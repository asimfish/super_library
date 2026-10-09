# Experiment narrative revision: scope and evidence

The 2026-10-09 revision addresses result prose that reads like a numerical
laundry list. It changes the existing experiment guides and two normalized
records, not the corpus architecture or paper-coverage target. A paragraph-level
calibration study records twelve passages from seven existing published sources.
The study is maintainer evidence, not additional default Agent context.

## What changes at writing time

The Agent identifies an empirical point before drafting and privately maps its
evidence to manuscript locations. Setup defines shared evaluation protocols;
captions explain displays; tables retain complete measurements; analysis selects
comparisons and explains their consequence for the research question. This is
conditional on the display actually remaining available. A standalone passage,
exact translation, or explicit all-value request must preserve all required
measurements and qualifiers in the prose.

The analysis guide supplies choices rather than a sentence-by-sentence form:
main comparison, ablation, regime-dependent/null result, outcome-to-diagnostic
chain, or failure analysis. Explanations are optional. A hedged mechanism still
needs supplied support; it cannot be generated to complete a narrative. No
universal paragraph length, numeric quota, or prohibition on quantitative prose
is introduced. Material reversals, null results, resource differences, and
uncertainty remain part of the argument.

Retrieve just one relevant protocol and a few records:

```bash
python3 scripts/superlib.py bundle \
  --rhetoric-query "experimental narrative table to prose selective evidence" \
  --technical-query "task success rate" \
  --domain embodied_ai --section experiments --intent evidence \
  --guide experiments.analysis --limit 4 --max-chars 24000
```

The complete experiment protocol contains a compact evidence-allocation rule,
so existing one-file experiment routes also carry the behavior. They do not
load the full analysis guide or the study. Explicit analysis queries select the
analysis guide; explicit caption requests select the appropriate table guide.

Integration testing exposed a JSON budget defect: a 24,000-character request
emitted 37,769 characters because selection counted Markdown instead. The
revision now measures the selected serialized format, preserves complete
records/protocols, and rejects an oversized protocol. Retrieval considers the
two passes in alternating rank order rather than letting rhetoric fill the
budget before technical records. These are measured context behaviors, not
prose-effectiveness evidence.

## Editorial illustration, not an A/B result

The following data and prose are synthetic editorial fixtures, not measurements
from any cited paper. Both prose versions were authored during this revision,
not generated in a blind comparison. This public fixture differs from the
benchmark packets and is not a reference answer for any case. Neither version
is a no-library model baseline or a benchmark output.

Assume the following table and caption remain unchanged in the manuscript:

| Condition | Baseline successes | Proposed successes |
|---|---:|---:|
| Unobstructed corridor | 34/40 | 34/40 |
| Narrow doorway | 24/40 | 32/40 |
| Cluttered scene | 18/40 | 26/40 |
| Low lighting | 28/40 | 24/40 |

Table 7. Successful navigation trials out of 40 independent trials per condition,
evaluated in the same simulator under matched training data and model-selection
protocols. Higher success is better. Conditions are equally weighted: aggregate
success is 65% for the baseline and 72.5% for the proposed policy. No uncertainty estimate or
significance test was computed.

A row-led report might read:

> Table 7 shows that baseline and proposed success are both 85% in unobstructed
> corridors, 60% and 80% at narrow doorways, 45% and 65% in cluttered scenes,
> and 70% and 60% in low lighting, with average success increasing from 65% to
> 72.5% under matched training data and model selection in the same simulator.

An original finding-led version is:

> The higher aggregate navigation success reflects gains at narrow doorways and
> in cluttered scenes (Table 7), where success rises by 20 percentage points in
> each condition. Unobstructed corridors are unchanged, while success in low
> lighting falls by 10 percentage points. The benefit therefore depends on the
> evaluated scene condition, rather than extending uniformly across conditions.

The second version selects numbers with different roles: the gain anchors the
finding, the reversal qualifies its scope, and redundant endpoints remain in
the unchanged table. It makes no causal claim about sensing or representations.
Whether readers prefer it, and whether an Agent reliably produces it, require
separate evaluation. This example does not establish either result.

The same allocation principle does not collapse distinct evidence types. For
world models, prediction comparisons and downstream control comparisons still
answer different questions. A paragraph may connect those questions, but cannot
transfer a prediction result into an unsupported planning claim or infer
equivalence from reported dispersion.

## Effectiveness evaluation still required

The existing paired harness has a `narrative` slice with five condition-neutral
tasks covering robot outcomes, world-model horizon/control mismatch, RL scaling
costs, VLA speed/generalization, and standalone fidelity. The full suite now has
47 cases, including the four upstream fabrication traps; previous runs must be
interpreted under their pinned case lists rather than re-scored on this revision.
Machine checks observe selected invariants, not scientific semantics or prose
quality. No old check or quality threshold is relaxed by this revision.

Before making an effectiveness claim:

1. Freeze the corpus commit, both evaluation JSON files, generator revision,
   prompt pipeline, decoding controls, and output budget. Keep baseline and
   library arms isolated; do not expose tests or these illustrations to writers.
2. Generate fresh paired outputs with identical condition-neutral tasks. For a
   repair-specific old-versus-new comparison, use the same current case set and
   change only the pinned library revision; historical scores are not its control.
3. Have at least two independent raters score the six existing dimensions in
   blind order. Check finding selection, sentence-to-sentence continuity,
   useful numerical anchors, and preservation of adverse outcomes. Do not score
   numeric count as quality or confuse legitimate display references with missing
   standalone facts. Disclose whether raters are humans or language models.
4. Report paired uncertainty, preference, critical errors, and absolute quality.
   Inspect the standalone control and old tasks for regressions. A five-case
   pilot cannot establish venue-wide or model-wide improvement.
5. Add a separately frozen author-owned manuscript set with retained tables and
   actual task boundaries before claiming benefits for real research writing.

No fresh paired generation or independent human rating is included in this
revision. The measurable delivered claims are source traceability, bounded
retrieval, routing behavior, and preserved regression contracts. Professional
writing improvement remains an effectiveness hypothesis, not a completed result.

## Verification scope

The integration branch is `feat/experimental-narrative-evidence`, based on
`5a5c55c0e553fc11c6b2886a5fa1a3f6094108a7` (the upstream fabrication repairs).
The original worktree's pending changes were not folded into this branch.
Its four fabrication traps and aggregate/subset scope guard are retained.

| Criterion | Evidence and boundary |
|---|---|
| Canonical data | `validate`: 276 entries, 336 sources; paragraph-study schema and source/card/guide references are checked in the new tests |
| Retrieval | `eval-retrieval`: 42/42; English and Chinese prose requests, specialized captions, and full-section requests retain separate routes |
| Regression | 84 native tests pass on the integration tree, including ten new narrative/budget contracts |
| Context | Analysis guide 10,161 bytes; complete experiment guide 11,927 bytes; four experiment routes remain below 18,000 bytes; both output formats are character-bounded |
| Budget rejection | A 2,000-character guide-only JSON request exits 2 with empty stdout, instead of emitting a partial protocol |
| Generated artifacts | Native determinism, manifest, mirror, guide/route count, and budget tests pass |
| Static/data safety | `py_compile` and `git diff --check` pass; corpus markup guard tests pass; no new endpoint, dependency, credential use, global skill install, or redistributed paper text |
| Draft check | The distinct synthetic navigation illustration passes the limited wording audit; its numbers and scope were checked editorially, not independently |
| Effectiveness | Not evaluated in a fresh paired generation run; no new independent human rating, real-manuscript result, or venue-wide benefit claim |

Reproduce the local technical gate with `make check` on this branch. Remote CI
must be checked against its actual delivery commit, not inferred from these
local results. No merge, release tag, or replacement of the old pinned `v0.4.0`
link is performed by this revision; use a checkout of the feature branch to
exercise the new CLI and skill behavior.
