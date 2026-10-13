# Drafting view: compact language context without a second corpus

Use `--view drafting` only when composing or revising the current artifact:

```bash
python3 scripts/superlib.py bundle \
  --rhetoric-query "finding led experimental narrative" \
  --technical-query "model query latency" \
  --domain vision_language_action --section experiments \
  --guide experiments.analysis --limit 1 --max-chars 24000 --view drafting
```

The default `--view reference` remains complete. Inspect a known record with
`show`, or one protocol with `guide`, when teaching examples or a complete
source record are needed. Do not load both views for ordinary drafting.

Standalone consumers can run:

```bash
python3 skills/super-library/scripts/lookup.py "model query latency" \
  --domain vision_language_action --limit 1 --view drafting
```

Selection/ranking is unchanged. Projection follows selection, and the complete
serialized bundle determines budget admission. More records may therefore fit
with the same limit; this is not a guarantee that every query uses fewer tokens.
Portable lookup is bounded by record count, as before; it does not implement
the repository bundle's hard `--max-chars` gate.

The projected term retains meaning, guidance, avoid notes, source IDs, provenance
type, one optional structural example, attestations when present, and contextual
sense/collocations/confusables/rule references. It omits classification/index
metadata, detailed provenance notes, extra examples and teaching contrasts.
Source navigation retains ID, title, venue, year and URL, not author lists.

The projected protocol retains its purpose, all inputs, moves and checks,
verification, avoid notes, and matching domain overlay. It omits aliases,
navigation links and alternative template menus. Table assets are still selected
through `template`; no table skeleton is removed or silently substituted.
With no domain specified, all overlays remain available rather than guessing.

JSON bundles label `context_view: drafting` and `projection_notice`.
They are intentionally not complete canonical records; consumers requiring
full-card schemas must use reference. No records or generation facts are learned
from the projection itself. No new dependency, service or credential is required.

At fixed limit 1, the same two VLA-analysis records measured 15,337 → 10,808
characters in Markdown and 22,664 → 13,276 in JSON. Those sizes include the
protocol, compact rules and final newline, but not the user's task or host
instructions. They are character measurements, not tokenizer counts or latency
benchmarks. The existing 24,000-character gate was not enlarged.

The opt-in remains reversible. Generated cards and one-file routes stay complete
reference artifacts; the old pinned release does not acquire new code until
explicitly released. See [ADR-008](adr/ADR-008-reference-versus-drafting-context.md).
