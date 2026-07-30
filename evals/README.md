# Fresh-agent smoke evaluation

These cases test behavior rather than prose similarity. Run each case in a fresh
Agent session with either:

1. the repository checkout;
2. only the pinned compact URL; or
3. the installed `super-library` skill.

Give the Agent the `request` and `facts` from `smoke.json`. A pass must satisfy
every invariant and should report which corpus entry IDs it retrieved. Reviewers
should compare meaning and evidence boundaries, not reward exact template copying.

The suite is intentionally small. It checks Related Work synthesis, rebuttal,
Chinese–English technical translation, an action-chunking method description,
real-robot setup, result analysis, Introduction alignment, and Abstract scope.
Cases with `expected_guide_id` must load that one protocol without loading the
entire guide directory. The suite does not measure venue-specific style or
scientific correctness of new claims.
