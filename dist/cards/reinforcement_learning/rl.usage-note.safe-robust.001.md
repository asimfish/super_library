# Super Library card: rl.usage-note.safe-robust.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### distinguish safety constraints from robustness to perturbations

`rl.usage-note.safe-robust.001` · usage_note · reinforcement_learning · related_work, experiments, limitations

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

Safety concerns satisfaction of specified cost or risk criteria, whereas robustness concerns stability of performance or constraint satisfaction under distributional or observational perturbations.

**Use:** Name the safety criterion, perturbation set or shift, and evaluate reward and violations separately.

**Avoid:** Do not infer safety from average-return robustness or robustness from nominal constraint satisfaction.

**Patterns:**

- We report nominal and perturbed return together with {violation metric} under {specified perturbation set}.

**Verify in primary sources:**

- `liu2023-robustness-safe-reinforcement-learning` — [On the Robustness of Safe Reinforcement Learning under Observational Perturbations](https://iclr.cc/virtual/2023/poster/11925) (ICLR 2023)
- `khattar2023-cmdp-within-online-framework` — [A CMDP-within-online framework for Meta-Safe Reinforcement Learning](https://iclr.cc/virtual/2023/poster/11412) (ICLR 2023)

Catalog routes:
- [domain: reinforcement_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/reinforcement_learning.md)
- [section: related_work](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/related_work.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [topic: safe_robust_rl](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/safe_robust_rl.md)
