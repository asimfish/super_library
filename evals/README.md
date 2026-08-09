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

The suite checks Related Work synthesis, rebuttal,
Chinese–English technical translation, an action-chunking method description,
real-robot setup, result analysis, Introduction alignment, and Abstract scope.
It also covers Limitations, Conclusion, efficiency captions, and VLA
generalization-table captions. Cases with `expected_guide_id` should load that
one protocol without loading the entire guide directory. The suite does not
measure venue-specific house style or certify scientific correctness.

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
