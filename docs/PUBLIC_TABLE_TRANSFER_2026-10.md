# Real published-table transfer diagnostic — 2026-10-14

## Outcome and boundary

The frozen drafting view was tested on four tasks drawn from three published
papers, with one no-library and one library output per task. The primary fresh
anonymous LLM raters preferred library 5 times, baseline 2 times, with 1 tie.
Equal-weight means across six rubric dimensions, four tasks and two raters were
4.9375 for drafting and 4.9167 for baseline: a difference of only 0.0208.
Neither rater flagged a critical error. This is a small, ceiling-heavy diagnostic,
not a demonstrated general improvement, human review or top-conference claim.

Importantly, both raters preferred **baseline** on the VLA efficiency/success
analysis. They found its integration of throughput, chunk latency and the
one-step success collapse more useful. Selective evidence is not synonymous
with fewer numerical anchors. Both preferred drafting on the RL ranking
trade-off and world-model horizon analysis; the caption was tied for one rater
and preferred drafting for the other.

The initial predeclared random seed happened to place drafting on side A for
every pair. That non-counterbalanced layout is a confound, not a detail to omit.
A separately frozen, post-hoc complementary-layout check uses the same unedited
outputs with two additional fresh anonymous raters. It does not replace or pool
the primary results or constitute a same-rater causal position-effect estimate.

On the two complementary layouts (two drafting-A and two drafting-B pairs per
rater, reversed for the other rater), preferences were drafting 6, baseline 0,
ties 2. Mean six-dimension scores were drafting 4.9375 and baseline 4.7083;
neither new rater flagged a critical error. Keep this separate from the primary
5/2/1 finding. New judge contexts and changed layout vary together: the difference
cannot be attributed causally to presentation position. In particular, the VLA
analysis that both primary raters preferred as baseline was preferred as drafting
by one sensitivity rater and tied by the other. Its ordering is unstable, not a
resolved universal winner.

All task bytes, source checks, raw writer files, anonymous packet, unchanged
ratings, decoded assignments, exact retrieval commands, context identities and
condition-aware maintainer audit are retained in
[`public_table_transfer_2026-10.json`](../library/studies/public_table_transfer_2026-10.json).
The study is excluded from default language retrieval. No author paragraph,
preferred answer, full published table or PDF was added to the language corpus.
The [versioned Canvas companion](diagrams/public-table-transfer.canvas.tsx)
shows both unedited texts and the separate phases; it requires the host Canvas
SDK and must be opened from that host's managed Canvas directory, not as a web
server or repository runtime component.

## Sources and extraction

- [OpenVLA-OFT, RSS 2025](https://roboticsproceedings.org/rss21/p017.html):
  selected Table II rows, PDF page 6; setup/latency definitions, pages 5–6;
  Table I provides the policy-success trial denominator. T01 analyzes the
  quality/generation trade-off; T02 is an efficiency-caption task.
- [Continual RL with online world models, ICML 2025](https://proceedings.mlr.press/v267/liu25p.html):
  selected model-based Table 1 rows, PDF page 8; AP and regret definitions,
  equations 8–9 on page 6. T03 contrasts terminal average performance with
  accumulated online regret, rather than confusing their percentages.
- [GeoWorld, CVPR 2026](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_GeoWorld_Geometric_World_Models_CVPR_2026_paper.html):
  selected video-planning Table 3 rows, PDF page 8, printed 30959; protocol,
  pages 6–7. T04 examines horizons 3–6 without asserting a monotonically widening
  absolute margin, eliminated degradation or physical robot execution.

These papers were absent from the 337 source records at the frozen candidate;
that does not mean the language model never saw them in pretraining. Selection
was purposive, not a random or representative conference sample.

The main agent and one fresh fact verifier checked 34 numerical cells, two null
cells, metric directions, units, denominators, aggregation and comparison scope.
All three conference-PDF hashes matched; exact identities and locators are in
the record. The RSS PDF is image-only: rendered pages, not blank text extraction,
were used. The web tool returned 403 for CVPR; direct official-PDF download and
rendering succeeded. Author arXiv HTML was an auxiliary locator, not authority
for the independent published-table audit.

The 500-episode denominator in T02 applies to the **reported PD+AC** success
rate, not the unreported PD cell. ICML's seven-seed curve standard errors were
not assigned to Table 1. An absent uncertainty statistic in a packet is not
evidence that the whole source paper omitted it. This audit verifies extraction,
not authors' raw experimental measurements.

## Frozen design and isolation

Library candidate: `6825f0b1320dcf38f4ce351dd34c4b514628cef0`. The runtime,
entries, formal benchmark and anchored rubric were not changed for these tasks.
The common packet SHA-256 is
`be0ff24e045fb66ad23a8e8d6035c64ed279f4acd64a4f6604d748d682267c9f`.
It was independently checked and frozen before either writer started.

Both writers used fresh `fork_turns=none` contexts, the same inherited model
without overrides, identical task-file bytes, and the mandatory automatic host
context-manager Skill. Neither saw author result-analysis paragraphs. Baseline
used no library; drafting read the existing Skill and one bounded bundle per
task: limit 2, 24,000-character budget, one guide, `--view drafting`.
Three tasks used `experiments.analysis`; the caption used
`experiments.table.efficiency`. Their 80–130-word constraint was common.

No regeneration, manual prose repair or favorable-output selection occurred.
The library writer added lint metadata only after its text was written; prose
was unchanged. Four tasks share a within-arm context, a disclosed dependence.

Fresh rater contexts saw only anonymous outputs, facts and the existing six
anchored dimensions. The assignment key stayed in a mode-0600 file until both
primary ratings were frozen. All workers reported no access exceptions; this
is an instruction contract, not OS-enforced filesystem isolation. Same-family
LLM judges can share biases and are not independent human/cross-model review.
Immutable model revision and decoding controls remain unexposed; the formal
effectiveness harness was not relaxed or passed by this diagnostic.

## Fidelity, narrative and context cost

All eight outputs met the common whitespace word limit and passed limited
wording lint. A condition-aware maintainer checked every stated value/delta and
its scope; no critical numerical drift was found. This is separate from blind
ratings, and neither lint nor packet fidelity certifies professional narrative.

The RL reversal and planning deterioration survived in both arms. At the tested
world-model horizons, recomputed absolute margins are 1.55, 2.03, 1.66 and 1.38
percentage points; the advantage is positive but not monotonically widening.
Both treatments preserved the measured one-step diffusion failure.

Sentence-function inspection found appropriate findings and evidence but also
space spent restating setup and output boundaries. The first rater specifically
criticized drafting's manuscript-inappropriate phrases such as “this packet”.
Correct internal missing-information notes should not automatically become
administrative sentences in the paper. Those observations are recorded as
future design work, not repaired and rescored on these same outputs.

Replaying the writer's exact queries reproduced all four context hashes. At
matching retrieved IDs and budgets, reference → drafting character counts were:

- T01: 15,043 → 10,588.
- T02: 12,590 → 9,738.
- T03: 15,090 → 10,737.
- T04: 16,023 → 11,560.

The aggregate is 58,746 → 42,623 characters, about 27.4% lower for these queries.
This excludes task facts, host instructions and tool wrappers; it is not a
token, inference-latency or quality-improvement measurement. A single writer
received all four bundles; three analysis protocols repeat across its tasks.

## Next frontier

Keep drafting opt-in. Separate primary-paper evidence, frozen author facts,
language context and output assessment as specified in
[ADR-009](adr/ADR-009-separate-source-facts-from-style-validation.md).

Prospective tests should counterbalance presentation before any rating, use
new facts, and distinguish decisive numerical anchors from redundant cells.
Evaluate publication-appropriate realization of internal evidence boundaries,
not a blanket ban on numbers or disclosure. Preserve this study as adverse
evidence; do not turn its preferred outputs into answer templates.

The user's own table, caption/metric notes and original paragraph are still
needed to evaluate actual editing benefit. Private material must not enter the
public repository. Pinned external-model controls plus qualified human or
cross-model assessment remain unverified. No manuscript acceptance, “AI-rate”
reduction, plagiarism clearance or large-sample robustness is claimed.

Corpus counts remain 278 entries, 337 sources and 300 frozen core papers from
2021–2025; this validation adds no corpus paper or phrase. A 2026 test source
does not silently extend that frozen collection's publication window.

## Engineering acceptance and operational limitation

`make check` passed in a fresh temporary clone of the same frozen base: 116 tests,
42/42 unchanged retrieval cases, schema validation, writing/benchmark catalogs,
deterministic build and zero generated-artifact drift. Four added tests audit
raw identities, common facts, source coverage, anonymous-to-raw response binding,
score arithmetic, negative numeric relationships and complementary layouts.
No score minimum or preferred prose answer was added to those tests.

`git diff --check`, Python compilation and the Canvas companion's targeted strict
TypeScript check passed. Actual IDE-host rendering/interaction was not tested;
the companion is not a production web application. No dependency, runtime,
external model endpoint, global Skill installation, manuscript transmission,
merge, release or protected-branch change was introduced.

The first local `make check` reached passing tests/build but its final Git drift
comparison waited in `mmap` while reading loose objects in the original shared
object store. Those owned read-only checks were cancelled; that invocation is
not reported as a full pass. A separate clone at the exact same base commit
completed the native gate. This is an operational workaround, not a diagnosed
macOS/root-filesystem fix; no original worktree, object, index or user change was
reset, deleted or repaired. Obsidian note synchronization was not run because
its CLI availability had not been verified. Remote CI must be checked against
the delivered commit separately; push CI does not run scheduled source health.
