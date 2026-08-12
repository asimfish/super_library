# Super Library card: rl.definition.explainable-rl.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### explainable reinforcement learning

`rl.definition.explainable-rl.001` · definition · reinforcement_learning · introduction, related_work, method, limitations, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Methods that expose evidence for a learned agent's decisions, for example attention masks, critical states, or feature attributions, so that humans can inspect what information drives behavior without changing the underlying policy class.

**Use:** State the explanation form and whether it is built into training or produced post hoc, what the explanation is evidence for (input relevance, decision points, or failure causes), and how explanation quality is evaluated beyond visual appeal.

**Avoid:** Do not present attention or saliency as proof of causal reasoning, and do not conflate explaining a black-box policy with learning an intrinsically interpretable policy structure.

**Patterns:**

- The framework produces {explanation form} highlighting {task-relevant information} behind the agent's decisions.
- We evaluate explanations by {quantitative protocol}, beyond qualitative inspection on {tasks}.

**Verify in primary sources:**

- `shi2021-self-supervised-discovering-interpretable` — [Self-Supervised Discovering of Interpretable Features for Reinforcement Learning](https://doi.org/10.1109/tpami.2020.3037898) (TPAMI 2021)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: introduction](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/introduction.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/translation.md)
- [topic: rl_theory_evaluation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/rl_theory_evaluation.md)
