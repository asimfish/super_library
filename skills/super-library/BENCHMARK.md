# Super Library effectiveness benchmark

## Status

The benchmark harness is reproducible and locally executable. No measured
effectiveness claim is made until a completed blind A/B run, its pinned run
manifest, independent ratings, and the generated report are reviewed together.

## Outcome contract

The benchmark asks two different questions:

1. Does the Super Library condition meet an absolute professional-writing bar?
2. With the model, decoding parameters, user prompt, and output budget held
   fixed, does access to the pinned Super Library improve the output over the
   no-library baseline?

The 20 source tasks remain in `evals/writing.json`. The separate
`evals/professionalism.json` defines the treatment conditions, suites, six
professionalism dimensions, five critical-error classes, provisional quality
gates, and deterministic bootstrap settings. Keeping these files separate
prevents the generation prompt from revealing the scoring contract.

## Experimental design

- Generate both conditions with the same pinned model revision, decoding
  parameters, seed policy, output budget, and condition-neutral user prompt.
- The baseline may not read Super Library artifacts. The treatment may use only
  the pinned repository or installed-skill revision recorded in the run manifest.
- Save responses as `baseline/<case-id>.md` and
  `super_library/<case-id>.md` under one run directory.
- Randomize both pair order and A/B side assignment. The blind bundle carries the
  scoring anchors but no condition mapping. Keep the generated key away from
  raters until all ratings are frozen. The CLI writes the key with owner-only
  permissions (`0600`) and refuses symbolic-link output targets.
- Use at least two independent raters with current AI/ML paper-writing or review
  experience. Raters score A and B separately before recording pairwise
  preference.
- Do not tell raters which system, retrieval path, or condition produced either
  response.

The `smoke` suite tests the harness only. Use `core` for a lower-cost balanced
manual run, `experiments` for the reporting stress slice, and `full` for an
effectiveness claim.

## Rubric

Each response receives an integer 1–5 score for:

1. scientific fidelity;
2. terminology and collocation;
3. section-specific rhetorical function;
4. evidence calibration;
5. reporting completeness; and
6. clarity and concision.

Use the 1/3/5 anchors in `evals/professionalism.json`; use 2 or 4 only when the
response lies genuinely between adjacent anchors. Separately flag any fabricated
evidence or citation, number/negation/modality drift, unsupported
scope/causality/ranking, comparison/protocol misreporting, or source-copying
misrepresentation. A critical error cannot be compensated by polished style.

## Reproduction

Run these commands from a full repository checkout. The lightweight standalone
skill intentionally bundles only selective lookup assets, not the maintainer
benchmark harness or response files.

Inspect the benchmark and emit condition-neutral prompts:

```bash
python3 scripts/superlib.py benchmark list
python3 scripts/superlib.py benchmark prompt rebuttal-existing-evidence
```

Copy `evals/professionalism-run.example.json`, replace every example field,
record SHA-256 hashes of the actual system prompts, and use the full 40-character
commit SHA of the evaluated library. The CLI rejects the example placeholders.
Then create the blind bundle:

```bash
python3 scripts/superlib.py benchmark prepare \
  --suite full \
  --responses path/to/responses \
  --run-manifest path/to/run.json \
  --blind-output path/to/blind.json \
  --key-output path/to/private-key.json
```

Ratings use this shape for every pair and rater; `scores` must contain exactly
the six dimension IDs, and `critical_errors` may contain only declared IDs:

```json
{
  "schema_version": "1.0",
  "benchmark_id": "super-library-professionalism-v1",
  "raters": [
    {"id": "rater-01", "qualification": "AI/ML paper author and reviewer", "independent": true},
    {"id": "rater-02", "qualification": "AI/ML paper author and reviewer", "independent": true}
  ],
  "ratings": [
    {
      "pair_id": "pair-001-xxxxxxxx",
      "rater_id": "rater-01",
      "a": {"scores": {"scientific_fidelity": 4, "terminology_and_collocation": 4, "rhetorical_function": 4, "evidence_calibration": 4, "reporting_completeness": 4, "clarity_and_concision": 4}, "critical_errors": []},
      "b": {"scores": {"scientific_fidelity": 3, "terminology_and_collocation": 3, "rhetorical_function": 3, "evidence_calibration": 3, "reporting_completeness": 3, "clarity_and_concision": 3}, "critical_errors": []},
      "preference": "a",
      "rationale": "A is more precise and preserves the evidence boundary."
    }
  ]
}
```

Score only after ratings are complete:

```bash
python3 scripts/superlib.py benchmark score \
  --blind-file path/to/blind.json \
  --key-file path/to/private-key.json \
  --ratings-file path/to/ratings.json \
  --strict
```

The report includes deterministic invariant pass rates, six dimension means,
critical-error rates, paired mean change, a paired-case bootstrap interval,
blind preference, rater agreement, and each release gate.

## Interpretation limits

- Regex checks observe declared invariants, not semantic equivalence or truth.
- Human ratings are subjective; report rater qualifications and agreement.
- The bootstrap interval describes the sampled cases, not all papers or venues.
- One run does not establish robustness across models or decoding regimes.
- Prompts are synthetic but evidence-bounded; a separate future study is needed
  for author-owned full manuscripts and external reviewer outcomes.
- Do not tune corpus records directly against hidden case wording. Add or revise
  records only when primary-paper evidence and general writing value justify it.
