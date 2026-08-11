# Blind writing evaluation

These cases test behavior rather than prose similarity. Run each case in a fresh
Agent session with either:

1. the repository checkout;
2. only the pinned compact URL; or
3. the installed `super-library` skill.

Use the CLI to obtain a prompt packet from `writing.json`; it intentionally hides
the machine checks, manual rubric, expected guide, and expected record IDs:

```bash
python3 scripts/superlib.py eval-writing --list
python3 scripts/superlib.py eval-writing --case paper-experiment-real-robot-setup
```

Save the Agent output as a Markdown file, then score objective invariants:

```bash
python3 scripts/superlib.py eval-writing \
  --case paper-experiment-real-robot-setup \
  --response-file response.md --strict
```

For a complete run, store files as `<case-id>.md` and use
`eval-writing --responses <directory> --strict`. A machine pass is not an overall
pass. A human must apply every `manual_rubric` item and verify scientific claims,
citations, terminology consistency, source overlap, and translation fidelity.

The 20-case suite checks Related Work synthesis, evidence-bounded rebuttal,
Chinese–English technical translation, action-chunking and train/deployment
method boundaries, real-robot setup, result analysis, Introduction alignment,
and Abstract scope. It also covers mixed or null results, Limitations,
Conclusion, main-result, efficiency, and generalization captions, factorial
ablation interactions, and requests for experiments that were not run. Cases
with `expected_guide_id` should load that one protocol without loading the entire
guide directory. The suite does not measure venue-specific house style or
certify scientific correctness.

## Blind paired professionalism benchmark

`writing.json` tests one output against hard invariants. The paired benchmark in
`professionalism.json` tests whether the same pinned model writes better with the
library than without it, while also imposing an absolute professional-quality
bar. It deliberately uses no reference answers.

```bash
python3 scripts/superlib.py benchmark list
python3 scripts/superlib.py benchmark prompt paper-related-work-world-model
python3 scripts/superlib.py benchmark prepare \
  --suite full --responses path/to/responses \
  --run-manifest path/to/run.json \
  --blind-output path/to/blind.json \
  --key-output path/to/private-key.json
python3 scripts/superlib.py benchmark score \
  --blind-file path/to/blind.json \
  --key-file path/to/private-key.json \
  --ratings-file path/to/ratings.json --strict
```

The response root must contain `baseline/<case-id>.md` and
`super_library/<case-id>.md`. Keep the private key from raters until they finish.
At least two independent raters score scientific fidelity, terminology and
collocation, rhetorical function, evidence calibration, reporting completeness,
and clarity/conciseness on anchored 1–5 scales. They separately flag critical
scientific errors and choose A, B, or tie. The report includes absolute quality,
paired change, deterministic bootstrap uncertainty, pairwise preference, and
inter-rater agreement. See `skills/super-library/BENCHMARK.md` for the complete
protocol and interpretation limits.

## Deterministic retrieval evaluation

`retrieval.json` checks the part of the workflow that can be scored without a
language model: domain/topic/section/intent ranking, guide selection, and the
one-file task route. It includes English and Chinese queries for world models,
reinforcement learning, embodied AI, VLA, rebuttal, and translation.

Run it after any taxonomy, alias, entry, guide, or route change:

```bash
python3 scripts/superlib.py eval-retrieval
python3 scripts/superlib.py eval-retrieval --verbose
```

A case passes only when every declared expected entry appears within its own
`limit` and the expected guide and task route are selected. This is a routing
regression test, not a claim-correctness or prose-quality score.
