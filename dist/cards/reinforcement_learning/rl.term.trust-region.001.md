# Super Library card: rl.term.trust-region.001

Corpus `0.3.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### trust-region policy update

`rl.term.trust-region.001` · term · reinforcement_learning · related_work, method, translation

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

A policy update constrained to keep the new policy sufficiently close to the old policy, commonly measured by KL divergence, to improve optimization stability.

**Use:** Specify whether the constraint is hard, approximate, or implemented through a penalty or clipped surrogate. Do not transfer theoretical guarantees across variants.

**Avoid:** Do not claim monotonic improvement for a practical approximation unless its assumptions and guarantee apply.

**Patterns:**

- The policy update is restricted by a KL-divergence constraint between {old and new policies}.
- A trust region limits the step size in policy space.

**Verify in primary sources:**

- `schulman2015trpo` — [Trust Region Policy Optimization](https://proceedings.mlr.press/v37/schulman15.html) (ICML 2015)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/method.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/sections/translation.md)
- [topic: policy_optimization](https://raw.githubusercontent.com/asimfish/super_library/v0.3.0/dist/catalogs/topics/policy_optimization.md)
