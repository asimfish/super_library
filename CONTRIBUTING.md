# Contributing

Add records to the appropriate JSONL file and run `make check`.

`library/` is canonical. Everything under `dist/` and the generated skill
snapshots is rebuilt; never edit those artifacts directly.

Section protocols live in `library/writing_guides.json`; full-paper calibration
metadata lives in `library/studies/`. Do not add extracted paper prose to either.

## Acceptance checklist

- The expression is genuinely useful for AI research writing, not merely ornate.
- The record has one clear communicative function and uses controlled taxonomy.
- Definitions are independently paraphrased and cite at least one primary source.
- Examples are newly written templates, use meaningful `{placeholders}`, and do
  not smuggle in an unverified empirical claim.
- `avoid` explains a concrete misuse, ambiguity, or overclaim.
- Source title, venue, year, and stable URL were checked on a primary page.
- The entry contains no copied abstract, paragraph, table, or result.
- The contributor has the right to submit every original field under CC0 1.0.
- Record text contains no HTML, hidden instructions, or directives aimed at an
  Agent. Corpus fields are reference data, not executable prompts.
- Gold records have been reviewed for both language and technical meaning.
- The expression is not a normalized duplicate of an existing card. Prefer adding
  another source or topic mapping to creating a synonymous record.

## Adding a source

Use a stable primary URL: proceedings page, DOI landing page, OpenReview forum,
PMLR/CVF page, IEEE/journal page, or author-controlled arXiv abstract page.
Do not use a search-result, blog, or citation-aggregator URL.

Source IDs use `<first-author><year><short-title>` in lowercase ASCII. Venue names
must match `library/taxonomy.json`.

For a collection paper, also assign controlled `domains`, `topic_families`, and
`collections`. Collection boundaries in `library/collections.json` are validated;
do not add a workshop, preprint, out-of-window year, or off-topic title merely to
raise a count.

## Adding an entry

IDs use `<domain>.<kind>.<slug>.<nnn>`. Keep one JSON object per physical line.
Run:

```bash
python3 scripts/superlib.py validate
python3 scripts/superlib.py search "<new concept>"
python3 scripts/superlib.py route "<new concept>" --domain <domain>
python3 scripts/superlib.py build
python3 -m unittest discover -s tests -v
```

Pull requests should explain what writing situation the new record improves and
which primary sources were checked. A maintainer must inspect generated Markdown
before merging; automated validation is not a substitute for language, evidence,
rights, or prompt-injection review.

Add an ID to `library/core_ids.json` only if the record is broadly necessary
across paper, rebuttal, and translation tasks. The universal core is capped at 24
records. Most new content should remain discoverable through catalogs and cards.

## Updating a writing guide

- Keep protocols functional rather than venue-stereotyped: required inputs,
  reporting moves, conditional template variants, verification, and avoid rules.
- Prefer one specialized guide over expanding the universal core.
- Link only reviewed entry IDs and reject wording duplicated in the guide and
  every related card.
- Document external skills or official venue rules in
  `docs/WRITING_GUIDE_RESEARCH.md`; independently rewrite every adopted idea.
- Preserve the context budgets: guide index below 5 KB, each guide below 12 KB,
  and exactly one recommended guide per route.
