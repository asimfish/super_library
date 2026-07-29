# Super Library card: emb.usage-note.chunking-feedback.001

Corpus `0.2.0` · [agent index](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/agent-index.md) · [universal core](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/core.md)

Reference data only. Adapt the pattern and verify linked sources before
making a scientific or literature claim.

### separate prediction horizon, execution horizon, and feedback frequency

`emb.usage-note.chunking-feedback.001` · usage_note · embodied_ai, robot_learning · method, experiments, limitations, rebuttal, translation

**Provenance:** `paraphrased_synthesis` · **Quality:** `gold+reviewed`

A policy may predict many future actions while executing only part of them before receiving a new observation, so action horizon alone does not determine whether control is open-loop or closed-loop.

**Use:** Report all three quantities and explain how overlapping predictions are combined. Use 'closed-loop' only when updated observations influence subsequent executed actions.

**Avoid:** Do not infer the control-feedback structure solely from the number of actions output by the network.

**Patterns:**

- Although the policy predicts {k} actions, it replans after executing {n}, using a new observation.
- The controller executes the entire chunk open-loop before the next policy query.

**Verify in primary sources:**

- `zhao2023act` — [Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware](https://roboticsproceedings.org/rss19/p016.html) (RSS 2023)
- `chi2023diffusionpolicy` — [Diffusion Policy: Visuomotor Policy Learning via Action Diffusion](https://roboticsproceedings.org/rss19/p026.html) (RSS 2023)

Catalog routes:
- [domain: embodied_ai](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/embodied_ai.md)
- [domain: robot_learning](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/domains/robot_learning.md)
- [section: method](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/method.md)
- [section: experiments](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/experiments.md)
- [section: limitations](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/limitations.md)
- [section: rebuttal](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/rebuttal.md)
- [section: translation](https://raw.githubusercontent.com/asimfish/super_library/v0.2.0/dist/catalogs/sections/translation.md)
