# Fresh-agent smoke evaluation

These cases test behavior rather than prose similarity. Run each case in a fresh
Agent session with either:

1. the repository checkout;
2. only the pinned compact URL; or
3. the installed `super-library` skill.

Give the Agent the `request` and `facts` from `smoke.json`. A pass must satisfy
every invariant and should report which corpus entry IDs it retrieved. Reviewers
should compare meaning and evidence boundaries, not reward exact template copying.

The suite is intentionally small. It checks the three initial workflows:
Related Work synthesis, rebuttal, and Chinese–English technical translation.
It does not measure venue-specific style or scientific correctness of new claims.
