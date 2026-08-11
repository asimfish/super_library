# Super Library card: wm.usage-note.multistep-consistency.001

Corpus `0.4.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### evaluate multi-step consistency separately from one-step prediction

`wm.usage-note.multistep-consistency.001` · usage_note · world_models · method, experiments, limitations

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

One-step loss measures local transition fit, whereas multi-step consistency tests whether iterated or direct predictions remain coherent over decision-relevant horizons.

**Use:** Report horizon-conditioned errors or task outcomes and distinguish teacher-forced, open-loop, and replanned predictions.

**Avoid:** Do not use a low one-step reconstruction loss as sufficient evidence of long-horizon planning fidelity.

**Patterns:**

- We evaluate one-step prediction under {protocol} and multi-step consistency over {horizons} under {rollout mode}.

**Verify in primary sources:**

- `lin2025-any-step-dynamics-model` — [Any-step Dynamics Model Improves Future Predictions for Online and Offline Reinforcement Learning](https://iclr.cc/virtual/2025/poster/30099) (ICLR 2025)
- `ma2024-do-transformer-world-models` — [Do Transformer World Models Give Better Policy Gradients?](https://proceedings.mlr.press/v235/ma24i.html) (ICML 2024)

Catalog routes:
- [domain: world_models](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/domains/world_models.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/sections/limitations.md)
- [topic: dynamics_representation](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/dynamics_representation.md)
- [topic: planning_imagination](https://raw.githubusercontent.com/asimfish/super_library/v0.4.0/dist/catalogs/topics/planning_imagination.md)
