# Super Library card: rl.term.action-gap.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### action gap

`rl.term.action-gap.001` · term · reinforcement_learning · related_work, method

**Provenance:** `terminology` · **Quality:** `gold+reviewed`

The difference between the value of a preferred action and that of an alternative action at a state, with the precise comparator determined by the formulation.

**Use:** Define which actions are compared, which value functional or return distribution is used, and whether time is discrete or continuous.

**Avoid:** Do not use action gap as a generic synonym for advantage without specifying the baseline action or policy.

**Patterns:**

- We define the action gap as {value of selected action} minus {value of comparator} under {value criterion}.

**Verify in primary sources:**

- `wiltzer2024-action-gaps-advantages-continuous` — [Action Gaps and Advantages in Continuous-Time Distributional Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/55769e1208c7f45e9acc98f06279c10c-Abstract-Conference.html) (NeurIPS 2024)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [topic: value_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/value_learning.md)
